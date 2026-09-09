# Evolution run 20260908-185849

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1307 · games 23,564 (11,775/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 440 | 880 |
| dead_pattern | 242 | 484 |
| dead_smoke | 195 | 1560 |
| alive | 430 | 20640 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 13109 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1585
- M2: best -16,461 (`0c25e1226b27`), n=1630
- c1: best -16,310 (`23734cef4da1`), n=2368
- queue: best -15,412 (`fe4745b56024`), n=3240
- v312: best -15,275 (`52b3d5cc236e`), n=2236
- wide: best -16,047 (`512e53fe15bc`), n=2050

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +20,677 | 120 | 50 | 143 | 13100 | 65.34 | 120: -21,091 (n=5), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,592 (n=3), 19: -28,045 (n=14), 141: -28,093 (n=5), 5: -28,588 (n=46), 112: -28,796 (n=13), 35: -28,878 (n=10), 56: -29,255 (n=13), 71: -29,378 (n=25), 27: -29,473 (n=35), 89: -29,645 (n=29), 58: -29,749 (n=96), 26: -29,760 (n=7), 92: -29,763 (n=325), 18: -29,983 (n=761), 74: -30,138 (n=196), 63: -30,473 (n=208), 49: -30,553 (n=74), 51: -30,565 (n=12), 72: -30,614 (n=8), 61: -30,688 (n=95), 48: -30,738 (n=507), 50: -30,785 (n=6485), 150: -30,836 (n=153), 80: -30,851 (n=12), 65: -30,904 (n=126), 86: -31,018 (n=9), 144: -31,182 (n=2), 60: -31,184 (n=29), 42: -31,212 (n=731), 106: -31,241 (n=8), 40: -31,260 (n=92), 85: -31,279 (n=9), 33: -31,322 (n=21), 45: -31,409 (n=108), 66: -31,423 (n=217), 70: -31,583 (n=31), 97: -31,673 (n=26), 59: -31,678 (n=18), 2: -31,685 (n=2), 57: -31,735 (n=82), 9: -31,745 (n=15), 93: -31,753 (n=7), 73: -31,772 (n=16), 14: -31,806 (n=20), 96: -31,865 (n=7), 36: -31,919 (n=107), 113: -32,094 (n=12), 62: -32,220 (n=17), 110: -32,277 (n=4), 39: -32,323 (n=52), 69: -32,403 (n=22), 68: -32,488 (n=14), 115: -32,512 (n=8), 84: -32,518 (n=13), 94: -32,527 (n=15), 103: -32,559 (n=8), 25: -32,636 (n=8), 76: -32,669 (n=12), 38: -32,804 (n=17), 52: -32,811 (n=14), 20: -32,812 (n=6), 109: -32,844 (n=3), 98: -32,926 (n=20), 88: -32,953 (n=10), 55: -33,001 (n=532), 31: -33,053 (n=13), 21: -33,189 (n=10), 108: -33,264 (n=5), 104: -33,266 (n=4), 6: -33,331 (n=10), 119: -33,340 (n=2), 41: -33,381 (n=37), 4: -33,399 (n=36), 0: -33,422 (n=191), 95: -33,449 (n=5), 83: -33,464 (n=99), 13: -33,499 (n=7), 22: -33,559 (n=15), 43: -33,691 (n=18), 54: -33,751 (n=19), 90: -33,822 (n=7), 81: -33,835 (n=24), 24: -33,884 (n=19), 30: -33,916 (n=15), 32: -33,992 (n=9), 111: -34,111 (n=8), 44: -34,233 (n=20), 99: -34,244 (n=72), 10: -34,299 (n=13), 102: -34,320 (n=4), 78: -34,340 (n=10), 28: -34,350 (n=19), 82: -34,387 (n=43), 1: -34,413 (n=5), 134: -34,464 (n=2), 136: -34,521 (n=38), 7: -34,621 (n=7), 23: -34,633 (n=12), 64: -34,667 (n=20), 37: -34,729 (n=11), 16: -34,787 (n=14), 46: -34,861 (n=31), 79: -34,930 (n=14), 107: -34,965 (n=5), 15: -35,051 (n=9), 77: -35,116 (n=220), 34: -35,158 (n=58), 101: -35,278 (n=11), 100: -35,413 (n=44), 17: -35,508 (n=6), 11: -35,563 (n=13), 91: -35,821 (n=9), 87: -35,852 (n=10), 129: -35,903 (n=76), 53: -35,974 (n=27), 47: -36,381 (n=19), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 67: -37,049 (n=18), 29: -37,128 (n=24), 75: -37,220 (n=8), 114: -37,341 (n=4), 12: -37,385 (n=10), 127: -38,268 (n=2), 140: -38,489 (n=3), 131: -38,847 (n=2), 124: -39,372 (n=2), 132: -39,931 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,148 | 26 | 30 | 25 | 13108 | 10.56 | 26: -30,605 (n=431), 25: -30,733 (n=6315), 30: -30,922 (n=4222), 31: -31,552 (n=118), 29: -32,010 (n=111), 27: -32,356 (n=214), 28: -33,525 (n=1107), 41: -34,307 (n=3), 32: -34,703 (n=125), 35: -34,707 (n=172), 38: -35,532 (n=17), 33: -35,601 (n=112), 37: -35,850 (n=22), 34: -36,089 (n=57), 39: -36,441 (n=11), 42: -36,612 (n=3), 36: -37,791 (n=33), 40: -38,440 (n=11), 46: -38,521 (n=3), 44: -38,790 (n=5), 47: -39,384 (n=2), 50: -40,198 (n=7), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,222 | 3 | 3 | 4 | 13109 | 2.61 | 3: -30,761 (n=11828), 2: -35,894 (n=914), 4: -36,491 (n=349), 5: -42,983 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,215 | 1 | 0 | 33 | 13107 | 25.45 | 1: -30,311 (n=791), 9: -31,017 (n=87), 0: -31,031 (n=11184), 22: -31,539 (n=2), 2: -32,609 (n=126), 4: -33,267 (n=81), 8: -33,374 (n=69), 17: -33,465 (n=11), 6: -33,631 (n=75), 5: -34,345 (n=127), 11: -34,373 (n=58), 19: -34,546 (n=5), 3: -34,562 (n=159), 7: -35,744 (n=76), 13: -35,887 (n=39), 14: -36,260 (n=21), 12: -36,313 (n=26), 28: -36,361 (n=2), 18: -36,506 (n=19), 16: -36,588 (n=9), 23: -36,694 (n=6), 15: -36,765 (n=26), 20: -36,836 (n=5), 24: -37,048 (n=7), 10: -37,294 (n=42), 21: -38,756 (n=6), 39: -38,850 (n=9), 40: -39,508 (n=8), 26: -40,268 (n=3), 29: -41,280 (n=24), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,537 | 0.0 | 0.0 | 13 | 13109 | 10.18 | 0.0: -30,892 (n=11278), 0.1: -33,042 (n=899), 0.2: -33,811 (n=550), 0.4: -34,056 (n=80), 0.3: -34,517 (n=151), 0.5: -34,985 (n=49), 1.1: -35,241 (n=6), 0.7: -36,163 (n=16), 0.6: -36,955 (n=38), 0.9: -37,347 (n=5), 1.0: -37,742 (n=23), 1.2: -39,081 (n=9), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 13108 | 62.27 | 61: -27,918 (n=2), 138: -28,049 (n=2), 69: -28,538 (n=7), 130: -28,649 (n=12), 80: -29,422 (n=140), 85: -30,012 (n=87), 65: -30,099 (n=5), 93: -30,142 (n=351), 120: -30,188 (n=14), 81: -30,237 (n=75), 91: -30,273 (n=81), 114: -30,288 (n=22), 92: -30,325 (n=18), 86: -30,338 (n=600), 129: -30,493 (n=16), 100: -30,712 (n=8294), 111: -30,789 (n=35), 113: -30,885 (n=18), 62: -30,897 (n=5), 107: -30,975 (n=24), 94: -31,021 (n=30), 78: -31,121 (n=70), 84: -31,192 (n=61), 133: -31,210 (n=9), 125: -31,389 (n=85), 141: -31,447 (n=3), 115: -31,492 (n=28), 83: -31,569 (n=109), 123: -31,601 (n=37), 147: -31,607 (n=7), 64: -31,620 (n=10), 95: -31,833 (n=34), 63: -31,882 (n=9), 102: -31,919 (n=40), 70: -31,925 (n=18), 82: -31,935 (n=21), 57: -31,969 (n=5), 132: -31,971 (n=11), 109: -32,016 (n=27), 105: -32,129 (n=87), 149: -32,176 (n=3), 99: -32,241 (n=30), 53: -32,281 (n=4), 66: -32,339 (n=13), 103: -32,387 (n=26), 71: -32,513 (n=20), 90: -32,530 (n=74), 87: -32,552 (n=18), 104: -32,557 (n=521), 67: -32,561 (n=7), 117: -32,661 (n=73), 55: -32,666 (n=3), 56: -32,821 (n=2), 119: -33,009 (n=14), 136: -33,061 (n=6), 112: -33,147 (n=196), 122: -33,164 (n=35), 101: -33,191 (n=33), 88: -33,335 (n=61), 128: -33,413 (n=21), 76: -33,459 (n=17), 110: -33,465 (n=20), 97: -33,478 (n=52), 127: -33,524 (n=26), 134: -33,531 (n=8), 68: -33,616 (n=10), 89: -33,674 (n=141), 135: -33,756 (n=438), 59: -33,898 (n=4), 96: -33,929 (n=39), 126: -33,969 (n=24), 116: -33,989 (n=57), 124: -34,000 (n=20), 143: -34,012 (n=11), 121: -34,025 (n=11), 79: -34,147 (n=40), 98: -34,314 (n=37), 108: -34,320 (n=25), 74: -34,399 (n=29), 75: -34,479 (n=58), 144: -34,772 (n=2), 137: -34,809 (n=4), 106: -34,885 (n=40), 150: -35,585 (n=166), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 131: -36,462 (n=12), 148: -36,528 (n=3), 50: -36,565 (n=41), 77: -36,576 (n=17), 58: -36,674 (n=4), 118: -36,824 (n=14), 51: -37,500 (n=2), 72: -37,554 (n=9), 73: -37,735 (n=11), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,892 | 6 | 6 | 8 | 13109 | 6.12 | 6: -30,693 (n=11675), 5: -34,654 (n=574), 7: -36,275 (n=348), 4: -37,320 (n=319), 3: -37,828 (n=114), 8: -38,279 (n=54), 9: -40,761 (n=19), 10: -41,585 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,797 | 13 | 20 | 11 | 13109 | 4.99 | 13: -30,230 (n=33), 17: -30,846 (n=4148), 14: -31,084 (n=108), 16: -31,117 (n=295), 19: -31,331 (n=639), 18: -31,337 (n=608), 20: -31,520 (n=7139), 15: -32,191 (n=115), 11: -32,310 (n=3), 12: -35,207 (n=13), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,721 | 20 | 20 | 15 | 13109 | 7.22 | 20: -30,462 (n=7180), 19: -30,966 (n=4120), 18: -31,709 (n=299), 17: -34,319 (n=652), 21: -36,277 (n=276), 16: -36,482 (n=121), 15: -37,279 (n=59), 23: -37,303 (n=65), 22: -37,659 (n=145), 14: -38,136 (n=32), 26: -38,591 (n=38), 24: -39,100 (n=70), 25: -39,310 (n=20), 13: -39,412 (n=17), 12: -41,183 (n=15) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,683 | 6 | 18 | 21 | 13109 | 9.21 | 6: -29,449 (n=15), 21: -30,458 (n=2222), 14: -30,548 (n=17), 22: -30,769 (n=6372), 20: -31,257 (n=624), 23: -31,375 (n=595), 16: -32,155 (n=77), 25: -32,397 (n=1115), 17: -32,490 (n=685), 18: -32,929 (n=539), 24: -33,129 (n=384), 12: -33,342 (n=11), 15: -33,444 (n=44), 19: -33,597 (n=173), 13: -33,955 (n=22), 9: -34,042 (n=48), 10: -34,585 (n=65), 5: -36,228 (n=43), 11: -36,402 (n=33), 7: -36,441 (n=21), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,147 | 7 | 7 | 8 | 13109 | 6.09 | 7: -30,603 (n=11623), 6: -36,437 (n=768), 5: -36,596 (n=63), 8: -36,674 (n=419), 10: -36,809 (n=102), 9: -37,170 (n=87), 4: -38,293 (n=39), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +9,972 | 10 | 8 | 11 | 13109 | 8.26 | 10: -30,635 (n=11038), 7: -32,539 (n=393), 8: -34,777 (n=850), 9: -34,941 (n=486), 6: -35,417 (n=155), 5: -36,350 (n=19), 12: -38,056 (n=42), 4: -38,137 (n=22), 11: -38,415 (n=56), 14: -39,191 (n=25), 13: -40,607 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,773 | 0.55 | 0.5 | 15 | 13109 | 6.99 | 0.55: -30,154 (n=6980), 0.65: -31,717 (n=1124), 0.5: -31,868 (n=3426), 0.75: -32,029 (n=93), 0.7: -32,293 (n=217), 0.6: -32,787 (n=308), 0.8: -33,495 (n=41), 0.45: -34,644 (n=405), 0.9: -35,286 (n=10), 0.85: -35,798 (n=11), 0.35: -36,071 (n=143), 0.4: -36,182 (n=144), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,928 (n=197) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,707 | 0 | 0 | 9 | 13109 | 7.15 | 0: -30,951 (n=11868), 1: -34,029 (n=663), 2: -34,674 (n=259), 3: -34,911 (n=209), 4: -35,771 (n=66), 5: -36,331 (n=18), 7: -36,592 (n=4), 6: -37,530 (n=19), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +9,419 | 14 | 13 | 9 | 13109 | 4.38 | 14: -30,581 (n=1927), 13: -31,276 (n=7836), 11: -31,335 (n=711), 15: -31,358 (n=389), 12: -31,433 (n=1858), 16: -33,370 (n=228), 10: -33,923 (n=101), 9: -37,197 (n=42), 8: -40,000 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,811 | 2 | 2 | 4 | 13109 | 2.84 | 2: -31,034 (n=12586), 1: -36,963 (n=423), 3: -38,436 (n=36), 0: -39,845 (n=64) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,948 | 14 | 12 | 11 | 13108 | 7.48 | 14: -31,073 (n=11116), 13: -31,173 (n=920), 12: -32,837 (n=575), 11: -32,871 (n=191), 6: -34,434 (n=3), 9: -34,835 (n=26), 10: -35,392 (n=237), 7: -36,209 (n=9), 8: -37,183 (n=28), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,726 | frontier | frontier | 2 | 13109 | 0.92 | frontier: -30,963 (n=12557), v312: -38,690 (n=552) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,391 | 2 | 2 | 3 | 13109 | 1.82 | 2: -30,893 (n=12327), 1: -37,474 (n=734), 3: -38,284 (n=48) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,304 | 38 | 40 | 30 | 13109 | 7.49 | 38: -30,261 (n=2778), 34: -30,547 (n=223), 43: -30,575 (n=3711), 49: -30,609 (n=390), 33: -30,876 (n=51), 30: -30,966 (n=60), 44: -31,119 (n=333), 47: -31,133 (n=214), 37: -31,166 (n=463), 39: -31,259 (n=441), 45: -31,278 (n=482), 27: -31,389 (n=8), 28: -31,698 (n=14), 32: -31,993 (n=57), 46: -32,301 (n=88), 26: -32,308 (n=41), 31: -32,613 (n=37), 35: -32,705 (n=205), 29: -32,718 (n=15), 40: -32,719 (n=2567), 42: -32,923 (n=205), 50: -33,053 (n=330), 36: -33,127 (n=174), 41: -33,261 (n=86), 25: -33,906 (n=6), 20: -34,918 (n=35), 48: -34,953 (n=62), 24: -35,533 (n=23), 23: -36,212 (n=6), 22: -37,564 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2474)
- (10, 3, 6): -16,840 (n=2098)
- (8, 3, 5): -16,866 (n=242)
- (9, 3, 6): -16,959 (n=1622)
- (12, 4, 6): -17,058 (n=434)
- (8, 3, 6): -17,552 (n=688)
- (10, 4, 6): -17,975 (n=1826)
- (11, 3, 6): -18,175 (n=459)
- (11, 4, 6): -19,867 (n=472)
- (17, 3, 6): -20,013 (n=56)
- (8, 4, 6): -21,051 (n=625)
- (13, 4, 6): -21,868 (n=170)
- (8, 3, 4): -22,126 (n=67)
- (13, 3, 6): -22,174 (n=250)
- (10, 3, 5): -22,188 (n=55)

_Generated 2026-09-08 20:58. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 4064 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=4064); harvest_min=1–3 (n=4064); wheat_tiles=0–8 (n=4064); wheat_stock=0–40 (n=4064); min_hands=3–6 (n=4064); load_per_hand=12–26 (n=4064); geese=0–2 (n=4064); open_melons=4–14 (n=4064)
- **Evidence:** 4064 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 55 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=55); harvest_min=1–3 (n=55); wheat_tiles=0–2 (n=55); wheat_stock=0–4 (n=55); min_hands=3–6 (n=55); load_per_hand=15–21 (n=55); geese=0–2 (n=55); open_melons=7–13 (n=55)
- **Evidence:** 55 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 29 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=29); harvest_min=1–3 (n=29); wheat_tiles=0; wheat_stock=0–39 (n=29); min_hands=3–6 (n=29); load_per_hand=12–20 (n=29); geese=0–1 (n=29); open_melons=4–13 (n=29)
- **Evidence:** 29 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 18 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=18); harvest_min=1–3 (n=18); wheat_tiles=0–8 (n=18); wheat_stock=0–39 (n=18); min_hands=3–6 (n=18); load_per_hand=12–23 (n=18); geese=0–2 (n=18); open_melons=8–14 (n=18)
- **Evidence:** 18 candidates, multiple seeds. Confidence: high

### None (observed in 9 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=9); harvest_min=1–3 (n=9); wheat_tiles=0; wheat_stock=0–11 (n=9); min_hands=3–6 (n=9); load_per_hand=12–18 (n=9); geese=0–2 (n=9); open_melons=10–14 (n=9)
- **Evidence:** 9 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 20:58. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._