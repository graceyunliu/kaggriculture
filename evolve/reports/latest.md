# Evolution run 20260912-034716

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.01 h · candidates evaluated this run: 135 · games 32,106 (15,973/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 17 | 34 |
| dead_pattern | 12 | 24 |
| dead_smoke | 2 | 16 |
| alive | 26 | 3328 |
| held_fail | 14 | 5152 |
| held_pass | 64 | 23552 |
| error | 0 | 0 |

Population (all runs, reached dev): 1113 · held-out evaluated: 801 · held-out PASS: 701

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
| `4abd19f6a514` | o15 | mutate | +10,905 | 5.1 | 10-0 | -6,092 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `b82471d91ab7` | queue | archive_crossover:crossover_g000100_20260912-053435_1 | +10,882 | 5.5 | 10-0 | -7,173 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `dbf281819c7d` | o15 | mutate | +10,811 | 4.8 | 10-0 | -6,255 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→150, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `c262b6590f29` | queue | archive_crossover:crossover_g000075_20260912-005550_1 | +10,794 | 4.6 | 10-0 | -8,416 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `207974341d4d` | queue | archive_crossover:crossover_g000075_20260912-051050_1 | +10,683 | 4.9 | 10-0 | -6,168 | held_pass | melon_floor 0→150, harvest_min 1→3, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_SLACK 6.0→7.0, ORCH_SLACK_HOUR 14→15 |
| `31b8c13ba6a7` | queue | archive_crossover:crossover_g000075_20260912-032444_0 | +10,616 | 4.5 | 10-0 | -8,683 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `bde07613a6ba` | queue | archive_crossover:crossover_g000025_20260912-042518_0 | +10,584 | 6.0 | 10-0 | -6,823 | held_pass | melon_floor 0→150, min_hands 3→4, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `d40162bbeaa3` | orch | crossover | +10,545 | 6.0 | 10-0 | -6,551 | held_pass | melon_floor 0→150, harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→15 |
| `9cb98ae7bdd0` | queue | archive_crossover:crossover_g000050_20260912-003221_1 | +10,530 | 5.7 | 10-0 | -7,179 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→18, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WWATER 0.5→0.25, ORCH_P_PLANT 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `c1bd9a294f54` | queue | ablate:ORCH_P_WATER | +10,528 | 6.7 | 10-0 | -6,356 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `e31fc28b0264` | wide | paired | +10,476 | 4.9 | 10-0 | -8,354 | held_fail | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, MAX_SHEEP 14→9, OPENING_MELONS 14→6, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `474847e21687` | queue | archive_crossover:crossover_g000075_20260912-051050_0 | +10,419 | 6.0 | 10-0 | -6,698 | held_pass | melon_floor 0→150, harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `f25e784d65ee` | queue | mutate | +10,406 | 5.5 | 10-0 | -6,883 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `508ceae58587` | orch | ablate:ORCH_COMMIT | +10,405 | 6.4 | 10-0 | -6,287 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,905 (`4abd19f6a514`), n=233
- orch: best +10,545 (`d40162bbeaa3`), n=292
- queue: best +11,378 (`a421574edbc1`), n=325
- wide: best +10,476 (`e31fc28b0264`), n=241

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,606 | 123 | 92 | 60 | 1080 | 18.43 | 123: +9,616 (n=2), 79: +9,486 (n=2), 102: +9,151 (n=3), 66: +9,132 (n=2), 90: +9,060 (n=2), 132: +8,639 (n=2), 35: +8,205 (n=7), 86: +7,210 (n=4), 110: +6,095 (n=96), 81: +5,433 (n=84), 111: +5,074 (n=29), 89: +5,024 (n=2), 92: +4,995 (n=777), 99: +4,310 (n=13), 82: +4,186 (n=6), 119: +3,803 (n=10), 150: +3,779 (n=9), 63: +3,619 (n=3), 133: +3,432 (n=3), 96: +3,017 (n=4), 54: +2,856 (n=5), 0: +1,824 (n=3), 105: +1,576 (n=2), 91: +1,573 (n=2), 121: -1,255 (n=2), 125: -2,734 (n=4), 65: -2,990 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,928 | 89 | 100 | 55 | 1088 | 15.19 | 89: +8,449 (n=3), 108: +8,353 (n=2), 93: +8,014 (n=2), 124: +6,478 (n=5), 137: +6,404 (n=2), 132: +6,378 (n=19), 110: +6,328 (n=158), 109: +6,303 (n=57), 141: +6,004 (n=24), 86: +5,930 (n=42), 117: +5,882 (n=2), 99: +5,759 (n=3), 135: +5,245 (n=4), 150: +5,209 (n=111), 87: +5,023 (n=5), 67: +4,927 (n=4), 104: +4,853 (n=3), 102: +4,781 (n=2), 100: +4,572 (n=587), 68: +4,532 (n=3), 127: +4,377 (n=3), 105: +4,150 (n=7), 50: +3,696 (n=10), 112: +3,142 (n=3), 126: +3,135 (n=3), 94: +2,970 (n=14), 97: +1,571 (n=2), 62: +519 (n=4), 82: -1,635 (n=2), 121: -3,479 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,223 | 0.6 | 0.55 | 13 | 1113 | 8.31 | 0.6: +6,348 (n=188), 0.55: +5,211 (n=797), 0.65: +4,814 (n=18), 0.5: +4,804 (n=12), 0.85: +3,951 (n=4), 0.4: +3,285 (n=20), 0.7: +2,524 (n=6), 0.75: +2,055 (n=14), 0.8: +1,788 (n=25), 0.45: +296 (n=4), 0.35: -593 (n=4), 0.9: -1,906 (n=8), 0.3: -4,875 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,970 | 17 | 20 | 14 | 1113 | 9.11 | 17: +6,091 (n=13), 18: +5,963 (n=197), 19: +5,549 (n=29), 20: +4,935 (n=804), 22: +4,602 (n=10), 21: +3,996 (n=33), 16: +3,369 (n=6), 15: +2,678 (n=4), 24: +1,532 (n=2), 26: +1,168 (n=2), 13: +284 (n=3), 14: +39 (n=5), 12: -1,224 (n=2), 23: -4,879 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,752 | 2 | 3 | 4 | 1112 | 1.47 | 2: +5,920 (n=915), 3: +963 (n=194), 4: -4,832 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,354 | 1.25 | 0.5 | 12 | 1110 | 6.52 | 1.25: +7,095 (n=14), 0.25: +6,960 (n=30), 1.75: +6,043 (n=9), 0.5: +5,066 (n=927), 3.0: +4,399 (n=9), 0.0: +4,387 (n=98), 0.75: +4,385 (n=9), 1.0: +3,984 (n=9), 2.75: -3,259 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +9,909 | 18 | 19 | 9 | 1112 | 1.95 | 18: +6,193 (n=63), 14: +6,048 (n=15), 16: +5,953 (n=370), 17: +5,211 (n=20), 19: +4,441 (n=410), 20: +4,264 (n=215), 15: +3,926 (n=17), 12: -3,716 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +9,509 | 2.25 | 1.5 | 21 | 1111 | 10.05 | 2.25: +8,585 (n=3), 1.25: +7,749 (n=7), 2.5: +6,850 (n=16), 3.5: +6,332 (n=305), 3.0: +6,004 (n=39), 1.0: +5,671 (n=9), 4.0: +5,616 (n=2), 0.25: +5,272 (n=3), 4.5: +5,009 (n=4), 1.5: +4,458 (n=646), 0.5: +4,457 (n=10), 0.75: +4,441 (n=4), 3.25: +4,405 (n=4), 1.75: +4,014 (n=9), 2.0: +4,004 (n=6), 4.75: +3,994 (n=3), 0.0: +3,841 (n=17), 2.75: +1,865 (n=15), 5.0: -923 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,229 | 4 | 0 | 20 | 1106 | 11.18 | 4: +8,585 (n=2), 2: +6,484 (n=4), 0: +5,262 (n=1036), 7: +3,312 (n=5), 1: +3,030 (n=7), 5: +2,717 (n=4), 13: +2,243 (n=2), 6: +1,924 (n=4), 11: +1,588 (n=7), 14: +1,234 (n=7), 10: +1,147 (n=8), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +8,967 | 14 | 17 | 10 | 1111 | 6.13 | 14: +6,167 (n=3), 15: +5,270 (n=5), 17: +5,170 (n=990), 18: +4,356 (n=29), 16: +4,356 (n=61), 20: +1,830 (n=7), 19: +1,829 (n=12), 10: -2,800 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +8,171 | 11 | 14 | 15 | 1112 | 7.85 | 11: +6,172 (n=73), 13: +5,664 (n=22), 15: +5,600 (n=703), 10: +5,021 (n=12), 19: +4,724 (n=8), 18: +3,958 (n=5), 9: +3,937 (n=3), 16: +3,835 (n=10), 14: +3,658 (n=222), 12: +3,270 (n=24), 22: +1,787 (n=3), 17: +1,590 (n=3), 8: +480 (n=18), 20: -1,999 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +8,118 | 2.5 | 0.5 | 11 | 1112 | 5.28 | 2.5: +7,420 (n=2), 0.25: +6,278 (n=151), 1.0: +5,657 (n=82), 0.0: +5,441 (n=126), 0.5: +4,861 (n=698), 1.5: +3,621 (n=9), 1.25: +3,162 (n=5), 2.0: +2,812 (n=4), 1.75: +605 (n=24), 0.75: -698 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,877 | frontier | frontier | 2 | 1113 | 0.84 | frontier: +5,644 (n=1024), v312: -2,232 (n=89) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +7,668 | 0.25 | 1.0 | 15 | 1112 | 6.38 | 0.25: +5,965 (n=13), 0.5: +5,867 (n=24), 0.75: +5,776 (n=5), 1.5: +5,461 (n=586), 2.0: +5,355 (n=17), 1.25: +5,206 (n=105), 1.75: +4,726 (n=19), 1.0: +4,245 (n=310), 3.0: +3,973 (n=2), 0.0: +3,569 (n=16), 2.25: +3,046 (n=4), 2.5: +2,727 (n=6), 3.5: -1,048 (n=3), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +7,605 | 1.5 | 1.25 | 5 | 1113 | 3.5 | 1.5: +5,166 (n=60), 1.25: +5,129 (n=1002), 0.75: +4,832 (n=4), 1.0: +2,964 (n=42), 0.5: -2,439 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,551 | 0.3 | 0.0 | 9 | 1111 | 5.59 | 0.3: +5,410 (n=7), 0.0: +5,191 (n=1046), 0.4: +3,653 (n=6), 0.1: +2,733 (n=30), 0.6: +2,212 (n=4), 0.2: +1,596 (n=11), 0.7: -2,140 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,376 | 28 | 30 | 19 | 1109 | 9.59 | 28: +6,762 (n=99), 26: +6,676 (n=4), 25: +5,975 (n=121), 27: +5,032 (n=38), 30: +4,833 (n=783), 34: +4,562 (n=19), 37: +3,940 (n=8), 36: +3,856 (n=3), 29: +3,022 (n=4), 33: +2,905 (n=4), 32: +2,402 (n=5), 35: +951 (n=7), 45: +241 (n=2), 31: -89 (n=8), 39: -614 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,306 | 34 | 38 | 26 | 1110 | 8.49 | 34: +7,874 (n=2), 42: +7,510 (n=3), 50: +6,994 (n=85), 37: +6,956 (n=7), 24: +6,542 (n=3), 22: +6,104 (n=2), 35: +5,952 (n=458), 32: +5,911 (n=8), 41: +5,604 (n=51), 47: +5,368 (n=4), 26: +5,305 (n=32), 20: +5,106 (n=2), 44: +5,076 (n=3), 43: +4,778 (n=3), 31: +4,610 (n=15), 28: +4,378 (n=7), 27: +4,366 (n=6), 29: +4,306 (n=2), 38: +4,023 (n=344), 39: +2,789 (n=3), 33: +2,341 (n=3), 40: +1,596 (n=3), 30: +567 (n=64) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,971 | 8 | 10 | 11 | 1111 | 6.25 | 8: +5,908 (n=17), 9: +5,715 (n=119), 10: +5,134 (n=895), 12: +4,750 (n=10), 11: +2,749 (n=41), 7: +2,693 (n=15), 6: +2,273 (n=4), 13: -124 (n=7), 4: -1,063 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +6,912 | 2 | 2 | 4 | 1113 | 2.69 | 2: +5,395 (n=1028), 3: +3,269 (n=3), 1: +475 (n=75), 0: -1,517 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +11,378 (n=142)
- (10, 3, 5): +10,905 (n=172)
- (11, 3, 5): +10,683 (n=162)
- (9, 3, 4): +10,584 (n=198)
- (10, 3, 4): +10,309 (n=39)
- (11, 3, 6): +10,254 (n=117)
- (10, 3, 6): +10,183 (n=18)
- (12, 3, 6): +10,084 (n=87)
- (9, 3, 6): +9,706 (n=9)
- (12, 3, 5): +9,662 (n=58)
- (13, 3, 5): +8,853 (n=5)
- (13, 3, 6): +8,762 (n=14)
- (11, 3, 4): +8,559 (n=9)
- (14, 3, 6): +7,609 (n=15)
- (8, 3, 5): +6,544 (n=6)

_Generated 2026-09-12 05:47. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 272 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=272); harvest_min=1–3 (n=272); wheat_tiles=0–7 (n=272); wheat_stock=0–40 (n=272); min_hands=3–6 (n=272); load_per_hand=12–26 (n=272); geese=0–2 (n=272); open_melons=6–14 (n=272)
- **Evidence:** 272 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1113 candidates** with action_table data, **146172 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,068 (n=15350) |         +5,014 (n=7791) |         +5,014 (n=8904) | 32045 |
| BUY_ANIMAL |         +4,455 (n=6186) |         +5,357 (n=1347) |              — (n=0) | 7533 |
| BUY_SEED |         +5,056 (n=11368) |         +5,100 (n=4245) |         +4,588 (n=1538) | 17151 |
| BUY_LAND |         +5,016 (n=3959) |         +5,557 (n=1065) |              — (n=0) | 5024 |
| BUY_PRODUCT |         +5,014 (n=16687) |         +5,014 (n=7791) |         +5,015 (n=7789) | 32267 |
| HIRE |         +4,855 (n=6643) |         +4,849 (n=3854) |         +5,153 (n=2889) | 13386 |
| WATER_MISSED |         +5,014 (n=12441) |         +5,014 (n=7791) |         +5,015 (n=8898) | 29130 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,686 (n=5736) |         +4,695 (n=1496) |         +4,581 (n=2404) | 9636 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,152 |      +5,014 |      +5,069 |      +4,996 |      +4,965 |      +5,010 |
| BUY_ANIMAL |      +4,376 |           — |      +1,809 |      +5,123 |      +5,159 |      +4,558 |
| BUY_SEED |      +4,442 |      +5,805 |      -3,489 |      -4,523 |      +2,861 |      +5,110 |
| BUY_LAND |      -2,439 |      -3,874 |      +5,097 |      -1,110 |      +5,835 |      +5,031 |
| BUY_PRODUCT |      +5,014 |           — |           — |           — |           — |           — |
| HIRE |      +4,918 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,014 |      +2,527 |      +5,014 |      +5,045 |
| FEED_MISSED |           — |      +5,031 |      +2,853 |           — |      +1,809 |      +4,637 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +5,557 | 1065 | 1.36 |
| 2 | BUY_ANIMAL | mid | +5,357 | 1347 | 1.27 |
| 3 | HIRE | late | +5,153 | 2889 | 1.2 |
| 4 | BUY_SEED | mid | +5,100 | 4245 | 1.16 |
| 5 | SELL | early | +5,068 | 15350 | 1.17 |
| 6 | BUY_SEED | early | +5,056 | 11368 | 1.17 |
| 7 | BUY_LAND | early | +5,016 | 3959 | 1.14 |
| 8 | BUY_PRODUCT | late | +5,015 | 7789 | 1.15 |
| 9 | WATER_MISSED | late | +5,015 | 8898 | 1.15 |
| 10 | SELL | mid | +5,014 | 7791 | 1.15 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,280 (n=507)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,280 (n=507)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,554 (n=697)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,548 (n=695)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,524 (n=716)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,466 (n=719)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,446 (n=724)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,300 (n=70)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +5,977 (n=886)
- **HIRE** in ('low', 'mid', 'mid', 'mid'): +5,828 (n=8)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +5,753 (n=1152)
- **SELL** in ('mid', 'mid', 'high', 'mid'): +5,748 (n=12)
- **WATER_MISSED** in ('mid', 'mid', 'high', 'mid'): +5,748 (n=12)
- **FEED_MISSED** in ('mid', 'mid', 'high', 'mid'): +5,748 (n=12)
- **SELL** in ('low', 'mid', 'low', 'mid'): +5,676 (n=15)

_Generated 2026-09-12 05:47. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._