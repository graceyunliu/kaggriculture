# Evolution run 20260904-134610

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.00 h · candidates evaluated this run: 472 · games 18,244 (9,111/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 22 | 44 |
| dead_smoke | 85 | 680 |
| alive | 365 | 17520 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 3155 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=807
- queue: best +12,820 (`e4a45816755f`), n=867
- v312: best +14,798 (`a65aa7a26283`), n=872
- wide: best +10,939 (`daba421dc7ec`), n=609

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 24,591 | 145 | 100 | 145: +1,855 (4), 74: -507 (26), 114: -4,027 (43), 130: -5,163 (6), 72: -5,795 (2), 120: -5,851 (8), 98: -5,884 (22), 131: -6,046 (8), 134: -6,719 (4), 83: -7,173 (11), 127: -8,005 (147), 100: -9,362 (2064), 124: -9,404 (3), 121: -10,061 (2), 59: -11,288 (3), 135: -11,352 (3), 105: -11,370 (16), 129: -11,767 (39), 97: -11,824 (10), 117: -11,874 (10), 112: -12,020 (8), 116: -12,248 (79), 78: -12,289 (6), 91: -12,302 (10), 67: -12,305 (26), 133: -12,318 (33), 50: -12,608 (25), 77: -12,660 (7), 106: -12,841 (6), 140: -12,957 (13), 101: -13,089 (29), 96: -13,321 (37), 69: -13,405 (3), 85: -13,560 (30), 150: -13,562 (46), 92: -13,778 (20), 95: -13,979 (5), 87: -14,046 (3), 144: -14,072 (3), 80: -14,082 (4), 65: -14,104 (2), 93: -14,436 (21), 89: -14,473 (5), 94: -14,500 (9), 75: -14,643 (7), 90: -14,653 (34), 88: -14,727 (7), 115: -15,095 (17), 102: -15,137 (7), 118: -15,218 (10), 68: -15,252 (4), 73: -15,324 (5), 110: -15,331 (7), 123: -15,394 (18), 119: -15,576 (7), 103: -15,643 (3), 109: -15,672 (7), 137: -15,708 (2), 132: -15,741 (7), 143: -15,769 (3), 62: -15,808 (6), 107: -16,060 (14), 125: -16,061 (11), 66: -16,165 (12), 138: -16,447 (2), 122: -16,552 (4), 84: -16,741 (7), 126: -16,797 (3), 82: -16,844 (3), 79: -16,945 (12), 113: -17,057 (5), 108: -17,351 (5), 99: -17,422 (4), 76: -17,430 (6), 139: -17,675 (3), 111: -17,722 (16), 81: -17,903 (10), 128: -18,034 (2), 63: -18,295 (2), 136: -19,272 (3), 60: -20,456 (2), 64: -20,739 (2), 148: -22,736 (2) |
| demand_share | 18,426 | 0.75 | 0.5 | 0.75: -6,655 (22), 0.8: -8,415 (7), 0.7: -9,109 (40), 0.5: -9,155 (1944), 0.45: -10,824 (520), 0.4: -11,380 (84), 0.55: -12,281 (231), 0.35: -13,900 (34), 0.6: -14,500 (136), 0.3: -14,874 (96), 0.65: -15,177 (30), 0.95: -17,648 (4), 0.85: -24,619 (2), 1.0: -25,082 (4) |
| wheat_stock | 17,838 | 16 | 0 | 16: -4,328 (6), 21: -5,788 (10), 7: -7,629 (32), 5: -9,670 (71), 0: -9,716 (2410), 2: -10,264 (121), 10: -10,656 (48), 13: -11,071 (16), 12: -11,309 (48), 20: -11,897 (2), 14: -12,474 (16), 1: -12,527 (55), 6: -13,132 (62), 4: -13,592 (136), 11: -13,907 (40), 15: -14,047 (6), 17: -14,133 (3), 3: -14,849 (26), 9: -15,164 (13), 35: -17,198 (2), 8: -17,202 (9), 28: -18,108 (3), 40: -18,510 (4), 23: -19,111 (2), 22: -19,282 (4), 33: -22,166 (2) |
| wheat_tiles | 16,415 | 3 | 0 | 3: -8,245 (65), 0: -9,971 (2711), 4: -10,481 (22), 2: -12,083 (123), 1: -12,712 (223), 5: -19,193 (4), 8: -23,634 (3), 6: -24,660 (3) |
| wheat_sell_price | 14,769 | 37 | 30 | 37: -6,716 (29), 27: -7,029 (216), 28: -7,287 (111), 38: -7,312 (15), 50: -8,114 (116), 31: -9,275 (60), 44: -9,542 (9), 30: -10,367 (2053), 25: -10,611 (186), 47: -10,956 (3), 29: -10,968 (80), 35: -11,753 (45), 32: -12,695 (29), 33: -14,279 (29), 36: -14,437 (37), 41: -14,598 (5), 26: -14,635 (56), 34: -15,582 (44), 43: -15,960 (4), 40: -16,177 (7), 46: -17,175 (2), 39: -17,780 (12), 45: -17,975 (4), 48: -21,485 (2) |
| load_per_hand | 13,652 | 20 | 20 | 20: -8,726 (1721), 19: -9,759 (265), 22: -10,795 (59), 18: -11,229 (187), 16: -11,879 (408), 13: -12,138 (16), 15: -12,640 (236), 21: -12,942 (89), 23: -13,561 (33), 17: -14,091 (59), 14: -14,732 (13), 24: -17,438 (16), 25: -18,583 (8), 12: -20,168 (26), 26: -22,377 (19) |
| MAX_HANDS | 12,406 | 13 | 13 | 13: -9,407 (2168), 11: -10,421 (96), 16: -10,686 (48), 15: -11,164 (103), 12: -12,105 (552), 14: -12,736 (137), 10: -13,576 (26), 9: -20,094 (12), 8: -21,813 (13) |
| wheat_per_animal | 12,084 | 0.1 | 0.0 | 0.1: -7,929 (461), 0.0: -10,133 (2214), 0.5: -10,929 (46), 0.2: -12,104 (240), 0.6: -12,491 (23), 0.3: -14,000 (112), 0.8: -15,252 (6), 0.9: -15,646 (5), 0.4: -16,764 (37), 0.7: -19,491 (3), 1.2: -20,014 (7) |
| MELON_MAX_TILES | 11,808 | 41 | 40 | 41: -7,944 (685), 44: -9,244 (31), 40: -9,512 (1147), 32: -9,985 (20), 50: -10,027 (404), 31: -10,488 (55), 47: -10,591 (54), 45: -11,149 (16), 26: -11,379 (4), 23: -11,387 (5), 35: -12,092 (24), 37: -12,254 (102), 39: -13,011 (30), 38: -13,365 (115), 34: -13,583 (80), 42: -13,706 (27), 46: -13,874 (11), 43: -13,890 (224), 27: -14,402 (6), 49: -14,502 (39), 36: -14,747 (12), 48: -15,032 (10), 30: -15,232 (7), 33: -15,239 (18), 29: -15,539 (4), 22: -15,686 (7), 28: -16,907 (7), 25: -18,483 (5), 20: -19,752 (5) |
| max_animals | 11,335 | 20 | 20 | 20: -9,713 (2014), 17: -10,148 (730), 16: -10,933 (65), 18: -11,724 (106), 19: -13,397 (164), 13: -13,708 (9), 15: -14,774 (40), 11: -17,496 (3), 14: -18,838 (12), 12: -20,368 (6), 10: -21,048 (6) |
| ROUTE_LEN | 11,072 | 3 | 3 | 3: -9,955 (2721), 2: -11,248 (254), 4: -12,947 (169), 5: -21,026 (11) |
| MAX_SHEEP | 10,757 | 12 | 12 | 12: -8,295 (833), 11: -10,209 (261), 14: -10,487 (1381), 9: -10,728 (43), 4: -10,967 (3), 13: -12,158 (494), 10: -12,158 (121), 6: -14,949 (4), 8: -16,826 (6), 7: -19,052 (8) |
| open_melons | 9,312 | 10 | 8 | 10: -9,345 (203), 5: -9,354 (689), 8: -9,466 (1345), 6: -11,178 (308), 7: -11,519 (254), 11: -12,286 (41), 9: -13,136 (143), 12: -14,151 (19), 4: -14,454 (139), 14: -18,562 (6), 13: -18,657 (8) |
| wheat_cap | 9,133 | 15 | 18 | 15: -8,106 (485), 18: -8,480 (1269), 23: -9,282 (41), 14: -9,803 (33), 21: -9,933 (96), 17: -11,088 (112), 20: -11,657 (510), 12: -12,186 (29), 22: -12,403 (33), 8: -13,525 (9), 24: -13,601 (23), 19: -14,245 (113), 13: -14,538 (130), 25: -14,575 (84), 16: -14,782 (115), 11: -15,194 (14), 10: -15,495 (5), 5: -16,641 (17), 6: -16,821 (4), 7: -17,043 (22), 9: -17,239 (11) |
| STRAW_CUTOFF | 8,828 | 12 | 17 | 12: -8,286 (61), 17: -9,214 (1754), 16: -9,464 (527), 19: -11,027 (82), 18: -11,645 (236), 15: -13,570 (233), 14: -13,976 (152), 20: -15,901 (93), 13: -17,114 (17) |
| OPP_GROWTH | 8,780 | 1.3 | 1.3 | 1.3: -8,172 (1630), 1.6: -9,577 (91), 1.1: -10,194 (126), 1.4: -11,264 (432), 1.5: -11,858 (320), 1.7: -14,483 (71), 1.2: -14,519 (389), 1.0: -15,849 (71), 1.8: -16,952 (25) |
| CROP_SWEEP_LEN | 8,776 | 3 | 6 | 3: -9,104 (96), 6: -9,708 (2165), 7: -10,307 (340), 5: -11,494 (383), 4: -12,241 (74), 8: -16,746 (63), 9: -17,638 (22), 10: -17,880 (12) |
| opening | 8,626 | frontier | frontier | frontier: -8,893 (2656), v312: -17,519 (499) |
| OPENING_MELONS | 8,363 | 6 | 10 | 6: -5,178 (32), 10: -9,604 (1501), 8: -10,119 (80), 11: -10,151 (1035), 7: -10,418 (104), 14: -12,636 (67), 13: -13,244 (39), 12: -13,526 (172), 9: -13,541 (125) |
| open_sheep | 8,332 | 2 | 2 | 2: -9,697 (2873), 1: -14,947 (148), 3: -16,336 (73), 0: -18,028 (61) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=124)
- (13, 3, 6): +14,567 (n=219)
- (7, 3, 5): +11,849 (n=36)
- (15, 3, 6): +11,582 (n=112)
- (10, 3, 6): +11,227 (n=314)
- (8, 3, 6): +11,158 (n=319)
- (17, 3, 6): +10,971 (n=96)
- (11, 3, 6): +10,963 (n=128)
- (17, 4, 6): +10,740 (n=7)
- (9, 4, 6): +10,652 (n=118)
- (16, 3, 6): +10,603 (n=40)
- (7, 4, 6): +10,358 (n=20)
- (8, 3, 4): +10,272 (n=59)
- (12, 4, 6): +10,123 (n=93)
- (9, 3, 6): +9,773 (n=352)

_Generated 2026-09-04 15:46. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._