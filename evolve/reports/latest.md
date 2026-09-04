# Evolution run 20260903-191532

Frontier opponent: `V3_12.py` · clone: `tape_milanleonard_102563171.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_7bd4980c7158.py` (sha `7bd4980c7158`)
Elapsed 2.00 h · candidates evaluated this run: 303 · games 19,174 (9,584/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 75 | 150 |
| dead_smoke | 32 | 256 |
| alive | 79 | 3792 |
| held_fail | 5 | 640 |
| held_pass | 112 | 14336 |
| error | 0 | 0 |

Population (all runs, reached dev): 306 · held-out evaluated: 166 · held-out PASS: 156

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | — | — | None-None | — | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `c2747c8ab595` | queue | llm:llm_20260903-181110_2 | **+10,796** | 12.3 | 20-0 | -15,472 | +10,500 |  · blocks: crop_admission |  |  |
| `080778954358` | wide | ablate:MAX_SHEEP | **+10,382** | 8.2 | 20-0 | -18,862 | +7,787 | melon_floor 150→100, load_per_hand 20→15, open_wheat 7→8, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4, MAX_SHEEP 12→11 · blocks: crop_admission |  | cand falls behind C1 from day 24 (gap -4,385 -> final -7,079); days 22-29 drivers: sales_rev -7,230, idle_turns +142, water_hour +2.37. Hands 4 vs 3, animals 8 vs 9, plants 0 vs 0. |
| `c7307de95966` | v312 | ablate:CROP_SWEEP_LEN | **+10,368** | 8.3 | 20-0 | -9,160 | +9,287 | melon_floor 150→200, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 13 (gap +4,492 -> final +41,843); days 11-18 drivers: sales_rev +13,250, missed_water -56, work_turns +80, feed_hour -1.19. Hands 9 vs 10, animals 11 vs 8, plants 53 vs |
| `62ed32b18967` | queue | ablate:MAX_HANDS | **+10,309** | 11.7 | 20-0 | -15,001 | +9,750 | harvest_min 2→1, wheat_sell_price 30→25, HERD_LAST_DAY 19→20, OPP_GROWTH 1.3→1.4 · blocks: crop_admission |  |  |
| `0d032724cbc2` | c1 | mutate | **+10,225** | 6.8 | 19-1 | -13,965 | +8,785 | melon_floor 150→200, load_per_hand 20→16, open_melons 8→10, open_wheat 7→8, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, OPP_GROWTH 1.3→1.4 · blocks: crop_admission | load_per_hand -55, wheat_water_tier +1,841, CROP_SWEEP_LEN -465, MELON_MAX_TILES ? | cand pulls ahead of C1 from day 25 (gap +3,800 -> final +12,221); days 23-29 drivers: sales_rev +17,957, work_turns +100, missed_water -16, weeds_new -3. Hands 6 vs 3, animals 8 vs 9, plants 40 vs 0. |
| `8f9446df9d9d` | queue | crossover | **+10,085** | 7.9 | 20-0 | -10,111 | +9,454 | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.2, wheat_water_tier 0→1, CROP_SWEEP_RADIUS 4→3, NEAR_RADIUS 3→2, MAX_SHEEP 12→14 · blocks: crop_admission |  | cand pulls ahead of C1 from day 15 (gap +3,541 -> final +2,952); days 13-20 drivers: sales_rev +16,675, missed_water -30, work_turns +124, feed_hour -0.88. Hands 12 vs 13, animals 13 vs 8, plants 60 v |
| `200028cd79de` | wide | crossover | **+10,080** | 7.2 | 19-1 | -18,493 | +7,446 | melon_floor 150→200, load_per_hand 20→15, open_wheat 7→8, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4, MAX_SHEEP 12→11 · blocks: crop_admission |  | cand falls behind C1 from day 17 (gap -1,975 -> final -9,186); days 15-22 drivers: idle_turns +84, water_hour +0.82. Hands 12 vs 13, animals 8 vs 9, plants 67 vs 62. |
| `d8afe2b5d651` | wide | ablate:wheat_sell_price | **+10,019** | 7.6 | 19-1 | -17,843 | +4,503 | melon_floor 150→100, load_per_hand 20→15, open_wheat 7→8, wheat_sell_price 30→50, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4 · blocks: crop_admission |  | cand pulls ahead of C1 from day 25 (gap +2,494 -> final +4,558); days 23-29 drivers: sales_rev +7,517, work_turns +96, missed_water -12, missed_feed -2. Hands 6 vs 3, animals 13 vs 9, plants 9 vs 0. |
| `21960003cac0` | wide | crossover | **+9,553** | 7.2 | 19-1 | -19,107 | +7,125 | melon_floor 150→100, load_per_hand 20→15, open_wheat 7→8, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4 · blocks: crop_admission | melon_floor +495, open_wheat +2,502, wheat_sell_price +2,622, STRAW_CUTOFF ?, NEAR_RADIUS +827, MAX_SHEEP -662 | cand falls behind C1 from day 24 (gap -4,385 -> final -7,079); days 22-29 drivers: sales_rev -7,230, idle_turns +142, water_hour +2.37. Hands 4 vs 3, animals 8 vs 9, plants 0 vs 0. |
| `f8be9cdc3861` | v312 | ablate:wheat_tiles | **+9,528** | 5.5 | 19-1 | -10,148 | +11,582 | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  |  |
| `be30f72ec3ad` | v312 | ablate:CROP_SWEEP_RADIUS | **+9,269** | 7.6 | 19-1 | -5,732 | +5,412 | melon_floor 150→200, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 28 (gap +2,355 -> final +2,121); days 26-29 drivers: sales_rev +9,623, work_turns +93, missed_water -6, feed_hour -0.67. Hands 6 vs 3, animals 16 vs 9, plants 4 vs 0. |
| `a7dfd95b1e24` | wide | ablate:melon_floor | **+9,115** | 6.2 | 18-2 | -18,491 | +6,630 | melon_floor 150→200, load_per_hand 20→15, open_wheat 7→8, MAX_HANDS 13→12, STRAW_CUTOFF 17→15, MELON_MAX_TILES 40→50, HERD_LAST_DAY 19→22, NEAR_RADIUS 3→4 · blocks: crop_admission |  | cand falls behind C1 from day 17 (gap -1,975 -> final -9,186); days 15-22 drivers: idle_turns +84, water_hour +0.82. Hands 12 vs 13, animals 8 vs 9, plants 67 vs 62. |
| `789b7a7d84ec` | v312 | ablate:MAX_HANDS | **+8,880** | 7.0 | 18-2 | -6,741 | +9,339 | melon_floor 150→0, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, MELON_PRICE_CUSHION 100→74, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 21 (gap +4,750 -> final +17,936); days 19-26 drivers: sales_rev +22,286, work_turns +207, idle_turns -47, missed_feed -1. Hands 13 vs 11, animals 15 vs 9, plants 50 vs  |
| `81e1feec12e1` | v312 | ablate:wheat_water_tier | **+8,809** | 6.3 | 19-1 | -6,270 | +10,123 | melon_floor 150→200, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |  | cand pulls ahead of C1 from day 23 (gap +3,389 -> final +22,810); days 21-28 drivers: sales_rev +29,199, work_turns +233, idle_turns -51, missed_feed -4. Hands 11 vs 8, animals 17 vs 9, plants 34 vs 2 |
| `052762d0e8c0` | v312 | crossover | **+8,689** | 7.2 | 19-1 | -6,366 | +7,106 | melon_floor 150→200, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission | geese +2,677, open_cows +4,317, demand_share -1,581, wheat_water_tier -3,017, CROP_SWEEP_LEN -2,181, CROP_SWEEP_RADIUS +1,694 | cand pulls ahead of C1 from day 20 (gap +1,910 -> final +32,975); days 18-25 drivers: sales_rev +29,002, work_turns +115, missed_feed -2, idle_turns -7. Hands 13 vs 11, animals 13 vs 9, plants 56 vs 5 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `f8be9cdc3861` | v312 | ablate:wheat_tiles | +11,582 | 6.0 | 10-0 | -17,834 | held_pass | melon_floor 150→200, open_melons 8→5, open_wheat 7→9, open_cows 2→3, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `974a722e40d2` | queue | ablate:MAX_SHEEP | +11,545 | 5.7 | 10-0 | -14,402 | held_pass | harvest_min 2→1, open_wheat 7→8, early_hire_days 5→7, HERD_LAST_DAY 19→20 · blocks: crop_admission |
| `2ed37e718be7` | queue | ablate:fert_keep | +11,161 | 5.6 | 10-0 | -13,859 | held_pass | open_wheat 7→8, early_hire_days 5→4 · blocks: crop_admission |
| `5eeb0745fc2d` | queue | ablate:NEAR_RADIUS | +11,160 | 5.6 | 10-0 | -12,708 | held_pass | melon_floor 150→100, open_wheat 7→8 · blocks: crop_admission |
| `fe09c53a316a` | queue | ablate:melon_floor | +10,967 | 4.9 | 10-0 | -13,451 | held_pass | open_wheat 7→8, early_hire_days 5→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `de4e1e1f2dc2` | queue | crossover | +10,965 | 4.9 | 10-0 | -12,299 | held_pass | melon_floor 150→0, open_wheat 7→8, early_hire_days 5→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `f2e8414b9e0e` | v312 | ablate:MAX_HANDS | +10,652 | 3.2 | 10-0 | -16,665 | held_pass | melon_floor 150→200, harvest_min 2→1, wheat_tiles 0→2, open_melons 8→5, open_wheat 7→9, open_cows 2→3, fert_carry 3→2, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.2, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→28, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `c2747c8ab595` | queue | llm:llm_20260903-181110_2 | +10,500 | 4.4 | 10-0 | -12,480 | held_pass |  · blocks: crop_admission |
| `4a1ce10d69bb` | v312 | ablate:demand_share | +10,487 | 3.4 | 10-0 | -15,811 | held_pass | melon_floor 150→200, harvest_min 2→3, wheat_tiles 0→2, open_melons 8→5, open_wheat 7→9, open_cows 2→3, fert_carry 3→2, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.2, wheat_cap 18→15, wheat_water_tier 0→1, wheat_sell_price 30→28, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→9 · blocks: crop_admission |
| `88454a193228` | queue | crossover | +10,448 | 4.0 | 9-1 | -13,993 | held_pass | harvest_min 2→1, open_wheat 7→8, early_hire_days 5→7, HERD_LAST_DAY 19→20, MAX_SHEEP 12→14 · blocks: crop_admission |
| `48f6ae0f43dd` | v312 | crossover | +10,383 | 4.7 | 10-0 | -16,176 | held_pass | open_melons 8→5, open_wheat 7→9, open_cows 2→3, wheat_per_animal 0.0→0.1, wheat_cap 18→17, wheat_water_tier 0→1, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `9a7eeeba76c5` | queue | ablate:open_wheat | +10,358 | 6.8 | 10-0 | -22,538 | held_pass | melon_floor 150→100, NEAR_RADIUS 3→2 · blocks: crop_admission |
| `98e26f5cc876` | queue | crossover | +10,267 | 7.5 | 10-0 | -21,491 | held_pass | early_hire_days 5→4, wheat_cap 18→25, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `81e1feec12e1` | v312 | ablate:wheat_water_tier | +10,123 | 4.2 | 10-0 | -13,155 | held_pass | melon_floor 150→200, harvest_min 2→1, open_melons 8→5, open_wheat 7→9, open_cows 2→3, demand_share 0.5→0.45, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→15, wheat_water_tier 0→1, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 4→3, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→41, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, OPENING_MELONS 10→11 · blocks: crop_admission |
| `02732ca5fbd9` | queue | mutate | +9,800 | 5.7 | 10-0 | -15,106 | held_pass | open_wheat 7→8, early_hire_days 5→4, fert_keep 0→1 · blocks: crop_admission |

## Islands (best dev margin, population size)

- c1: best +9,250 (`212463b18745`), n=70
- queue: best +11,545 (`974a722e40d2`), n=85
- v312: best +11,582 (`f8be9cdc3861`), n=86
- wide: best +9,265 (`a13d19f8dcf0`), n=65

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| ROUTE_LEN | 13,070 | 3 | 3 | 3: +4,535 (230), 2: +2,304 (39), 4: +7 (35), 5: -8,536 (2) |
| early_hire_days | 10,947 | 7 | 5 | 7: +9,347 (5), 4: +4,699 (44), 3: +4,040 (8), 5: +3,673 (225), 0: +584 (11), 6: +562 (8), 1: -1,599 (4) |
| demand_share | 10,523 | 0.4 | 0.5 | 0.4: +5,897 (5), 0.45: +4,937 (33), 0.5: +4,605 (210), 0.8: +1,612 (3), 0.55: +414 (15), 0.6: +205 (3), 0.35: +160 (5), 0.75: -621 (3), 0.3: -946 (14), 0.7: -1,883 (12), 0.65: -4,626 (2) |
| wheat_sell_price | 9,815 | 28 | 30 | 28: +5,770 (12), 30: +3,956 (171), 31: +3,845 (17), 50: +3,684 (26), 27: +3,395 (11), 25: +3,377 (43), 29: +2,645 (4), 37: +2,388 (9), 32: +1,447 (2), 44: +763 (3), 26: -4,045 (2) |
| OPENING_MELONS | 9,378 | 6 | 10 | 6: +4,341 (11), 11: +4,075 (89), 10: +3,767 (182), 9: +3,568 (9), 13: +2,611 (2), 7: +636 (2), 8: +283 (3), 12: -842 (5), 14: -5,037 (3) |
| wheat_per_animal | 8,995 | 0.1 | 0.0 | 0.1: +4,940 (42), 0.2: +4,054 (17), 0.0: +3,615 (237), 0.3: -237 (6), 0.4: -4,055 (2) |
| MELON_MAX_TILES | 7,997 | 31 | 40 | 31: +5,178 (7), 41: +4,397 (77), 50: +4,103 (58), 40: +3,500 (143), 44: +2,226 (2), 37: +1,014 (2), 32: +966 (4), 45: -438 (2), 39: -1,967 (2), 38: -2,819 (2) |
| load_per_hand | 7,778 | 15 | 20 | 15: +4,217 (26), 20: +4,017 (213), 19: +3,752 (24), 16: +3,396 (12), 21: +2,576 (14), 22: +412 (2), 18: -598 (10), 17: -1,042 (2), 13: -3,561 (2) |
| MELON_PRICE_CUSHION | 7,210 | 74 | 100 | 74: +5,443 (5), 83: +4,646 (5), 114: +4,028 (16), 100: +3,961 (259), 112: +3,357 (2), 50: -1,767 (8) |
| wheat_tiles | 6,536 | 1 | 0 | 1: +3,808 (14), 2: +3,763 (14), 0: +3,736 (259), 3: +3,549 (15), 4: -2,728 (4) |
| NEAR_RADIUS | 6,231 | 2 | 3 | 2: +4,172 (104), 3: +3,639 (171), 4: +2,697 (26), 5: -2,059 (5) |
| CROP_SWEEP_RADIUS | 6,082 | 3 | 4 | 3: +4,993 (28), 2: +4,850 (6), 4: +3,932 (223), 5: +1,658 (45), 6: -1,089 (4) |
| open_wheat | 6,045 | 8 | 7 | 8: +4,870 (70), 9: +4,211 (80), 3: +3,940 (5), 7: +2,988 (136), 10: +2,377 (2), 5: +2,305 (2), 6: +1,089 (7), 4: -1,175 (4) |
| opening | 5,916 | frontier | frontier | frontier: +4,053 (285), v312: -1,863 (21) |
| wheat_cap | 5,836 | 17 | 18 | 17: +5,234 (3), 25: +4,137 (2), 15: +4,049 (71), 18: +3,760 (193), 21: +3,433 (9), 14: +2,867 (3), 20: +2,367 (9), 22: +1,965 (3), 12: +1,547 (4), 24: +98 (2), 13: -602 (3) |
| feed_spare_poor | 5,297 | 0 | 0 | 0: +3,790 (291), 2: +2,980 (8), 1: -1,507 (7) |
| open_sheep | 5,141 | 2 | 2 | 2: +3,846 (294), 0: -964 (2), 3: -1,218 (3), 1: -1,295 (7) |
| HERD_LAST_DAY | 5,079 | 22 | 19 | 22: +4,252 (71), 20: +3,746 (53), 19: +3,618 (170), 18: +370 (6), 21: +160 (2), 17: -827 (3) |
| max_animals | 4,991 | 19 | 20 | 19: +4,724 (3), 17: +4,462 (52), 20: +3,633 (238), 15: +3,125 (2), 18: -267 (10) |
| open_melons | 4,972 | 5 | 8 | 5: +4,252 (66), 8: +3,978 (141), 10: +3,976 (22), 7: +3,820 (28), 11: +2,787 (8), 6: +2,121 (22), 9: +1,350 (12), 4: -719 (7) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (15, 3, 6): +11,582 (n=7)
- (7, 3, 5): +11,545 (n=14)
- (9, 4, 6): +10,652 (n=11)
- (13, 3, 6): +10,500 (n=24)
- (7, 4, 6): +10,358 (n=8)
- (12, 4, 6): +10,123 (n=4)
- (17, 3, 6): +9,492 (n=11)
- (14, 3, 6): +9,451 (n=15)
- (8, 4, 6): +9,450 (n=8)
- (13, 2, 5): +9,389 (n=2)
- (8, 2, 3): +9,354 (n=2)
- (11, 3, 6): +9,287 (n=5)
- (7, 3, 6): +9,265 (n=15)
- (8, 3, 6): +9,250 (n=20)
- (8, 3, 5): +9,204 (n=6)

_Generated 2026-09-03 21:15. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._