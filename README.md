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
