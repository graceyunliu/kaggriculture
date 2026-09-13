# Evolution run 20260912-201121

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.00 h · candidates evaluated this run: 128 · games 31,246 (15,597/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 12 | 24 |
| dead_pattern | 11 | 22 |
| dead_smoke | 4 | 32 |
| alive | 25 | 3200 |
| held_fail | 10 | 3680 |
| held_pass | 66 | 24288 |
| error | 0 | 0 |

Population (all runs, reached dev): 1878 · held-out evaluated: 1416 · held-out PASS: 1217

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
| `485efdc2781b` | wide | crossover | **+10,963** | 7.9 | 20-0 | -16,072 | +10,336 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.5, SPREAD_W 1.25→1.5, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→1.0, ORCH_P_WWATER 0.5→0.25, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,056 -> final +4,261); days 16-23 drivers: missed_water -38, work_turns +119, sales_rev +3,701, idle_turns -30. Hands 12 vs 8, animals 12 vs 11, plants 55 vs  |
| `2d7b81d266ed` | queue | mutate | **+10,873** | 6.8 | 20-0 | -16,760 | +8,364 | harvest_min 1→3, min_hands 3→4, load_per_hand 20→19, geese 0→1, wheat_cap 22→20, setup_capital_share 0.25→0.1, MAX_HANDS 14→12, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 17→15, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WWATER 0.5→0.75, ORCH_P_WATER 1.0→0.25, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, MAX_SHEEP ?, SPREAD_CAP ?, ORCH_P_WWATER ? | cand pulls ahead of C1 from day 18 (gap +2,142 -> final +7,049); days 16-23 drivers: sales_rev +6,229, missed_water -24, work_turns +112, idle_turns -28. Hands 12 vs 8, animals 12 vs 11, plants 58 vs  |
| `ccfc4b5bf05a` | orch | ablate:ORCH_P_WEEDS | **+10,842** | 8.3 | 20-0 | -16,936 | +8,340 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, geese 0→1, wheat_cap 22→25, setup_capital_share 0.25→0.3, labor_reserve_buffer 92→67, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→26, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→2.25, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 19 (gap +2,275 -> final +6,584); days 17-24 drivers: missed_water -45, work_turns +139, sales_rev +1,558, idle_turns -36. Hands 12 vs 14, animals 12 vs 11, plants 55 vs |
| `122ac868b5fe` | wide | crossover | **+10,798** | 9.2 | 20-0 | -16,234 | +10,801 | harvest_min 1→2, min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→8.0, ORCH_COMMIT 0.75→0.0, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 16 (gap +2,594 -> final +3,868); days 14-21 drivers: missed_water -32, work_turns +72, idle_turns -72, sales_rev +2,809. Hands 13 vs 8, animals 10 vs 11, plants 58 vs 5 |
| `de988febe942` | o15 | paired | **+10,757** | 7.7 | 20-0 | -17,354 | +7,450 | harvest_min 1→3, open_melons 10→11, early_hire_days 3→5, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +3,607 -> final +3,476); days 16-23 drivers: missed_water -33, work_turns +107, sales_rev +2,925, feed_hour -1.16. Hands 11 vs 8, animals 12 vs 11, plants 52 vs |
| `6e498867e484` | orch | mutate | **+10,732** | 8.5 | 20-0 | -16,811 | +8,263 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, geese 0→1, wheat_cap 22→25, setup_capital_share 0.25→0.3, labor_reserve_buffer 92→67, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→26, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.0, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→15 | wheat_water_tier +204, labor_reserve_buffer ?, SPREAD_W ?, ORCH_P_WEEDS -77, ORCH_COMMIT -885 | cand pulls ahead of C1 from day 19 (gap +2,044 -> final +5,514); days 17-24 drivers: missed_water -43, work_turns +143, sales_rev +1,154, feed_hour -1.46. Hands 13 vs 14, animals 12 vs 11, plants 55 v |
| `7db78783cfe5` | orch | crossover | **+10,730** | 9.0 | 20-0 | -15,843 | +10,109 | harvest_min 1→2, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→35, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→8, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.5, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +3,237 -> final +4,315); days 14-21 drivers: missed_water -46, work_turns +125, idle_turns -69, sales_rev +2,699. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `e00215f1e98a` | orch | ablate:wheat_water_tier | **+10,643** | 8.1 | 20-0 | -16,717 | +8,430 | melon_floor 0→150, harvest_min 1→3, min_hands 3→4, geese 0→1, wheat_cap 22→25, wheat_water_tier 0→1, setup_capital_share 0.25→0.3, labor_reserve_buffer 92→35, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→26, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→13, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.0, ORCH_P_FERT 0.5→1.25, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→1.75, ORCH_SLACK_HOUR 14→13 |  | cand pulls ahead of C1 from day 18 (gap +1,926 -> final +7,053); days 16-23 drivers: missed_water -32, work_turns +130, sales_rev +4,817, idle_turns -39. Hands 12 vs 8, animals 12 vs 11, plants 55 vs  |
| `f619488bed80` | wide | paired | **+10,531** | 7.1 | 19-1 | -16,153 | +11,072 | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |  | cand pulls ahead of C1 from day 16 (gap +2,647 -> final +3,907); days 14-21 drivers: missed_water -34, work_turns +84, sales_rev +1,806, idle_turns -36. Hands 12 vs 8, animals 10 vs 11, plants 57 vs 5 |
| `1b7641b11a93` | orch | crossover | **+10,492** | 8.2 | 20-0 | -16,430 | +9,624 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 | wheat_sell_price ?, CROP_SWEEP_LEN -173, STRAW_CUTOFF ?, NEAR_RADIUS +214, OPP_GROWTH ?, ORCH_P_WEEDS -121 | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,400); days 16-23 drivers: missed_water -44, work_turns +122, sales_rev +3,509, idle_turns -44. Hands 13 vs 8, animals 12 vs 11, plants 59 vs  |
| `9aed5a4df4b1` | wide | crossover | **+10,484** | 10.4 | 20-0 | -17,069 | +8,913 | min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→14, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→136, NEAR_RADIUS 2→3, OPENING_MELONS 14→11, SPREAD_W 1.25→1.5, SPREAD_CAP 3→7, ORCH_ON 0→1, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |  | cand pulls ahead of C1 from day 16 (gap +2,887 -> final +2,817); days 14-21 drivers: missed_water -40, work_turns +126, idle_turns -59, sales_rev +1,191. Hands 12 vs 8, animals 12 vs 11, plants 54 vs  |
| `33d973e44a24` | o15 | paired | **+10,471** | 8.8 | 20-0 | -16,658 | +10,015 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 | min_hands +147, ORCH_P_SLACK -275 | cand pulls ahead of C1 from day 18 (gap +2,562 -> final +3,705); days 16-23 drivers: missed_water -55, work_turns +105, sales_rev +3,264, idle_turns -60. Hands 11 vs 8, animals 12 vs 11, plants 59 vs  |
| `67924b68c4e5` | orch | crossover | **+10,454** | 8.4 | 20-0 | -16,968 | +8,588 | harvest_min 1→3, geese 0→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,927 -> final +5,568); days 16-23 drivers: sales_rev +5,449, work_turns +119, missed_water -20, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 56 vs  |
| `071d8fbb43d4` | orch | paired | **+10,446** | 8.8 | 20-0 | -15,854 | +9,717 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, labor_reserve_buffer 92→79, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +2,794); days 16-23 drivers: missed_water -45, work_turns +115, sales_rev +2,645, idle_turns -33. Hands 13 vs 8, animals 12 vs 11, plants 58 vs  |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `8d9c94322bf0` | orch | crossover | +11,437 | 6.9 | 10-0 | -6,035 | held_pass | melon_floor 0→150, harvest_min 1→3, wheat_cap 22→25, wheat_hold_days 0→1, labor_reserve_buffer 92→98, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→1, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WEEDS 1.5→4.25, ORCH_SLACK_HOUR 14→15 |
| `7ba1f29425e1` | queue | ablate:open_melons | +11,407 | 6.0 | 10-0 | -7,193 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a421574edbc1` | queue | ablate:ORCH_P_WWATER | +11,378 | 5.7 | 10-0 | -7,389 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `eba7caf2ddc3` | queue | archive_crossover:crossover_g000075_20260912-133527_1 | +11,358 | 5.3 | 10-0 | -7,298 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `f5a7c8c85384` | o15 | crossover | +11,356 | 5.3 | 10-0 | -6,700 | held_pass | harvest_min 1→3, early_hire_days 3→1, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→98, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, MAX_SHEEP 14→9, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_SLACK 6.0→7.0 |
| `8b3317022e8c` | queue | archive_crossover:crossover_g000025_20260912-205839_0 | +11,345 | 5.5 | 10-0 | -6,587 | held_pass | harvest_min 1→3, wheat_cap 22→21, wheat_water_tier 0→1, setup_capital_share 0.25→0.4, labor_reserve_buffer 92→81, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→1, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→2.5, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→15 |
| `e30359fe931f` | queue | mutate | +11,298 | 5.4 | 10-0 | -7,149 | held_pass | harvest_min 1→3, wheat_cap 22→21, wheat_water_tier 0→1, setup_capital_share 0.25→0.4, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→1, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→2.5, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→15 |
| `54fc13dbeeaf` | queue | ablate:ORCH_COMMIT | +11,242 | 5.9 | 10-0 | -6,937 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `9d05ea7e9c8a` | queue | crossover | +11,190 | 5.6 | 10-0 | -7,102 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→2.75, ORCH_SLACK_HOUR 14→15 |
| `cedac1a0d5b4` | o15 | crossover | +11,168 | 5.9 | 10-0 | -7,354 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, labor_reserve_buffer 92→82, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→35, MAX_SHEEP 14→10, OPENING_MELONS 14→12, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `896a2b024e3e` | queue | archive_crossover:crossover_g000025_20260912-184321_1 | +11,145 | 5.9 | 10-0 | -7,009 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `c7ea442d8a3d` | o15 | paired | +11,089 | 5.4 | 10-0 | -6,862 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→1, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `97ac424f27b8` | queue | archive_crossover:crossover_g000025_20260912-102645_1 | +11,079 | 5.2 | 10-0 | -7,363 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `6364d01e7479` | wide | paired | +11,072 | 5.1 | 10-0 | -6,581 | held_pass | harvest_min 1→2, min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |
| `f619488bed80` | wide | paired | +11,072 | 5.1 | 10-0 | -6,594 | held_pass | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +11,356 (`f5a7c8c85384`), n=409
- orch: best +11,437 (`8d9c94322bf0`), n=486
- queue: best +11,407 (`7ba1f29425e1`), n=549
- wide: best +11,072 (`6364d01e7479`), n=412

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +13,774 | 88 | 100 | 72 | 1850 | 20.38 | 88: +10,295 (n=3), 129: +8,573 (n=2), 89: +8,449 (n=3), 93: +7,966 (n=5), 108: +7,883 (n=3), 137: +7,282 (n=3), 85: +7,106 (n=2), 141: +6,794 (n=205), 132: +6,503 (n=29), 117: +6,480 (n=3), 124: +6,478 (n=5), 102: +6,327 (n=3), 109: +6,275 (n=64), 110: +6,165 (n=252), 86: +6,055 (n=47), 99: +5,993 (n=5), 123: +5,795 (n=2), 115: +5,793 (n=3), 96: +5,721 (n=12), 150: +5,633 (n=195), 100: +5,357 (n=899), 135: +5,245 (n=4), 107: +5,141 (n=3), 140: +5,136 (n=2), 87: +5,023 (n=5), 67: +4,927 (n=4), 104: +4,853 (n=3), 126: +4,754 (n=4), 94: +4,704 (n=22), 81: +4,662 (n=2), 68: +4,532 (n=3), 127: +4,377 (n=3), 112: +4,340 (n=4), 98: +4,100 (n=4), 50: +4,056 (n=11), 105: +3,647 (n=8), 118: +3,248 (n=2), 97: +3,205 (n=3), 148: +2,198 (n=3), 133: +1,898 (n=5), 147: +1,266 (n=2), 62: +519 (n=4), 82: -1,635 (n=2), 121: -3,479 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +13,044 | 78 | 92 | 84 | 1842 | 30.04 | 78: +9,816 (n=4), 123: +9,616 (n=2), 79: +9,486 (n=2), 45: +9,341 (n=5), 66: +9,132 (n=2), 69: +9,077 (n=2), 55: +8,751 (n=2), 102: +8,508 (n=7), 41: +8,428 (n=2), 35: +8,104 (n=25), 90: +7,608 (n=5), 132: +7,364 (n=3), 118: +7,255 (n=3), 98: +7,224 (n=20), 100: +7,204 (n=4), 86: +7,176 (n=7), 67: +6,899 (n=10), 61: +6,418 (n=5), 82: +6,343 (n=19), 81: +6,287 (n=160), 110: +6,238 (n=192), 71: +5,786 (n=2), 92: +5,618 (n=1191), 150: +5,357 (n=32), 91: +5,283 (n=5), 111: +4,920 (n=36), 57: +4,482 (n=2), 99: +4,310 (n=13), 87: +3,999 (n=2), 105: +3,892 (n=11), 119: +3,803 (n=10), 89: +3,669 (n=3), 63: +3,619 (n=3), 133: +3,298 (n=4), 96: +3,017 (n=4), 54: +2,856 (n=5), 74: +2,116 (n=2), 0: +1,824 (n=3), 141: +1,349 (n=2), 53: +1,236 (n=2), 40: +924 (n=8), 95: +745 (n=2), 106: +681 (n=3), 121: +313 (n=3), 144: +173 (n=3), 65: -1,128 (n=3), 125: -2,734 (n=4), 131: -3,228 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,842 | 2 | 3 | 4 | 1877 | 1.64 | 2: +6,323 (n=1653), 3: +1,037 (n=215), 4: -4,519 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +10,567 | 0.6 | 0.55 | 14 | 1878 | 8.53 | 0.6: +6,422 (n=373), 0.5: +6,284 (n=34), 0.55: +5,902 (n=1278), 0.65: +5,613 (n=26), 0.7: +5,350 (n=13), 0.85: +4,079 (n=5), 0.45: +4,062 (n=14), 0.4: +3,201 (n=40), 0.75: +3,041 (n=24), 1.0: +2,864 (n=2), 0.8: +2,297 (n=34), 0.35: -821 (n=6), 0.9: -2,323 (n=12), 0.3: -4,145 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,304 | 1.5 | 0.5 | 12 | 1877 | 8.0 | 1.5: +7,045 (n=7), 1.25: +6,718 (n=41), 0.25: +6,483 (n=67), 1.0: +6,182 (n=35), 0.75: +6,152 (n=20), 0.5: +5,717 (n=1535), 1.75: +5,542 (n=11), 0.0: +4,565 (n=143), 3.0: +4,444 (n=11), 2.0: +2,632 (n=2), 2.75: -3,259 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,987 | 3 | 0 | 23 | 1870 | 13.23 | 3: +9,266 (n=5), 4: +7,147 (n=3), 0: +5,843 (n=1774), 2: +5,654 (n=6), 7: +5,220 (n=7), 5: +4,145 (n=6), 9: +3,279 (n=2), 6: +3,146 (n=5), 13: +2,243 (n=2), 14: +2,146 (n=8), 10: +1,899 (n=9), 1: +1,618 (n=9), 8: +1,348 (n=9), 11: +882 (n=9), 35: -721 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +9,981 | 21 | 14 | 15 | 1878 | 8.35 | 21: +7,981 (n=3), 11: +6,698 (n=194), 15: +6,109 (n=1171), 16: +5,960 (n=18), 13: +5,632 (n=29), 19: +5,466 (n=14), 10: +5,101 (n=17), 17: +4,598 (n=7), 14: +4,431 (n=345), 9: +4,231 (n=4), 18: +4,213 (n=6), 12: +3,328 (n=30), 8: +704 (n=28), 22: +590 (n=6), 20: -1,999 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +9,610 | 10 | 14 | 9 | 1876 | 3.25 | 10: +8,798 (n=4), 12: +6,814 (n=199), 13: +6,498 (n=420), 6: +5,345 (n=31), 14: +5,318 (n=1140), 11: +3,309 (n=80), 7: -812 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +9,528 | 4.25 | 1.5 | 21 | 1878 | 10.37 | 4.25: +8,694 (n=10), 4.0: +7,569 (n=4), 2.25: +6,730 (n=16), 3.5: +6,714 (n=569), 2.5: +6,210 (n=39), 3.75: +6,142 (n=9), 0.25: +6,052 (n=4), 1.0: +5,978 (n=12), 3.0: +5,898 (n=42), 1.25: +5,873 (n=10), 1.5: +5,215 (n=1017), 4.75: +5,076 (n=10), 3.25: +5,017 (n=7), 1.75: +4,948 (n=22), 0.5: +4,675 (n=17), 2.0: +4,540 (n=14), 0.75: +4,539 (n=8), 2.75: +3,843 (n=27), 0.0: +3,745 (n=23), 4.5: +2,666 (n=8), 5.0: -834 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +9,039 | 40 | 30 | 20 | 1876 | 11.42 | 40: +7,880 (n=4), 29: +6,814 (n=21), 28: +6,573 (n=244), 26: +6,554 (n=7), 25: +6,005 (n=176), 30: +5,630 (n=1294), 27: +5,233 (n=40), 34: +5,151 (n=24), 37: +4,356 (n=9), 36: +3,222 (n=6), 38: +3,188 (n=2), 32: +2,819 (n=6), 33: +1,749 (n=5), 35: +1,582 (n=10), 31: +742 (n=14), 45: +241 (n=2), 39: -157 (n=10), 50: -1,159 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +9,025 | 17 | 17 | 11 | 1878 | 8.52 | 17: +5,808 (n=1626), 13: +5,539 (n=2), 16: +5,490 (n=141), 15: +5,124 (n=12), 18: +5,012 (n=50), 14: +4,725 (n=6), 19: +3,000 (n=17), 12: +2,900 (n=3), 20: +1,370 (n=11), 11: +1,062 (n=3), 10: -3,216 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +8,901 | 18 | 19 | 9 | 1877 | 1.88 | 18: +6,248 (n=144), 16: +6,173 (n=508), 14: +6,048 (n=15), 20: +5,415 (n=482), 19: +5,407 (n=675), 17: +5,344 (n=30), 15: +4,527 (n=20), 12: -2,653 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +8,626 | 2.25 | 0.5 | 11 | 1878 | 4.79 | 2.25: +9,029 (n=2), 0.25: +6,784 (n=493), 2.5: +5,858 (n=4), 0.0: +5,732 (n=205), 1.0: +5,519 (n=118), 0.5: +5,358 (n=988), 1.25: +3,967 (n=7), 1.5: +3,339 (n=10), 2.0: +2,812 (n=4), 1.75: +1,272 (n=33), 0.75: +404 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +8,508 | 1.5 | 1.25 | 5 | 1878 | 3.22 | 1.5: +6,069 (n=218), 1.25: +5,697 (n=1584), 0.75: +4,478 (n=11), 1.0: +4,026 (n=60), 0.5: -2,439 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +8,092 | 0.75 | 1.0 | 16 | 1877 | 5.09 | 0.75: +6,803 (n=17), 1.25: +6,698 (n=271), 0.5: +6,402 (n=32), 0.25: +6,253 (n=20), 1.5: +5,703 (n=762), 1.0: +5,369 (n=679), 2.0: +5,355 (n=17), 2.25: +4,774 (n=8), 1.75: +4,687 (n=23), 0.0: +4,452 (n=27), 3.0: +3,973 (n=2), 2.5: +2,727 (n=6), 3.25: +1,023 (n=2), 3.5: -1,181 (n=8), 4.0: -1,290 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +8,032 | frontier | frontier | 2 | 1878 | 0.85 | frontier: +6,269 (n=1735), v312: -1,762 (n=143) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,932 | 0.0 | 0.0 | 9 | 1877 | 6.6 | 0.0: +5,792 (n=1782), 0.3: +5,454 (n=13), 0.4: +3,965 (n=7), 0.2: +3,411 (n=22), 0.1: +3,338 (n=40), 0.6: +2,212 (n=4), 0.5: +1,763 (n=2), 0.7: -2,140 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,714 | 34 | 38 | 29 | 1877 | 10.38 | 34: +7,874 (n=2), 43: +7,652 (n=10), 24: +7,612 (n=8), 48: +7,331 (n=10), 50: +7,216 (n=225), 49: +7,157 (n=7), 45: +6,664 (n=4), 35: +6,251 (n=763), 22: +6,104 (n=2), 37: +6,103 (n=24), 26: +5,997 (n=59), 47: +5,720 (n=17), 41: +5,594 (n=64), 29: +5,537 (n=3), 42: +5,328 (n=5), 27: +5,158 (n=9), 44: +5,100 (n=4), 38: +4,917 (n=515), 32: +4,684 (n=17), 31: +4,610 (n=15), 20: +4,413 (n=5), 39: +4,138 (n=7), 28: +3,986 (n=9), 46: +3,492 (n=2), 40: +3,434 (n=4), 33: +1,520 (n=7), 30: +708 (n=75), 36: +160 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +7,302 | 2 | 2 | 4 | 1878 | 2.75 | 2: +5,981 (n=1761), 3: +1,209 (n=6), 1: +939 (n=103), 0: -1,321 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +7,255 | 5 | 10 | 11 | 1877 | 7.28 | 5: +6,463 (n=2), 10: +5,847 (n=1555), 9: +5,756 (n=187), 8: +5,291 (n=23), 12: +4,824 (n=18), 7: +3,433 (n=18), 11: +3,067 (n=54), 6: +2,068 (n=8), 13: +6 (n=8), 4: -792 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +11,437 (n=249)
- (9, 3, 4): +11,407 (n=342)
- (11, 3, 6): +11,356 (n=179)
- (10, 3, 5): +11,345 (n=284)
- (10, 3, 4): +11,072 (n=83)
- (11, 3, 5): +10,683 (n=239)
- (12, 3, 6): +10,547 (n=154)
- (10, 3, 6): +10,467 (n=39)
- (12, 3, 5): +10,336 (n=119)
- (9, 3, 6): +9,771 (n=18)
- (13, 3, 5): +8,853 (n=5)
- (11, 3, 4): +8,841 (n=14)
- (13, 3, 6): +8,762 (n=22)
- (14, 3, 6): +7,609 (n=19)
- (15, 3, 6): +7,459 (n=34)

_Generated 2026-09-12 22:11. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 470 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=470); harvest_min=1–3 (n=470); wheat_tiles=0–7 (n=470); wheat_stock=0–40 (n=470); min_hands=3–6 (n=470); load_per_hand=12–26 (n=470); geese=0–2 (n=470); open_melons=6–14 (n=470)
- **Evidence:** 470 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1878 candidates** with action_table data, **245906 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,708 (n=25936) |         +5,658 (n=13146) |         +5,658 (n=15024) | 54106 |
| BUY_ANIMAL |         +5,097 (n=10271) |         +5,898 (n=2223) |              — (n=0) | 12494 |
| BUY_SEED |         +5,693 (n=19131) |         +5,728 (n=7159) |         +5,193 (n=2545) | 28835 |
| BUY_LAND |         +5,715 (n=6736) |         +6,131 (n=1792) |              — (n=0) | 8528 |
| BUY_PRODUCT |         +5,658 (n=28156) |         +5,658 (n=13146) |         +5,658 (n=13143) | 54445 |
| HIRE |         +5,490 (n=11054) |         +5,510 (n=6456) |         +5,789 (n=4886) | 22396 |
| WATER_MISSED |         +5,654 (n=20932) |         +5,658 (n=13146) |         +5,659 (n=15016) | 49094 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +5,311 (n=9623) |         +5,261 (n=2425) |         +5,313 (n=3960) | 16008 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,787 |      +5,658 |      +5,715 |      +5,635 |      +5,599 |      +5,654 |
| BUY_ANIMAL |      +5,015 |           — |      +1,809 |      +5,684 |      +5,776 |      +5,175 |
| BUY_SEED |      +5,048 |      +6,406 |      -3,214 |      -3,836 |      +3,205 |      +5,744 |
| BUY_LAND |      -2,439 |      -3,354 |      +5,720 |        -945 |      +6,472 |      +5,712 |
| BUY_PRODUCT |      +5,658 |           — |           — |           — |           — |           — |
| HIRE |      +5,561 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,658 |      +2,762 |      +5,658 |      +5,689 |
| FEED_MISSED |           — |      +5,675 |      +2,891 |           — |      +1,809 |      +5,277 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +6,131 | 1792 | 1.49 |
| 2 | BUY_ANIMAL | mid | +5,898 | 2223 | 1.39 |
| 3 | HIRE | late | +5,789 | 4886 | 1.34 |
| 4 | BUY_SEED | mid | +5,728 | 7159 | 1.3 |
| 5 | BUY_LAND | early | +5,715 | 6736 | 1.3 |
| 6 | SELL | early | +5,708 | 25936 | 1.31 |
| 7 | BUY_SEED | early | +5,693 | 19131 | 1.32 |
| 8 | WATER_MISSED | late | +5,659 | 15016 | 1.29 |
| 9 | SELL | mid | +5,658 | 13146 | 1.29 |
| 10 | SELL | late | +5,658 | 15024 | 1.29 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,687 (n=940)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,679 (n=941)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +7,105 (n=1290)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +7,101 (n=1283)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +7,075 (n=1314)
- **SELL** in ('low', 'low', 'low', 'mid'): +7,033 (n=1321)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +7,018 (n=1327)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +6,624 (n=1541)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +6,448 (n=2045)
- **BUY_PRODUCT** in ('low', 'low', 'high', 'high'): +6,352 (n=1595)
- **SELL** in ('low', 'low', 'high', 'high'): +6,346 (n=1596)
- **WATER_MISSED** in ('low', 'low', 'high', 'high'): +6,346 (n=1596)
- **WATER_MISSED** in ('mid', 'low', 'high', 'mid'): +6,267 (n=1366)
- **SELL** in ('mid', 'low', 'high', 'mid'): +6,259 (n=1371)
- **FEED_MISSED** in ('mid', 'low', 'high', 'mid'): +6,259 (n=1371)

_Generated 2026-09-12 22:11. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._