# Evolution run 20260904-054322

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.00 h · candidates evaluated this run: 429 · games 17,144 (8,559/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 8 | 16 |
| dead_smoke | 77 | 616 |
| alive | 344 | 16512 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 1671 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=414
- queue: best +12,820 (`e4a45816755f`), n=465
- v312: best +14,798 (`a65aa7a26283`), n=490
- wide: best +10,939 (`daba421dc7ec`), n=302

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| wheat_stock | 23,809 | 16 | 0 | 16: +2,617 (4), 7: -1,405 (18), 10: -4,754 (18), 21: -4,852 (9), 0: -5,845 (1359), 5: -6,835 (47), 2: -7,049 (69), 13: -7,247 (7), 12: -7,617 (24), 4: -9,369 (24), 1: -10,604 (27), 14: -10,711 (12), 15: -11,351 (3), 6: -12,276 (10), 11: -12,826 (6), 9: -12,921 (5), 3: -14,379 (13), 17: -15,637 (2), 8: -17,572 (4), 40: -20,803 (2), 22: -21,192 (2) |
| MELON_PRICE_CUSHION | 21,255 | 145 | 100 | 145: +1,855 (4), 120: +679 (5), 74: -507 (26), 98: -597 (13), 83: -1,890 (7), 114: -1,940 (35), 130: -1,957 (5), 131: -3,787 (6), 100: -5,371 (1167), 72: -5,795 (2), 106: -5,974 (2), 127: -6,128 (117), 134: -6,719 (4), 50: -7,882 (15), 88: -8,576 (3), 116: -8,590 (18), 117: -8,651 (5), 93: -8,794 (6), 97: -8,962 (4), 112: -9,050 (6), 144: -9,580 (2), 133: -9,664 (7), 85: -10,053 (4), 105: -10,092 (11), 129: -10,284 (28), 96: -10,581 (5), 115: -11,178 (5), 67: -11,392 (2), 140: -11,523 (3), 94: -11,638 (5), 101: -11,698 (13), 92: -11,941 (3), 76: -11,973 (2), 107: -12,203 (3), 135: -12,487 (2), 150: -12,616 (14), 119: -12,638 (3), 78: -12,644 (3), 109: -12,929 (4), 90: -13,933 (9), 65: -14,104 (2), 113: -14,415 (3), 69: -14,818 (2), 118: -15,059 (4), 110: -15,265 (3), 95: -15,272 (2), 79: -15,281 (6), 75: -15,318 (3), 125: -15,338 (7), 84: -15,624 (4), 123: -15,642 (10), 108: -15,922 (2), 132: -16,242 (3), 111: -16,250 (5), 66: -17,388 (5), 81: -18,062 (5), 63: -18,295 (2), 136: -19,400 (2) |
| load_per_hand | 19,769 | 19 | 20 | 19: -4,323 (107), 20: -5,657 (1124), 15: -6,239 (71), 22: -6,400 (26), 18: -7,125 (76), 16: -7,770 (149), 13: -8,406 (11), 21: -8,629 (40), 23: -10,667 (18), 14: -12,895 (8), 17: -14,064 (18), 24: -16,717 (7), 12: -18,706 (11), 26: -24,092 (4) |
| wheat_per_animal | 18,892 | 0.6 | 0.0 | 0.6: -1,588 (4), 0.1: -4,535 (303), 0.8: -5,910 (2), 0.0: -6,379 (1198), 0.2: -7,435 (88), 0.5: -7,560 (26), 0.3: -11,675 (33), 0.9: -13,147 (2), 0.4: -16,263 (12), 1.2: -20,479 (3) |
| MELON_MAX_TILES | 18,289 | 41 | 40 | 41: -4,422 (448), 46: -4,665 (2), 32: -5,331 (8), 44: -5,519 (19), 40: -5,567 (641), 35: -6,256 (12), 50: -7,088 (267), 47: -7,380 (24), 43: -7,729 (35), 26: -8,525 (3), 45: -8,849 (11), 31: -9,029 (42), 22: -9,103 (3), 27: -9,851 (2), 37: -10,544 (42), 38: -11,379 (34), 42: -11,574 (12), 34: -11,746 (11), 39: -12,620 (13), 49: -12,871 (19), 48: -13,577 (5), 23: -13,953 (2), 29: -14,376 (2), 33: -16,126 (5), 25: -19,485 (2), 20: -22,711 (3) |
| MAX_HANDS | 18,026 | 16 | 13 | 16: -4,804 (28), 11: -5,668 (52), 13: -5,790 (1251), 15: -7,077 (63), 14: -7,908 (55), 12: -8,411 (201), 10: -11,444 (14), 9: -19,389 (3), 8: -22,829 (4) |
| wheat_cap | 16,035 | 23 | 18 | 23: -897 (13), 15: -2,794 (268), 14: -4,754 (15), 8: -5,285 (4), 18: -5,811 (882), 21: -6,387 (57), 20: -7,325 (185), 17: -8,641 (63), 12: -9,770 (17), 22: -10,653 (13), 19: -11,115 (24), 24: -12,514 (13), 25: -12,644 (35), 16: -12,700 (23), 13: -13,208 (31), 5: -13,808 (5), 11: -15,128 (7), 7: -15,169 (8), 9: -16,932 (6) |
| wheat_tiles | 15,513 | 3 | 0 | 3: -2,895 (41), 0: -6,048 (1456), 4: -7,679 (15), 2: -7,840 (51), 1: -9,853 (103), 5: -18,409 (2) |
| wheat_sell_price | 14,978 | 37 | 30 | 37: -3,640 (22), 27: -3,910 (152), 50: -4,108 (76), 31: -4,320 (34), 38: -4,651 (12), 28: -4,842 (87), 35: -5,131 (16), 30: -6,329 (1021), 29: -6,682 (32), 25: -6,888 (111), 32: -8,354 (13), 47: -8,727 (2), 44: -9,542 (9), 33: -12,697 (15), 26: -13,698 (22), 36: -13,875 (9), 34: -15,095 (25), 41: -15,600 (4), 43: -15,862 (3), 45: -16,302 (2), 39: -18,618 (2) |
| STRAW_CUTOFF | 14,711 | 12 | 17 | 12: -2,206 (37), 16: -5,313 (289), 19: -5,957 (33), 17: -6,090 (1115), 18: -7,961 (91), 15: -9,515 (67), 14: -12,770 (19), 20: -16,917 (19) |
| demand_share | 14,623 | 0.8 | 0.5 | 0.8: +1,684 (4), 0.75: -1,361 (15), 0.7: -3,219 (23), 0.45: -4,465 (191), 0.5: -5,904 (1193), 0.4: -7,610 (47), 0.55: -8,678 (73), 0.35: -11,554 (23), 0.95: -12,276 (2), 0.3: -12,358 (53), 0.6: -12,852 (33), 0.65: -12,939 (12) |
| max_animals | 13,833 | 17 | 20 | 17: -4,607 (315), 16: -6,200 (35), 18: -6,232 (42), 20: -6,465 (1208), 19: -10,499 (49), 15: -12,826 (18), 14: -18,440 (2) |
| open_melons | 13,752 | 5 | 8 | 5: -5,150 (361), 8: -5,787 (779), 6: -6,321 (138), 10: -6,443 (125), 7: -7,612 (113), 11: -8,893 (22), 9: -10,344 (54), 4: -10,355 (59), 12: -11,516 (12), 14: -15,801 (2), 13: -18,902 (6) |
| CROP_SWEEP_LEN | 11,804 | 7 | 6 | 7: -4,939 (151), 3: -5,285 (67), 6: -5,858 (1185), 5: -7,797 (177), 4: -8,693 (42), 8: -15,254 (34), 9: -16,432 (10), 10: -16,743 (5) |
| OPP_GROWTH | 11,803 | 1.1 | 1.3 | 1.1: -4,443 (54), 1.3: -5,189 (1104), 1.6: -5,626 (53), 1.4: -6,968 (182), 1.5: -9,006 (166), 1.2: -12,665 (69), 1.8: -13,951 (9), 1.7: -14,217 (14), 1.0: -16,245 (20) |
| fert_buy | 11,406 | 0 | 0 | 0: -6,097 (1528), 2: -7,367 (46), 1: -9,079 (95), 3: -17,503 (2) |
| wheat_hold_days | 11,320 | 0 | 0 | 0: -6,039 (1575), 1: -10,204 (59), 2: -11,400 (34), 3: -17,359 (3) |
| open_sheep | 10,898 | 2 | 2 | 2: -5,736 (1543), 1: -11,489 (71), 3: -14,834 (34), 0: -16,634 (23) |
| MAX_SHEEP | 10,543 | 12 | 12 | 12: -5,353 (558), 14: -5,535 (636), 11: -7,345 (165), 9: -7,477 (28), 6: -8,828 (2), 10: -9,036 (54), 13: -9,173 (223), 4: -10,356 (2), 7: -15,896 (2) |
| feed_spare_poor | 10,141 | 0 | 0 | 0: -5,955 (1460), 2: -7,331 (22), 1: -8,708 (182), 3: -16,097 (7) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=66)
- (13, 3, 6): +14,567 (n=150)
- (7, 3, 5): +11,849 (n=30)
- (15, 3, 6): +11,582 (n=56)
- (10, 3, 6): +11,227 (n=165)
- (8, 3, 6): +11,158 (n=132)
- (17, 3, 6): +10,971 (n=65)
- (11, 3, 6): +10,963 (n=56)
- (17, 4, 6): +10,740 (n=6)
- (9, 4, 6): +10,652 (n=57)
- (16, 3, 6): +10,603 (n=25)
- (7, 4, 6): +10,358 (n=15)
- (8, 3, 4): +10,272 (n=35)
- (12, 4, 6): +10,123 (n=46)
- (9, 3, 6): +9,773 (n=158)

_Generated 2026-09-04 07:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._