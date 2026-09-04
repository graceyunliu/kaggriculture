# Kaggriculture Daily Report — 2026-08-28

## Sync summary
- Mine: 44 new episodes ingested (across all my submissions, capped 10/submission; most already-synced subs returned 0 new).
- Leaderboard: 50 new episodes ingested across 5 scouted teams: Crop Dusta, Subramanya N, Ryo Hasegawa, William Diment, Michael Timbs.
- Total DB size: 2,400 episodes with a result (`my_result` set): 430 WIN / 460 LOSS / 5 TIE.

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v11a_compact_livestock.py | 634.7 | 97 | 123 | 0 | +22,237 | -31,446 |
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
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,687 | -16,062 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,913 | -30,258 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| v2_1_experimental_ladder.zip | 437.2 | 2 | 8 | 0 | +3,018 | -26,776 |
| v2_1_minimal_scenario_challenger.zip | 448.1 | 4 | 6 | 0 | +7,720 | -18,324 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,835 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |

Note: W/L/T counts reflect all games logged in the DB across syncs to date, not just today's new episodes.

## Loss tags
- SHED_AT_CAP: 116 losses tagged (only tag currently populated in DB).

## Top opponents in the data
(Most-represented non-Grace profiles currently in DB — mix of real ladder + leaderboard-scouted opponents.)

| name | n games | avg final money | wheat | carrot | tomato | strawberry | melon | quad2_day | avg hires |
|---|---|---|---|---|---|---|---|---|---|
| Solve Langseth | 4 | 67,020 | 39.5 | 26.5 | 0.0 | 0.0 | 29.5 | 9.0 | 6.59 |
| Khoa Le | 4 | 70,224 | 92.8 | 0.0 | 0.0 | 18.2 | 21.2 | 0.0 | 10.16 |
| Darshan Makwana | 4 | 95,656 | 93.0 | 2.0 | 0.0 | 1.2 | 30.0 | 11.0 | 7.07 |
| pengshy | 3 | 81,135 | 42.3 | 2.7 | 0.0 | 34.0 | 28.7 | 9.0 | 8.94 |
| mchicen | 3 | 67,399 | 13.3 | 0.0 | 0.0 | 5.3 | 5.0 | 9.0 | 8.00 |

Notable sells (raw unit totals — caveat: can be inflated by round-trip buy/sell within a match, don't over-read absolute volume):
- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 / CARROT 9,355 / WHEAT 9,212 — extremely high, round-trip-inflated.
- Khoa Le: WHEAT 1,380 / MILK 867 / FERTILIZER 630.
- Darshan Makwana (highest avg money, $95.6k): FERTILIZER 1,237 / WOOL 729 / MILK 576 — wheat-heavy (93 plantings) with early quad2 (day 11) and moderate hires.

## Local versions not yet submitted
- main_v10.6a_radius3.py
- main_v_clonereplica1.py

(Neutral fact only — not a recommendation on which to submit. See project memory for why v_clonereplica1 was built/tested: it was rejected in self-play evaluation, so its absence from the submitted set is expected.)

## Notes
- Auth via persisted `.kaggle/access_token` succeeded without issue.
- Leaderboard sync (`sync_replays.py leaderboard 5 --max-episodes 10`) is long-running (~5+ min); required 2 invocations to fully complete due to shell timeout — idempotent, no data loss, second call resumed and finished cleanly with a "Done." line.
- `tags` table currently only contains the `SHED_AT_CAP` tag type — no other loss-tag categories logged yet in this DB.
- Darshan Makwana stands out as the strongest opponent by avg final money ($95.6k) among the 5 sampled — worth a closer look if targeting a specific opponent profile for future strategy tuning.
