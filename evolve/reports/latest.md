# Evolution run 20260904-022501

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.00 h · candidates evaluated this run: 444 · games 17,676 (8,828/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 6 | 12 |
| dead_smoke | 84 | 672 |
| alive | 354 | 16992 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 1093 · held-out evaluated: 477 · held-out PASS: 448

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | +8,847 | 3.5 | 10-0 | +11,447 | +4,793 | 3.6 | 16-4 |

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

- c1: best +14,567 (`8c6f5b00cc43`), n=253
- queue: best +12,820 (`e4a45816755f`), n=316
- v312: best +14,798 (`a65aa7a26283`), n=331
- wide: best +10,939 (`daba421dc7ec`), n=193

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| load_per_hand | 27,004 | 19 | 20 | 19: +1,743 (65), 14: -119 (2), 20: -1,442 (771), 15: -1,708 (48), 18: -1,901 (44), 22: -2,046 (18), 13: -2,719 (6), 23: -3,206 (9), 21: -3,380 (22), 16: -3,852 (92), 17: -9,296 (6), 24: -15,866 (4), 12: -17,940 (4), 26: -25,261 (2) |
| MELON_PRICE_CUSHION | 26,909 | 116 | 100 | 116: +6,549 (5), 131: +6,391 (3), 98: +3,376 (10), 112: +3,357 (2), 74: +2,225 (22), 145: +1,855 (4), 114: +745 (28), 120: +679 (5), 83: +646 (6), 130: +238 (4), 96: -833 (2), 100: -939 (794), 127: -2,153 (80), 50: -2,832 (10), 134: -4,560 (3), 117: -5,185 (3), 97: -5,394 (2), 93: -5,901 (4), 106: -5,974 (2), 119: -6,342 (2), 105: -6,359 (7), 101: -7,536 (5), 90: -7,920 (2), 129: -8,535 (20), 133: -9,102 (5), 115: -9,553 (4), 150: -9,764 (5), 94: -9,789 (3), 111: -11,530 (2), 125: -11,744 (2), 140: -12,033 (2), 135: -12,487 (2), 79: -13,076 (2), 113: -14,368 (2), 123: -14,824 (3), 108: -15,922 (2), 81: -20,361 (2) |
| MAX_HANDS | 20,966 | 16 | 13 | 16: -820 (22), 15: -1,073 (39), 13: -1,430 (839), 11: -1,520 (36), 14: -2,197 (30), 12: -3,655 (117), 10: -8,089 (8), 8: -21,786 (2) |
| wheat_sell_price | 20,851 | 38 | 30 | 38: +4,550 (6), 35: +1,999 (10), 31: +1,793 (21), 29: +939 (17), 28: -78 (59), 50: -569 (58), 27: -795 (117), 32: -1,074 (5), 37: -1,784 (19), 30: -1,835 (664), 25: -2,732 (76), 44: -7,359 (6), 33: -8,633 (7), 47: -8,727 (2), 34: -8,768 (8), 26: -12,373 (8), 36: -12,965 (5), 45: -16,302 (2) |
| wheat_stock | 20,345 | 16 | 0 | 16: +2,617 (4), 12: +2,398 (9), 10: +2,046 (11), 7: +319 (16), 0: -1,392 (911), 1: -2,104 (9), 5: -2,558 (30), 13: -2,669 (4), 21: -2,880 (8), 4: -3,411 (11), 2: -3,541 (47), 14: -6,624 (7), 15: -7,650 (2), 9: -8,519 (2), 6: -10,489 (6), 3: -11,770 (9), 8: -17,728 (3) |
| wheat_cap | 18,413 | 23 | 18 | 23: +1,970 (11), 14: +1,871 (9), 15: +1,263 (199), 18: -1,893 (621), 20: -1,894 (106), 21: -2,429 (37), 12: -3,149 (6), 17: -3,941 (37), 8: -4,226 (3), 24: -5,629 (4), 19: -6,392 (11), 22: -6,476 (7), 25: -7,091 (13), 16: -8,919 (10), 13: -12,032 (11), 11: -14,686 (3), 9: -16,443 (3) |
| feed_spare_poor | 17,864 | 2 | 0 | 2: +1,172 (11), 0: -1,471 (973), 1: -4,228 (106), 3: -16,692 (3) |
| wheat_per_animal | 15,834 | 0.6 | 0.0 | 0.6: +2,265 (3), 0.1: -454 (214), 0.5: -1,541 (16), 0.0: -1,939 (789), 0.2: -2,118 (50), 0.3: -4,074 (11), 0.9: -13,147 (2), 0.4: -13,568 (6) |
| OPP_GROWTH | 15,633 | 1.8 | 1.3 | 1.8: +56 (2), 1.3: -1,028 (777), 1.1: -1,857 (44), 1.4: -2,286 (106), 1.6: -2,749 (42), 1.5: -3,704 (89), 1.2: -9,423 (21), 1.0: -11,055 (8), 1.7: -15,577 (4) |
| open_melons | 15,618 | 5 | 8 | 5: -184 (235), 11: -713 (10), 8: -1,724 (538), 10: -1,970 (82), 6: -2,144 (91), 7: -2,364 (66), 4: -4,113 (30), 9: -6,924 (32), 12: -7,094 (7), 14: -15,801 (2) |
| STRAW_CUTOFF | 15,596 | 12 | 17 | 12: +911 (31), 16: -273 (190), 19: -320 (21), 17: -1,830 (750), 18: -3,063 (49), 15: -3,845 (34), 14: -10,739 (8), 20: -14,685 (10) |
| MAX_SHEEP | 15,339 | 14 | 12 | 14: -557 (410), 12: -1,459 (397), 11: -2,195 (106), 9: -3,215 (19), 10: -3,620 (28), 13: -5,205 (128), 6: -8,828 (2), 7: -15,896 (2) |
| HERD_LAST_DAY | 14,560 | 19 | 19 | 19: -754 (634), 20: -1,410 (121), 22: -3,098 (274), 16: -5,002 (10), 18: -5,474 (23), 17: -7,492 (8), 21: -7,694 (20), 14: -15,314 (2) |
| MELON_MAX_TILES | 14,193 | 43 | 40 | 43: +2,889 (13), 41: +56 (312), 47: -294 (11), 35: -849 (8), 40: -1,400 (438), 26: -1,571 (2), 44: -2,490 (14), 50: -3,058 (187), 32: -3,611 (7), 31: -3,901 (25), 45: -4,750 (6), 22: -5,673 (2), 42: -5,750 (6), 34: -6,561 (4), 38: -7,659 (12), 37: -7,828 (22), 39: -9,534 (9), 49: -11,304 (8) |
| CROP_SWEEP_LEN | 12,895 | 7 | 6 | 7: +495 (96), 3: -1,463 (51), 6: -1,493 (795), 5: -3,253 (102), 4: -3,974 (26), 8: -11,696 (17), 9: -12,400 (5) |
| demand_share | 12,859 | 0.8 | 0.5 | 0.8: +1,684 (4), 0.75: +967 (13), 0.45: +534 (126), 0.5: -1,528 (802), 0.7: -2,529 (22), 0.4: -2,867 (29), 0.55: -3,511 (34), 0.3: -6,857 (29), 0.6: -8,435 (10), 0.35: -9,177 (15), 0.65: -11,175 (8) |
| opening | 10,583 | frontier | frontier | frontier: -601 (974), v312: -11,184 (119) |
| max_animals | 9,293 | 17 | 20 | 17: +18 (208), 20: -1,968 (796), 16: -2,121 (25), 18: -3,478 (33), 19: -4,853 (23), 15: -9,275 (8) |
| geese | 8,841 | 0 | 0 | 0: -1,493 (1013), 1: -4,124 (68), 2: -10,334 (12) |
| open_wheat | 8,479 | 3 | 7 | 3: -145 (22), 9: -213 (307), 7: -806 (316), 4: -2,001 (18), 8: -3,046 (373), 5: -3,502 (9), 10: -7,467 (21), 6: -8,624 (27) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=47)
- (13, 3, 6): +14,567 (n=109)
- (7, 3, 5): +11,849 (n=28)
- (15, 3, 6): +11,582 (n=33)
- (10, 3, 6): +11,227 (n=115)
- (8, 3, 6): +11,158 (n=79)
- (17, 3, 6): +10,971 (n=50)
- (11, 3, 6): +10,963 (n=39)
- (17, 4, 6): +10,740 (n=5)
- (9, 4, 6): +10,652 (n=35)
- (16, 3, 6): +10,603 (n=19)
- (7, 4, 6): +10,358 (n=14)
- (8, 3, 4): +10,272 (n=29)
- (12, 4, 6): +10,123 (n=23)
- (9, 3, 6): +9,773 (n=80)

_Generated 2026-09-04 04:25. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._