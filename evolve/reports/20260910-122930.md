# Evolution run 20260910-122930

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.80 h · candidates evaluated this run: 53 · games 7,582 (9,529/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 5 | 10 |
| dead_pattern | 2 | 4 |
| dead_smoke | 0 | 0 |
| alive | 39 | 4992 |
| held_fail | 7 | 2576 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 625 · held-out evaluated: 79 · held-out PASS: 1

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
| `572cf859ec7f` | queue | mutate | **+5,091** | 5.7 | 18-2 | -26,809 | +5,321 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_water_tier 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,862 -> final -35,905); days 15-22 drivers: sales_rev -16,882, work_turns -199, weeds_new +1, water_hour +0.5. Hands 14 vs 14, animals 7 vs 11, plants 63 vs 85. |
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
| `1b09520012a4` | queue | crossover | **+3,641** | 3.3 | 17-3 | -25,898 | +4,859 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→27, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,259 -> final -4,863); days 14-21 drivers: sales_rev -16,071, work_turns -227. Hands 10 vs 14, animals 7 vs 11, plants 66 vs 84. |
| `0550420abff9` | v312 | mutate | **+3,610** | 3.9 | 16-4 | -24,128 | +2,461 | melon_floor 0→200, harvest_min 1→2, wheat_stock 0→3, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→19, wheat_cap 22→17, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -4,310 -> final -17,224); days 21-28 drivers: sales_rev -19,422, weeds_new +4, work_turns -54, water_hour +1.39. Hands 8 vs 9, animals 15 vs 11, plants 20 vs 33. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `eaaa039aa15f` | v312 | mutate | +7,275 | 3.5 | 9-1 | -21,152 | held_fail | melon_floor 0→100, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_sell_price 30→29, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `32a6642f084e` | queue | mutate | +6,510 | 3.3 | 9-1 | -23,092 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |
| `d5d57976e061` | queue | archive_crossover:crossover_g000075_20260910-122443_0 | +6,378 | 3.2 | 9-1 | -23,444 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `484eef25d104` | queue | mutate | +6,313 | 2.4 | 8-2 | -26,423 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→11, fert_keep 0→1, max_animals 17→20, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `01e555df4a78` | queue | mutate | +6,006 | 4.5 | 10-0 | -22,883 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `d1e7da72c022` | queue | archive_crossover:crossover_g000025_20260910-115246_0 | +5,947 | 3.2 | 9-1 | -24,175 | held_fail | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `9022cee22a50` | wide | crossover | +5,625 | 2.9 | 8-2 | -24,614 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, feed_spare_poor 0→1, wheat_sell_price 30→27, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→63, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `396122e8b4e3` | queue | archive_crossover:crossover_g000025_20260910-131447_1 | +5,533 | 3.1 | 8-2 | -25,686 | held_fail | melon_floor 0→100, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, fert_keep 0→1, demand_share 0.55→0.6, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `d9f6714af711` | queue | archive_crossover:crossover_g000050_20260910-120943_0 | +5,523 | 2.6 | 8-2 | -26,352 | held_fail | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→27, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `1019eca510ac` | wide | paired | +5,473 | 2.3 | 8-2 | -24,553 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `8d73168f191f` | wide | paired | +5,425 | 2.7 | 9-1 | -28,015 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→27, wheat_hold_days 0→2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |
| `d5fdd7605657` | queue | archive_crossover:crossover_g000050_20260910-111312_1 | +5,411 | 2.6 | 8-2 | -23,346 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `bcf4dbd52f8d` | queue | mutate | +5,330 | 3.5 | 9-1 | -20,888 | held_fail | load_per_hand 20→19, open_wheat 7→4, early_hire_days 5→6, feed_spare_poor 0→1, demand_share 0.55→0.7, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, OPP_GROWTH 1.4→1.2 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,590 (`e131bf22f2da`), n=77
- M2: best +4,110 (`2521e3906eb6`), n=72
- c1: best +4,572 (`f5e71682ea28`), n=105
- queue: best +6,527 (`edd7288369ba`), n=191
- v312: best +7,275 (`eaaa039aa15f`), n=88
- wide: best +5,625 (`9022cee22a50`), n=92

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +9,574 | 63 | 100 | 44 | 604 | 15.6 | 63: +2,964 (n=2), 61: +2,889 (n=24), 90: +1,059 (n=12), 78: +904 (n=6), 91: +839 (n=2), 124: +405 (n=3), 112: +174 (n=3), 74: -125 (n=2), 82: -126 (n=3), 102: -437 (n=37), 115: -447 (n=6), 100: -629 (n=436), 84: -734 (n=8), 85: -1,044 (n=21), 83: -1,174 (n=3), 92: -2,308 (n=18), 117: -2,348 (n=2), 71: -2,386 (n=2), 114: -3,075 (n=2), 104: -3,341 (n=2), 110: -4,472 (n=6), 95: -5,822 (n=2), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +8,440 | 0.4 | 0.0 | 8 | 624 | 3.7 | 0.4: +2,344 (n=4), 0.1: +773 (n=24), 0.2: -90 (n=47), 0.0: -471 (n=419), 0.3: -1,271 (n=125), 0.6: -3,949 (n=3), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,519 | 40 | 38 | 23 | 621 | 4.94 | 40: +2,066 (n=65), 37: +1,270 (n=9), 39: +548 (n=77), 27: +190 (n=11), 41: +28 (n=10), 33: -247 (n=3), 50: -251 (n=3), 35: -696 (n=69), 32: -731 (n=10), 34: -846 (n=194), 31: -1,204 (n=3), 38: -1,760 (n=135), 36: -1,766 (n=3), 25: -1,798 (n=3), 28: -1,927 (n=2), 43: -2,597 (n=12), 42: -2,924 (n=3), 46: -3,322 (n=7), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +7,478 | 95 | 92 | 46 | 608 | 18.46 | 95: +1,743 (n=12), 134: +1,252 (n=3), 102: +578 (n=20), 124: +54 (n=10), 58: -274 (n=36), 85: -292 (n=2), 92: -380 (n=408), 107: -433 (n=12), 121: -689 (n=6), 106: -780 (n=2), 87: -942 (n=4), 81: -1,046 (n=2), 118: -1,081 (n=2), 0: -1,208 (n=4), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 11: -1,652 (n=44), 73: -1,731 (n=2), 16: -1,741 (n=3), 150: -1,878 (n=11), 72: -1,999 (n=3), 78: -2,201 (n=2), 108: -2,567 (n=2), 76: -3,783 (n=2), 115: -3,837 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +6,911 | 27 | 30 | 14 | 623 | 4.72 | 27: +886 (n=24), 25: -180 (n=219), 29: -347 (n=19), 31: -606 (n=5), 30: -703 (n=297), 26: -1,548 (n=32), 37: -1,594 (n=2), 28: -2,037 (n=9), 36: -2,144 (n=8), 34: -2,305 (n=4), 35: -2,708 (n=2), 33: -6,025 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,765 | 18 | 20 | 11 | 624 | 4.42 | 18: +1,059 (n=55), 19: +529 (n=137), 22: -666 (n=10), 20: -812 (n=338), 15: -1,302 (n=4), 16: -1,526 (n=2), 17: -1,740 (n=12), 21: -2,353 (n=50), 23: -2,536 (n=11), 24: -5,706 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +6,641 | 0.7 | 0.55 | 14 | 622 | 5.35 | 0.7: +2,447 (n=8), 0.45: -120 (n=57), 0.65: -233 (n=49), 0.6: -266 (n=55), 0.55: -287 (n=359), 0.5: -1,961 (n=64), 0.75: -2,922 (n=5), 0.8: -3,532 (n=4), 0.3: -3,955 (n=16), 0.85: -4,162 (n=2), 0.35: -4,194 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +6,118 | 2 | 3 | 3 | 625 | 0.84 | 2: +1,052 (n=225), 3: -1,326 (n=383), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,843 | 2 | 2 | 4 | 625 | 2.56 | 2: -342 (n=557), 1: -2,037 (n=58), 0: -4,267 (n=7), 3: -6,185 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,774 | 0.3 | 0.25 | 11 | 624 | 5.71 | 0.3: +1,307 (n=21), 0.4: +596 (n=102), 0.45: +237 (n=29), 0.5: -673 (n=6), 0.25: -762 (n=419), 0.1: -945 (n=2), 0.2: -1,385 (n=10), 0.15: -1,761 (n=4), 0.35: -3,197 (n=29), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +5,654 | 9 | 14 | 9 | 624 | 3.35 | 9: +1,706 (n=4), 10: +812 (n=154), 14: -1,014 (n=339), 12: -1,027 (n=65), 13: -1,079 (n=50), 11: -1,180 (n=7), 8: -2,826 (n=3), 7: -3,948 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,511 | 6 | 8 | 10 | 625 | 3.66 | 6: +92 (n=9), 10: +83 (n=291), 9: -572 (n=29), 11: -646 (n=47), 14: -756 (n=4), 8: -1,197 (n=222), 4: -1,964 (n=3), 7: -2,219 (n=10), 12: -2,235 (n=5), 5: -5,419 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +4,959 | 13 | 14 | 7 | 625 | 3.86 | 13: -207 (n=64), 14: -393 (n=434), 12: -785 (n=68), 15: -1,551 (n=34), 11: -1,601 (n=9), 16: -2,466 (n=11), 10: -5,166 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,826 | 2 | 2 | 3 | 625 | 1.85 | 2: -398 (n=593), 1: -3,236 (n=23), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +4,788 | 1 | 5 | 9 | 625 | 5.77 | 1: +2,196 (n=2), 4: -51 (n=31), 6: -210 (n=20), 5: -520 (n=470), 8: -556 (n=13), 7: -749 (n=25), 2: -1,089 (n=3), 3: -1,159 (n=53), 0: -2,592 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_buy | +4,185 | 1 | 3 | 3 | 625 | 1.65 | 1: +2,404 (n=3), 3: -437 (n=553), 0: -1,782 (n=69) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +4,155 | 22 | 17 | 9 | 624 | 2.74 | 22: +1,668 (n=78), 18: +124 (n=31), 20: +36 (n=12), 17: -883 (n=292), 16: -932 (n=10), 19: -967 (n=180), 21: -2,174 (n=6), 14: -2,487 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,911 | frontier | frontier | 2 | 625 | 0.87 | frontier: -309 (n=583), v312: -4,220 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +3,886 | 1 | 0 | 3 | 625 | 1.57 | 1: +1,829 (n=85), 0: -941 (n=536), 2: -2,057 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +3,796 | 5 | 22 | 15 | 622 | 5.42 | 5: +1,086 (n=12), 13: +243 (n=80), 22: -400 (n=333), 24: -606 (n=14), 12: -690 (n=25), 25: -815 (n=92), 17: -1,225 (n=5), 21: -1,542 (n=2), 20: -1,859 (n=18), 18: -2,116 (n=25), 19: -2,474 (n=7), 23: -2,710 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 4, 6): +7,275 (n=37)
- (7, 3, 4): +6,527 (n=75)
- (9, 3, 5): +6,313 (n=21)
- (9, 3, 3): +6,108 (n=9)
- (7, 3, 3): +6,006 (n=32)
- (8, 3, 5): +5,533 (n=19)
- (12, 4, 6): +5,330 (n=14)
- (8, 3, 4): +4,836 (n=31)
- (10, 3, 4): +4,807 (n=20)
- (6, 3, 3): +4,589 (n=15)
- (7, 3, 5): +4,572 (n=11)
- (7, 4, 6): +4,026 (n=4)
- (16, 3, 6): +4,008 (n=7)
- (9, 3, 4): +3,671 (n=42)
- (14, 3, 6): +3,652 (n=11)

_Generated 2026-09-10 13:17. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 290 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=290); harvest_min=1–3 (n=290); wheat_tiles=0–5 (n=290); wheat_stock=0–19 (n=290); min_hands=3–6 (n=290); load_per_hand=12–26 (n=290); geese=0–2 (n=290); open_melons=4–14 (n=290)
- **Evidence:** 290 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 13:17. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._