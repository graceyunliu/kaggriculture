# Evolution run 20260910-121401

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.22 h · candidates evaluated this run: 15 · games 2,136 (9,539/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 4 | 8 |
| dead_smoke | 0 | 0 |
| alive | 8 | 1024 |
| held_fail | 3 | 1104 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 536 · held-out evaluated: 62 · held-out PASS: 1

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `2757e6c92f26` | queue | mutate | **+5,444** | 4.3 | 18-2 | -25,327 | +5,290 | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,317 -> final -13,211); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `b3324e9b7110` | queue | mutate | **+4,961** | 3.3 | 19-1 | -29,707 | +6,108 | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -6,908 -> final -18,802); days 22-29 drivers: sales_rev -23,772, weeds_new +9, work_turns -103, reversals +2. Hands 3 vs 6, animals 9 vs 11, plants 0 vs 17. |
| `da68944524c1` | v312 | mutate | **+4,758** | 4.6 | 18-2 | -25,433 | +2,514 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 22 (gap -3,186 -> final -29,992); days 20-27 drivers: sales_rev -36,606, work_turns -73, water_hour +1.41. Hands 10 vs 11, animals 10 vs 11, plants 42 vs 47. |
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `721d894fe338` | queue | mutate | **+4,281** | 4.7 | 17-3 | -28,345 | +3,190 | feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→112, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -3,167 -> final -14,247); days 22-29 drivers: sales_rev -20,412, weeds_new +19, idle_turns +34, missed_feed +6. Hands 6 vs 6, animals 16 vs 11, plants 12 vs 17. |
| `4da7ca753338` | queue | mutate | **+4,083** | 3.5 | 16-4 | -23,668 | +4,086 | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,249 -> final -24,602); days 14-21 drivers: sales_rev -16,963, work_turns -270, weeds_new +2, water_hour +0.96. Hands 7 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `cf9f405831de` | v312 | crossover | **+4,014** | 5.4 | 18-2 | -24,787 | +2,332 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, max_animals 17→19, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -9,334 -> final -20,201); days 21-28 drivers: sales_rev -21,532, work_turns -65, weeds_new +3, water_hour +1.41. Hands 7 vs 9, animals 13 vs 11, plants 14 vs 33. |
| `3e744f448178` | v312 | mutate | **+3,805** | 3.6 | 16-4 | -24,664 | +3,207 | melon_floor 0→200, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -3,487 -> final -12,279); days 21-28 drivers: sales_rev -16,154, work_turns -87, idle_turns +39, weeds_new +1. Hands 9 vs 9, animals 10 vs 11, plants 22 vs 33. |
| `85560bea67d0` | c1 | paired | **+3,802** | 3.8 | 16-4 | -28,204 | +4,511 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→7, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,507 -> final -16,484); days 14-21 drivers: sales_rev -16,601, work_turns -222. Hands 9 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `0550420abff9` | v312 | mutate | **+3,610** | 3.9 | 16-4 | -24,128 | +2,461 | melon_floor 0→200, harvest_min 1→2, wheat_stock 0→3, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→19, wheat_cap 22→17, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -4,310 -> final -17,224); days 21-28 drivers: sales_rev -19,422, weeds_new +4, work_turns -54, water_hour +1.39. Hands 8 vs 9, animals 15 vs 11, plants 20 vs 33. |
| `d1e7da72c022` | queue | archive_crossover:crossover_g000025_20260910-115246_0 | **+3,531** | 2.7 | 14-6 | -30,530 | +5,947 | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,761 -> final -14,679); days 14-21 drivers: sales_rev -15,329, work_turns -210, water_hour +0.29, travel_per_task +0.02. Hands 13 vs 14, animals 7 vs 11, plants |
| `ba3da54ca5af` | queue | crossover | **+3,476** | 3.4 | 15-5 | -24,717 | +3,431 | melon_floor 0→150, min_hands 3→4, open_wheat 7→4, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,912 -> final -35,280); days 14-21 drivers: sales_rev -19,978, work_turns -213, weeds_new +3, water_hour +0.69. Hands 9 vs 14, animals 7 vs 11, plants 64 vs 84. |
| `db61805ecfa9` | M2 | mutate | **+3,427** | 3.2 | 17-3 | -28,163 | +2,910 | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 20 (gap -3,060 -> final -43,282); days 18-25 drivers: sales_rev -43,924, work_turns -118, water_hour +0.9. Hands 11 vs 13, animals 9 vs 11, plants 60 vs 62. |
| `59e05f8dc434` | c1 | mutate | **+3,308** | 2.6 | 15-5 | -23,769 | +2,800 | melon_floor 0→200, harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→11, FERT_RADIUS 3→4 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -3,108 -> final -8,911); days 14-21 drivers: sales_rev -14,712, work_turns -237, travel_per_task +0.06. Hands 11 vs 14, animals 7 vs 11, plants 67 vs 84. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `d5d57976e061` | queue | archive_crossover:crossover_g000075_20260910-122443_0 | +6,378 | 3.2 | 9-1 | -23,444 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `484eef25d104` | queue | mutate | +6,313 | 2.4 | 8-2 | -26,423 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→11, fert_keep 0→1, max_animals 17→20, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `d1e7da72c022` | queue | archive_crossover:crossover_g000025_20260910-115246_0 | +5,947 | 3.2 | 9-1 | -24,175 | held_fail | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `d9f6714af711` | queue | archive_crossover:crossover_g000050_20260910-120943_0 | +5,523 | 2.6 | 8-2 | -26,352 | held_fail | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→27, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `1019eca510ac` | wide | paired | +5,473 | 2.3 | 8-2 | -24,553 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `8d73168f191f` | wide | paired | +5,425 | 2.7 | 9-1 | -28,015 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→27, wheat_hold_days 0→2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `d5fdd7605657` | queue | archive_crossover:crossover_g000050_20260910-111312_1 | +5,411 | 2.6 | 8-2 | -23,346 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `bcf4dbd52f8d` | queue | mutate | +5,330 | 3.5 | 9-1 | -20,888 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |
| `2757e6c92f26` | queue | mutate | +5,290 | 5.1 | 10-0 | -18,243 | held_fail | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `c06c14efa4e0` | queue | archive_crossover:crossover_g000050_20260910-111312_0 | +5,132 | 3.4 | 9-1 | -23,025 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, fert_keep 0→1, demand_share 0.55→0.7, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |
| `cc8718994c22` | wide | block_pair | +5,046 | 2.1 | 9-1 | -24,840 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.2, wheat_sell_price 30→27, wheat_hold_days 0→2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `e05397e4510f` | v312 | migrate | +4,992 | 2.6 | 8-2 | -23,981 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.2, wheat_sell_price 30→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→37, HERD_LAST_DAY 17→18, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `b78610c183a0` | wide | crossover | +4,886 | 2.9 | 8-2 | -25,073 | held_fail | melon_floor 0→100, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=65
- M2: best +4,110 (`2521e3906eb6`), n=61
- c1: best +4,572 (`f5e71682ea28`), n=90
- queue: best +6,527 (`edd7288369ba`), n=165
- v312: best +4,992 (`e05397e4510f`), n=77
- wide: best +5,473 (`1019eca510ac`), n=78

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +10,389 | 61 | 100 | 37 | 519 | 13.95 | 61: +3,780 (n=16), 91: +839 (n=2), 78: +683 (n=5), 124: +405 (n=3), 74: -125 (n=2), 90: -267 (n=7), 115: -447 (n=6), 102: -680 (n=30), 100: -768 (n=388), 84: -830 (n=6), 83: -1,174 (n=3), 85: -1,380 (n=16), 112: -1,554 (n=2), 82: -2,202 (n=2), 92: -2,233 (n=17), 71: -2,386 (n=2), 114: -3,075 (n=2), 104: -3,341 (n=2), 110: -4,472 (n=6), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,828 | 0.4 | 0.0 | 7 | 536 | 3.66 | 0.4: +1,733 (n=2), 0.1: +534 (n=20), 0.2: -307 (n=37), 0.0: -663 (n=357), 0.3: -1,372 (n=115), 0.6: -3,949 (n=3), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,274 | 40 | 38 | 22 | 532 | 4.48 | 40: +1,822 (n=44), 37: +1,373 (n=6), 39: +620 (n=68), 27: +439 (n=10), 41: -192 (n=9), 33: -247 (n=3), 50: -251 (n=3), 32: -731 (n=10), 35: -790 (n=64), 34: -1,133 (n=162), 31: -1,204 (n=3), 25: -1,798 (n=3), 38: -1,802 (n=122), 28: -1,927 (n=2), 42: -2,924 (n=3), 43: -3,001 (n=11), 46: -3,322 (n=7), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,987 | 134 | 92 | 45 | 517 | 16.5 | 134: +1,252 (n=3), 95: +944 (n=9), 102: +627 (n=17), 124: -39 (n=8), 58: -251 (n=29), 107: -484 (n=10), 92: -583 (n=348), 121: -689 (n=6), 106: -780 (n=2), 87: -942 (n=4), 81: -1,046 (n=2), 118: -1,081 (n=2), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 16: -1,522 (n=2), 73: -1,731 (n=2), 11: -1,755 (n=39), 72: -1,999 (n=3), 150: -2,267 (n=10), 0: -2,575 (n=3), 76: -3,783 (n=2), 115: -3,837 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,619 | 18 | 20 | 11 | 535 | 4.68 | 18: +912 (n=38), 19: +249 (n=112), 15: -715 (n=3), 22: -836 (n=9), 20: -919 (n=304), 16: -1,526 (n=2), 17: -2,180 (n=9), 23: -2,297 (n=10), 21: -2,588 (n=43), 24: -5,706 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +6,615 | 0.7 | 0.55 | 13 | 534 | 5.39 | 0.7: +2,421 (n=7), 0.65: +141 (n=43), 0.45: -224 (n=49), 0.55: -550 (n=310), 0.6: -625 (n=40), 0.5: -2,170 (n=57), 0.75: -2,922 (n=5), 0.8: -3,532 (n=4), 0.3: -3,855 (n=14), 0.85: -4,162 (n=2), 0.35: -4,194 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,896 | 2 | 3 | 3 | 536 | 0.98 | 2: +830 (n=166), 3: -1,324 (n=353), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,668 | 13 | 14 | 7 | 536 | 3.74 | 13: -128 (n=57), 14: -654 (n=363), 12: -916 (n=63), 11: -1,360 (n=8), 15: -1,601 (n=31), 16: -2,938 (n=10), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,632 | 2 | 2 | 4 | 536 | 2.55 | 2: -553 (n=476), 1: -2,079 (n=50), 0: -4,267 (n=7), 3: -6,185 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +5,583 | 9 | 14 | 8 | 535 | 3.1 | 9: +2,492 (n=3), 10: +383 (n=111), 13: -963 (n=43), 14: -1,065 (n=313), 11: -1,234 (n=5), 12: -1,243 (n=58), 8: -3,091 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,544 | 6 | 8 | 10 | 536 | 3.48 | 6: +125 (n=4), 10: -232 (n=240), 11: -583 (n=40), 9: -604 (n=25), 14: -756 (n=4), 8: -1,281 (n=204), 7: -1,453 (n=8), 12: -2,682 (n=4), 4: -4,132 (n=2), 5: -5,419 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,028 | 0.3 | 0.25 | 10 | 536 | 6.0 | 0.3: +562 (n=12), 0.4: +521 (n=78), 0.45: -429 (n=24), 0.25: -837 (n=375), 0.1: -945 (n=2), 0.5: -1,613 (n=5), 0.15: -1,761 (n=4), 0.2: -1,768 (n=9), 0.35: -3,875 (n=25), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,633 | 2 | 2 | 3 | 536 | 1.84 | 2: -591 (n=508), 1: -3,600 (n=19), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +4,139 | frontier | frontier | 2 | 536 | 0.87 | frontier: -497 (n=500), v312: -4,636 (n=36) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,987 | 22 | 17 | 9 | 535 | 2.95 | 22: +1,500 (n=49), 18: -143 (n=26), 20: -806 (n=9), 17: -960 (n=264), 19: -1,068 (n=160), 16: -1,257 (n=9), 21: -1,750 (n=3), 14: -2,487 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +3,939 | 1 | 0 | 3 | 536 | 1.68 | 1: +1,882 (n=54), 0: -1,065 (n=478), 2: -2,057 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +3,727 | 5 | 22 | 15 | 533 | 5.44 | 5: +1,017 (n=11), 13: +79 (n=71), 12: -264 (n=21), 22: -663 (n=286), 25: -1,058 (n=77), 17: -1,225 (n=5), 24: -1,388 (n=7), 21: -1,542 (n=2), 20: -1,999 (n=14), 18: -2,173 (n=24), 19: -2,301 (n=6), 23: -2,710 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,033 | 6 | 5 | 9 | 535 | 4.97 | 6: -206 (n=17), 4: -211 (n=24), 7: -481 (n=22), 8: -556 (n=13), 5: -778 (n=399), 3: -1,082 (n=50), 2: -1,089 (n=3), 0: -3,239 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +3,033 | 3 | 6 | 7 | 536 | 3.27 | 3: +139 (n=131), 6: -972 (n=327), 8: -1,059 (n=4), 4: -1,245 (n=3), 7: -1,268 (n=41), 5: -1,751 (n=27), 9: -2,894 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| NEAR_RADIUS | +2,843 | 5 | 2 | 4 | 536 | 2.74 | 5: +1,608 (n=2), 3: +339 (n=14), 2: -799 (n=501), 4: -1,235 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +6,527 (n=61)
- (9, 3, 5): +6,313 (n=16)
- (9, 3, 3): +6,108 (n=9)
- (12, 4, 6): +5,330 (n=13)
- (8, 3, 5): +5,290 (n=16)
- (7, 3, 3): +4,876 (n=24)
- (8, 3, 4): +4,836 (n=28)
- (10, 3, 4): +4,807 (n=18)
- (6, 3, 3): +4,589 (n=13)
- (7, 3, 5): +4,572 (n=11)
- (10, 4, 6): +4,214 (n=32)
- (16, 3, 6): +4,008 (n=6)
- (9, 3, 4): +3,671 (n=36)
- (14, 3, 6): +3,652 (n=11)
- (10, 3, 5): +3,207 (n=20)

_Generated 2026-09-10 12:27. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 260 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=260); harvest_min=1–3 (n=260); wheat_tiles=0–5 (n=260); wheat_stock=0–19 (n=260); min_hands=3–6 (n=260); load_per_hand=12–26 (n=260); geese=0–2 (n=260); open_melons=4–14 (n=260)
- **Evidence:** 260 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 12:27. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._