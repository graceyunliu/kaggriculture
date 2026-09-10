# Evolution run 20260910-113849

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 1.19 h · candidates evaluated this run: 110 · games 11,000 (9,249/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 15 | 30 |
| dead_pattern | 15 | 30 |
| dead_smoke | 9 | 72 |
| alive | 55 | 5940 |
| held_fail | 16 | 4928 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 579 · held-out evaluated: 69 · held-out PASS: 1

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `01e555df4a78` | queue | mutate | **+5,528** | 4.3 | 18-2 | -26,568 | +6,006 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,862 -> final -36,124); days 15-22 drivers: sales_rev -18,382, work_turns -200, idle_turns +7. Hands 14 vs 14, animals 7 vs 11, plants 66 vs 85. |
| `2757e6c92f26` | queue | mutate | **+5,444** | 4.3 | 18-2 | -25,327 | +5,290 | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,317 -> final -13,211); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `b3324e9b7110` | queue | mutate | **+4,961** | 3.3 | 19-1 | -29,707 | +6,108 | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -6,908 -> final -18,802); days 22-29 drivers: sales_rev -23,772, weeds_new +9, work_turns -103, reversals +2. Hands 3 vs 6, animals 9 vs 11, plants 0 vs 17. |
| `da68944524c1` | v312 | mutate | **+4,758** | 4.6 | 18-2 | -25,433 | +2,514 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 22 (gap -3,186 -> final -29,992); days 20-27 drivers: sales_rev -36,606, work_turns -73, water_hour +1.41. Hands 10 vs 11, animals 10 vs 11, plants 42 vs 47. |
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `721d894fe338` | queue | mutate | **+4,281** | 4.7 | 17-3 | -28,345 | +3,190 | feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→112, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -3,167 -> final -14,247); days 22-29 drivers: sales_rev -20,412, weeds_new +19, idle_turns +34, missed_feed +6. Hands 6 vs 6, animals 16 vs 11, plants 12 vs 17. |
| `bcfe45a8f2f1` | queue | archive_crossover:crossover_g000075_20260910-122443_1 | **+4,166** | 3.4 | 17-3 | -27,271 | +4,807 | melon_floor 0→150, harvest_min 1→2, open_wheat 7→8, demand_share 0.55→0.65, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 21 (gap -3,281 -> final -40,264); days 19-26 drivers: sales_rev -36,636, weeds_new +8, work_turns -89, water_hour +0.81. Hands 11 vs 11, animals 12 vs 11, plants 43 vs 53 |
| `4da7ca753338` | queue | mutate | **+4,083** | 3.5 | 16-4 | -23,668 | +4,086 | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,249 -> final -24,602); days 14-21 drivers: sales_rev -16,963, work_turns -270, weeds_new +2, water_hour +0.96. Hands 7 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `cf9f405831de` | v312 | crossover | **+4,014** | 5.4 | 18-2 | -24,787 | +2,332 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, max_animals 17→19, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -9,334 -> final -20,201); days 21-28 drivers: sales_rev -21,532, work_turns -65, weeds_new +3, water_hour +1.41. Hands 7 vs 9, animals 13 vs 11, plants 14 vs 33. |
| `3e744f448178` | v312 | mutate | **+3,805** | 3.6 | 16-4 | -24,664 | +3,207 | melon_floor 0→200, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -3,487 -> final -12,279); days 21-28 drivers: sales_rev -16,154, work_turns -87, idle_turns +39, weeds_new +1. Hands 9 vs 9, animals 10 vs 11, plants 22 vs 33. |
| `85560bea67d0` | c1 | paired | **+3,802** | 3.8 | 16-4 | -28,204 | +4,511 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→7, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,507 -> final -16,484); days 14-21 drivers: sales_rev -16,601, work_turns -222. Hands 9 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `0550420abff9` | v312 | mutate | **+3,610** | 3.9 | 16-4 | -24,128 | +2,461 | melon_floor 0→200, harvest_min 1→2, wheat_stock 0→3, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→19, wheat_cap 22→17, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -4,310 -> final -17,224); days 21-28 drivers: sales_rev -19,422, weeds_new +4, work_turns -54, water_hour +1.39. Hands 8 vs 9, animals 15 vs 11, plants 20 vs 33. |
| `d1e7da72c022` | queue | archive_crossover:crossover_g000025_20260910-115246_0 | **+3,531** | 2.7 | 14-6 | -30,530 | +5,947 | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,761 -> final -14,679); days 14-21 drivers: sales_rev -15,329, work_turns -210, water_hour +0.29, travel_per_task +0.02. Hands 13 vs 14, animals 7 vs 11, plants |
| `ba3da54ca5af` | queue | crossover | **+3,476** | 3.4 | 15-5 | -24,717 | +3,431 | melon_floor 0→150, min_hands 3→4, open_wheat 7→4, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,912 -> final -35,280); days 14-21 drivers: sales_rev -19,978, work_turns -213, weeds_new +3, water_hour +0.69. Hands 9 vs 14, animals 7 vs 11, plants 64 vs 84. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `d5d57976e061` | queue | archive_crossover:crossover_g000075_20260910-122443_0 | +6,378 | 3.2 | 9-1 | -23,444 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `484eef25d104` | queue | mutate | +6,313 | 2.4 | 8-2 | -26,423 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→11, fert_keep 0→1, max_animals 17→20, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `01e555df4a78` | queue | mutate | +6,006 | 4.5 | 10-0 | -22,883 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
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

## Islands (best dev margin, population size)

- H32: best +2,590 (`e131bf22f2da`), n=73
- M2: best +4,110 (`2521e3906eb6`), n=66
- c1: best +4,572 (`f5e71682ea28`), n=96
- queue: best +6,527 (`edd7288369ba`), n=178
- v312: best +4,992 (`e05397e4510f`), n=82
- wide: best +5,473 (`1019eca510ac`), n=84

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +9,498 | 61 | 100 | 39 | 561 | 14.5 | 61: +2,889 (n=21), 78: +904 (n=6), 91: +839 (n=2), 124: +405 (n=3), 112: +174 (n=3), 90: -66 (n=8), 74: -125 (n=2), 115: -447 (n=6), 102: -570 (n=32), 84: -646 (n=7), 100: -693 (n=414), 85: -943 (n=19), 83: -1,174 (n=3), 82: -2,202 (n=2), 92: -2,233 (n=17), 71: -2,386 (n=2), 114: -3,075 (n=2), 104: -3,341 (n=2), 110: -4,472 (n=6), 95: -5,822 (n=2), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,879 | 0.4 | 0.0 | 7 | 579 | 3.7 | 0.4: +1,784 (n=3), 0.1: +773 (n=24), 0.2: -319 (n=39), 0.0: -563 (n=389), 0.3: -1,354 (n=119), 0.6: -3,949 (n=3), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,442 | 40 | 38 | 22 | 576 | 4.9 | 40: +1,990 (n=52), 37: +1,446 (n=7), 39: +584 (n=72), 27: +439 (n=10), 41: +28 (n=10), 33: -247 (n=3), 50: -251 (n=3), 32: -731 (n=10), 35: -797 (n=66), 36: -884 (n=2), 34: -975 (n=179), 31: -1,204 (n=3), 38: -1,755 (n=130), 25: -1,798 (n=3), 28: -1,927 (n=2), 43: -2,597 (n=12), 42: -2,924 (n=3), 46: -3,322 (n=7), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,987 | 134 | 92 | 45 | 562 | 17.83 | 134: +1,252 (n=3), 95: +944 (n=9), 102: +578 (n=20), 124: +54 (n=10), 85: -292 (n=2), 58: -314 (n=32), 92: -478 (n=378), 107: -484 (n=10), 121: -689 (n=6), 106: -780 (n=2), 87: -942 (n=4), 81: -1,046 (n=2), 118: -1,081 (n=2), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 11: -1,702 (n=40), 73: -1,731 (n=2), 16: -1,741 (n=3), 150: -1,878 (n=11), 72: -1,999 (n=3), 78: -2,201 (n=2), 0: -2,575 (n=3), 76: -3,783 (n=2), 115: -3,837 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +6,641 | 0.7 | 0.55 | 14 | 576 | 5.36 | 0.7: +2,447 (n=8), 0.65: +20 (n=45), 0.45: -107 (n=54), 0.55: -429 (n=333), 0.6: -652 (n=46), 0.5: -2,016 (n=61), 0.75: -2,922 (n=5), 0.8: -3,532 (n=4), 0.3: -3,973 (n=15), 0.85: -4,162 (n=2), 0.35: -4,194 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,547 | 18 | 20 | 11 | 578 | 4.5 | 18: +840 (n=48), 19: +379 (n=124), 22: -836 (n=9), 20: -862 (n=318), 15: -1,302 (n=4), 16: -1,526 (n=2), 17: -1,971 (n=10), 21: -2,347 (n=47), 23: -2,536 (n=11), 24: -5,706 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,408 | 6 | 8 | 10 | 579 | 3.51 | 6: +988 (n=6), 10: -115 (n=261), 9: -460 (n=28), 11: -569 (n=44), 14: -756 (n=4), 8: -1,227 (n=213), 4: -1,964 (n=3), 7: -2,219 (n=10), 12: -2,235 (n=5), 5: -5,419 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +6,396 | 27 | 30 | 14 | 577 | 4.89 | 27: +371 (n=19), 25: -339 (n=197), 31: -606 (n=5), 30: -691 (n=283), 29: -893 (n=16), 37: -1,594 (n=2), 26: -1,640 (n=30), 28: -2,037 (n=9), 36: -2,144 (n=8), 34: -2,305 (n=4), 35: -2,708 (n=2), 33: -6,025 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,974 | 2 | 3 | 3 | 579 | 0.89 | 2: +908 (n=197), 3: -1,330 (n=365), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,732 | 2 | 2 | 4 | 579 | 2.56 | 2: -453 (n=516), 1: -2,083 (n=53), 0: -4,267 (n=7), 3: -6,185 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +5,654 | 9 | 14 | 9 | 578 | 3.53 | 9: +1,706 (n=4), 10: +559 (n=127), 12: -996 (n=63), 14: -1,029 (n=327), 13: -1,069 (n=47), 11: -1,152 (n=6), 8: -3,091 (n=2), 7: -3,948 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,556 | 13 | 14 | 7 | 579 | 3.81 | 13: -240 (n=61), 14: -526 (n=398), 12: -832 (n=66), 11: -1,360 (n=8), 15: -1,574 (n=32), 16: -2,938 (n=10), 10: -5,796 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,548 | 0.3 | 0.25 | 11 | 578 | 5.85 | 0.3: +1,081 (n=16), 0.4: +581 (n=93), 0.45: -172 (n=25), 0.25: -787 (n=396), 0.1: -945 (n=2), 0.5: -1,613 (n=5), 0.15: -1,761 (n=4), 0.2: -1,768 (n=9), 0.35: -3,916 (n=26), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,732 | 2 | 2 | 3 | 579 | 1.84 | 2: -492 (n=548), 1: -3,451 (n=22), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +4,286 | 22 | 17 | 9 | 578 | 2.85 | 22: +1,567 (n=63), 18: -68 (n=27), 20: -271 (n=11), 17: -922 (n=278), 19: -997 (n=171), 16: -1,257 (n=9), 14: -2,487 (n=15), 21: -2,719 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_buy | +4,264 | 1 | 3 | 3 | 579 | 1.64 | 1: +2,428 (n=2), 3: -538 (n=510), 0: -1,836 (n=67) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,976 | frontier | frontier | 2 | 579 | 0.87 | frontier: -410 (n=540), v312: -4,386 (n=39) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +3,914 | 1 | 0 | 3 | 579 | 1.62 | 1: +1,857 (n=69), 0: -1,013 (n=506), 2: -2,057 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +3,796 | 5 | 22 | 15 | 576 | 5.38 | 5: +1,086 (n=12), 13: +153 (n=77), 12: -391 (n=22), 22: -564 (n=306), 25: -887 (n=83), 24: -955 (n=11), 17: -1,225 (n=5), 21: -1,542 (n=2), 20: -1,750 (n=17), 18: -2,116 (n=25), 19: -2,474 (n=7), 23: -2,710 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +3,164 | 3 | 6 | 7 | 579 | 3.16 | 3: +270 (n=152), 6: -928 (n=344), 8: -1,059 (n=4), 4: -1,245 (n=3), 7: -1,311 (n=42), 5: -1,382 (n=31), 9: -2,894 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (7, 3, 4): +6,527 (n=65)
- (9, 3, 5): +6,313 (n=18)
- (9, 3, 3): +6,108 (n=9)
- (7, 3, 3): +6,006 (n=26)
- (12, 4, 6): +5,330 (n=13)
- (8, 3, 5): +5,290 (n=17)
- (8, 3, 4): +4,836 (n=30)
- (10, 3, 4): +4,807 (n=19)
- (6, 3, 3): +4,589 (n=14)
- (7, 3, 5): +4,572 (n=11)
- (10, 4, 6): +4,214 (n=35)
- (16, 3, 6): +4,008 (n=6)
- (9, 3, 4): +3,671 (n=38)
- (14, 3, 6): +3,652 (n=11)
- (10, 3, 5): +3,207 (n=21)

_Generated 2026-09-10 12:50. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 274 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=274); harvest_min=1–3 (n=274); wheat_tiles=0–5 (n=274); wheat_stock=0–19 (n=274); min_hands=3–6 (n=274); load_per_hand=12–26 (n=274); geese=0–2 (n=274); open_melons=4–14 (n=274)
- **Evidence:** 274 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 12:50. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._