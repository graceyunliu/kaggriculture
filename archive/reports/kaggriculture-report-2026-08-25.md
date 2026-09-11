# Kaggriculture Daily Report — 2026-08-25

## Sync summary
- Mine: 25 new episodes ingested (5 from `submission-v2-reopened-provisional.zip`, 20 from `main_v11a_compact_livestock.py`, across two capped runs — v11a has a large backlog, 250 episodes total).
- Leaderboard (top 5 teams): 50 new episodes ingested — Crop Dusta (10), Ryo Hasegawa (10), Subramanya N (10), tyz123456 (10), Kronki (10).
- 1 episode failed ingestion (harness.py `extract()` KeyError on a malformed `order` entry in one replay's market actions) — not fixed, out of scope for this sync-only task. All other 74 attempted ingests succeeded.

## My submissions
| version | live public score | W | L | T | avg win margin | avg loss margin |
|---|---|---|---|---|---|---|
| main_v9.3_fertilize.py | 755.8 | 16 | 12 | 0 | +17,519 | -19,057 |
| main_v9.10_hire_calibrated.py | 732.6 | 17 | 15 | 0 | +17,198 | -22,038 |
| main_v9.5_statehygiene.py | 720.8 | 13 | 14 | 0 | +12,102 | -27,614 |
| turn_08_small_cow_fleet.py | 711.3 | 17 | 15 | 0 | +16,029 | -38,293 |
| main_v9.1_buyfeed_herd.py | 701.9 | 14 | 11 | 0 | +20,056 | -17,532 |
| main_v8.3.py | 684.2 | 22 | 21 | 1 | +31,836 | -31,240 |
| main_v10.5_siting.py | 681.5 | 17 | 21 | 0 | +30,931 | -34,082 |
| main_v7.5.py | 680.9 | 15 | 6 | 0 | +20,004 | -53,481 |
| main_v8.py | 673.8 | 10 | 10 | 0 | +25,913 | -30,258 |
| main_v8.2.py | 676.2 | 15 | 12 | 1 | +25,197 | -12,689 |
| main_v10.6_radius3.py | 657.4 | 28 | 31 | 0 | +27,330 | -22,675 |
| main_v11a_compact_livestock.py | 647.9 | 85 | 105 | 0 | +22,791 | -31,544 |
| main_v9.2_parallel_build.py | 695.2 | 14 | 11 | 0 | +27,687 | -16,062 |
| main_v7.9.py | 608.6 | 11 | 14 | 0 | +30,425 | -36,078 |
| main_v2.1.py | 596.2 | 5 | 3 | 0 | +27,198 | -21,401 |
| main_v7.2.py | 579.0 | 8 | 5 | 1 | +9,724 | -83,517 |
| main_v5.py | 556.8 | 14 | 12 | 1 | +19,641 | -43,033 |
| main_v3.py | 550.6 | 8 | 6 | 1 | +34,316 | -37,710 |
| main_v2.py | 564.2 | 4 | 4 | 0 | +27,302 | -46,835 |
| submission-v2-reopened-provisional.zip | 512.7 | 68 | 81 | 0 | +15,417 | -32,198 |

(Table sorted by live public score, descending. W/L/T are from all replay episodes currently in the DB for that version, not just today's new ones.)

## Loss tags
- SHED_AT_CAP: 97 (the only tag currently populated in the DB)

Overall today's DB snapshot: 401 WIN / 409 LOSS / 5 TIE across all my episodes with a recorded result.

## Top opponents in the data
Most-represented distinct opponents currently in the DB (max 4 games each — no single opponent dominates the sample):

| opponent | n | avg final money | plant wheat/carrot/tomato/strawberry/melon | quad2_day | avg hires/day | notable sells |
|---|---|---|---|---|---|---|
| Solve Langseth | 4 | $67,020 | 39.5/26.5/0/0/29.5 | 9.0 | 6.6 | MILK 9920, FERTILIZER 9804, MELON 9784, CARROT 9355, WHEAT 9212 |
| Khoa Le | 4 | $70,224 | 92.8/0/0/18.2/21.2 | 0.0 | 10.2 | WHEAT 1380, MILK 867, FERTILIZER 630, MELON 483, WOOL 454 |
| Darshan Makwana | 4 | $95,656 | 93.0/2.0/0/1.2/30.0 | 11.0 | 7.1 | FERTILIZER 1237, WOOL 729, MILK 576, MELON 502, WHEAT 205 |
| pengshy | 3 | $81,135 | 42.3/2.7/0/34.0/28.7 | 9.0 | 8.9 | WHEAT 2328, MILK 586, FERTILIZER 578, MELON 445, WOOL 256 |
| mchicen | 3 | $67,399 | 13.3/0/0/5.3/5.0 | 9.0 | 8.0 | FERTILIZER 953, MILK 693, WOOL 333, EGG 208, STRAWBERRY 4 |

Caveat: raw sell-unit totals (especially Solve Langseth's ~9-10k/item figures) can be inflated by round-trip buy/sell activity within a match — a known engine artifact, don't read as pure production output.

## Local versions not yet submitted
- main_v10.6a_radius3.py
- main_v_clonereplica1.py

## Notes
- Sample sizes per named opponent are small (3-4 games) — today's leaderboard scout pulled from 5 different teams, so no single opponent has deep history yet.
- One episode failed ingestion due to a pre-existing `harness.py extract()` bug (assumes market `order` is a list; one replay had a malformed/dict order). Left unfixed per task scope (read-only analysis, no code changes).
- `main_v11a_compact_livestock.py` has a much larger episode backlog (250 total) than other versions — required two sync passes today to pull 20 of its new episodes (capped at 10/run).
