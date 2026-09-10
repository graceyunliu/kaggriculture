# Evolution run 20260910-092014

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.18 h · candidates evaluated this run: 18 · games 1,538 (8,649/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 1 | 2 |
| dead_smoke | 3 | 24 |
| alive | 14 | 1512 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 215 · held-out evaluated: 7 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |
| `ffbf75678458` | M2 | paired | **+59** | 0.1 | 10-10 | -27,551 | +2,170 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 22 (gap -4,389 -> final -18,581); days 20-27 drivers: sales_rev -21,759, work_turns -185, weeds_new +2, reversals +5. Hands 11 vs 11, animals 8 vs 11, plants 42 vs 47. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `bfe4bb8d3609` | v312 | migrate | +4,008 | 1.6 | 7-3 | -21,783 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_sell_price 30→29, labor_reserve_buffer 92→95, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `89822c12eba2` | wide | crossover | +3,032 | 1.6 | 8-2 | -22,099 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→4, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ef9bb31c7a35` | c1 | mutate | +2,574 | 1.6 | 8-2 | -24,298 | alive | melon_floor 0→150, open_melons 8→10, open_wheat 7→3, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→102 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `961ab6fb4730` | M2 | mutate | +2,342 | 1.8 | 6-4 | -19,878 | alive | melon_floor 0→150, harvest_min 1→3, wheat_tiles 0→1, load_per_hand 20→21, open_melons 8→9, open_wheat 7→6, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ffbf75678458` | M2 | paired | +2,170 | 2.3 | 7-3 | -27,607 | held_fail | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `be39051210fb` | c1 | block_pair | +2,143 | 0.3 | 2-8 | -28,277 | alive | geese 0→1, open_melons 8→6 · blocks: sweep |
| `362ca8604fb4` | c1 | paired | +2,033 | 1.6 | 7-3 | -24,144 | alive | MAX_HANDS 14→13, SPREAD_W 1.25→1.0 |
| `926d7668ad53` | queue | mutate | +1,769 | 1.9 | 8-2 | -28,807 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→3, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4 |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=28
- M2: best +2,342 (`961ab6fb4730`), n=20
- c1: best +2,683 (`5fd05605827b`), n=38
- queue: best +4,836 (`7ec902ce836b`), n=66
- v312: best +4,008 (`bfe4bb8d3609`), n=32
- wide: best +3,032 (`89822c12eba2`), n=31

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +7,700 | 102 | 100 | 21 | 203 | 6.8 | 102: +1,091 (n=6), 74: -125 (n=2), 83: -654 (n=2), 85: -927 (n=5), 100: -1,613 (n=176), 114: -3,075 (n=2), 110: -3,429 (n=3), 92: -4,998 (n=5), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +6,302 | 95 | 92 | 21 | 206 | 7.74 | 95: +2,439 (n=2), 58: +1,091 (n=6), 124: -423 (n=5), 107: -755 (n=7), 11: -1,574 (n=20), 73: -1,731 (n=2), 92: -1,815 (n=150), 94: -2,049 (n=2), 150: -2,225 (n=6), 59: -3,300 (n=2), 76: -3,783 (n=2), 102: -3,863 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +5,537 | 39 | 38 | 12 | 212 | 2.31 | 39: +84 (n=19), 35: -924 (n=26), 34: -1,292 (n=68), 32: -1,346 (n=4), 38: -2,210 (n=78), 43: -3,008 (n=10), 41: -3,113 (n=2), 46: -5,356 (n=3), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +5,061 | 18 | 20 | 9 | 214 | 4.23 | 18: -676 (n=6), 19: -1,205 (n=36), 20: -1,562 (n=140), 23: -2,102 (n=4), 22: -2,577 (n=3), 17: -2,651 (n=2), 21: -2,811 (n=21), 24: -5,738 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,041 | 2 | 2 | 4 | 215 | 2.52 | 2: -1,430 (n=189), 1: -3,099 (n=20), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +4,972 | 9 | 8 | 7 | 214 | 1.92 | 9: -717 (n=8), 10: -1,090 (n=85), 11: -1,680 (n=11), 8: -2,076 (n=104), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +4,847 | 4 | 5 | 8 | 214 | 4.3 | 4: +684 (n=5), 8: -345 (n=4), 3: -1,375 (n=29), 5: -1,725 (n=162), 7: -2,431 (n=8), 0: -4,047 (n=4), 6: -4,164 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +4,424 | 13 | 14 | 7 | 214 | 3.4 | 13: +194 (n=12), 12: -475 (n=27), 14: -1,878 (n=157), 11: -2,042 (n=6), 15: -3,228 (n=9), 16: -4,231 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +4,320 | 2 | 3 | 3 | 215 | 1.53 | 2: -1,190 (n=21), 3: -1,464 (n=181), 4: -5,510 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +4,056 | 0.6 | 0.55 | 8 | 213 | 2.8 | 0.6: -154 (n=11), 0.45: -239 (n=15), 0.65: -945 (n=18), 0.55: -1,642 (n=135), 0.5: -3,004 (n=28), 0.3: -4,210 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +3,830 | 25 | 22 | 10 | 212 | 3.56 | 25: -864 (n=23), 13: -986 (n=22), 22: -1,639 (n=138), 20: -2,279 (n=6), 18: -2,797 (n=15), 24: -3,782 (n=3), 23: -4,694 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,670 | frontier | frontier | 2 | 215 | 0.88 | frontier: -1,460 (n=202), v312: -5,130 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,628 | 0.2 | 0.25 | 9 | 214 | 4.79 | 0.2: -662 (n=3), 0.15: -704 (n=2), 0.4: -971 (n=19), 0.45: -1,073 (n=11), 0.25: -1,433 (n=155), 0.3: -3,075 (n=2), 0.5: -3,672 (n=3), 0.35: -4,290 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +3,612 | 3 | 6 | 6 | 214 | 2.76 | 3: -898 (n=36), 5: -1,506 (n=9), 6: -1,767 (n=161), 8: -1,921 (n=2), 7: -4,510 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +3,511 | 29 | 30 | 10 | 214 | 3.5 | 29: -904 (n=3), 34: -1,041 (n=2), 31: -1,149 (n=3), 25: -1,226 (n=63), 26: -1,727 (n=23), 30: -1,810 (n=107), 28: -1,913 (n=7), 36: -3,346 (n=3), 27: -4,415 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +3,474 | 2 | 2 | 3 | 215 | 1.85 | 2: -1,530 (n=204), 3: -4,081 (n=6), 1: -5,004 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +3,305 | 9 | 7 | 8 | 215 | 4.69 | 9: -407 (n=3), 3: -441 (n=10), 4: -1,079 (n=35), 6: -1,473 (n=7), 7: -1,874 (n=153), 8: -2,526 (n=3), 10: -3,113 (n=2), 5: -3,711 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +3,253 | 14 | 17 | 8 | 213 | 3.68 | 14: -381 (n=2), 17: -1,396 (n=166), 18: -1,624 (n=6), 16: -1,682 (n=4), 15: -2,203 (n=15), 20: -3,634 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +2,567 | 16 | 17 | 8 | 214 | 2.83 | 16: -679 (n=3), 19: -873 (n=64), 18: -1,319 (n=11), 17: -1,933 (n=117), 22: -2,656 (n=7), 20: -3,144 (n=3), 14: -3,246 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_hold_days | +2,485 | 3 | 0 | 4 | 215 | 2.0 | 3: +71 (n=2), 2: -1,063 (n=36), 0: -1,769 (n=161), 1: -2,414 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=14)
- (16, 3, 6): +4,008 (n=2)
- (7, 3, 4): +3,920 (n=22)
- (14, 3, 6): +3,066 (n=4)
- (7, 3, 3): +3,032 (n=11)
- (9, 3, 4): +2,683 (n=14)
- (11, 3, 5): +2,663 (n=12)
- (11, 3, 6): +2,574 (n=8)
- (9, 3, 5): +2,565 (n=4)
- (6, 3, 3): +2,293 (n=4)
- (15, 3, 6): +2,143 (n=3)
- (10, 4, 6): +2,033 (n=15)
- (12, 3, 4): +1,251 (n=4)
- (6, 3, 4): +1,192 (n=3)
- (10, 3, 5): +1,108 (n=7)

_Generated 2026-09-10 09:30. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 106 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=106); harvest_min=1–3 (n=106); wheat_tiles=0–5 (n=106); wheat_stock=0–19 (n=106); min_hands=3–6 (n=106); load_per_hand=12–25 (n=106); geese=0–1 (n=106); open_melons=4–12 (n=106)
- **Evidence:** 106 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 09:30. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._