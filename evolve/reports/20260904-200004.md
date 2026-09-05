# Evolution run 20260904-200004

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.12 h · candidates evaluated this run: 1195 · games 30,026 (14,163/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 206 | 412 |
| dead_pattern | 263 | 526 |
| dead_smoke | 144 | 1152 |
| alive | 582 | 27936 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 4473 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=1138
- queue: best +12,820 (`e4a45816755f`), n=1294
- v312: best +14,798 (`a65aa7a26283`), n=1184
- wide: best +10,939 (`daba421dc7ec`), n=857

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 18,303 | 145 | 100 | 145: -2,153 (5), 74: -2,975 (32), 114: -5,279 (47), 72: -5,795 (2), 98: -6,909 (26), 56: -7,248 (2), 120: -7,604 (10), 130: -8,012 (8), 127: -8,206 (152), 134: -8,481 (6), 131: -9,304 (11), 83: -10,165 (15), 100: -10,632 (2790), 55: -11,189 (2), 117: -11,431 (13), 105: -11,621 (21), 129: -11,737 (43), 69: -12,080 (4), 143: -12,422 (9), 116: -12,536 (93), 112: -12,701 (10), 124: -12,745 (5), 133: -12,762 (52), 104: -12,764 (2), 59: -12,807 (5), 58: -12,876 (3), 67: -12,943 (118), 68: -13,153 (17), 54: -13,220 (4), 103: -13,237 (10), 77: -13,294 (9), 91: -13,405 (17), 78: -13,489 (7), 101: -13,555 (40), 85: -13,600 (43), 97: -13,616 (15), 96: -13,643 (54), 95: -13,707 (17), 75: -13,723 (10), 86: -13,855 (6), 121: -13,945 (12), 135: -13,980 (9), 82: -13,982 (11), 144: -14,072 (3), 65: -14,104 (2), 87: -14,118 (10), 53: -14,137 (2), 89: -14,169 (16), 118: -14,186 (12), 140: -14,249 (22), 92: -14,264 (101), 64: -14,293 (7), 102: -14,317 (25), 93: -14,370 (27), 70: -14,394 (4), 137: -14,436 (4), 88: -14,530 (10), 150: -14,544 (60), 50: -14,788 (39), 94: -14,799 (11), 109: -14,815 (12), 115: -14,839 (19), 90: -14,867 (56), 62: -14,967 (26), 126: -15,003 (6), 106: -15,129 (9), 132: -15,167 (9), 141: -15,224 (2), 113: -15,299 (7), 66: -15,472 (14), 107: -15,478 (15), 119: -15,576 (7), 123: -15,592 (20), 108: -15,598 (7), 139: -15,750 (5), 63: -15,832 (5), 61: -15,877 (3), 110: -15,988 (9), 125: -16,311 (14), 73: -16,399 (7), 138: -16,447 (2), 136: -16,482 (4), 76: -16,695 (7), 84: -16,741 (7), 142: -16,916 (3), 122: -17,058 (5), 111: -17,072 (21), 80: -17,102 (6), 79: -17,210 (13), 81: -17,255 (12), 99: -17,681 (6), 128: -18,034 (2), 148: -20,210 (4), 60: -20,456 (2) |
| wheat_stock | 16,235 | 21 | 0 | 21: -6,697 (11), 7: -8,917 (39), 16: -9,961 (12), 5: -10,487 (86), 2: -10,675 (136), 0: -11,065 (3389), 12: -11,585 (59), 10: -11,825 (82), 20: -11,897 (2), 24: -12,364 (2), 1: -12,726 (81), 14: -13,071 (20), 13: -13,126 (23), 17: -13,316 (8), 4: -13,357 (212), 6: -13,417 (136), 19: -13,425 (2), 11: -13,729 (62), 18: -14,623 (2), 3: -14,855 (33), 15: -15,324 (7), 9: -15,518 (22), 8: -16,173 (13), 35: -17,198 (2), 27: -17,367 (4), 40: -18,164 (7), 22: -19,282 (4), 23: -20,979 (3), 28: -21,367 (5), 33: -22,166 (2), 38: -22,932 (2) |
| demand_share | 13,949 | 0.75 | 0.5 | 0.75: -9,565 (29), 0.5: -10,092 (2390), 0.7: -11,677 (60), 0.45: -12,218 (975), 0.4: -12,371 (111), 0.55: -12,468 (374), 0.8: -14,174 (12), 0.35: -14,314 (51), 0.65: -14,726 (46), 0.6: -14,776 (279), 0.3: -15,707 (128), 0.95: -19,830 (6), 0.85: -23,193 (4), 1.0: -23,514 (7) |
| wheat_tiles | 13,124 | 3 | 0 | 3: -10,510 (92), 0: -11,220 (3857), 4: -12,661 (34), 2: -12,665 (160), 1: -13,143 (315), 5: -19,153 (7), 6: -23,326 (4), 8: -23,634 (3) |
| wheat_sell_price | 13,112 | 28 | 30 | 28: -8,373 (130), 27: -8,415 (274), 37: -8,791 (41), 50: -9,175 (134), 38: -9,759 (20), 44: -10,615 (10), 47: -10,956 (3), 30: -11,421 (2872), 31: -11,591 (121), 25: -11,821 (258), 29: -12,296 (125), 35: -12,849 (75), 32: -13,338 (44), 26: -14,441 (166), 33: -14,507 (40), 36: -14,657 (60), 41: -14,964 (7), 34: -15,460 (48), 40: -16,446 (9), 39: -17,286 (16), 43: -17,320 (5), 45: -18,506 (7), 46: -19,338 (5), 48: -21,485 (2) |
| load_per_hand | 12,394 | 20 | 20 | 20: -9,831 (2214), 19: -11,067 (437), 18: -11,794 (242), 22: -12,414 (95), 16: -12,812 (645), 21: -13,377 (106), 15: -13,513 (424), 13: -13,896 (27), 23: -14,298 (44), 17: -14,417 (102), 14: -16,546 (27), 24: -17,084 (18), 25: -19,448 (12), 12: -20,033 (58), 26: -22,225 (22) |
| MAX_HANDS | 11,994 | 13 | 13 | 13: -10,574 (2916), 11: -11,733 (148), 16: -12,317 (64), 12: -12,821 (938), 15: -13,275 (142), 14: -13,447 (192), 10: -15,043 (40), 9: -20,429 (18), 8: -22,569 (15) |
| ROUTE_LEN | 10,967 | 3 | 3 | 3: -11,164 (3902), 2: -12,326 (342), 4: -14,148 (211), 5: -22,131 (18) |
| wheat_per_animal | 10,864 | 0.1 | 0.0 | 0.1: -9,310 (586), 0.0: -11,219 (3064), 0.5: -12,805 (97), 0.2: -12,811 (426), 0.6: -13,970 (43), 0.3: -14,927 (173), 0.8: -15,252 (6), 0.9: -16,127 (9), 0.4: -16,688 (50), 1.2: -19,061 (8), 1.0: -19,164 (2), 0.7: -20,174 (8) |
| MELON_MAX_TILES | 10,691 | 41 | 40 | 41: -9,136 (857), 40: -10,831 (1555), 32: -10,836 (26), 50: -11,092 (520), 44: -11,328 (47), 47: -11,376 (73), 23: -11,387 (5), 31: -11,627 (80), 45: -12,713 (25), 37: -12,757 (159), 35: -12,944 (31), 26: -13,094 (5), 46: -13,248 (19), 38: -13,388 (143), 34: -13,487 (155), 30: -13,896 (18), 48: -13,904 (15), 39: -13,953 (42), 43: -14,027 (511), 49: -14,101 (48), 42: -14,304 (41), 36: -14,418 (28), 27: -14,604 (7), 33: -15,156 (23), 22: -15,344 (8), 29: -16,218 (6), 28: -16,616 (11), 25: -18,884 (7), 20: -19,827 (6) |
| MAX_SHEEP | 10,304 | 12 | 12 | 12: -9,721 (1054), 9: -11,362 (54), 11: -11,413 (360), 14: -11,695 (2098), 10: -12,655 (198), 13: -12,673 (673), 6: -15,040 (6), 4: -16,499 (7), 8: -17,232 (13), 7: -19,052 (8), 5: -20,025 (2) |
| open_melons | 9,704 | 8 | 8 | 8: -10,705 (1863), 5: -10,722 (988), 10: -11,612 (291), 6: -12,174 (483), 7: -12,233 (344), 11: -12,731 (50), 9: -13,326 (202), 12: -13,727 (34), 4: -14,963 (198), 14: -19,484 (10), 13: -20,408 (10) |
| max_animals | 9,665 | 20 | 20 | 20: -10,851 (2634), 17: -11,552 (1214), 16: -11,848 (95), 18: -12,310 (158), 19: -13,894 (257), 13: -14,179 (14), 15: -15,642 (53), 14: -17,384 (21), 11: -18,241 (7), 10: -18,864 (11), 12: -20,516 (9) |
| wheat_cap | 8,418 | 15 | 18 | 15: -9,738 (671), 18: -9,773 (1627), 14: -10,674 (44), 21: -10,965 (116), 17: -11,875 (140), 23: -11,891 (73), 20: -12,354 (786), 12: -12,470 (35), 22: -13,189 (64), 24: -13,450 (28), 19: -14,001 (209), 13: -14,347 (193), 16: -14,672 (249), 25: -14,824 (121), 11: -15,440 (22), 10: -15,875 (10), 8: -16,452 (17), 7: -16,525 (25), 5: -17,189 (24), 6: -17,393 (6), 9: -18,156 (13) |
| opening | 7,852 | frontier | frontier | frontier: -10,165 (3748), v312: -18,017 (725) |
| CROP_SWEEP_LEN | 7,487 | 3 | 6 | 3: -10,716 (120), 6: -10,949 (3037), 7: -11,831 (554), 5: -12,052 (511), 4: -13,309 (102), 8: -16,881 (105), 9: -17,464 (28), 10: -18,204 (16) |
| open_sheep | 7,236 | 2 | 2 | 2: -10,966 (4083), 1: -15,272 (201), 3: -16,974 (102), 0: -18,203 (87) |
| CROP_SWEEP_RADIUS | 6,608 | 4 | 4 | 4: -7,772 (1245), 5: -10,451 (155), 3: -12,369 (1458), 2: -13,499 (1583), 6: -14,380 (32) |
| OPP_GROWTH | 6,534 | 1.3 | 1.3 | 1.3: -9,473 (2069), 1.6: -10,633 (119), 1.4: -11,786 (548), 1.1: -12,036 (250), 1.5: -12,640 (418), 1.7: -14,221 (124), 1.2: -14,293 (762), 1.8: -15,180 (48), 1.0: -16,007 (135) |
| open_wheat | 5,905 | 3 | 7 | 3: -8,794 (42), 7: -9,552 (758), 9: -11,060 (1468), 4: -11,217 (49), 8: -11,527 (1513), 5: -14,229 (196), 6: -14,305 (85), 10: -14,698 (362) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=171)
- (13, 3, 6): +14,567 (n=276)
- (7, 3, 5): +11,849 (n=45)
- (15, 3, 6): +11,582 (n=144)
- (10, 3, 6): +11,227 (n=426)
- (8, 3, 6): +11,158 (n=497)
- (17, 3, 6): +10,971 (n=134)
- (11, 3, 6): +10,963 (n=206)
- (17, 4, 6): +10,740 (n=9)
- (9, 4, 6): +10,652 (n=180)
- (16, 3, 6): +10,603 (n=57)
- (7, 4, 6): +10,358 (n=24)
- (8, 3, 4): +10,272 (n=82)
- (12, 4, 6): +10,123 (n=124)
- (9, 3, 6): +9,773 (n=538)

_Generated 2026-09-04 22:07. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._