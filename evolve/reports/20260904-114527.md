# Evolution run 20260904-114527

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.00 h · candidates evaluated this run: 477 · games 18,650 (9,306/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 21 | 42 |
| dead_smoke | 82 | 656 |
| alive | 374 | 17952 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 2790 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=712
- queue: best +12,820 (`e4a45816755f`), n=771
- v312: best +14,798 (`a65aa7a26283`), n=776
- wide: best +10,939 (`daba421dc7ec`), n=531

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| MELON_PRICE_CUSHION | 22,311 | 145 | 100 | 145: +1,855 (4), 74: -507 (26), 130: -1,957 (5), 114: -4,027 (43), 83: -4,592 (9), 98: -5,449 (20), 72: -5,795 (2), 120: -5,851 (8), 131: -6,046 (8), 134: -6,719 (4), 127: -7,940 (143), 100: -8,873 (1865), 124: -9,180 (2), 144: -9,580 (2), 117: -11,202 (8), 105: -11,547 (15), 129: -11,578 (37), 67: -11,911 (10), 112: -12,020 (8), 140: -12,027 (9), 59: -12,065 (2), 116: -12,081 (63), 133: -12,173 (24), 78: -12,289 (6), 97: -12,411 (8), 135: -12,487 (2), 50: -12,608 (25), 92: -12,829 (10), 101: -12,954 (28), 96: -13,128 (30), 69: -13,405 (3), 106: -13,489 (5), 150: -13,551 (40), 85: -13,610 (26), 119: -13,617 (5), 91: -13,671 (5), 93: -13,707 (16), 90: -13,884 (22), 94: -13,963 (8), 80: -14,082 (4), 65: -14,104 (2), 89: -14,140 (4), 125: -14,478 (9), 88: -14,727 (7), 118: -14,769 (9), 75: -14,830 (6), 95: -14,876 (4), 123: -14,987 (17), 115: -15,006 (13), 132: -15,127 (6), 73: -15,145 (3), 110: -15,331 (7), 113: -15,511 (4), 107: -15,539 (13), 84: -15,624 (4), 109: -15,672 (7), 137: -15,708 (2), 66: -16,165 (12), 138: -16,447 (2), 122: -16,552 (4), 79: -16,555 (11), 77: -16,735 (2), 126: -16,797 (3), 82: -16,844 (3), 68: -17,029 (2), 111: -17,086 (12), 108: -17,351 (5), 99: -17,422 (4), 62: -17,505 (5), 103: -17,571 (2), 102: -17,595 (5), 139: -17,675 (3), 76: -17,890 (5), 81: -17,903 (10), 63: -18,295 (2), 136: -19,272 (3), 60: -20,456 (2) |
| wheat_stock | 20,272 | 16 | 0 | 16: -1,895 (5), 21: -5,788 (10), 7: -7,342 (31), 5: -8,656 (64), 0: -9,208 (2157), 10: -9,486 (37), 2: -9,975 (110), 12: -10,556 (42), 13: -10,903 (15), 14: -12,474 (16), 1: -12,534 (52), 6: -13,089 (40), 4: -13,405 (111), 11: -13,834 (28), 17: -14,133 (3), 15: -14,437 (4), 3: -15,061 (24), 9: -15,609 (9), 8: -16,929 (7), 35: -17,198 (2), 40: -18,510 (4), 23: -19,111 (2), 28: -19,249 (2), 22: -19,282 (4), 33: -22,166 (2) |
| demand_share | 19,843 | 0.8 | 0.5 | 0.8: -5,239 (6), 0.75: -5,461 (20), 0.7: -7,517 (34), 0.5: -8,819 (1799), 0.45: -10,050 (422), 0.4: -10,856 (76), 0.55: -11,754 (173), 0.35: -13,762 (33), 0.3: -14,446 (85), 0.6: -14,490 (106), 0.65: -14,693 (25), 0.95: -17,648 (4), 0.85: -24,619 (2), 1.0: -25,082 (4) |
| wheat_tiles | 17,287 | 3 | 0 | 3: -7,420 (61), 0: -9,495 (2419), 4: -10,481 (22), 2: -11,432 (97), 1: -12,227 (181), 5: -19,193 (4), 6: -24,660 (3), 8: -24,707 (2) |
| wheat_sell_price | 15,983 | 37 | 30 | 37: -5,502 (25), 27: -6,413 (202), 38: -6,637 (14), 28: -7,018 (109), 50: -7,709 (111), 47: -8,727 (2), 31: -8,758 (50), 44: -9,542 (9), 25: -9,820 (165), 30: -9,902 (1803), 29: -10,593 (70), 35: -10,755 (34), 32: -12,160 (27), 33: -14,118 (25), 36: -14,406 (34), 26: -15,207 (41), 41: -15,600 (4), 34: -15,683 (41), 43: -15,862 (3), 40: -16,486 (5), 45: -17,699 (3), 39: -18,645 (9), 48: -21,485 (2) |
| load_per_hand | 14,466 | 20 | 20 | 20: -8,351 (1604), 19: -8,972 (213), 22: -10,342 (52), 18: -10,835 (157), 16: -11,481 (331), 13: -11,706 (15), 15: -12,126 (190), 21: -12,568 (81), 23: -12,935 (29), 14: -14,137 (12), 17: -14,225 (51), 24: -17,783 (14), 25: -18,646 (6), 12: -19,432 (23), 26: -22,817 (12) |
| MAX_HANDS | 12,909 | 13 | 13 | 13: -8,904 (1951), 11: -9,967 (89), 16: -10,226 (45), 15: -10,791 (96), 12: -11,663 (444), 14: -12,236 (117), 10: -13,682 (25), 9: -20,449 (10), 8: -21,813 (13) |
| MELON_MAX_TILES | 12,724 | 41 | 40 | 41: -7,374 (628), 44: -8,852 (27), 40: -9,008 (1028), 32: -9,614 (16), 50: -9,689 (376), 31: -10,184 (50), 47: -10,584 (48), 45: -11,149 (16), 26: -11,379 (4), 35: -11,676 (22), 37: -11,861 (84), 23: -12,094 (3), 46: -13,036 (7), 39: -13,166 (25), 27: -13,251 (5), 38: -13,289 (99), 34: -13,353 (64), 43: -13,534 (167), 42: -14,030 (22), 36: -14,140 (9), 48: -14,213 (8), 49: -14,432 (36), 30: -15,232 (7), 29: -15,539 (4), 22: -15,686 (7), 33: -15,708 (13), 28: -16,907 (7), 25: -18,308 (3), 20: -20,098 (4) |
| wheat_per_animal | 12,065 | 0.1 | 0.0 | 0.1: -7,329 (421), 0.0: -9,680 (1967), 0.6: -9,952 (14), 0.5: -10,106 (39), 0.8: -11,525 (4), 0.2: -11,833 (212), 0.3: -13,771 (92), 0.9: -15,433 (4), 0.4: -16,930 (30), 1.2: -19,394 (5) |
| ROUTE_LEN | 11,390 | 3 | 3 | 3: -9,433 (2398), 2: -10,798 (230), 4: -12,387 (152), 5: -20,823 (10) |
| max_animals | 10,986 | 17 | 20 | 17: -9,332 (608), 20: -9,337 (1846), 16: -10,581 (59), 18: -11,212 (86), 19: -13,315 (136), 15: -14,427 (31), 13: -14,606 (6), 14: -19,126 (7), 12: -19,664 (5), 10: -20,318 (5) |
| STRAW_CUTOFF | 10,639 | 12 | 17 | 12: -7,130 (54), 17: -8,729 (1602), 16: -9,070 (477), 19: -9,563 (59), 18: -11,392 (210), 15: -13,108 (185), 14: -14,558 (114), 20: -16,166 (77), 13: -17,768 (12) |
| open_melons | 10,028 | 5 | 8 | 5: -8,629 (594), 8: -8,983 (1207), 10: -9,062 (191), 6: -10,588 (269), 7: -11,061 (215), 11: -11,909 (39), 9: -12,866 (123), 12: -14,151 (19), 4: -14,228 (119), 14: -18,562 (6), 13: -18,657 (8) |
| wheat_cap | 9,861 | 15 | 18 | 15: -7,378 (432), 18: -8,116 (1188), 23: -8,126 (29), 14: -9,624 (28), 21: -9,823 (91), 17: -10,653 (99), 20: -11,162 (419), 8: -11,533 (7), 12: -12,186 (29), 22: -12,348 (27), 24: -13,836 (22), 19: -14,229 (86), 10: -14,422 (3), 13: -14,500 (102), 16: -14,529 (93), 25: -14,575 (76), 11: -14,738 (12), 5: -16,138 (14), 7: -16,586 (18), 6: -16,821 (4), 9: -17,239 (11) |
| MAX_SHEEP | 9,465 | 12 | 12 | 12: -7,911 (778), 11: -9,824 (236), 14: -9,867 (1191), 9: -10,427 (41), 4: -10,967 (3), 10: -11,878 (94), 13: -11,898 (431), 6: -14,949 (4), 8: -15,728 (5), 7: -17,376 (6) |
| OPP_GROWTH | 9,277 | 1.3 | 1.3 | 1.3: -7,776 (1517), 1.6: -9,106 (82), 1.1: -9,319 (102), 1.4: -10,858 (383), 1.5: -11,585 (285), 1.2: -14,491 (287), 1.7: -14,581 (60), 1.0: -15,933 (50), 1.8: -17,053 (24) |
| opening | 8,848 | frontier | frontier | frontier: -8,352 (2350), v312: -17,199 (440) |
| fert_buy | 8,741 | 0 | 0 | 0: -9,112 (2307), 2: -11,506 (112), 1: -13,049 (362), 3: -17,853 (9) |
| OPENING_MELONS | 8,693 | 6 | 10 | 6: -4,475 (30), 10: -9,212 (1363), 11: -9,453 (890), 8: -9,817 (72), 7: -10,225 (100), 14: -12,568 (59), 9: -13,074 (107), 13: -13,079 (35), 12: -13,167 (134) |
| CROP_SWEEP_LEN | 8,618 | 3 | 6 | 3: -8,434 (89), 6: -9,210 (1922), 7: -9,623 (293), 5: -11,136 (336), 4: -12,055 (67), 8: -16,326 (55), 9: -16,975 (18), 10: -17,052 (10) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=105)
- (13, 3, 6): +14,567 (n=208)
- (7, 3, 5): +11,849 (n=36)
- (15, 3, 6): +11,582 (n=92)
- (10, 3, 6): +11,227 (n=272)
- (8, 3, 6): +11,158 (n=274)
- (17, 3, 6): +10,971 (n=85)
- (11, 3, 6): +10,963 (n=111)
- (17, 4, 6): +10,740 (n=7)
- (9, 4, 6): +10,652 (n=98)
- (16, 3, 6): +10,603 (n=36)
- (7, 4, 6): +10,358 (n=19)
- (8, 3, 4): +10,272 (n=55)
- (12, 4, 6): +10,123 (n=80)
- (9, 3, 6): +9,773 (n=322)

_Generated 2026-09-04 13:45. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._