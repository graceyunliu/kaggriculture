# Evolution run 20260904-094442

Frontier opponent: `H10.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.01 h · candidates evaluated this run: 465 · games 18,774 (9,354/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 11 | 22 |
| dead_smoke | 76 | 608 |
| alive | 378 | 18144 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 2416 · held-out evaluated: 477 · held-out PASS: 448

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

- c1: best +14,567 (`8c6f5b00cc43`), n=612
- queue: best +12,820 (`e4a45816755f`), n=670
- v312: best +14,798 (`a65aa7a26283`), n=683
- wide: best +10,939 (`daba421dc7ec`), n=451

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| demand_share | 26,766 | 0.8 | 0.5 | 0.8: +1,684 (4), 0.75: -2,590 (16), 0.7: -5,768 (29), 0.5: -8,189 (1623), 0.45: -8,891 (337), 0.4: -10,009 (64), 0.55: -10,955 (133), 0.35: -12,966 (27), 0.3: -13,987 (74), 0.6: -14,569 (75), 0.65: -14,638 (24), 0.95: -16,393 (3), 0.85: -24,619 (2), 1.0: -25,082 (4) |
| MELON_PRICE_CUSHION | 22,714 | 145 | 100 | 145: +1,855 (4), 74: -507 (26), 130: -1,957 (5), 98: -2,288 (15), 83: -3,499 (8), 120: -3,720 (7), 114: -4,027 (43), 72: -5,795 (2), 131: -6,046 (8), 134: -6,719 (4), 127: -7,255 (135), 100: -8,059 (1635), 124: -9,180 (2), 144: -9,580 (2), 105: -10,132 (13), 112: -10,475 (7), 129: -10,691 (33), 67: -10,721 (3), 117: -10,962 (7), 97: -11,235 (7), 50: -11,516 (22), 140: -11,523 (3), 91: -11,808 (2), 78: -11,836 (5), 92: -11,941 (3), 133: -12,026 (19), 59: -12,065 (2), 116: -12,184 (47), 135: -12,487 (2), 101: -12,505 (23), 119: -12,669 (4), 96: -12,799 (21), 85: -13,025 (20), 93: -13,172 (12), 150: -13,289 (35), 94: -13,382 (7), 69: -13,405 (3), 106: -13,489 (5), 90: -13,496 (17), 65: -14,104 (2), 89: -14,140 (4), 115: -14,354 (11), 88: -14,563 (6), 118: -14,863 (7), 95: -14,876 (4), 123: -14,891 (15), 125: -14,929 (8), 73: -15,145 (3), 132: -15,310 (5), 107: -15,499 (12), 113: -15,511 (4), 75: -15,547 (4), 84: -15,624 (4), 109: -15,672 (7), 102: -15,675 (3), 137: -15,708 (2), 66: -15,749 (11), 110: -15,883 (5), 80: -15,929 (2), 126: -16,198 (2), 79: -16,703 (10), 77: -16,735 (2), 82: -16,844 (3), 139: -16,868 (2), 111: -16,967 (11), 76: -17,160 (4), 99: -17,529 (3), 103: -17,571 (2), 108: -17,642 (3), 63: -18,295 (2), 81: -18,397 (8), 122: -18,415 (2), 136: -19,272 (3), 60: -20,456 (2), 62: -20,859 (3) |
| wheat_stock | 19,297 | 16 | 0 | 16: -1,895 (5), 21: -5,788 (10), 7: -6,781 (29), 5: -7,799 (56), 0: -8,436 (1896), 10: -8,854 (32), 13: -9,160 (11), 2: -9,614 (103), 12: -9,956 (35), 14: -11,028 (13), 1: -12,214 (45), 4: -12,692 (77), 6: -12,995 (26), 11: -13,073 (18), 15: -14,437 (4), 9: -15,105 (8), 3: -15,228 (23), 17: -15,637 (2), 35: -17,198 (2), 8: -17,902 (6), 23: -19,111 (2), 28: -19,249 (2), 40: -20,803 (2), 22: -21,192 (2) |
| wheat_tiles | 18,660 | 3 | 0 | 3: -6,046 (53), 0: -8,748 (2112), 4: -8,895 (19), 2: -10,636 (78), 1: -11,423 (146), 5: -20,748 (3), 6: -22,648 (2), 8: -24,707 (2) |
| MELON_MAX_TILES | 16,065 | 41 | 40 | 41: -6,646 (571), 40: -8,167 (894), 44: -8,420 (26), 32: -8,821 (13), 50: -9,053 (348), 47: -9,562 (36), 31: -9,953 (48), 45: -10,565 (15), 27: -11,090 (3), 35: -11,292 (20), 26: -11,379 (4), 37: -11,555 (64), 23: -12,094 (3), 39: -12,785 (19), 38: -12,825 (80), 43: -12,882 (112), 46: -13,036 (7), 34: -13,190 (48), 42: -13,761 (20), 48: -13,906 (6), 49: -14,221 (32), 29: -14,376 (2), 36: -14,643 (8), 33: -15,012 (10), 30: -15,232 (7), 22: -15,686 (7), 28: -16,574 (6), 25: -18,308 (3), 20: -22,711 (3) |
| load_per_hand | 15,973 | 19 | 20 | 19: -7,543 (166), 20: -7,712 (1453), 22: -9,181 (40), 18: -10,089 (135), 16: -10,819 (270), 15: -10,851 (145), 13: -10,917 (14), 21: -12,004 (69), 23: -12,376 (25), 17: -13,983 (39), 14: -14,137 (12), 24: -16,611 (12), 25: -19,642 (5), 12: -19,870 (20), 26: -23,516 (11) |
| wheat_sell_price | 14,615 | 38 | 30 | 38: -4,651 (12), 37: -5,502 (25), 27: -5,929 (191), 28: -6,504 (103), 50: -6,692 (99), 31: -7,663 (45), 47: -8,727 (2), 35: -8,840 (24), 30: -9,087 (1535), 25: -9,139 (148), 44: -9,542 (9), 29: -9,812 (54), 32: -11,474 (25), 33: -13,933 (23), 36: -14,688 (28), 34: -15,417 (37), 26: -15,463 (34), 41: -15,600 (4), 43: -15,862 (3), 40: -16,149 (4), 45: -16,302 (2), 39: -19,266 (6) |
| MAX_HANDS | 13,713 | 13 | 13 | 13: -8,183 (1728), 16: -8,775 (39), 11: -9,073 (77), 15: -10,133 (85), 12: -11,006 (350), 14: -11,315 (99), 10: -13,826 (24), 9: -20,197 (7), 8: -21,896 (7) |
| max_animals | 13,673 | 17 | 20 | 17: -8,093 (490), 20: -8,660 (1644), 16: -9,514 (51), 18: -10,536 (76), 19: -12,836 (105), 15: -14,458 (29), 13: -14,606 (6), 12: -18,552 (4), 14: -20,091 (6), 10: -21,766 (4) |
| wheat_per_animal | 12,786 | 0.1 | 0.0 | 0.1: -6,608 (385), 0.0: -8,914 (1709), 0.6: -9,239 (8), 0.5: -9,497 (34), 0.2: -11,004 (170), 0.8: -11,135 (3), 0.3: -13,454 (76), 0.9: -16,472 (3), 0.4: -16,783 (22), 1.2: -19,394 (5) |
| STRAW_CUTOFF | 11,845 | 12 | 17 | 12: -6,406 (50), 19: -7,772 (43), 17: -8,001 (1428), 16: -8,301 (423), 18: -10,764 (176), 15: -12,722 (148), 14: -14,432 (88), 20: -16,456 (52), 13: -18,251 (8) |
| ROUTE_LEN | 11,099 | 3 | 3 | 3: -8,683 (2079), 2: -9,983 (204), 4: -11,224 (126), 5: -19,782 (7) |
| open_melons | 11,049 | 5 | 8 | 5: -7,828 (515), 8: -8,283 (1076), 10: -8,454 (167), 6: -9,621 (222), 7: -10,355 (181), 11: -10,686 (32), 9: -12,050 (95), 4: -13,515 (100), 12: -13,562 (17), 14: -18,615 (4), 13: -18,877 (7) |
| wheat_cap | 10,951 | 15 | 18 | 15: -6,357 (380), 23: -6,618 (22), 18: -7,512 (1088), 14: -8,477 (24), 21: -8,842 (80), 8: -9,125 (5), 17: -10,296 (91), 20: -10,402 (327), 12: -11,714 (27), 22: -12,205 (25), 24: -13,930 (21), 19: -14,061 (69), 13: -14,194 (79), 16: -14,369 (69), 25: -14,400 (64), 11: -14,414 (10), 5: -14,594 (9), 6: -14,993 (3), 7: -15,530 (14), 9: -17,308 (8) |
| fert_buy | 10,163 | 0 | 0 | 0: -8,382 (2062), 2: -10,933 (87), 1: -12,604 (260), 3: -18,545 (7) |
| MAX_SHEEP | 9,742 | 12 | 12 | 12: -7,280 (709), 11: -8,962 (205), 14: -9,035 (1007), 9: -10,104 (39), 4: -10,967 (3), 13: -11,148 (362), 10: -11,269 (80), 6: -14,949 (4), 7: -16,315 (4), 8: -17,022 (2) |
| OPP_GROWTH | 9,403 | 1.3 | 1.3 | 1.3: -7,197 (1393), 1.6: -8,017 (72), 1.1: -8,143 (83), 1.4: -10,137 (322), 1.5: -10,765 (240), 1.2: -14,324 (205), 1.7: -14,746 (43), 1.0: -16,102 (38), 1.8: -16,601 (20) |
| open_wheat | 9,230 | 3 | 7 | 3: -5,197 (30), 7: -7,044 (547), 9: -8,108 (704), 4: -8,829 (31), 8: -9,644 (865), 6: -12,391 (54), 10: -14,154 (109), 5: -14,426 (76) |
| opening | 9,172 | frontier | frontier | frontier: -7,564 (2049), v312: -16,736 (367) |
| open_sheep | 9,136 | 2 | 2 | 2: -8,378 (2209), 1: -13,801 (112), 3: -16,014 (51), 0: -17,515 (44) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=92)
- (13, 3, 6): +14,567 (n=188)
- (7, 3, 5): +11,849 (n=33)
- (15, 3, 6): +11,582 (n=86)
- (10, 3, 6): +11,227 (n=234)
- (8, 3, 6): +11,158 (n=233)
- (17, 3, 6): +10,971 (n=77)
- (11, 3, 6): +10,963 (n=96)
- (17, 4, 6): +10,740 (n=6)
- (9, 4, 6): +10,652 (n=76)
- (16, 3, 6): +10,603 (n=31)
- (7, 4, 6): +10,358 (n=19)
- (8, 3, 4): +10,272 (n=48)
- (12, 4, 6): +10,123 (n=68)
- (9, 3, 6): +9,773 (n=266)

_Generated 2026-09-04 11:45. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._