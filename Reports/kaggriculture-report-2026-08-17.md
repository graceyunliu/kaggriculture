# Kaggriculture Daily Report — 2026-08-17

## Sync summary

- Mine: 20 new episodes (submission-v2-reopened-provisional.zip: 10, main_v11a_compact_livestock.py: 10; all other 18 submissions already fully synced, 0 new)
- Leaderboard (top 5 scouted): 50 new episodes — カワシギ (10), Thomas Tschinkel (10), tetsuya (10), ReCurSiON (10), Utkarsh #2 (10)
- Total new: 70 episodes

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,687 | -16,062 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,913 | -30,258 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v11a_compact_livestock.py | 656.2 | 47 | 53 | 0 | +22,602 | -33,452 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,835 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| submission-v2-reopened-provisional.zip | 518.9 | 41 | 49 | 0 | +17,343 | -28,903 |

Note: table covers full historical replay data in the DB, not just today's 20 new "mine" episodes (per-version breakouts for just today's batch weren't separately isolated — the 20 new episodes are folded into the totals above for `submission-v2-reopened-provisional.zip` and `main_v11a_compact_livestock.py`, the only two versions with new games today).

## Loss tags (all-time, all versions)

- SHED_AT_CAP: 81 losses tagged (only loss tag present in DB)
- Of today's 9 new losses specifically: SHED_AT_CAP tagged on 3

## Top opponents in the data

Ranked by games logged (mix of real ladder + leaderboard-scouted):

| opponent | n games | avg final money | plant mix (wheat/carrot/tomato/straw/melon) | quad2_day | avg hires |
|---|---|---|---|---|---|
| islet | 3 | $106,912 | 82.7/0/0/32.7/20.3 | 7.0 | 9.77 |
| Darshan Makwana | 4 | $95,656 | 93.0/2.0/0/1.25/30.0 | 11.0 | 7.07 |
| pengshy | 3 | $81,135 | 42.3/2.7/0/34.0/28.7 | 9.0 | 8.94 |
| Khoa Le | 4 | $70,224 | 92.75/0/0/18.25/21.25 | 0.0 | 10.16 |
| Solve Langseth | 4 | $67,020 | 39.5/26.5/0/0/29.5 | 9.0 | 6.59 |

Top sell totals (unit sums across their games — round-trip buy/sell inflation caveat applies, don't over-read absolute volume):
- islet: FERTILIZER 551, STRAWBERRY 510, MILK 409
- Darshan Makwana: FERTILIZER 1,237, WOOL 729, MILK 576
- pengshy: WHEAT 2,328, MILK 586, FERTILIZER 578
- Khoa Le: WHEAT 1,380, MILK 867, FERTILIZER 630
- Solve Langseth: MILK 9,920, FERTILIZER 9,804, MELON 9,784 (likely heavy round-trip artifact given the near-equal magnitudes across items)

None of the top-5 opponents plant TOMATO at all; wheat is the dominant crop for 4/5.

## Local versions not yet submitted

- main_v10.6a_radius3.py
- main_v_clonereplica1.py

(Per memory: v10.6_radius3.py is the current champion; v10.6a and the clone-replica variant exist locally but were never pushed to the ladder as separate submissions.)

## Notes

- Auth via persisted `.kaggle/access_token` worked cleanly, no token issues.
- `sync_replays.py mine` completed in a single invocation. `sync_replays.py leaderboard 5` needed a second, longer-timeout invocation to finish (first call hit the shell timeout partway through, was safely re-run/resumed).
- Per-version W/L breakout for *only* today's new episodes wasn't separated from cumulative history in this report — the table above is full lifetime replay stats per version, consistent with prior daily reports.
