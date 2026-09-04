# Evolution run 20260904-155053

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.01 h · candidates evaluated this run: 476 · games 18,328 (9,099/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 20 | 40 |
| dead_smoke | 90 | 720 |
| alive | 366 | 17568 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 3521 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=903
- queue: best +12,820 (`e4a45816755f`), n=967
- v312: best +14,798 (`a65aa7a26283`), n=966
- wide: best +10,939 (`daba421dc7ec`), n=685

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 20,231 | 74 | 100 | 74: -507 (26), 145: -2,153 (5), 114: -4,422 (44), 72: -5,795 (2), 120: -5,851 (8), 98: -5,884 (22), 134: -6,719 (4), 83: -7,173 (11), 131: -7,549 (9), 130: -8,012 (8), 127: -8,044 (148), 100: -9,748 (2250), 55: -11,189 (2), 59: -11,288 (3), 105: -11,370 (16), 129: -11,761 (40), 117: -11,947 (11), 78: -12,289 (6), 116: -12,454 (86), 86: -12,462 (5), 112: -12,523 (9), 67: -12,576 (52), 133: -12,726 (42), 104: -12,764 (2), 124: -12,838 (4), 106: -12,841 (6), 97: -12,867 (13), 91: -12,919 (12), 89: -13,049 (8), 135: -13,181 (8), 101: -13,291 (33), 85: -13,374 (33), 69: -13,405 (3), 96: -13,637 (43), 77: -13,711 (8), 50: -13,820 (31), 75: -13,823 (8), 62: -13,849 (13), 140: -13,891 (19), 95: -13,979 (5), 144: -14,072 (3), 80: -14,082 (4), 103: -14,083 (7), 65: -14,104 (2), 143: -14,237 (4), 102: -14,382 (9), 150: -14,386 (53), 92: -14,413 (36), 90: -14,485 (44), 87: -14,591 (5), 93: -14,721 (24), 88: -14,727 (7), 115: -14,738 (18), 109: -14,819 (10), 94: -14,951 (10), 121: -15,076 (7), 118: -15,218 (10), 68: -15,252 (4), 110: -15,331 (7), 82: -15,423 (4), 123: -15,480 (19), 126: -15,531 (5), 119: -15,576 (7), 73: -15,933 (6), 63: -16,036 (4), 107: -16,060 (14), 125: -16,061 (11), 66: -16,165 (12), 132: -16,307 (8), 138: -16,447 (2), 137: -16,449 (3), 84: -16,741 (7), 139: -16,742 (4), 79: -16,945 (12), 81: -17,043 (11), 113: -17,057 (5), 122: -17,058 (5), 108: -17,351 (5), 76: -17,430 (6), 111: -17,448 (19), 99: -17,650 (5), 128: -18,034 (2), 136: -19,272 (3), 60: -20,456 (2), 148: -20,614 (3), 64: -20,739 (2) |
| wheat_stock | 16,379 | 21 | 0 | 21: -5,788 (10), 16: -6,308 (7), 7: -7,748 (33), 5: -9,918 (74), 0: -10,210 (2686), 2: -10,485 (126), 10: -11,173 (57), 13: -11,572 (18), 12: -11,656 (51), 20: -11,897 (2), 14: -12,474 (16), 1: -12,511 (61), 4: -13,344 (153), 6: -13,496 (83), 11: -13,847 (51), 17: -14,133 (3), 3: -14,785 (28), 9: -15,309 (16), 15: -15,324 (7), 8: -16,348 (11), 35: -17,198 (2), 40: -17,215 (5), 28: -18,108 (3), 27: -18,285 (2), 23: -19,111 (2), 22: -19,282 (4), 33: -22,166 (2) |
| demand_share | 16,080 | 0.75 | 0.5 | 0.75: -8,540 (25), 0.5: -9,492 (2082), 0.7: -9,749 (46), 0.8: -10,428 (8), 0.45: -11,399 (635), 0.4: -11,785 (94), 0.55: -12,363 (274), 0.35: -14,157 (37), 0.6: -14,495 (165), 0.3: -15,153 (107), 0.65: -15,318 (33), 0.95: -19,830 (6), 1.0: -23,314 (6), 0.85: -24,619 (2) |
| wheat_tiles | 15,715 | 3 | 0 | 3: -8,945 (72), 0: -10,423 (3027), 4: -11,068 (25), 2: -12,363 (135), 1: -12,877 (250), 5: -18,807 (5), 8: -23,634 (3), 6: -24,660 (3) |
| wheat_sell_price | 14,135 | 27 | 30 | 27: -7,350 (227), 28: -7,492 (114), 38: -8,424 (17), 50: -8,459 (121), 37: -8,710 (36), 31: -10,377 (78), 44: -10,615 (10), 30: -10,724 (2277), 47: -10,956 (3), 25: -11,001 (206), 29: -11,584 (99), 35: -12,298 (57), 32: -12,511 (32), 36: -14,315 (46), 33: -14,435 (31), 41: -14,598 (5), 26: -15,065 (81), 34: -15,448 (45), 43: -15,960 (4), 40: -16,177 (7), 39: -17,593 (13), 46: -18,796 (4), 45: -19,469 (5), 48: -21,485 (2) |
| load_per_hand | 13,163 | 20 | 20 | 20: -9,062 (1846), 19: -10,271 (325), 22: -11,524 (71), 18: -11,530 (204), 16: -12,215 (472), 13: -12,489 (18), 21: -13,143 (95), 15: -13,205 (294), 23: -14,024 (38), 17: -14,516 (67), 14: -15,878 (17), 24: -17,438 (16), 25: -18,583 (8), 12: -20,303 (28), 26: -22,225 (22) |
| MAX_HANDS | 12,236 | 13 | 13 | 13: -9,799 (2375), 11: -10,864 (106), 16: -11,318 (53), 15: -11,473 (110), 12: -12,480 (667), 14: -13,105 (153), 10: -14,380 (30), 9: -20,289 (13), 8: -22,035 (14) |
| wheat_per_animal | 12,057 | 0.1 | 0.0 | 0.1: -8,546 (500), 0.0: -10,534 (2461), 0.5: -11,429 (57), 0.2: -12,345 (286), 0.6: -12,788 (27), 0.3: -14,253 (126), 0.8: -15,252 (6), 0.9: -15,646 (5), 0.4: -16,502 (39), 1.2: -20,014 (7), 0.7: -20,604 (6) |
| ROUTE_LEN | 11,944 | 3 | 3 | 3: -10,391 (3049), 2: -11,533 (275), 4: -13,457 (184), 5: -22,334 (13) |
| MELON_MAX_TILES | 11,356 | 41 | 40 | 41: -8,396 (743), 40: -9,970 (1267), 44: -10,050 (37), 50: -10,399 (430), 47: -10,601 (55), 31: -10,717 (62), 32: -10,811 (23), 45: -11,177 (18), 26: -11,379 (4), 23: -11,387 (5), 37: -12,433 (118), 35: -12,749 (26), 39: -13,174 (32), 38: -13,429 (128), 34: -13,597 (103), 42: -13,758 (30), 46: -13,874 (11), 43: -14,016 (297), 48: -14,547 (11), 49: -14,582 (42), 27: -14,604 (7), 33: -15,226 (19), 30: -15,232 (7), 29: -15,539 (4), 36: -15,608 (15), 22: -15,686 (7), 28: -16,752 (8), 25: -18,985 (6), 20: -19,752 (5) |
| MAX_SHEEP | 10,362 | 12 | 12 | 12: -8,691 (893), 11: -10,593 (285), 9: -10,955 (46), 14: -10,960 (1586), 4: -10,967 (3), 10: -12,434 (140), 13: -12,443 (548), 6: -14,949 (4), 8: -18,075 (7), 7: -19,052 (8) |
| max_animals | 10,272 | 20 | 20 | 20: -10,096 (2195), 17: -10,657 (851), 16: -11,387 (70), 18: -12,197 (119), 19: -13,687 (200), 13: -13,907 (10), 15: -14,962 (43), 11: -17,226 (4), 14: -18,326 (14), 10: -19,253 (9), 12: -20,368 (6) |
| open_melons | 10,144 | 10 | 8 | 10: -9,575 (213), 5: -9,929 (788), 8: -9,960 (1493), 6: -11,385 (352), 7: -11,874 (284), 11: -12,267 (42), 9: -13,340 (158), 12: -14,151 (19), 4: -14,755 (155), 13: -18,657 (8), 14: -19,718 (9) |
| wheat_cap | 8,618 | 15 | 18 | 15: -8,620 (537), 18: -8,819 (1352), 14: -9,994 (37), 21: -10,413 (103), 23: -11,163 (53), 17: -11,322 (120), 20: -11,964 (595), 12: -12,073 (31), 22: -13,277 (44), 24: -13,446 (26), 8: -14,026 (11), 19: -14,198 (134), 13: -14,605 (150), 25: -14,715 (96), 16: -14,919 (152), 11: -15,108 (16), 10: -15,495 (5), 6: -16,821 (4), 7: -16,894 (23), 5: -16,912 (21), 9: -17,239 (11) |
| CROP_SWEEP_LEN | 8,519 | 3 | 6 | 3: -9,680 (104), 6: -10,159 (2401), 7: -10,752 (395), 5: -11,755 (424), 4: -12,420 (79), 8: -16,719 (78), 9: -17,266 (25), 10: -18,199 (15) |
| opening | 8,411 | frontier | frontier | frontier: -9,346 (2961), v312: -17,757 (560) |
| open_wheat | 7,895 | 3 | 7 | 3: -6,956 (36), 7: -8,203 (636), 9: -10,199 (1102), 4: -10,333 (40), 8: -11,047 (1243), 6: -13,889 (74), 5: -14,496 (144), 10: -14,850 (246) |
| open_sheep | 7,765 | 2 | 2 | 2: -10,157 (3203), 1: -14,990 (170), 3: -16,511 (81), 0: -17,922 (67) |
| OPP_GROWTH | 7,595 | 1.3 | 1.3 | 1.3: -8,555 (1745), 1.6: -9,802 (99), 1.1: -10,875 (162), 1.4: -11,439 (470), 1.5: -12,328 (353), 1.2: -14,457 (479), 1.7: -14,651 (86), 1.0: -16,084 (95), 1.8: -16,150 (32) |
| CROP_SWEEP_RADIUS | 7,323 | 4 | 4 | 4: -6,637 (1097), 5: -9,514 (130), 3: -11,958 (1118), 2: -13,363 (1147), 6: -13,960 (29) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=139)
- (13, 3, 6): +14,567 (n=235)
- (7, 3, 5): +11,849 (n=40)
- (15, 3, 6): +11,582 (n=114)
- (10, 3, 6): +11,227 (n=345)
- (8, 3, 6): +11,158 (n=377)
- (17, 3, 6): +10,971 (n=112)
- (11, 3, 6): +10,963 (n=149)
- (17, 4, 6): +10,740 (n=8)
- (9, 4, 6): +10,652 (n=136)
- (16, 3, 6): +10,603 (n=46)
- (7, 4, 6): +10,358 (n=21)
- (8, 3, 4): +10,272 (n=66)
- (12, 4, 6): +10,123 (n=105)
- (9, 3, 6): +9,773 (n=398)

_Generated 2026-09-04 17:51. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._