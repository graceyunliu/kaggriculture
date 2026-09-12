# Evolution run 20260912-075002

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.05 h · candidates evaluated this run: 121 · games 31,562 (15,408/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 12 | 24 |
| dead_pattern | 9 | 18 |
| dead_smoke | 0 | 0 |
| alive | 22 | 2816 |
| held_fail | 13 | 4784 |
| held_pass | 65 | 23920 |
| error | 0 | 0 |

Population (all runs, reached dev): 1303 · held-out evaluated: 957 · held-out PASS: 830

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
| `1b7641b11a93` | orch | crossover | **+10,492** | 8.2 | 20-0 | -16,430 | +9,624 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 | wheat_sell_price ?, CROP_SWEEP_LEN -173, STRAW_CUTOFF ?, NEAR_RADIUS +214, OPP_GROWTH ?, ORCH_P_WEEDS -121 | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,400); days 16-23 drivers: missed_water -44, work_turns +122, sales_rev +3,509, idle_turns -44. Hands 13 vs 8, animals 12 vs 11, plants 59 vs  |
| `33d973e44a24` | o15 | paired | **+10,471** | 8.8 | 20-0 | -16,658 | +10,015 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 | min_hands +147, ORCH_P_SLACK -275 | cand pulls ahead of C1 from day 18 (gap +2,562 -> final +3,705); days 16-23 drivers: missed_water -55, work_turns +105, sales_rev +3,264, idle_turns -60. Hands 11 vs 8, animals 12 vs 11, plants 59 vs  |
| `67924b68c4e5` | orch | crossover | **+10,454** | 8.4 | 20-0 | -16,968 | +8,588 | harvest_min 1→3, geese 0→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,927 -> final +5,568); days 16-23 drivers: sales_rev +5,449, work_turns +119, missed_water -20, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `071d8fbb43d4` | orch | paired | **+10,446** | 8.8 | 20-0 | -15,854 | +9,717 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, labor_reserve_buffer 92→79, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +2,794); days 16-23 drivers: missed_water -45, work_turns +115, sales_rev +2,645, idle_turns -33. Hands 13 vs 8, animals 12 vs 11, plants 58 vs  |
| `58b3cc435646` | orch | crossover | **+10,433** | 8.5 | 20-0 | -15,890 | +9,957 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, setup_capital_share 0.25→0.1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.5, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,340); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |
| `1df16554118d` | queue | archive_crossover:crossover_g000025_20260912-022223_1 | **+10,410** | 9.5 | 20-0 | -16,096 | +9,300 | load_per_hand 20→19, wheat_cap 22→25, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,319 -> final +8,705); days 14-21 drivers: missed_water -24, work_turns +82, sales_rev +1,959, idle_turns -32. Hands 12 vs 8, animals 9 vs 11, plants 63 vs 57 |
| `19e5809e9eb7` | orch | crossover | **+10,403** | 8.3 | 20-0 | -16,627 | +9,293 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→41, MELON_PRICE_CUSHION 100→89, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,097 -> final +4,649); days 16-23 drivers: missed_water -31, work_turns +102, idle_turns -38, sales_rev +937. Hands 12 vs 8, animals 10 vs 11, plants 57 vs 57 |
| `2fbfc0622b49` | orch | mutate | **+10,401** | 10.4 | 20-0 | -16,928 | +9,486 | melon_floor 0→150, harvest_min 1→2, min_hands 3→5, early_hire_days 3→5, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.75, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,294 -> final +9,203); days 14-21 drivers: missed_water -32, work_turns +69, idle_turns -47, feed_hour -1.6. Hands 10 vs 8, animals 9 vs 11, plants 63 vs 57. |
| `69f9eaac2d61` | orch | ablate:ORCH_P_WEEDS | **+10,383** | 7.5 | 20-0 | -16,425 | +9,745 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,404); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |
| `0b037ebcf3fa` | queue | crossover | **+10,260** | 9.1 | 20-0 | -16,918 | +9,033 | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 19 (gap +1,809 -> final +4,428); days 17-24 drivers: missed_water -44, work_turns +114, idle_turns -35, sales_rev +999. Hands 13 vs 14, animals 11 vs 11, plants 60 vs 5 |
| `c6c0f103ec5a` | orch | ablate:ORCH_P_WEEDS | **+10,251** | 9.5 | 20-0 | -16,989 | +9,377 | melon_floor 0→150, harvest_min 1→3, min_hands 3→5, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→35, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→26, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 20 (gap +1,763 -> final +4,485); days 18-25 drivers: missed_water -38, sales_rev +5,593, work_turns +127, feed_hour -1.82. Hands 12 vs 11, animals 11 vs 11, plants 60 v |
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `a421574edbc1` | queue | ablate:ORCH_P_WWATER | +11,378 | 5.7 | 10-0 | -7,389 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `b2f83c7bf97d` | orch | paired | +11,033 | 6.2 | 10-0 | -6,460 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |
| `49b347e98185` | queue | mutate | +10,978 | 5.8 | 10-0 | -7,266 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `da31de598b96` | queue | archive_crossover:crossover_g000050_20260912-084131_1 | +10,905 | 5.4 | 10-0 | -7,176 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→11 |
| `4abd19f6a514` | o15 | mutate | +10,905 | 5.1 | 10-0 | -6,092 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `3181632e71c8` | orch | ablate:CROP_SWEEP_RADIUS | +10,902 | 6.6 | 10-0 | -6,398 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |
| `b82471d91ab7` | queue | archive_crossover:crossover_g000100_20260912-053435_1 | +10,882 | 5.5 | 10-0 | -7,173 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `bfeced195cd5` | queue | crossover | +10,876 | 5.0 | 10-0 | -8,784 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WWATER 0.5→0.75, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `1dab5a8158b4` | o15 | paired | +10,859 | 6.2 | 10-0 | -6,285 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, max_animals 17→18, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |
| `39677209a26b` | queue | mutate | +10,849 | 5.2 | 10-0 | -6,758 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→48, MELON_PRICE_CUSHION 100→96, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `dbf281819c7d` | o15 | mutate | +10,811 | 4.8 | 10-0 | -6,255 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→150, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `0f97df4b5529` | orch | ablate:ORCH_SLACK_HOUR | +10,807 | 6.0 | 10-0 | -6,627 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→15 |
| `c262b6590f29` | queue | archive_crossover:crossover_g000075_20260912-005550_1 | +10,794 | 4.6 | 10-0 | -8,416 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `71da6d96308f` | queue | archive_crossover:crossover_g000050_20260912-084131_0 | +10,793 | 5.4 | 10-0 | -6,743 | held_pass | melon_floor 0→150, harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→11 |
| `99d5e088e880` | queue | archive_crossover:crossover_g000100_20260912-094223_0 | +10,698 | 5.6 | 10-0 | -6,462 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_SLACK_HOUR 14→11 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,905 (`4abd19f6a514`), n=278
- orch: best +11,033 (`b2f83c7bf97d`), n=332
- queue: best +11,378 (`a421574edbc1`), n=391
- wide: best +10,476 (`e31fc28b0264`), n=280

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,448 | 123 | 92 | 68 | 1272 | 24.77 | 123: +9,616 (n=2), 79: +9,486 (n=2), 102: +9,424 (n=4), 45: +9,274 (n=4), 66: +9,132 (n=2), 69: +9,077 (n=2), 132: +8,639 (n=2), 35: +8,244 (n=9), 118: +8,204 (n=2), 90: +7,608 (n=5), 86: +7,210 (n=4), 100: +6,901 (n=3), 110: +6,173 (n=124), 81: +5,736 (n=96), 92: +5,261 (n=886), 111: +5,127 (n=31), 89: +5,024 (n=2), 150: +4,687 (n=12), 105: +4,600 (n=5), 57: +4,482 (n=2), 99: +4,310 (n=13), 82: +4,186 (n=6), 119: +3,803 (n=10), 63: +3,619 (n=3), 133: +3,432 (n=3), 98: +3,050 (n=3), 96: +3,017 (n=4), 54: +2,856 (n=5), 91: +2,293 (n=3), 74: +2,116 (n=2), 0: +1,824 (n=3), 141: +1,349 (n=2), 121: +313 (n=3), 65: -1,128 (n=3), 40: -1,292 (n=4), 125: -2,734 (n=4), 131: -2,832 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +12,051 | 129 | 100 | 58 | 1282 | 17.79 | 129: +8,573 (n=2), 89: +8,449 (n=3), 108: +8,353 (n=2), 115: +8,034 (n=2), 93: +8,014 (n=2), 107: +7,383 (n=2), 141: +6,833 (n=70), 132: +6,629 (n=22), 124: +6,478 (n=5), 137: +6,404 (n=2), 109: +6,388 (n=60), 110: +6,332 (n=183), 86: +6,055 (n=47), 117: +5,882 (n=2), 123: +5,795 (n=2), 99: +5,759 (n=3), 150: +5,441 (n=133), 135: +5,245 (n=4), 96: +5,107 (n=7), 87: +5,023 (n=5), 67: +4,927 (n=4), 104: +4,853 (n=3), 100: +4,800 (n=651), 102: +4,781 (n=2), 68: +4,532 (n=3), 127: +4,377 (n=3), 98: +4,372 (n=2), 94: +4,250 (n=19), 105: +4,150 (n=7), 50: +4,056 (n=11), 97: +3,205 (n=3), 112: +3,142 (n=3), 126: +3,135 (n=3), 133: +1,390 (n=2), 62: +519 (n=4), 82: -1,635 (n=2), 121: -3,479 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,282 | 0.6 | 0.55 | 13 | 1303 | 8.19 | 0.6: +6,408 (n=234), 0.55: +5,515 (n=921), 0.65: +5,181 (n=20), 0.5: +4,562 (n=17), 0.85: +3,951 (n=4), 0.7: +3,834 (n=8), 0.4: +3,021 (n=25), 0.75: +2,558 (n=16), 0.8: +1,799 (n=26), 0.45: +296 (n=4), 0.35: -313 (n=5), 0.9: -1,664 (n=10), 0.3: -4,875 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,082 | 18 | 20 | 15 | 1302 | 9.14 | 18: +6,203 (n=231), 19: +5,934 (n=33), 17: +5,384 (n=14), 20: +5,227 (n=943), 22: +4,985 (n=12), 21: +4,430 (n=36), 16: +3,369 (n=6), 15: +3,053 (n=6), 24: +1,887 (n=3), 26: +1,168 (n=2), 13: +408 (n=4), 14: +138 (n=6), 12: -210 (n=3), 23: -4,879 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,012 | 2 | 3 | 4 | 1302 | 1.53 | 2: +6,121 (n=1098), 3: +1,009 (n=199), 4: -4,891 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +10,126 | 18 | 19 | 9 | 1302 | 1.72 | 18: +6,410 (n=89), 14: +6,048 (n=15), 16: +6,045 (n=421), 17: +5,385 (n=22), 20: +5,097 (n=293), 19: +4,549 (n=443), 15: +3,926 (n=17), 12: -3,716 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +9,498 | 0.25 | 0.5 | 12 | 1300 | 6.52 | 0.25: +6,240 (n=42), 1.25: +6,210 (n=16), 1.75: +6,208 (n=10), 0.5: +5,388 (n=1086), 0.75: +5,318 (n=13), 3.0: +4,917 (n=10), 1.0: +4,497 (n=10), 0.0: +4,382 (n=108), 2.75: -3,259 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,236 | 4 | 0 | 20 | 1296 | 11.28 | 4: +8,585 (n=2), 2: +6,484 (n=4), 0: +5,516 (n=1224), 7: +3,312 (n=5), 1: +3,030 (n=7), 5: +2,717 (n=4), 13: +2,243 (n=2), 6: +1,924 (n=4), 10: +1,899 (n=9), 11: +1,588 (n=7), 14: +1,234 (n=7), 8: -473 (n=6), 35: -651 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +9,217 | 14 | 17 | 10 | 1303 | 7.72 | 14: +6,167 (n=3), 15: +5,563 (n=7), 13: +5,539 (n=2), 18: +5,461 (n=38), 17: +5,406 (n=1136), 16: +5,092 (n=87), 19: +2,143 (n=14), 20: +1,413 (n=8), 11: +1,062 (n=3), 10: -3,050 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +8,963 | 21 | 14 | 15 | 1303 | 8.39 | 21: +6,964 (n=2), 11: +6,535 (n=113), 15: +5,813 (n=816), 13: +5,531 (n=23), 10: +5,450 (n=13), 19: +4,982 (n=9), 16: +4,074 (n=11), 14: +3,975 (n=249), 18: +3,958 (n=5), 9: +3,937 (n=3), 12: +3,270 (n=24), 22: +2,203 (n=4), 17: +1,590 (n=3), 8: +181 (n=22), 20: -1,999 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +8,445 | 34 | 38 | 26 | 1302 | 9.18 | 34: +7,874 (n=2), 50: +7,019 (n=108), 37: +6,961 (n=9), 48: +6,912 (n=5), 24: +6,542 (n=3), 35: +6,140 (n=530), 22: +6,104 (n=2), 47: +6,070 (n=11), 20: +5,956 (n=3), 41: +5,658 (n=55), 29: +5,537 (n=3), 26: +5,458 (n=36), 42: +5,328 (n=5), 44: +5,076 (n=3), 27: +4,933 (n=7), 32: +4,800 (n=13), 43: +4,778 (n=3), 31: +4,610 (n=15), 38: +4,480 (n=399), 28: +4,378 (n=7), 39: +4,235 (n=6), 40: +3,434 (n=4), 33: +2,431 (n=4), 30: +570 (n=66), 36: -571 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +8,121 | 0.3 | 0.0 | 9 | 1301 | 5.62 | 0.3: +5,980 (n=9), 0.0: +5,444 (n=1230), 0.4: +3,653 (n=6), 0.1: +2,988 (n=33), 0.6: +2,212 (n=4), 0.2: +2,207 (n=12), 0.7: -2,140 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +8,028 | 1.25 | 1.5 | 21 | 1301 | 9.85 | 1.25: +7,105 (n=8), 2.5: +6,984 (n=20), 2.25: +6,590 (n=7), 3.5: +6,494 (n=372), 3.0: +5,859 (n=41), 1.0: +5,671 (n=9), 4.0: +5,616 (n=2), 0.5: +5,610 (n=14), 0.75: +5,520 (n=7), 0.25: +5,272 (n=3), 4.5: +5,009 (n=4), 1.5: +4,788 (n=743), 4.75: +4,720 (n=5), 2.0: +4,505 (n=7), 3.25: +4,257 (n=5), 1.75: +4,014 (n=9), 0.0: +3,624 (n=19), 2.75: +1,930 (n=17), 5.0: -923 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +8,003 | frontier | frontier | 2 | 1303 | 0.85 | frontier: +5,901 (n=1203), v312: -2,101 (n=100) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +7,844 | 1.25 | 1.25 | 5 | 1303 | 3.45 | 1.25: +5,405 (n=1160), 1.5: +5,240 (n=89), 0.75: +5,238 (n=6), 1.0: +3,104 (n=43), 0.5: -2,439 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +7,843 | 0.5 | 1.0 | 15 | 1302 | 5.81 | 0.5: +6,141 (n=26), 0.25: +6,065 (n=14), 1.25: +5,756 (n=127), 1.5: +5,542 (n=633), 2.25: +5,542 (n=7), 0.75: +5,405 (n=6), 2.0: +5,355 (n=17), 1.75: +5,040 (n=21), 1.0: +4,884 (n=417), 0.0: +4,151 (n=18), 3.0: +3,973 (n=2), 2.5: +2,727 (n=6), 3.5: +298 (n=6), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +7,526 | 5 | 10 | 11 | 1302 | 7.12 | 5: +6,463 (n=2), 8: +5,908 (n=17), 9: +5,759 (n=136), 10: +5,437 (n=1057), 12: +4,842 (n=14), 11: +2,919 (n=44), 6: +2,804 (n=6), 7: +2,693 (n=15), 13: +6 (n=8), 4: -1,063 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,351 | 28 | 30 | 20 | 1298 | 9.49 | 28: +6,709 (n=130), 26: +6,676 (n=4), 29: +6,198 (n=8), 25: +6,024 (n=144), 30: +5,163 (n=908), 27: +5,032 (n=38), 36: +4,931 (n=4), 34: +4,562 (n=19), 37: +3,940 (n=8), 33: +2,905 (n=4), 32: +2,402 (n=5), 35: +1,917 (n=8), 45: +241 (n=2), 31: -84 (n=10), 39: -642 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +7,182 | 2 | 2 | 4 | 1303 | 2.71 | 2: +5,664 (n=1210), 3: +1,439 (n=4), 1: +490 (n=82), 0: -1,517 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,047 | 9 | 14 | 11 | 1301 | 5.75 | 9: +6,608 (n=99), 10: +6,598 (n=121), 12: +5,426 (n=13), 14: +5,161 (n=976), 7: +4,826 (n=4), 13: +4,741 (n=58), 11: +1,727 (n=22), 6: +528 (n=2), 8: -439 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +11,378 (n=166)
- (9, 3, 4): +11,033 (n=246)
- (10, 3, 5): +10,905 (n=203)
- (11, 3, 5): +10,683 (n=180)
- (10, 3, 4): +10,309 (n=49)
- (11, 3, 6): +10,254 (n=125)
- (10, 3, 6): +10,183 (n=25)
- (12, 3, 6): +10,084 (n=100)
- (9, 3, 6): +9,706 (n=13)
- (12, 3, 5): +9,662 (n=71)
- (13, 3, 5): +8,853 (n=5)
- (11, 3, 4): +8,841 (n=10)
- (13, 3, 6): +8,762 (n=18)
- (14, 3, 6): +7,609 (n=16)
- (8, 3, 5): +6,544 (n=6)

_Generated 2026-09-12 09:53. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 320 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=320); harvest_min=1–3 (n=320); wheat_tiles=0–7 (n=320); wheat_stock=0–40 (n=320); min_hands=3–6 (n=320); load_per_hand=12–26 (n=320); geese=0–2 (n=320); open_melons=6–14 (n=320)
- **Evidence:** 320 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1303 candidates** with action_table data, **170959 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,339 (n=17985) |         +5,287 (n=9121) |         +5,287 (n=10424) | 37530 |
| BUY_ANIMAL |         +4,726 (n=7172) |         +5,604 (n=1573) |              — (n=0) | 8745 |
| BUY_SEED |         +5,325 (n=13305) |         +5,377 (n=4987) |         +4,847 (n=1785) | 20077 |
| BUY_LAND |         +5,316 (n=4644) |         +5,804 (n=1252) |              — (n=0) | 5896 |
| BUY_PRODUCT |         +5,286 (n=19535) |         +5,287 (n=9121) |         +5,287 (n=9118) | 37774 |
| HIRE |         +5,119 (n=7734) |         +5,123 (n=4508) |         +5,450 (n=3406) | 15648 |
| WATER_MISSED |         +5,285 (n=14545) |         +5,287 (n=9121) |         +5,288 (n=10417) | 34083 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,960 (n=6684) |         +4,986 (n=1734) |         +4,883 (n=2788) | 11206 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,420 |      +5,287 |      +5,339 |      +5,257 |      +5,234 |      +5,284 |
| BUY_ANIMAL |      +4,632 |           — |      +1,809 |      +5,544 |      +5,419 |      +4,826 |
| BUY_SEED |      +4,695 |      +6,059 |      -3,489 |      -4,523 |      +2,984 |      +5,381 |
| BUY_LAND |      -2,439 |      -3,874 |      +5,360 |        -592 |      +6,090 |      +5,326 |
| BUY_PRODUCT |      +5,287 |           — |           — |           — |           — |           — |
| HIRE |      +5,192 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,287 |      +2,614 |      +5,287 |      +5,318 |
| FEED_MISSED |           — |      +5,305 |      +2,921 |           — |      +1,809 |      +4,921 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +5,804 | 1252 | 1.42 |
| 2 | BUY_ANIMAL | mid | +5,604 | 1573 | 1.33 |
| 3 | HIRE | late | +5,450 | 3406 | 1.27 |
| 4 | BUY_SEED | mid | +5,377 | 4987 | 1.23 |
| 5 | SELL | early | +5,339 | 17985 | 1.23 |
| 6 | BUY_SEED | early | +5,325 | 13305 | 1.23 |
| 7 | BUY_LAND | early | +5,316 | 4644 | 1.21 |
| 8 | WATER_MISSED | late | +5,288 | 10417 | 1.21 |
| 9 | SELL | mid | +5,287 | 9121 | 1.21 |
| 10 | SELL | late | +5,287 | 10424 | 1.21 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,453 (n=619)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,453 (n=619)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,797 (n=847)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,791 (n=843)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,767 (n=866)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,715 (n=870)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,693 (n=876)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +6,248 (n=1056)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,172 (n=76)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +6,099 (n=1393)
- **SELL** in ('low', 'low', 'high', 'high'): +5,948 (n=1099)
- **BUY_PRODUCT** in ('low', 'low', 'high', 'high'): +5,948 (n=1099)
- **WATER_MISSED** in ('low', 'low', 'high', 'high'): +5,948 (n=1099)
- **WATER_MISSED** in ('mid', 'low', 'high', 'mid'): +5,850 (n=934)
- **SELL** in ('mid', 'low', 'high', 'mid'): +5,849 (n=938)

_Generated 2026-09-12 09:53. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._