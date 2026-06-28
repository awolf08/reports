# Latest Ranking Tracker Run

- History: `/home/runner/work/tennis_ranking/tennis_ranking/data/ranking_history.csv`
- Chart: `/home/runner/work/tennis_ranking/tennis_ranking/reports/trend.svg`

## Captured Values
- 2026-06-10 wtn WTN Singles: 35.77
- 2026-06-10 wtn WTN Doubles: 36.53
- 2026-06-24 wtn WTN Singles: 35.14
- 2026-06-24 wtn WTN Doubles: 36.54
- 2026-06-03 usta Boys' 12 Northern California Quota List Points: 242
- 2026-06-03 usta Boys' 12 Northern California Quota List NorCal Rank: 145

## Diagnostics
- USTA playerInfo unavailable: HTTP 400; empty response
- USTA playerRankings unavailable: HTTP 400; empty response
- USTA page exposes these public endpoint declarations, but direct calls returned no data: /usta/api?type=playerRankings, /usta/api?type=playerRanklists&uaid={uaid}
- WTN URL is a USTA profile tab; skipped generic text scraping to avoid reading page-template numbers as WTN values.
