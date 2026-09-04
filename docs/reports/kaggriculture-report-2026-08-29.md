# Kaggriculture Daily Report — 2026-08-29

## Sync summary
- Mine: 10 new episodes downloaded and ingested for `main_v11a_compact_livestock.py` (submission 55338773).
- Leaderboard: partial only. Attempted 7x (task budget was 5-6); each `sync_replays.py leaderboard 5 --max-episodes 10` call hit the shell timeout mid-download. Files downloaded to disk for 4 teams (Crop_Dusta 38, Milan_Leonard 62, Yusuke_Hayashi 34, Kenjo1209 5 — partial) but **not yet ingested into the DB** (episode count unchanged at 2410 before/after). Re-run `sync_replays.py leaderboard 5 --max-episodes 10` again next time; it's idempotent and will finish the ingest.

## My submissions
| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v11a_compact_livestock.py | 634.7 | 102 | 128 | 0 | +21,808 | -30,824 |
| submission-v2-reopened-provisional.zip | 489.3 | 75 | 94 | 0 | +15,729 | -31,791 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v9.3_fertilize.py | 755.8 | 20 | 18 | 0 | +16,914 | -19,230 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| v2_1_experimental_ladder.zip | 448.7 | 2 | 8 | 0 | +3,018 | -26,776 |
| v2_1_minimal_scenario_challenger.zip | 425.3 | 4 | 6 | 0 | +7,720 | -18,324 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |

(V2_1_MINIMAL_SCENARIO_CHALLENGER_CLEAN.zip has 0 games in local DB — not yet played/logged locally.)

Overall today's DB: 435 W / 465 L / 5 T across all versions combined.

## Loss tags
- SHED_AT_CAP: 118 losses tagged (only tag currently populated in this DB).

## Top opponents in the data
Top 5 by game count logged (mix of real ladder + leaderboard scouts):

| opponent | n games | avg final money | plant mix (wheat/carrot/tomato/strawberry/melon) | quad2_day | avg hires |
|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9.0 | 6.6 |
| Khoa Le | 4 | $70,224 | 92.75 / 0 / 0 / 18.25 / 21.25 | 0.0 | 10.2 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0 / 1.25 / 30.0 | 11.0 | 7.1 |
| pengshy | 3 | $81,135 | 42.3 / 2.7 / 0 / 34.0 / 28.7 | 9.0 | 8.9 |
| mchicen | 3 | $67,399 | 13.3 / 0 / 0 / 5.3 / 5.0 | 9.0 | 8.0 |

Notable sell totals (top items, round-trip buy/sell inflation caveat applies — don't over-read absolute volume):
- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 / CARROT 9,355 / WHEAT 9,212 — very high, likely round-trip-inflated.
- Khoa Le: WHEAT 1,380 / MILK 867 / FERTILIZER 630 / MELON 483 / WOOL 454.
- Darshan Makwana: FERTILIZER 1,237 / WOOL 729 / MILK 576 / MELON 502 / WHEAT 205 — highest avg final money ($95.6k) of the five.

## Local versions not yet submitted
- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

## Notes
- Leaderboard sync (`sync_replays.py leaderboard 5 --max-episodes 10`) did not complete in this run — repeated shell timeouts (7 attempts) meant replay files for 4 teams downloaded to `Replays/Auto/leaderboard-*` but weren't ingested (DB episode count stayed at 2410 throughout). Needs a follow-up run to finish ingestion.
- `tags` table currently only has one tag type populated (SHED_AT_CAP) — no breakdown diversity to report beyond that.
- Auth via persisted `.kaggle/access_token` worked without issue.
