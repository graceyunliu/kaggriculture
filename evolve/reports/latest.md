# Evolution run 20260904-221043

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.05 h · candidates evaluated this run: 919 · games 30,070 (14,674/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 35 | 70 |
| dead_pattern | 212 | 424 |
| dead_smoke | 67 | 536 |
| alive | 605 | 29040 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 5078 · held-out evaluated: 477 · held-out PASS: 448

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | -11,526 | -1.8 | 1-9 | -16,823 | — | — | —-— |
| C1 | -18,630 | -7.8 | 0-10 | -19,663 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `c956f895839b` | c1 | mutate | **+11,824** | 9.3 | 20-0 | -16,689 | +7,590 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1 · blocks: crop_admission | wheat_sell_price ?, NEAR_RADIUS ?, OPP_GROWTH ? | cand pulls ahead of C1 from day 10 (gap +2,987 -> final +14,339); days 8-15 drivers: missed_water -35, sales_rev +3,738, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `1021e7262bf2` | c1 | ablate:load_per_hand | **+11,382** | 8.7 | 20-0 | -23,063 | +7,069 | melon_floor 150→200, harvest_min 2→1, wheat_stock 0→5, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, early_hire_days 5→6, fert_carry 3→4, max_animals 20→18, wheat_cap 18→23, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, MELON_PRICE_CUSHION 100→130, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→13, OPENING_MELONS 10→6 · blocks: crop_admission |  | cand pulls ahead of C1 from day 10 (gap +2,991 -> final +22,781); days 8-15 drivers: missed_water -35, sales_rev +3,744, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `daba421dc7ec` | wide | ablate:ROUTE_LEN | **+11,274** | 13.0 | 19-1 | -14,917 | +10,939 | melon_floor 150→200, early_hire_days 5→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, MAX_SHEEP 12→11, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,079 -> final +42,744); days 10-17 drivers: missed_water -59, sales_rev +10,680, work_turns +118, feed_hour -0.63. Hands 11 vs 8, animals 15 vs 8, plants 43 v |
| `e83ac3dafe96` | v312 | ablate:CROP_SWEEP_RADIUS | **+11,099** | 10.3 | 20-0 | -12,184 | +10,740 | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→13, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 16 (gap +3,157 -> final +60,413); days 14-21 drivers: sales_rev +28,375, work_turns +302, feed_hour -1.31, travel_per_task -0.23. Hands 13 vs 11, animals 17 vs 8, plant |
| `a65aa7a26283` | v312 | ablate:open_cows | **+11,091** | 8.2 | 20-0 | -9,982 | +14,798 | melon_floor 150→200, min_hands 3→5, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, demand_share 0.5→0.45, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +1,962 -> final +53,812); days 10-17 drivers: missed_water -87, sales_rev +9,772, work_turns +143, feed_hour -1.33. Hands 9 vs 8, animals 14 vs 8, plants 60 vs  |
| `9d4a5923e4a2` | v312 | crossover | **+11,024** | 7.0 | 20-0 | -11,663 | +10,307 | open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission | melon_floor -25, early_hire_days +919, wheat_cap ?, wheat_sell_price ?, CROP_SWEEP_RADIUS -21, MELON_PRICE_CUSHION ? | cand pulls ahead of C1 from day 9 (gap +1,784 -> final +43,988); days 7-14 drivers: missed_water -44, sales_rev +6,420, work_turns +78, feed_hour -0.93. Hands 9 vs 7, animals 17 vs 8, plants 44 vs 64. |
| `709c0fe12985` | v312 | crossover | **+10,960** | 8.4 | 20-0 | -11,390 | +9,868 | wheat_stock 0→5, open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission | melon_floor +134, wheat_stock ?, early_hire_days -424 | cand pulls ahead of C1 from day 12 (gap +2,081 -> final +38,180); days 10-17 drivers: sales_rev +15,722, missed_water -64, work_turns +168, feed_hour -1.25. Hands 13 vs 8, animals 15 vs 8, plants 58 v |
| `8e3b811495ea` | v312 | ablate:load_per_hand | **+10,812** | 7.0 | 19-1 | -9,552 | +7,770 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→13, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +2,552 -> final +39,312); days 7-14 drivers: missed_water -34, sales_rev +5,424, work_turns +58, feed_hour -1.46. Hands 12 vs 7, animals 14 vs 8, plants 46 vs 64 |
| `c2747c8ab595` | queue | llm:llm_20260903-181110_2 | **+10,796** | 12.3 | 20-0 | -15,472 | +10,500 |  · blocks: crop_admission |  |  |
| `5da0776c3c23` | queue | mutate | **+10,782** | 12.2 | 20-0 | -14,552 | +10,546 | melon_floor 150→100 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,078 -> final +29,298); days 10-17 drivers: missed_water -62, sales_rev +10,613, work_turns +125, feed_hour -0.65. Hands 11 vs 8, animals 15 vs 8, plants 42 v |
| `d5f89d5870e0` | v312 | ablate:melon_floor | **+10,760** | 7.7 | 20-0 | -11,699 | +9,734 | melon_floor 150→200, wheat_stock 0→5, open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +2,081 -> final +42,751); days 10-17 drivers: sales_rev +15,764, missed_water -64, work_turns +171, feed_hour -1.25. Hands 13 vs 8, animals 15 vs 8, plants 58 v |
| `616d161b196b` | queue | coupled:coupled_factorial_sep03 | **+10,746** | 10.3 | 20-0 | -15,934 | +8,734 | fert_buy 0→1 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,078 -> final +18,552); days 10-17 drivers: missed_water -62, sales_rev +10,613, work_turns +123, feed_hour -0.65. Hands 11 vs 8, animals 15 vs 8, plants 42 v |
| `35f286364d59` | v312 | ablate:melon_floor | **+10,638** | 6.6 | 20-0 | -12,523 | +10,332 | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +1,784 -> final +44,147); days 7-14 drivers: missed_water -44, sales_rev +6,420, work_turns +78, feed_hour -0.93. Hands 9 vs 7, animals 17 vs 8, plants 44 vs 64. |
| `eb81a9bff031` | queue | ablate:MAX_HANDS | **+10,556** | 8.0 | 19-1 | -14,034 | +9,530 | harvest_min 2→1, wheat_stock 0→14, open_wheat 7→8, early_hire_days 5→7, wheat_cap 18→19, HERD_LAST_DAY 19→20, OPP_GROWTH 1.3→1.4 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +1,688 -> final +25,223); days 7-14 drivers: missed_water -21, sales_rev +4,179, work_turns +35, feed_hour -1.51. Hands 9 vs 7, animals 10 vs 8, plants 62 vs 64. |
| `d6b0d379d52a` | c1 | ablate:wheat_tiles | **+10,532** | 7.8 | 20-0 | -21,781 | +8,841 | melon_floor 150→200, wheat_stock 0→5, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, MELON_PRICE_CUSHION 100→129, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→13, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 10 (gap +2,991 -> final +22,616); days 8-15 drivers: missed_water -35, sales_rev +3,744, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `a65aa7a26283` | v312 | ablate:open_cows | +14,798 | 3.4 | 9-1 | -12,652 | held_pass | melon_floor 150→200, min_hands 3→5, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, demand_share 0.5→0.45, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `8c6f5b00cc43` | c1 | ablate:wheat_stock | +14,567 | 11.4 | 10-0 | -2,495 | held_pass | melon_floor 150→100, open_wheat 7→8, early_hire_days 5→4, CROP_SWEEP_RADIUS 4→2, HERD_LAST_DAY 19→22, OPP_GROWTH 1.3→1.5, MAX_SHEEP 12→13 · blocks: crop_admission |
| `b779268453ef` | c1 | migrate | +12,886 | 10.7 | 10-0 | -1,568 | held_pass | melon_floor 150→100, open_wheat 7→8, early_hire_days 5→4, feed_spare_poor 0→1, fert_keep 0→1, wheat_sell_price 30→28, CROP_SWEEP_RADIUS 4→2 · blocks: crop_admission |
| `e4a45816755f` | queue | ablate:NEAR_RADIUS | +12,820 | 11.0 | 10-0 | -3,176 | held_pass | open_wheat 7→8, early_hire_days 5→4, fert_keep 0→1, CROP_SWEEP_RADIUS 4→2 · blocks: crop_admission |
| `bb56bdea4bf1` | c1 | crossover | +12,631 | 8.7 | 10-0 | -7,383 | held_pass | melon_floor 150→100, wheat_stock 0→2, open_wheat 7→8, early_hire_days 5→4, CROP_SWEEP_RADIUS 4→2, HERD_LAST_DAY 19→22, OPP_GROWTH 1.3→1.5, MAX_SHEEP 12→13 · blocks: crop_admission |
| `64476e04983d` | v312 | ablate:open_wheat | +11,849 | 6.1 | 10-0 | -16,943 | held_pass | wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `f8be9cdc3861` | v312 | ablate:wheat_tiles | +11,582 | 6.0 | 10-0 | -17,834 | held_pass | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `974a722e40d2` | queue | ablate:MAX_SHEEP | +11,545 | 5.7 | 10-0 | -14,402 | held_pass | harvest_min 2→1, open_wheat 7→8, early_hire_days 5→7, HERD_LAST_DAY 19→20 · blocks: crop_admission |
| `948f7f7debac` | c1 | ablate:fert_keep | +11,468 | 7.3 | 10-0 | -7,529 | held_pass | melon_floor 150→100, wheat_stock 0→2, open_wheat 7→8, early_hire_days 5→4, fert_keep 0→1, CROP_SWEEP_RADIUS 4→2, HERD_LAST_DAY 19→22, OPP_GROWTH 1.3→1.5, MAX_SHEEP 12→13 · blocks: crop_admission |
| `fb47561f2293` | queue | ablate:open_wheat | +11,303 | 7.5 | 10-0 | -3,176 | held_pass | open_wheat 7→8, early_hire_days 5→3, fert_keep 0→1, CROP_SWEEP_RADIUS 4→2, STRAW_CUTOFF 17→18 · blocks: crop_admission |
| `2ee1ba1b5941` | v312 | ablate:CROP_SWEEP_RADIUS | +11,298 | 5.9 | 10-0 | -17,006 | held_pass | melon_floor 150→200, wheat_per_animal 0.0→0.1, wheat_cap 18→21, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→37, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `2d6808e383d0` | c1 | ablate:min_hands | +11,279 | 7.2 | 10-0 | -1,568 | alive | melon_floor 150→0, open_wheat 7→8, early_hire_days 5→3, fert_keep 0→1, CROP_SWEEP_RADIUS 4→2, STRAW_CUTOFF 17→16 · blocks: crop_admission |
| `b1b4de2e23d7` | v312 | ablate:ROUTE_LEN | +11,227 | 7.4 | 10-0 | -7,017 | held_pass | load_per_hand 20→18, wheat_cap 18→21, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `2ed37e718be7` | queue | ablate:fert_keep | +11,161 | 5.6 | 10-0 | -13,859 | held_pass | open_wheat 7→8, early_hire_days 5→4 · blocks: crop_admission |
| `5eeb0745fc2d` | queue | ablate:NEAR_RADIUS | +11,160 | 5.6 | 10-0 | -12,708 | held_pass | melon_floor 150→100, open_wheat 7→8 · blocks: crop_admission |

## Islands (best dev margin, population size)

- c1: best +14,567 (`8c6f5b00cc43`), n=1297
- queue: best +12,820 (`e4a45816755f`), n=1455
- v312: best +14,798 (`a65aa7a26283`), n=1345
- wide: best +10,939 (`daba421dc7ec`), n=981

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 17,155 | 74 | 100 | 74: -3,300 (33), 145: -4,073 (6), 114: -6,014 (50), 98: -7,098 (27), 120: -8,038 (12), 127: -8,313 (154), 72: -8,331 (3), 134: -8,481 (6), 130: -8,967 (10), 56: -10,156 (3), 83: -10,350 (18), 131: -10,469 (14), 100: -10,906 (3031), 55: -11,189 (2), 117: -11,431 (13), 143: -11,498 (13), 105: -11,882 (23), 129: -11,960 (46), 69: -12,080 (4), 59: -12,362 (6), 121: -12,465 (29), 68: -12,619 (22), 124: -12,637 (6), 112: -12,701 (10), 116: -12,715 (101), 58: -12,876 (3), 133: -13,001 (91), 88: -13,022 (23), 67: -13,144 (165), 97: -13,182 (22), 61: -13,337 (6), 103: -13,370 (12), 64: -13,386 (9), 51: -13,435 (3), 82: -13,448 (23), 91: -13,702 (18), 85: -13,755 (46), 92: -13,782 (165), 101: -13,828 (41), 96: -13,902 (66), 77: -13,908 (12), 95: -13,932 (24), 102: -13,949 (31), 135: -13,980 (9), 144: -14,072 (3), 78: -14,097 (9), 87: -14,118 (10), 53: -14,137 (2), 140: -14,183 (23), 118: -14,186 (12), 93: -14,238 (28), 126: -14,257 (8), 70: -14,394 (4), 89: -14,465 (20), 50: -14,503 (55), 75: -14,517 (11), 86: -14,548 (7), 150: -14,557 (67), 137: -14,634 (5), 54: -14,657 (6), 62: -14,700 (34), 90: -14,728 (60), 94: -14,799 (11), 109: -14,815 (12), 104: -14,854 (3), 115: -14,901 (20), 110: -14,989 (10), 132: -15,092 (10), 141: -15,224 (2), 113: -15,299 (7), 65: -15,432 (3), 66: -15,472 (14), 106: -15,485 (10), 119: -15,576 (7), 123: -15,592 (20), 128: -15,612 (3), 76: -15,646 (8), 108: -15,695 (9), 125: -15,710 (15), 122: -16,061 (6), 63: -16,202 (7), 107: -16,267 (18), 73: -16,399 (7), 138: -16,447 (2), 136: -16,482 (4), 84: -16,741 (7), 142: -16,916 (3), 80: -16,944 (8), 79: -16,976 (15), 111: -17,006 (22), 81: -17,255 (12), 99: -17,306 (9), 139: -17,379 (7), 71: -18,230 (2), 148: -20,210 (4), 60: -20,456 (2) |
| wheat_stock | 16,235 | 21 | 0 | 21: -6,697 (11), 7: -9,195 (41), 16: -10,480 (13), 5: -10,818 (90), 2: -11,071 (146), 0: -11,351 (3820), 12: -11,795 (65), 10: -12,192 (103), 24: -12,364 (2), 1: -12,402 (96), 14: -13,071 (20), 13: -13,290 (26), 6: -13,343 (174), 17: -13,358 (20), 19: -13,425 (2), 4: -13,443 (243), 32: -13,668 (2), 20: -13,890 (3), 11: -13,969 (71), 18: -14,623 (2), 3: -15,517 (38), 9: -15,518 (25), 8: -16,095 (15), 15: -16,315 (13), 35: -17,198 (2), 27: -17,367 (4), 33: -18,492 (3), 40: -18,678 (8), 22: -19,282 (4), 23: -20,979 (3), 28: -21,021 (6), 29: -21,537 (2), 38: -22,932 (2) |
| demand_share | 13,543 | 0.75 | 0.5 | 0.75: -9,971 (32), 0.5: -10,377 (2577), 0.7: -12,366 (67), 0.45: -12,405 (1217), 0.55: -12,509 (460), 0.4: -12,529 (122), 0.6: -14,649 (301), 0.65: -14,827 (55), 0.35: -14,865 (61), 0.8: -15,896 (17), 0.3: -16,039 (150), 0.95: -19,830 (6), 0.85: -22,635 (5), 1.0: -23,514 (7) |
| wheat_sell_price | 12,825 | 28 | 30 | 28: -8,660 (141), 27: -9,212 (326), 50: -9,337 (139), 38: -10,137 (21), 37: -10,227 (61), 44: -10,615 (10), 47: -10,956 (3), 30: -11,653 (3189), 31: -11,746 (132), 25: -12,291 (306), 29: -12,631 (141), 35: -13,056 (86), 32: -13,219 (48), 26: -13,879 (247), 36: -14,679 (64), 33: -14,787 (48), 41: -15,431 (8), 34: -15,547 (56), 42: -15,904 (3), 40: -16,786 (11), 39: -17,145 (17), 43: -17,320 (5), 45: -18,332 (8), 46: -20,201 (6), 48: -21,485 (2) |
| load_per_hand | 12,029 | 20 | 20 | 20: -10,196 (2445), 19: -11,386 (491), 18: -12,064 (297), 22: -12,647 (104), 16: -12,961 (737), 21: -13,412 (117), 15: -13,516 (537), 13: -13,745 (30), 17: -14,234 (118), 23: -14,313 (50), 14: -16,504 (31), 24: -17,193 (20), 25: -19,448 (12), 12: -19,663 (67), 26: -22,225 (22) |
| MAX_HANDS | 11,721 | 13 | 13 | 13: -10,848 (3222), 11: -12,003 (186), 16: -12,678 (69), 12: -12,996 (1155), 15: -13,525 (154), 14: -13,689 (208), 10: -15,545 (49), 9: -19,951 (20), 8: -22,569 (15) |
| wheat_tiles | 11,458 | 3 | 0 | 3: -10,917 (105), 0: -11,502 (4378), 2: -12,872 (185), 1: -13,298 (347), 4: -13,575 (40), 5: -17,929 (10), 6: -20,657 (7), 8: -22,375 (5) |
| ROUTE_LEN | 11,063 | 3 | 3 | 3: -11,412 (4423), 2: -12,764 (394), 4: -14,553 (236), 5: -22,475 (25) |
| wheat_per_animal | 10,495 | 0.1 | 0.0 | 0.1: -9,705 (632), 0.0: -11,504 (3478), 0.2: -12,962 (523), 0.5: -13,059 (111), 0.6: -14,072 (46), 0.8: -14,259 (7), 0.3: -14,835 (192), 0.9: -15,766 (12), 0.4: -16,566 (57), 1.2: -19,061 (8), 0.7: -20,174 (8), 1.0: -20,200 (3) |
| MAX_SHEEP | 10,037 | 12 | 12 | 12: -10,024 (1135), 11: -11,547 (377), 14: -11,968 (2428), 9: -12,287 (62), 13: -12,776 (807), 10: -12,846 (228), 6: -15,040 (6), 8: -17,232 (13), 4: -17,470 (9), 7: -17,967 (10), 5: -20,061 (3) |
| MELON_MAX_TILES | 9,376 | 41 | 40 | 41: -9,508 (934), 40: -11,058 (1667), 32: -11,288 (29), 50: -11,325 (547), 23: -11,387 (5), 44: -11,545 (50), 47: -11,779 (93), 31: -12,108 (89), 37: -12,761 (172), 46: -12,935 (25), 35: -12,973 (36), 26: -13,094 (5), 45: -13,470 (48), 34: -13,510 (192), 48: -13,654 (20), 38: -13,659 (166), 43: -13,721 (709), 49: -13,984 (53), 27: -14,168 (8), 42: -14,283 (49), 39: -14,285 (47), 36: -14,385 (37), 22: -14,648 (10), 30: -14,776 (22), 33: -14,870 (26), 29: -15,153 (10), 28: -17,627 (12), 21: -18,762 (2), 20: -18,836 (7), 25: -18,884 (7) |
| open_melons | 8,902 | 8 | 8 | 8: -11,002 (2099), 5: -11,077 (1116), 10: -11,871 (308), 7: -12,360 (377), 6: -12,379 (579), 11: -12,845 (54), 9: -13,330 (258), 12: -14,418 (38), 4: -15,183 (227), 14: -19,484 (10), 13: -19,904 (12) |
| max_animals | 7,928 | 20 | 20 | 20: -11,135 (2893), 17: -11,812 (1421), 16: -12,159 (123), 18: -12,650 (181), 19: -13,981 (303), 13: -14,179 (14), 15: -14,610 (89), 14: -17,728 (23), 10: -18,139 (13), 11: -18,241 (7), 12: -19,063 (11) |
| CROP_SWEEP_LEN | 7,799 | 6 | 6 | 6: -11,237 (3463), 3: -11,331 (136), 7: -12,068 (637), 5: -12,353 (559), 4: -13,445 (108), 8: -16,773 (122), 9: -17,436 (34), 10: -19,036 (19) |
| wheat_cap | 7,771 | 18 | 18 | 18: -10,127 (1773), 15: -10,198 (757), 14: -11,125 (49), 21: -11,138 (122), 17: -11,977 (149), 23: -12,158 (83), 12: -12,462 (47), 20: -12,491 (880), 24: -13,627 (32), 22: -13,889 (91), 19: -13,918 (240), 13: -14,171 (227), 16: -14,211 (356), 25: -14,652 (138), 11: -15,274 (24), 10: -15,403 (14), 8: -15,921 (18), 7: -16,526 (26), 6: -16,637 (7), 5: -17,612 (30), 9: -17,898 (15) |
| opening | 7,706 | frontier | frontier | frontier: -10,453 (4245), v312: -18,159 (833) |
| open_sheep | 7,137 | 2 | 2 | 2: -11,267 (4635), 1: -15,337 (238), 3: -17,095 (110), 0: -18,403 (95) |
| CROP_SWEEP_RADIUS | 6,395 | 4 | 4 | 4: -8,057 (1298), 5: -10,853 (166), 3: -12,528 (1672), 2: -13,523 (1907), 6: -14,452 (35) |
| OPP_GROWTH | 6,202 | 1.3 | 1.3 | 1.3: -9,818 (2231), 1.6: -10,823 (129), 1.4: -11,987 (586), 1.1: -12,424 (310), 1.5: -12,659 (460), 1.2: -14,034 (975), 1.7: -14,212 (150), 1.8: -14,403 (68), 1.0: -16,020 (169) |
| open_wheat | 5,592 | 3 | 7 | 3: -8,954 (44), 7: -9,773 (782), 9: -11,434 (1727), 4: -11,596 (52), 8: -11,759 (1713), 5: -14,171 (223), 6: -14,539 (96), 10: -14,546 (441) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=186)
- (13, 3, 6): +14,567 (n=307)
- (7, 3, 5): +11,849 (n=52)
- (15, 3, 6): +11,582 (n=164)
- (10, 3, 6): +11,227 (n=475)
- (8, 3, 6): +11,158 (n=583)
- (17, 3, 6): +10,971 (n=141)
- (11, 3, 6): +10,963 (n=256)
- (17, 4, 6): +10,740 (n=9)
- (9, 4, 6): +10,652 (n=198)
- (16, 3, 6): +10,603 (n=57)
- (7, 4, 6): +10,358 (n=28)
- (8, 3, 4): +10,272 (n=87)
- (12, 4, 6): +10,123 (n=133)
- (9, 3, 6): +9,773 (n=624)

_Generated 2026-09-05 00:13. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._