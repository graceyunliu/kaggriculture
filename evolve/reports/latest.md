# Evolution run 20260911-132004

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.06 h · candidates evaluated this run: 124 · games 31,724 (15,371/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 10 | 20 |
| dead_pattern | 8 | 16 |
| dead_smoke | 3 | 24 |
| alive | 26 | 3328 |
| held_fail | 7 | 2576 |
| held_pass | 70 | 25760 |
| error | 0 | 0 |

Population (all runs, reached dev): 430 · held-out evaluated: 272 · held-out PASS: 244

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
| `446bcf7935c1` | queue | mutate | **+10,239** | 6.1 | 19-1 | -16,457 | +7,512 | melon_floor 0→100, open_melons 10→9, open_cows 2→1, open_sheep 2→3, wheat_cap 22→25, labor_reserve_buffer 92→118, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→115, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_P_SLACK 6.0→7.0, ORCH_COMMIT 0.75→0.25, ORCH_SLACK_HOUR 14→16 |  | cand pulls ahead of C1 from day 18 (gap +1,811 -> final +6,371); days 16-23 drivers: missed_water -35, sales_rev +5,930, work_turns +109, feed_hour -1.68. Hands 12 vs 8, animals 11 vs 11, plants 58 vs |
| `d7eec7135f06` | queue | mutate | **+10,140** | 7.2 | 19-1 | -16,966 | +8,831 | melon_floor 0→100, harvest_min 1→3, geese 0→2, wheat_cap 22→23, wheat_water_tier 0→1, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→5, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→94, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 18 (gap +1,640 -> final +6,963); days 16-23 drivers: sales_rev +5,689, work_turns +140, missed_water -12, idle_turns -23. Hands 12 vs 8, animals 12 vs 11, plants 57 vs  |
| `369ac717437c` | queue | mutate | **+10,014** | 8.0 | 20-0 | -16,804 | +9,070 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, CROP_SWEEP_RADIUS -91, STRAW_CUTOFF ?, MELON_PRICE_CUSHION ?, FERT_RADIUS ? | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `fb4e3411021e` | queue | ablate:CROP_SWEEP_RADIUS | **+9,894** | 8.1 | 20-0 | -16,815 | +9,160 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `a141ecf7c8cc` | wide | crossover | **+9,789** | 7.6 | 20-0 | -16,435 | +10,071 | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |  | cand pulls ahead of C1 from day 16 (gap +1,841 -> final +5,832); days 14-21 drivers: missed_water -31, work_turns +112, sales_rev +2,171, idle_turns -34. Hands 11 vs 8, animals 11 vs 11, plants 60 vs  |
| `054925826fd0` | orch | crossover | **+9,643** | 9.0 | 20-0 | -16,486 | +8,658 | melon_floor 0→100, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→105, OPP_GROWTH 1.4→1.6, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.25, ORCH_P_PLANT 1.0→2.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→10 |  | cand pulls ahead of C1 from day 16 (gap +1,962 -> final +4,469); days 14-21 drivers: work_turns +109, missed_water -20, sales_rev +2,405, idle_turns -57. Hands 11 vs 8, animals 11 vs 11, plants 58 vs  |
| `94a200092138` | queue | crossover | **+9,642** | 10.8 | 20-0 | -16,617 | +8,905 | early_hire_days 3→2, max_animals 17→18, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→18, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→1.25, ORCH_P_SLACK 6.0→5.0, ORCH_SLACK_HOUR 14→13 |  | cand pulls ahead of C1 from day 16 (gap +2,440 -> final +10,248); days 14-21 drivers: missed_water -29, work_turns +71, idle_turns -63, feed_hour -1.54. Hands 9 vs 8, animals 9 vs 11, plants 65 vs 57. |
| `4a249e017ed5` | queue | crossover | **+9,487** | 7.0 | 20-0 | -17,366 | +7,755 | melon_floor 0→150, harvest_min 1→2, open_melons 10→11, fert_carry 2→1, wheat_cap 22→25, MAX_HANDS 14→13, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→86, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→2.0 |  | cand pulls ahead of C1 from day 11 (gap +2,635 -> final +6,495); days 9-16 drivers: sales_rev +3,408, missed_water -13, work_turns +38, idle_turns -32. Hands 10 vs 12, animals 11 vs 11, plants 59 vs 6 |
| `76bd5c416c98` | orch | mutate | **+9,481** | 7.0 | 19-1 | -17,906 | +7,838 | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, open_melons 10→12, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 11 (gap +3,754 -> final +9,184); days 9-16 drivers: missed_water -29, sales_rev +3,141, feed_hour -1.58, weeds_new -1. Hands 8 vs 12, animals 9 vs 11, plants 59 vs 60. |
| `03259b4d97b8` | queue | crossover | **+9,449** | 10.4 | 20-0 | -16,079 | +8,751 | wheat_cap 22→23, labor_reserve_buffer 92→119, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→87, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5 |  | cand pulls ahead of C1 from day 16 (gap +2,491 -> final +10,314); days 14-21 drivers: missed_water -14, idle_turns -55, sales_rev +2,074, work_turns +47. Hands 9 vs 8, animals 9 vs 11, plants 62 vs 57 |
| `480286010979` | queue | crossover | **+9,415** | 7.0 | 20-0 | -16,888 | +7,085 | melon_floor 0→150, geese 0→1, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→18, OPP_GROWTH 1.4→1.0, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.75, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 17 (gap +1,682 -> final +6,385); days 15-22 drivers: sales_rev +5,156, missed_water -20, work_turns +93, feed_hour -1.49. Hands 14 vs 14, animals 12 vs 11, plants 59 vs |
| `9f2856d00c56` | orch | crossover | **+9,406** | 9.1 | 20-0 | -16,316 | +9,116 | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | harvest_min ?, OPP_GROWTH ? | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,791); days 14-21 drivers: missed_water -17, work_turns +72, idle_turns -53, sales_rev +732. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `c7c22656484a` | wide | paired | **+9,405** | 9.2 | 20-0 | -16,802 | +8,776 | melon_floor 0→150, early_hire_days 3→1, fert_keep 0→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→132, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,009 -> final +7,883); days 14-21 drivers: missed_water -20, work_turns +89, idle_turns -49, sales_rev +387. Hands 10 vs 8, animals 10 vs 11, plants 60 vs 57. |
| `cfedf9caf279` | orch | ablate:load_per_hand | **+9,389** | 9.3 | 20-0 | -20,989 | +9,210 | melon_floor 0→150, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,797); days 14-21 drivers: missed_water -19, work_turns +74, idle_turns -53, sales_rev +738. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `a141ecf7c8cc` | wide | crossover | +10,071 | 5.8 | 10-0 | -6,073 | held_pass | feed_spare_poor 0→2, demand_share 0.55→0.6, wheat_cap 22→21, wheat_water_tier 0→1, wheat_sell_price 30→28, labor_reserve_buffer 92→110, MAX_HANDS 14→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, NEAR_RADIUS 2→3, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0 |
| `933e21488445` | orch | paired | +10,055 | 7.6 | 10-0 | -6,750 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, NEAR_RADIUS 2→3, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, SPREAD_CAP 3→4, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `cbeff72fd1ca` | queue | ablate:ORCH_SLACK_HOUR | +9,946 | 6.0 | 10-0 | -7,031 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a9e2da40d2b1` | orch | ablate:open_cows | +9,761 | 5.3 | 10-0 | -7,117 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `2bcc9334a840` | orch | migrate | +9,696 | 5.3 | 10-0 | -13,946 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `249c9825c232` | wide | block_pair | +9,635 | 6.9 | 10-0 | -6,448 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `25f7a412756d` | orch | mutate | +9,594 | 5.2 | 10-0 | -7,384 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, setup_capital_share 0.25→0.5, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_SLACK_HOUR 14→15 |
| `d5885e3a3a52` | queue | archive_crossover:crossover_g000050_20260911-122309_0 | +9,545 | 5.5 | 10-0 | -8,447 | held_pass | harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `20aecc07a779` | orch | migrate | +9,540 | 6.6 | 10-0 | -6,904 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `72888332678b` | queue | mutate | +9,517 | 6.0 | 10-0 | -8,678 | held_pass | harvest_min 1→2, wheat_cap 22→25, wheat_sell_price 30→34, setup_capital_share 0.25→0.2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, CROP_SWEEP_RADIUS 5→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→0.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→1.0 |
| `b40c471ca6c0` | queue | archive_crossover:crossover_g000025_20260911-115603_1 | +9,495 | 7.9 | 10-0 | -6,630 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `e16636629475` | queue | ablate:wheat_sell_price | +9,476 | 5.6 | 10-0 | -8,575 | held_pass | harvest_min 1→2, wheat_cap 22→25, wheat_sell_price 30→34, setup_capital_share 0.25→0.2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→0.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→1.0, ORCH_SLACK_HOUR 14→15 |
| `348945b7a860` | o15 | migrate | +9,471 | 5.1 | 10-0 | -8,209 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, early_hire_days 3→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→7.0, ORCH_SLACK_HOUR 14→15 |
| `e5a16e1feca0` | queue | archive_crossover:crossover_g000125_20260911-002105_0 | +9,455 | 5.6 | 10-0 | -8,515 | held_pass | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→132, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `74bed543643f` | wide | paired | +9,438 | 7.3 | 10-0 | -6,384 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→132, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +9,471 (`348945b7a860`), n=70
- orch: best +10,055 (`933e21488445`), n=118
- queue: best +9,946 (`cbeff72fd1ca`), n=128
- wide: best +10,071 (`a141ecf7c8cc`), n=92

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +11,706 | 132 | 92 | 25 | 419 | 10.69 | 132: +8,639 (n=2), 119: +7,669 (n=5), 99: +7,079 (n=3), 111: +5,342 (n=20), 81: +5,199 (n=13), 63: +3,619 (n=3), 92: +3,611 (n=350), 110: +3,302 (n=6), 54: +2,856 (n=5), 82: +2,781 (n=2), 96: +1,931 (n=3), 125: -1,050 (n=3), 121: -1,255 (n=2), 150: -3,067 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,211 | 17 | 20 | 11 | 428 | 5.9 | 17: +6,766 (n=5), 18: +4,850 (n=64), 19: +4,226 (n=7), 20: +3,535 (n=328), 22: +2,737 (n=4), 16: +2,566 (n=4), 21: +2,285 (n=12), 14: -2,284 (n=2), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,785 | 0.55 | 0.55 | 11 | 428 | 7.14 | 0.55: +3,910 (n=387), 0.6: +3,071 (n=15), 0.8: +2,881 (n=6), 0.5: +2,811 (n=5), 0.7: +1,886 (n=3), 0.65: +153 (n=4), 0.4: +126 (n=2), 0.45: -1,525 (n=3), 0.3: -5,876 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +9,102 | 2 | 0 | 13 | 425 | 6.23 | 2: +8,459 (n=3), 0: +3,968 (n=384), 1: +3,843 (n=4), 7: +3,007 (n=2), 11: +899 (n=6), 10: +616 (n=6), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +8,892 | 4 | 3 | 7 | 429 | 3.59 | 4: +5,944 (n=8), 1: +4,218 (n=71), 3: +3,632 (n=328), 2: +1,935 (n=12), 0: +1,271 (n=8), 6: -2,947 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_SLACK | +8,723 | 3.5 | 6.0 | 12 | 430 | 8.01 | 3.5: +8,211 (n=2), 4.0: +6,744 (n=3), 9.5: +6,703 (n=7), 5.0: +5,597 (n=13), 7.5: +4,682 (n=4), 7.0: +4,448 (n=58), 5.5: +4,310 (n=6), 8.0: +3,779 (n=8), 6.0: +3,330 (n=323), 6.5: +3,091 (n=2), 2.0: +2,182 (n=2), 8.5: -512 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,119 | 17 | 22 | 10 | 429 | 5.55 | 17: +7,947 (n=2), 25: +4,522 (n=312), 23: +3,756 (n=22), 9: +3,620 (n=3), 24: +3,279 (n=4), 21: +2,938 (n=13), 12: +2,652 (n=2), 20: +942 (n=4), 22: -172 (n=67) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +8,112 | 2 | 3 | 4 | 430 | 2.13 | 2: +5,599 (n=79), 3: +3,340 (n=337), 1: +1,638 (n=10), 4: -2,513 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +7,962 | 0.75 | 0.5 | 7 | 427 | 2.52 | 0.75: +5,919 (n=2), 0.0: +4,054 (n=47), 0.5: +3,635 (n=376), 1.0: -2,044 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +7,849 | 0.5 | 0.25 | 8 | 430 | 6.01 | 0.5: +5,903 (n=9), 0.2: +5,308 (n=18), 0.35: +4,488 (n=3), 0.25: +3,674 (n=377), 0.3: +1,993 (n=15), 0.45: +1,670 (n=2), 0.4: -553 (n=4), 0.15: -1,945 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +7,516 | 19 | 14 | 14 | 429 | 5.7 | 19: +6,690 (n=3), 13: +5,461 (n=8), 16: +5,121 (n=5), 15: +4,595 (n=221), 10: +4,284 (n=9), 11: +3,856 (n=9), 12: +3,501 (n=14), 14: +2,513 (n=135), 22: +2,182 (n=2), 17: +1,989 (n=2), 8: +212 (n=17), 20: +26 (n=2), 18: -826 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,456 | 28 | 30 | 13 | 428 | 7.82 | 28: +7,179 (n=6), 26: +6,892 (n=2), 27: +5,343 (n=27), 37: +4,645 (n=3), 34: +4,226 (n=15), 35: +4,044 (n=4), 25: +3,846 (n=16), 30: +3,531 (n=343), 29: +927 (n=3), 32: +411 (n=2), 31: -278 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,117 | frontier | frontier | 2 | 430 | 0.83 | frontier: +4,274 (n=393), v312: -2,843 (n=37) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +6,456 | 1.25 | 1.5 | 18 | 425 | 8.54 | 1.25: +7,854 (n=6), 3.0: +6,666 (n=15), 4.0: +5,616 (n=2), 3.5: +5,529 (n=57), 2.5: +3,786 (n=2), 3.25: +3,698 (n=3), 1.5: +3,224 (n=312), 2.0: +2,778 (n=2), 0.5: +2,701 (n=4), 2.75: +2,513 (n=9), 0.0: +2,443 (n=8), 5.0: +1,670 (n=2), 1.75: +1,398 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,237 | 24 | 38 | 20 | 420 | 4.02 | 24: +6,542 (n=3), 41: +6,121 (n=22), 26: +5,183 (n=18), 35: +5,151 (n=95), 31: +4,579 (n=10), 50: +3,372 (n=6), 38: +3,370 (n=211), 28: +1,280 (n=3), 39: +915 (n=2), 30: +305 (n=50) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +6,215 | 110 | 100 | 29 | 414 | 8.01 | 110: +6,734 (n=12), 135: +6,542 (n=3), 132: +5,571 (n=7), 109: +4,970 (n=15), 67: +4,927 (n=4), 86: +4,545 (n=15), 87: +4,376 (n=4), 105: +4,150 (n=7), 150: +3,898 (n=47), 94: +3,620 (n=7), 100: +3,249 (n=287), 104: +2,769 (n=2), 62: +519 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +6,190 | 2 | 2 | 4 | 429 | 1.57 | 2: +4,292 (n=368), 1: -123 (n=58), 0: -1,897 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +5,690 | 9 | 14 | 8 | 428 | 4.36 | 9: +5,505 (n=2), 13: +4,813 (n=37), 14: +3,622 (n=382), 12: +2,293 (n=2), 8: +1,670 (n=2), 11: -186 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,618 | 8 | 10 | 8 | 429 | 4.4 | 8: +5,494 (n=7), 9: +5,435 (n=48), 12: +3,970 (n=2), 10: +3,635 (n=331), 11: +2,155 (n=27), 7: +155 (n=7), 13: -124 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_FERT | +5,536 | 1.0 | 0.5 | 9 | 430 | 5.01 | 1.0: +5,501 (n=86), 1.5: +5,397 (n=3), 0.75: +3,698 (n=31), 0.25: +3,552 (n=10), 0.5: +3,224 (n=287), 1.75: +2,001 (n=3), 2.0: +1,199 (n=3), 0.0: -15 (n=5), 1.25: -35 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (11, 3, 5): +10,071 (n=77)
- (11, 3, 6): +10,055 (n=52)
- (9, 3, 5): +9,946 (n=56)
- (10, 3, 5): +9,696 (n=72)
- (9, 3, 4): +9,402 (n=102)
- (10, 3, 6): +9,276 (n=3)
- (12, 3, 5): +9,160 (n=13)
- (11, 3, 4): +8,559 (n=3)
- (12, 3, 6): +7,522 (n=22)
- (15, 3, 6): +6,377 (n=3)
- (10, 3, 4): +5,361 (n=10)
- (14, 3, 6): +5,342 (n=3)
- (8, 3, 4): +1,764 (n=1)
- (13, 3, 5): +1,174 (n=2)
- (13, 3, 6): +950 (n=5)

_Generated 2026-09-11 15:24. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 103 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=103); harvest_min=1–3 (n=103); wheat_tiles=0–7 (n=103); wheat_stock=0–40 (n=103); min_hands=3–6 (n=103); load_per_hand=12–26 (n=103); geese=0–2 (n=103); open_melons=7–14 (n=103)
- **Evidence:** 103 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**430 candidates** with action_table data, **56853 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +3,718 (n=5926) |         +3,661 (n=3010) |         +3,661 (n=3440) | 12376 |
| BUY_ANIMAL |         +3,215 (n=2460) |         +3,919 (n=521) |              — (n=0) | 2981 |
| BUY_SEED |         +3,718 (n=4425) |         +3,785 (n=1645) |         +3,295 (n=611) | 6681 |
| BUY_LAND |         +3,603 (n=1515) |         +4,218 (n=414) |              — (n=0) | 1929 |
| BUY_PRODUCT |         +3,661 (n=6448) |         +3,661 (n=3010) |         +3,661 (n=3010) | 12468 |
| HIRE |         +3,541 (n=2652) |         +3,501 (n=1490) |         +3,808 (n=1128) | 5270 |
| WATER_MISSED |         +3,666 (n=4826) |         +3,661 (n=3010) |         +3,659 (n=3438) | 11274 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +3,388 (n=2260) |         +3,219 (n=617) |         +3,096 (n=997) | 3874 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +3,800 |      +3,661 |      +3,716 |      +3,778 |      +3,629 |      +3,646 |
| BUY_ANIMAL |      +3,072 |           — |           — |      +4,111 |      +3,783 |      +3,308 |
| BUY_SEED |      +3,157 |      +4,527 |      -3,985 |           — |      +2,229 |      +3,763 |
| BUY_LAND |      -1,073 |      -3,120 |      +3,733 |      -2,321 |      +4,357 |      +3,619 |
| BUY_PRODUCT |      +3,661 |           — |           — |           — |           — |           — |
| HIRE |      +3,587 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +3,661 |      +1,820 |      +3,661 |      +3,692 |
| FEED_MISSED |           — |      +3,650 |      +2,220 |           — |           — |      +3,259 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +4,218 | 414 | 1.06 |
| 2 | BUY_ANIMAL | mid | +3,919 | 521 | 0.94 |
| 3 | HIRE | late | +3,808 | 1128 | 0.93 |
| 4 | BUY_SEED | mid | +3,785 | 1645 | 0.89 |
| 5 | SELL | early | +3,718 | 5926 | 0.9 |
| 6 | BUY_SEED | early | +3,718 | 4425 | 0.9 |
| 7 | WATER_MISSED | early | +3,666 | 4826 | 0.88 |
| 8 | SELL | mid | +3,661 | 3010 | 0.88 |
| 9 | SELL | late | +3,661 | 3440 | 0.88 |
| 10 | BUY_PRODUCT | early | +3,661 | 6448 | 0.88 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +6,257 (n=30)
- **SELL** in ('low', 'mid', 'mid', 'mid'): +6,007 (n=135)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +6,007 (n=135)
- **WATER_MISSED** in ('low', 'high', 'high', 'high'): -5,923 (n=14)
- **SELL** in ('low', 'high', 'high', 'high'): -5,859 (n=15)
- **BUY_PRODUCT** in ('low', 'high', 'high', 'high'): -5,859 (n=15)
- **HIRE** in ('low', 'high', 'high', 'high'): -5,540 (n=10)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +5,535 (n=38)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +5,535 (n=38)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +5,359 (n=215)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +5,349 (n=218)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +5,319 (n=224)
- **SELL** in ('low', 'low', 'low', 'mid'): +5,203 (n=228)
- **BUY_PRODUCT** in ('low', 'low', 'low', 'mid'): +5,150 (n=230)
- **BUY_LAND** in ('high', 'mid', 'high', 'high'): +5,143 (n=7)

_Generated 2026-09-11 15:24. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._