# Evolution run 20260912-014435

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.03 h · candidates evaluated this run: 124 · games 31,796 (15,686/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 14 | 28 |
| dead_pattern | 12 | 24 |
| dead_smoke | 2 | 16 |
| alive | 15 | 1920 |
| held_fail | 11 | 4048 |
| held_pass | 70 | 25760 |
| error | 0 | 0 |

Population (all runs, reached dev): 1009 · held-out evaluated: 723 · held-out PASS: 637

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
| `1df16554118d` | queue | archive_crossover:crossover_g000025_20260912-022223_1 | **+10,410** | 9.5 | 20-0 | -16,096 | +9,300 | load_per_hand 20→19, wheat_cap 22→25, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,319 -> final +8,705); days 14-21 drivers: missed_water -24, work_turns +82, sales_rev +1,959, idle_turns -32. Hands 12 vs 8, animals 9 vs 11, plants 63 vs 57 |
| `19e5809e9eb7` | orch | crossover | **+10,403** | 8.3 | 20-0 | -16,627 | +9,293 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→41, MELON_PRICE_CUSHION 100→89, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,097 -> final +4,649); days 16-23 drivers: missed_water -31, work_turns +102, idle_turns -38, sales_rev +937. Hands 12 vs 8, animals 10 vs 11, plants 57 vs 57 |
| `2fbfc0622b49` | orch | mutate | **+10,401** | 10.4 | 20-0 | -16,928 | +9,486 | melon_floor 0→150, harvest_min 1→2, min_hands 3→5, early_hire_days 3→5, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.75, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,294 -> final +9,203); days 14-21 drivers: missed_water -32, work_turns +69, idle_turns -47, feed_hour -1.6. Hands 10 vs 8, animals 9 vs 11, plants 63 vs 57. |
| `69f9eaac2d61` | orch | ablate:ORCH_P_WEEDS | **+10,383** | 7.5 | 20-0 | -16,425 | +9,745 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,404); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |
| `0b037ebcf3fa` | queue | crossover | **+10,260** | 9.1 | 20-0 | -16,918 | +9,033 | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 19 (gap +1,809 -> final +4,428); days 17-24 drivers: missed_water -44, work_turns +114, idle_turns -35, sales_rev +999. Hands 13 vs 14, animals 11 vs 11, plants 60 vs 5 |
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `f668bf4d1549` | o15 | crossover | **+10,237** | 6.4 | 19-1 | -17,033 | +9,662 | melon_floor 0→150, harvest_min 1→2, open_melons 10→9, feed_spare_poor 0→2, demand_share 0.55→0.6, max_animals 17→16, wheat_water_tier 0→1, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.7, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→1.0, ORCH_P_WWATER 0.5→0.0, ORCH_P_PLANT 1.0→0.75, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 24 (gap +2,624 -> final +2,239); days 22-29 drivers: missed_water -37, sales_rev +4,218, work_turns +19, idle_turns -12. Hands 5 vs 5, animals 12 vs 11, plants 7 vs 8. |
| `f25e784d65ee` | queue | mutate | **+10,227** | 8.3 | 20-0 | -16,406 | +10,406 | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +1,739 -> final +7,620); days 17-24 drivers: missed_water -36, sales_rev +2,327, work_turns +50, idle_turns -37. Hands 12 vs 14, animals 9 vs 11, plants 57 vs 5 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `4abd19f6a514` | o15 | mutate | +10,905 | 5.1 | 10-0 | -6,092 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `dbf281819c7d` | o15 | mutate | +10,811 | 4.8 | 10-0 | -6,255 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_tiles 0→1, open_melons 10→9, early_hire_days 3→1, feed_spare_poor 0→1, demand_share 0.55→0.6, max_animals 17→16, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, wheat_hold_days 0→1, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→150, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→18, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `c262b6590f29` | queue | archive_crossover:crossover_g000075_20260912-005550_1 | +10,794 | 4.6 | 10-0 | -8,416 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `31b8c13ba6a7` | queue | archive_crossover:crossover_g000075_20260912-032444_0 | +10,616 | 4.5 | 10-0 | -8,683 | held_fail | harvest_min 1→3, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `d40162bbeaa3` | orch | crossover | +10,545 | 6.0 | 10-0 | -6,551 | held_pass | melon_floor 0→150, harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→15 |
| `9cb98ae7bdd0` | queue | archive_crossover:crossover_g000050_20260912-003221_1 | +10,530 | 5.7 | 10-0 | -7,179 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→18, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WWATER 0.5→0.25, ORCH_P_PLANT 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `e31fc28b0264` | wide | paired | +10,476 | 4.9 | 10-0 | -8,354 | held_fail | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, MAX_SHEEP 14→9, OPENING_MELONS 14→6, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `f25e784d65ee` | queue | mutate | +10,406 | 5.5 | 10-0 | -6,883 | held_pass | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, wheat_cap 22→21, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `508ceae58587` | orch | ablate:ORCH_COMMIT | +10,405 | 6.4 | 10-0 | -6,287 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `53b40a96cac7` | queue | archive_crossover:crossover_g000050_20260911-185026_0 | +10,332 | 4.6 | 10-0 | -8,543 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `63bd49376d83` | queue | mutate | +10,320 | 4.5 | 10-0 | -8,617 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_SLACK_HOUR 14→15 |
| `09bcd201ef44` | queue | archive_crossover:crossover_g000050_20260912-003221_0 | +10,309 | 5.9 | 10-0 | -6,831 | held_pass | harvest_min 1→2, early_hire_days 3→1, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, setup_capital_share 0.25→0.35, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→10, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.0 |
| `6c7e6434ea83` | o15 | ablate:ORCH_P_SLACK | +10,290 | 6.4 | 10-0 | -7,259 | held_pass | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |
| `8b03f1857f52` | queue | migrate | +10,263 | 4.9 | 10-0 | -8,584 | held_fail | load_per_hand 20→18, wheat_cap 22→25, wheat_sell_price 30→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `7c3c00c7830d` | queue | archive_crossover:crossover_g000075_20260911-205656_0 | +10,254 | 5.5 | 10-0 | -6,593 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +10,905 (`4abd19f6a514`), n=207
- orch: best +10,545 (`d40162bbeaa3`), n=270
- queue: best +10,794 (`c262b6590f29`), n=289
- wide: best +10,476 (`e31fc28b0264`), n=221

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +12,606 | 123 | 92 | 53 | 977 | 14.58 | 123: +9,616 (n=2), 35: +9,592 (n=3), 102: +9,151 (n=3), 132: +8,639 (n=2), 86: +7,210 (n=4), 110: +5,917 (n=83), 81: +5,330 (n=67), 111: +5,074 (n=29), 150: +5,054 (n=6), 92: +4,890 (n=725), 99: +4,310 (n=13), 82: +4,186 (n=6), 119: +3,803 (n=10), 63: +3,619 (n=3), 96: +3,017 (n=4), 54: +2,856 (n=5), 91: +1,573 (n=2), 121: -1,255 (n=2), 0: -1,278 (n=2), 125: -2,734 (n=4), 65: -2,990 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +11,522 | 0.6 | 0.55 | 13 | 1009 | 8.56 | 0.6: +6,324 (n=160), 0.55: +5,064 (n=742), 0.5: +4,727 (n=11), 0.85: +3,951 (n=4), 0.7: +3,630 (n=5), 0.4: +3,468 (n=17), 0.65: +2,512 (n=11), 0.75: +2,463 (n=12), 0.8: +2,450 (n=21), 0.45: +296 (n=4), 0.35: +40 (n=3), 0.9: -1,508 (n=7), 0.3: -5,198 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,755 | 18 | 20 | 14 | 1008 | 8.35 | 18: +5,876 (n=183), 17: +5,705 (n=11), 19: +5,549 (n=29), 20: +4,820 (n=725), 22: +4,068 (n=9), 21: +3,994 (n=28), 16: +3,369 (n=6), 24: +1,532 (n=2), 15: +1,470 (n=3), 13: +284 (n=3), 14: -765 (n=4), 12: -1,224 (n=2), 23: -4,879 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,715 | 2 | 3 | 3 | 1009 | 1.42 | 2: +5,883 (n=813), 3: +947 (n=193), 4: -4,832 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,477 | 0.25 | 0.5 | 12 | 1006 | 6.56 | 0.25: +6,653 (n=26), 1.25: +6,065 (n=8), 1.75: +6,043 (n=9), 0.5: +5,003 (n=845), 3.0: +4,399 (n=9), 0.75: +4,385 (n=9), 0.0: +4,138 (n=88), 1.0: +3,319 (n=8), 2.75: -3,825 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +9,987 | 108 | 100 | 50 | 986 | 14.17 | 108: +8,353 (n=2), 93: +8,014 (n=2), 89: +7,995 (n=2), 112: +7,521 (n=2), 135: +6,542 (n=3), 124: +6,478 (n=5), 109: +6,461 (n=56), 137: +6,404 (n=2), 132: +6,378 (n=19), 110: +6,325 (n=126), 117: +5,882 (n=2), 99: +5,759 (n=3), 141: +5,616 (n=17), 86: +5,500 (n=38), 150: +5,199 (n=97), 87: +5,023 (n=5), 67: +4,927 (n=4), 104: +4,853 (n=3), 102: +4,781 (n=2), 68: +4,532 (n=3), 100: +4,420 (n=554), 105: +4,150 (n=7), 50: +3,359 (n=9), 126: +3,135 (n=3), 94: +2,970 (n=14), 62: +519 (n=4), 82: -1,635 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,229 | 4 | 0 | 19 | 1003 | 11.13 | 4: +8,585 (n=2), 2: +6,484 (n=4), 0: +5,166 (n=936), 1: +3,030 (n=7), 6: +2,980 (n=3), 5: +2,717 (n=4), 13: +2,243 (n=2), 7: +1,940 (n=4), 11: +1,588 (n=7), 10: +1,147 (n=8), 14: +580 (n=6), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +9,202 | 15 | 17 | 10 | 1007 | 6.23 | 15: +5,270 (n=5), 14: +5,201 (n=2), 17: +5,026 (n=910), 18: +4,760 (n=26), 16: +4,263 (n=44), 20: +2,302 (n=6), 19: +1,829 (n=12), 10: -3,932 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +7,832 | 1.25 | 1.25 | 5 | 1009 | 3.54 | 1.25: +5,032 (n=917), 1.5: +4,960 (n=45), 0.75: +4,342 (n=3), 1.0: +2,811 (n=40), 0.5: -2,801 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,781 | frontier | frontier | 2 | 1009 | 0.84 | frontier: +5,524 (n=929), v312: -2,257 (n=80) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +7,755 | 10 | 14 | 7 | 1008 | 3.79 | 10: +9,114 (n=2), 13: +5,947 (n=114), 14: +5,016 (n=805), 6: +4,748 (n=9), 11: +2,444 (n=60), 12: +1,360 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,742 | 0.3 | 0.0 | 9 | 1007 | 5.6 | 0.3: +5,410 (n=7), 0.0: +5,066 (n=949), 0.4: +3,653 (n=6), 0.1: +3,145 (n=26), 0.2: +1,430 (n=10), 0.6: +1,067 (n=3), 0.7: -2,331 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +7,479 | 0.75 | 1.0 | 15 | 1008 | 6.58 | 0.75: +5,776 (n=5), 0.25: +5,660 (n=12), 1.5: +5,416 (n=546), 2.0: +5,355 (n=17), 0.5: +5,167 (n=20), 1.25: +5,090 (n=94), 1.75: +4,572 (n=17), 1.0: +3,994 (n=268), 3.0: +3,973 (n=2), 0.0: +3,307 (n=15), 2.25: +2,523 (n=3), 2.5: +1,968 (n=5), 3.5: +774 (n=2), 4.0: -1,702 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,306 | 34 | 38 | 26 | 1006 | 8.26 | 34: +7,874 (n=2), 42: +7,510 (n=3), 37: +6,956 (n=7), 24: +6,542 (n=3), 50: +6,477 (n=62), 22: +6,104 (n=2), 35: +5,964 (n=405), 32: +5,911 (n=8), 41: +5,801 (n=48), 27: +5,190 (n=4), 20: +5,106 (n=2), 44: +5,076 (n=3), 26: +4,979 (n=28), 43: +4,778 (n=3), 31: +4,610 (n=15), 28: +4,378 (n=7), 29: +4,306 (n=2), 38: +4,039 (n=327), 39: +2,789 (n=3), 33: +2,341 (n=3), 40: +1,596 (n=3), 47: +795 (n=2), 30: +567 (n=64) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +7,085 | 9 | 10 | 11 | 1007 | 6.27 | 9: +6,022 (n=104), 8: +5,819 (n=14), 10: +4,996 (n=813), 12: +3,695 (n=8), 11: +2,732 (n=39), 7: +2,693 (n=15), 6: +2,273 (n=4), 13: -124 (n=7), 4: -1,063 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +7,038 | 1.25 | 1.5 | 21 | 1005 | 9.28 | 1.25: +7,749 (n=7), 2.5: +6,635 (n=13), 3.5: +6,229 (n=255), 3.0: +6,004 (n=39), 1.0: +5,671 (n=9), 4.0: +5,616 (n=2), 0.25: +5,272 (n=3), 4.5: +5,009 (n=4), 0.75: +4,441 (n=4), 1.5: +4,363 (n=608), 0.0: +4,059 (n=15), 1.75: +4,014 (n=9), 0.5: +3,930 (n=9), 3.25: +3,698 (n=3), 2.0: +3,185 (n=5), 2.75: +2,334 (n=14), 5.0: +710 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,025 | 28 | 30 | 18 | 1006 | 9.63 | 28: +6,935 (n=79), 26: +6,676 (n=4), 25: +5,912 (n=110), 27: +5,032 (n=38), 30: +4,691 (n=713), 34: +4,562 (n=19), 37: +3,940 (n=8), 36: +3,856 (n=3), 29: +3,022 (n=4), 33: +2,905 (n=4), 32: +2,402 (n=5), 35: +2,046 (n=6), 39: +746 (n=3), 45: +241 (n=2), 31: -89 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +6,864 | 2.5 | 0.5 | 11 | 1008 | 5.54 | 2.5: +7,420 (n=2), 0.25: +5,923 (n=119), 1.0: +5,584 (n=71), 0.0: +5,513 (n=110), 0.5: +4,767 (n=659), 1.5: +3,621 (n=9), 1.25: +3,162 (n=5), 2.0: +2,812 (n=4), 0.75: +858 (n=7), 1.75: +556 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +6,829 | 2 | 2 | 4 | 1009 | 2.68 | 2: +5,311 (n=928), 3: +3,269 (n=3), 1: +327 (n=71), 0: -1,517 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +6,553 | 9 | 14 | 10 | 1007 | 5.58 | 9: +6,195 (n=50), 10: +5,892 (n=44), 14: +4,894 (n=828), 13: +4,885 (n=56), 12: +3,568 (n=8), 11: +2,502 (n=14), 7: +776 (n=2), 8: -357 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +10,905 (n=161)
- (9, 3, 5): +10,794 (n=130)
- (9, 3, 4): +10,545 (n=184)
- (10, 3, 4): +10,309 (n=37)
- (11, 3, 6): +10,254 (n=104)
- (10, 3, 6): +10,183 (n=18)
- (11, 3, 5): +10,071 (n=146)
- (12, 3, 6): +10,015 (n=72)
- (9, 3, 6): +9,706 (n=8)
- (12, 3, 5): +9,662 (n=52)
- (11, 3, 4): +8,559 (n=9)
- (13, 3, 5): +7,918 (n=4)
- (14, 3, 6): +7,609 (n=13)
- (8, 3, 5): +6,544 (n=5)
- (15, 3, 6): +6,377 (n=19)

_Generated 2026-09-12 03:46. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 244 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=244); harvest_min=1–3 (n=244); wheat_tiles=0–7 (n=244); wheat_stock=0–40 (n=244); min_hands=3–6 (n=244); load_per_hand=12–26 (n=244); geese=0–2 (n=244); open_melons=6–14 (n=244)
- **Evidence:** 244 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1009 candidates** with action_table data, **132552 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +4,962 (n=13919) |         +4,907 (n=7063) |         +4,907 (n=8072) | 29054 |
| BUY_ANIMAL |         +4,365 (n=5617) |         +5,251 (n=1225) |              — (n=0) | 6842 |
| BUY_SEED |         +4,954 (n=10309) |         +4,984 (n=3837) |         +4,507 (n=1396) | 15542 |
| BUY_LAND |         +4,888 (n=3584) |         +5,430 (n=967) |              — (n=0) | 4551 |
| BUY_PRODUCT |         +4,907 (n=15129) |         +4,907 (n=7063) |         +4,907 (n=7062) | 29254 |
| HIRE |         +4,763 (n=6043) |         +4,734 (n=3502) |         +5,076 (n=2618) | 12163 |
| WATER_MISSED |         +4,907 (n=11282) |         +4,907 (n=7063) |         +4,908 (n=8067) | 26412 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +4,590 (n=5199) |         +4,663 (n=1353) |         +4,497 (n=2182) | 8734 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,045 |      +4,907 |      +4,957 |      +4,908 |      +4,866 |      +4,901 |
| BUY_ANIMAL |      +4,282 |           — |      +1,809 |      +5,066 |      +5,038 |      +4,471 |
| BUY_SEED |      +4,349 |      +5,709 |      -3,317 |      -4,178 |      +2,830 |      +5,002 |
| BUY_LAND |      -2,645 |      -3,737 |      +4,978 |      -1,110 |      +5,707 |      +4,903 |
| BUY_PRODUCT |      +4,907 |           — |           — |           — |           — |           — |
| HIRE |      +4,822 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +4,907 |      +2,504 |      +4,907 |      +4,938 |
| FEED_MISSED |           — |      +4,923 |      +2,842 |           — |      +1,809 |      +4,557 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +5,430 | 967 | 1.33 |
| 2 | BUY_ANIMAL | mid | +5,251 | 1225 | 1.26 |
| 3 | HIRE | late | +5,076 | 2618 | 1.2 |
| 4 | BUY_SEED | mid | +4,984 | 3837 | 1.15 |
| 5 | SELL | early | +4,962 | 13919 | 1.16 |
| 6 | BUY_SEED | early | +4,954 | 10309 | 1.16 |
| 7 | WATER_MISSED | late | +4,908 | 8067 | 1.14 |
| 8 | SELL | mid | +4,907 | 7063 | 1.14 |
| 9 | SELL | late | +4,907 | 8072 | 1.14 |
| 10 | BUY_PRODUCT | early | +4,907 | 15129 | 1.14 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,164 (n=447)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,164 (n=447)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +6,527 (n=614)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +6,507 (n=614)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +6,494 (n=633)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,471 (n=66)
- **SELL** in ('low', 'low', 'low', 'mid'): +6,440 (n=635)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,422 (n=639)
- **SELL** in ('low', 'low', 'high', 'mid'): -6,099 (n=6)
- **WATER_MISSED** in ('low', 'low', 'high', 'mid'): -6,099 (n=6)
- **FEED_MISSED** in ('low', 'low', 'high', 'mid'): -6,099 (n=6)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +5,864 (n=80)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +5,864 (n=80)
- **SELL** in ('low', 'mid', 'low', 'mid'): +5,842 (n=13)
- **BUY_ANIMAL** in ('low', 'mid', 'low', 'mid'): +5,842 (n=13)

_Generated 2026-09-12 03:46. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._