# Evolution run 20260905-022611

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.01 h · candidates evaluated this run: 919 · games 30,102 (14,944/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 46 | 92 |
| dead_pattern | 209 | 418 |
| dead_smoke | 57 | 456 |
| alive | 607 | 29136 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 6290 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=1624
- queue: best +12,820 (`e4a45816755f`), n=1772
- v312: best +14,798 (`a65aa7a26283`), n=1651
- wide: best +10,939 (`daba421dc7ec`), n=1243

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 16,968 | 145 | 100 | 145: -4,073 (6), 74: -4,209 (35), 114: -6,547 (53), 98: -7,246 (29), 127: -8,579 (158), 130: -8,967 (10), 120: -9,019 (14), 57: -9,192 (2), 56: -10,156 (3), 83: -10,350 (18), 134: -10,507 (8), 131: -10,868 (15), 105: -11,166 (27), 100: -11,226 (3468), 117: -11,672 (14), 141: -11,763 (4), 143: -11,814 (18), 124: -12,061 (14), 129: -12,141 (48), 82: -12,338 (49), 59: -12,362 (6), 88: -12,437 (82), 116: -12,788 (110), 133: -12,805 (203), 67: -12,879 (240), 69: -13,045 (6), 112: -13,168 (12), 97: -13,188 (40), 61: -13,203 (7), 68: -13,230 (24), 92: -13,321 (318), 126: -13,334 (11), 121: -13,430 (44), 103: -13,597 (17), 78: -13,671 (10), 87: -13,707 (12), 77: -13,734 (16), 102: -13,736 (35), 118: -13,773 (17), 101: -13,775 (44), 58: -13,809 (6), 85: -13,814 (57), 93: -13,865 (30), 86: -13,879 (11), 91: -13,961 (20), 94: -13,981 (14), 96: -14,036 (76), 53: -14,137 (2), 140: -14,137 (26), 80: -14,167 (13), 72: -14,201 (10), 128: -14,220 (4), 110: -14,262 (14), 132: -14,289 (12), 75: -14,314 (12), 135: -14,351 (12), 70: -14,394 (4), 64: -14,428 (13), 109: -14,500 (13), 95: -14,614 (33), 54: -14,657 (6), 90: -14,659 (61), 113: -14,676 (9), 62: -14,692 (41), 66: -14,752 (18), 89: -14,799 (26), 50: -14,810 (107), 55: -14,891 (5), 144: -14,954 (5), 150: -14,961 (76), 115: -15,136 (27), 147: -15,286 (4), 51: -15,361 (6), 65: -15,432 (3), 142: -15,492 (5), 119: -15,543 (10), 108: -15,583 (11), 123: -15,592 (20), 106: -15,594 (14), 63: -15,610 (8), 137: -15,793 (7), 76: -15,828 (9), 125: -15,879 (19), 107: -16,025 (19), 104: -16,273 (5), 73: -16,399 (7), 122: -16,456 (8), 84: -16,709 (11), 60: -16,752 (13), 136: -16,899 (5), 71: -16,950 (4), 81: -17,209 (14), 139: -17,379 (7), 138: -17,442 (5), 111: -17,509 (29), 99: -17,523 (10), 79: -17,548 (18), 148: -20,595 (6), 52: -21,042 (2) |
| demand_share | 15,095 | 0.5 | 0.5 | 0.5: -10,700 (2957), 0.75: -11,029 (38), 0.55: -12,590 (643), 0.45: -12,673 (1709), 0.7: -12,925 (74), 0.4: -13,082 (155), 0.6: -14,569 (334), 0.65: -14,685 (64), 0.35: -15,006 (77), 0.3: -16,609 (194), 0.8: -17,037 (19), 0.95: -19,727 (7), 1.0: -21,501 (9), 0.85: -23,508 (7), 0.9: -25,795 (3) |
| wheat_stock | 14,236 | 21 | 0 | 21: -8,236 (13), 7: -10,824 (56), 5: -11,293 (109), 2: -11,396 (160), 0: -11,709 (4685), 12: -11,940 (77), 10: -12,228 (140), 1: -12,445 (118), 18: -12,533 (7), 16: -12,587 (19), 17: -13,310 (36), 4: -13,343 (308), 13: -13,538 (37), 32: -13,668 (2), 6: -13,752 (221), 11: -13,821 (89), 20: -13,890 (3), 14: -13,949 (28), 19: -14,422 (7), 8: -15,104 (21), 3: -15,157 (49), 9: -15,231 (30), 24: -16,597 (4), 15: -16,837 (16), 35: -17,198 (2), 27: -17,367 (4), 40: -17,808 (11), 26: -18,262 (2), 33: -18,492 (3), 29: -19,018 (3), 22: -19,282 (4), 38: -19,458 (3), 28: -20,798 (13), 23: -20,979 (3), 30: -22,109 (2), 37: -22,472 (2) |
| load_per_hand | 11,882 | 20 | 20 | 20: -10,591 (2858), 19: -11,653 (588), 18: -12,314 (447), 22: -12,858 (117), 16: -13,086 (889), 15: -13,613 (765), 21: -13,878 (133), 17: -13,978 (190), 23: -14,113 (59), 13: -14,467 (36), 14: -15,308 (44), 24: -16,822 (29), 25: -18,903 (17), 12: -19,209 (89), 26: -22,473 (29) |
| wheat_sell_price | 11,799 | 50 | 30 | 50: -9,686 (147), 28: -9,702 (169), 27: -10,148 (468), 44: -10,615 (10), 47: -10,956 (3), 38: -11,380 (27), 37: -11,704 (82), 30: -11,883 (3748), 31: -11,901 (174), 25: -12,681 (401), 29: -12,866 (164), 35: -13,517 (105), 32: -13,528 (63), 26: -13,703 (446), 36: -14,727 (74), 33: -15,407 (64), 34: -15,715 (69), 41: -15,892 (13), 42: -15,904 (3), 43: -16,014 (8), 40: -16,977 (14), 39: -17,410 (22), 45: -18,332 (8), 46: -20,201 (6), 48: -21,485 (2) |
| MAX_HANDS | 11,569 | 13 | 13 | 13: -11,248 (3709), 11: -12,045 (260), 12: -12,916 (1683), 16: -13,674 (80), 14: -13,712 (262), 15: -13,746 (176), 10: -16,214 (72), 9: -19,862 (26), 8: -22,817 (22) |
| ROUTE_LEN | 11,056 | 3 | 3 | 3: -11,738 (5485), 2: -13,396 (488), 4: -14,862 (286), 5: -22,794 (31) |
| MAX_SHEEP | 10,692 | 12 | 12 | 12: -10,445 (1274), 11: -11,811 (397), 14: -12,320 (3204), 9: -12,743 (73), 10: -12,820 (263), 13: -12,851 (1029), 6: -15,818 (7), 8: -16,808 (17), 4: -18,150 (11), 7: -18,448 (11), 5: -21,137 (4) |
| wheat_tiles | 10,429 | 3 | 0 | 3: -11,667 (122), 0: -11,879 (5479), 2: -13,144 (228), 1: -13,420 (390), 4: -13,586 (41), 5: -17,735 (14), 6: -19,727 (9), 8: -22,096 (6) |
| wheat_per_animal | 9,920 | 0.1 | 0.0 | 0.1: -10,280 (707), 0.0: -11,838 (4364), 0.2: -13,092 (677), 0.5: -13,446 (135), 0.6: -14,753 (57), 0.3: -14,823 (228), 0.8: -15,073 (8), 0.4: -16,087 (78), 0.9: -16,641 (13), 0.7: -19,848 (10), 1.2: -19,871 (9), 1.0: -20,200 (3) |
| open_melons | 8,956 | 8 | 8 | 8: -11,418 (2655), 5: -11,494 (1340), 10: -12,098 (331), 7: -12,593 (430), 6: -12,642 (751), 9: -13,299 (377), 11: -13,468 (67), 12: -14,817 (42), 4: -15,417 (267), 14: -19,089 (14), 13: -20,374 (16) |
| MELON_MAX_TILES | 7,731 | 41 | 40 | 41: -10,258 (1147), 40: -11,300 (1861), 32: -11,362 (31), 44: -11,749 (55), 50: -11,844 (606), 31: -12,171 (94), 47: -12,364 (138), 37: -12,850 (191), 45: -12,857 (122), 23: -13,082 (8), 43: -13,447 (1119), 34: -13,568 (248), 38: -13,607 (187), 46: -13,789 (40), 33: -13,866 (35), 35: -13,920 (48), 49: -13,922 (60), 22: -14,021 (11), 48: -14,043 (23), 42: -14,099 (66), 27: -14,168 (8), 26: -14,238 (8), 39: -14,423 (58), 30: -14,545 (26), 36: -14,590 (46), 29: -14,688 (11), 21: -16,990 (6), 28: -17,259 (16), 20: -17,774 (11), 25: -17,988 (9) |
| max_animals | 7,710 | 20 | 20 | 20: -11,472 (3402), 17: -12,209 (1834), 16: -12,558 (152), 18: -12,972 (230), 15: -13,615 (207), 19: -13,938 (365), 13: -14,212 (21), 14: -15,924 (38), 10: -17,875 (16), 12: -18,501 (15), 11: -19,182 (10) |
| opening | 7,529 | frontier | frontier | frontier: -10,796 (5231), v312: -18,325 (1059) |
| CROP_SWEEP_LEN | 7,458 | 6 | 6 | 6: -11,578 (4302), 3: -12,289 (164), 7: -12,471 (796), 5: -12,578 (676), 4: -13,874 (134), 8: -16,896 (154), 9: -17,841 (45), 10: -19,036 (19) |
| wheat_cap | 7,035 | 18 | 18 | 18: -10,494 (1972), 15: -10,752 (908), 14: -11,334 (58), 21: -11,831 (140), 17: -12,107 (163), 23: -12,279 (118), 20: -12,629 (1037), 12: -13,116 (68), 24: -13,562 (39), 16: -13,626 (675), 19: -13,653 (293), 13: -13,681 (325), 11: -13,863 (46), 22: -14,460 (124), 25: -14,785 (171), 10: -16,424 (22), 7: -16,472 (30), 8: -16,598 (28), 9: -16,723 (26), 5: -17,148 (39), 6: -17,529 (8) |
| CROP_SWEEP_RADIUS | 6,994 | 4 | 4 | 4: -8,461 (1373), 5: -11,164 (179), 3: -12,754 (2072), 2: -13,408 (2622), 6: -15,455 (44) |
| open_sheep | 6,959 | 2 | 2 | 2: -11,595 (5726), 1: -15,836 (313), 3: -17,591 (136), 0: -18,554 (115) |
| OPP_GROWTH | 4,922 | 1.3 | 1.3 | 1.3: -10,204 (2477), 1.6: -11,234 (147), 1.4: -12,174 (664), 1.1: -12,658 (469), 1.5: -12,745 (591), 1.7: -13,884 (197), 1.2: -13,939 (1377), 1.8: -14,153 (98), 1.0: -15,125 (270) |
| open_wheat | 4,721 | 7 | 7 | 7: -10,216 (842), 3: -10,680 (55), 9: -11,803 (2189), 8: -12,055 (2200), 4: -12,211 (58), 5: -14,037 (263), 10: -14,461 (570), 6: -14,938 (113) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=235)
- (13, 3, 6): +14,567 (n=372)
- (7, 3, 5): +11,849 (n=58)
- (15, 3, 6): +11,582 (n=185)
- (10, 3, 6): +11,227 (n=578)
- (8, 3, 6): +11,158 (n=778)
- (17, 3, 6): +10,971 (n=158)
- (11, 3, 6): +10,963 (n=337)
- (17, 4, 6): +10,740 (n=9)
- (9, 4, 6): +10,652 (n=231)
- (16, 3, 6): +10,603 (n=69)
- (7, 4, 6): +10,358 (n=36)
- (8, 3, 4): +10,272 (n=106)
- (12, 4, 6): +10,123 (n=153)
- (9, 3, 6): +9,773 (n=759)

_Generated 2026-09-05 04:27. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._