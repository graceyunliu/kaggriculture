# Evolution run 20260904-074354

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.01 h · candidates evaluated this run: 457 · games 18,234 (9,085/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 17 | 34 |
| dead_smoke | 73 | 584 |
| alive | 367 | 17616 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 2038 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=516
- queue: best +12,820 (`e4a45816755f`), n=568
- v312: best +14,798 (`a65aa7a26283`), n=582
- wide: best +10,939 (`daba421dc7ec`), n=372

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| demand_share | 28,659 | 0.8 | 0.5 | 0.8: +1,684 (4), 0.75: -1,361 (15), 0.7: -5,188 (27), 0.45: -6,853 (247), 0.5: -7,329 (1428), 0.4: -8,359 (52), 0.55: -10,266 (102), 0.35: -12,098 (24), 0.95: -12,276 (2), 0.3: -12,937 (62), 0.6: -14,133 (54), 0.65: -14,580 (17), 1.0: -26,975 (2) |
| MELON_PRICE_CUSHION | 23,362 | 145 | 100 | 145: +1,855 (4), 74: -507 (26), 98: -597 (13), 130: -1,957 (5), 120: -2,823 (6), 114: -3,438 (40), 83: -3,499 (8), 131: -5,195 (7), 72: -5,795 (2), 134: -6,719 (4), 127: -6,809 (127), 100: -6,861 (1388), 144: -9,580 (2), 133: -9,663 (9), 50: -9,911 (19), 105: -10,352 (12), 112: -10,475 (7), 106: -10,527 (3), 129: -10,538 (31), 67: -10,721 (3), 117: -10,962 (7), 97: -11,235 (7), 116: -11,303 (33), 140: -11,523 (3), 93: -11,613 (10), 94: -11,638 (5), 85: -11,804 (13), 78: -11,836 (5), 92: -11,941 (3), 59: -12,065 (2), 135: -12,487 (2), 101: -12,532 (19), 119: -12,669 (4), 89: -12,700 (3), 96: -13,000 (15), 150: -13,039 (22), 107: -13,796 (8), 90: -13,997 (14), 65: -14,104 (2), 115: -14,425 (9), 88: -14,563 (6), 76: -14,629 (3), 69: -14,818 (2), 123: -14,819 (13), 125: -14,929 (8), 118: -15,007 (6), 110: -15,265 (3), 95: -15,272 (2), 66: -15,497 (8), 113: -15,511 (4), 75: -15,547 (4), 84: -15,624 (4), 109: -15,672 (7), 108: -15,922 (2), 80: -15,929 (2), 126: -16,198 (2), 132: -16,242 (3), 102: -17,220 (2), 103: -17,571 (2), 73: -17,694 (2), 81: -18,062 (5), 79: -18,100 (8), 111: -18,177 (9), 63: -18,295 (2), 136: -19,272 (3), 82: -19,379 (2), 62: -21,507 (2) |
| wheat_tiles | 19,427 | 3 | 0 | 3: -5,280 (48), 0: -7,635 (1781), 4: -8,142 (17), 2: -9,169 (62), 1: -10,713 (123), 5: -18,409 (2), 6: -22,648 (2), 8: -24,707 (2) |
| wheat_stock | 19,297 | 16 | 0 | 16: -1,895 (5), 7: -5,458 (25), 21: -5,788 (10), 10: -6,424 (22), 5: -7,193 (50), 0: -7,355 (1625), 13: -9,055 (10), 12: -9,080 (29), 2: -9,321 (95), 4: -10,820 (48), 14: -11,028 (13), 15: -11,351 (3), 1: -11,705 (35), 11: -11,837 (7), 6: -12,359 (14), 9: -15,105 (8), 3: -15,158 (20), 17: -15,637 (2), 8: -17,719 (5), 28: -19,249 (2), 40: -20,803 (2), 22: -21,192 (2) |
| STRAW_CUTOFF | 18,275 | 12 | 17 | 12: -3,714 (42), 19: -6,443 (36), 17: -7,214 (1277), 16: -7,361 (372), 18: -9,904 (130), 15: -11,834 (104), 14: -13,210 (42), 20: -17,277 (32), 13: -21,989 (3) |
| MELON_MAX_TILES | 17,165 | 41 | 40 | 41: -5,546 (500), 32: -6,524 (9), 44: -7,132 (22), 40: -7,228 (784), 35: -7,278 (13), 50: -8,345 (314), 26: -8,525 (3), 47: -8,658 (28), 31: -9,609 (46), 45: -9,659 (12), 27: -9,851 (2), 43: -10,936 (68), 37: -11,243 (54), 38: -12,047 (48), 42: -12,306 (14), 39: -12,691 (16), 46: -13,036 (7), 49: -13,170 (27), 34: -13,256 (31), 48: -13,577 (5), 23: -13,953 (2), 29: -14,376 (2), 30: -14,407 (3), 22: -15,228 (6), 36: -15,281 (4), 33: -16,488 (8), 25: -19,485 (2), 28: -19,578 (4), 20: -22,711 (3) |
| load_per_hand | 16,708 | 19 | 20 | 19: -6,309 (135), 20: -6,846 (1298), 22: -8,044 (34), 13: -8,871 (12), 18: -8,979 (102), 15: -9,031 (107), 16: -9,548 (198), 23: -11,139 (19), 21: -11,345 (60), 14: -13,641 (10), 17: -14,480 (23), 24: -16,063 (11), 12: -19,741 (17), 25: -20,191 (4), 26: -23,016 (8) |
| MAX_HANDS | 15,787 | 16 | 13 | 16: -6,584 (32), 13: -7,154 (1484), 11: -7,499 (64), 15: -8,991 (75), 12: -10,118 (273), 14: -10,135 (81), 10: -13,062 (19), 9: -20,663 (4), 8: -22,371 (6) |
| wheat_per_animal | 15,026 | 0.1 | 0.0 | 0.1: -5,701 (343), 0.0: -7,822 (1444), 0.5: -7,927 (27), 0.6: -8,858 (6), 0.2: -9,989 (135), 0.8: -11,135 (3), 0.3: -12,869 (59), 0.9: -13,147 (2), 0.4: -16,985 (14), 1.2: -20,728 (4) |
| wheat_cap | 14,333 | 23 | 18 | 23: -2,866 (16), 15: -4,749 (318), 18: -6,844 (998), 21: -7,293 (64), 14: -8,176 (21), 20: -9,003 (249), 8: -9,125 (5), 17: -9,695 (76), 12: -10,399 (21), 22: -12,158 (20), 24: -13,040 (17), 19: -13,679 (50), 5: -13,808 (5), 25: -13,910 (48), 13: -13,919 (56), 16: -13,943 (45), 11: -15,082 (8), 7: -16,429 (11), 9: -16,777 (7), 6: -17,199 (2) |
| fert_buy | 13,704 | 0 | 0 | 0: -7,435 (1795), 2: -9,846 (65), 1: -11,259 (174), 3: -21,139 (4) |
| wheat_sell_price | 12,977 | 37 | 30 | 37: -4,170 (23), 38: -4,651 (12), 27: -4,897 (170), 50: -5,653 (88), 31: -5,852 (39), 28: -5,935 (96), 29: -7,926 (40), 35: -7,990 (20), 30: -8,039 (1281), 25: -8,089 (127), 47: -8,727 (2), 44: -9,542 (9), 32: -10,450 (17), 33: -12,956 (17), 36: -14,131 (21), 26: -14,301 (28), 40: -14,962 (2), 34: -15,207 (31), 41: -15,600 (4), 43: -15,862 (3), 45: -16,302 (2), 39: -17,147 (3) |
| max_animals | 12,797 | 17 | 20 | 17: -6,385 (382), 20: -7,807 (1443), 16: -8,004 (42), 18: -8,441 (58), 19: -12,347 (79), 15: -13,918 (23), 13: -15,893 (3), 14: -19,182 (5) |
| open_melons | 12,343 | 5 | 8 | 5: -6,534 (422), 8: -7,302 (939), 10: -7,683 (149), 6: -8,539 (187), 7: -9,205 (146), 11: -9,873 (27), 9: -11,480 (71), 4: -12,022 (71), 12: -13,398 (16), 14: -16,344 (3), 13: -18,877 (7) |
| MAX_SHEEP | 11,017 | 12 | 12 | 12: -6,542 (643), 14: -7,638 (810), 9: -8,094 (31), 11: -8,272 (184), 6: -8,828 (2), 10: -10,211 (67), 4: -10,356 (2), 13: -10,366 (294), 7: -17,559 (3) |
| CROP_SWEEP_LEN | 10,565 | 3 | 6 | 3: -6,568 (74), 7: -7,125 (192), 6: -7,341 (1432), 5: -9,607 (232), 4: -9,977 (50), 8: -15,813 (41), 9: -16,783 (11), 10: -17,132 (6) |
| OPP_GROWTH | 10,290 | 1.1 | 1.3 | 1.1: -5,851 (63), 1.3: -6,333 (1249), 1.6: -6,731 (60), 1.4: -8,867 (251), 1.5: -10,349 (215), 1.2: -13,946 (125), 1.7: -14,804 (30), 1.0: -15,568 (29), 1.8: -16,141 (16) |
| open_sheep | 10,274 | 2 | 2 | 2: -7,276 (1874), 1: -13,209 (92), 3: -15,470 (40), 0: -17,549 (32) |
| OPENING_MELONS | 10,039 | 6 | 10 | 6: -1,468 (25), 11: -7,155 (611), 10: -7,621 (1055), 8: -8,951 (60), 7: -9,252 (88), 14: -10,567 (44), 13: -11,010 (22), 9: -11,394 (65), 12: -11,507 (68) |
| ROUTE_LEN | 9,463 | 3 | 3 | 3: -7,618 (1750), 2: -8,955 (177), 4: -9,700 (106), 5: -17,081 (5) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=83)
- (13, 3, 6): +14,567 (n=169)
- (7, 3, 5): +11,849 (n=32)
- (15, 3, 6): +11,582 (n=68)
- (10, 3, 6): +11,227 (n=200)
- (8, 3, 6): +11,158 (n=183)
- (17, 3, 6): +10,971 (n=72)
- (11, 3, 6): +10,963 (n=74)
- (17, 4, 6): +10,740 (n=6)
- (9, 4, 6): +10,652 (n=67)
- (16, 3, 6): +10,603 (n=29)
- (7, 4, 6): +10,358 (n=17)
- (8, 3, 4): +10,272 (n=41)
- (12, 4, 6): +10,123 (n=56)
- (9, 3, 6): +9,773 (n=214)

_Generated 2026-09-04 09:44. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._