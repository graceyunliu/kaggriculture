# Evolution run 20260910-055925

Frontier opponent: `H32.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 1.82 h · candidates evaluated this run: 1183 · games 20,052 (11,020/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 476 | 952 |
| dead_pattern | 186 | 372 |
| dead_smoke | 157 | 1256 |
| alive | 364 | 17472 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 20151 · held-out evaluated: 0 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | — | — | None-None | — | — | — | —-— |
| C1 | -37,097 | -9.3 | 0-10 | -27,047 | — | — | —-— |

## Held-out results (the only numbers that count)

None reached held-out this run.

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `0c3989f7d742` | H32 | crossover | -15,269 | -3.2 | 2-8 | -16,318 | alive | melon_floor 150→0, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, labor_reserve_buffer 50→92, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25, SPREAD_CAP 5→3 |
| `52b3d5cc236e` | v312 | crossover | -15,275 | -3.0 | 3-7 | -28,470 | alive | harvest_min 2→3, geese 0→1, open_melons 8→10, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→45, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11 |
| `fe4745b56024` | queue | archive_crossover:crossover_g000675_20260905-224724_0 | -15,412 | -3.3 | 2-8 | -17,273 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `d62b0acfe68b` | queue | archive_crossover:crossover_g001100_20260907-023009_1 | -15,495 | -2.9 | 3-7 | -15,324 | alive | open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, setup_capital_share 0.25→0.2, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `9d926b677e93` | H32 | mutate | -15,512 | -3.2 | 2-8 | -16,318 | alive | melon_floor 150→0, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, labor_reserve_buffer 50→66, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→39, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25, SPREAD_CAP 5→3 |
| `a3436012d4f9` | queue | archive_crossover:crossover_g000725_20260906-214654_0 | -15,590 | -3.3 | 2-8 | -16,712 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `667332b39bf5` | queue | archive_crossover:crossover_g000850_20260905-205857_1 | -15,738 | -3.0 | 3-7 | -27,827 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `97e03be128cb` | queue | archive_crossover:crossover_g000400_20260906-211828_1 | -15,791 | -3.5 | 2-8 | -16,760 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `7056bf4454ac` | queue | archive_crossover:crossover_g000600_20260907-014214_1 | -15,811 | -3.0 | 3-7 | -15,804 | alive | harvest_min 2→1, open_melons 8→10, early_hire_days 5→8, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `2286322870c4` | v312 | mutate | -15,854 | -3.0 | 3-7 | -14,497 | alive | harvest_min 2→3, open_melons 8→10, early_hire_days 5→8, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→42, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5 |
| `a442a9ceb68e` | queue | archive_crossover:crossover_g000075_20260906-225544_1 | -15,885 | -3.6 | 2-8 | -17,122 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, SPREAD_W 1.0→1.25 |
| `5b63d512ad81` | queue | archive_crossover:crossover_g000775_20260906-215507_0 | -15,896 | -3.3 | 2-8 | -15,996 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `081b43704bb8` | queue | archive_crossover:crossover_g000125_20260905-215729_0 | -15,916 | -3.1 | 2-8 | -28,354 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→7, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `165447af42cc` | queue | mutate | -15,936 | -3.5 | 2-8 | -16,892 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→0, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3 |
| `512e53fe15bc` | wide | paired | -16,047 | -3.7 | 1-9 | -15,964 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→37, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |

## Islands (best dev margin, population size)

- H32: best -15,269 (`0c3989f7d742`), n=2697
- M2: best -16,102 (`8b77b3e994bc`), n=2751
- c1: best -16,235 (`18fc0546be4a`), n=3549
- queue: best -15,412 (`fe4745b56024`), n=4685
- v312: best -15,275 (`52b3d5cc236e`), n=3248
- wide: best -16,047 (`512e53fe15bc`), n=3221

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +17,280 | 120 | 50 | 147 | 20144 | 66.56 | 120: -24,488 (n=13), 118: -25,349 (n=2), 138: -25,750 (n=2), 141: -28,023 (n=6), 8: -28,586 (n=8), 5: -28,630 (n=62), 143: -28,964 (n=3), 112: -29,479 (n=14), 26: -30,065 (n=10), 70: -30,068 (n=101), 27: -30,093 (n=41), 97: -30,326 (n=50), 106: -30,367 (n=53), 89: -30,394 (n=34), 19: -30,408 (n=20), 63: -30,424 (n=371), 18: -30,458 (n=1432), 58: -30,561 (n=175), 74: -30,590 (n=459), 80: -30,675 (n=20), 35: -30,680 (n=18), 48: -30,692 (n=582), 92: -30,722 (n=557), 60: -30,728 (n=39), 117: -30,761 (n=3), 150: -30,813 (n=325), 65: -30,911 (n=177), 50: -30,981 (n=9721), 49: -30,988 (n=106), 96: -31,232 (n=9), 44: -31,344 (n=55), 72: -31,363 (n=16), 30: -31,400 (n=65), 61: -31,428 (n=133), 86: -31,454 (n=10), 40: -31,470 (n=120), 42: -31,483 (n=995), 94: -31,527 (n=22), 71: -31,541 (n=36), 66: -31,627 (n=392), 108: -31,642 (n=10), 85: -31,657 (n=15), 73: -31,710 (n=23), 14: -31,712 (n=43), 36: -31,713 (n=170), 104: -31,742 (n=6), 56: -31,811 (n=27), 45: -31,824 (n=129), 38: -31,829 (n=29), 51: -31,851 (n=26), 110: -31,911 (n=8), 53: -31,932 (n=126), 144: -32,005 (n=12), 9: -32,055 (n=20), 57: -32,144 (n=90), 59: -32,150 (n=27), 119: -32,268 (n=4), 87: -32,316 (n=24), 33: -32,365 (n=27), 55: -32,466 (n=820), 25: -32,475 (n=13), 115: -32,512 (n=8), 39: -32,547 (n=63), 28: -32,568 (n=23), 41: -32,597 (n=59), 54: -32,716 (n=31), 62: -32,741 (n=24), 134: -32,782 (n=3), 84: -32,795 (n=18), 52: -32,865 (n=24), 109: -32,944 (n=4), 95: -32,957 (n=7), 17: -32,977 (n=15), 125: -33,009 (n=2), 43: -33,057 (n=23), 4: -33,111 (n=40), 122: -33,131 (n=2), 20: -33,148 (n=14), 98: -33,151 (n=21), 68: -33,247 (n=19), 6: -33,253 (n=15), 88: -33,282 (n=15), 93: -33,297 (n=10), 31: -33,327 (n=21), 21: -33,335 (n=14), 78: -33,339 (n=17), 113: -33,352 (n=17), 0: -33,357 (n=264), 69: -33,413 (n=32), 2: -33,419 (n=4), 83: -33,497 (n=118), 81: -33,523 (n=32), 103: -33,542 (n=11), 47: -33,560 (n=40), 22: -33,586 (n=19), 102: -33,689 (n=6), 24: -33,733 (n=26), 32: -33,760 (n=15), 76: -33,828 (n=20), 13: -33,976 (n=8), 82: -34,020 (n=52), 90: -34,046 (n=8), 15: -34,073 (n=13), 111: -34,111 (n=8), 135: -34,236 (n=2), 79: -34,292 (n=26), 64: -34,299 (n=26), 99: -34,315 (n=77), 1: -34,445 (n=10), 10: -34,451 (n=15), 11: -34,452 (n=20), 140: -34,453 (n=4), 46: -34,592 (n=40), 7: -34,648 (n=12), 12: -34,899 (n=15), 101: -34,931 (n=14), 107: -35,073 (n=7), 16: -35,226 (n=20), 37: -35,307 (n=18), 77: -35,356 (n=250), 34: -35,380 (n=77), 3: -35,585 (n=8), 91: -35,640 (n=11), 100: -35,769 (n=65), 136: -35,844 (n=59), 23: -36,020 (n=26), 75: -36,234 (n=16), 67: -36,238 (n=22), 129: -36,265 (n=101), 128: -36,508 (n=3), 105: -36,563 (n=3), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 29: -38,710 (n=79), 127: -39,229 (n=3), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,834 | 25 | 30 | 26 | 20150 | 11.19 | 25: -30,918 (n=9825), 26: -30,986 (n=736), 30: -31,137 (n=6591), 31: -31,913 (n=160), 29: -32,181 (n=167), 27: -32,409 (n=296), 28: -33,357 (n=1531), 32: -33,625 (n=209), 41: -34,692 (n=4), 35: -35,198 (n=208), 45: -35,319 (n=2), 33: -35,543 (n=163), 37: -35,606 (n=32), 34: -35,790 (n=89), 38: -36,301 (n=27), 39: -36,375 (n=14), 36: -36,875 (n=46), 42: -36,946 (n=4), 46: -38,521 (n=3), 40: -38,534 (n=17), 43: -38,819 (n=7), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,586 (n=9), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,209 | 1 | 0 | 35 | 20148 | 24.96 | 1: -30,317 (n=1962), 9: -30,938 (n=114), 0: -31,186 (n=16344), 22: -31,572 (n=3), 2: -32,749 (n=233), 6: -33,176 (n=155), 8: -33,198 (n=100), 4: -33,529 (n=147), 3: -34,357 (n=235), 19: -34,452 (n=9), 11: -34,699 (n=81), 17: -34,967 (n=19), 20: -34,967 (n=8), 7: -35,323 (n=119), 13: -35,358 (n=58), 5: -35,384 (n=232), 28: -35,676 (n=3), 12: -35,729 (n=42), 14: -35,930 (n=32), 16: -36,049 (n=24), 15: -36,478 (n=38), 23: -36,568 (n=8), 10: -36,914 (n=64), 18: -36,999 (n=24), 24: -37,048 (n=7), 27: -37,332 (n=2), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,234 (n=15), 26: -40,268 (n=3), 29: -40,595 (n=44), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,922 | 3 | 3 | 4 | 20151 | 2.61 | 3: -30,914 (n=18174), 2: -35,613 (n=1405), 4: -36,307 (n=550), 5: -42,836 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,263 | 6 | 6 | 8 | 20151 | 6.13 | 6: -30,805 (n=17947), 5: -34,632 (n=895), 7: -36,735 (n=479), 4: -37,565 (n=549), 3: -37,641 (n=169), 8: -38,109 (n=77), 9: -40,142 (n=27), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,689 | 13 | 20 | 11 | 20151 | 4.58 | 13: -30,338 (n=48), 16: -30,935 (n=437), 17: -31,077 (n=6891), 19: -31,309 (n=1112), 18: -31,364 (n=1062), 11: -31,405 (n=4), 14: -31,628 (n=151), 20: -31,629 (n=10224), 15: -32,185 (n=190), 12: -33,855 (n=24), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +9,924 | 10 | 8 | 11 | 20151 | 8.37 | 10: -30,837 (n=17172), 7: -32,318 (n=687), 8: -34,730 (n=1117), 9: -35,121 (n=674), 6: -35,309 (n=206), 5: -35,659 (n=33), 11: -37,933 (n=88), 4: -37,936 (n=31), 12: -38,070 (n=62), 14: -39,599 (n=36), 13: -40,760 (n=45) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +9,659 | 130 | 100 | 101 | 20151 | 61.67 | 130: -29,781 (n=16), 80: -30,045 (n=497), 93: -30,226 (n=454), 120: -30,297 (n=23), 50: -30,415 (n=272), 91: -30,416 (n=112), 81: -30,537 (n=99), 62: -30,567 (n=11), 86: -30,571 (n=1128), 66: -30,748 (n=40), 78: -30,864 (n=198), 85: -30,883 (n=109), 123: -30,901 (n=58), 63: -30,948 (n=14), 129: -30,960 (n=23), 100: -31,023 (n=12503), 90: -31,113 (n=206), 59: -31,163 (n=6), 125: -31,180 (n=96), 111: -31,285 (n=45), 107: -31,313 (n=31), 61: -31,371 (n=3), 65: -31,453 (n=8), 92: -31,472 (n=36), 147: -31,607 (n=7), 115: -31,609 (n=37), 117: -31,713 (n=136), 99: -31,724 (n=50), 133: -31,740 (n=10), 94: -31,805 (n=41), 83: -31,819 (n=130), 138: -31,825 (n=6), 113: -31,924 (n=26), 103: -31,927 (n=37), 87: -31,948 (n=25), 64: -31,993 (n=16), 84: -32,045 (n=114), 95: -32,092 (n=49), 132: -32,285 (n=12), 88: -32,307 (n=81), 102: -32,333 (n=48), 149: -32,426 (n=4), 110: -32,447 (n=32), 82: -32,452 (n=28), 70: -32,455 (n=21), 104: -32,469 (n=697), 71: -32,526 (n=23), 53: -32,538 (n=6), 128: -32,590 (n=39), 127: -32,636 (n=41), 105: -32,660 (n=152), 114: -32,696 (n=36), 109: -32,740 (n=62), 119: -32,778 (n=24), 98: -32,827 (n=75), 97: -32,947 (n=62), 67: -32,961 (n=12), 76: -33,107 (n=25), 112: -33,134 (n=228), 89: -33,250 (n=202), 57: -33,366 (n=7), 122: -33,424 (n=41), 68: -33,466 (n=12), 116: -33,485 (n=82), 141: -33,486 (n=4), 69: -33,501 (n=14), 146: -33,664 (n=4), 96: -33,717 (n=56), 101: -33,730 (n=50), 126: -33,773 (n=31), 55: -33,777 (n=5), 135: -33,828 (n=537), 56: -33,830 (n=7), 108: -34,231 (n=36), 74: -34,234 (n=37), 124: -34,343 (n=29), 143: -34,383 (n=13), 75: -34,408 (n=62), 72: -34,412 (n=15), 106: -34,657 (n=54), 121: -34,838 (n=20), 79: -35,020 (n=82), 134: -35,055 (n=11), 137: -35,119 (n=6), 139: -35,190 (n=10), 136: -35,406 (n=9), 144: -35,500 (n=3), 150: -35,967 (n=191), 131: -35,981 (n=19), 52: -36,201 (n=4), 142: -36,242 (n=8), 118: -36,780 (n=18), 77: -37,054 (n=30), 73: -37,334 (n=16), 148: -37,549 (n=4), 51: -37,583 (n=6), 58: -37,802 (n=7), 140: -38,416 (n=3), 54: -38,470 (n=4), 145: -39,395 (n=13), 60: -39,441 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,509 | 0.0 | 0.0 | 13 | 20151 | 10.38 | 0.0: -31,074 (n=17642), 0.1: -33,111 (n=1198), 0.4: -33,621 (n=120), 0.2: -33,823 (n=717), 0.3: -34,017 (n=255), 0.5: -34,627 (n=72), 1.1: -34,978 (n=7), 0.7: -35,518 (n=19), 0.6: -36,974 (n=71), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -38,489 (n=11), 0.8: -40,582 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,483 | 20 | 20 | 15 | 20151 | 7.94 | 20: -30,752 (n=12005), 19: -30,899 (n=5564), 18: -31,678 (n=468), 17: -34,360 (n=783), 16: -36,396 (n=182), 21: -36,751 (n=432), 15: -37,339 (n=94), 23: -37,899 (n=118), 22: -37,917 (n=227), 26: -38,356 (n=52), 14: -38,709 (n=46), 13: -38,834 (n=22), 25: -39,099 (n=27), 24: -39,331 (n=107), 12: -40,235 (n=24) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +9,262 | 7 | 7 | 8 | 20151 | 6.14 | 7: -30,780 (n=17992), 6: -36,372 (n=1032), 5: -36,555 (n=85), 8: -36,582 (n=679), 10: -36,633 (n=139), 9: -37,348 (n=130), 4: -37,594 (n=83), 3: -40,042 (n=11) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,215 | 0.55 | 0.5 | 15 | 20151 | 7.76 | 0.55: -30,485 (n=11770), 0.5: -31,761 (n=4537), 0.65: -31,794 (n=1379), 0.7: -32,588 (n=358), 0.75: -32,622 (n=153), 0.6: -33,454 (n=499), 0.8: -34,431 (n=79), 0.45: -34,652 (n=591), 0.9: -35,790 (n=13), 0.35: -35,912 (n=194), 0.4: -36,089 (n=231), 0.85: -36,822 (n=17), 0.95: -36,836 (n=4), 1.0: -38,742 (n=9), 0.3: -39,700 (n=317) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,535 | 2 | 2 | 4 | 20151 | 2.83 | 2: -31,138 (n=19302), 1: -37,017 (n=699), 3: -38,253 (n=53), 0: -39,674 (n=97) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +8,324 | 0 | 0 | 9 | 20151 | 7.18 | 0: -31,108 (n=18321), 1: -33,967 (n=948), 2: -34,222 (n=399), 3: -34,928 (n=297), 4: -34,934 (n=118), 5: -35,355 (n=27), 7: -35,571 (n=8), 6: -37,848 (n=28), 8: -39,432 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,181 | 13 | 12 | 11 | 20151 | 8.24 | 13: -30,840 (n=1730), 14: -31,304 (n=16918), 11: -32,118 (n=260), 12: -32,444 (n=831), 9: -32,665 (n=36), 6: -34,639 (n=5), 7: -35,242 (n=13), 10: -35,350 (n=317), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,076 | 11 | 13 | 9 | 20151 | 4.21 | 11: -31,094 (n=908), 14: -31,106 (n=3654), 13: -31,367 (n=11673), 12: -31,403 (n=2657), 15: -31,725 (n=636), 10: -33,043 (n=161), 16: -33,511 (n=375), 9: -36,608 (n=64), 8: -39,170 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,593 | frontier | frontier | 2 | 20151 | 0.91 | frontier: -31,066 (n=19259), v312: -38,659 (n=892) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 20151 | 9.61 | 6: -30,481 (n=23), 21: -30,851 (n=3765), 22: -30,942 (n=10178), 23: -31,349 (n=899), 14: -31,397 (n=30), 20: -31,446 (n=762), 16: -31,695 (n=127), 13: -31,951 (n=40), 17: -32,355 (n=954), 25: -32,650 (n=1543), 18: -32,943 (n=710), 24: -33,241 (n=503), 15: -33,253 (n=67), 19: -33,273 (n=247), 12: -34,065 (n=16), 9: -34,566 (n=60), 10: -34,911 (n=71), 11: -36,015 (n=40), 7: -36,374 (n=23), 5: -36,852 (n=87), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,079 | 2 | 2 | 3 | 20151 | 1.83 | 2: -31,032 (n=19025), 1: -37,629 (n=1055), 3: -38,111 (n=71) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,536 | 21 | 40 | 31 | 20151 | 7.74 | 21: -30,358 (n=2), 34: -30,360 (n=375), 49: -30,688 (n=526), 43: -30,783 (n=5684), 33: -30,811 (n=74), 38: -30,830 (n=4812), 47: -30,852 (n=353), 44: -30,907 (n=600), 45: -31,274 (n=916), 30: -31,387 (n=80), 37: -31,521 (n=801), 39: -31,622 (n=768), 28: -31,851 (n=24), 26: -31,899 (n=70), 27: -31,953 (n=13), 25: -32,002 (n=10), 50: -32,242 (n=575), 29: -32,324 (n=20), 32: -32,683 (n=70), 40: -32,777 (n=3030), 36: -32,843 (n=231), 31: -32,889 (n=52), 42: -32,948 (n=256), 41: -33,037 (n=170), 35: -33,312 (n=280), 46: -33,599 (n=157), 48: -33,870 (n=90), 20: -34,655 (n=71), 23: -35,631 (n=7), 24: -36,135 (n=26), 22: -36,894 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3716)
- (9, 3, 6): -16,461 (n=2657)
- (12, 4, 6): -16,525 (n=607)
- (10, 3, 6): -16,840 (n=3314)
- (8, 3, 5): -16,866 (n=340)
- (8, 3, 6): -17,253 (n=944)
- (10, 4, 6): -17,975 (n=2916)
- (11, 3, 6): -18,175 (n=702)
- (11, 4, 6): -19,867 (n=668)
- (17, 3, 6): -20,013 (n=73)
- (8, 4, 6): -21,051 (n=902)
- (13, 3, 6): -21,440 (n=394)
- (13, 4, 6): -21,564 (n=268)
- (14, 3, 6): -21,679 (n=301)
- (8, 3, 4): -22,126 (n=99)

_Generated 2026-09-10 07:48. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 10320 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=10320); harvest_min=1–3 (n=10320); wheat_tiles=0–8 (n=10320); wheat_stock=0–40 (n=10320); min_hands=3–6 (n=10320); load_per_hand=12–26 (n=10320); geese=0–2 (n=10320); open_melons=4–14 (n=10320)
- **Evidence:** 10320 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 127 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=127); harvest_min=1–3 (n=127); wheat_tiles=0–2 (n=127); wheat_stock=0–6 (n=127); min_hands=3–6 (n=127); load_per_hand=15–23 (n=127); geese=0–2 (n=127); open_melons=7–13 (n=127)
- **Evidence:** 127 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 78 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=78); harvest_min=1–3 (n=78); wheat_tiles=0–3 (n=78); wheat_stock=0–40 (n=78); min_hands=3–6 (n=78); load_per_hand=12–26 (n=78); geese=0–2 (n=78); open_melons=4–13 (n=78)
- **Evidence:** 78 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 52 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=52); harvest_min=1–3 (n=52); wheat_tiles=0–8 (n=52); wheat_stock=0–39 (n=52); min_hands=3–6 (n=52); load_per_hand=12–23 (n=52); geese=0–2 (n=52); open_melons=6–14 (n=52)
- **Evidence:** 52 candidates, multiple seeds. Confidence: high

### None (observed in 23 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=23); harvest_min=1–3 (n=23); wheat_tiles=0; wheat_stock=0–11 (n=23); min_hands=3–6 (n=23); load_per_hand=12–18 (n=23); geese=0–2 (n=23); open_melons=7–14 (n=23)
- **Evidence:** 23 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 07:48. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._