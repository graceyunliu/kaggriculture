# Evolution run 20260911-111843

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_feeltheagi_107564195.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.00 h · candidates evaluated this run: 133 · games 31,010 (15,497/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 23 | 46 |
| dead_pattern | 6 | 12 |
| dead_smoke | 5 | 40 |
| alive | 23 | 2944 |
| held_fail | 8 | 2944 |
| held_pass | 68 | 25024 |
| error | 0 | 0 |

Population (all runs, reached dev): 327 · held-out evaluated: 195 · held-out PASS: 174

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
| `369ac717437c` | queue | mutate | **+10,014** | 8.0 | 20-0 | -16,804 | +9,070 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→4, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | geese ?, wheat_cap ?, CROP_SWEEP_RADIUS -91, STRAW_CUTOFF ?, MELON_PRICE_CUSHION ?, FERT_RADIUS ? | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `fb4e3411021e` | queue | ablate:CROP_SWEEP_RADIUS | **+9,894** | 8.1 | 20-0 | -16,815 | +9,160 | harvest_min 1→2, geese 0→2, wheat_cap 22→23, ROUTE_LEN 3→2, STRAW_CUTOFF 19→15, MELON_PRICE_CUSHION 100→94, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 17 (gap +1,983 -> final +6,074); days 15-22 drivers: sales_rev +5,172, missed_water -24, work_turns +86, idle_turns -46. Hands 13 vs 14, animals 12 vs 11, plants 60 vs  |
| `054925826fd0` | orch | crossover | **+9,643** | 9.0 | 20-0 | -16,486 | +8,658 | melon_floor 0→100, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_PRICE_CUSHION 100→105, OPP_GROWTH 1.4→1.6, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.25, ORCH_P_PLANT 1.0→2.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→10 |  | cand pulls ahead of C1 from day 16 (gap +1,962 -> final +4,469); days 14-21 drivers: work_turns +109, missed_water -20, sales_rev +2,405, idle_turns -57. Hands 11 vs 8, animals 11 vs 11, plants 58 vs  |
| `4a249e017ed5` | queue | crossover | **+9,487** | 7.0 | 20-0 | -17,366 | +7,755 | melon_floor 0→150, harvest_min 1→2, open_melons 10→11, fert_carry 2→1, wheat_cap 22→25, MAX_HANDS 14→13, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→86, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→2.0 |  | cand pulls ahead of C1 from day 11 (gap +2,635 -> final +6,495); days 9-16 drivers: sales_rev +3,408, missed_water -13, work_turns +38, idle_turns -32. Hands 10 vs 12, animals 11 vs 11, plants 59 vs 6 |
| `76bd5c416c98` | orch | mutate | **+9,481** | 7.0 | 19-1 | -17,906 | +7,838 | melon_floor 0→150, harvest_min 1→2, min_hands 3→4, open_melons 10→12, wheat_cap 22→25, wheat_sell_price 30→28, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 11 (gap +3,754 -> final +9,184); days 9-16 drivers: missed_water -29, sales_rev +3,141, feed_hour -1.58, weeds_new -1. Hands 8 vs 12, animals 9 vs 11, plants 59 vs 60. |
| `03259b4d97b8` | queue | crossover | **+9,449** | 10.4 | 20-0 | -16,079 | +8,751 | wheat_cap 22→23, labor_reserve_buffer 92→119, MAX_HANDS 14→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, CROP_SWEEP_RADIUS 5→6, MELON_PRICE_CUSHION 100→87, OPP_GROWTH 1.4→1.2, OPENING_MELONS 14→13, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5 |  | cand pulls ahead of C1 from day 16 (gap +2,491 -> final +10,314); days 14-21 drivers: missed_water -14, idle_turns -55, sales_rev +2,074, work_turns +47. Hands 9 vs 8, animals 9 vs 11, plants 62 vs 57 |
| `480286010979` | queue | crossover | **+9,415** | 7.0 | 20-0 | -16,888 | +7,085 | melon_floor 0→150, geese 0→1, wheat_cap 22→25, wheat_water_tier 0→1, ROUTE_LEN 3→2, STRAW_CUTOFF 19→18, OPP_GROWTH 1.4→1.0, ORCH_ON 0→1, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.75, ORCH_P_WEEDS 1.5→3.5, ORCH_P_SLACK 6.0→5.5, ORCH_SLACK_HOUR 14→19 |  | cand pulls ahead of C1 from day 17 (gap +1,682 -> final +6,385); days 15-22 drivers: sales_rev +5,156, missed_water -20, work_turns +93, feed_hour -1.49. Hands 14 vs 14, animals 12 vs 11, plants 59 vs |
| `9f2856d00c56` | orch | crossover | **+9,406** | 9.1 | 20-0 | -16,316 | +9,116 | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | harvest_min ?, OPP_GROWTH ? | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,791); days 14-21 drivers: missed_water -17, work_turns +72, idle_turns -53, sales_rev +732. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `c7c22656484a` | wide | paired | **+9,405** | 9.2 | 20-0 | -16,802 | +8,776 | melon_floor 0→150, early_hire_days 3→1, fert_keep 0→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→132, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,009 -> final +7,883); days 14-21 drivers: missed_water -20, work_turns +89, idle_turns -49, sales_rev +387. Hands 10 vs 8, animals 10 vs 11, plants 60 vs 57. |
| `cfedf9caf279` | orch | ablate:load_per_hand | **+9,389** | 9.3 | 20-0 | -20,989 | +9,210 | melon_floor 0→150, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,797); days 14-21 drivers: missed_water -19, work_turns +74, idle_turns -53, sales_rev +738. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `556aa625d136` | queue | ablate:CROP_SWEEP_LEN | **+9,376** | 10.9 | 20-0 | -16,463 | +9,109 | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5 |  | cand pulls ahead of C1 from day 16 (gap +2,077 -> final +9,389); days 14-21 drivers: missed_water -17, sales_rev +2,404, work_turns +55, idle_turns -34. Hands 9 vs 8, animals 9 vs 11, plants 64 vs 57. |
| `c4d1ba53ca8c` | orch | crossover | **+9,349** | 9.1 | 20-0 | -16,586 | +8,512 | wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_PRICE_CUSHION 100→105, OPP_GROWTH 1.4→1.6, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→2.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→10 |  | cand pulls ahead of C1 from day 16 (gap +2,311 -> final +5,712); days 14-21 drivers: missed_water -25, work_turns +105, sales_rev +2,500, idle_turns -50. Hands 10 vs 8, animals 11 vs 11, plants 59 vs  |
| `cbeff72fd1ca` | queue | ablate:ORCH_SLACK_HOUR | **+9,340** | 8.4 | 20-0 | -16,526 | +9,946 | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,077 -> final +10,559); days 14-21 drivers: missed_water -28, work_turns +72, idle_turns -64, sales_rev +1,313. Hands 8 vs 8, animals 9 vs 11, plants 64 vs 57 |
| `591e81db71f2` | queue | crossover | **+9,339** | 9.4 | 20-0 | -21,117 | +8,990 | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,761); days 14-21 drivers: missed_water -17, work_turns +72, idle_turns -53, sales_rev +732. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `249c9825c232` | wide | block_pair | **+9,331** | 10.7 | 20-0 | -16,296 | +9,635 | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +1,918 -> final +10,276); days 14-21 drivers: missed_water -19, work_turns +70, idle_turns -50, sales_rev +808. Hands 10 vs 8, animals 10 vs 11, plants 62 vs 57 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `cbeff72fd1ca` | queue | ablate:ORCH_SLACK_HOUR | +9,946 | 6.0 | 10-0 | -7,031 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `a9e2da40d2b1` | orch | ablate:open_cows | +9,761 | 5.3 | 10-0 | -7,117 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `2bcc9334a840` | orch | migrate | +9,696 | 5.3 | 10-0 | -13,946 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `249c9825c232` | wide | block_pair | +9,635 | 6.9 | 10-0 | -6,448 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `25f7a412756d` | orch | mutate | +9,594 | 5.2 | 10-0 | -7,384 | held_pass | melon_floor 0→150, open_melons 10→9, open_cows 2→1, wheat_cap 22→25, setup_capital_share 0.25→0.5, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→41, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.0, ORCH_SLACK_HOUR 14→15 |
| `d5885e3a3a52` | queue | archive_crossover:crossover_g000050_20260911-122309_0 | +9,545 | 5.5 | 10-0 | -8,447 | held_pass | harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `20aecc07a779` | orch | migrate | +9,540 | 6.6 | 10-0 | -6,904 | held_pass | harvest_min 1→3, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→20, MELON_PRICE_CUSHION 100→110, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→0.25, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→15 |
| `72888332678b` | queue | mutate | +9,517 | 6.0 | 10-0 | -8,678 | held_pass | harvest_min 1→2, wheat_cap 22→25, wheat_sell_price 30→34, setup_capital_share 0.25→0.2, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→9, CROP_SWEEP_RADIUS 5→4, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→0.5, ORCH_P_WEEDS 1.5→3.5, ORCH_COMMIT 0.75→1.0 |
| `b40c471ca6c0` | queue | archive_crossover:crossover_g000025_20260911-115603_1 | +9,495 | 7.9 | 10-0 | -6,630 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `348945b7a860` | o15 | migrate | +9,471 | 5.1 | 10-0 | -8,209 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, early_hire_days 3→1, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→150, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_SLACK 6.0→7.0, ORCH_SLACK_HOUR 14→15 |
| `e5a16e1feca0` | queue | archive_crossover:crossover_g000125_20260911-002105_0 | +9,455 | 5.6 | 10-0 | -8,515 | held_pass | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→132, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `74bed543643f` | wide | paired | +9,438 | 7.3 | 10-0 | -6,384 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→132, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.25, ORCH_SLACK_HOUR 14→15 |
| `0ed6105adec5` | o15 | migrate | +9,402 | 5.8 | 10-0 | -7,474 | held_pass | harvest_min 1→3, wheat_cap 22→25, labor_reserve_buffer 92→81, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_PRICE_CUSHION 100→109, OPP_GROWTH 1.4→1.7, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→11 |
| `ed09b91b9bc9` | o15 | paired | +9,396 | 5.5 | 10-0 | -7,629 | held_pass | harvest_min 1→3, wheat_cap 22→25, labor_reserve_buffer 92→81, MAX_HANDS 14→15, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_PRICE_CUSHION 100→109, OPP_GROWTH 1.4→1.7, FERT_RADIUS 3→2, ORCH_ON 0→1, ORCH_P_HARVEST 0.5→1.0, ORCH_P_FERT 0.5→0.75, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5, ORCH_SLACK_HOUR 14→11 |
| `cc394c4b807f` | orch | paired | +9,316 | 5.6 | 10-0 | -8,221 | held_pass | melon_floor 0→150, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→0.5, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +9,471 (`348945b7a860`), n=43
- orch: best +9,761 (`a9e2da40d2b1`), n=93
- queue: best +9,946 (`cbeff72fd1ca`), n=97
- wide: best +9,635 (`249c9825c232`), n=72

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +11,706 | 132 | 92 | 23 | 315 | 8.6 | 132: +8,639 (n=2), 119: +7,669 (n=5), 111: +5,200 (n=4), 81: +5,051 (n=12), 92: +3,197 (n=275), 54: +2,435 (n=4), 96: +2,109 (n=2), 110: +1,062 (n=4), 125: -1,050 (n=3), 121: -1,255 (n=2), 150: -3,067 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,211 | 17 | 20 | 10 | 326 | 6.37 | 17: +6,766 (n=5), 18: +4,178 (n=31), 19: +3,464 (n=5), 16: +3,256 (n=2), 20: +3,199 (n=267), 21: +1,426 (n=10), 22: -422 (n=2), 14: -2,284 (n=2), 23: -4,446 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,575 | 0.5 | 0.55 | 9 | 326 | 6.34 | 0.5: +3,699 (n=3), 0.55: +3,435 (n=299), 0.8: +2,879 (n=5), 0.6: +2,348 (n=7), 0.7: +1,886 (n=3), 0.65: +153 (n=4), 0.45: -2,558 (n=2), 0.3: -5,876 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WATER | +8,933 | 1.25 | 1.0 | 11 | 324 | 3.84 | 1.25: +7,675 (n=11), 2.5: +5,642 (n=2), 0.5: +4,948 (n=7), 1.75: +4,611 (n=6), 1.5: +4,321 (n=196), 2.0: +4,236 (n=6), 1.0: +139 (n=91), 0.0: -1,259 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +8,910 | 2 | 3 | 4 | 327 | 2.19 | 2: +5,525 (n=55), 3: +2,850 (n=261), 1: +1,139 (n=8), 4: -3,385 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +8,845 | 2 | 0 | 10 | 325 | 6.06 | 2: +8,202 (n=2), 1: +4,766 (n=3), 0: +3,552 (n=287), 7: +3,007 (n=2), 11: +899 (n=6), 10: -120 (n=5), 8: -473 (n=6), 35: -643 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +8,607 | 110 | 100 | 21 | 317 | 7.19 | 110: +9,126 (n=2), 132: +5,132 (n=5), 105: +5,094 (n=6), 109: +4,970 (n=15), 67: +4,927 (n=4), 87: +4,401 (n=3), 86: +4,251 (n=14), 100: +2,946 (n=236), 94: +2,752 (n=6), 150: +2,571 (n=22), 62: +519 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +8,183 | 0.5 | 0.25 | 8 | 327 | 6.0 | 0.5: +6,238 (n=7), 0.35: +4,488 (n=3), 0.2: +3,818 (n=10), 0.25: +3,250 (n=286), 0.3: +1,891 (n=13), 0.45: +1,670 (n=2), 0.4: -553 (n=4), 0.15: -1,945 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_HARVEST | +8,137 | 0.0 | 0.5 | 8 | 326 | 4.5 | 0.0: +5,935 (n=25), 1.0: +4,865 (n=12), 0.25: +4,406 (n=8), 0.5: +3,132 (n=256), 1.5: +3,117 (n=3), 1.75: +33 (n=20), 0.75: -2,202 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WEEDS | +7,805 | 1.25 | 1.5 | 16 | 323 | 8.18 | 1.25: +8,480 (n=4), 0.5: +8,201 (n=2), 3.0: +7,194 (n=10), 4.0: +5,616 (n=2), 3.5: +5,300 (n=37), 3.25: +3,698 (n=3), 2.0: +2,778 (n=2), 1.5: +2,745 (n=247), 5.0: +1,670 (n=2), 1.75: +1,398 (n=3), 2.75: +1,214 (n=6), 0.0: +675 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,693 | 28 | 30 | 13 | 324 | 7.43 | 28: +7,415 (n=3), 26: +6,892 (n=2), 27: +5,176 (n=13), 25: +4,222 (n=8), 35: +4,044 (n=4), 34: +3,875 (n=9), 30: +3,119 (n=273), 29: +927 (n=3), 32: +411 (n=2), 31: -278 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +7,023 | 9 | 6 | 6 | 327 | 3.46 | 9: +5,938 (n=9), 7: +5,453 (n=57), 6: +2,749 (n=243), 8: +2,595 (n=8), 3: -197 (n=5), 5: -1,085 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +6,963 | frontier | frontier | 2 | 327 | 0.8 | frontier: +3,903 (n=294), v312: -3,059 (n=33) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,835 | 41 | 38 | 17 | 319 | 3.74 | 41: +6,878 (n=16), 26: +5,392 (n=5), 35: +5,312 (n=65), 31: +4,071 (n=8), 50: +3,372 (n=6), 38: +2,840 (n=168), 28: +1,280 (n=3), 39: +915 (n=2), 30: +43 (n=46) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +6,721 | 0.3 | 0.0 | 8 | 324 | 3.74 | 0.3: +4,915 (n=3), 0.0: +3,417 (n=307), 0.4: +762 (n=2), 0.1: -272 (n=6), 0.2: -1,805 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,203 | 8 | 10 | 8 | 325 | 3.73 | 8: +6,079 (n=4), 9: +5,027 (n=32), 10: +3,211 (n=256), 11: +1,369 (n=19), 7: +155 (n=7), 13: -124 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +6,064 | 0.0 | 0.5 | 6 | 324 | 1.68 | 0.0: +4,020 (n=33), 0.5: +3,132 (n=289), 1.0: -2,044 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_SLACK | +6,029 | 3.5 | 6.0 | 12 | 326 | 7.94 | 3.5: +8,211 (n=2), 4.0: +7,380 (n=2), 9.5: +7,057 (n=5), 5.5: +4,310 (n=6), 5.0: +4,060 (n=5), 7.0: +3,510 (n=30), 6.5: +3,091 (n=2), 6.0: +3,022 (n=265), 7.5: +2,785 (n=2), 8.0: +2,571 (n=5), 2.0: +2,182 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,843 | 2 | 2 | 3 | 327 | 1.48 | 2: +3,946 (n=270), 1: -241 (n=54), 0: -1,897 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_COMMIT | +5,730 | 1.0 | 0.75 | 8 | 326 | 5.1 | 1.0: +3,473 (n=15), 0.75: +3,431 (n=284), 0.25: +2,690 (n=4), 1.25: +1,644 (n=10), 0.0: +1,467 (n=3), 1.5: +217 (n=7), 0.5: -2,257 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +9,946 (n=43)
- (11, 3, 5): +9,761 (n=62)
- (10, 3, 5): +9,696 (n=54)
- (11, 3, 6): +9,594 (n=37)
- (9, 3, 4): +9,402 (n=76)
- (10, 3, 6): +9,276 (n=1)
- (12, 3, 5): +9,160 (n=11)
- (11, 3, 4): +8,559 (n=3)
- (12, 3, 6): +7,522 (n=15)
- (15, 3, 6): +6,377 (n=2)
- (10, 3, 4): +5,361 (n=9)
- (13, 3, 5): +1,174 (n=2)
- (13, 3, 6): +950 (n=5)
- (14, 3, 6): +142 (n=2)
- (9, 3, 3): -2,030 (n=1)

_Generated 2026-09-11 13:18. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 85 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=85); harvest_min=1–3 (n=85); wheat_tiles=0–4 (n=85); wheat_stock=0–40 (n=85); min_hands=3–6 (n=85); load_per_hand=12–26 (n=85); geese=0–2 (n=85); open_melons=7–14 (n=85)
- **Evidence:** 85 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**327 candidates** with action_table data, **43329 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +3,265 (n=4514) |         +3,201 (n=2289) |         +3,201 (n=2616) | 9419 |
| BUY_ANIMAL |         +2,720 (n=1897) |         +3,432 (n=393) |              — (n=0) | 2290 |
| BUY_SEED |         +3,251 (n=3360) |         +3,357 (n=1247) |         +2,909 (n=468) | 5075 |
| BUY_LAND |         +3,142 (n=1165) |         +3,816 (n=309) |              — (n=0) | 1474 |
| BUY_PRODUCT |         +3,200 (n=4904) |         +3,201 (n=2289) |         +3,201 (n=2289) | 9482 |
| HIRE |         +3,056 (n=2019) |         +3,042 (n=1136) |         +3,360 (n=848) | 4003 |
| WATER_MISSED |         +3,201 (n=3673) |         +3,201 (n=2289) |         +3,197 (n=2614) | 8576 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +2,891 (n=1739) |         +2,648 (n=488) |         +2,561 (n=783) | 3010 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +3,354 |      +3,201 |      +3,220 |      +3,295 |      +3,188 |      +3,192 |
| BUY_ANIMAL |      +2,581 |           — |           — |      +3,617 |      +3,339 |      +2,801 |
| BUY_SEED |      +2,626 |      +4,149 |      -3,985 |           — |      +1,488 |      +3,328 |
| BUY_LAND |      -1,541 |      -3,120 |      +3,278 |      -2,321 |      +3,958 |      +3,163 |
| BUY_PRODUCT |      +3,200 |           — |           — |           — |           — |           — |
| HIRE |      +3,117 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +3,201 |      +1,110 |      +3,201 |      +3,233 |
| FEED_MISSED |           — |      +3,180 |      +2,027 |           — |           — |      +2,731 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +3,816 | 309 | 0.96 |
| 2 | BUY_ANIMAL | mid | +3,432 | 393 | 0.81 |
| 3 | HIRE | late | +3,360 | 848 | 0.82 |
| 4 | BUY_SEED | mid | +3,357 | 1247 | 0.78 |
| 5 | SELL | early | +3,265 | 4514 | 0.78 |
| 6 | BUY_SEED | early | +3,251 | 3360 | 0.77 |
| 7 | SELL | mid | +3,201 | 2289 | 0.76 |
| 8 | SELL | late | +3,201 | 2616 | 0.76 |
| 9 | BUY_PRODUCT | mid | +3,201 | 2289 | 0.76 |
| 10 | BUY_PRODUCT | late | +3,201 | 2289 | 0.76 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **WATER_MISSED** in ('low', 'high', 'high', 'high'): -6,420 (n=13)
- **SELL** in ('low', 'high', 'high', 'high'): -6,316 (n=14)
- **BUY_PRODUCT** in ('low', 'high', 'high', 'high'): -6,316 (n=14)
- **HIRE** in ('low', 'high', 'high', 'high'): -6,216 (n=9)
- **BUY_SEED** in ('low', 'high', 'high', 'high'): -6,173 (n=5)
- **SELL** in ('low', 'mid', 'mid', 'mid'): +6,058 (n=88)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +6,058 (n=88)
- **BUY_ANIMAL** in ('mid', 'low', 'high', 'high'): +5,969 (n=26)
- **BUY_SEED** in ('mid', 'low', 'high', 'high'): +5,169 (n=32)
- **BUY_PRODUCT** in ('mid', 'low', 'high', 'high'): +5,169 (n=32)
- **BUY_LAND** in ('high', 'mid', 'high', 'high'): +5,064 (n=5)
- **FEED_MISSED** in ('low', 'low', 'low', 'mid'): +4,893 (n=149)
- **WATER_MISSED** in ('low', 'low', 'low', 'mid'): +4,887 (n=153)
- **BUY_ANIMAL** in ('low', 'low', 'low', 'mid'): +4,858 (n=157)
- **SELL** in ('low', 'low', 'low', 'mid'): +4,736 (n=160)

_Generated 2026-09-11 13:18. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._