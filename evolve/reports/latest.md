# Evolution run 20260911-233210

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.19 h · candidates evaluated this run: 136 · games 31,508 (14,387/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 19 | 38 |
| dead_pattern | 11 | 22 |
| dead_smoke | 5 | 40 |
| alive | 24 | 3072 |
| held_fail | 14 | 5152 |
| held_pass | 63 | 23184 |
| error | 0 | 0 |

Population (all runs, reached dev): 913 · held-out evaluated: 642 · held-out PASS: 567

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
| `69f9eaac2d61` | orch | ablate:ORCH_P_WEEDS | **+10,383** | 7.5 | 20-0 | -16,425 | +9,745 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,404); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |
| `0b037ebcf3fa` | queue | crossover | **+10,260** | 9.1 | 20-0 | -16,918 | +9,033 | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 19 (gap +1,809 -> final +4,428); days 17-24 drivers: missed_water -44, work_turns +114, idle_turns -35, sales_rev +999. Hands 13 vs 14, animals 11 vs 11, plants 60 vs 5 |
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `f25e784d65ee` | queue | mutate | **+10,227** | 8.3 | 20-0 | -16,406 | +10,406 | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +1,739 -> final +7,620); days 17-24 drivers: missed_water -36, sales_rev +2,327, work_turns +50, idle_turns -37. Hands 12 vs 14, animals 9 vs 11, plants 57 vs 5 |
| `99cf71eb0b6b` | queue | archive_crossover:crossover_g000100_20260912-012458_1 | **+10,219** | 8.5 | 19-1 | -16,252 | +9,927 | harvest_min 1→3, early_hire_days 3→1, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_COMMIT 0.75→0.0, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,175 -> final +5,236); days 16-23 drivers: missed_water -41, work_turns +85, idle_turns -36, sales_rev +1,415. Hands 11 vs 8, animals 10 vs 11, plants 59 vs 5 |
| `d7eec7135f06` | queue | mutate | **+10,140** | 7.2 | 19-1 | -16,966 | +8,831 | melon_floor 0→100, harvest_min 1→3, geese 0→2, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→94, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,640 -> final +6,963); days 16-23 drivers: sales_rev +5,689, work_turns +140, missed_water -12, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 57 vs  |
| `ad621af0852e` | orch | migrate | **+10,100** | 9.9 | 20-0 | -16,287 | +8,812 | harvest_min 1→3, load_per_hand 20→21, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→93, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +2,751 -> final +9,033); days 17-24 drivers: missed_water -35, work_turns +53, idle_turns -39, sales_rev +1,137. Hands 12 vs 14, animals 9 vs 11, plants 62 vs 5 |
| `2bf642462b16` | queue | archive_crossover:crossover_g000025_20260911-200819_1 | **+10,065** | 8.1 | 20-0 | -16,732 | +8,489 | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +1,553 -> final +4,539); days 14-21 drivers: work_turns +81, idle_turns -50, missed_water -5, feed_hour -1.16. Hands 13 vs 8, animals 11 vs 11, plants 60 vs 57. |
| `09bcd201ef44` | queue | archive_crossover:crossover_g000050_20260912-003221_0 | **+10,047** | 8.7 | 20-0 | -16,450 | +10,309 | harvest_min 1→2, early_hire_days 3→1, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |  | cand pulls ahead of C1 from day 16 (gap +2,085 -> final +3,657); days 14-21 drivers: missed_water -17, work_turns +83, idle_turns -28, feed_hour -1.56. Hands 13 vs 8, animals 10 vs 11, plants 60 vs 57 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `4abd19f6a514` | o15 | mutate | +10,905 | 5.1 | 10-0 | -6,092 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `c262b6590f29` | queue | archive_crossover:crossover_g000075_20260912-005550_1 | +10,794 | 4.6 | 10-0 | -8,416 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `d40162bbeaa3` | orch | crossover | +10,545 | 6.0 | 10-0 | -6,551 | held_pass | melon_floor 0→150, harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→15 |
| `9cb98ae7bdd0` | queue | archive_crossover:crossover_g000050_20260912-003221_1 | +10,530 | 5.7 | 10-0 | -7,179 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→18, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WWATER 0.5→0.25, ORCH_P_PLANT 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `f25e784d65ee` | queue | mutate | +10,406 | 5.5 | 10-0 | -6,883 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `508ceae58587` | orch | ablate:ORCH_COMMIT | +10,405 | 6.4 | 10-0 | -6,287 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `53b40a96cac7` | queue | archive_crossover:crossover_g000050_20260911-185026_0 | +10,332 | 4.6 | 10-0 | -8,543 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `63bd49376d83` | queue | mutate | +10,320 | 4.5 | 10-0 | -8,617 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `09bcd201ef44` | queue | archive_crossover:crossover_g000050_20260912-003221_0 | +10,309 | 5.9 | 10-0 | -6,831 | held_pass | harvest_min 1→2, early_hire_days 3→1, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `6c7e6434ea83` | o15 | ablate:ORCH_P_SLACK | +10,290 | 6.4 | 10-0 | -7,259 | held_pass | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `8b03f1857f52` | queue | migrate | +10,263 | 4.9 | 10-0 | -8,584 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `7c3c00c7830d` | queue | archive_crossover:crossover_g000075_20260911-205656_0 | +10,254 | 5.5 | 10-0 | -6,593 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `64e5a7b2f56a` | wide | crossover | +10,209 | 4.9 | 10-0 | -8,314 | held_fail | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `b55411f71d8d` | orch | crossover | +10,109 | 7.3 | 10-0 | -6,781 | held_pass | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, max_animals 17→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `a45b4a44d86f` | queue | archive_crossover:crossover_g000050_20260911-162231_1 | +10,107 | 5.9 | 10-0 | -6,749 | held_pass | harvest_min 1→3, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,905 (`4abd19f6a514`), n=184
- orch: best +10,545 (`d40162bbeaa3`), n=240
- queue: best +10,794 (`c262b6590f29`), n=264
- wide: best +10,209 (`64e5a7b2f56a`), n=203

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,606 | 123 | 92 | 50 | 884 | 14.68 | 123: +9,616 (n=2), 35: +9,592 (n=3), 102: +9,151 (n=3), 132: +8,639 (n=2), 86: +7,210 (n=4), 110: +5,520 (n=62), 81: +5,503 (n=64), 111: +4,937 (n=27), 92: +4,762 (n=660), 99: +4,310 (n=13), 82: +4,186 (n=6), 150: +3,903 (n=5), 119: +3,803 (n=10), 63: +3,619 (n=3), 54: +2,856 (n=5), 96: +1,931 (n=3), 91: +1,573 (n=2), 121: -1,255 (n=2), 0: -1,278 (n=2), 125: -2,734 (n=4), 65: -2,990 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,135 | 0.6 | 0.55 | 12 | 913 | 8.19 | 0.6: +6,049 (n=132), 0.55: +4,935 (n=699), 0.7: +3,630 (n=5), 0.4: +3,565 (n=12), 0.5: +3,197 (n=8), 0.65: +3,011 (n=9), 0.75: +2,689 (n=8), 0.8: +1,487 (n=16), 0.45: +296 (n=4), 0.35: +40 (n=3), 0.9: -1,874 (n=6), 0.3: -5,086 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,651 | 2 | 3 | 3 | 913 | 1.36 | 2: +5,820 (n=717), 3: +947 (n=193), 4: -4,832 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,259 | 18 | 20 | 14 | 911 | 7.68 | 18: +5,813 (n=170), 17: +5,015 (n=9), 19: +4,942 (n=19), 20: +4,656 (n=659), 22: +4,068 (n=9), 21: +3,856 (n=27), 16: +3,297 (n=5), 24: +1,532 (n=2), 13: +284 (n=3), 14: -765 (n=4), 12: -1,224 (n=2), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,081 | 1.25 | 0.5 | 12 | 910 | 6.69 | 1.25: +7,126 (n=7), 0.25: +6,312 (n=15), 1.75: +5,821 (n=6), 0.5: +4,873 (n=778), 0.75: +4,165 (n=7), 0.0: +3,843 (n=78), 3.0: +3,789 (n=8), 1.0: +3,319 (n=8), 2.75: -2,956 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +9,987 | 108 | 100 | 46 | 891 | 12.95 | 108: +8,353 (n=2), 93: +8,014 (n=2), 112: +7,521 (n=2), 135: +6,542 (n=3), 124: +6,478 (n=5), 109: +6,461 (n=53), 110: +6,364 (n=108), 132: +6,305 (n=18), 141: +6,213 (n=9), 117: +5,882 (n=2), 99: +5,759 (n=3), 87: +5,023 (n=5), 86: +4,957 (n=27), 67: +4,927 (n=4), 150: +4,865 (n=88), 104: +4,853 (n=3), 100: +4,289 (n=518), 105: +4,150 (n=7), 94: +3,701 (n=13), 50: +3,314 (n=8), 126: +3,135 (n=3), 68: +2,481 (n=2), 62: +519 (n=4), 82: -1,635 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,229 | 4 | 0 | 18 | 907 | 10.17 | 4: +8,585 (n=2), 2: +6,484 (n=4), 0: +5,032 (n=844), 1: +3,030 (n=7), 6: +2,980 (n=3), 7: +1,940 (n=4), 11: +1,588 (n=7), 10: +1,472 (n=7), 5: +745 (n=3), 14: +580 (n=6), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +9,133 | 14 | 17 | 10 | 911 | 6.24 | 14: +5,201 (n=2), 17: +4,915 (n=825), 18: +4,574 (n=25), 15: +4,254 (n=4), 16: +3,398 (n=36), 19: +1,829 (n=12), 20: +1,115 (n=5), 10: -3,932 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,767 | 28 | 30 | 18 | 910 | 10.03 | 28: +6,995 (n=54), 26: +6,676 (n=4), 25: +5,866 (n=89), 27: +4,944 (n=37), 30: +4,592 (n=669), 34: +4,562 (n=19), 37: +3,940 (n=8), 36: +3,856 (n=3), 35: +2,046 (n=6), 32: +1,080 (n=4), 29: +927 (n=3), 39: +774 (n=2), 45: +241 (n=2), 31: -89 (n=8), 33: -772 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,596 | frontier | frontier | 2 | 913 | 0.84 | frontier: +5,362 (n=840), v312: -2,234 (n=73) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +7,119 | 2.0 | 1.0 | 15 | 911 | 6.29 | 2.0: +5,417 (n=16), 0.5: +5,356 (n=18), 1.5: +5,348 (n=511), 1.25: +5,147 (n=90), 0.75: +5,010 (n=4), 1.75: +4,572 (n=17), 0.25: +4,466 (n=7), 1.0: +3,479 (n=227), 2.25: +2,523 (n=3), 2.5: +1,968 (n=5), 0.0: +1,870 (n=9), 3.5: +774 (n=2), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +7,100 | 2.5 | 0.5 | 10 | 913 | 5.78 | 2.5: +7,420 (n=2), 0.25: +5,648 (n=91), 1.0: +5,525 (n=63), 0.0: +5,352 (n=92), 0.5: +4,684 (n=619), 1.5: +3,621 (n=9), 1.25: +3,162 (n=5), 2.0: +2,812 (n=4), 0.75: +858 (n=7), 1.75: +319 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +7,038 | 1.25 | 1.5 | 21 | 909 | 9.3 | 1.25: +7,749 (n=7), 4.5: +6,549 (n=2), 2.5: +6,473 (n=11), 3.5: +6,142 (n=230), 3.0: +5,917 (n=38), 4.0: +5,616 (n=2), 1.0: +5,350 (n=8), 0.25: +5,272 (n=3), 1.75: +4,719 (n=7), 0.75: +4,441 (n=4), 2.0: +4,284 (n=4), 1.5: +4,163 (n=551), 0.0: +3,699 (n=13), 3.25: +3,698 (n=3), 0.5: +2,793 (n=7), 2.75: +2,046 (n=13), 5.0: +710 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,922 | 0.3 | 0.0 | 9 | 911 | 5.56 | 0.3: +5,410 (n=7), 0.0: +4,907 (n=854), 0.4: +3,653 (n=6), 0.1: +3,145 (n=26), 0.2: +1,430 (n=10), 0.6: +1,067 (n=3), 0.7: -1,512 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,919 | 9 | 10 | 11 | 911 | 6.2 | 9: +5,856 (n=94), 8: +5,683 (n=12), 10: +4,856 (n=729), 12: +3,695 (n=8), 11: +2,732 (n=39), 7: +2,693 (n=15), 6: +2,273 (n=4), 13: -124 (n=7), 4: -1,063 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +6,646 | 1.5 | 1.25 | 5 | 913 | 3.53 | 1.5: +5,056 (n=40), 1.25: +4,858 (n=827), 0.75: +4,342 (n=3), 1.0: +2,811 (n=40), 0.5: -1,590 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +6,581 | 10 | 6 | 8 | 913 | 3.43 | 10: +7,813 (n=12), 7: +6,152 (n=280), 9: +5,981 (n=23), 4: +5,958 (n=6), 5: +5,234 (n=32), 8: +4,210 (n=42), 6: +3,937 (n=506), 3: +1,231 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +6,547 | 11 | 14 | 14 | 912 | 7.03 | 11: +6,323 (n=56), 13: +5,707 (n=20), 15: +5,293 (n=563), 10: +5,021 (n=12), 19: +4,724 (n=8), 16: +3,835 (n=10), 18: +3,794 (n=4), 12: +3,455 (n=21), 14: +3,406 (n=192), 22: +2,182 (n=2), 17: +1,590 (n=3), 8: +480 (n=18), 20: -224 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +6,485 | 2 | 2 | 4 | 913 | 2.66 | 2: +5,180 (n=835), 3: +3,269 (n=3), 1: +195 (n=69), 0: -1,305 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +6,415 | 10 | 14 | 10 | 910 | 4.83 | 10: +6,058 (n=31), 9: +6,022 (n=41), 13: +4,820 (n=54), 14: +4,731 (n=758), 12: +4,477 (n=7), 11: +2,502 (n=14), 8: -357 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +10,905 (n=151)
- (9, 3, 5): +10,794 (n=115)
- (9, 3, 4): +10,545 (n=174)
- (10, 3, 4): +10,309 (n=33)
- (11, 3, 6): +10,254 (n=96)
- (11, 3, 5): +10,071 (n=143)
- (12, 3, 6): +10,015 (n=63)
- (10, 3, 6): +9,935 (n=12)
- (9, 3, 6): +9,706 (n=7)
- (12, 3, 5): +9,598 (n=43)
- (11, 3, 4): +8,559 (n=9)
- (13, 3, 5): +7,918 (n=3)
- (14, 3, 6): +7,609 (n=10)
- (8, 3, 5): +6,544 (n=5)
- (15, 3, 6): +6,377 (n=9)

_Generated 2026-09-12 01:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 219 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=219); harvest_min=1–3 (n=219); wheat_tiles=0–7 (n=219); wheat_stock=0–40 (n=219); min_hands=3–6 (n=219); load_per_hand=12–26 (n=219); geese=0–2 (n=219); open_melons=6–14 (n=219)
- **Evidence:** 219 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**913 candidates** with action_table data, **120055 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,811 (n=12601) |         +4,754 (n=6391) |         +4,754 (n=7304) | 26296 |
| BUY_ANIMAL |         +4,216 (n=5099) |         +5,146 (n=1116) |              — (n=0) | 6215 |
| BUY_SEED |         +4,798 (n=9341) |         +4,837 (n=3477) |         +4,385 (n=1267) | 14085 |
| BUY_LAND |         +4,731 (n=3238) |         +5,264 (n=873) |              — (n=0) | 4111 |
| BUY_PRODUCT |         +4,754 (n=13689) |         +4,754 (n=6391) |         +4,754 (n=6390) | 26470 |
| HIRE |         +4,619 (n=5490) |         +4,590 (n=3150) |         +4,937 (n=2372) | 11012 |
| WATER_MISSED |         +4,756 (n=10211) |         +4,754 (n=6391) |         +4,755 (n=7301) | 23903 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,437 (n=4722) |         +4,518 (n=1251) |         +4,314 (n=1990) | 7963 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +4,896 |      +4,754 |      +4,813 |      +4,773 |      +4,705 |      +4,747 |
| BUY_ANIMAL |      +4,139 |           — |      +1,809 |      +5,083 |      +4,875 |      +4,335 |
| BUY_SEED |      +4,197 |      +5,557 |      -3,237 |      -4,178 |      +2,716 |      +4,852 |
| BUY_LAND |      -2,014 |      -3,514 |      +4,824 |      -1,110 |      +5,545 |      +4,734 |
| BUY_PRODUCT |      +4,754 |           — |           — |           — |           — |           — |
| HIRE |      +4,679 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,754 |      +2,386 |      +4,754 |      +4,786 |
| FEED_MISSED |           — |      +4,761 |      +2,828 |           — |      +1,809 |      +4,398 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +5,264 | 873 | 1.28 |
| 2 | BUY_ANIMAL | mid | +5,146 | 1116 | 1.23 |
| 3 | HIRE | late | +4,937 | 2372 | 1.17 |
| 4 | BUY_SEED | mid | +4,837 | 3477 | 1.11 |
| 5 | SELL | early | +4,811 | 12601 | 1.12 |
| 6 | BUY_SEED | early | +4,798 | 9341 | 1.12 |
| 7 | WATER_MISSED | early | +4,756 | 10211 | 1.11 |
| 8 | WATER_MISSED | late | +4,755 | 7301 | 1.1 |
| 9 | SELL | mid | +4,754 | 6391 | 1.1 |
| 10 | SELL | late | +4,754 | 7304 | 1.1 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,060 (n=393)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,060 (n=393)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,440 (n=65)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,399 (n=548)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,366 (n=544)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,360 (n=562)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,300 (n=564)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,280 (n=568)
- **HIRE** in ('low', 'mid', 'mid', 'mid'): +6,128 (n=7)
- **SELL** in ('low', 'low', 'high', 'mid'): -6,032 (n=5)
- **WATER_MISSED** in ('low', 'low', 'high', 'mid'): -6,032 (n=5)
- **FEED_MISSED** in ('low', 'low', 'high', 'mid'): -6,032 (n=5)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +5,825 (n=78)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +5,825 (n=78)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +5,682 (n=719)

_Generated 2026-09-12 01:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._