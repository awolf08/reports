import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('assemble_site', Path(__file__).parents[1] / 'scripts' / 'assemble-site.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AssembleSiteTests(unittest.TestCase):
    def test_preserves_archives_and_excludes_source_and_untracked_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            reports, dashboard, output = (root / name for name in ('reports', 'dashboard', 'site'))
            reports.mkdir()
            dashboard.mkdir()
            subprocess.run(['git', 'init', '-q', str(reports)], check=True)
            files = {'index.html': 'old homepage', 'CNAME': 'baybell.com',
                     'daily-finance/2026-05-27.html': 'older report',
                     'daily-finance/2026-05-28.html': 'latest report',
                     'assets/styles.css': 'existing styles', 'README.md': 'internal docs',
                     'private/report.json': '{"sample":"private fixture"}',
                     '.github/workflows/example.yml': 'not a web asset'}
            for name in ('daily-finance', 'weekly-finance', 'guru-position', 'private'):
                files[f'{name}/index.html'] = name
            for name, body in files.items():
                file = reports / name
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text(body)
            subprocess.run(['git', '-C', str(reports), 'add', '.'], check=True)
            (reports / 'private/untracked.json').write_text('must not be copied')
            (dashboard / 'index.html').write_text('new dashboard')
            (dashboard / '_next').mkdir()
            (dashboard / '_next/app.js').write_text('app')
            (dashboard / 'data').mkdir()
            (dashboard / 'data/market.json').write_text('{"provider":"finnhub"}')
            for name in ('daily-finance', 'weekly-finance'):
                (dashboard / name).mkdir()
                (dashboard / name / 'index.html').write_text(f'new {name} landing')
            (dashboard / '.vite').mkdir()
            (dashboard / '.vite/manifest.json').write_text('build internals')
            module.assemble(reports, dashboard, output)
            self.assertIn('./2026-05-28.html', (output / 'daily-finance/latest.html').read_text())
            self.assertEqual((output / 'index.html').read_text(), 'new dashboard')
            self.assertEqual((output / 'report-index.html').read_text(), 'old homepage')
            self.assertEqual((reports / 'index.html').read_text(), 'old homepage')
            for name in files:
                if name in ('daily-finance/index.html', 'weekly-finance/index.html'):
                    continue
                if name.split('/')[0] in module.REPORT_DIRS or name == 'CNAME':
                    self.assertEqual((output / name).read_bytes(), (reports / name).read_bytes())
            self.assertEqual((output / 'daily-finance/index.html').read_text(), 'new daily-finance landing')
            self.assertEqual((output / 'weekly-finance/index.html').read_text(), 'new weekly-finance landing')
            for name in ('README.md', '.github', '.git', '.vite', 'private/untracked.json'):
                self.assertFalse((output / name).exists())
            with self.assertRaises(ValueError):
                module.assemble(reports, dashboard, reports)


if __name__ == '__main__':
    unittest.main()
