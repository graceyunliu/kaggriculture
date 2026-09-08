# Evolution run 20260908-165405

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1245 · games 24,338 (12,150/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 427 | 854 |
| dead_pattern | 210 | 420 |
| dead_smoke | 153 | 1224 |
| alive | 455 | 21840 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 12679 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1520
- M2: best -16,461 (`0c25e1226b27`), n=1564
- c1: best -16,310 (`23734cef4da1`), n=2293
- queue: best -15,412 (`fe4745b56024`), n=3152
- v312: best -15,275 (`52b3d5cc236e`), n=2163
- wide: best -16,047 (`512e53fe15bc`), n=1987

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +22,242 | 120 | 50 | 143 | 12670 | 65.24 | 120: -19,526 (n=4), 141: -24,735 (n=4), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,428 (n=2), 19: -28,045 (n=14), 112: -28,098 (n=12), 5: -28,572 (n=45), 35: -28,878 (n=10), 27: -29,195 (n=34), 56: -29,255 (n=13), 71: -29,378 (n=25), 92: -29,643 (n=311), 89: -29,645 (n=29), 58: -29,647 (n=92), 26: -29,760 (n=7), 18: -29,973 (n=718), 74: -30,126 (n=182), 49: -30,375 (n=72), 61: -30,449 (n=93), 63: -30,467 (n=198), 51: -30,565 (n=12), 72: -30,614 (n=8), 48: -30,761 (n=502), 50: -30,787 (n=6263), 65: -30,824 (n=121), 80: -30,851 (n=12), 150: -30,986 (n=147), 86: -31,018 (n=9), 106: -31,136 (n=7), 60: -31,180 (n=28), 144: -31,182 (n=2), 42: -31,197 (n=716), 40: -31,207 (n=89), 85: -31,279 (n=9), 66: -31,317 (n=211), 33: -31,322 (n=21), 45: -31,409 (n=108), 2: -31,685 (n=2), 57: -31,735 (n=82), 93: -31,753 (n=7), 73: -31,772 (n=16), 9: -31,796 (n=14), 96: -31,865 (n=7), 36: -31,890 (n=104), 97: -31,904 (n=25), 70: -32,076 (n=30), 21: -32,085 (n=9), 14: -32,112 (n=19), 39: -32,212 (n=51), 62: -32,220 (n=17), 59: -32,251 (n=15), 110: -32,277 (n=4), 25: -32,369 (n=7), 69: -32,403 (n=22), 115: -32,512 (n=8), 84: -32,518 (n=13), 94: -32,527 (n=15), 103: -32,559 (n=8), 76: -32,669 (n=12), 113: -32,757 (n=11), 38: -32,804 (n=17), 20: -32,812 (n=6), 109: -32,844 (n=3), 88: -32,953 (n=10), 31: -33,053 (n=13), 55: -33,095 (n=512), 108: -33,264 (n=5), 104: -33,266 (n=4), 68: -33,293 (n=12), 6: -33,331 (n=10), 119: -33,340 (n=2), 41: -33,381 (n=37), 4: -33,399 (n=36), 0: -33,411 (n=188), 24: -33,425 (n=18), 95: -33,449 (n=5), 83: -33,462 (n=97), 13: -33,499 (n=7), 23: -33,511 (n=11), 52: -33,514 (n=13), 22: -33,559 (n=15), 43: -33,691 (n=18), 98: -33,709 (n=18), 90: -33,822 (n=7), 81: -33,835 (n=24), 54: -33,902 (n=18), 30: -33,916 (n=15), 32: -33,992 (n=9), 82: -34,104 (n=41), 111: -34,111 (n=8), 44: -34,233 (n=20), 10: -34,299 (n=13), 102: -34,320 (n=4), 64: -34,325 (n=19), 99: -34,331 (n=70), 78: -34,340 (n=10), 28: -34,350 (n=19), 136: -34,374 (n=36), 1: -34,413 (n=5), 134: -34,464 (n=2), 7: -34,621 (n=7), 15: -34,699 (n=8), 46: -34,716 (n=30), 37: -34,729 (n=11), 16: -34,787 (n=14), 107: -34,996 (n=4), 79: -35,022 (n=13), 77: -35,100 (n=218), 34: -35,155 (n=56), 100: -35,183 (n=42), 101: -35,278 (n=11), 17: -35,508 (n=6), 11: -35,563 (n=13), 91: -35,821 (n=9), 87: -35,852 (n=10), 129: -35,921 (n=75), 53: -35,980 (n=24), 47: -36,077 (n=18), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 67: -36,875 (n=17), 145: -36,990 (n=7), 29: -37,119 (n=23), 75: -37,220 (n=8), 114: -37,341 (n=4), 12: -37,385 (n=10), 127: -38,268 (n=2), 140: -38,489 (n=3), 131: -38,847 (n=2), 124: -39,372 (n=2), 132: -39,931 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,124 | 26 | 30 | 25 | 12678 | 10.54 | 26: -30,629 (n=408), 25: -30,716 (n=6095), 30: -30,901 (n=4085), 31: -31,610 (n=115), 29: -32,027 (n=106), 27: -32,469 (n=210), 28: -33,579 (n=1080), 35: -34,680 (n=171), 32: -34,796 (n=124), 38: -35,532 (n=17), 41: -35,551 (n=2), 33: -35,614 (n=108), 37: -35,850 (n=22), 34: -36,089 (n=57), 39: -36,523 (n=10), 42: -36,846 (n=2), 36: -37,906 (n=32), 40: -38,012 (n=10), 46: -38,521 (n=3), 44: -38,790 (n=5), 47: -39,384 (n=2), 50: -40,198 (n=7), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,431 | 3 | 3 | 4 | 12679 | 2.61 | 3: -30,757 (n=11438), 2: -35,925 (n=884), 4: -36,532 (n=341), 5: -43,188 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,227 | 1 | 0 | 33 | 12677 | 25.53 | 1: -30,300 (n=740), 0: -31,032 (n=10849), 9: -31,098 (n=86), 22: -31,539 (n=2), 2: -32,575 (n=121), 4: -33,333 (n=77), 8: -33,450 (n=66), 17: -33,465 (n=11), 6: -33,493 (n=69), 5: -34,225 (n=118), 11: -34,342 (n=56), 19: -34,546 (n=5), 3: -34,619 (n=155), 7: -35,675 (n=73), 13: -35,887 (n=39), 14: -36,260 (n=21), 12: -36,313 (n=26), 28: -36,361 (n=2), 18: -36,506 (n=19), 16: -36,588 (n=9), 23: -36,694 (n=6), 15: -36,765 (n=26), 20: -36,836 (n=5), 10: -37,294 (n=42), 24: -37,504 (n=4), 21: -38,756 (n=6), 39: -38,995 (n=8), 26: -40,268 (n=3), 40: -41,262 (n=6), 29: -41,310 (n=23), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,541 | 0.0 | 0.0 | 13 | 12679 | 10.17 | 0.0: -30,887 (n=10892), 0.1: -33,016 (n=882), 0.2: -33,847 (n=538), 0.4: -34,144 (n=75), 0.3: -34,509 (n=147), 0.5: -34,985 (n=46), 1.1: -35,241 (n=6), 0.7: -36,163 (n=16), 0.9: -37,063 (n=4), 0.6: -37,193 (n=36), 1.0: -37,742 (n=23), 1.2: -39,081 (n=9), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 12678 | 62.36 | 61: -27,918 (n=2), 138: -28,049 (n=2), 69: -28,538 (n=7), 130: -28,649 (n=12), 80: -29,512 (n=126), 85: -30,083 (n=85), 65: -30,099 (n=5), 93: -30,162 (n=348), 81: -30,176 (n=71), 114: -30,288 (n=22), 86: -30,302 (n=565), 92: -30,325 (n=18), 91: -30,413 (n=79), 129: -30,419 (n=15), 111: -30,687 (n=33), 100: -30,703 (n=8033), 120: -30,726 (n=13), 62: -30,897 (n=5), 113: -30,977 (n=17), 84: -30,996 (n=59), 94: -31,021 (n=30), 133: -31,210 (n=9), 115: -31,211 (n=26), 107: -31,239 (n=21), 78: -31,253 (n=61), 125: -31,291 (n=83), 141: -31,447 (n=3), 64: -31,517 (n=9), 83: -31,549 (n=108), 147: -31,607 (n=7), 123: -31,609 (n=34), 70: -31,724 (n=16), 95: -31,833 (n=34), 63: -31,882 (n=9), 102: -31,919 (n=40), 82: -31,935 (n=21), 57: -31,969 (n=5), 132: -31,971 (n=11), 105: -32,069 (n=80), 103: -32,141 (n=23), 109: -32,142 (n=25), 149: -32,176 (n=3), 87: -32,233 (n=17), 99: -32,241 (n=30), 53: -32,281 (n=4), 66: -32,339 (n=13), 90: -32,520 (n=69), 104: -32,558 (n=504), 67: -32,561 (n=7), 55: -32,666 (n=3), 68: -32,715 (n=9), 71: -32,801 (n=19), 56: -32,821 (n=2), 128: -33,000 (n=20), 101: -33,002 (n=32), 119: -33,009 (n=14), 136: -33,061 (n=6), 112: -33,116 (n=194), 122: -33,164 (n=35), 127: -33,168 (n=25), 88: -33,335 (n=61), 97: -33,453 (n=51), 76: -33,459 (n=17), 117: -33,504 (n=65), 134: -33,531 (n=8), 89: -33,661 (n=139), 135: -33,777 (n=429), 96: -33,887 (n=38), 59: -33,898 (n=4), 79: -33,944 (n=38), 124: -34,000 (n=20), 143: -34,012 (n=11), 121: -34,025 (n=11), 126: -34,049 (n=23), 116: -34,074 (n=53), 110: -34,145 (n=19), 98: -34,314 (n=37), 74: -34,399 (n=29), 108: -34,468 (n=24), 75: -34,479 (n=58), 144: -34,772 (n=2), 137: -34,809 (n=4), 106: -34,885 (n=40), 150: -35,464 (n=163), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 77: -36,309 (n=16), 131: -36,462 (n=12), 148: -36,528 (n=3), 50: -36,575 (n=40), 58: -36,674 (n=4), 73: -37,196 (n=10), 118: -37,259 (n=13), 51: -37,500 (n=2), 72: -37,554 (n=9), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +11,435 | 13 | 20 | 11 | 12679 | 5.03 | 13: -30,454 (n=32), 17: -30,841 (n=3973), 14: -31,052 (n=107), 16: -31,121 (n=287), 18: -31,289 (n=586), 19: -31,372 (n=610), 20: -31,522 (n=6951), 15: -32,016 (n=111), 11: -32,310 (n=3), 12: -34,934 (n=12), 10: -41,889 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,893 | 6 | 6 | 8 | 12679 | 6.12 | 6: -30,692 (n=11292), 5: -34,673 (n=552), 7: -36,310 (n=341), 4: -37,269 (n=305), 3: -37,766 (n=111), 8: -38,279 (n=53), 9: -40,761 (n=19), 10: -41,585 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,728 | 20 | 20 | 15 | 12679 | 7.15 | 20: -30,455 (n=6893), 19: -30,974 (n=4032), 18: -31,740 (n=291), 17: -34,311 (n=639), 21: -36,247 (n=267), 16: -36,420 (n=119), 15: -37,262 (n=57), 23: -37,299 (n=60), 22: -37,714 (n=138), 14: -38,122 (n=31), 26: -38,726 (n=35), 24: -39,084 (n=66), 25: -39,206 (n=19), 13: -39,412 (n=17), 12: -41,183 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,683 | 6 | 18 | 21 | 12679 | 9.21 | 6: -29,449 (n=15), 14: -29,940 (n=16), 21: -30,460 (n=2116), 22: -30,761 (n=6163), 20: -31,274 (n=612), 23: -31,400 (n=579), 16: -32,259 (n=74), 25: -32,369 (n=1079), 17: -32,511 (n=665), 18: -32,882 (n=528), 24: -33,073 (n=378), 12: -33,342 (n=11), 19: -33,655 (n=170), 15: -33,782 (n=42), 13: -33,955 (n=22), 9: -33,961 (n=45), 10: -34,579 (n=64), 5: -35,963 (n=42), 11: -36,402 (n=33), 7: -36,441 (n=21), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,161 | 7 | 7 | 8 | 12679 | 6.08 | 7: -30,589 (n=11219), 6: -36,459 (n=757), 5: -36,531 (n=62), 8: -36,684 (n=411), 10: -36,797 (n=101), 9: -37,081 (n=85), 4: -38,504 (n=36), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,794 | 0.55 | 0.5 | 15 | 12679 | 6.89 | 0.55: -30,135 (n=6669), 0.65: -31,680 (n=1111), 0.5: -31,885 (n=3366), 0.75: -32,089 (n=89), 0.7: -32,214 (n=212), 0.6: -32,806 (n=302), 0.8: -33,195 (n=40), 0.45: -34,617 (n=395), 0.9: -35,286 (n=10), 0.85: -35,798 (n=11), 0.35: -36,070 (n=141), 0.4: -36,308 (n=137), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,929 (n=186) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +9,787 | 10 | 8 | 11 | 12679 | 8.25 | 10: -30,624 (n=10659), 7: -32,601 (n=380), 8: -34,811 (n=837), 9: -34,906 (n=472), 6: -35,463 (n=148), 5: -36,350 (n=19), 12: -38,056 (n=42), 4: -38,137 (n=22), 11: -38,543 (n=54), 14: -39,191 (n=25), 13: -40,410 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,711 | 0 | 0 | 9 | 12679 | 7.14 | 0: -30,948 (n=11472), 1: -34,068 (n=644), 2: -34,607 (n=253), 3: -34,934 (n=203), 4: -35,798 (n=64), 5: -36,331 (n=18), 7: -36,592 (n=4), 6: -37,436 (n=18), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +9,369 | 14 | 13 | 9 | 12679 | 4.4 | 14: -30,523 (n=1834), 13: -31,281 (n=7604), 11: -31,301 (n=694), 15: -31,373 (n=376), 12: -31,474 (n=1803), 16: -33,379 (n=215), 10: -33,946 (n=97), 9: -37,211 (n=40), 8: -39,892 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,831 | 2 | 2 | 4 | 12679 | 2.84 | 2: -31,033 (n=12176), 1: -37,016 (n=404), 3: -38,436 (n=36), 0: -39,864 (n=63) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,963 | 14 | 12 | 11 | 12678 | 7.48 | 14: -31,057 (n=10756), 13: -31,294 (n=873), 12: -32,867 (n=563), 11: -32,943 (n=186), 6: -34,434 (n=3), 9: -34,672 (n=25), 10: -35,409 (n=233), 7: -36,209 (n=9), 8: -37,161 (n=27), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,765 | frontier | frontier | 2 | 12679 | 0.92 | frontier: -30,962 (n=12146), v312: -38,727 (n=533) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,604 | 2 | 2 | 3 | 12679 | 1.82 | 2: -30,895 (n=11927), 1: -37,461 (n=706), 3: -38,500 (n=46) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,321 | 38 | 40 | 30 | 12679 | 7.48 | 38: -30,243 (n=2647), 34: -30,457 (n=212), 43: -30,556 (n=3582), 49: -30,651 (n=380), 33: -30,734 (n=49), 30: -30,867 (n=59), 44: -31,121 (n=320), 37: -31,174 (n=441), 39: -31,175 (n=434), 47: -31,183 (n=207), 45: -31,281 (n=454), 27: -31,389 (n=8), 28: -31,698 (n=14), 26: -31,715 (n=37), 32: -31,993 (n=57), 29: -32,205 (n=14), 46: -32,377 (n=82), 31: -32,429 (n=35), 35: -32,635 (n=196), 40: -32,720 (n=2533), 42: -32,960 (n=202), 50: -33,121 (n=324), 36: -33,127 (n=174), 41: -33,374 (n=84), 25: -33,906 (n=6), 20: -34,877 (n=33), 48: -34,953 (n=62), 24: -35,533 (n=23), 23: -36,212 (n=6), 22: -37,564 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2400)
- (10, 3, 6): -16,840 (n=2013)
- (8, 3, 5): -16,866 (n=239)
- (9, 3, 6): -16,959 (n=1550)
- (8, 3, 6): -17,552 (n=671)
- (12, 4, 6): -17,899 (n=427)
- (10, 4, 6): -17,975 (n=1771)
- (11, 3, 6): -18,175 (n=447)
- (11, 4, 6): -19,867 (n=468)
- (17, 3, 6): -20,013 (n=54)
- (8, 4, 6): -21,051 (n=607)
- (13, 4, 6): -21,868 (n=165)
- (8, 3, 4): -22,126 (n=66)
- (13, 3, 6): -22,174 (n=238)
- (10, 3, 5): -22,188 (n=54)

_Generated 2026-09-08 18:54. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 3644 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=3644); harvest_min=1–3 (n=3644); wheat_tiles=0–8 (n=3644); wheat_stock=0–40 (n=3644); min_hands=3–6 (n=3644); load_per_hand=12–26 (n=3644); geese=0–2 (n=3644); open_melons=4–14 (n=3644)
- **Evidence:** 3644 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 48 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=48); harvest_min=1–3 (n=48); wheat_tiles=0–2 (n=48); wheat_stock=0–4 (n=48); min_hands=3–6 (n=48); load_per_hand=19–21 (n=48); geese=0–2 (n=48); open_melons=7–13 (n=48)
- **Evidence:** 48 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 24 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=24); harvest_min=1–3 (n=24); wheat_tiles=0; wheat_stock=0–39 (n=24); min_hands=3–6 (n=24); load_per_hand=12–20 (n=24); geese=0–1 (n=24); open_melons=9–13 (n=24)
- **Evidence:** 24 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 14 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=14); harvest_min=1–3 (n=14); wheat_tiles=0–8 (n=14); wheat_stock=0–39 (n=14); min_hands=3–6 (n=14); load_per_hand=12–17 (n=14); geese=0–2 (n=14); open_melons=8–14 (n=14)
- **Evidence:** 14 candidates, multiple seeds. Confidence: moderate

### None (observed in 8 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=8); harvest_min=1–2 (n=8); wheat_tiles=0; wheat_stock=0–11 (n=8); min_hands=3–6 (n=8); load_per_hand=12–18 (n=8); geese=0–2 (n=8); open_melons=10–14 (n=8)
- **Evidence:** 8 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 18:54. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._