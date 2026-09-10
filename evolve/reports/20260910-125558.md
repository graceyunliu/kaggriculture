# Evolution run 20260910-125558

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 1.06 h · candidates evaluated this run: 105 · games 12,002 (11,268/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 11 | 22 |
| dead_pattern | 12 | 24 |
| dead_smoke | 5 | 40 |
| alive | 59 | 6372 |
| held_fail | 18 | 5544 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 681 · held-out evaluated: 93 · held-out PASS: 1

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `6f3d8ebff9ba` | queue | archive_crossover:crossover_g000075_20260910-134012_1 | **+5,961** | 4.6 | 18-2 | -25,943 | +5,741 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,968 -> final -16,571); days 21-28 drivers: sales_rev -12,145, weeds_new +9, work_turns -80, missed_feed +5. Hands 6 vs 9, animals 12 vs 11, plants 11 vs 33. |
| `01e555df4a78` | queue | mutate | **+5,528** | 4.3 | 18-2 | -26,568 | +6,006 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,862 -> final -36,124); days 15-22 drivers: sales_rev -18,382, work_turns -200, idle_turns +7. Hands 14 vs 14, animals 7 vs 11, plants 66 vs 85. |
| `2757e6c92f26` | queue | mutate | **+5,444** | 4.3 | 18-2 | -25,327 | +5,290 | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,317 -> final -13,211); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `572cf859ec7f` | queue | mutate | **+5,091** | 5.7 | 18-2 | -26,809 | +5,321 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_water_tier 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,862 -> final -35,905); days 15-22 drivers: sales_rev -16,882, work_turns -199, weeds_new +1, water_hour +0.5. Hands 14 vs 14, animals 7 vs 11, plants 63 vs 85. |
| `b3324e9b7110` | queue | mutate | **+4,961** | 3.3 | 19-1 | -29,707 | +6,108 | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -6,908 -> final -18,802); days 22-29 drivers: sales_rev -23,772, weeds_new +9, work_turns -103, reversals +2. Hands 3 vs 6, animals 9 vs 11, plants 0 vs 17. |
| `da68944524c1` | v312 | mutate | **+4,758** | 4.6 | 18-2 | -25,433 | +2,514 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 22 (gap -3,186 -> final -29,992); days 20-27 drivers: sales_rev -36,606, work_turns -73, water_hour +1.41. Hands 10 vs 11, animals 10 vs 11, plants 42 vs 47. |
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `da35edd17aae` | c1 | mutate | **+4,444** | 3.5 | 16-4 | -28,173 | +3,141 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→7, fert_keep 0→1, max_animals 17→15, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→56, HERD_LAST_DAY 17→21, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→11 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,507 -> final -16,484); days 14-21 drivers: sales_rev -16,601, work_turns -222. Hands 9 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `721d894fe338` | queue | mutate | **+4,281** | 4.7 | 17-3 | -28,345 | +3,190 | feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→112, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -3,167 -> final -14,247); days 22-29 drivers: sales_rev -20,412, weeds_new +19, idle_turns +34, missed_feed +6. Hands 6 vs 6, animals 16 vs 11, plants 12 vs 17. |
| `bcfe45a8f2f1` | queue | archive_crossover:crossover_g000075_20260910-122443_1 | **+4,166** | 3.4 | 17-3 | -27,271 | +4,807 | melon_floor 0→150, harvest_min 1→2, open_wheat 7→8, demand_share 0.55→0.65, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 21 (gap -3,281 -> final -40,264); days 19-26 drivers: sales_rev -36,636, weeds_new +8, work_turns -89, water_hour +0.81. Hands 11 vs 11, animals 12 vs 11, plants 43 vs 53 |
| `4da7ca753338` | queue | mutate | **+4,083** | 3.5 | 16-4 | -23,668 | +4,086 | open_wheat 7→4, feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,249 -> final -24,602); days 14-21 drivers: sales_rev -16,963, work_turns -270, weeds_new +2, water_hour +0.96. Hands 7 vs 14, animals 7 vs 11, plants 67 vs 84. |
| `cf9f405831de` | v312 | crossover | **+4,014** | 5.4 | 18-2 | -24,787 | +2,332 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, max_animals 17→19, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -9,334 -> final -20,201); days 21-28 drivers: sales_rev -21,532, work_turns -65, weeds_new +3, water_hour +1.41. Hands 7 vs 9, animals 13 vs 11, plants 14 vs 33. |
| `3e744f448178` | v312 | mutate | **+3,805** | 3.6 | 16-4 | -24,664 | +3,207 | melon_floor 0→200, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 23 (gap -3,487 -> final -12,279); days 21-28 drivers: sales_rev -16,154, work_turns -87, idle_turns +39, weeds_new +1. Hands 9 vs 9, animals 10 vs 11, plants 22 vs 33. |
| `85560bea67d0` | c1 | paired | **+3,802** | 3.8 | 16-4 | -28,204 | +4,511 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→7, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,507 -> final -16,484); days 14-21 drivers: sales_rev -16,601, work_turns -222. Hands 9 vs 14, animals 7 vs 11, plants 68 vs 84. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `eaaa039aa15f` | v312 | mutate | +7,275 | 3.5 | 9-1 | -21,152 | held_fail | melon_floor 0→100, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_sell_price 30→29, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `0e5fdf0a265c` | queue | migrate | +7,036 | 3.4 | 9-1 | -21,325 | held_fail | melon_floor 0→100, harvest_min 1→2, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_sell_price 30→29, labor_reserve_buffer 92→109, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `47f6c615f8e1` | H32 | paired | +6,967 | 3.6 | 10-0 | -25,995 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→4, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, SPREAD_CAP 3→4 · blocks: hiring |
| `ca945e166163` | queue | archive_crossover:crossover_g000050_20260910-132600_1 | +6,843 | 2.6 | 9-1 | -26,353 | held_fail | melon_floor 0→100, wheat_tiles 0→1, load_per_hand 20→18, open_melons 8→10, early_hire_days 5→4, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→61, MAX_SHEEP 14→9 · blocks: hiring |
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `32a6642f084e` | queue | mutate | +6,510 | 3.3 | 9-1 | -23,092 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |
| `d5d57976e061` | queue | archive_crossover:crossover_g000075_20260910-122443_0 | +6,378 | 3.2 | 9-1 | -23,444 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `484eef25d104` | queue | mutate | +6,313 | 2.4 | 8-2 | -26,423 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→11, fert_keep 0→1, max_animals 17→20, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `01e555df4a78` | queue | mutate | +6,006 | 4.5 | 10-0 | -22,883 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `d1e7da72c022` | queue | archive_crossover:crossover_g000025_20260910-115246_0 | +5,947 | 3.2 | 9-1 | -24,175 | held_fail | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `7dc55534f846` | v312 | mutate | +5,864 | 4.4 | 9-1 | -21,547 | held_fail | wheat_tiles 0→1, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_sell_price 30→29, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→9, SPREAD_W 1.25→1.0 · blocks: hiring |
| `6f3d8ebff9ba` | queue | archive_crossover:crossover_g000075_20260910-134012_1 | +5,741 | 7.2 | 10-0 | -23,843 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `9022cee22a50` | wide | crossover | +5,625 | 2.9 | 8-2 | -24,614 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, feed_spare_poor 0→1, wheat_sell_price 30→27, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→63, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `396122e8b4e3` | queue | archive_crossover:crossover_g000025_20260910-131447_1 | +5,533 | 3.1 | 8-2 | -25,686 | held_fail | melon_floor 0→100, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, fert_keep 0→1, demand_share 0.55→0.6, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +6,967 (`47f6c615f8e1`), n=85
- M2: best +4,110 (`2521e3906eb6`), n=79
- c1: best +4,572 (`f5e71682ea28`), n=114
- queue: best +7,036 (`0e5fdf0a265c`), n=206
- v312: best +7,275 (`eaaa039aa15f`), n=97
- wide: best +5,625 (`9022cee22a50`), n=100

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +9,574 | 63 | 100 | 48 | 658 | 16.44 | 63: +2,964 (n=2), 61: +2,499 (n=33), 90: +1,425 (n=18), 91: +839 (n=2), 150: +785 (n=2), 78: +458 (n=8), 130: +426 (n=2), 124: +405 (n=3), 112: +174 (n=3), 74: -125 (n=2), 102: -364 (n=41), 115: -447 (n=6), 84: -582 (n=10), 100: -587 (n=459), 82: -775 (n=4), 83: -1,174 (n=3), 85: -1,436 (n=23), 92: -2,057 (n=19), 117: -2,348 (n=2), 71: -2,386 (n=2), 114: -3,075 (n=2), 104: -3,341 (n=2), 110: -4,472 (n=6), 95: -5,822 (n=2), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +9,068 | 44 | 38 | 25 | 676 | 5.3 | 44: +3,616 (n=2), 40: +2,108 (n=74), 37: +979 (n=10), 39: +681 (n=88), 27: +105 (n=12), 33: +22 (n=4), 41: -127 (n=11), 50: -251 (n=3), 35: -662 (n=71), 32: -731 (n=10), 34: -875 (n=213), 31: -1,204 (n=3), 38: -1,729 (n=140), 36: -1,766 (n=3), 25: -1,798 (n=3), 28: -1,927 (n=2), 43: -2,137 (n=13), 42: -2,157 (n=4), 46: -2,600 (n=8), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +7,223 | 95 | 92 | 48 | 663 | 18.82 | 95: +1,488 (n=18), 134: +1,252 (n=3), 102: +578 (n=20), 124: +54 (n=10), 87: -263 (n=5), 107: -288 (n=13), 58: -307 (n=39), 92: -322 (n=438), 78: -337 (n=3), 85: -408 (n=3), 110: -471 (n=3), 121: -935 (n=7), 81: -1,046 (n=2), 118: -1,081 (n=2), 106: -1,134 (n=3), 0: -1,222 (n=5), 150: -1,356 (n=14), 88: -1,408 (n=2), 59: -1,461 (n=3), 94: -1,493 (n=3), 11: -1,569 (n=47), 73: -1,731 (n=2), 16: -1,741 (n=3), 72: -1,999 (n=3), 108: -2,567 (n=2), 76: -3,783 (n=2), 115: -3,837 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,022 | 27 | 30 | 14 | 679 | 4.6 | 27: +997 (n=27), 29: +227 (n=27), 25: -101 (n=243), 31: -606 (n=5), 30: -685 (n=317), 26: -1,458 (n=33), 37: -1,594 (n=2), 28: -2,037 (n=9), 36: -2,144 (n=8), 34: -2,305 (n=4), 35: -2,708 (n=2), 33: -6,025 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,812 | 0.1 | 0.0 | 8 | 680 | 3.69 | 0.1: +717 (n=25), 0.2: +217 (n=54), 0.0: -372 (n=456), 0.4: -637 (n=7), 0.3: -1,211 (n=132), 0.6: -3,382 (n=4), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +6,441 | 0.7 | 0.55 | 14 | 678 | 5.25 | 0.7: +1,843 (n=9), 0.6: -32 (n=66), 0.45: -124 (n=60), 0.55: -146 (n=385), 0.65: -331 (n=52), 0.5: -1,827 (n=71), 0.75: -2,542 (n=6), 0.8: -3,532 (n=4), 0.3: -3,947 (n=17), 0.85: -4,162 (n=2), 0.35: -4,598 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,363 | 18 | 20 | 11 | 680 | 4.35 | 18: +1,067 (n=63), 19: +710 (n=153), 22: -666 (n=10), 20: -758 (n=364), 15: -1,302 (n=4), 16: -1,526 (n=2), 17: -1,556 (n=13), 21: -2,340 (n=52), 23: -2,536 (n=11), 24: -5,296 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +6,270 | 9 | 14 | 9 | 680 | 3.19 | 9: +3,269 (n=7), 10: +848 (n=178), 11: -531 (n=10), 14: -989 (n=356), 13: -1,005 (n=55), 12: -1,095 (n=68), 8: -2,826 (n=3), 7: -3,001 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +6,227 | 2 | 3 | 3 | 681 | 0.81 | 2: +1,161 (n=254), 3: -1,316 (n=410), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,988 | 0.3 | 0.25 | 11 | 680 | 5.59 | 0.3: +1,522 (n=23), 0.45: +516 (n=32), 0.4: +501 (n=120), 0.25: -695 (n=448), 0.1: -945 (n=2), 0.5: -966 (n=7), 0.2: -1,385 (n=10), 0.15: -1,761 (n=4), 0.35: -2,754 (n=32), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,921 | 2 | 2 | 4 | 681 | 2.58 | 2: -264 (n=609), 1: -1,945 (n=61), 0: -4,111 (n=8), 3: -6,185 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,596 | 10 | 8 | 10 | 681 | 3.74 | 10: +177 (n=323), 6: +126 (n=12), 14: -439 (n=5), 9: -534 (n=32), 11: -820 (n=52), 8: -1,161 (n=230), 12: -1,253 (n=6), 7: -1,535 (n=13), 4: -1,964 (n=3), 5: -5,419 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +4,947 | 13 | 14 | 7 | 681 | 3.94 | 13: -219 (n=68), 14: -264 (n=481), 12: -877 (n=71), 11: -1,601 (n=9), 15: -1,640 (n=36), 16: -2,466 (n=11), 10: -5,166 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,907 | 2 | 2 | 3 | 681 | 1.85 | 2: -317 (n=646), 1: -3,035 (n=26), 3: -5,224 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +4,788 | 1 | 5 | 9 | 681 | 5.74 | 1: +2,196 (n=2), 4: +427 (n=41), 8: -346 (n=14), 5: -461 (n=510), 7: -521 (n=28), 6: -564 (n=22), 2: -1,089 (n=3), 3: -1,159 (n=53), 0: -2,592 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +3,973 | 5 | 22 | 16 | 677 | 5.42 | 5: +1,263 (n=13), 13: +175 (n=87), 22: -258 (n=362), 21: -550 (n=3), 12: -586 (n=26), 25: -782 (n=99), 24: -948 (n=18), 17: -1,225 (n=5), 19: -1,644 (n=9), 20: -1,826 (n=20), 18: -2,052 (n=26), 23: -2,710 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,783 | frontier | frontier | 2 | 681 | 0.86 | frontier: -219 (n=633), v312: -4,002 (n=48) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +3,708 | 3 | 0 | 14 | 676 | 6.84 | 3: +259 (n=5), 0: -361 (n=589), 7: -559 (n=9), 9: -814 (n=11), 1: -1,183 (n=4), 14: -1,284 (n=2), 6: -1,556 (n=7), 4: -1,644 (n=47), 15: -3,450 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,697 | 22 | 17 | 9 | 680 | 2.65 | 22: +1,519 (n=100), 20: +143 (n=13), 18: +124 (n=31), 17: -819 (n=310), 19: -929 (n=192), 16: -932 (n=10), 21: -1,449 (n=8), 14: -2,178 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +3,396 | 4 | 6 | 7 | 681 | 2.98 | 4: +502 (n=8), 3: +330 (n=191), 6: -732 (n=387), 5: -811 (n=38), 7: -1,348 (n=48), 8: -1,670 (n=6), 9: -2,894 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 4, 6): +7,275 (n=40)
- (7, 3, 4): +6,967 (n=81)
- (7, 3, 3): +6,843 (n=34)
- (9, 3, 5): +6,313 (n=24)
- (9, 3, 3): +6,108 (n=10)
- (12, 3, 5): +5,741 (n=10)
- (8, 3, 5): +5,533 (n=20)
- (12, 4, 6): +5,330 (n=15)
- (14, 3, 6): +5,311 (n=12)
- (15, 3, 6): +5,205 (n=10)
- (8, 3, 4): +4,836 (n=35)
- (10, 3, 4): +4,807 (n=21)
- (6, 3, 3): +4,589 (n=18)
- (7, 3, 5): +4,572 (n=13)
- (7, 4, 6): +4,026 (n=4)

_Generated 2026-09-10 13:59. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 315 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=315); harvest_min=1–3 (n=315); wheat_tiles=0–5 (n=315); wheat_stock=0–19 (n=315); min_hands=3–6 (n=315); load_per_hand=12–26 (n=315); geese=0–2 (n=315); open_melons=4–14 (n=315)
- **Evidence:** 315 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 13:59. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._