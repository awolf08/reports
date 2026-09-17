import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('publisher_git', Path(__file__).parents[1] / 'scripts/publish-report.py')
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)


class PublisherGitTests(unittest.TestCase):
    def test_publish_to_one_origin_and_skip_repeat(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            origin, checkout = base / 'origin.git', base / 'checkout'
            subprocess.run(['git', 'init', '-q', '--bare', str(origin)], check=True)
            subprocess.run(['git', 'init', '-q', '-b', 'main', str(checkout)], check=True)
            def git(*args):
                return subprocess.check_output(['git', '-C', str(checkout), *args], text=True).strip()
            git('config', 'user.name', 'Test')
            git('config', 'user.email', 'test@example.invalid')
            git('remote', 'add', 'origin', str(origin))
            (checkout / 'daily-finance').mkdir()
            (checkout / 'README.md').write_text('fixture')
            git('add', '.')
            git('commit', '-qm', 'Initial')
            git('push', '-u', 'origin', 'main')
            before = git('rev-parse', 'HEAD')
            real_run = subprocess.run
            generated = []
            def run(command, **kwargs):
                if '-m' in command and 'finance_daily_report' in command:
                    output = Path(command[command.index('--output-dir') + 1])
                    (output / '2026-09-16.html').write_text('<html>Valid report</html>')
                    (output / '2026-09-16.md').write_text('Valid report')
                    (output / '2026-09-16.snapshots.json').write_text(json.dumps({
                        'report_date': '2026-09-16', 'snapshots': [{'slot': '05:55'}]}))
                    generated.append(True)
                    return subprocess.CompletedProcess(command, 0)
                return real_run(command, **kwargs)
            with patch.object(publisher, 'ROOT', checkout), \
                 patch('sys.argv', ['publisher', '--date', '2026-09-16']), \
                 patch.dict('os.environ', {}, clear=True), \
                 patch.object(publisher.subprocess, 'run', side_effect=run):
                publisher.main()
                after = git('rev-parse', 'HEAD')
                self.assertNotEqual(before, after)
                self.assertEqual(git('rev-parse', 'origin/main'), after)
                publisher.main()
                self.assertEqual(git('rev-parse', 'HEAD'), after)
            self.assertEqual(len(generated), 1)
            self.assertEqual(git('status', '--porcelain'), '')


if __name__ == '__main__':
    unittest.main()
