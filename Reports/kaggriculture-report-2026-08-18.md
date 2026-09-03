# Kaggriculture Daily Report — 2026-08-18

## Sync summary

- Mine: 20 new episodes ingested. New activity on `submission-v2-reopened-provisional.zip` (10 new) and `main_v11a_compact_livestock.py` (10 new); all other own submissions had 0 new (already fully synced from prior runs).
- Leaderboard (top 5 scouted teams): 50 new episodes ingested, 10 each from カワシギ (score 3188.8), tetsuya (3055.4), Matteo123383iend (3016.6), ReCurSiON (2995.7), peikopon (2993.2).
- Total: 70 new episodes this run.

## My submissions

| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| submission-v2-reopened-provisional.zip | 513.3 | 45 | 55 | 0 | +16,421 | -28,667 |
| main_v11a_compact_livestock.py | 651.9 | 50 | 60 | 0 | +21,677 | -34,912 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,686 | -16,062 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,912 | -30,258 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,834 |

Cumulative across all versions: 343 W / 338 L / 5 T (all-time DB, not just today's new episodes).

## Loss tags

- `SHED_AT_CAP`: 83 (only tag currently logged as a loss factor across the full DB).

## Top opponents in the data

| opponent | games | avg final money | plant mix (wheat/carrot/tomato/strawberry/melon) | quad2_day | avg hires |
|---|---|---|---|---|---|
| islet | 3 | $106,912 | 82.7 / 0 / 0 / 32.7 / 20.3 | 7.0 | 9.8 |
| Darshan Makwana | 4 | $95,656 | 93.0 / 2.0 / 0 / 1.3 / 30.0 | 11.0 | 7.1 |
| pengshy | 3 | $81,135 | 42.3 / 2.7 / 0 / 34.0 / 28.7 | 9.0 | 8.9 |
| Khoa Le | 4 | $70,224 | 92.8 / 0 / 0 / 18.2 / 21.2 | 0.0 | 10.2 |
| Solve Langseth | 4 | $67,020 | 39.5 / 26.5 / 0 / 0 / 29.5 | 9.0 | 6.6 |

Notable sell totals (units, summed across games — caveat: round-trip buy/sell within a match can inflate these, don't read as pure production volume):
- Solve Langseth: MILK 9,920 / FERTILIZER 9,804 / MELON 9,784 — extreme volumes, near-certain round-trip artifact.
- islet: FERTILIZER 551 / STRAWBERRY 510 / MILK 409 — plausible production-scale numbers.
- Khoa Le: WHEAT 1,380 / MILK 867 / FERTILIZER 630.

## Local versions not yet submitted

- `main_v10.6a_radius3.py`
- `main_v_clonereplica1.py`

(Per memory: main_v10.6_radius3.py is the current standing champion at +$k/game across 58 hypotheses; v_clonereplica1 was already tested and decisively rejected per round 10 findings — its presence unsubmitted is expected, not a gap.)

## Notes

- 11 historically-submitted files (main_v2.py through main_v9.5_statehygiene.py, plus main_v7.2/7.5/7.9, v8, v8.2, v11a) no longer exist locally — expected churn from iterative development, not a data issue.
- Auth and both sync passes completed cleanly on the first attempt, no retries needed.
- Top-opponent list mixes real ladder opponents and today's leaderboard-scouted teams (per task instructions) — game counts per opponent are still small (3-4 games each) so profile averages here are noisy, not statistically firm.
