# Evolution run 20260910-093245

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.55 h · candidates evaluated this run: 52 · games 4,862 (8,817/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 3 | 6 |
| dead_pattern | 6 | 12 |
| dead_smoke | 4 | 32 |
| alive | 36 | 3888 |
| held_fail | 3 | 924 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 284 · held-out evaluated: 12 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `db61805ecfa9` | M2 | mutate | **+3,427** | 3.2 | 17-3 | -28,163 | +2,910 | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 20 (gap -3,060 -> final -43,282); days 18-25 drivers: sales_rev -43,924, work_turns -118, water_hour +0.9. Hands 11 vs 13, animals 9 vs 11, plants 60 vs 62. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `935becadf7d7` | queue | archive_crossover:crossover_g000025_20260910-094825_0 | **+1,563** | 1.6 | 14-6 | -25,481 | +2,260 | open_melons 8→10, open_wheat 7→6, early_hire_days 5→7, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |  | cand falls behind C1 from day 17 (gap -1,626 -> final -37,310); days 15-22 drivers: sales_rev -24,138, work_turns -183, feed_hour +0.89, reversals +7. Hands 14 vs 14, animals 11 vs 11, plants 57 vs 85 |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |
| `ffbf75678458` | M2 | paired | **+59** | 0.1 | 10-10 | -27,551 | +2,170 | melon_floor 0→200, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 22 (gap -4,389 -> final -18,581); days 20-27 drivers: sales_rev -21,759, work_turns -185, weeds_new +2, reversals +5. Hands 11 vs 11, animals 8 vs 11, plants 42 vs 47. |
| `71af3ce6e1eb` | queue | mutate | **-176** | -0.2 | 9-11 | -23,259 | +1,942 | melon_floor 0→150, load_per_hand 20→19, open_melons 8→10, max_animals 17→18, wheat_water_tier 0→1, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→16, SPREAD_W 1.25→1.0 |  | cand falls behind C1 from day 20 (gap -2,908 -> final -21,056); days 18-25 drivers: sales_rev -15,990, work_turns -147, feed_hour +0.99, water_hour +0.83. Hands 12 vs 13, animals 11 vs 11, plants 52 v |
| `a82c355f4ada` | queue | mutate | **-304** | -0.3 | 13-7 | -26,016 | +1,642 | melon_floor 0→150, load_per_hand 20→21, open_melons 8→10, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 5→3, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,723 -> final -7,677); days 14-21 drivers: sales_rev -17,098, work_turns -288, weeds_new +1. Hands 6 vs 14, animals 7 vs 11, plants 66 vs 84. |
| `af8e5e34dea8` | queue | mutate | **-488** | -0.5 | 7-13 | -22,576 | +1,881 | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, wheat_water_tier 0→1, MAX_HANDS 14→12, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, SPREAD_W 1.25→1.0 |  | cand falls behind C1 from day 20 (gap -2,908 -> final -21,009); days 18-25 drivers: sales_rev -15,157, work_turns -147, feed_hour +0.99, water_hour +0.83. Hands 12 vs 13, animals 11 vs 11, plants 52 v |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `bfe4bb8d3609` | v312 | migrate | +4,008 | 1.6 | 7-3 | -21,783 | alive | melon_floor 0→150, min_hands 3→4, open_melons 8→10, early_hire_days 5→4, demand_share 0.55→0.6, wheat_sell_price 30→29, labor_reserve_buffer 92→95, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, MELON_PRICE_CUSHION 100→90, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, SPREAD_W 1.25→1.0 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `57c65535c63e` | M2 | paired | +3,091 | 1.6 | 6-4 | -28,471 | alive | open_wheat 7→6, early_hire_days 5→7, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13, SPREAD_W 1.25→1.5 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `89822c12eba2` | wide | crossover | +3,032 | 1.6 | 8-2 | -22,099 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→4, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, NEAR_RADIUS 2→4, MAX_SHEEP 14→10 · blocks: hiring |
| `71f26bab2993` | v312 | mutate | +2,962 | 1.6 | 7-3 | -24,707 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, open_wheat 7→6, demand_share 0.55→0.45, max_animals 17→19, wheat_water_tier 0→1, setup_capital_share 0.25→0.45, labor_reserve_buffer 92→102, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→27, OPP_GROWTH 1.4→1.2, SPREAD_CAP 3→4 |
| `db61805ecfa9` | M2 | mutate | +2,910 | 2.2 | 8-2 | -22,620 | held_fail | open_wheat 7→6, feed_spare_poor 0→1, max_animals 17→18, wheat_cap 22→12, ROUTE_LEN 3→2, CROP_SWEEP_LEN 6→7, CROP_SWEEP_RADIUS 5→4, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3, MAX_SHEEP 14→13 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `ef9bb31c7a35` | c1 | mutate | +2,574 | 1.6 | 8-2 | -24,298 | alive | melon_floor 0→150, open_melons 8→10, open_wheat 7→3, demand_share 0.55→0.6, wheat_per_animal 0.0→0.2, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→6, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→102 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `961ab6fb4730` | M2 | mutate | +2,342 | 1.8 | 6-4 | -19,878 | alive | melon_floor 0→150, harvest_min 1→3, wheat_tiles 0→1, load_per_hand 20→21, open_melons 8→9, open_wheat 7→6, wheat_cap 22→20, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `a029795a2e69` | queue | archive_crossover:crossover_g000050_20260910-100503_1 | +2,298 | 1.6 | 7-3 | -25,004 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, MAX_HANDS 14→12, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85 · blocks: hiring |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=35
- M2: best +3,091 (`57c65535c63e`), n=29
- c1: best +2,683 (`5fd05605827b`), n=50
- queue: best +4,836 (`7ec902ce836b`), n=85
- v312: best +4,008 (`bfe4bb8d3609`), n=41
- wide: best +3,032 (`89822c12eba2`), n=44

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +6,946 | 84 | 100 | 24 | 273 | 9.62 | 84: +336 (n=2), 102: +101 (n=12), 74: -125 (n=2), 115: -403 (n=3), 85: -1,124 (n=9), 83: -1,174 (n=3), 90: -1,291 (n=2), 100: -1,527 (n=223), 71: -2,386 (n=2), 114: -3,075 (n=2), 92: -3,202 (n=7), 110: -3,785 (n=4), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +5,721 | 12 | 22 | 11 | 283 | 5.04 | 12: +1,798 (n=5), 13: -621 (n=28), 25: -1,197 (n=38), 21: -1,542 (n=2), 22: -1,663 (n=171), 20: -2,006 (n=10), 17: -2,111 (n=3), 18: -2,797 (n=15), 24: -3,679 (n=5), 23: -3,923 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +5,648 | 39 | 38 | 16 | 279 | 2.75 | 39: +195 (n=27), 33: -996 (n=2), 32: -1,047 (n=6), 35: -1,082 (n=40), 34: -1,568 (n=95), 38: -2,095 (n=90), 43: -3,008 (n=10), 41: -3,113 (n=2), 42: -4,467 (n=2), 46: -5,356 (n=3), 45: -5,453 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +5,497 | 13 | 14 | 7 | 284 | 3.73 | 13: -57 (n=23), 12: -743 (n=42), 14: -1,803 (n=192), 11: -2,042 (n=6), 15: -2,476 (n=13), 16: -3,013 (n=5), 10: -5,553 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +5,434 | 6 | 8 | 8 | 284 | 2.52 | 6: -255 (n=2), 10: -1,220 (n=119), 11: -1,322 (n=16), 9: -1,388 (n=14), 8: -1,844 (n=125), 7: -3,578 (n=2), 4: -4,132 (n=2), 5: -5,688 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,097 | 2 | 2 | 4 | 284 | 2.45 | 2: -1,374 (n=245), 1: -2,693 (n=33), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,015 | 2 | 3 | 3 | 284 | 1.49 | 2: -375 (n=33), 3: -1,533 (n=236), 4: -5,390 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,778 | 19 | 20 | 9 | 283 | 4.09 | 19: -960 (n=49), 20: -1,485 (n=180), 22: -1,696 (n=4), 18: -1,835 (n=9), 17: -2,506 (n=3), 21: -2,616 (n=29), 23: -2,685 (n=7), 24: -5,738 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +4,758 | 6 | 7 | 8 | 284 | 4.72 | 6: +25 (n=12), 3: -395 (n=15), 9: -709 (n=5), 4: -840 (n=40), 7: -1,846 (n=203), 10: -3,113 (n=2), 5: -3,711 (n=2), 8: -4,733 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +4,494 | 58 | 92 | 27 | 271 | 8.82 | 58: +711 (n=12), 124: +10 (n=6), 121: +6 (n=2), 95: -37 (n=4), 107: -755 (n=7), 102: -803 (n=4), 88: -1,408 (n=2), 92: -1,697 (n=190), 73: -1,731 (n=2), 11: -1,812 (n=26), 94: -2,049 (n=2), 150: -2,267 (n=10), 59: -3,300 (n=2), 76: -3,783 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,970 | frontier | frontier | 2 | 284 | 0.86 | frontier: -1,322 (n=264), v312: -5,292 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +3,929 | 19 | 17 | 8 | 283 | 4.32 | 19: +593 (n=3), 18: -744 (n=13), 14: -992 (n=3), 17: -1,461 (n=215), 16: -1,758 (n=5), 15: -1,911 (n=21), 20: -3,336 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +3,866 | 2 | 2 | 3 | 284 | 1.83 | 2: -1,407 (n=268), 1: -4,469 (n=8), 3: -5,272 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,690 | 0.6 | 0.55 | 9 | 282 | 3.29 | 0.6: -350 (n=18), 0.65: -474 (n=21), 0.45: -997 (n=26), 0.55: -1,603 (n=173), 0.5: -2,626 (n=34), 0.75: -2,732 (n=2), 0.3: -4,040 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +3,265 | 31 | 30 | 10 | 283 | 3.52 | 31: -1,149 (n=3), 30: -1,416 (n=142), 34: -1,432 (n=3), 25: -1,576 (n=86), 26: -1,853 (n=26), 28: -1,913 (n=7), 29: -2,014 (n=9), 36: -2,913 (n=4), 27: -4,415 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,261 | 8 | 5 | 8 | 283 | 4.32 | 8: -599 (n=5), 4: -861 (n=10), 7: -1,165 (n=12), 3: -1,476 (n=33), 5: -1,638 (n=215), 6: -2,961 (n=3), 0: -3,861 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +3,238 | 16 | 17 | 8 | 283 | 2.69 | 16: -8 (n=5), 18: -1,097 (n=12), 19: -1,454 (n=94), 17: -1,561 (n=149), 22: -2,538 (n=11), 20: -3,144 (n=3), 14: -3,246 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,197 | 0.45 | 0.25 | 10 | 283 | 5.52 | 0.45: -1,270 (n=15), 0.25: -1,289 (n=205), 0.2: -1,513 (n=5), 0.4: -1,659 (n=26), 0.15: -1,761 (n=4), 0.3: -3,075 (n=2), 0.5: -3,672 (n=3), 0.35: -4,179 (n=21), 0.05: -4,467 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +3,130 | 14 | 14 | 5 | 284 | 3.19 | 14: -1,307 (n=238), 12: -1,660 (n=9), 11: -2,539 (n=4), 13: -3,511 (n=30), 10: -4,437 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +2,966 | 3 | 0 | 4 | 284 | 2.69 | 3: -204 (n=2), 0: -1,542 (n=262), 1: -2,255 (n=14), 2: -3,170 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=18)
- (16, 3, 6): +4,008 (n=2)
- (7, 3, 4): +3,920 (n=25)
- (10, 3, 5): +3,091 (n=12)
- (14, 3, 6): +3,066 (n=6)
- (7, 3, 3): +3,032 (n=14)
- (9, 3, 4): +2,962 (n=19)
- (9, 3, 3): +2,910 (n=4)
- (11, 3, 5): +2,663 (n=13)
- (11, 3, 6): +2,574 (n=11)
- (9, 3, 5): +2,565 (n=6)
- (8, 3, 5): +2,298 (n=11)
- (6, 3, 3): +2,293 (n=5)
- (6, 3, 5): +2,260 (n=2)
- (15, 3, 6): +2,143 (n=5)

_Generated 2026-09-10 10:05. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 129 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=129); harvest_min=1–3 (n=129); wheat_tiles=0–5 (n=129); wheat_stock=0–19 (n=129); min_hands=3–6 (n=129); load_per_hand=12–25 (n=129); geese=0–2 (n=129); open_melons=4–12 (n=129)
- **Evidence:** 129 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 10:05. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._