"""Generate and commit a report in this repository; never clone a second repository."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def report_complete(directory: Path, day: str, weekly: bool, slot: str) -> bool:
    if not all((directory / f'{day}.{ext}').is_file() for ext in ('html', 'md')):
        return False
    if weekly:
        return True
    try:
        data = json.loads((directory / f'{day}.snapshots.json').read_text())
        return data.get('report_date') == day and (not slot or any(
            item.get('slot') == slot for item in data.get('snapshots', [])))
    except (OSError, ValueError, AttributeError, TypeError):
        return False


def validate_report(directory: Path, day: str, weekly: bool) -> None:
    if not report_complete(directory, day, weekly, ''):
        raise RuntimeError('Generated report is incomplete; refusing to publish.')
    for ext in ('html', 'md'):
        if not (directory / f'{day}.{ext}').read_text().strip():
            raise RuntimeError('Generated report is empty; refusing to publish.')
    if not weekly:
        markdown = (directory / f'{day}.md').read_text()
        failures = ('Network readiness: unavailable', 'Failed to resolve', 'NameResolutionError',
                    'Market movers source unavailable', 'No news items returned')
        if any(message in markdown for message in failures):
            raise RuntimeError('Core report source unavailable; refusing to publish.')


@contextmanager
def publication_lock():
    lock = Path(git('rev-parse', '--git-common-dir'))
    if not lock.is_absolute():
        lock = ROOT / lock
    lock = lock / 'finance-publication.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        raise RuntimeError(f'Another publisher holds {lock}. If a run crashed, verify it stopped before removing this directory.')
    try:
        yield
    finally:
        lock.rmdir()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--weekly', action='store_true')
    parser.add_argument('--date', default=os.getenv('REPORT_DATE'))
    parser.add_argument('--force', action='store_true', default=os.getenv('REPORT_FORCE_GENERATE') == 'true')
    parser.add_argument('--dry-run', action='store_true', default=os.getenv('REPORT_DRY_RUN') == 'true')
    args = parser.parse_args()
    now = datetime.now(ZoneInfo(os.getenv('REPORT_TIMEZONE', 'America/Los_Angeles')))
    hours = os.getenv('REPORT_ALLOWED_HOURS', '')
    if hours:
        start, end = map(int, hours.split('-'))
        if not start <= now.hour <= end:
            print('Outside configured publication hours; skipping.')
            return
    day = args.date or now.date().isoformat()
    datetime.strptime(day, '%Y-%m-%d')
    folder = 'weekly-finance' if args.weekly else 'daily-finance'
    slot = os.getenv('REPORT_SNAPSHOT_SLOT', '')
    destination = ROOT / folder
    with publication_lock():
        if not args.dry_run:
            if git('branch', '--show-current') != 'main':
                raise RuntimeError('Publishing requires the main branch.')
            if git('status', '--porcelain', '--untracked-files=normal'):
                raise RuntimeError('Working tree must be clean before publishing.')
            git('fetch', 'origin', 'main')
            if git('rev-list', '--count', 'origin/main..HEAD') != '0':
                raise RuntimeError('Local commits are not published automatically; sync main first.')
            git('merge', '--ff-only', 'origin/main')
        if not args.force and report_complete(destination, day, args.weekly, slot):
            print(f'{folder}/{day} already contains the requested report/snapshot; skipping generation.')
            return
        # Stage generation separately: a failed fetch never overwrites a published report.
        with tempfile.TemporaryDirectory(prefix='baybell-report-') as temp:
            staging = Path(temp)
            snapshot = destination / f'{day}.snapshots.json'
            if not args.weekly and snapshot.exists():
                shutil.copy2(snapshot, staging / snapshot.name)
            command = [sys.executable, '-m', 'finance_daily_report', '--date', day,
                       '--output-dir', str(staging)]
            if args.weekly:
                command.append('--weekly')
            subprocess.run(command, cwd=ROOT, check=True)
            validate_report(staging, day, args.weekly)
            if args.dry_run:
                print('Dry run passed; no archive, commit, email or deployment changes.')
                return
            extensions = ('html', 'md') if args.weekly else ('html', 'md', 'snapshots.json')
            paths = []
            for extension in extensions:
                name = f'{day}.{extension}'
                shutil.copy2(staging / name, destination / name)
                paths.append(f'{folder}/{name}')
            git('add', '--', *paths)
            if not git('diff', '--cached', '--name-only'):
                print('No report changes to commit.')
                return
            git('commit', '-m', f'Update {folder} report for {day}' + (f' ({slot})' if slot else ''))
            for attempt in range(3):
                pushed = subprocess.run(['git', 'push', 'origin', 'HEAD:main'], cwd=ROOT)
                if pushed.returncode == 0:
                    # Send only after publication, never during retries or dry runs.
                    if not args.weekly:
                        sys.path.insert(0, str(ROOT))
                        from finance_daily_report.config import Settings, load_dotenv
                        from finance_daily_report.emailer import send_email
                        load_dotenv(ROOT / '.env')
                        settings = Settings.from_env()
                        if settings.email_configured:
                            send_email(settings, f'Finance Daily Report - {day}',
                                       (destination / f'{day}.md').read_text())
                    return
                git('fetch', 'origin', 'main')
                try:
                    git('rebase', 'origin/main')
                except subprocess.CalledProcessError:
                    git('rebase', '--abort')
                    raise RuntimeError('Concurrent report changes conflict; local commit retained for review. No force push attempted.')
            raise RuntimeError('Push failed after three attempts; local commit retained for review.')


if __name__ == '__main__':
    main()
