# Evolution run 20260905-001716

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.07 h · candidates evaluated this run: 914 · games 30,138 (14,586/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 43 | 86 |
| dead_pattern | 186 | 372 |
| dead_smoke | 80 | 640 |
| alive | 605 | 29040 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 5683 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=1457
- queue: best +12,820 (`e4a45816755f`), n=1612
- v312: best +14,798 (`a65aa7a26283`), n=1498
- wide: best +10,939 (`daba421dc7ec`), n=1116

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 17,148 | 74 | 100 | 74: -3,809 (34), 145: -4,073 (6), 114: -6,322 (52), 98: -7,098 (27), 127: -8,579 (158), 120: -8,666 (13), 130: -8,967 (10), 57: -9,192 (2), 72: -9,783 (4), 56: -10,156 (3), 134: -10,237 (7), 83: -10,350 (18), 131: -10,868 (15), 100: -11,114 (3260), 124: -11,625 (7), 117: -11,672 (14), 143: -11,864 (17), 105: -11,882 (23), 129: -11,960 (46), 69: -12,322 (5), 59: -12,362 (6), 116: -12,739 (108), 141: -12,814 (3), 68: -12,923 (23), 133: -13,013 (138), 112: -13,019 (11), 97: -13,091 (33), 82: -13,105 (30), 67: -13,111 (191), 88: -13,151 (48), 121: -13,151 (39), 61: -13,337 (6), 144: -13,366 (4), 92: -13,431 (247), 58: -13,434 (5), 78: -13,671 (10), 85: -13,682 (52), 77: -13,732 (14), 102: -13,736 (35), 87: -13,751 (11), 86: -13,762 (10), 118: -13,765 (15), 101: -13,828 (41), 103: -13,897 (16), 96: -13,917 (72), 126: -13,922 (9), 140: -13,939 (25), 91: -13,961 (20), 94: -14,097 (13), 53: -14,137 (2), 147: -14,181 (3), 93: -14,238 (28), 55: -14,288 (3), 132: -14,289 (12), 75: -14,314 (12), 70: -14,394 (4), 64: -14,442 (11), 95: -14,512 (30), 110: -14,598 (12), 89: -14,626 (24), 54: -14,657 (6), 150: -14,724 (72), 62: -14,725 (38), 90: -14,728 (60), 135: -14,794 (11), 50: -14,814 (82), 109: -14,815 (12), 80: -14,893 (11), 115: -14,996 (24), 113: -15,002 (8), 106: -15,229 (13), 66: -15,244 (15), 51: -15,361 (6), 65: -15,432 (3), 119: -15,543 (10), 123: -15,592 (20), 128: -15,612 (3), 125: -15,631 (16), 76: -15,646 (8), 108: -15,695 (9), 137: -15,793 (7), 107: -16,025 (19), 122: -16,061 (6), 63: -16,202 (7), 104: -16,273 (5), 71: -16,298 (3), 142: -16,375 (4), 73: -16,399 (7), 136: -16,482 (4), 60: -16,645 (7), 84: -16,862 (8), 138: -16,947 (4), 79: -17,021 (16), 99: -17,306 (9), 139: -17,379 (7), 81: -17,645 (13), 111: -17,864 (26), 148: -20,957 (5) |
| demand_share | 14,970 | 0.75 | 0.5 | 0.75: -10,544 (36), 0.5: -10,574 (2765), 0.55: -12,617 (547), 0.45: -12,622 (1469), 0.7: -12,648 (70), 0.4: -12,883 (139), 0.65: -14,639 (60), 0.6: -14,701 (315), 0.35: -15,032 (70), 0.3: -16,351 (172), 0.8: -17,037 (19), 0.95: -19,830 (6), 1.0: -21,739 (8), 0.85: -22,635 (5), 0.9: -25,514 (2) |
| wheat_stock | 14,344 | 21 | 0 | 21: -6,697 (11), 7: -10,125 (49), 5: -10,965 (95), 2: -11,276 (155), 16: -11,474 (16), 0: -11,593 (4251), 12: -11,960 (74), 18: -12,022 (5), 10: -12,126 (116), 1: -12,728 (107), 17: -12,891 (29), 13: -13,483 (33), 4: -13,494 (273), 6: -13,522 (201), 32: -13,668 (2), 20: -13,890 (3), 14: -13,930 (25), 11: -13,963 (83), 24: -14,203 (3), 19: -14,592 (4), 3: -15,045 (46), 9: -15,320 (26), 8: -15,808 (16), 15: -16,315 (13), 35: -17,198 (2), 27: -17,367 (4), 40: -17,857 (9), 26: -18,262 (2), 33: -18,492 (3), 29: -19,018 (3), 22: -19,282 (4), 38: -19,458 (3), 23: -20,979 (3), 28: -21,041 (9) |
| wheat_sell_price | 12,313 | 28 | 30 | 28: -9,172 (154), 50: -9,520 (144), 27: -9,652 (375), 44: -10,615 (10), 38: -10,617 (24), 47: -10,956 (3), 37: -11,292 (72), 30: -11,816 (3485), 31: -11,878 (142), 25: -12,554 (360), 29: -12,704 (155), 32: -13,432 (58), 35: -13,528 (99), 26: -13,779 (344), 36: -14,778 (69), 33: -15,178 (55), 34: -15,554 (61), 41: -15,892 (13), 42: -15,904 (3), 43: -15,975 (6), 40: -16,977 (14), 39: -17,461 (21), 45: -18,332 (8), 46: -20,201 (6), 48: -21,485 (2) |
| load_per_hand | 12,222 | 20 | 20 | 20: -10,441 (2640), 19: -11,591 (543), 18: -12,296 (371), 22: -12,802 (107), 16: -13,024 (809), 15: -13,617 (673), 21: -13,746 (125), 13: -13,989 (33), 23: -14,142 (56), 17: -14,149 (147), 14: -15,772 (37), 24: -16,783 (26), 25: -18,978 (14), 12: -19,393 (76), 26: -22,663 (26) |
| MAX_HANDS | 11,990 | 13 | 13 | 13: -11,108 (3492), 11: -12,193 (219), 16: -12,873 (71), 12: -13,000 (1406), 14: -13,699 (227), 15: -13,704 (167), 10: -16,097 (59), 9: -19,816 (24), 8: -23,098 (18) |
| ROUTE_LEN | 11,370 | 3 | 3 | 3: -11,616 (4949), 2: -13,168 (439), 4: -14,867 (266), 5: -22,986 (29) |
| wheat_tiles | 10,739 | 3 | 0 | 3: -11,357 (115), 0: -11,747 (4917), 2: -13,021 (210), 1: -13,388 (373), 4: -13,575 (40), 5: -17,851 (13), 6: -20,603 (8), 8: -22,096 (6) |
| wheat_per_animal | 10,112 | 0.1 | 0.0 | 0.1: -10,089 (675), 0.0: -11,712 (3903), 0.2: -13,102 (608), 0.5: -13,425 (125), 0.6: -14,760 (56), 0.3: -14,837 (208), 0.8: -15,073 (8), 0.9: -15,766 (12), 0.4: -16,322 (67), 1.2: -19,061 (8), 0.7: -19,182 (9), 1.0: -20,200 (3) |
| MAX_SHEEP | 9,782 | 12 | 12 | 12: -10,279 (1209), 11: -11,760 (393), 14: -12,212 (2810), 9: -12,446 (67), 10: -12,842 (249), 13: -12,862 (908), 6: -15,818 (7), 8: -16,808 (17), 4: -17,470 (9), 7: -18,448 (11), 5: -20,061 (3) |
| open_melons | 9,128 | 8 | 8 | 8: -11,246 (2375), 5: -11,374 (1239), 10: -11,996 (316), 7: -12,507 (405), 6: -12,610 (666), 9: -13,407 (311), 11: -13,531 (61), 12: -14,485 (39), 4: -15,323 (245), 14: -19,484 (10), 13: -20,374 (16) |
| MELON_MAX_TILES | 8,942 | 41 | 40 | 41: -9,942 (1038), 40: -11,192 (1761), 32: -11,362 (31), 44: -11,681 (52), 50: -11,694 (579), 23: -12,152 (7), 31: -12,174 (91), 47: -12,291 (119), 37: -12,798 (186), 45: -13,303 (78), 26: -13,510 (7), 35: -13,540 (41), 48: -13,577 (21), 43: -13,595 (918), 38: -13,621 (180), 34: -13,673 (227), 46: -13,881 (29), 49: -13,945 (56), 42: -14,047 (57), 27: -14,168 (8), 39: -14,454 (51), 36: -14,538 (42), 22: -14,648 (10), 30: -14,718 (25), 33: -14,831 (27), 29: -15,153 (10), 28: -17,592 (13), 21: -17,764 (3), 20: -18,229 (8), 25: -18,884 (7) |
| opening | 7,601 | frontier | frontier | frontier: -10,672 (4730), v312: -18,272 (953) |
| max_animals | 7,596 | 20 | 20 | 20: -11,321 (3124), 17: -12,104 (1647), 16: -12,504 (144), 18: -13,026 (213), 19: -13,963 (338), 15: -14,145 (141), 13: -14,961 (17), 14: -17,126 (25), 10: -17,508 (14), 11: -18,064 (8), 12: -18,917 (12) |
| CROP_SWEEP_LEN | 7,574 | 6 | 6 | 6: -11,461 (3881), 3: -11,669 (149), 7: -12,359 (728), 5: -12,495 (601), 4: -13,713 (124), 8: -16,905 (143), 9: -17,969 (38), 10: -19,036 (19) |
| CROP_SWEEP_RADIUS | 7,039 | 4 | 4 | 4: -8,290 (1340), 5: -11,001 (173), 3: -12,707 (1880), 2: -13,501 (2251), 6: -15,329 (39) |
| wheat_cap | 6,992 | 18 | 18 | 18: -10,351 (1876), 15: -10,534 (830), 14: -11,460 (54), 21: -11,659 (134), 17: -11,938 (155), 23: -12,137 (107), 20: -12,591 (961), 12: -12,649 (58), 24: -13,747 (38), 19: -13,890 (259), 16: -13,898 (520), 13: -13,984 (264), 22: -14,355 (111), 25: -14,653 (156), 11: -15,155 (30), 10: -16,336 (17), 7: -16,607 (29), 6: -16,637 (7), 8: -16,688 (22), 5: -17,218 (35), 9: -17,343 (20) |
| open_sheep | 6,969 | 2 | 2 | 2: -11,476 (5171), 1: -15,668 (278), 3: -17,459 (127), 0: -18,445 (107) |
| OPP_GROWTH | 5,685 | 1.3 | 1.3 | 1.3: -10,053 (2356), 1.6: -11,069 (135), 1.4: -12,061 (626), 1.1: -12,669 (375), 1.5: -12,772 (517), 1.2: -13,980 (1195), 1.7: -13,985 (174), 1.8: -14,252 (89), 1.0: -15,737 (216) |
| open_wheat | 5,081 | 3 | 7 | 3: -9,843 (48), 7: -10,011 (812), 9: -11,681 (1945), 4: -11,767 (56), 8: -11,937 (1952), 5: -14,110 (251), 10: -14,591 (513), 6: -14,924 (106) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=217)
- (13, 3, 6): +14,567 (n=346)
- (7, 3, 5): +11,849 (n=53)
- (15, 3, 6): +11,582 (n=177)
- (10, 3, 6): +11,227 (n=518)
- (8, 3, 6): +11,158 (n=681)
- (17, 3, 6): +10,971 (n=149)
- (11, 3, 6): +10,963 (n=296)
- (17, 4, 6): +10,740 (n=9)
- (9, 4, 6): +10,652 (n=214)
- (16, 3, 6): +10,603 (n=63)
- (7, 4, 6): +10,358 (n=31)
- (8, 3, 4): +10,272 (n=98)
- (12, 4, 6): +10,123 (n=141)
- (9, 3, 6): +9,773 (n=680)

_Generated 2026-09-05 02:21. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._