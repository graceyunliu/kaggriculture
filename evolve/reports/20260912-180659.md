# Evolution run 20260912-180659

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.06 h · candidates evaluated this run: 137 · games 31,726 (15,435/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 18 | 36 |
| dead_pattern | 17 | 34 |
| dead_smoke | 3 | 24 |
| alive | 20 | 2560 |
| held_fail | 12 | 4416 |
| held_pass | 67 | 24656 |
| error | 0 | 0 |

Population (all runs, reached dev): 1777 · held-out evaluated: 1340 · held-out PASS: 1151

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
| `58b3cc435646` | orch | crossover | **+10,433** | 8.5 | 20-0 | -15,890 | +9,957 | harvest_min 1→3, min_hands 3→4, demand_share 0.55→0.6, wheat_cap 22→25, wheat_sell_price 30→28, setup_capital_share 0.25→0.1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→50, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, SPREAD_W 1.25→1.5, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +2,429 -> final +3,340); days 16-23 drivers: missed_water -44, work_turns +119, sales_rev +3,354, idle_turns -57. Hands 12 vs 8, animals 12 vs 11, plants 59 vs  |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ba1f29425e1` | queue | ablate:open_melons | +11,407 | 6.0 | 10-0 | -7,193 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a421574edbc1` | queue | ablate:ORCH_P_WWATER | +11,378 | 5.7 | 10-0 | -7,389 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `eba7caf2ddc3` | queue | archive_crossover:crossover_g000075_20260912-133527_1 | +11,358 | 5.3 | 10-0 | -7,298 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→6.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `f5a7c8c85384` | o15 | crossover | +11,356 | 5.3 | 10-0 | -6,700 | held_pass | harvest_min 1→3, early_hire_days 3→1, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→98, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, NEAR_RADIUS 2→3, MAX_SHEEP 14→9, OPENING_MELONS 14→13, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_SLACK 6.0→7.0 |
| `e30359fe931f` | queue | mutate | +11,298 | 5.4 | 10-0 | -7,149 | held_pass | harvest_min 1→3, wheat_cap 22→21, wheat_water_tier 0→1, setup_capital_share 0.25→0.4, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→1, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→2.5, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→15 |
| `54fc13dbeeaf` | queue | ablate:ORCH_COMMIT | +11,242 | 5.9 | 10-0 | -6,937 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `9d05ea7e9c8a` | queue | crossover | +11,190 | 5.6 | 10-0 | -7,102 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.1, MAX_SHEEP 14→10, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→2.75, ORCH_SLACK_HOUR 14→15 |
| `cedac1a0d5b4` | o15 | crossover | +11,168 | 5.9 | 10-0 | -7,354 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, labor_reserve_buffer 92→82, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→35, MAX_SHEEP 14→10, OPENING_MELONS 14→12, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `896a2b024e3e` | queue | archive_crossover:crossover_g000025_20260912-184321_1 | +11,145 | 5.9 | 10-0 | -7,009 | held_pass | harvest_min 1→3, min_hands 3→4, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.5, ORCH_SLACK_HOUR 14→15 |
| `c7ea442d8a3d` | o15 | paired | +11,089 | 5.4 | 10-0 | -6,862 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, MAX_HANDS 14→13, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→1, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `97ac424f27b8` | queue | archive_crossover:crossover_g000025_20260912-102645_1 | +11,079 | 5.2 | 10-0 | -7,363 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `f619488bed80` | wide | paired | +11,072 | 5.1 | 10-0 | -6,594 | held_pass | min_hands 3→4, feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→14, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, SPREAD_CAP 3→6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→1.25, ORCH_P_FERT 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_SLACK 6.0→10.0, ORCH_COMMIT 0.75→0.0 |
| `22712cc7392f` | queue | crossover | +11,071 | 6.2 | 10-0 | -7,093 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→50, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `aba9a97eaa4d` | queue | archive_crossover:crossover_g000050_20260912-151350_0 | +11,063 | 5.9 | 10-0 | -7,473 | held_pass | harvest_min 1→3, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→81, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.0, MAX_SHEEP 14→9, OPENING_MELONS 14→12, FERT_RADIUS 3→2, SPREAD_W 1.25→1.5, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.25, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→15 |
| `b2f83c7bf97d` | orch | paired | +11,033 | 6.2 | 10-0 | -6,460 | held_pass | melon_floor 0→150, harvest_min 1→3, fert_buy 3→2, wheat_cap 22→25, wheat_hold_days 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→141, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→10, OPENING_MELONS 14→13, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_SLACK_HOUR 14→11 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +11,356 (`f5a7c8c85384`), n=389
- orch: best +11,033 (`b2f83c7bf97d`), n=457
- queue: best +11,407 (`7ba1f29425e1`), n=518
- wide: best +11,072 (`f619488bed80`), n=391

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +13,774 | 88 | 100 | 69 | 1750 | 19.57 | 88: +10,295 (n=3), 129: +8,573 (n=2), 89: +8,449 (n=3), 108: +8,353 (n=2), 115: +8,034 (n=2), 93: +7,966 (n=5), 141: +6,815 (n=182), 132: +6,503 (n=29), 117: +6,480 (n=3), 124: +6,478 (n=5), 137: +6,404 (n=2), 109: +6,275 (n=64), 110: +6,144 (n=241), 86: +6,055 (n=47), 99: +5,993 (n=5), 123: +5,795 (n=2), 96: +5,721 (n=12), 150: +5,631 (n=182), 100: +5,306 (n=857), 135: +5,245 (n=4), 107: +5,141 (n=3), 140: +5,136 (n=2), 87: +5,023 (n=5), 67: +4,927 (n=4), 104: +4,853 (n=3), 102: +4,781 (n=2), 126: +4,754 (n=4), 94: +4,704 (n=22), 81: +4,662 (n=2), 68: +4,532 (n=3), 127: +4,377 (n=3), 112: +4,340 (n=4), 133: +4,178 (n=3), 50: +4,056 (n=11), 105: +3,647 (n=8), 97: +3,205 (n=3), 98: +2,983 (n=3), 148: +2,198 (n=3), 147: +1,266 (n=2), 62: +519 (n=4), 82: -1,635 (n=2), 121: -3,479 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +13,044 | 78 | 92 | 81 | 1743 | 29.71 | 78: +9,816 (n=4), 123: +9,616 (n=2), 79: +9,486 (n=2), 45: +9,341 (n=5), 66: +9,132 (n=2), 69: +9,077 (n=2), 55: +8,751 (n=2), 132: +8,639 (n=2), 41: +8,428 (n=2), 35: +8,104 (n=25), 102: +7,950 (n=5), 90: +7,608 (n=5), 118: +7,255 (n=3), 86: +7,176 (n=7), 100: +6,901 (n=3), 98: +6,852 (n=13), 67: +6,780 (n=8), 61: +6,418 (n=5), 110: +6,275 (n=185), 81: +6,141 (n=144), 82: +5,856 (n=17), 71: +5,786 (n=2), 144: +5,648 (n=2), 92: +5,599 (n=1139), 150: +5,415 (n=31), 91: +5,283 (n=5), 111: +5,040 (n=35), 89: +5,024 (n=2), 57: +4,482 (n=2), 99: +4,310 (n=13), 87: +3,999 (n=2), 105: +3,854 (n=10), 119: +3,803 (n=10), 63: +3,619 (n=3), 133: +3,298 (n=4), 96: +3,017 (n=4), 54: +2,856 (n=5), 74: +2,116 (n=2), 0: +1,824 (n=3), 141: +1,349 (n=2), 53: +1,236 (n=2), 106: +885 (n=2), 121: +313 (n=3), 40: +248 (n=7), 65: -1,128 (n=3), 125: -2,734 (n=4), 131: -3,228 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +10,834 | 2 | 3 | 4 | 1776 | 1.63 | 2: +6,315 (n=1556), 3: +1,088 (n=211), 4: -4,519 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +10,544 | 0.6 | 0.55 | 14 | 1776 | 7.89 | 0.6: +6,399 (n=354), 0.5: +6,082 (n=29), 0.55: +5,887 (n=1214), 0.65: +5,613 (n=26), 0.7: +5,350 (n=13), 0.85: +4,079 (n=5), 0.4: +3,173 (n=38), 0.45: +3,123 (n=10), 0.75: +2,688 (n=21), 0.8: +2,234 (n=32), 0.35: -313 (n=5), 0.9: -2,323 (n=12), 0.3: -4,145 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +10,304 | 1.5 | 0.5 | 12 | 1776 | 8.0 | 1.5: +7,045 (n=7), 1.25: +6,588 (n=35), 0.25: +6,460 (n=64), 1.0: +6,166 (n=31), 0.75: +6,152 (n=20), 0.5: +5,705 (n=1453), 1.75: +5,542 (n=11), 0.0: +4,463 (n=137), 3.0: +4,444 (n=11), 2.0: +2,632 (n=2), 2.75: -3,259 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,987 | 3 | 0 | 23 | 1769 | 13.24 | 3: +9,266 (n=5), 4: +8,585 (n=2), 2: +6,222 (n=5), 0: +5,823 (n=1679), 7: +4,338 (n=6), 9: +3,279 (n=2), 5: +3,229 (n=5), 6: +3,146 (n=5), 13: +2,243 (n=2), 1: +2,240 (n=8), 10: +1,899 (n=9), 8: +1,348 (n=9), 14: +1,234 (n=7), 11: +882 (n=9), 35: -721 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +9,658 | 10 | 14 | 9 | 1775 | 3.44 | 10: +8,847 (n=3), 12: +6,759 (n=155), 13: +6,529 (n=383), 14: +5,331 (n=1126), 6: +5,311 (n=29), 11: +3,419 (n=77), 7: -812 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +9,039 | 40 | 30 | 20 | 1775 | 11.33 | 40: +7,880 (n=4), 26: +7,486 (n=6), 29: +6,814 (n=21), 28: +6,587 (n=227), 25: +6,015 (n=174), 30: +5,595 (n=1216), 27: +5,233 (n=40), 34: +5,151 (n=24), 37: +4,356 (n=9), 38: +3,188 (n=2), 32: +2,819 (n=6), 36: +2,756 (n=5), 33: +1,749 (n=5), 35: +1,582 (n=10), 45: +241 (n=2), 31: -79 (n=12), 39: -157 (n=10), 50: -1,159 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +8,998 | 17 | 17 | 11 | 1776 | 7.65 | 17: +5,782 (n=1536), 15: +5,649 (n=10), 13: +5,539 (n=2), 16: +5,470 (n=138), 18: +5,046 (n=48), 14: +4,042 (n=5), 19: +2,873 (n=16), 20: +1,370 (n=11), 11: +1,062 (n=3), 10: -3,216 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +8,963 | 21 | 14 | 15 | 1777 | 8.37 | 21: +6,964 (n=2), 11: +6,692 (n=183), 15: +6,083 (n=1110), 16: +5,928 (n=17), 13: +5,662 (n=28), 10: +5,101 (n=17), 19: +5,056 (n=13), 14: +4,431 (n=324), 9: +4,231 (n=4), 18: +4,213 (n=6), 17: +3,743 (n=6), 12: +3,540 (n=29), 22: +590 (n=6), 8: +377 (n=26), 20: -1,999 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +8,879 | 18 | 19 | 9 | 1776 | 1.81 | 18: +6,226 (n=137), 16: +6,190 (n=503), 14: +6,048 (n=15), 17: +5,504 (n=29), 20: +5,445 (n=445), 19: +5,270 (n=624), 15: +4,527 (n=20), 12: -2,653 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +8,779 | 4.25 | 1.5 | 21 | 1777 | 10.5 | 4.25: +7,945 (n=2), 4.0: +7,569 (n=4), 2.25: +6,836 (n=14), 3.5: +6,727 (n=541), 3.75: +6,530 (n=8), 0.25: +6,052 (n=4), 1.0: +5,978 (n=12), 2.5: +5,935 (n=33), 3.0: +5,898 (n=42), 1.25: +5,873 (n=10), 4.75: +5,609 (n=9), 1.5: +5,223 (n=973), 3.25: +5,017 (n=7), 2.0: +4,844 (n=11), 1.75: +4,768 (n=21), 0.5: +4,613 (n=16), 0.75: +4,539 (n=8), 0.0: +3,620 (n=22), 2.75: +2,655 (n=23), 4.5: +1,657 (n=7), 5.0: -834 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +8,626 | 2.25 | 0.5 | 11 | 1777 | 4.87 | 2.25: +9,029 (n=2), 0.25: +6,780 (n=440), 2.5: +5,858 (n=4), 0.0: +5,684 (n=199), 1.0: +5,510 (n=116), 0.5: +5,366 (n=949), 1.25: +3,967 (n=7), 1.5: +3,339 (n=10), 2.0: +2,812 (n=4), 1.75: +1,290 (n=32), 0.75: +404 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +8,504 | 1.5 | 1.25 | 5 | 1777 | 3.25 | 1.5: +6,064 (n=194), 1.25: +5,667 (n=1509), 0.75: +4,478 (n=11), 1.0: +4,170 (n=58), 0.5: -2,439 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +8,438 | 0.75 | 1.0 | 16 | 1775 | 4.9 | 0.75: +7,149 (n=15), 0.25: +6,826 (n=19), 1.25: +6,558 (n=241), 0.5: +6,390 (n=31), 1.5: +5,682 (n=748), 1.0: +5,368 (n=632), 2.0: +5,355 (n=17), 1.75: +5,040 (n=21), 2.25: +4,774 (n=8), 0.0: +4,335 (n=24), 3.0: +3,973 (n=2), 2.5: +2,727 (n=6), 3.5: -1,181 (n=8), 4.0: -1,290 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,992 | frontier | frontier | 2 | 1777 | 0.85 | frontier: +6,225 (n=1645), v312: -1,767 (n=132) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +7,911 | 0.0 | 0.0 | 9 | 1776 | 6.59 | 0.0: +5,771 (n=1684), 0.3: +5,617 (n=11), 0.4: +3,965 (n=7), 0.2: +3,411 (n=22), 0.1: +3,246 (n=39), 0.6: +2,212 (n=4), 0.5: +1,763 (n=2), 0.7: -2,140 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,714 | 34 | 38 | 29 | 1776 | 10.48 | 34: +7,874 (n=2), 43: +7,652 (n=10), 24: +7,612 (n=8), 48: +7,331 (n=10), 50: +7,258 (n=191), 49: +7,157 (n=7), 37: +6,834 (n=22), 47: +6,266 (n=15), 35: +6,232 (n=728), 22: +6,104 (n=2), 26: +6,042 (n=57), 20: +5,962 (n=4), 45: +5,868 (n=3), 41: +5,554 (n=62), 29: +5,537 (n=3), 42: +5,328 (n=5), 27: +5,158 (n=9), 44: +5,100 (n=4), 38: +4,864 (n=497), 31: +4,610 (n=15), 32: +4,600 (n=16), 39: +4,235 (n=6), 28: +3,986 (n=9), 46: +3,492 (n=2), 40: +3,434 (n=4), 33: +1,520 (n=7), 30: +796 (n=73), 36: +160 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +7,278 | 2 | 2 | 4 | 1777 | 2.74 | 2: +5,957 (n=1663), 3: +1,209 (n=6), 1: +1,035 (n=100), 0: -1,321 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +7,255 | 5 | 10 | 11 | 1776 | 7.22 | 5: +6,463 (n=2), 9: +5,897 (n=182), 10: +5,804 (n=1460), 8: +5,291 (n=23), 12: +4,824 (n=18), 7: +3,433 (n=18), 11: +3,158 (n=53), 6: +2,068 (n=8), 13: +6 (n=8), 4: -792 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 4): +11,407 (n=320)
- (9, 3, 5): +11,378 (n=234)
- (11, 3, 6): +11,356 (n=166)
- (10, 3, 5): +11,298 (n=272)
- (10, 3, 4): +11,072 (n=77)
- (11, 3, 5): +10,683 (n=227)
- (10, 3, 6): +10,467 (n=39)
- (12, 3, 5): +10,336 (n=110)
- (12, 3, 6): +10,109 (n=150)
- (9, 3, 6): +9,771 (n=18)
- (13, 3, 5): +8,853 (n=5)
- (11, 3, 4): +8,841 (n=14)
- (13, 3, 6): +8,762 (n=21)
- (14, 3, 6): +7,609 (n=18)
- (15, 3, 6): +7,459 (n=31)

_Generated 2026-09-12 20:10. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 445 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=445); harvest_min=1–3 (n=445); wheat_tiles=0–7 (n=445); wheat_stock=0–40 (n=445); min_hands=3–6 (n=445); load_per_hand=12–26 (n=445); geese=0–2 (n=445); open_melons=6–14 (n=445)
- **Evidence:** 445 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**1777 candidates** with action_table data, **232794 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +5,681 (n=24539) |         +5,631 (n=12439) |         +5,631 (n=14216) | 51194 |
| BUY_ANIMAL |         +5,079 (n=9724) |         +5,882 (n=2113) |              — (n=0) | 11837 |
| BUY_SEED |         +5,665 (n=18115) |         +5,700 (n=6791) |         +5,188 (n=2413) | 27319 |
| BUY_LAND |         +5,687 (n=6377) |         +6,100 (n=1698) |              — (n=0) | 8075 |
| BUY_PRODUCT |         +5,631 (n=26641) |         +5,631 (n=12439) |         +5,631 (n=12436) | 51516 |
| HIRE |         +5,459 (n=10470) |         +5,485 (n=6122) |         +5,759 (n=4634) | 21226 |
| WATER_MISSED |         +5,628 (n=19818) |         +5,631 (n=12439) |         +5,632 (n=14208) | 46465 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +5,299 (n=9107) |         +5,267 (n=2304) |         +5,287 (n=3751) | 15162 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +5,759 |      +5,631 |      +5,685 |      +5,604 |      +5,570 |      +5,628 |
| BUY_ANIMAL |      +4,998 |           — |      +1,809 |      +5,602 |      +5,749 |      +5,161 |
| BUY_SEED |      +5,042 |      +6,366 |      -3,093 |      -3,836 |      +3,180 |      +5,716 |
| BUY_LAND |      -2,439 |      -3,354 |      +5,697 |        -779 |      +6,425 |      +5,689 |
| BUY_PRODUCT |      +5,631 |           — |           — |           — |           — |           — |
| HIRE |      +5,532 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +5,631 |      +2,872 |      +5,631 |      +5,661 |
| FEED_MISSED |           — |      +5,650 |      +2,967 |           — |      +1,809 |      +5,266 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +6,100 | 1698 | 1.49 |
| 2 | BUY_ANIMAL | mid | +5,882 | 2113 | 1.39 |
| 3 | HIRE | late | +5,759 | 4634 | 1.34 |
| 4 | BUY_SEED | mid | +5,700 | 6791 | 1.3 |
| 5 | BUY_LAND | early | +5,687 | 6377 | 1.3 |
| 6 | SELL | early | +5,681 | 24539 | 1.31 |
| 7 | BUY_SEED | early | +5,665 | 18115 | 1.31 |
| 8 | WATER_MISSED | late | +5,632 | 14208 | 1.29 |
| 9 | SELL | mid | +5,631 | 12439 | 1.29 |
| 10 | SELL | late | +5,631 | 14216 | 1.29 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **SELL** in ('low', 'mid', 'mid', 'mid'): +7,648 (n=892)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +7,640 (n=893)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +7,077 (n=1214)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +7,074 (n=1207)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +7,045 (n=1237)
- **SELL** in ('low', 'low', 'low', 'mid'): +7,002 (n=1243)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +6,986 (n=1249)
- **BUY_SEED** in ('low', 'low', 'high', 'high'): +6,585 (n=1457)
- **BUY_LAND** in ('mid', 'high', 'high', 'high'): +6,401 (n=1950)
- **BUY_PRODUCT** in ('low', 'low', 'high', 'high'): +6,319 (n=1509)
- **SELL** in ('low', 'low', 'high', 'high'): +6,312 (n=1510)
- **WATER_MISSED** in ('low', 'low', 'high', 'high'): +6,312 (n=1510)
- **WATER_MISSED** in ('mid', 'low', 'high', 'mid'): +6,240 (n=1291)
- **SELL** in ('mid', 'low', 'high', 'mid'): +6,232 (n=1296)
- **FEED_MISSED** in ('mid', 'low', 'high', 'mid'): +6,232 (n=1296)

_Generated 2026-09-12 20:10. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._