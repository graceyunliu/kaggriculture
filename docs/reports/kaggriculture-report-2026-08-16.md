# Kaggriculture Daily Report — 2026-08-16

## Sync summary
- Mine: 20 new episodes — 10 from `submission-v2-reopened-provisional.zip`, 10 from `main_v11a_compact_livestock.py`. All other own submissions already fully synced (0 new).
- Leaderboard (top 5): 50 new episodes — 10 each from カワシギ, Thomas Tschinkel, peikopon, Utkarsh #2, ReCurSiON.

## My submissions
(Cumulative DB history per version, not just today's new episodes.)

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v11a_compact_livestock.py | 669.0 | 42 | 48 | 0 | +23,956 | -33,615 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| submission-v2-reopened-provisional.zip | 510.1 | 35 | 45 | 0 | +17,782 | -29,899 |

Overall totals (all versions, all time in DB): 325 W / 316 L / 5 T.

## Loss tags
- SHED_AT_CAP: 78 (only tag currently populated)

## Top opponents in the data
| opponent | n games | avg final money | wheat | carrot | tomato | straw | melon | quad2_day | avg hires |
|---|---|---|---|---|---|---|---|---|---|
| Darshan Makwana | 4 | $95,656 | 93.0 | 2.0 | 0.0 | 1.2 | 30.0 | 11.0 | 7.07 |
| islet | 3 | $106,912 | 82.7 | 0.0 | 0.0 | 32.7 | 20.3 | 7.0 | 9.77 |
| pengshy | 3 | $81,135 | 42.3 | 2.7 | 0.0 | 34.0 | 28.7 | 9.0 | 8.94 |
| Khoa Le | 4 | $70,224 | 92.8 | 0.0 | 0.0 | 18.2 | 21.2 | 0.0 | 10.16 |
| Solve Langseth | 4 | $67,020 | 39.5 | 26.5 | 0.0 | 0.0 | 29.5 | 9.0 | 6.59 |

Notable sells (raw unit totals — inflated by same-match buy/sell round-trips, don't over-read):
- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 (extreme volumes, likely round-trip artifact)
- Darshan Makwana: FERTILIZER 1,237 / WOOL 729 / MILK 576
- islet: FERTILIZER 551 / STRAWBERRY 510 / MILK 409

Sample sizes here are small (3-4 games each) — directional signal only.

## Local versions not yet submitted
- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

(`main_v11a_compact_livestock.py` was submitted but the working copy now only exists under `Archived versions/` and `Chatgpt Agents/`, not in the project root.)

## Notes
- Auth via persisted `.kaggle/access_token` succeeded, no issues.
- Both sync commands (`mine`, `leaderboard 5`) completed in a single pass each — no retries needed.
- Loss-tag data is thin (only `SHED_AT_CAP` populated) — likely reflects current tag-instrumentation coverage in `harness.py`, not that shed capacity is the only real loss driver.
- Top-opponent numbers pull from whichever profiles happen to be in the DB today (mostly newly-scouted leaderboard teams), not a stable long-run sample — treat as a snapshot.
