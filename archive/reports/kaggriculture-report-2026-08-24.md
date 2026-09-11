# Kaggriculture Daily Report — 2026-08-24

## Sync summary
- Mine: 16 new episodes ingested (across 20 submissions checked; only `submission-v2-reopened-provisional.zip` and `main_v11a_compact_livestock.py` had new games — all older submissions already at their 10-episode cap).
- Leaderboard: 50 new episodes ingested, 10 each from 5 scouted teams: Ryo Hasegawa, Crop Dusta, Subramanya N, junseok lee, Arman Tuganbaev.
- Today's new "mine" games: 8 W / 8 L (50/50 split — see loss tags below).

## My submissions
(All-time, full DB — not just today's new episodes)

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v11a_compact_livestock.py | 639.3 | 78 | 92 | 0 | +23,180 | -33,326 |
| submission-v2-reopened-provisional.zip | 506.3 | 68 | 81 | 0 | +15,417 | -32,198 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |

Overall DB totals: 394 WIN / 396 LOSS / 5 TIE.

## Loss tags
- `SHED_AT_CAP`: 93 losses (the only tag present in the DB — every tagged loss hits this, consistent with the known ~10-animal service ceiling documented in project memory).

## Top opponents in the data
(By game count — mix of real ladder + today's scouted teams; not the same as the 5 scouted teams specifically.)

| opponent | n games | avg final money | wheat/carrot/tomato/straw/melon (avg) | quad2_day | avg hires | notable sells |
|---|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5/26.5/0/0/29.5 | 9.0 | 6.59 | MILK 9,920; FERTILIZER 9,804; MELON 9,784; CARROT 9,355; WHEAT 9,212 |
| Khoa Le | 4 | $70,224 | 92.75/0/0/18.25/21.25 | 0.0 | 10.16 | WHEAT 1,380; MILK 867; FERTILIZER 630 |
| Darshan Makwana | 4 | $95,656 | 93.0/2.0/0/1.25/30.0 | 11.0 | 7.07 | FERTILIZER 1,237; WOOL 729; MILK 576 |
| pengshy | 3 | $81,135 | 42.33/2.67/0/34.0/28.67 | 9.0 | 8.94 | WHEAT 2,328; MILK 586; FERTILIZER 578 |
| mchicen | 3 | $67,399 | 13.33/0/0/5.33/5.0 | 9.0 | 8.0 | FERTILIZER 953; MILK 693; WOOL 333 |

Caveat: Solve Langseth's sell totals (~9-10k units per item) are wildly out of line with the rest and almost certainly reflect round-trip buy/sell activity within matches (a known engine artifact), not real production volume — don't read those numbers as a genuine 10x production edge.

Darshan Makwana stands out with the highest avg final money ($95,656) on a wheat-heavy, near-zero-strawberry mix — worth a look if hypothesis-testing continues in that direction, though this is only 4 games.

## Local versions not yet submitted
- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py` (per memory, this is the rejected clone-replica rebuild — expected to be unsubmitted)

## Notes
- Auth via persisted token worked cleanly, no issues.
- `main_v11a_compact_livestock.py` is currently submitted and being scored live (639.3) despite memory recording it as a **rejected** hypothesis (0/40 wins in the round-11 test harness vs v10.5 and opp_scenario_v14) — worth flagging to Grace, since the ladder is actively playing a version she decisively rejected in testing.
- 12 submitted `.py` files (main_v2.py through main_v9.5_statehygiene.py, plus turn_08_small_cow_fleet.py and main_v11a) are not present locally in the project root — likely archived elsewhere (e.g. "Archived versions/") or cleaned up; not flagged as a problem, just noted since step 8 only checked the root directory.
- Today's 8W/8L "mine" split is a small sample (16 games) skewed toward the 6 new submission-v2-reopened-provisional and 10 new main_v11a_compact_livestock episodes — not representative of the full-DB win rates above.
