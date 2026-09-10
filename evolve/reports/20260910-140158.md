# Evolution run 20260910-140158

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 1.31 h · candidates evaluated this run: 102 · games 11,320 (8,634/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 8 | 16 |
| dead_pattern | 8 | 16 |
| dead_smoke | 14 | 112 |
| alive | 55 | 5940 |
| held_fail | 17 | 5236 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 807 · held-out evaluated: 129 · held-out PASS: 1

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `5251330b0932` | queue | crossover | **+6,035** | 4.7 | 18-2 | -26,119 | +4,743 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_water_tier 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,968 -> final -16,571); days 21-28 drivers: sales_rev -12,145, weeds_new +9, work_turns -80, missed_feed +5. Hands 6 vs 9, animals 12 vs 11, plants 11 vs 33. |
| `6f3d8ebff9ba` | queue | archive_crossover:crossover_g000075_20260910-134012_1 | **+5,961** | 4.6 | 18-2 | -25,943 | +5,741 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,968 -> final -16,571); days 21-28 drivers: sales_rev -12,145, weeds_new +9, work_turns -80, missed_feed +5. Hands 6 vs 9, animals 12 vs 11, plants 11 vs 33. |
| `01e555df4a78` | queue | mutate | **+5,528** | 4.3 | 18-2 | -26,568 | +6,006 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,862 -> final -36,124); days 15-22 drivers: sales_rev -18,382, work_turns -200, idle_turns +7. Hands 14 vs 14, animals 7 vs 11, plants 66 vs 85. |
| `2757e6c92f26` | queue | mutate | **+5,444** | 4.3 | 18-2 | -25,327 | +5,290 | melon_floor 0→150, open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, max_animals 17→16, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,317 -> final -13,211); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `572cf859ec7f` | queue | mutate | **+5,091** | 5.7 | 18-2 | -26,809 | +5,321 | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_water_tier 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,862 -> final -35,905); days 15-22 drivers: sales_rev -16,882, work_turns -199, weeds_new +1, water_hour +0.5. Hands 14 vs 14, animals 7 vs 11, plants 63 vs 85. |
| `b3324e9b7110` | queue | mutate | **+4,961** | 3.3 | 19-1 | -29,707 | +6,108 | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -6,908 -> final -18,802); days 22-29 drivers: sales_rev -23,772, weeds_new +9, work_turns -103, reversals +2. Hands 3 vs 6, animals 9 vs 11, plants 0 vs 17. |
| `da68944524c1` | v312 | mutate | **+4,758** | 4.6 | 18-2 | -25,433 | +2,514 | melon_floor 0→100, harvest_min 1→2, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→1, max_animals 17→18, labor_reserve_buffer 92→102, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_CAP 3→4 |  | cand falls behind C1 from day 22 (gap -3,186 -> final -29,992); days 20-27 drivers: sales_rev -36,606, work_turns -73, water_hour +1.41. Hands 10 vs 11, animals 10 vs 11, plants 42 vs 47. |
| `ea07aebc19a0` | queue | archive_crossover:crossover_g000050_20260910-143309_1 | **+4,741** | 3.1 | 16-4 | -27,503 | +6,461 | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -2,185 -> final -36,727); days 15-22 drivers: sales_rev -14,437, work_turns -169, water_hour +0.49. Hands 14 vs 14, animals 8 vs 11, plants 63 vs 85. |
| `aade4d85f6fe` | queue | mutate | **+4,575** | 3.2 | 16-4 | -25,453 | +3,787 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, wheat_water_tier 0→1, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.2 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `ad2831ed391f` | queue | crossover | **+4,571** | 6.1 | 20-0 | -28,053 | +3,607 | melon_floor 0→100, harvest_min 1→2, wheat_tiles 0→1, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→61, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -3,343 -> final -15,627); days 15-22 drivers: sales_rev -12,015, work_turns -206, weeds_new +5, water_hour +0.35. Hands 13 vs 14, animals 7 vs 11, plants 63 vs 85 |
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `da35edd17aae` | c1 | mutate | **+4,444** | 3.5 | 16-4 | -28,173 | +3,141 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→7, fert_keep 0→1, max_animals 17→15, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→56, HERD_LAST_DAY 17→21, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→11 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,507 -> final -16,484); days 14-21 drivers: sales_rev -16,601, work_turns -222. Hands 9 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `721d894fe338` | queue | mutate | **+4,281** | 4.7 | 17-3 | -28,345 | +3,190 | feed_spare_poor 0→1, wheat_cap 22→13, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→112, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→5 · blocks: hiring |  | cand falls behind C1 from day 24 (gap -3,167 -> final -14,247); days 22-29 drivers: sales_rev -20,412, weeds_new +19, idle_turns +34, missed_feed +6. Hands 6 vs 6, animals 16 vs 11, plants 12 vs 17. |
| `da34aefecb69` | queue | crossover | **+4,275** | 5.4 | 18-2 | -27,911 | +5,114 | load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→50, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,205 -> final -24,664); days 14-21 drivers: sales_rev -14,873, work_turns -225, idle_turns +28, water_hour +0.72. Hands 8 vs 14, animals 7 vs 11, plants 67 vs 8 |
| `bcfe45a8f2f1` | queue | archive_crossover:crossover_g000075_20260910-122443_1 | **+4,166** | 3.4 | 17-3 | -27,271 | +4,807 | melon_floor 0→150, harvest_min 1→2, open_wheat 7→8, demand_share 0.55→0.65, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 21 (gap -3,281 -> final -40,264); days 19-26 drivers: sales_rev -36,636, weeds_new +8, work_turns -89, water_hour +0.81. Hands 11 vs 11, animals 12 vs 11, plants 43 vs 53 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `eaaa039aa15f` | v312 | mutate | +7,275 | 3.5 | 9-1 | -21,152 | held_fail | melon_floor 0→100, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_sell_price 30→29, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `0e5fdf0a265c` | queue | migrate | +7,036 | 3.4 | 9-1 | -21,325 | held_fail | melon_floor 0→100, harvest_min 1→2, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_sell_price 30→29, labor_reserve_buffer 92→109, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `47f6c615f8e1` | H32 | paired | +6,967 | 3.6 | 10-0 | -25,995 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→4, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, SPREAD_CAP 3→4 · blocks: hiring |
| `ca945e166163` | queue | archive_crossover:crossover_g000050_20260910-132600_1 | +6,843 | 2.6 | 9-1 | -26,353 | held_fail | melon_floor 0→100, wheat_tiles 0→1, load_per_hand 20→18, open_melons 8→10, early_hire_days 5→4, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, labor_reserve_buffer 92→95, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→61, MAX_SHEEP 14→9 · blocks: hiring |
| `edd7288369ba` | queue | archive_crossover:crossover_g000025_20260910-105611_0 | +6,527 | 2.8 | 9-1 | -21,613 | held_fail | load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `32a6642f084e` | queue | mutate | +6,510 | 3.3 | 9-1 | -23,092 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |
| `ea07aebc19a0` | queue | archive_crossover:crossover_g000050_20260910-143309_1 | +6,461 | 4.0 | 10-0 | -22,249 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |
| `d5d57976e061` | queue | archive_crossover:crossover_g000075_20260910-122443_0 | +6,378 | 3.2 | 9-1 | -23,444 | held_fail | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `8805e34ee0d9` | queue | archive_crossover:crossover_g000025_20260910-141420_0 | +6,359 | 4.0 | 10-0 | -23,095 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, fert_keep 0→1, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |
| `484eef25d104` | queue | mutate | +6,313 | 2.4 | 8-2 | -26,423 | held_fail | melon_floor 0→200, load_per_hand 20→18, open_melons 8→11, fert_keep 0→1, max_animals 17→20, wheat_cap 22→24, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `503a6cc9fcd7` | c1 | crossover | +6,205 | 2.7 | 10-0 | -26,931 | held_fail | melon_floor 0→200, min_hands 3→4, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→3, MAX_SHEEP 14→9 · blocks: hiring |
| `4f90e211be96` | c1 | paired | +6,134 | 2.8 | 8-2 | -20,775 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, max_animals 17→15, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→40, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→3, MAX_SHEEP 14→10 · blocks: hiring |
| `b3324e9b7110` | queue | mutate | +6,108 | 2.6 | 10-0 | -28,038 | held_fail | harvest_min 1→2, load_per_hand 20→19, open_melons 8→10, open_wheat 7→8, fert_keep 0→1, wheat_sell_price 30→25, setup_capital_share 0.25→0.3, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→40, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10 · blocks: hiring |
| `3d03d9c72eee` | M2 | paired | +6,052 | 2.7 | 9-1 | -21,898 | held_fail | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, fert_keep 0→1, max_animals 17→20, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.45, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, NEAR_RADIUS 2→4, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |
| `3acf744e0aac` | wide | paired | +6,007 | 2.8 | 8-2 | -18,820 | held_fail | melon_floor 0→150, load_per_hand 20→18, open_melons 8→10, early_hire_days 5→8, fert_keep 0→1, fert_buy 3→2, max_animals 17→18, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→3, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→61, HERD_LAST_DAY 17→22, MAX_SHEEP 14→10, FERT_RADIUS 3→4, SPREAD_W 1.25→1.5 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +6,967 (`47f6c615f8e1`), n=101
- M2: best +6,052 (`3d03d9c72eee`), n=98
- c1: best +6,205 (`503a6cc9fcd7`), n=135
- queue: best +7,036 (`0e5fdf0a265c`), n=243
- v312: best +7,275 (`eaaa039aa15f`), n=116
- wide: best +6,007 (`3acf744e0aac`), n=114

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +9,574 | 63 | 100 | 52 | 788 | 20.32 | 63: +2,964 (n=2), 50: +2,863 (n=2), 61: +2,782 (n=62), 91: +1,562 (n=4), 56: +1,298 (n=3), 90: +1,253 (n=27), 124: +882 (n=4), 150: +785 (n=2), 112: +174 (n=3), 130: -107 (n=3), 74: -125 (n=2), 113: -208 (n=2), 149: -295 (n=2), 78: -318 (n=10), 104: -333 (n=4), 109: -403 (n=2), 115: -447 (n=6), 102: -466 (n=49), 100: -472 (n=509), 82: -775 (n=4), 84: -912 (n=11), 94: -1,151 (n=2), 83: -1,174 (n=3), 85: -1,549 (n=25), 92: -1,694 (n=25), 96: -2,205 (n=2), 117: -2,348 (n=2), 71: -2,386 (n=2), 103: -2,619 (n=2), 114: -3,075 (n=2), 110: -4,472 (n=6), 95: -5,822 (n=2), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +8,300 | 109 | 92 | 56 | 785 | 20.83 | 109: +2,564 (n=5), 93: +2,098 (n=2), 95: +1,953 (n=29), 41: +1,878 (n=2), 134: +1,252 (n=3), 81: +816 (n=3), 113: +767 (n=3), 102: +685 (n=25), 78: +334 (n=5), 59: +137 (n=5), 87: -32 (n=10), 124: -51 (n=11), 92: -111 (n=504), 85: -408 (n=3), 110: -471 (n=3), 58: -495 (n=45), 107: -576 (n=16), 118: -1,081 (n=2), 106: -1,134 (n=3), 121: -1,140 (n=9), 150: -1,214 (n=16), 88: -1,408 (n=2), 11: -1,480 (n=50), 94: -1,493 (n=3), 0: -1,635 (n=6), 73: -1,731 (n=2), 16: -1,741 (n=3), 72: -1,999 (n=3), 108: -2,567 (n=2), 76: -3,783 (n=2), 115: -3,837 (n=2), 114: -4,072 (n=2), 91: -5,597 (n=2), 69: -5,735 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,848 | 44 | 38 | 26 | 801 | 5.27 | 44: +2,395 (n=5), 40: +2,098 (n=103), 39: +863 (n=112), 37: +732 (n=13), 27: +219 (n=14), 41: +26 (n=13), 50: -251 (n=3), 34: -590 (n=251), 35: -717 (n=75), 32: -942 (n=11), 31: -1,204 (n=3), 36: -1,258 (n=4), 46: -1,523 (n=13), 38: -1,640 (n=149), 43: -1,693 (n=14), 25: -1,798 (n=3), 28: -1,927 (n=2), 42: -1,960 (n=5), 33: -2,467 (n=6), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_buy | +7,231 | 2 | 3 | 4 | 807 | 2.55 | 2: +5,751 (n=2), 1: +1,085 (n=5), 3: -145 (n=716), 0: -1,480 (n=84) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,572 | 0.1 | 0.0 | 8 | 807 | 4.39 | 0.1: +477 (n=30), 0.0: -40 (n=544), 0.2: -102 (n=72), 0.8: -295 (n=2), 0.4: -507 (n=9), 0.3: -1,171 (n=143), 0.6: -2,302 (n=5), 0.5: -6,095 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +6,441 | 0.7 | 0.55 | 14 | 805 | 5.8 | 0.7: +1,843 (n=9), 0.4: +597 (n=3), 0.6: +282 (n=93), 0.55: +112 (n=456), 0.45: -236 (n=68), 0.65: -365 (n=56), 0.5: -1,519 (n=82), 0.75: -2,303 (n=7), 0.3: -3,857 (n=18), 0.85: -4,162 (n=2), 0.8: -4,444 (n=5), 0.35: -4,598 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,429 | 18 | 20 | 12 | 805 | 4.12 | 18: +1,382 (n=94), 19: +856 (n=189), 22: -552 (n=13), 20: -640 (n=412), 15: -1,302 (n=4), 17: -1,419 (n=14), 16: -1,526 (n=2), 23: -2,063 (n=12), 21: -2,174 (n=56), 24: -5,046 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +6,336 | 2 | 3 | 3 | 807 | 0.64 | 2: +1,270 (n=350), 3: -1,294 (n=440), 4: -5,066 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +5,927 | 0.3 | 0.25 | 11 | 806 | 5.28 | 0.3: +1,461 (n=29), 0.4: +973 (n=155), 0.45: +764 (n=44), 0.1: -116 (n=4), 0.25: -602 (n=506), 0.5: -966 (n=7), 0.15: -1,314 (n=7), 0.2: -1,342 (n=11), 0.35: -2,172 (n=41), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +5,745 | 9 | 14 | 9 | 806 | 2.82 | 9: +2,773 (n=16), 10: +1,160 (n=239), 11: +329 (n=15), 14: -954 (n=385), 13: -968 (n=64), 12: -1,091 (n=78), 8: -2,342 (n=5), 7: -2,972 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +5,221 | 27 | 30 | 14 | 806 | 4.65 | 27: +986 (n=33), 29: +454 (n=40), 25: +277 (n=307), 31: +14 (n=7), 30: -617 (n=350), 26: -1,410 (n=38), 37: -1,594 (n=2), 28: -2,037 (n=9), 36: -2,144 (n=8), 34: -2,305 (n=4), 35: -2,708 (n=2), 32: -3,536 (n=3), 33: -4,235 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +5,200 | 1 | 5 | 9 | 807 | 5.62 | 1: +2,609 (n=3), 4: +1,046 (n=62), 8: -210 (n=19), 5: -257 (n=594), 7: -400 (n=36), 6: -661 (n=24), 2: -1,021 (n=4), 3: -1,267 (n=57), 0: -2,592 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,169 | 14 | 14 | 7 | 807 | 3.94 | 14: +3 (n=569), 13: -85 (n=80), 12: -812 (n=80), 15: -1,304 (n=43), 11: -1,433 (n=12), 16: -2,352 (n=18), 10: -5,166 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +4,788 | 2 | 2 | 4 | 807 | 2.57 | 2: -24 (n=720), 1: -1,807 (n=74), 0: -4,563 (n=9), 3: -4,812 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +4,545 | 1.8 | 1.4 | 9 | 806 | 4.46 | 1.8: +3,073 (n=2), 1.2: -112 (n=68), 1.4: -128 (n=550), 1.1: -233 (n=6), 1.3: -522 (n=88), 1.6: -721 (n=23), 1.5: -965 (n=51), 1.0: -1,472 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +4,439 | 2 | 2 | 3 | 807 | 1.84 | 2: -115 (n=764), 1: -2,372 (n=33), 3: -4,554 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +4,002 | 10 | 8 | 10 | 807 | 3.91 | 10: +408 (n=396), 6: +186 (n=16), 12: -195 (n=10), 9: -280 (n=38), 14: -439 (n=5), 11: -566 (n=63), 8: -1,071 (n=256), 7: -1,535 (n=13), 4: -1,964 (n=3), 5: -3,595 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,999 | frontier | frontier | 2 | 807 | 0.86 | frontier: +21 (n=750), v312: -3,979 (n=57) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +3,713 | 3 | 0 | 14 | 803 | 7.78 | 3: +263 (n=6), 1: +119 (n=6), 0: -124 (n=705), 9: -814 (n=11), 6: -862 (n=8), 7: -1,119 (n=12), 14: -1,284 (n=2), 4: -1,679 (n=49), 11: -2,959 (n=2), 15: -3,450 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +3,607 | 5 | 22 | 17 | 803 | 6.04 | 5: +1,251 (n=18), 13: +210 (n=95), 22: +48 (n=435), 24: -14 (n=25), 16: -544 (n=3), 21: -550 (n=3), 12: -624 (n=30), 19: -794 (n=13), 25: -914 (n=111), 17: -1,044 (n=6), 18: -1,580 (n=29), 20: -1,698 (n=25), 23: -2,356 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 4, 6): +7,275 (n=46)
- (7, 3, 4): +6,967 (n=99)
- (7, 3, 3): +6,843 (n=43)
- (9, 3, 5): +6,313 (n=29)
- (9, 3, 3): +6,108 (n=11)
- (12, 3, 5): +5,741 (n=12)
- (8, 3, 5): +5,533 (n=25)
- (7, 3, 5): +5,433 (n=18)
- (12, 4, 6): +5,330 (n=19)
- (14, 3, 6): +5,311 (n=17)
- (15, 3, 6): +5,205 (n=11)
- (8, 3, 4): +5,004 (n=45)
- (10, 3, 4): +4,807 (n=25)
- (13, 3, 5): +4,600 (n=7)
- (6, 3, 3): +4,589 (n=21)

_Generated 2026-09-10 15:20. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 390 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=390); harvest_min=1–3 (n=390); wheat_tiles=0–8 (n=390); wheat_stock=0–19 (n=390); min_hands=3–6 (n=390); load_per_hand=12–26 (n=390); geese=0–2 (n=390); open_melons=4–14 (n=390)
- **Evidence:** 390 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**99 candidates** with action_table data, **10562 total action events** extracted.

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |              — (n=0) |              — (n=0) |              — (n=0) | 0 |
| BUY_ANIMAL |           +782 (n=737) |         +1,449 (n=208) |            -56 (n=18) | 963 |
| BUY_SEED |           +822 (n=1028) |           +683 (n=292) |           +635 (n=124) | 1444 |
| BUY_LAND |           +881 (n=410) |           -231 (n=13) |              — (n=0) | 423 |
| BUY_PRODUCT |           +838 (n=1482) |           +838 (n=693) |           +842 (n=692) | 2867 |
| HIRE |           +777 (n=630) |           +555 (n=351) |           +804 (n=227) | 1208 |
| WATER_MISSED |           +784 (n=1091) |           +838 (n=693) |           +838 (n=792) | 2576 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |           +793 (n=666) |         +1,042 (n=181) |           +484 (n=234) | 1081 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |           — |           — |           — |           — |           — |           — |
| BUY_ANIMAL |           — |           — |           — |           — |           — |           — |
| BUY_SEED |           — |           — |           — |           — |           — |           — |
| BUY_LAND |           — |           — |           — |           — |           — |           — |
| BUY_PRODUCT |           — |           — |           — |           — |           — |           — |
| HIRE |           — |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |           — |           — |           — |           — |
| FEED_MISSED |           — |           — |           — |           — |           — |           — |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_ANIMAL | mid | +1,449 | 208 | 0.48 |
| 2 | FEED_MISSED | mid | +1,042 | 181 | 0.32 |
| 3 | BUY_LAND | early | +881 | 410 | 0.28 |
| 4 | BUY_PRODUCT | late | +842 | 692 | 0.27 |
| 5 | BUY_PRODUCT | early | +838 | 1482 | 0.26 |
| 6 | BUY_PRODUCT | mid | +838 | 693 | 0.26 |
| 7 | WATER_MISSED | mid | +838 | 693 | 0.26 |
| 8 | WATER_MISSED | late | +838 | 792 | 0.26 |
| 9 | BUY_SEED | early | +822 | 1028 | 0.26 |
| 10 | HIRE | late | +804 | 227 | 0.27 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_PRODUCT** in ('high', 'mid', 'high', 'mid'): +6,059 (n=3)
- **WATER_MISSED** in ('high', 'mid', 'high', 'mid'): +3,417 (n=5)
- **FEED_MISSED** in ('high', 'mid', 'high', 'mid'): +3,417 (n=5)
- **BUY_ANIMAL** in ('mid', 'mid', 'low', 'high'): -3,288 (n=3)
- **BUY_SEED** in ('mid', 'mid', 'low', 'high'): -3,288 (n=3)
- **BUY_PRODUCT** in ('mid', 'mid', 'low', 'high'): -3,288 (n=3)
- **FEED_MISSED** in ('mid', 'mid', 'low', 'high'): -3,288 (n=3)
- **BUY_SEED** in ('low', 'high', 'mid', 'high'): -3,189 (n=4)
- **BUY_LAND** in ('low', 'high', 'mid', 'high'): -3,129 (n=5)
- **BUY_PRODUCT** in ('low', 'high', 'mid', 'high'): -3,129 (n=5)
- **HIRE** in ('low', 'high', 'mid', 'high'): -3,129 (n=5)
- **HIRE** in ('low', 'low', 'high', 'high'): +2,707 (n=10)
- **BUY_SEED** in ('low', 'high', 'high', 'high'): +2,659 (n=33)
- **WATER_MISSED** in ('low', 'mid', 'mid', 'mid'): -2,239 (n=3)
- **WATER_MISSED** in ('low', 'high', 'mid', 'high'): -2,210 (n=4)

_Generated 2026-09-10 15:20. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._