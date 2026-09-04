# Evolution run 20260904-175508

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.01 h · candidates evaluated this run: 470 · games 18,458 (9,180/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 17 | 34 |
| dead_smoke | 83 | 664 |
| alive | 370 | 17760 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 3891 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=1001
- queue: best +12,820 (`e4a45816755f`), n=1074
- v312: best +14,798 (`a65aa7a26283`), n=1058
- wide: best +10,939 (`daba421dc7ec`), n=758

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 18,521 | 74 | 100 | 74: -2,093 (29), 145: -2,153 (5), 114: -4,785 (45), 72: -5,795 (2), 98: -6,776 (25), 83: -7,173 (11), 56: -7,248 (2), 134: -7,564 (5), 120: -7,639 (9), 130: -8,012 (8), 127: -8,044 (148), 131: -8,868 (10), 100: -10,089 (2450), 55: -11,189 (2), 105: -11,532 (19), 117: -11,661 (12), 129: -11,737 (43), 59: -12,096 (4), 78: -12,289 (6), 67: -12,400 (74), 112: -12,523 (9), 116: -12,585 (91), 104: -12,764 (2), 124: -12,838 (4), 58: -12,842 (2), 133: -12,940 (46), 97: -13,090 (14), 143: -13,251 (6), 91: -13,336 (14), 96: -13,357 (48), 69: -13,405 (3), 101: -13,480 (36), 68: -13,543 (9), 85: -13,556 (36), 103: -13,680 (8), 77: -13,711 (8), 95: -13,756 (9), 75: -13,823 (8), 89: -13,839 (9), 86: -13,855 (6), 140: -13,905 (20), 135: -13,980 (9), 50: -14,051 (33), 54: -14,067 (3), 144: -14,072 (3), 65: -14,104 (2), 118: -14,186 (12), 87: -14,257 (8), 102: -14,370 (19), 137: -14,436 (4), 62: -14,549 (19), 150: -14,597 (59), 90: -14,598 (50), 93: -14,636 (25), 92: -14,711 (60), 88: -14,727 (7), 109: -14,816 (11), 115: -14,839 (19), 106: -14,908 (8), 94: -14,951 (10), 126: -15,003 (6), 121: -15,076 (7), 141: -15,224 (2), 110: -15,331 (7), 82: -15,403 (7), 119: -15,576 (7), 123: -15,592 (20), 139: -15,750 (5), 61: -15,959 (2), 63: -16,036 (4), 107: -16,060 (14), 66: -16,165 (12), 64: -16,220 (4), 132: -16,307 (8), 73: -16,399 (7), 138: -16,447 (2), 136: -16,482 (4), 125: -16,505 (12), 108: -16,674 (6), 76: -16,695 (7), 84: -16,741 (7), 142: -16,916 (3), 113: -17,057 (5), 122: -17,058 (5), 80: -17,102 (6), 111: -17,114 (20), 79: -17,210 (13), 81: -17,255 (12), 99: -17,650 (5), 128: -18,034 (2), 60: -20,456 (2), 148: -20,614 (3) |
| wheat_stock | 17,144 | 21 | 0 | 21: -5,788 (10), 7: -8,006 (35), 16: -8,930 (10), 5: -9,937 (77), 2: -10,464 (130), 0: -10,575 (2955), 10: -11,284 (69), 12: -11,747 (52), 20: -11,897 (2), 14: -12,474 (16), 1: -12,758 (68), 13: -12,768 (20), 4: -13,364 (180), 6: -13,648 (106), 11: -13,799 (58), 17: -14,204 (6), 3: -14,882 (30), 15: -15,324 (7), 9: -15,595 (18), 8: -16,655 (12), 35: -17,198 (2), 40: -17,215 (5), 28: -18,108 (3), 27: -18,285 (2), 22: -19,282 (4), 23: -20,979 (3), 33: -22,166 (2), 38: -22,932 (2) |
| demand_share | 16,080 | 0.75 | 0.5 | 0.75: -8,540 (25), 0.5: -9,714 (2201), 0.7: -10,640 (51), 0.45: -11,897 (782), 0.4: -11,976 (99), 0.55: -12,521 (318), 0.8: -13,055 (10), 0.35: -14,330 (42), 0.6: -14,548 (197), 0.65: -15,258 (36), 0.3: -15,354 (114), 0.95: -19,830 (6), 1.0: -23,514 (7), 0.85: -24,619 (2) |
| wheat_tiles | 13,966 | 3 | 0 | 3: -9,668 (81), 0: -10,753 (3336), 4: -11,886 (30), 2: -12,511 (146), 1: -13,106 (283), 5: -19,153 (7), 6: -23,326 (4), 8: -23,634 (3) |
| wheat_sell_price | 13,569 | 27 | 30 | 27: -7,916 (248), 28: -7,929 (120), 38: -8,424 (17), 37: -8,656 (37), 50: -8,911 (130), 44: -10,615 (10), 47: -10,956 (3), 31: -10,974 (94), 30: -11,020 (2506), 25: -11,424 (222), 29: -11,879 (108), 32: -12,479 (34), 35: -12,556 (64), 33: -14,245 (37), 36: -14,366 (54), 41: -14,598 (5), 26: -14,648 (117), 34: -15,409 (46), 43: -15,960 (4), 40: -16,560 (8), 39: -17,699 (14), 46: -18,796 (4), 45: -19,303 (6), 48: -21,485 (2) |
| load_per_hand | 12,844 | 20 | 20 | 20: -9,381 (1981), 19: -10,802 (381), 18: -11,687 (220), 22: -11,941 (83), 16: -12,357 (524), 21: -13,303 (100), 15: -13,455 (351), 13: -13,805 (22), 23: -14,205 (40), 17: -14,529 (85), 14: -15,888 (21), 24: -17,106 (17), 25: -18,713 (11), 12: -19,690 (33), 26: -22,225 (22) |
| MAX_HANDS | 12,436 | 13 | 13 | 13: -10,132 (2585), 11: -11,482 (126), 15: -11,780 (116), 16: -11,976 (61), 12: -12,651 (773), 14: -13,284 (166), 10: -14,734 (34), 9: -20,439 (15), 8: -22,569 (15) |
| wheat_per_animal | 11,577 | 0.1 | 0.0 | 0.1: -8,930 (539), 0.0: -10,832 (2688), 0.5: -11,906 (64), 0.2: -12,602 (350), 0.6: -13,309 (33), 0.3: -14,300 (140), 0.8: -15,252 (6), 0.9: -16,231 (8), 0.4: -16,616 (46), 1.2: -19,061 (8), 0.7: -20,508 (7) |
| ROUTE_LEN | 11,415 | 3 | 3 | 3: -10,731 (3373), 2: -11,905 (310), 4: -13,680 (192), 5: -22,146 (16) |
| max_animals | 11,081 | 20 | 20 | 20: -10,374 (2348), 17: -11,177 (1011), 16: -11,678 (79), 18: -12,210 (129), 19: -13,758 (227), 13: -14,115 (11), 15: -14,997 (48), 11: -16,738 (5), 14: -17,875 (16), 10: -19,252 (10), 12: -21,455 (7) |
| MELON_MAX_TILES | 11,072 | 41 | 40 | 41: -8,755 (791), 40: -10,215 (1364), 32: -10,670 (25), 50: -10,787 (458), 44: -10,838 (42), 47: -11,032 (59), 31: -11,262 (72), 23: -11,387 (5), 45: -11,465 (20), 37: -12,667 (137), 35: -12,912 (29), 26: -13,094 (5), 38: -13,445 (134), 39: -13,615 (37), 34: -13,627 (127), 46: -13,632 (14), 36: -13,947 (23), 30: -13,981 (10), 43: -14,047 (386), 42: -14,116 (35), 48: -14,216 (12), 49: -14,479 (43), 27: -14,604 (7), 22: -15,344 (8), 33: -15,372 (20), 29: -15,566 (5), 28: -16,747 (10), 25: -18,985 (6), 20: -19,827 (6) |
| MAX_SHEEP | 11,038 | 12 | 12 | 12: -8,987 (946), 11: -10,988 (306), 9: -11,286 (51), 14: -11,356 (1803), 13: -12,500 (597), 10: -12,580 (160), 4: -13,211 (4), 6: -14,949 (4), 8: -17,128 (10), 7: -19,052 (8), 5: -20,025 (2) |
| open_melons | 10,172 | 10 | 8 | 10: -9,748 (228), 8: -10,288 (1633), 5: -10,366 (877), 6: -11,775 (411), 7: -12,128 (317), 11: -12,618 (46), 9: -13,483 (170), 12: -14,415 (21), 4: -14,917 (170), 14: -19,718 (9), 13: -19,921 (9) |
| wheat_cap | 9,221 | 18 | 18 | 18: -9,084 (1435), 15: -9,216 (601), 14: -10,266 (41), 21: -10,546 (107), 17: -11,603 (130), 23: -11,720 (60), 20: -12,189 (671), 12: -12,191 (33), 22: -13,394 (54), 24: -13,446 (26), 19: -14,163 (171), 13: -14,670 (170), 16: -14,783 (190), 25: -14,791 (104), 8: -15,059 (14), 11: -15,407 (18), 10: -15,946 (6), 6: -16,821 (4), 7: -16,894 (23), 5: -16,912 (21), 9: -18,305 (12) |
| opening | 8,268 | frontier | frontier | frontier: -9,672 (3258), v312: -17,939 (633) |
| CROP_SWEEP_LEN | 8,057 | 3 | 6 | 3: -10,142 (111), 6: -10,465 (2627), 7: -11,376 (471), 5: -11,915 (461), 4: -12,663 (86), 8: -16,839 (93), 9: -17,451 (27), 10: -18,199 (15) |
| open_sheep | 7,718 | 2 | 2 | 2: -10,496 (3536), 1: -15,140 (184), 3: -16,547 (89), 0: -18,214 (82) |
| OPP_GROWTH | 7,320 | 1.3 | 1.3 | 1.3: -8,884 (1861), 1.6: -10,209 (105), 1.1: -11,319 (188), 1.4: -11,613 (509), 1.5: -12,506 (383), 1.7: -14,184 (107), 1.2: -14,461 (592), 1.8: -15,919 (38), 1.0: -16,204 (108) |
| CROP_SWEEP_RADIUS | 7,060 | 4 | 4 | 4: -6,899 (1128), 5: -9,823 (137), 3: -12,209 (1271), 2: -13,436 (1326), 6: -13,960 (29) |
| open_wheat | 6,933 | 3 | 7 | 3: -7,896 (39), 7: -8,443 (658), 9: -10,627 (1250), 4: -11,035 (47), 8: -11,292 (1360), 6: -14,136 (82), 5: -14,439 (161), 10: -14,829 (294) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=151)
- (13, 3, 6): +14,567 (n=256)
- (7, 3, 5): +11,849 (n=44)
- (15, 3, 6): +11,582 (n=123)
- (10, 3, 6): +11,227 (n=383)
- (8, 3, 6): +11,158 (n=422)
- (17, 3, 6): +10,971 (n=123)
- (11, 3, 6): +10,963 (n=171)
- (17, 4, 6): +10,740 (n=8)
- (9, 4, 6): +10,652 (n=148)
- (16, 3, 6): +10,603 (n=53)
- (7, 4, 6): +10,358 (n=22)
- (8, 3, 4): +10,272 (n=71)
- (12, 4, 6): +10,123 (n=113)
- (9, 3, 6): +9,773 (n=446)

_Generated 2026-09-04 19:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._