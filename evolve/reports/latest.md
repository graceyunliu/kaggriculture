# Evolution run 20260910-202200

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_pensukesan_107199477.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_48c23c84c0d8.py` (sha `48c23c84c0d8`)
Elapsed 2.01 h · candidates evaluated this run: 161 · games 26,410 (13,113/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 22 | 44 |
| dead_pattern | 11 | 22 |
| dead_smoke | 17 | 136 |
| alive | 61 | 7808 |
| held_fail | 5 | 1840 |
| held_pass | 45 | 16560 |
| error | 0 | 0 |

Population (all runs, reached dev): 111 · held-out evaluated: 50 · held-out PASS: 45

## Reference points

Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real `candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| chassis defaults (seed row) | +3,605 | 3.6 | 9-1 | -13,427 | +4,376 | 7.2 | 18-2 |
| chassis + C1 params (seed row) | +0 | 0.0 | not evaluated (no-op) | -16,635 | — | — | —-— |
| C1.py (file) vs O15_SALE_PRIORITY.py | -21,945 | -16.8 | 0-10 | — | — | — | — |
| V3_12.py (file) vs O15_SALE_PRIORITY.py | -25,061 | -10.2 | 0-10 | — | — | — | — |
| O15_SALE_PRIORITY.py own panel (dev / held) | — | — | — | -16,635 / -24,907 | — | — | — |

Measurement mode: `KAGG_FIXED_SHOPS=1` (shop unlocks policy-independent; panel margins comparable at ±$3k/opponent).

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `cfedf9caf279` | orch | ablate:load_per_hand | **+9,389** | 9.3 | 20-0 | -20,989 | +9,210 | melon_floor 0→150, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,797); days 14-21 drivers: missed_water -19, work_turns +74, idle_turns -53, sales_rev +738. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `591e81db71f2` | queue | crossover | **+9,339** | 9.4 | 20-0 | -21,117 | +8,990 | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,761); days 14-21 drivers: missed_water -17, work_turns +72, idle_turns -53, sales_rev +732. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `2bcc9334a840` | orch | migrate | **+9,160** | 8.9 | 20-0 | -22,928 | +9,696 | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 | melon_floor ?, harvest_min ?, load_per_hand +486, ROUTE_LEN +6,649, STRAW_CUTOFF ?, MELON_MAX_TILES ?, OPP_GROWTH ? | cand pulls ahead of C1 from day 18 (gap +2,290 -> final +8,311); days 16-23 drivers: missed_water -45, sales_rev +4,192, work_turns +96, idle_turns -9. Hands 12 vs 8, animals 10 vs 11, plants 59 vs 57 |
| `db6866135372` | queue | archive_crossover:crossover_g000125_20260910-221838_0 | **+9,110** | 8.5 | 20-0 | -21,268 | +9,231 | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +11,116); days 14-21 drivers: missed_water -17, work_turns +82, idle_turns -49, sales_rev +691. Hands 11 vs 8, animals 10 vs 11, plants 65 vs 57 |
| `14f11fa0362e` | queue | archive_crossover:crossover_g000075_20260910-213717_1 | **+8,933** | 11.0 | 20-0 | -21,093 | +8,979 | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +2,032 -> final +9,767); days 14-21 drivers: missed_water -19, work_turns +74, idle_turns -53, sales_rev +738. Hands 9 vs 8, animals 10 vs 11, plants 64 vs 57. |
| `9d80b5649d1c` | orch | crossover | **+8,674** | 6.5 | 19-1 | -21,504 | +7,188 | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,121 -> final +9,897); days 14-21 drivers: missed_water -29, idle_turns -60, work_turns +58, sales_rev +1,812. Hands 9 vs 8, animals 9 vs 11, plants 66 vs 57. |
| `9597203b3962` | orch | migrate | **+7,894** | 6.8 | 19-1 | -20,766 | +7,821 | melon_floor 0→200, harvest_min 1→2, wheat_stock 0→2, max_animals 17→18, wheat_cap 22→25, MAX_HANDS 14→13, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→67, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→13, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +1,854 -> final +9,024); days 14-21 drivers: missed_water -14, sales_rev +2,520, work_turns +53, idle_turns -26. Hands 12 vs 8, animals 9 vs 11, plants 60 vs 57 |
| `275c6e29b07d` | orch | mutate | **+7,731** | 6.5 | 19-1 | -21,737 | +7,822 | melon_floor 0→150, wheat_cap 22→25, wheat_sell_price 30→25, ROUTE_LEN 3→2, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5, ORCH_COMMIT 0.75→1.25, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 16 (gap +2,552 -> final +10,175); days 14-21 drivers: missed_water -25, work_turns +67, sales_rev +2,369, idle_turns -54. Hands 10 vs 8, animals 9 vs 11, plants 64 vs 5 |
| `b4dfba3512ed` | queue | mutate | **+7,706** | 6.3 | 18-2 | -23,018 | +4,821 | harvest_min 1→2, open_melons 10→11, early_hire_days 3→2, wheat_per_animal 0.0→0.2, wheat_cap 22→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.75, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 21 (gap +2,320 -> final +4,579); days 19-26 drivers: missed_water -57, work_turns +146, idle_turns -57, feed_hour -1.17. Hands 11 vs 12, animals 11 vs 11, plants 48 vs  |
| `8fc478c77bf5` | orch | mutate | **+5,378** | 4.3 | 17-3 | -23,702 | +6,393 | wheat_cap 22→25, wheat_sell_price 30→35, ROUTE_LEN 3→2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 21 (gap +3,849 -> final +3,745); days 19-26 drivers: missed_water -51, work_turns +97, idle_turns -43, feed_hour -1.45. Hands 10 vs 12, animals 9 vs 11, plants 46 vs 42 |
| `d27d4e3d6a8d` | orch | paired | **+4,395** | 4.9 | 17-3 | -22,222 | +6,011 | harvest_min 1→2, fert_keep 0→2, wheat_cap 22→25, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 | harvest_min +400, fert_keep +1,690 | cand pulls ahead of C1 from day 16 (gap +1,664 -> final +7,299); days 14-21 drivers: missed_water -27, idle_turns -49, work_turns +38, sales_rev +541. Hands 11 vs 8, animals 9 vs 11, plants 62 vs 57. |
| `8e7a0bc5c98e` | orch | seed:orch | **+4,376** | 7.2 | 18-2 | -21,607 | +3,605 | ORCH_ON 0→1 |  | cand pulls ahead of C1 from day 18 (gap +2,158 -> final +6,840); days 16-23 drivers: missed_water -42, idle_turns -47, sales_rev +1,039, work_turns +24. Hands 10 vs 8, animals 9 vs 11, plants 61 vs 57 |
| `9d5a11ae925c` | orch | ablate:harvest_min | **+4,357** | 5.1 | 17-3 | -22,103 | +5,611 | fert_keep 0→2, wheat_cap 22→25, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 16 (gap +1,664 -> final +7,299); days 14-21 drivers: missed_water -27, idle_turns -49, work_turns +38, sales_rev +541. Hands 11 vs 8, animals 9 vs 11, plants 62 vs 57. |
| `2049168497f4` | orch | crossover | **+4,124** | 3.5 | 15-5 | -22,314 | +3,604 | melon_floor 0→150, open_wheat 7→8, wheat_cap 22→25, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→1, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |  | cand pulls ahead of C1 from day 20 (gap +1,695 -> final +7,179); days 18-25 drivers: sales_rev +6,175, missed_water -30, idle_turns -47, work_turns +46. Hands 12 vs 11, animals 9 vs 11, plants 59 vs 5 |
| `94483021ceb8` | orch | migrate | **+4,095** | 4.4 | 17-3 | -22,107 | +4,348 | fert_keep 0→2, wheat_cap 22→25, setup_capital_share 0.25→0.3, MELON_PRICE_CUSHION 100→105, OPP_GROWTH 1.4→1.6, ORCH_ON 0→1, ORCH_P_PLANT 1.0→1.5, ORCH_P_WATER 1.0→1.5 |  | cand pulls ahead of C1 from day 18 (gap +1,698 -> final +7,669); days 16-23 drivers: missed_water -29, work_turns +58, idle_turns -44, sales_rev +1,713. Hands 12 vs 8, animals 9 vs 11, plants 61 vs 57 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `2bcc9334a840` | orch | migrate | +9,696 | 5.3 | 10-0 | -13,946 | held_pass | melon_floor 0→150, harvest_min 1→2, load_per_hand 20→18, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `db6866135372` | queue | archive_crossover:crossover_g000125_20260910-221838_0 | +9,231 | 6.7 | 10-0 | -12,254 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `cfedf9caf279` | orch | ablate:load_per_hand | +9,210 | 6.8 | 10-0 | -12,076 | held_pass | melon_floor 0→150, harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `591e81db71f2` | queue | crossover | +8,990 | 5.9 | 10-0 | -11,710 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→86, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |
| `14f11fa0362e` | queue | archive_crossover:crossover_g000075_20260910-213717_1 | +8,979 | 6.3 | 10-0 | -11,983 | held_pass | harvest_min 1→2, wheat_cap 22→25, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |
| `275c6e29b07d` | orch | mutate | +7,822 | 6.1 | 10-0 | -12,498 | held_pass | melon_floor 0→150, wheat_cap 22→25, wheat_sell_price 30→25, ROUTE_LEN 3→2, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_FERT 0.5→1.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5, ORCH_COMMIT 0.75→1.25, ORCH_SLACK_HOUR 14→15 |
| `9597203b3962` | orch | migrate | +7,821 | 5.3 | 10-0 | -11,995 | held_pass | melon_floor 0→200, harvest_min 1→2, wheat_stock 0→2, max_animals 17→18, wheat_cap 22→25, MAX_HANDS 14→13, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→67, OPP_GROWTH 1.4→1.2, MAX_SHEEP 14→13, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `9d80b5649d1c` | orch | crossover | +7,188 | 5.0 | 10-0 | -11,971 | held_pass | melon_floor 0→150, wheat_cap 22→25, ROUTE_LEN 3→2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `8fc478c77bf5` | orch | mutate | +6,393 | 3.2 | 9-1 | -14,430 | held_pass | wheat_cap 22→25, wheat_sell_price 30→35, ROUTE_LEN 3→2, ORCH_ON 0→1, ORCH_P_WWATER 0.5→0.0, ORCH_P_PLANT 1.0→0.0, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `d27d4e3d6a8d` | orch | paired | +6,011 | 3.9 | 10-0 | -13,186 | held_pass | harvest_min 1→2, fert_keep 0→2, wheat_cap 22→25, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |
| `9d5a11ae925c` | orch | ablate:harvest_min | +5,611 | 3.5 | 10-0 | -13,368 | held_pass | fert_keep 0→2, wheat_cap 22→25, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5 |
| `e189f81eb9f9` | orch | ablate:open_wheat | +5,501 | 5.7 | 10-0 | -12,644 | held_pass | melon_floor 0→150, load_per_hand 20→21, wheat_cap 22→25, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_SLACK_HOUR 14→15 |
| `21e7e51f3626` | queue | migrate | +5,208 | 3.5 | 8-2 | -13,140 | held_pass | melon_floor 0→200, harvest_min 1→2, fert_keep 0→2, wheat_cap 22→25, wheat_water_tier 0→1, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_COMMIT 0.75→1.0 |
| `f67d66fe2dc3` | queue | archive_crossover:crossover_g000100_20260910-215325_0 | +4,995 | 3.9 | 10-0 | -13,147 | held_pass | melon_floor 0→150, harvest_min 1→2, fert_carry 2→1, wheat_cap 22→25, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→35, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_WATER 1.0→1.5, ORCH_P_WEEDS 1.5→3.5 |
| `b4dfba3512ed` | queue | mutate | +4,821 | 3.0 | 9-1 | -14,377 | held_pass | harvest_min 1→2, open_melons 10→11, early_hire_days 3→2, wheat_per_animal 0.0→0.2, wheat_cap 22→25, MAX_HANDS 14→16, ROUTE_LEN 3→2, STRAW_CUTOFF 19→16, OPP_GROWTH 1.4→1.2, ORCH_ON 0→1, ORCH_P_FERT 0.5→1.0, ORCH_P_WATER 1.0→1.75, ORCH_SLACK_HOUR 14→15 |

## Islands (best dev margin, population size)

- capital: best +3,278 (`5a8a2ea4702e`), n=22
- o15: best +0 (`2dc64f647872`), n=1
- orch: best +9,696 (`2bcc9334a840`), n=37
- queue: best +9,231 (`db6866135372`), n=24
- wide: best +2,891 (`aba8bf4da11e`), n=27

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| load_per_hand | +8,656 | 18 | 20 | 6 | 109 | 2.71 | 18: +6,371 (n=2), 20: +1,500 (n=101), 21: +838 (n=4), 14: -2,284 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +8,031 | 0.55 | 0.55 | 5 | 108 | 0.96 | 0.55: +1,659 (n=106), 0.3: -6,373 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +7,163 | 25 | 30 | 7 | 107 | 1.8 | 25: +5,550 (n=2), 30: +1,510 (n=100), 31: -1,613 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_FERT | +6,419 | 1.0 | 0.5 | 7 | 107 | 1.8 | 1.0: +4,661 (n=5), 0.5: +1,559 (n=100), 0.25: -1,758 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +5,763 | frontier | frontier | 2 | 111 | 0.75 | frontier: +2,185 (n=97), v312: -3,578 (n=14) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| feed_spare_poor | +5,704 | 0 | 0 | 3 | 111 | 1.38 | 0: +2,089 (n=88), 2: -558 (n=20), 1: -3,615 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +5,652 | 16 | 19 | 4 | 110 | 1.07 | 16: +4,960 (n=12), 19: +1,589 (n=76), 20: -691 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +5,583 | 105 | 100 | 7 | 109 | 3.4 | 105: +3,560 (n=2), 86: +2,735 (n=7), 87: +2,226 (n=2), 100: +1,395 (n=96), 62: -2,023 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +5,573 | 35 | 38 | 6 | 109 | 1.9 | 35: +4,799 (n=9), 28: +2,141 (n=2), 38: +1,663 (n=79), 30: -774 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_SLACK_HOUR | +4,861 | 12 | 14 | 6 | 109 | 1.09 | 12: +3,418 (n=5), 15: +3,193 (n=38), 14: +736 (n=57), 8: -1,444 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +4,623 | 1.2 | 1.4 | 6 | 107 | 0.74 | 1.2: +5,557 (n=14), 1.4: +934 (n=93) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| melon_floor | +4,595 | 200 | 0 | 4 | 111 | 1.2 | 200: +4,734 (n=3), 150: +2,148 (n=44), 0: +864 (n=61), 100: +139 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +4,495 | 18 | 17 | 5 | 110 | 2.67 | 18: +3,515 (n=3), 16: +3,176 (n=3), 17: +1,494 (n=101), 19: -980 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +4,373 | 1.25 | 1.25 | 3 | 111 | 1.84 | 1.25: +1,612 (n=105), 1.5: -484 (n=4), 1.0: -2,761 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ORCH_P_WWATER | +4,323 | 0.0 | 0.5 | 2 | 111 | 0.91 | 0.0: +5,586 (n=5), 0.5: +1,263 (n=106) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +4,104 | 7 | 7 | 7 | 110 | 4.13 | 7: +1,820 (n=94), 6: +889 (n=4), 8: +182 (n=4), 9: -825 (n=4), 4: -1,255 (n=2), 10: -2,284 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| harvest_min | +4,014 | 2 | 1 | 3 | 110 | 0.73 | 2: +4,952 (n=15), 1: +937 (n=95) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +4,014 | 14 | 14 | 5 | 110 | 2.16 | 14: +1,991 (n=87), 12: +259 (n=10), 11: -896 (n=11), 6: -2,023 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| fert_keep | +3,980 | 2 | 0 | 2 | 111 | 0.93 | 2: +5,294 (n=4), 0: +1,314 (n=107) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,931 | 0.3 | 0.25 | 5 | 109 | 1.75 | 0.3: +1,986 (n=7), 0.25: +1,591 (n=100), 0.15: -1,945 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 5): +9,696 (n=10)
- (9, 3, 5): +7,822 (n=10)
- (9, 3, 4): +7,821 (n=37)
- (11, 3, 5): +4,821 (n=26)
- (10, 3, 4): +4,059 (n=3)
- (12, 3, 5): +3,504 (n=6)
- (11, 3, 6): +3,278 (n=8)
- (12, 3, 6): +2,800 (n=6)
- (13, 3, 5): +1,174 (n=1)
- (11, 3, 4): +284 (n=1)
- (9, 3, 3): -2,030 (n=1)
- (6, 3, 3): -6,168 (n=2)

_Generated 2026-09-10 22:23. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 33 recent candidates)

- **Observed outcome:** sales=96,679; missed_water=406; idle_share=0.16
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=33); harvest_min=1–2 (n=33); wheat_tiles=0–2 (n=33); wheat_stock=0–35 (n=33); min_hands=3–6 (n=33); load_per_hand=20–23 (n=33); geese=0–2 (n=33); open_melons=7–13 (n=33)
- **Evidence:** 33 candidates, multiple seeds. Confidence: high

## Action timing patterns (AGE-359: observational — correlations, not causes)

**111 candidates** with action_table data, **14751 total action events** extracted (SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).

Action timing vs outcome correlation. For each action type, the table shows mean dev_margin of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. This is NOT causal — a candidate that sells early may also have other good properties. Use as a guide for what to test, not as a proven mechanism.

| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |
|---|---|---:|---|---|---:|
| SELL |         +1,524 (n=1535) |         +1,458 (n=777) |         +1,458 (n=888) | 3200 |
| BUY_ANIMAL |         +1,017 (n=652) |         +1,942 (n=132) |              — (n=0) | 784 |
| BUY_SEED |         +1,452 (n=1136) |         +1,518 (n=413) |         +1,202 (n=175) | 1724 |
| BUY_LAND |         +1,450 (n=410) |         +2,137 (n=108) |              — (n=0) | 518 |
| BUY_PRODUCT |         +1,458 (n=1665) |         +1,458 (n=777) |         +1,458 (n=777) | 3219 |
| HIRE |         +1,316 (n=669) |         +1,415 (n=389) |         +1,695 (n=290) | 1348 |
| WATER_MISSED |         +1,454 (n=1238) |         +1,458 (n=777) |         +1,458 (n=888) | 2903 |
  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._
| FEED_MISSED |         +1,265 (n=594) |         +1,221 (n=175) |           +967 (n=286) | 1055 |
  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._

## Postponement cost curves (mean dev_margin by days postponed)

For each action type, how does outcome vary with how late the action was taken? Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.

| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |
|---|---|---:|---:|---:|---:|---:|---:|
| SELL |      +1,614 |      +1,458 |      +1,491 |      +1,297 |      +1,430 |      +1,468 |
| BUY_ANIMAL |        +798 |           — |           — |      +1,134 |      +1,644 |      +1,178 |
| BUY_SEED |        +788 |      +2,199 |      -3,326 |           — |        -980 |      +1,549 |
| BUY_LAND |        -575 |      -3,326 |      +1,547 |      -3,123 |      +2,279 |      +1,472 |
| BUY_PRODUCT |      +1,458 |           — |           — |           — |           — |           — |
| HIRE |      +1,426 |           — |           — |           — |           — |           — |
| WATER_MISSED |           — |           — |      +1,458 |      -1,221 |      +1,458 |      +1,494 |
| FEED_MISSED |           — |      +1,470 |         -90 |           — |           — |      +1,166 |

## Action contexts with strongest outcome signal (top 10)

Action × horizon combinations sorted by |mean_dev|. These are the patterns most associated with outcome variation — candidates for matrix-informed runtime rules.

| rank | action_type | horizon | mean_dev | n | signal/noise |
|---|---|---:|---:|---:|---:|
| 1 | BUY_LAND | mid | +2,137 | 108 | 0.59 |
| 2 | BUY_ANIMAL | mid | +1,942 | 132 | 0.53 |
| 3 | HIRE | late | +1,695 | 290 | 0.47 |
| 4 | SELL | early | +1,524 | 1535 | 0.42 |
| 5 | BUY_SEED | mid | +1,518 | 413 | 0.41 |
| 6 | SELL | mid | +1,458 | 777 | 0.39 |
| 7 | SELL | late | +1,458 | 888 | 0.39 |
| 8 | BUY_PRODUCT | early | +1,458 | 1665 | 0.39 |
| 9 | BUY_PRODUCT | mid | +1,458 | 777 | 0.39 |
| 10 | BUY_PRODUCT | late | +1,458 | 777 | 0.39 |

## Action × context bucket (mean dev_margin, n≥3)

**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)

- **WATER_MISSED** in ('low', 'high', 'high', 'high'): -6,420 (n=13)
- **SELL** in ('low', 'high', 'high', 'high'): -6,316 (n=14)
- **BUY_PRODUCT** in ('low', 'high', 'high', 'high'): -6,316 (n=14)
- **HIRE** in ('low', 'high', 'high', 'high'): -6,216 (n=9)
- **BUY_SEED** in ('low', 'high', 'high', 'high'): -6,173 (n=5)
- **FEED_MISSED** in ('low', 'mid', 'high', 'high'): -4,975 (n=4)
- **SELL** in ('low', 'mid', 'mid', 'mid'): +3,756 (n=22)
- **BUY_PRODUCT** in ('low', 'mid', 'mid', 'mid'): +3,756 (n=22)
- **SELL** in ('low', 'mid', 'low', 'high'): -3,734 (n=13)
- **BUY_PRODUCT** in ('low', 'mid', 'low', 'high'): -3,734 (n=13)
- **WATER_MISSED** in ('low', 'mid', 'low', 'high'): -3,734 (n=13)
- **HIRE** in ('low', 'mid', 'low', 'high'): -3,632 (n=12)
- **SELL** in ('mid', 'mid', 'low', 'high'): -3,252 (n=9)
- **BUY_ANIMAL** in ('mid', 'mid', 'low', 'high'): -3,252 (n=9)
- **BUY_SEED** in ('mid', 'mid', 'low', 'high'): -3,252 (n=9)

_Generated 2026-09-10 22:23. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._