"""Assemble the Baybell homepage without altering the tracked report archive."""
from pathlib import Path
import argparse
import shutil
import subprocess
import hashlib

REPORT_DIRS = ('assets', 'daily-finance', 'weekly-finance', 'guru-position', 'private')
DASHBOARD_ITEMS = ('index.html', 'index.rsc', '_next', 'data', 'favicon.svg')


def assemble(reports: Path, dashboard: Path, output: Path):
    reports, dashboard, output = reports.resolve(), dashboard.resolve(), output.resolve()
    if output == reports or output in reports.parents or output == dashboard or output in dashboard.parents:
        raise ValueError('Output must not replace either source directory or its parents.')
    for required in ('index.html', '_next', 'data/market.json'):
        if not (dashboard / required).exists():
            raise ValueError(f'Missing dashboard build file: {required}')
    if output.exists():
        raise ValueError('Output already exists; select an empty output path.')
    output.mkdir(parents=True)
    tracked = subprocess.check_output(['git', '-C', str(reports), 'ls-files', '-z']).decode().split('\0')
    preserved = []
    for name in filter(None, tracked):
        relative = Path(name)
        if relative.parts[0] not in REPORT_DIRS and name != 'CNAME':
            continue
        source = reports / relative
        if source.is_symlink() or not source.is_file():
            raise ValueError(f'Only regular tracked report files are supported: {name}')
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        preserved.append(relative)
    # Keep the former homepage at the same directory depth so its links work.
    shutil.copy2(reports / 'index.html', output / 'report-index.html')
    for name in DASHBOARD_ITEMS:
        source = dashboard / name
        if source.is_dir():
            shutil.copytree(source, output / name)
        elif source.is_file():
            shutil.copy2(source, output / name)
    (output / '.nojekyll').write_text('')
    for relative in preserved:
        if hashlib.sha256((reports / relative).read_bytes()).digest() != hashlib.sha256((output / relative).read_bytes()).digest():
            raise ValueError(f'Report content changed during assembly: {relative}')
    for name in ('daily-finance', 'weekly-finance', 'guru-position', 'private'):
        if not (output / name / 'index.html').is_file():
            raise ValueError(f'Missing preserved landing page: {name}')
    print(f'Assembled Dashboard and preserved {len(preserved)} report/assets files in {output}.')
    return preserved


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--reports', type=Path, default=Path('.'))
    parser.add_argument('--dashboard', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assemble(args.reports, args.dashboard, args.output)
