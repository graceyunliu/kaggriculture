# Kaggriculture Daily Report — 2026-08-12

## Sync summary

- Mine: 30 new episodes across 3 submissions — submission-v2-reopened-provisional.zip (10), main_v11a_compact_livestock.py (10), main_v10.6_radius3.py (10). All other submissions had 0 new (already fully synced).
- Leaderboard: 50 new episodes across 5 scouted teams (10 each) — カワシギ, researchstudio.site, Filip Strzałka, Arda Ceylan, Syed Muhammad Gillani.
- Total new: 80 episodes ingested. No errors, both syncs completed on first attempt.

## My submissions

All-time W/L/T and margins per version, from the full DB (not just today's new episodes). Live public score from Kaggle submissions list.

| version | public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v11a_compact_livestock.py | 677.2 | 22 | 28 | 0 | +27,864 | -28,878 |
| main_v10.6_radius3.py | 657.4 | 22 | 28 | 0 | +29,489 | -24,482 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| submission-v2-reopened-provisional.zip | 494.1 | 12 | 28 | 0 | +14,827 | -29,540 |

Overall totals across all versions in DB: 276 W / 276 L / 5 T.

Today's 30 new episodes (submission-v2-reopened-provisional.zip, main_v11a_compact_livestock.py, main_v10.6_radius3.py, 10 each): 12 W / 18 L.

## Loss tags

All-time (all losses in DB, all versions):

- SHED_AT_CAP: 67

Today's new losses only (18 losses across the 3 versions synced today):

- SHED_AT_CAP: 4

## Top opponents in the data

Most-represented non-Grace profiles currently in the DB (mix of real ladder opponents and today's leaderboard scouting):

| opponent | n games | avg final money | plant mix (wheat/carrot/tomato/straw/melon) | quad2_day | avg hires |
|---|---|---|---|---|---|
| islet | 3 | 106,912 | 82.7 / 0 / 0 / 32.7 / 20.3 | 7 | 9.77 |
| Darshan Makwana | 4 | 95,656 | 93.0 / 2.0 / 0 / 1.2 / 30.0 | 11 | 7.07 |
| Syed Muhammad Gillani | 3 | 86,041 | 117.2 / 0 / 0 / 34.0 / 21.0 | 6.6 | 8.55 |
| Khoa Le | 4 | 70,224 | 92.8 / 0 / 0 / 18.2 / 21.2 | 0 | 10.16 |
| Solve Langseth | 4 | 67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9 | 6.59 |

Notable sells (raw units, round-trip buy/sell within a match can inflate these — treat as directional, not precise volume):

- Syed Muhammad Gillani: WHEAT 14,879, STRAWBERRY 5,634, MILK 5,122 — outlier volumes vs. the rest of this cohort, likely round-trip inflated.
- Solve Langseth: near-even spread across MILK (9,920), FERTILIZER (9,804), MELON (9,784), CARROT (9,355), WHEAT (9,212) — also looks round-trip inflated given the uniformity.
- islet and Darshan Makwana have the most "normal"-looking sell totals (hundreds, not thousands) and also the two highest avg final money — worth another look as credible top performers rather than volume artifacts.

## Local versions not yet submitted

- main_v10.6a_radius3.py
- main_v_clonereplica1.py

## Notes

- main_v11a_compact_livestock.py is submitted (score 677.2, in the ladder history) but the file no longer exists locally in the project root — likely cleaned up after testing per the memory log (round 11 rejection).
- Auth, both syncs, and all DB/report queries completed without errors.
- sqlite3 CLI wasn't available in the sandbox; used Python's stdlib sqlite3 module instead — same DB, no functional difference.
