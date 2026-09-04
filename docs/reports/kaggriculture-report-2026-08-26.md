# Kaggriculture Daily Report — 2026-08-26

## Sync summary

- Mine: 20 new episodes — `submission-v2-reopened-provisional.zip` (10) + `main_v11a_compact_livestock.py` (10). All other submissions already fully synced (0 new).
- Leaderboard: 50 new episodes — 10 each from Crop Dusta, Ryo Hasegawa, Subramanya N, Blu3s, tyz123456.
- Total: 70 new episodes ingested. Today's mine-only record: 8W / 12L / 0T.

## My submissions

All-time DB record by version (live public score from Kaggle leaderboard):

| version | public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,835 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,913 | -30,258 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,687 | -16,062 |
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| **main_v10.6_radius3.py (champion)** | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v11a_compact_livestock.py | 644.7 | 89 | 111 | 0 | +22,167 | -31,056 |
| submission-v2-reopened-provisional.zip | 508.6 | 72 | 87 | 0 | +15,721 | -32,571 |

Note: sample sizes vary a lot (4-200 games) — public score is the more reliable ranking signal; W/L here is against whatever mix of opponents happened to be replayed, not a controlled benchmark.

## Loss tags

All-time: `SHED_AT_CAP` — 99 occurrences (only tag currently logged).
Today's new losses only: `SHED_AT_CAP` — 2 occurrences.

## Top opponents in the data

Ranked by games logged (mix of real ladder + today's leaderboard scouting):

| opponent | games | avg final money | wheat/carrot/tomato/strawberry/melon (avg planted) | quad2_day | avg hires |
|---|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9.0 | 6.6 |
| Khoa Le | 4 | $70,224 | 92.8 / 0 / 0 / 18.3 / 21.3 | 0.0 | 10.2 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0 / 1.3 / 30.0 | 11.0 | 7.1 |
| pengshy | 3 | $81,135 | 42.3 / 2.7 / 0 / 34.0 / 28.7 | 9.0 | 8.9 |
| mchicen | 3 | $67,399 | 13.3 / 0 / 0 / 5.3 / 5.0 | 9.0 | 8.0 |

Sell totals (units, sum across games) — caveat: raw totals can be inflated by round-trip buy/sell within a match; treat as directional only.

- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 / CARROT 9,355 / WHEAT 9,212 — these figures look implausibly high for 4 games and are almost certainly round-trip artifacts, not real sell volume.
- Darshan Makwana (highest avg money, $95.7k): FERTILIZER 1,237 / WOOL 729 / MILK 576 / MELON 502 / WHEAT 205 — heavy wheat planter (93 avg) but sells relatively little wheat directly; FERTILIZER-heavy sell mix stands out.
- Khoa Le: WHEAT 1,380 / MILK 867 / FERTILIZER 630 / MELON 483 / WOOL 454 — highest avg_hires (10.2) of the group, zero carrot/tomato, quad2_day=0 (expands to second quadrant immediately).

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py` (this is the round-10 clone-replica rebuild noted in memory — already tested internally and rejected, -$68k/game vs v10.6; not expected to be a submission candidate)

## Notes

- Auth via persisted token succeeded, no issues.
- Both sync commands (`mine`, `leaderboard 5`) completed in a single pass each — no retries needed.
- `Solve Langseth` sell totals are clear round-trip-inflation outliers (~9,000-9,900 units on 4 games) — flagged above, not a real production signal.
- Tags table only has one tag type currently populated (`SHED_AT_CAP`); no other loss-cause tags are being logged, worth checking if that's expected or if tagging logic elsewhere silently isn't firing.
