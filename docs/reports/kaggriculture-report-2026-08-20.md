# Kaggriculture Daily Report — 2026-08-20

## Sync summary

- Mine: 20 new episodes downloaded (across 2 submissions with new activity: `submission-v2-reopened-provisional.zip` +10, `main_v11a_compact_livestock.py` +10; all other submissions had 0 new).
- Leaderboard (top 5): 50 new episodes downloaded — Ryo Hasegawa +10, tetsuya +10, Crop Dusta +10, Arman Tuganbaev +10, Subramanya N +10.
- Total: 70 new episodes ingested into `kaggriculture.db`.

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v11a_compact_livestock.py | 643.1 | 60 | 70 | 0 | +22,277 | -33,591 |
| submission-v2-reopened-provisional.zip | 514.6 | 54 | 66 | 0 | +15,581 | -30,082 |
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
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,687 | -16,062 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,913 | -30,258 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,835 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |

Overall across all episodes with a recorded result: 362 W / 359 L / 5 T.

## Loss tags

- SHED_AT_CAP: 87 losses (only tag currently recorded).

## Top opponents in the data

| opponent | games | avg final money | plant mix (wheat/carrot/tomato/strawberry/melon) | quad2_day | avg hires/day |
|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9.0 | 6.59 |
| Khoa Le | 4 | $70,224 | 92.75 / 0 / 0 / 18.25 / 21.25 | 0.0 | 10.16 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0 / 1.25 / 30.0 | 11.0 | 7.07 |
| pengshy | 3 | $81,135 | 42.33 / 2.67 / 0 / 34.0 / 28.67 | 9.0 | 8.94 |
| mchicen | 3 | $67,399 | 13.33 / 0 / 0 / 5.33 / 5.0 | 9.0 | 8.00 |

Notable sell totals (round-trip buy/sell inflation caveat applies — raw unit totals can overstate real net production when items are bought and resold within the same match):

- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 — all four top items sit near 9,200-9,900, suspiciously uniform, likely round-trip inflated rather than genuine production volume.
- Darshan Makwana: FERTILIZER 1,237 / WOOL 729 — highest avg money of the five ($95.7k); no STRAWBERRY/TOMATO focus, wheat-heavy (93 plantings) like Khoa Le.
- Khoa Le: WHEAT 1,380, highest avg_hires (10.16/day) of the group.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

## Notes

- Auth via persisted token in `.kaggle/access_token` succeeded without issue.
- `sync_replays.py leaderboard` needed two attempts — first attempt exceeded the shell tool's per-call time budget (stdout was buffered so no partial progress was visible); re-run with `python3 -u` completed cleanly in one pass and ingested all 50 episodes with 0 already-known conflicts.
- Loss-tag table currently only has one tag (SHED_AT_CAP) instrumented in the harness; no other tag types have been logged to date.
- Per project memory, current champion is `main_v10.6_radius3.py` (undefeated across 58 internal self-play/adversarial hypotheses tested through Aug 7); `main_v11a_compact_livestock.py` was later rejected in that internal testing (0/40 wins vs v10.5 and a real-opponent clone) despite showing more raw win volume here — its higher W count reflects more episodes played, not a validated edge. Live ladder W/L ratios in this report are a smaller, noisier sample than the internal seed-controlled tests and shouldn't override that finding.
