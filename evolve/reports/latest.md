# Evolution run 20260910-095644

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 1.03 h · candidates evaluated this run: 93 · games 9,756 (9,511/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 5 | 10 |
| dead_pattern | 13 | 26 |
| dead_smoke | 9 | 72 |
| alive | 61 | 7808 |
| held_fail | 5 | 1840 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 384 · held-out evaluated: 26 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `2757e6c92f26` | queue | mutate | **+5,444** | 4.3 | 18-2 | -25,327 | +5,290 | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,317 -> final -13,211); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `4da7ca753338` | queue | mutate | **+4,083** | 3.5 | 16-4 | -23,668 | +4,086 | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,249 -> final -24,602); days 14-21 drivers: sales_rev -16,963, work_turns -270, weeds_new +2, water_hour +0.96. Hands 7 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `cf9f405831de` | v312 | crossover | **+4,014** | 5.4 | 18-2 | -24,787 | +2,332 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, max_animals 17→19, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -9,334 -> final -20,201); days 21-28 drivers: sales_rev -21,532, work_turns -65, weeds_new +3, water_hour +1.41. Hands 7 vs 9, animals 13 vs 11, plants 14 vs 33. |
| `db61805ecfa9` | M2 | mutate | **+3,427** | 3.2 | 17-3 | -28,163 | +2,910 | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 20 (gap -3,060 -> final -43,282); days 18-25 drivers: sales_rev -43,924, work_turns -118, water_hour +0.9. Hands 11 vs 13, animals 9 vs 11, plants 60 vs 62. |
| `bcf4dbd52f8d` | queue | mutate | **+3,075** | 2.0 | 12-8 | -23,822 | +5,330 | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand pulls ahead of C1 from day 26 (gap +5,036 -> final +8,642); days 24-29 drivers: sales_rev +17,235, work_turns +68, feed_hour -1.9, idle_turns -16. Hands 6 vs 6, animals 12 vs 11, plants 27 vs 17. |
| `b78610c183a0` | wide | crossover | **+3,072** | 2.0 | 17-3 | -26,162 | +4,886 | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,254 -> final -9,989); days 15-22 drivers: sales_rev -11,173, work_turns -225. Hands 13 vs 14, animals 7 vs 11, plants 67 vs 85. |
| `bb47f6f0b3ef` | queue | archive_crossover:crossover_g000025_20260910-102949_1 | **+2,737** | 2.8 | 16-4 | -25,920 | +3,291 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, MAX_SHEEP 14→12 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,781 -> final -34,668); days 15-22 drivers: sales_rev -16,255, work_turns -235, water_hour +0.63. Hands 14 vs 14, animals 7 vs 11, plants 66 vs 85. |
| `1019eca510ac` | wide | paired | **+2,593** | 1.9 | 15-5 | -29,280 | +5,473 | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,647 -> final -14,317); days 14-21 drivers: sales_rev -15,740, work_turns -238, travel_per_task +0.06. Hands 11 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | **+2,328** | 1.5 | 13-7 | -26,820 | +6,527 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,255 -> final -4,859); days 14-21 drivers: sales_rev -16,071, work_turns -227. Hands 10 vs 14, animals 7 vs 11, plants 66 vs 84. |
| `150b6a4263d7` | queue | archive_crossover:crossover_g000050_20260910-103203_0 | **+2,236** | 2.0 | 13-7 | -29,080 | +4,249 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→12, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,742 -> final -20,054); days 15-22 drivers: sales_rev -13,764, work_turns -255, water_hour +0.41. Hands 14 vs 14, animals 7 vs 11, plants 67 vs 85. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `935becadf7d7` | queue | archive_crossover:crossover_g000025_20260910-094825_0 | **+1,563** | 1.6 | 14-6 | -25,481 | +2,260 | open_melons 8→10, open_wheat 7→6, early_hire_days 5→7, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -1,626 -> final -37,310); days 15-22 drivers: sales_rev -24,138, work_turns -183, feed_hour +0.89, reversals +7. Hands 14 vs 14, animals 11 vs 11, plants 57 vs 85 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `1019eca510ac` | wide | paired | +5,473 | 2.3 | 8-2 | -24,553 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `bcf4dbd52f8d` | queue | mutate | +5,330 | 3.5 | 9-1 | -20,888 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |
| `2757e6c92f26` | queue | mutate | +5,290 | 5.1 | 10-0 | -18,243 | held_fail | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `b78610c183a0` | wide | crossover | +4,886 | 2.9 | 8-2 | -25,073 | held_fail | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `150b6a4263d7` | queue | archive_crossover:crossover_g000050_20260910-103203_0 | +4,249 | 3.1 | 8-2 | -20,451 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→12, FERT_RADIUS 3→4 · blocks: hiring |
| `4da7ca753338` | queue | mutate | +4,086 | 2.7 | 9-1 | -19,685 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |
| `bfe4bb8d3609` | v312 | migrate | +4,008 | 1.6 | 7-3 | -21,783 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_sell_price 30→29, labor_reserve_buffer 92→95, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `aade4d85f6fe` | queue | mutate | +3,787 | 3.2 | 8-2 | -21,617 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |
| `cfdd30201794` | queue | mutate | +3,486 | 4.2 | 10-0 | -20,077 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→40 · blocks: hiring |
| `bb47f6f0b3ef` | queue | archive_crossover:crossover_g000025_20260910-102949_1 | +3,291 | 2.4 | 8-2 | -21,309 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_cap 22→5, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→40, MAX_SHEEP 14→12 · blocks: hiring |
| `e6f11dfd6ed2` | queue | crossover | +3,098 | 1.7 | 7-3 | -24,025 | alive | melon_floor 0→100, wheat_stock 0→14, min_hands 3→4, open_melons 8→10, open_wheat 7→4, early_hire_days 5→4, feed_spare_poor 0→1, fert_keep 0→1, demand_share 0.55→0.65, wheat_per_animal 0.0→0.3, wheat_cap 22→13, wheat_sell_price 30→25, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→84, HERD_LAST_DAY 17→16, MAX_SHEEP 14→10, FERT_RADIUS 3→1, SPREAD_CAP 3→5 · blocks: hiring |
| `57c65535c63e` | M2 | paired | +3,091 | 1.6 | 6-4 | -28,471 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=51
- M2: best +3,091 (`57c65535c63e`), n=40
- c1: best +2,683 (`5fd05605827b`), n=63
- queue: best +6,527 (`edd7288369ba`), n=117
- v312: best +4,008 (`bfe4bb8d3609`), n=52
- wide: best +5,473 (`1019eca510ac`), n=61

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +7,866 | 84 | 100 | 30 | 371 | 12.43 | 84: +1,257 (n=3), 91: +839 (n=2), 78: -7 (n=3), 74: -125 (n=2), 102: -159 (n=19), 115: -403 (n=3), 124: -740 (n=2), 90: -950 (n=5), 100: -1,169 (n=293), 83: -1,174 (n=3), 85: -1,611 (n=12), 82: -2,202 (n=2), 71: -2,386 (n=2), 92: -2,528 (n=10), 114: -3,075 (n=2), 110: -4,472 (n=6), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,107 | 40 | 38 | 19 | 382 | 4.56 | 40: +1,654 (n=9), 39: +696 (n=46), 50: +235 (n=2), 27: -236 (n=5), 33: -247 (n=3), 32: -663 (n=7), 41: -866 (n=4), 35: -1,011 (n=49), 34: -1,513 (n=125), 38: -1,917 (n=107), 28: -1,927 (n=2), 31: -2,709 (n=2), 42: -2,924 (n=3), 43: -3,008 (n=10), 25: -3,320 (n=2), 46: -4,041 (n=4), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,624 | 0.1 | 0.0 | 6 | 384 | 2.97 | 0.1: +529 (n=8), 0.0: -1,185 (n=254), 0.2: -1,309 (n=21), 0.3: -1,573 (n=97), 0.6: -1,828 (n=2), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,538 | 95 | 92 | 31 | 376 | 14.17 | 95: +803 (n=7), 87: +415 (n=2), 58: -18 (n=19), 124: -40 (n=7), 102: -287 (n=6), 121: -689 (n=6), 107: -755 (n=7), 106: -780 (n=2), 118: -1,081 (n=2), 92: -1,252 (n=248), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 16: -1,522 (n=2), 73: -1,731 (n=2), 11: -1,827 (n=34), 72: -1,999 (n=3), 150: -2,267 (n=10), 0: -2,575 (n=3), 76: -3,783 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,899 | 13 | 14 | 7 | 384 | 3.7 | 13: +103 (n=36), 12: -971 (n=51), 14: -1,337 (n=258), 11: -2,042 (n=6), 15: -2,179 (n=22), 16: -2,642 (n=7), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +5,746 | 5 | 22 | 14 | 382 | 5.72 | 5: +1,822 (n=4), 12: +426 (n=11), 13: +107 (n=49), 22: -1,385 (n=214), 25: -1,466 (n=51), 21: -1,542 (n=2), 19: -1,887 (n=4), 20: -2,015 (n=12), 17: -2,111 (n=3), 18: -2,159 (n=21), 24: -3,679 (n=5), 23: -3,923 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,540 | 6 | 8 | 10 | 383 | 2.83 | 6: -149 (n=3), 14: -756 (n=4), 10: -885 (n=163), 7: -1,109 (n=7), 9: -1,152 (n=17), 8: -1,530 (n=160), 11: -1,604 (n=23), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,497 | 2 | 3 | 3 | 384 | 1.3 | 2: +431 (n=73), 3: -1,490 (n=294), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,396 | 2 | 2 | 4 | 384 | 2.53 | 2: -1,076 (n=339), 1: -2,485 (n=38), 0: -4,123 (n=5), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +5,196 | 0.65 | 0.55 | 11 | 383 | 4.98 | 0.65: +192 (n=32), 0.6: -465 (n=28), 0.45: -916 (n=32), 0.55: -1,288 (n=229), 0.5: -2,198 (n=42), 0.8: -2,202 (n=2), 0.75: -2,707 (n=4), 0.3: -4,103 (n=10), 0.85: -4,162 (n=2), 0.35: -5,004 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +4,611 | 4 | 7 | 8 | 384 | 4.58 | 4: -122 (n=55), 6: -360 (n=18), 3: -864 (n=21), 9: -1,086 (n=11), 7: -1,531 (n=268), 10: -1,893 (n=3), 5: -3,246 (n=3), 8: -4,733 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,559 | 19 | 20 | 10 | 383 | 4.66 | 19: -527 (n=66), 15: -1,043 (n=2), 20: -1,108 (n=241), 18: -1,360 (n=14), 22: -1,465 (n=6), 17: -2,638 (n=5), 21: -2,736 (n=36), 23: -2,815 (n=9), 24: -5,086 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +4,322 | 0.3 | 0.25 | 10 | 383 | 5.46 | 0.3: -144 (n=6), 0.4: -584 (n=44), 0.45: -913 (n=18), 0.25: -1,169 (n=275), 0.2: -1,303 (n=7), 0.15: -1,761 (n=4), 0.5: -2,713 (n=4), 0.35: -4,012 (n=23), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +4,175 | frontier | frontier | 2 | 384 | 0.86 | frontier: -1,000 (n=358), v312: -5,175 (n=26) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_CAP | +4,159 | 5 | 3 | 3 | 384 | 1.7 | 5: +2,642 (n=3), 3: -1,293 (n=346), 4: -1,516 (n=35) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,149 | 2 | 2 | 3 | 384 | 1.82 | 2: -1,075 (n=361), 1: -4,112 (n=14), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +3,523 | 9 | 0 | 10 | 380 | 4.23 | 9: -407 (n=6), 0: -1,232 (n=331), 7: -1,463 (n=2), 1: -1,595 (n=2), 4: -1,747 (n=37), 6: -3,930 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,446 | 16 | 17 | 9 | 382 | 2.61 | 16: +509 (n=6), 22: -527 (n=19), 18: -813 (n=16), 17: -1,222 (n=197), 19: -1,432 (n=129), 20: -2,204 (n=4), 14: -2,937 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +3,314 | 19 | 17 | 8 | 384 | 4.94 | 19: +491 (n=8), 16: -584 (n=6), 14: -935 (n=5), 18: -969 (n=19), 17: -1,187 (n=285), 15: -1,575 (n=31), 13: -1,877 (n=2), 20: -2,824 (n=28) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +2,848 | 4 | 5 | 8 | 383 | 4.32 | 4: -207 (n=15), 8: -909 (n=8), 7: -973 (n=15), 5: -1,303 (n=291), 3: -1,307 (n=41), 6: -2,300 (n=7), 0: -3,055 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +6,527 (n=41)
- (12, 4, 6): +5,330 (n=8)
- (8, 3, 5): +5,290 (n=14)
- (8, 3, 4): +4,836 (n=22)
- (7, 3, 5): +4,249 (n=4)
- (16, 3, 6): +4,008 (n=2)
- (7, 3, 3): +3,486 (n=17)
- (10, 3, 5): +3,091 (n=14)
- (14, 3, 6): +3,066 (n=8)
- (9, 3, 4): +2,962 (n=24)
- (9, 3, 3): +2,910 (n=6)
- (11, 3, 5): +2,663 (n=14)
- (11, 3, 6): +2,574 (n=16)
- (9, 3, 5): +2,565 (n=11)
- (6, 3, 3): +2,391 (n=7)

_Generated 2026-09-10 10:58. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 174 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=174); harvest_min=1–3 (n=174); wheat_tiles=0–5 (n=174); wheat_stock=0–19 (n=174); min_hands=3–6 (n=174); load_per_hand=12–26 (n=174); geese=0–2 (n=174); open_melons=4–12 (n=174)
- **Evidence:** 174 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 10:58. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._