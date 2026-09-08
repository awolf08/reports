# Baybell Reports

Static HTML report site for Baybell.

This project is designed for GitHub Pages and GoDaddy DNS at:

```text
https://baybell.com
```

Use `https://reports.baybell.com` as a forwarding URL to the same site.

- Daily finance reports
- Guru position reports
- Other future static research pages

## GitHub Pages

Suggested GitHub Pages settings:

1. Repository: `Settings` -> `Pages`
2. Source: `Deploy from a branch`
3. Branch: `main`
4. Folder: `/`
5. Custom domain: `baybell.com`

The `CNAME` file already contains:

```text
baybell.com
```

## Report Paths

Suggested report paths:

```text
daily-finance/2026-05-28.html
guru-position/2026-q2.html
options-flow/2026-05-28.html
```

## Private Report Paths

Private reports should live under:

```text
private/
private/trip-list/
```

Protect `https://baybell.com/private/*` with Cloudflare Access before publishing
real private content. Until that protection is active, anything committed under
`private/` is still publicly reachable on a static hosting service.

## GoDaddy DNS

Point the apex domain to GitHub Pages:

```text
@   A   185.199.108.153
@   A   185.199.109.153
@   A   185.199.110.153
@   A   185.199.111.153
```

Optional but recommended:

```text
www   CNAME   awolf08.github.io
```

Forward `reports.baybell.com` to `https://baybell.com` in GoDaddy domain forwarding.

After DNS propagates, enable `Enforce HTTPS` in GitHub Pages.

## Dashboard homepage publishing

The new `.github/workflows/deploy-homepage.yml` builds the homepage from
`awolf08/stock_dashboard` (`main`) and merges it with this repository's tracked
report archive. It runs hourly at minute 17 UTC, on eligible pushes, and manually.
The old root `index.html` remains the source for `/report-index.html` in the output;
existing daily-report scripts can continue updating that file normally.

The build enables `NEXT_PUBLIC_BAYBELL_HOME=1` so the Dashboard includes the
Daily Finance, Weekly Finance, Guru Positions, Options and Private Reports links.
Private Reports continues to point to `https://baybell.com/private/`, using the
owner's existing Cloudflare Access setup. The build does not create or modify
Access policies. Report files and their paths are copied without modification.
Only tracked report/archive files and the Dashboard's public build are published;
source code, untracked local files and build internals are excluded.

One-time setup:

```bash
gh secret set FINNHUB_API_KEY --repo awolf08/reports
gh api --method PUT repos/awolf08/reports/pages -f build_type=workflow
gh workflow run deploy-homepage.yml --repo awolf08/reports --ref main
```

The first command prompts for the key privately. The existing key in the
`stock_dashboard` repository cannot be read back or automatically copied.
Switch the Pages publishing mode only when the new workflow and secret are ready.
A failed quote fetch or build leaves the last deployment online.

The `CNAME` is preserved from this repository. Keep it set to `baybell.com`
until the `www` canonical-domain migration is ready. Before changing the custom
domain to `www.baybell.com`, verify Cloudflare Access protects private paths on
both hostnames and that the `www` DNS record remains proxied. GitHub may redirect
the apex to the configured `www` domain. No DNS or Access policy is changed by
the workflow itself.

Report-generator commits made with GitHub's automatic token may not trigger
another workflow; the hourly run still incorporates the latest archive.
GitHub can delay scheduled runs and can disable schedules in inactive public
repositories. Check Actions notifications and the Dashboard's snapshot timestamp.

Local checks (build the Dashboard at the domain root first):

```bash
python3 -m unittest discover -s tests -v
python3 scripts/assemble-site.py --reports . --dashboard ../stock_dashboard/dist/client --output site
```

The assembly command requires a new output directory and checks every preserved
file's SHA-256 digest. `site/` is ignored by Git. For another local assembly, choose
a different empty output directory or remove only the previously generated `site/`.

Rollback: change Pages back to branch publishing (`main`, root). The original
homepage and report archive remain tracked in this repository.
