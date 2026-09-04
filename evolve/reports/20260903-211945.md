# Evolution run 20260903-211945

Frontier opponent: `V3_12.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.01 h · candidates evaluated this run: 277 · games 19,522 (9,731/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 69 | 138 |
| dead_smoke | 31 | 248 |
| alive | 44 | 2112 |
| held_fail | 13 | 1664 |
| held_pass | 120 | 15360 |
| error | 0 | 0 |

Population (all runs, reached dev): 483 · held-out evaluated: 299 · held-out PASS: 276

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | — | — | None-None | — | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `c956f895839b` | c1 | mutate | **+11,824** | 9.3 | 20-0 | -16,689 | +7,590 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, wheat_sell_price 30→29, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1 · blocks: crop_admission | wheat_sell_price ?, NEAR_RADIUS ?, OPP_GROWTH ? | cand pulls ahead of C1 from day 10 (gap +2,987 -> final +14,339); days 8-15 drivers: missed_water -35, sales_rev +3,738, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `daba421dc7ec` | wide | ablate:ROUTE_LEN | **+11,274** | 13.0 | 19-1 | -14,917 | +10,939 | melon_floor 150→200, early_hire_days 5→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, MAX_SHEEP 12→11, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,079 -> final +42,744); days 10-17 drivers: missed_water -59, sales_rev +10,680, work_turns +118, feed_hour -0.63. Hands 11 vs 8, animals 15 vs 8, plants 43 v |
| `a65aa7a26283` | v312 | ablate:open_cows | **+11,091** | 8.2 | 20-0 | -9,982 | +14,798 | melon_floor 150→200, min_hands 3→5, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, demand_share 0.5→0.45, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +1,962 -> final +53,812); days 10-17 drivers: missed_water -87, sales_rev +9,772, work_turns +143, feed_hour -1.33. Hands 9 vs 8, animals 14 vs 8, plants 60 vs  |
| `c2747c8ab595` | queue | llm:llm_20260903-181110_2 | **+10,796** | 12.3 | 20-0 | -15,472 | +10,500 |  · blocks: crop_admission |  |  |
| `616d161b196b` | queue | coupled:coupled_factorial_sep03 | **+10,746** | 10.3 | 20-0 | -15,934 | +8,734 | fert_buy 0→1 · blocks: crop_admission |  | cand pulls ahead of C1 from day 12 (gap +7,078 -> final +18,552); days 10-17 drivers: missed_water -62, sales_rev +10,613, work_turns +123, feed_hour -0.65. Hands 11 vs 8, animals 15 vs 8, plants 42 v |
| `eb81a9bff031` | queue | ablate:MAX_HANDS | **+10,556** | 8.0 | 19-1 | -14,034 | +9,530 | harvest_min 2→1, wheat_stock 0→14, open_wheat 7→8, early_hire_days 5→7, wheat_cap 18→19, HERD_LAST_DAY 19→20, OPP_GROWTH 1.3→1.4 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +1,688 -> final +25,223); days 7-14 drivers: missed_water -21, sales_rev +4,179, work_turns +35, feed_hour -1.51. Hands 9 vs 7, animals 10 vs 8, plants 62 vs 64. |
| `d6b0d379d52a` | c1 | ablate:wheat_tiles | **+10,532** | 7.8 | 20-0 | -21,781 | +8,841 | melon_floor 150→200, wheat_stock 0→5, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, MELON_PRICE_CUSHION 100→129, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→13, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 10 (gap +2,991 -> final +22,616); days 8-15 drivers: missed_water -35, sales_rev +3,744, work_turns +50, feed_hour -0.56. Hands 11 vs 8, animals 10 vs 8, plants 65 vs 6 |
| `080778954358` | wide | ablate:MAX_SHEEP | **+10,382** | 8.2 | 20-0 | -18,862 | +7,787 | melon_floor 150→100, load_per_hand 20→15, open_wheat 7→8, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4, MAX_SHEEP 12→11 · blocks: crop_admission |  | cand falls behind C1 from day 24 (gap -4,385 -> final -7,079); days 22-29 drivers: sales_rev -7,230, idle_turns +142, water_hour +2.37. Hands 4 vs 3, animals 8 vs 9, plants 0 vs 0. |
| `c7307de95966` | v312 | ablate:CROP_SWEEP_LEN | **+10,368** | 8.3 | 20-0 | -9,160 | +9,287 | melon_floor 150→200, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 13 (gap +4,492 -> final +41,843); days 11-18 drivers: sales_rev +13,250, missed_water -56, work_turns +80, feed_hour -1.19. Hands 9 vs 10, animals 11 vs 8, plants 53 vs |
| `b1b4de2e23d7` | v312 | ablate:ROUTE_LEN | **+10,312** | 10.1 | 19-1 | -14,775 | +11,227 | load_per_hand 20→18, wheat_cap 18→21, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |  | cand pulls ahead of C1 from day 23 (gap +3,923 -> final +33,316); days 21-28 drivers: sales_rev +25,546, work_turns +130, missed_water -20, weeds_new -2. Hands 13 vs 8, animals 11 vs 9, plants 50 vs 2 |
| `62ed32b18967` | queue | ablate:MAX_HANDS | **+10,309** | 11.7 | 20-0 | -15,001 | +9,750 | harvest_min 2→1, wheat_sell_price 30→25, HERD_LAST_DAY 19→20, OPP_GROWTH 1.3→1.4 · blocks: crop_admission |  |  |
| `0d032724cbc2` | c1 | mutate | **+10,225** | 6.8 | 19-1 | -13,965 | +8,785 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, OPP_GROWTH 1.3→1.4 · blocks: crop_admission | load_per_hand -55, wheat_water_tier +1,841, CROP_SWEEP_LEN -465, MELON_MAX_TILES ? | cand pulls ahead of C1 from day 25 (gap +3,800 -> final +12,221); days 23-29 drivers: sales_rev +17,957, work_turns +100, missed_water -16, weeds_new -3. Hands 6 vs 3, animals 8 vs 9, plants 40 vs 0. |
| `b75cc81a7418` | v312 | ablate:load_per_hand | **+10,224** | 7.3 | 20-0 | -15,493 | +9,528 | melon_floor 150→200, harvest_min 2→3, wheat_tiles 0→4, open_melons 8→6, open_wheat 7→9, open_cows 2→3, fert_carry 3→4, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.2, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→28, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, MAX_SHEEP 12→14, OPENING_MELONS 10→8 · blocks: crop_admission |  | cand pulls ahead of C1 from day 15 (gap +3,350 -> final +21,010); days 13-20 drivers: sales_rev +23,490, work_turns +157, missed_water -15, feed_hour -0.65. Hands 12 vs 13, animals 15 vs 8, plants 54  |
| `07723e02d482` | queue | ablate:demand_share | **+10,142** | 9.0 | 20-0 | -11,659 | +10,214 | load_per_hand 20→19, open_wheat 7→8, early_hire_days 5→3, CROP_SWEEP_RADIUS 4→3 · blocks: crop_admission |  | cand vs C1: net worth never diverged by >$1,500 (final -114). |
| `03f250568de1` | v312 | ablate:load_per_hand | **+10,115** | 7.0 | 19-1 | -13,050 | +6,852 | melon_floor 150→200, harvest_min 2→1, wheat_stock 0→7, open_melons 8→5, open_wheat 7→9, feed_spare_poor 0→1, demand_share 0.5→0.45, max_animals 20→16, wheat_cap 18→15, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→7 · blocks: crop_admission |  | cand pulls ahead of C1 from day 9 (gap +1,700 -> final +27,797); days 7-14 drivers: missed_water -24, sales_rev +4,183, work_turns +59, feed_hour -1.39. Hands 9 vs 7, animals 12 vs 8, plants 60 vs 64. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `a65aa7a26283` | v312 | ablate:open_cows | +14,798 | 3.4 | 9-1 | -12,652 | held_pass | melon_floor 150→200, min_hands 3→5, load_per_hand 20→16, open_melons 8→5, open_wheat 7→9, open_cows 2→3, feed_spare_poor 0→1, demand_share 0.5→0.45, max_animals 20→17, wheat_cap 18→20, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `e4a45816755f` | queue | ablate:NEAR_RADIUS | +12,820 | 11.0 | 10-0 | -3,176 | held_pass | open_wheat 7→8, early_hire_days 5→4, fert_keep 0→1, CROP_SWEEP_RADIUS 4→2 · blocks: crop_admission |
| `64476e04983d` | v312 | ablate:open_wheat | +11,849 | 6.1 | 10-0 | -16,943 | held_pass | wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `f8be9cdc3861` | v312 | ablate:wheat_tiles | +11,582 | 6.0 | 10-0 | -17,834 | held_pass | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `974a722e40d2` | queue | ablate:MAX_SHEEP | +11,545 | 5.7 | 10-0 | -14,402 | held_pass | harvest_min 2→1, open_wheat 7→8, early_hire_days 5→7, HERD_LAST_DAY 19→20 · blocks: crop_admission |
| `b1b4de2e23d7` | v312 | ablate:ROUTE_LEN | +11,227 | 7.4 | 10-0 | -7,017 | held_pass | load_per_hand 20→18, wheat_cap 18→21, wheat_water_tier 0→1, wheat_sell_price 30→27, CROP_SWEEP_RADIUS 4→3, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `2ed37e718be7` | queue | ablate:fert_keep | +11,161 | 5.6 | 10-0 | -13,859 | held_pass | open_wheat 7→8, early_hire_days 5→4 · blocks: crop_admission |
| `5eeb0745fc2d` | queue | ablate:NEAR_RADIUS | +11,160 | 5.6 | 10-0 | -12,708 | held_pass | melon_floor 150→100, open_wheat 7→8 · blocks: crop_admission |
| `618e2a2e39c0` | v312 | ablate:CROP_SWEEP_RADIUS | +11,158 | 6.5 | 10-0 | -10,852 | held_pass | open_wheat 7→9, wheat_per_animal 0.0→0.1, wheat_cap 18→20, wheat_water_tier 0→1, wheat_sell_price 30→27, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→127, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |
| `fe09c53a316a` | queue | ablate:melon_floor | +10,967 | 4.9 | 10-0 | -13,451 | held_pass | open_wheat 7→8, early_hire_days 5→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `de4e1e1f2dc2` | queue | crossover | +10,965 | 4.9 | 10-0 | -12,299 | held_pass | melon_floor 150→0, open_wheat 7→8, early_hire_days 5→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `daba421dc7ec` | wide | ablate:ROUTE_LEN | +10,939 | 5.4 | 10-0 | -14,084 | held_pass | melon_floor 150→200, early_hire_days 5→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, MAX_SHEEP 12→11, OPENING_MELONS 10→7 · blocks: crop_admission |
| `f2e8414b9e0e` | v312 | ablate:MAX_HANDS | +10,652 | 3.2 | 10-0 | -16,665 | held_pass | melon_floor 150→200, harvest_min 2→1, wheat_tiles 0→2, open_melons 8→5, open_wheat 7→9, open_cows 2→3, fert_carry 3→2, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.2, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→28, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `c2747c8ab595` | queue | llm:llm_20260903-181110_2 | +10,500 | 4.4 | 10-0 | -12,480 | held_pass |  · blocks: crop_admission |
| `4a1ce10d69bb` | v312 | ablate:demand_share | +10,487 | 3.4 | 10-0 | -15,811 | held_pass | melon_floor 150→200, harvest_min 2→3, wheat_tiles 0→2, open_melons 8→5, open_wheat 7→9, open_cows 2→3, fert_carry 3→2, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.2, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→28, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→9 · blocks: crop_admission |

## Islands (best dev margin, population size)

- c1: best +9,855 (`815f4fb4f6db`), n=93
- queue: best +12,820 (`e4a45816755f`), n=146
- v312: best +14,798 (`a65aa7a26283`), n=154
- wide: best +10,939 (`daba421dc7ec`), n=90

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| ROUTE_LEN | 13,394 | 3 | 3 | 3: +4,858 (390), 2: +3,047 (54), 4: -298 (37), 5: -8,536 (2) |
| wheat_sell_price | 11,670 | 35 | 30 | 35: +7,625 (3), 27: +6,010 (31), 29: +5,010 (11), 28: +4,597 (29), 38: +4,550 (6), 30: +4,361 (287), 50: +3,965 (34), 31: +3,845 (17), 25: +3,421 (44), 37: +2,388 (9), 32: +1,447 (2), 44: +763 (3), 26: -4,045 (2) |
| wheat_stock | 10,600 | 14 | 0 | 14: +9,666 (2), 10: +7,215 (3), 2: +6,308 (9), 5: +6,151 (5), 0: +4,319 (429), 7: +2,807 (13), 1: +2,194 (2), 6: +2,040 (2), 21: +1,237 (5), 13: +823 (2), 4: -934 (7) |
| demand_share | 10,523 | 0.4 | 0.5 | 0.4: +5,897 (10), 0.45: +5,360 (73), 0.5: +4,913 (324), 0.55: +1,851 (20), 0.8: +1,612 (3), 0.75: +967 (13), 0.35: +160 (5), 0.6: -945 (4), 0.3: -1,345 (16), 0.7: -1,883 (12), 0.65: -4,626 (2) |
| early_hire_days | 10,009 | 7 | 5 | 7: +8,410 (10), 3: +5,646 (18), 4: +5,183 (66), 8: +4,255 (10), 5: +4,110 (354), 6: +742 (9), 0: +584 (11), 1: -1,599 (4) |
| wheat_per_animal | 9,765 | 0.1 | 0.0 | 0.1: +5,710 (81), 0.0: +4,168 (348), 0.2: +4,125 (30), 0.6: +2,354 (2), 0.3: -237 (6), 0.5: -337 (13), 0.4: -4,055 (2) |
| MELON_PRICE_CUSHION | 9,749 | 127 | 100 | 127: +7,982 (15), 129: +6,128 (6), 74: +5,650 (12), 120: +4,748 (4), 83: +4,646 (5), 100: +4,313 (395), 114: +3,844 (18), 112: +3,357 (2), 105: +3,227 (4), 50: -1,767 (8) |
| load_per_hand | 9,643 | 16 | 20 | 16: +5,804 (35), 19: +4,757 (35), 20: +4,296 (338), 15: +3,845 (28), 22: +3,776 (7), 18: +2,846 (16), 21: +2,576 (14), 23: +2,244 (4), 17: -1,042 (2), 13: -3,839 (3) |
| MELON_MAX_TILES | 8,759 | 31 | 40 | 31: +5,940 (12), 41: +5,269 (139), 50: +4,520 (86), 47: +3,879 (2), 40: +3,800 (217), 44: +2,226 (2), 42: +2,182 (3), 37: +1,014 (2), 32: +618 (5), 45: -22 (3), 39: -723 (3), 38: -2,819 (2) |
| wheat_cap | 7,405 | 19 | 18 | 19: +6,803 (4), 20: +6,409 (36), 17: +5,234 (3), 21: +4,728 (13), 15: +4,426 (111), 18: +3,985 (293), 14: +2,867 (3), 25: +2,221 (5), 22: +1,965 (3), 12: +1,547 (4), 24: +98 (2), 13: -602 (3) |
| MAX_HANDS | 7,145 | 11 | 13 | 11: +5,673 (10), 13: +4,480 (354), 15: +3,693 (24), 12: +3,677 (60), 16: +3,537 (15), 14: +1,806 (17), 10: -1,472 (3) |
| CROP_SWEEP_RADIUS | 7,037 | 3 | 4 | 3: +5,949 (84), 2: +5,007 (23), 4: +4,109 (321), 5: +1,995 (51), 6: -1,089 (4) |
| NEAR_RADIUS | 6,985 | 2 | 3 | 2: +5,072 (184), 3: +3,937 (262), 4: +2,515 (31), 5: -1,914 (6) |
| open_sheep | 6,862 | 2 | 2 | 2: +4,371 (469), 0: +43 (3), 1: -1,295 (7), 3: -2,491 (4) |
| OPENING_MELONS | 6,375 | 7 | 10 | 7: +5,533 (17), 11: +4,573 (137), 10: +4,183 (274), 6: +3,989 (14), 8: +3,712 (13), 9: +3,568 (9), 13: +2,611 (2), 14: +2,265 (12), 12: -842 (5) |
| opening | 6,026 | frontier | frontier | frontier: +4,555 (455), v312: -1,471 (28) |
| fert_keep | 5,843 | 0 | 0 | 0: +4,318 (414), 1: +3,799 (59), 2: +3,421 (7), 3: -1,525 (3) |
| open_wheat | 5,640 | 8 | 7 | 8: +5,122 (119), 9: +5,065 (146), 3: +4,121 (7), 7: +3,242 (185), 4: +2,677 (12), 5: +2,305 (2), 6: +2,048 (9), 10: -518 (3) |
| STRAW_CUTOFF | 5,622 | 16 | 17 | 16: +5,006 (101), 15: +4,306 (13), 17: +4,292 (318), 12: +2,293 (17), 18: +2,258 (22), 19: +1,992 (8), 14: -616 (3) |
| OPP_GROWTH | 5,493 | 1.4 | 1.3 | 1.4: +4,511 (52), 1.3: +4,431 (358), 1.1: +4,069 (19), 1.5: +3,145 (29), 1.0: +2,855 (2), 1.6: +1,820 (20), 1.2: -983 (2) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (14, 3, 6): +14,798 (n=29)
- (13, 3, 6): +12,820 (n=51)
- (7, 3, 5): +11,849 (n=19)
- (15, 3, 6): +11,582 (n=11)
- (10, 3, 6): +11,227 (n=59)
- (8, 3, 6): +11,158 (n=30)
- (9, 4, 6): +10,652 (n=12)
- (7, 4, 6): +10,358 (n=10)
- (12, 4, 6): +10,123 (n=4)
- (9, 3, 6): +9,773 (n=29)
- (12, 3, 5): +9,597 (n=1)
- (17, 3, 6): +9,492 (n=16)
- (8, 4, 6): +9,450 (n=12)
- (13, 2, 5): +9,389 (n=2)
- (8, 2, 3): +9,354 (n=7)

_Generated 2026-09-03 23:20. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._