import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from datetime import date

from finance_daily_report import __main__ as cli
from finance_daily_report.config import Settings
from finance_daily_report.fetchers import ReportData

spec = importlib.util.spec_from_file_location('publish_report', Path(__file__).parents[1] / 'scripts/publish-report.py')
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)


class PublicationTests(unittest.TestCase):
    def test_daily_cli_preserves_existing_snapshot_at_public_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            snapshot = output / '2026-09-16.snapshots.json'
            snapshot.write_text(json.dumps({'schema_version': 1, 'report_date': '2026-09-16',
                'snapshots': [{'slot': '05:55', 'captured_at': '2026-09-16T05:55:00-07:00'}]}))
            settings = Settings(output_dir=output, snapshot_slot='07:59')
            with patch('sys.argv', ['report', '--date', '2026-09-16']), \
                 patch.object(cli, 'load_dotenv'), \
                 patch.object(cli.Settings, 'from_env', return_value=settings), \
                 patch.object(cli, 'collect_report_data', return_value=ReportData(report_date=date(2026, 9, 16))), \
                 patch.object(cli, 'render_html', return_value='<html>report</html>'), \
                 patch.object(cli, 'render_markdown', return_value='Valid report'):
                self.assertEqual(cli.main(), 0)
            self.assertTrue((output / '2026-09-16.html').exists())
            self.assertEqual([x['slot'] for x in json.loads(snapshot.read_text())['snapshots']], ['05:55', '07:59'])
            self.assertTrue(publisher.report_complete(output, '2026-09-16', False, '07:59'))
            self.assertFalse(publisher.report_complete(output, '2026-09-16', False, '11:59'))
            publisher.validate_report(output, '2026-09-16', False)
            (output / '2026-09-16.md').write_text('No news items returned')
            with self.assertRaises(RuntimeError):
                publisher.validate_report(output, '2026-09-16', False)

    def test_weekly_default_directory(self):
        with patch('sys.argv', ['report', '--weekly']), \
             patch.dict('os.environ', {}, clear=True), \
             patch.object(cli, 'load_dotenv'), \
             patch.object(cli.Settings, 'from_env', return_value=Settings()), \
             patch.object(cli, 'collect_weekly_report_data'), \
             patch.object(cli, 'write_weekly_report', return_value=[]) as write:
            cli.main()
        self.assertEqual(write.call_args.args[2], Path('weekly-finance'))


if __name__ == '__main__':
    unittest.main()
