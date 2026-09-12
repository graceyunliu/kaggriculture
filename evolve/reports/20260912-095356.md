# Evolution run 20260912-095356

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.01 h · candidates evaluated this run: 114 · games 30,558 (15,219/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 12 | 24 |
| dead_pattern | 7 | 14 |
| dead_smoke | 3 | 24 |
| alive | 14 | 1792 |
| held_fail | 16 | 5888 |
| held_pass | 62 | 22816 |
| error | 0 | 0 |

Population (all runs, reached dev): 1395 · held-out evaluated: 1035 · held-out PASS: 892

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | +3,605 | 3.6 | 9-1 | -13,427 | +4,376 | 7.2 | 18-2 |
| chassis + C1 params (seed row) | +0 | 0.0 | not evaluated (no-op) | -16,635 | — | — | —-— |
| C1.py (file) vs O15_SALE_PRIORITY.py | -21,945 | -16.8 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O15_SALE_PRIORITY.py | -25,061 | -10.2 | 0-10 | — | — | — | — |
| O15_SALE_PRIORITY.py own panel (dev / held) | — | — | — | -11,387 / -20,836 | — | — | — |

Measurement mode: `KAGG_FIXED_SHOPS=1` (shop unlocks policy-independent; panel margins comparable at ±$3k/opponent).

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `4dac8845ebc8` | wide | crossover | **+11,121** | 9.1 | 20-0 | -16,794 | +8,469 | melon_floor 0→150, open_melons 10→11, early_hire_days 3→1, feed_spare_poor 0→2, wheat_water_tier 0→1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPENING_MELONS 14→6, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 13 (gap +1,703 -> final +6,758); days 11-18 drivers: missed_water -25, work_turns +53, idle_turns -38, feed_hour -1.35. Hands 12 vs 14, animals 11 vs 11, plants 61 vs 6 |
| `2d7b81d266ed` | queue | mutate | **+10,873** | 6.8 | 20-0 | -16,760 | +8,364 | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, geese 0→1, wheat_cap 22→20, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.75, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, MAX_SHEEP ?, SPREAD_CAP ?, ORCH_P_WWATER ? | cand pulls ahead of C1 from day 18 (gap +2,142 -> final +7,049); days 16-23 drivers: sales_rev +6,229, missed_water -24, work_turns +112, idle_turns -28. Hands 12 vs 8, animals 12 vs 11, plants 58 vs  |
| `de988febe942` | o15 | paired | **+10,757** | 7.7 | 20-0 | -17,354 | +7,450 | harvest_min 1→3, open_melons 10→11, early_hire_days 3→5, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +3,607 -> final +3,476); days 16-23 drivers: missed_water -33, work_turns +107, sales_rev +2,925, feed_hour -1.16. Hands 11 vs 8, animals 12 vs 11, plants 52 vs |
| `7db78783cfe5` | orch | crossover | **+10,730** | 9.0 | 20-0 | -15,843 | +10,109 | harvest_min 1→2, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→35, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.5, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +3,237 -> final +4,315); days 14-21 drivers: missed_water -46, work_turns +125, idle_turns -69, sales_rev +2,699. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `e00215f1e98a` | orch | ablate:wheat_water_tier | **+10,643** | 8.1 | 20-0 | -16,717 | +8,430 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, geese 0→1, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, labor_reserve_buffer 92→35, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→26, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→13, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.0, ORCH_P_FERT 0.5→1.25, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→1.75, ORCH_SLACK_HOUR 14→13 |  | cand pulls ahead of C1 from day 18 (gap +1,926 -> final +7,053); days 16-23 drivers: missed_water -32, work_turns +130, sales_rev +4,817, idle_turns -39. Hands 12 vs 8, animals 12 vs 11, plants 55 vs  |
| `f619488bed80` | wide | paired | **+10,531** | 7.1 | 19-1 | -16,153 | +11,072 | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |  | cand pulls ahead of C1 from day 16 (gap +2,647 -> final +3,907); days 14-21 drivers: missed_water -34, work_turns +84, sales_rev +1,806, idle_turns -36. Hands 12 vs 8, animals 10 vs 11, plants 57 vs 5 |
| `1b7641b11a93` | orch | crossover | **+10,492** | 8.2 | 20-0 | -16,430 | +9,624 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 | wheat_sell_price ?, CROP_SWEEP_LEN -173, STRAW_CUTOFF ?, NEAR_RADIUS +214, OPP_GROWTH ?, ORCH_P_WEEDS -121 | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,400); days 16-23 drivers: missed_water -44, work_turns +122, sales_rev +3,509, idle_turns -44. Hands 13 vs 8, animals 12 vs 11, plants 59 vs  |
| `33d973e44a24` | o15 | paired | **+10,471** | 8.8 | 20-0 | -16,658 | +10,015 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 | min_hands +147, ORCH_P_SLACK -275 | cand pulls ahead of C1 from day 18 (gap +2,562 -> final +3,705); days 16-23 drivers: missed_water -55, work_turns +105, sales_rev +3,264, idle_turns -60. Hands 11 vs 8, animals 12 vs 11, plants 59 vs  |
| `67924b68c4e5` | orch | crossover | **+10,454** | 8.4 | 20-0 | -16,968 | +8,588 | harvest_min 1→3, geese 0→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,927 -> final +5,568); days 16-23 drivers: sales_rev +5,449, work_turns +119, missed_water -20, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `071d8fbb43d4` | orch | paired | **+10,446** | 8.8 | 20-0 | -15,854 | +9,717 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, labor_reserve_buffer 92→79, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +2,794); days 16-23 drivers: missed_water -45, work_turns +115, sales_rev +2,645, idle_turns -33. Hands 13 vs 8, animals 12 vs 11, plants 58 vs  |
| `58b3cc435646` | orch | crossover | **+10,433** | 8.5 | 20-0 | -15,890 | +9,957 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, setup_capital_share 0.25→0.1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.5, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,340); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |
| `28922b1f21f9` | orch | block_pair | **+10,421** | 8.2 | 19-1 | -16,569 | +7,901 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, geese 0→1, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, labor_reserve_buffer 92→35, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→26, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→2.25, ORCH_P_SLACK 6.0→7.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 22 (gap +3,024 -> final +5,058); days 20-27 drivers: missed_water -34, work_turns +142, sales_rev +4,355, idle_turns -17. Hands 11 vs 9, animals 12 vs 11, plants 40 vs  |
| `1df16554118d` | queue | archive_crossover:crossover_g000025_20260912-022223_1 | **+10,410** | 9.5 | 20-0 | -16,096 | +9,300 | load_per_hand 20→19, wheat_cap 22→25, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,319 -> final +8,705); days 14-21 drivers: missed_water -24, work_turns +82, sales_rev +1,959, idle_turns -32. Hands 12 vs 8, animals 9 vs 11, plants 63 vs 57 |
| `19e5809e9eb7` | orch | crossover | **+10,403** | 8.3 | 20-0 | -16,627 | +9,293 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→41, MELON_PRICE_CUSHION 100→89, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,097 -> final +4,649); days 16-23 drivers: missed_water -31, work_turns +102, idle_turns -38, sales_rev +937. Hands 12 vs 8, animals 10 vs 11, plants 57 vs 57 |
| `2fbfc0622b49` | orch | mutate | **+10,401** | 10.4 | 20-0 | -16,928 | +9,486 | melon_floor 0→150, harvest_min 1→2, min_hands 3→5, early_hire_days 3→5, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.75, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,294 -> final +9,203); days 14-21 drivers: missed_water -32, work_turns +69, idle_turns -47, feed_hour -1.6. Hands 10 vs 8, animals 9 vs 11, plants 63 vs 57. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `a421574edbc1` | queue | ablate:ORCH_P_WWATER | +11,378 | 5.7 | 10-0 | -7,389 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `97ac424f27b8` | queue | archive_crossover:crossover_g000025_20260912-102645_1 | +11,079 | 5.2 | 10-0 | -7,363 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `f619488bed80` | wide | paired | +11,072 | 5.1 | 10-0 | -6,594 | held_pass | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |
| `b2f83c7bf97d` | orch | paired | +11,033 | 6.2 | 10-0 | -6,460 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |
| `49b347e98185` | queue | mutate | +10,978 | 5.8 | 10-0 | -7,266 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `c236a276207c` | queue | archive_crossover:crossover_g000050_20260912-105831_0 | +10,910 | 5.5 | 10-0 | -7,141 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `da31de598b96` | queue | archive_crossover:crossover_g000050_20260912-084131_1 | +10,905 | 5.4 | 10-0 | -7,176 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→11 |
| `4abd19f6a514` | o15 | mutate | +10,905 | 5.1 | 10-0 | -6,092 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `3181632e71c8` | orch | ablate:CROP_SWEEP_RADIUS | +10,902 | 6.6 | 10-0 | -6,398 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |
| `b82471d91ab7` | queue | archive_crossover:crossover_g000100_20260912-053435_1 | +10,882 | 5.5 | 10-0 | -7,173 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `bfeced195cd5` | queue | crossover | +10,876 | 5.0 | 10-0 | -8,784 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WWATER 0.5→0.75, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `1dab5a8158b4` | o15 | paired | +10,859 | 6.2 | 10-0 | -6,285 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, max_animals 17→18, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |
| `39677209a26b` | queue | mutate | +10,849 | 5.2 | 10-0 | -6,758 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→48, MELON_PRICE_CUSHION 100→96, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `dbf281819c7d` | o15 | mutate | +10,811 | 4.8 | 10-0 | -6,255 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→150, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `0f97df4b5529` | orch | ablate:ORCH_SLACK_HOUR | +10,807 | 6.0 | 10-0 | -6,627 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,905 (`4abd19f6a514`), n=296
- orch: best +11,033 (`b2f83c7bf97d`), n=355
- queue: best +11,378 (`a421574edbc1`), n=416
- wide: best +11,072 (`f619488bed80`), n=306

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,843 | 123 | 92 | 69 | 1365 | 25.63 | 123: +9,616 (n=2), 79: +9,486 (n=2), 102: +9,424 (n=4), 45: +9,341 (n=5), 66: +9,132 (n=2), 69: +9,077 (n=2), 55: +8,751 (n=2), 132: +8,639 (n=2), 35: +8,421 (n=16), 118: +8,204 (n=2), 90: +7,608 (n=5), 86: +7,210 (n=4), 100: +6,901 (n=3), 110: +6,090 (n=143), 81: +5,848 (n=106), 71: +5,786 (n=2), 92: +5,359 (n=932), 111: +5,127 (n=31), 89: +5,024 (n=2), 150: +4,929 (n=16), 98: +4,736 (n=4), 105: +4,600 (n=5), 57: +4,482 (n=2), 99: +4,310 (n=13), 82: +4,186 (n=6), 119: +3,803 (n=10), 63: +3,619 (n=3), 133: +3,432 (n=3), 96: +3,017 (n=4), 54: +2,856 (n=5), 91: +2,293 (n=3), 74: +2,116 (n=2), 0: +1,824 (n=3), 141: +1,349 (n=2), 121: +313 (n=3), 65: -1,128 (n=3), 40: -1,292 (n=4), 125: -2,734 (n=4), 131: -3,228 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +12,051 | 129 | 100 | 61 | 1373 | 18.46 | 129: +8,573 (n=2), 89: +8,449 (n=3), 108: +8,353 (n=2), 115: +8,034 (n=2), 93: +7,966 (n=5), 141: +6,823 (n=86), 132: +6,738 (n=23), 124: +6,478 (n=5), 137: +6,404 (n=2), 109: +6,403 (n=61), 110: +6,325 (n=198), 86: +6,055 (n=47), 96: +6,028 (n=10), 117: +5,882 (n=2), 123: +5,795 (n=2), 99: +5,759 (n=3), 150: +5,407 (n=143), 135: +5,245 (n=4), 107: +5,141 (n=3), 140: +5,136 (n=2), 87: +5,023 (n=5), 67: +4,927 (n=4), 100: +4,923 (n=685), 104: +4,853 (n=3), 102: +4,781 (n=2), 126: +4,754 (n=4), 68: +4,532 (n=3), 94: +4,432 (n=20), 127: +4,377 (n=3), 98: +4,372 (n=2), 112: +4,340 (n=4), 105: +4,150 (n=7), 50: +4,056 (n=11), 97: +3,205 (n=3), 133: +1,390 (n=2), 147: +1,266 (n=2), 62: +519 (n=4), 82: -1,635 (n=2), 121: -3,479 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,214 | 0.6 | 0.55 | 13 | 1395 | 8.1 | 0.6: +6,340 (n=264), 0.55: +5,629 (n=977), 0.65: +5,181 (n=20), 0.5: +4,556 (n=19), 0.85: +3,951 (n=4), 0.7: +3,834 (n=8), 0.4: +2,977 (n=26), 0.75: +2,676 (n=17), 0.45: +2,166 (n=6), 0.8: +1,799 (n=26), 0.35: -313 (n=5), 0.9: -1,664 (n=10), 0.3: -4,875 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,131 | 18 | 20 | 15 | 1394 | 9.13 | 18: +6,252 (n=246), 17: +5,643 (n=16), 19: +5,463 (n=37), 20: +5,354 (n=1009), 21: +4,523 (n=37), 22: +4,423 (n=13), 16: +3,644 (n=7), 15: +3,582 (n=7), 24: +1,887 (n=3), 26: +1,168 (n=2), 14: +782 (n=7), 13: +408 (n=4), 12: -210 (n=3), 23: -4,879 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,803 | 2 | 3 | 4 | 1394 | 1.56 | 2: +6,178 (n=1189), 3: +1,009 (n=199), 4: -4,625 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,049 | 1.25 | 0.5 | 12 | 1393 | 7.31 | 1.25: +6,790 (n=19), 0.25: +6,426 (n=45), 1.0: +5,973 (n=17), 1.75: +5,542 (n=11), 0.5: +5,468 (n=1157), 0.75: +5,318 (n=13), 3.0: +4,917 (n=10), 0.0: +4,401 (n=114), 1.5: +1,070 (n=2), 2.75: -3,259 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +9,855 | 18 | 19 | 9 | 1394 | 1.67 | 18: +6,139 (n=103), 16: +6,112 (n=448), 14: +6,048 (n=15), 17: +5,385 (n=22), 20: +5,186 (n=319), 19: +4,727 (n=465), 15: +4,527 (n=20), 12: -3,716 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,236 | 4 | 0 | 21 | 1387 | 11.31 | 4: +8,585 (n=2), 2: +6,484 (n=4), 0: +5,609 (n=1313), 7: +3,312 (n=5), 5: +2,717 (n=4), 13: +2,243 (n=2), 1: +2,240 (n=8), 6: +1,924 (n=4), 10: +1,899 (n=9), 11: +1,588 (n=7), 14: +1,234 (n=7), 8: +247 (n=7), 35: -651 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +9,217 | 14 | 17 | 10 | 1395 | 7.66 | 14: +6,167 (n=3), 15: +5,682 (n=9), 13: +5,539 (n=2), 17: +5,514 (n=1208), 18: +5,277 (n=40), 16: +5,139 (n=103), 19: +2,143 (n=14), 20: +1,413 (n=8), 11: +1,062 (n=3), 10: -3,050 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +8,963 | 21 | 14 | 15 | 1395 | 8.41 | 21: +6,964 (n=2), 11: +6,497 (n=122), 13: +5,961 (n=27), 15: +5,871 (n=875), 10: +5,450 (n=13), 19: +4,948 (n=10), 16: +4,510 (n=12), 14: +4,167 (n=265), 18: +3,958 (n=5), 9: +3,937 (n=3), 12: +3,480 (n=25), 22: +2,203 (n=4), 17: +1,590 (n=3), 8: +335 (n=23), 20: -1,999 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +8,748 | 0.75 | 1.0 | 15 | 1394 | 5.63 | 0.75: +7,045 (n=10), 0.5: +6,235 (n=28), 0.25: +6,065 (n=14), 1.25: +5,768 (n=147), 1.5: +5,576 (n=660), 2.25: +5,542 (n=7), 2.0: +5,355 (n=17), 1.0: +5,081 (n=455), 1.75: +5,040 (n=21), 0.0: +4,178 (n=19), 3.0: +3,973 (n=2), 2.5: +2,727 (n=6), 3.5: +298 (n=6), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +8,445 | 34 | 38 | 27 | 1393 | 9.23 | 34: +7,874 (n=2), 48: +7,790 (n=7), 37: +7,486 (n=11), 50: +7,094 (n=129), 24: +6,542 (n=3), 47: +6,385 (n=12), 35: +6,105 (n=570), 22: +6,104 (n=2), 20: +5,956 (n=3), 26: +5,879 (n=42), 41: +5,690 (n=56), 29: +5,537 (n=3), 27: +5,381 (n=8), 42: +5,328 (n=5), 44: +5,076 (n=3), 32: +4,800 (n=13), 43: +4,778 (n=3), 31: +4,610 (n=15), 38: +4,570 (n=415), 28: +4,378 (n=7), 39: +4,235 (n=6), 40: +3,434 (n=4), 33: +2,431 (n=4), 30: +630 (n=67), 36: -571 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +8,180 | 0.75 | 1.25 | 5 | 1395 | 3.45 | 0.75: +5,741 (n=8), 1.25: +5,487 (n=1242), 1.5: +5,454 (n=96), 1.0: +3,154 (n=44), 0.5: -2,439 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +8,121 | 0.3 | 0.0 | 9 | 1393 | 5.63 | 0.3: +5,980 (n=9), 0.0: +5,540 (n=1319), 0.4: +3,653 (n=6), 0.1: +2,988 (n=33), 0.2: +2,460 (n=15), 0.6: +2,212 (n=4), 0.7: -2,140 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +8,028 | 1.25 | 1.5 | 21 | 1393 | 9.8 | 1.25: +7,105 (n=8), 2.25: +6,964 (n=9), 3.5: +6,532 (n=399), 2.5: +6,353 (n=21), 1.0: +6,034 (n=10), 3.0: +5,898 (n=42), 4.0: +5,616 (n=2), 1.75: +5,562 (n=14), 4.75: +5,352 (n=6), 0.25: +5,272 (n=3), 2.0: +5,216 (n=8), 0.5: +5,016 (n=15), 4.5: +5,009 (n=4), 1.5: +4,920 (n=792), 3.25: +4,836 (n=6), 0.75: +4,539 (n=8), 0.0: +3,629 (n=20), 2.75: +1,930 (n=17), 5.0: -923 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +8,022 | frontier | frontier | 2 | 1395 | 0.85 | frontier: +6,005 (n=1287), v312: -2,017 (n=108) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,327 | 28 | 30 | 20 | 1390 | 9.38 | 28: +6,685 (n=155), 26: +6,676 (n=4), 29: +6,198 (n=8), 25: +6,174 (n=156), 30: +5,242 (n=962), 27: +5,032 (n=38), 36: +4,931 (n=4), 34: +4,721 (n=20), 37: +3,940 (n=8), 33: +2,905 (n=4), 32: +2,402 (n=5), 35: +1,917 (n=8), 45: +241 (n=2), 31: -84 (n=10), 39: -642 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +7,267 | 2 | 2 | 4 | 1395 | 2.72 | 2: +5,750 (n=1299), 3: +1,457 (n=5), 1: +545 (n=84), 0: -1,517 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +7,255 | 5 | 10 | 11 | 1394 | 7.14 | 5: +6,463 (n=2), 9: +5,764 (n=147), 8: +5,621 (n=18), 10: +5,551 (n=1135), 12: +4,761 (n=15), 11: +2,919 (n=44), 6: +2,804 (n=6), 7: +2,693 (n=15), 13: +6 (n=8), 4: -792 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +7,187 | 2.5 | 0.5 | 11 | 1394 | 4.75 | 2.5: +7,591 (n=3), 0.25: +6,764 (n=267), 0.0: +5,718 (n=170), 1.0: +5,533 (n=91), 0.5: +5,117 (n=802), 1.5: +3,339 (n=10), 1.25: +3,041 (n=6), 2.0: +2,812 (n=4), 1.75: +947 (n=27), 0.75: +404 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +11,378 (n=177)
- (10, 3, 4): +11,072 (n=53)
- (9, 3, 4): +11,033 (n=260)
- (10, 3, 5): +10,905 (n=217)
- (11, 3, 5): +10,683 (n=190)
- (10, 3, 6): +10,400 (n=30)
- (11, 3, 6): +10,254 (n=133)
- (12, 3, 6): +10,109 (n=110)
- (9, 3, 6): +9,706 (n=13)
- (12, 3, 5): +9,662 (n=83)
- (13, 3, 5): +8,853 (n=5)
- (11, 3, 4): +8,841 (n=10)
- (13, 3, 6): +8,762 (n=18)
- (14, 3, 6): +7,609 (n=17)
- (8, 3, 5): +6,544 (n=7)

_Generated 2026-09-12 11:54. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 346 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=346); harvest_min=1–3 (n=346); wheat_tiles=0–7 (n=346); wheat_stock=0–40 (n=346); min_hands=3–6 (n=346); load_per_hand=12–26 (n=346); geese=0–2 (n=346); open_melons=6–14 (n=346)
- **Evidence:** 346 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1395 candidates** with action_table data, **182989 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,436 (n=19256) |         +5,384 (n=9765) |         +5,384 (n=11160) | 40181 |
| BUY_ANIMAL |         +4,829 (n=7675) |         +5,691 (n=1684) |              — (n=0) | 9359 |
| BUY_SEED |         +5,424 (n=14238) |         +5,463 (n=5327) |         +4,963 (n=1910) | 21475 |
| BUY_LAND |         +5,427 (n=4981) |         +5,895 (n=1338) |              — (n=0) | 6319 |
| BUY_PRODUCT |         +5,384 (n=20914) |         +5,384 (n=9765) |         +5,384 (n=9762) | 40441 |
| HIRE |         +5,219 (n=8267) |         +5,228 (n=4829) |         +5,553 (n=3648) | 16744 |
| WATER_MISSED |         +5,384 (n=15561) |         +5,384 (n=9765) |         +5,385 (n=11153) | 36479 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +5,065 (n=7167) |         +5,087 (n=1850) |         +4,997 (n=2974) | 11991 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,517 |      +5,384 |      +5,432 |      +5,340 |      +5,332 |      +5,383 |
| BUY_ANIMAL |      +4,725 |           — |      +1,809 |      +5,752 |      +5,509 |      +4,929 |
| BUY_SEED |      +4,782 |      +6,166 |      -3,489 |      -4,523 |      +3,028 |      +5,479 |
| BUY_LAND |      -2,439 |      -3,874 |      +5,453 |        -438 |      +6,199 |      +5,433 |
| BUY_PRODUCT |      +5,384 |           — |           — |           — |           — |           — |
| HIRE |      +5,294 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,384 |      +2,653 |      +5,384 |      +5,417 |
| FEED_MISSED |           — |      +5,402 |      +2,968 |           — |      +1,809 |      +5,028 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +5,895 | 1338 | 1.45 |
| 2 | BUY_ANIMAL | mid | +5,691 | 1684 | 1.35 |
| 3 | HIRE | late | +5,553 | 3648 | 1.3 |
| 4 | BUY_SEED | mid | +5,463 | 5327 | 1.25 |
| 5 | SELL | early | +5,436 | 19256 | 1.26 |
| 6 | BUY_LAND | early | +5,427 | 4981 | 1.24 |
| 7 | BUY_SEED | early | +5,424 | 14238 | 1.26 |
| 8 | WATER_MISSED | late | +5,385 | 11153 | 1.24 |
| 9 | SELL | mid | +5,384 | 9765 | 1.24 |
| 10 | SELL | late | +5,384 | 11160 | 1.24 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,506 (n=676)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,506 (n=676)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,901 (n=916)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,895 (n=912)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,870 (n=935)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,821 (n=939)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,801 (n=945)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +6,347 (n=1133)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +6,229 (n=1517)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,164 (n=79)
- **SELL** in ('low', 'low', 'high', 'high'): +6,044 (n=1179)
- **BUY_PRODUCT** in ('low', 'low', 'high', 'high'): +6,044 (n=1179)
- **WATER_MISSED** in ('low', 'low', 'high', 'high'): +6,044 (n=1179)
- **SELL** in ('mid', 'low', 'high', 'mid'): +5,952 (n=1009)
- **WATER_MISSED** in ('mid', 'low', 'high', 'mid'): +5,952 (n=1005)

_Generated 2026-09-12 11:54. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._