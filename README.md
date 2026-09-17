# Baybell Reports

The single repository for Baybell's report generators, report archives and GitHub Pages publishing at https://baybell.com. The homepage and report landing pages remain maintained independently in [stock_dashboard](https://github.com/awolf08/stock_dashboard).

## Layout

- `finance_daily_report/`: Python daily/weekly generation and intraday snapshots.
- `daily-finance/YYYY-MM-DD.{html,md,snapshots.json}`: canonical daily archive.
- `weekly-finance/YYYY-MM-DD.{html,md}`: canonical weekly archive.
- `ChatGPT/`: curated market-close Markdown; `latest.md` is read by the Dashboard build.
- `guru-position/`, `private/`, `assets/`: existing report pages and assets.
- `scripts/assemble-site.py`: merges the Dashboard build with tracked report files.

## Generate locally

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m finance_daily_report
python -m finance_daily_report --weekly
```

Daily output defaults to `daily-finance/`; weekly output defaults to `weekly-finance/`. `--date YYYY-MM-DD`, `--output-dir PATH` and `--format md|html|both` remain available. For optional email, configure a local ignored `.env` using `.env.example`, then explicitly run `python -m finance_daily_report --email-if-configured`. The publisher sends optional configured email only after a successful commit/push, not during retries or dry runs. No SMTP repository secrets were configured in the source repository at migration.

## Publish

From a clean `main` checkout, with Python dependencies installed:

```bash
scripts/fallback-publish-report.sh
scripts/publish-weekly-report.sh
```

The publishers fast-forward from origin, generate in a temporary directory, validate the report, and commit/push only the dated report files in this repository. They retain existing snapshots. A local lock and shared Actions concurrency group coordinate daily/weekly writers; unrelated remote commits are rebased with bounded retries, and conflicts stop without a force push. Unpublished local commits are never pushed automatically.

`REPORT_DATE`, `REPORT_FORCE_GENERATE=true`, `REPORT_SNAPSHOT_SLOT`, `REPORT_TIMEZONE`, and `REPORT_ALLOWED_HOURS` control generation. `--dry-run` (or `REPORT_DRY_RUN=true`) generates and validates without modifying the archive, Git history, email or deployed site. Existing reports/slots are skipped unless forced.

- `daily-report.yml`: existing weekday backup schedule and snapshot-slot checks, plus manual dispatch.
- `weekly-report.yml`: Sunday generation, plus manual dispatch; existing reports are skipped.
- `deploy-homepage.yml`: builds on main pushes, successful report workflow completion, manual dispatch and every quarter-hour at UTC minutes 7, 22, 37 and 52. GitHub schedules may be delayed.

`workflow_run` explicitly deploys report changes committed by `GITHUB_TOKEN`, which do not trigger a new push workflow. The deployment checks out current main, pulls stock_dashboard/main, fetches market data, validates, assembles and deploys one Pages artifact. A failed build leaves the last deployment online.

Keep the existing `FINNHUB_API_KEY` secret and optional Dashboard variables. Cross-repository `REPORTS_DEPLOY_KEY` is no longer needed by this repository. Report settings can use repository variables `REPORT_TIMEZONE`, `REPORT_NEWS_LIMIT`, `REPORT_STOCK_LIMIT`, and `REPORT_WATCHLIST`.

## URLs and hosting

The custom domain remains `baybell.com`, with Pages source set to GitHub Actions. DNS and access policies are unchanged.

- `/`: Dashboard homepage.
- `/daily-finance/`, `/weekly-finance/`: Dashboard report landing pages.
- `/daily-finance/latest.html`, `/weekly-finance/latest.html`: redirects to the newest existing archived HTML report, including weekends.
- `/daily-finance/YYYY-MM-DD.html`, `/weekly-finance/YYYY-MM-DD.html`: unchanged dated report URLs.
- `/report-index.html`: original report navigation homepage.

The site assembler publishes only tracked report/assets directories, CNAME, and Dashboard public output. Generator source, tests, `.env`, and ChatGPT source files are not copied into the Pages artifact. Public repository files remain accessible on GitHub. Existing private paths require the owner's existing access protection.

## Validation

```bash
python -m unittest discover -s tests -v
python scripts/assemble-site.py --reports . --dashboard ../stock_dashboard/dist/client --output site
```

## Migration and rollback

Imported generator and tests from `awolf08/FinanceDailyReport` at `b3473f50b27da3cc4ef02803848921d9c8844202`. The 245 overlapping report files were byte-identical; May 26/27 HTML and Markdown were added to complete the archive. ChatGPT sources were retained. Original Git history remains in the old repository; it is not rewritten or deleted.

After the new workflows are verified, disable the old daily generation workflow and retarget the existing Codex daily automation to this repository without force-regeneration. The old Pages deployment is replaced with a compatibility redirect site so existing dated and latest links continue to work. Do not run both generators concurrently.

For rollback, disable the new generation workflows, restore the previous reports revision through a reviewed revert, restore the old publisher and automation target, and deploy again. Keep all newly produced report files when reverting code. The existing Dashboard homepage dependency and domain remain unchanged throughout.
