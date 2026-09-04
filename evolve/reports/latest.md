# Evolution run 20260903-232024

Frontier opponent: `V3_12.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.00 h · candidates evaluated this run: 269 · games 17,532 (8,752/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 90 | 180 |
| dead_smoke | 19 | 152 |
| alive | 41 | 1968 |
| held_fail | 3 | 384 |
| held_pass | 116 | 14848 |
| error | 0 | 0 |

Population (all runs, reached dev): 643 · held-out evaluated: 418 · held-out PASS: 392

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | — | — | None-None | — | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `c956f895839b` | c1 | mutate | **+11,824** | 9.3 | 20-0 | -16,689 | +7,590 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1 · blocks: crop_admission | wheat_sell_price ?, NEAR_RADIUS ?, OPP_GROWTH ? | cand pulls ahead of C1 from day 10 (gap +2,987 -> final +14,339); days 8-15 drivers: missed_water -35, sales_rev +3,738, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `1021e7262bf2` | c1 | ablate:load_per_hand | **+11,382** | 8.7 | 20-0 | -23,063 | +7,069 | melon_floor 150→200, harvest_min 2→1, wheat_stock 0→5, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, early_hire_days 5→6, fert_carry 3→4, max_animals 20→18, wheat_cap 18→23, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, MELON_PRICE_CUSHION 100→130, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→13, OPENING_MELONS 10→6 · blocks: crop_admission |  | cand pulls ahead of C1 from day 10 (gap +2,991 -> final +22,781); days 8-15 drivers: missed_water -35, sales_rev +3,744, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `daba421dc7ec` | wide | ablate:ROUTE_LEN | **+11,274** | 13.0 | 19-1 | -14,917 | +10,939 | melon_floor 150→200, early_hire_days 5→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, MAX_SHEEP 12→11, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,079 -> final +42,744); days 10-17 drivers: missed_water -59, sales_rev +10,680, work_turns +118, feed_hour -0.63. Hands 11 vs 8, animals 15 vs 8, plants 43 v |
| `e83ac3dafe96` | v312 | ablate:CROP_SWEEP_RADIUS | **+11,099** | 10.3 | 20-0 | -12,184 | +10,740 | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→13, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 16 (gap +3,157 -> final +60,413); days 14-21 drivers: sales_rev +28,375, work_turns +302, feed_hour -1.31, travel_per_task -0.23. Hands 13 vs 11, animals 17 vs 8, plant |
| `a65aa7a26283` | v312 | ablate:open_cows | **+11,091** | 8.2 | 20-0 | -9,982 | +14,798 | melon_floor 150→200, min_hands 3→5, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, demand_share 0.5→0.45, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +1,962 -> final +53,812); days 10-17 drivers: missed_water -87, sales_rev +9,772, work_turns +143, feed_hour -1.33. Hands 9 vs 8, animals 14 vs 8, plants 60 vs  |
| `9d4a5923e4a2` | v312 | crossover | **+11,024** | 7.0 | 20-0 | -11,663 | +10,307 | open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission | melon_floor -25, early_hire_days +919, wheat_cap ?, wheat_sell_price ?, CROP_SWEEP_RADIUS -21, MELON_PRICE_CUSHION ? | cand pulls ahead of C1 from day 9 (gap +1,784 -> final +43,988); days 7-14 drivers: missed_water -44, sales_rev +6,420, work_turns +78, feed_hour -0.93. Hands 9 vs 7, animals 17 vs 8, plants 44 vs 64. |
| `8e3b811495ea` | v312 | ablate:load_per_hand | **+10,812** | 7.0 | 19-1 | -9,552 | +7,770 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→13, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +2,552 -> final +39,312); days 7-14 drivers: missed_water -34, sales_rev +5,424, work_turns +58, feed_hour -1.46. Hands 12 vs 7, animals 14 vs 8, plants 46 vs 64 |
| `c2747c8ab595` | queue | llm:llm_20260903-181110_2 | **+10,796** | 12.3 | 20-0 | -15,472 | +10,500 |  · blocks: crop_admission |  |  |
| `616d161b196b` | queue | coupled:coupled_factorial_sep03 | **+10,746** | 10.3 | 20-0 | -15,934 | +8,734 | fert_buy 0→1 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,078 -> final +18,552); days 10-17 drivers: missed_water -62, sales_rev +10,613, work_turns +123, feed_hour -0.65. Hands 11 vs 8, animals 15 vs 8, plants 42 v |
| `35f286364d59` | v312 | ablate:melon_floor | **+10,638** | 6.6 | 20-0 | -12,523 | +10,332 | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +1,784 -> final +44,147); days 7-14 drivers: missed_water -44, sales_rev +6,420, work_turns +78, feed_hour -0.93. Hands 9 vs 7, animals 17 vs 8, plants 44 vs 64. |
| `eb81a9bff031` | queue | ablate:MAX_HANDS | **+10,556** | 8.0 | 19-1 | -14,034 | +9,530 | harvest_min 2→1, wheat_stock 0→14, open_wheat 7→8, early_hire_days 5→7, wheat_cap 18→19, HERD_LAST_DAY 19→20, OPP_GROWTH 1.3→1.4 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +1,688 -> final +25,223); days 7-14 drivers: missed_water -21, sales_rev +4,179, work_turns +35, feed_hour -1.51. Hands 9 vs 7, animals 10 vs 8, plants 62 vs 64. |
| `d6b0d379d52a` | c1 | ablate:wheat_tiles | **+10,532** | 7.8 | 20-0 | -21,781 | +8,841 | melon_floor 150→200, wheat_stock 0→5, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, MELON_PRICE_CUSHION 100→129, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→13, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 10 (gap +2,991 -> final +22,616); days 8-15 drivers: missed_water -35, sales_rev +3,744, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `f206c22b6024` | v312 | ablate:melon_floor | **+10,457** | 6.7 | 20-0 | -10,345 | +9,793 | wheat_stock 0→5, open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→27, wheat_hold_days 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 14 (gap +2,246 -> final +54,003); days 12-19 drivers: sales_rev +22,917, missed_water -34, work_turns +160, feed_hour -0.81. Hands 11 vs 8, animals 15 vs 8, plants 57 v |
| `306df023fc92` | v312 | crossover | **+10,454** | 6.3 | 19-1 | -11,347 | +9,913 | melon_floor 150→200, wheat_stock 0→5, open_melons 8→5, open_wheat 7→9, open_cows 2→3, early_hire_days 5→8, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→27, wheat_hold_days 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission | melon_floor +120, wheat_tiles +5,058 | cand pulls ahead of C1 from day 14 (gap +2,246 -> final +54,277); days 12-19 drivers: sales_rev +20,817, missed_water -34, work_turns +160, feed_hour -0.81. Hands 11 vs 8, animals 15 vs 8, plants 57 v |
| `080778954358` | wide | ablate:MAX_SHEEP | **+10,382** | 8.2 | 20-0 | -18,862 | +7,787 | melon_floor 150→100, load_per_hand 20→15, open_wheat 7→8, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4, MAX_SHEEP 12→11 · blocks: crop_admission |  | cand falls behind C1 from day 24 (gap -4,385 -> final -7,079); days 22-29 drivers: sales_rev -7,230, idle_turns +142, water_hour +2.37. Hands 4 vs 3, animals 8 vs 9, plants 0 vs 0. |

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
| `b1b4de2e23d7` | v312 | ablate:ROUTE_LEN | +11,227 | 7.4 | 10-0 | -7,017 | held_pass | load_per_hand 20→18, wheat_cap 18→21, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `2ed37e718be7` | queue | ablate:fert_keep | +11,161 | 5.6 | 10-0 | -13,859 | held_pass | open_wheat 7→8, early_hire_days 5→4 · blocks: crop_admission |
| `5eeb0745fc2d` | queue | ablate:NEAR_RADIUS | +11,160 | 5.6 | 10-0 | -12,708 | held_pass | melon_floor 150→100, open_wheat 7→8 · blocks: crop_admission |
| `618e2a2e39c0` | v312 | ablate:CROP_SWEEP_RADIUS | +11,158 | 6.5 | 10-0 | -10,852 | held_pass | open_wheat 7→9, wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `9e0ffe61daf5` | v312 | crossover | +10,971 | 13.1 | 10-0 | -18,795 | held_pass | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→13, OPENING_MELONS 10→11 · blocks: crop_admission |
| `fe09c53a316a` | queue | ablate:melon_floor | +10,967 | 4.9 | 10-0 | -13,451 | held_pass | open_wheat 7→8, early_hire_days 5→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |

## Islands (best dev margin, population size)

- c1: best +14,567 (`8c6f5b00cc43`), n=133
- queue: best +12,820 (`e4a45816755f`), n=195
- v312: best +14,798 (`a65aa7a26283`), n=198
- wide: best +10,939 (`daba421dc7ec`), n=117

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| ROUTE_LEN | 13,628 | 3 | 3 | 3: +5,092 (536), 2: +2,964 (59), 4: +158 (46), 5: -8,536 (2) |
| wheat_stock | 10,600 | 14 | 0 | 14: +9,666 (2), 16: +8,294 (3), 5: +7,001 (12), 2: +5,988 (23), 12: +5,423 (2), 10: +5,178 (8), 0: +4,531 (556), 7: +2,707 (14), 1: +2,194 (2), 21: +2,066 (6), 6: +2,040 (2), 13: +271 (3), 4: -934 (7) |
| demand_share | 10,332 | 0.4 | 0.5 | 0.4: +5,706 (17), 0.5: +5,174 (453), 0.45: +5,064 (90), 0.55: +2,138 (21), 0.8: +1,684 (4), 0.75: +967 (13), 0.35: +934 (6), 0.6: -945 (4), 0.3: -1,071 (19), 0.7: -2,257 (13), 0.65: -4,626 (2) |
| wheat_per_animal | 9,583 | 0.1 | 0.0 | 0.1: +5,528 (119), 0.0: +4,531 (467), 0.2: +3,883 (32), 0.6: +2,354 (2), 0.5: -166 (14), 0.3: -237 (6), 0.4: -4,055 (2) |
| wheat_sell_price | 9,544 | 27 | 30 | 27: +6,190 (55), 35: +5,612 (8), 29: +5,010 (11), 30: +4,727 (385), 28: +4,611 (33), 38: +4,550 (6), 37: +4,195 (14), 50: +3,904 (44), 31: +3,598 (19), 25: +3,247 (52), 32: +1,337 (4), 44: +763 (3), 33: -1,887 (2), 26: -3,354 (3) |
| MELON_MAX_TILES | 8,482 | 43 | 40 | 43: +6,910 (8), 31: +5,940 (12), 41: +5,422 (194), 44: +4,793 (9), 50: +4,440 (106), 40: +4,189 (272), 47: +4,025 (8), 35: +3,923 (3), 34: +2,190 (2), 42: +2,182 (3), 37: +1,993 (3), 32: +28 (6), 45: -22 (3), 38: -31 (4), 39: -723 (3), 26: -1,571 (2) |
| MELON_PRICE_CUSHION | 8,118 | 127 | 100 | 127: +7,238 (29), 130: +7,092 (3), 133: +6,445 (2), 129: +6,128 (6), 98: +5,991 (8), 74: +5,125 (18), 120: +4,748 (4), 83: +4,646 (5), 100: +4,543 (508), 114: +4,537 (23), 112: +3,357 (2), 105: +3,227 (4), 134: +1,227 (2), 93: +606 (2), 50: -880 (9) |
| wheat_cap | 7,442 | 20 | 18 | 20: +6,841 (48), 17: +6,829 (14), 19: +6,803 (4), 14: +5,819 (7), 23: +4,964 (6), 21: +4,577 (14), 15: +4,474 (149), 18: +4,288 (379), 12: +1,547 (4), 22: +743 (4), 25: +728 (6), 24: +98 (2), 13: -602 (3) |
| open_sheep | 7,421 | 2 | 2 | 2: +4,695 (618), 1: +568 (16), 0: +43 (3), 3: -2,725 (6) |
| min_hands | 7,335 | 5 | 3 | 5: +6,101 (31), 3: +4,466 (597), 4: +3,223 (13), 6: -1,234 (2) |
| NEAR_RADIUS | 6,841 | 2 | 3 | 2: +5,230 (257), 3: +4,277 (339), 4: +2,793 (40), 5: -1,611 (7) |
| load_per_hand | 6,752 | 16 | 20 | 16: +5,710 (48), 20: +4,645 (453), 19: +4,487 (47), 15: +4,112 (32), 18: +3,949 (26), 22: +3,776 (7), 21: +2,346 (15), 23: +2,244 (4), 13: +538 (5), 14: -119 (2), 17: -1,042 (2) |
| HERD_LAST_DAY | 6,463 | 16 | 19 | 16: +6,071 (5), 19: +4,630 (385), 20: +4,485 (81), 22: +4,479 (150), 18: +2,819 (12), 21: +2,359 (6), 17: -392 (4) |
| opening | 6,369 | frontier | frontier | frontier: +4,927 (600), v312: -1,442 (43) |
| early_hire_days | 6,366 | 7 | 5 | 7: +6,919 (31), 4: +5,509 (93), 3: +5,032 (23), 8: +5,014 (29), 5: +4,294 (431), 2: +3,219 (2), 1: +2,511 (7), 6: +1,689 (15), 0: +553 (12) |
| fert_keep | 6,118 | 0 | 0 | 0: +4,592 (548), 1: +4,209 (79), 2: +3,839 (13), 3: -1,525 (3) |
| STRAW_CUTOFF | 5,625 | 16 | 17 | 16: +5,009 (116), 19: +4,725 (15), 17: +4,629 (442), 15: +4,599 (14), 12: +2,817 (28), 18: +2,218 (24), 14: -616 (3) |
| open_wheat | 5,549 | 8 | 7 | 8: +5,405 (191), 9: +5,231 (184), 3: +3,819 (18), 5: +3,725 (6), 7: +3,459 (215), 4: +2,886 (14), 6: +2,267 (11), 10: -144 (4) |
| MAX_HANDS | 5,473 | 13 | 13 | 13: +4,884 (488), 11: +4,707 (16), 15: +3,693 (24), 12: +3,571 (72), 16: +3,332 (17), 14: +1,624 (22), 10: -588 (4) |
| CROP_SWEEP_RADIUS | 5,173 | 3 | 4 | 3: +5,984 (114), 2: +5,814 (42), 4: +4,333 (430), 5: +1,941 (52), 6: +811 (5) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=38)
- (13, 3, 6): +14,567 (n=68)
- (7, 3, 5): +11,849 (n=24)
- (15, 3, 6): +11,582 (n=19)
- (10, 3, 6): +11,227 (n=71)
- (8, 3, 6): +11,158 (n=39)
- (17, 3, 6): +10,971 (n=29)
- (11, 3, 6): +10,963 (n=20)
- (17, 4, 6): +10,740 (n=5)
- (9, 4, 6): +10,652 (n=18)
- (7, 4, 6): +10,358 (n=11)
- (8, 3, 4): +10,272 (n=22)
- (12, 4, 6): +10,123 (n=4)
- (9, 3, 6): +9,773 (n=33)
- (12, 3, 5): +9,597 (n=1)

_Generated 2026-09-04 01:20. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._