# Evolution run 20260909-011304

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1237 · games 23,332 (11,660/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 406 | 812 |
| dead_pattern | 228 | 456 |
| dead_smoke | 172 | 1376 |
| alive | 431 | 20688 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 14418 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1792
- M2: best -16,461 (`0c25e1226b27`), n=1839
- c1: best -16,310 (`23734cef4da1`), n=2583
- queue: best -15,412 (`fe4745b56024`), n=3515
- v312: best -15,275 (`52b3d5cc236e`), n=2426
- wide: best -16,047 (`512e53fe15bc`), n=2263

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +20,931 | 120 | 50 | 144 | 14409 | 65.63 | 120: -20,837 (n=6), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,592 (n=3), 19: -27,891 (n=15), 141: -28,023 (n=6), 5: -28,805 (n=47), 35: -28,918 (n=11), 112: -29,479 (n=14), 27: -29,531 (n=36), 89: -29,645 (n=29), 26: -29,760 (n=7), 58: -29,892 (n=109), 18: -30,052 (n=872), 92: -30,054 (n=370), 51: -30,123 (n=16), 74: -30,191 (n=241), 80: -30,197 (n=15), 56: -30,266 (n=15), 63: -30,435 (n=235), 49: -30,517 (n=77), 71: -30,611 (n=29), 48: -30,664 (n=528), 72: -30,675 (n=9), 65: -30,736 (n=136), 61: -30,770 (n=99), 50: -30,823 (n=7112), 108: -30,839 (n=6), 86: -31,018 (n=9), 150: -31,059 (n=182), 60: -31,184 (n=29), 70: -31,194 (n=43), 66: -31,287 (n=259), 40: -31,302 (n=100), 42: -31,311 (n=792), 97: -31,347 (n=29), 85: -31,513 (n=11), 33: -31,521 (n=22), 45: -31,621 (n=115), 14: -31,674 (n=21), 2: -31,685 (n=2), 94: -31,729 (n=18), 144: -31,766 (n=3), 106: -31,771 (n=12), 96: -31,865 (n=7), 9: -31,947 (n=16), 57: -31,948 (n=84), 36: -32,088 (n=112), 113: -32,112 (n=13), 110: -32,277 (n=4), 30: -32,300 (n=27), 39: -32,314 (n=55), 73: -32,323 (n=17), 69: -32,395 (n=23), 59: -32,412 (n=20), 103: -32,462 (n=9), 115: -32,512 (n=8), 62: -32,601 (n=18), 84: -32,611 (n=14), 25: -32,636 (n=8), 38: -32,687 (n=18), 54: -32,701 (n=24), 20: -32,812 (n=6), 109: -32,844 (n=3), 52: -32,916 (n=18), 98: -32,926 (n=20), 55: -32,946 (n=580), 41: -32,977 (n=40), 93: -32,999 (n=9), 31: -33,053 (n=13), 4: -33,065 (n=37), 21: -33,189 (n=10), 104: -33,266 (n=4), 6: -33,331 (n=10), 76: -33,355 (n=15), 83: -33,388 (n=105), 95: -33,449 (n=5), 53: -33,456 (n=40), 81: -33,458 (n=26), 0: -33,495 (n=203), 13: -33,499 (n=7), 43: -33,575 (n=20), 119: -33,699 (n=3), 28: -33,719 (n=20), 22: -33,797 (n=16), 68: -33,803 (n=17), 24: -33,814 (n=20), 90: -33,822 (n=7), 88: -33,874 (n=11), 32: -33,992 (n=9), 111: -34,111 (n=8), 1: -34,150 (n=7), 17: -34,184 (n=7), 10: -34,204 (n=14), 99: -34,244 (n=72), 82: -34,251 (n=45), 78: -34,276 (n=13), 102: -34,320 (n=4), 44: -34,396 (n=21), 140: -34,453 (n=4), 134: -34,464 (n=2), 15: -34,489 (n=10), 7: -34,621 (n=7), 23: -34,633 (n=12), 37: -34,726 (n=12), 16: -34,787 (n=16), 46: -34,818 (n=35), 136: -34,877 (n=41), 79: -34,930 (n=14), 64: -34,931 (n=21), 107: -34,965 (n=5), 77: -35,137 (n=229), 11: -35,182 (n=14), 101: -35,278 (n=11), 34: -35,328 (n=61), 87: -35,476 (n=11), 100: -35,511 (n=49), 129: -35,839 (n=81), 91: -35,887 (n=10), 128: -36,508 (n=3), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 12: -36,634 (n=11), 47: -36,764 (n=20), 145: -36,990 (n=7), 67: -37,049 (n=18), 114: -37,341 (n=4), 75: -37,579 (n=9), 29: -38,225 (n=35), 127: -38,268 (n=2), 131: -38,847 (n=2), 132: -39,931 (n=2), 124: -39,994 (n=3), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,255 | 26 | 30 | 25 | 14417 | 10.66 | 26: -30,498 (n=477), 25: -30,784 (n=7003), 30: -30,990 (n=4667), 31: -31,600 (n=128), 29: -32,198 (n=117), 27: -32,288 (n=227), 28: -33,520 (n=1175), 41: -34,307 (n=3), 32: -34,378 (n=137), 35: -34,758 (n=175), 33: -35,510 (n=119), 37: -35,653 (n=25), 38: -35,789 (n=19), 34: -36,046 (n=60), 39: -36,441 (n=11), 42: -36,946 (n=4), 36: -37,791 (n=33), 46: -38,521 (n=3), 44: -38,790 (n=5), 40: -39,180 (n=12), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,291 | 1 | 0 | 34 | 14415 | 25.18 | 1: -30,235 (n=966), 0: -31,070 (n=12175), 9: -31,072 (n=93), 22: -31,539 (n=2), 2: -32,497 (n=144), 4: -32,909 (n=92), 6: -33,073 (n=92), 8: -33,225 (n=81), 19: -34,158 (n=6), 17: -34,402 (n=14), 3: -34,409 (n=172), 11: -34,776 (n=66), 5: -34,776 (n=146), 16: -35,592 (n=13), 7: -35,760 (n=83), 13: -35,812 (n=45), 12: -36,044 (n=32), 14: -36,151 (n=22), 20: -36,357 (n=6), 28: -36,361 (n=2), 23: -36,694 (n=6), 15: -36,705 (n=27), 18: -36,728 (n=20), 24: -37,048 (n=7), 10: -37,219 (n=45), 39: -37,389 (n=10), 21: -37,766 (n=7), 40: -39,508 (n=8), 26: -40,268 (n=3), 29: -41,548 (n=26), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,266 | 3 | 3 | 4 | 14418 | 2.61 | 3: -30,791 (n=13015), 2: -35,851 (n=1002), 4: -36,546 (n=382), 5: -43,057 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 14418 | 62.96 | 61: -27,918 (n=2), 138: -28,049 (n=2), 130: -28,649 (n=12), 80: -29,439 (n=200), 120: -29,534 (n=15), 93: -30,097 (n=372), 65: -30,099 (n=5), 85: -30,150 (n=92), 81: -30,271 (n=81), 91: -30,404 (n=88), 86: -30,469 (n=689), 114: -30,605 (n=24), 100: -30,792 (n=9130), 123: -30,831 (n=43), 113: -30,885 (n=18), 111: -30,935 (n=37), 115: -30,975 (n=30), 94: -31,179 (n=33), 125: -31,182 (n=89), 133: -31,210 (n=9), 129: -31,219 (n=18), 64: -31,367 (n=11), 78: -31,387 (n=93), 63: -31,414 (n=10), 55: -31,425 (n=4), 141: -31,447 (n=3), 107: -31,477 (n=25), 90: -31,491 (n=95), 92: -31,528 (n=25), 83: -31,572 (n=111), 147: -31,607 (n=7), 67: -31,660 (n=9), 84: -31,692 (n=68), 69: -31,788 (n=9), 109: -31,865 (n=33), 57: -31,969 (n=5), 87: -31,970 (n=20), 132: -31,971 (n=11), 99: -31,977 (n=33), 102: -32,069 (n=42), 103: -32,079 (n=27), 70: -32,127 (n=19), 117: -32,152 (n=92), 105: -32,169 (n=105), 149: -32,176 (n=3), 53: -32,281 (n=4), 95: -32,307 (n=38), 66: -32,339 (n=13), 71: -32,513 (n=20), 82: -32,550 (n=22), 104: -32,570 (n=556), 128: -32,572 (n=24), 62: -32,574 (n=6), 127: -32,874 (n=30), 76: -32,934 (n=18), 110: -32,958 (n=24), 88: -32,996 (n=65), 119: -33,009 (n=14), 112: -33,091 (n=200), 122: -33,107 (n=37), 97: -33,465 (n=53), 101: -33,529 (n=36), 134: -33,531 (n=8), 68: -33,616 (n=10), 89: -33,689 (n=154), 135: -33,770 (n=451), 96: -33,780 (n=41), 116: -33,812 (n=63), 98: -33,817 (n=42), 59: -33,898 (n=4), 126: -33,966 (n=25), 143: -34,012 (n=11), 74: -34,126 (n=33), 79: -34,165 (n=42), 121: -34,209 (n=12), 136: -34,218 (n=7), 75: -34,479 (n=58), 108: -34,512 (n=27), 124: -34,550 (n=22), 137: -34,596 (n=5), 144: -34,772 (n=2), 106: -34,924 (n=43), 50: -35,284 (n=50), 72: -35,612 (n=10), 150: -35,653 (n=169), 56: -35,769 (n=4), 131: -35,872 (n=13), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 118: -36,824 (n=14), 58: -36,875 (n=5), 77: -37,179 (n=19), 51: -37,500 (n=2), 73: -37,735 (n=11), 146: -37,838 (n=2), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,512 | 0.0 | 0.0 | 13 | 14418 | 10.24 | 0.0: -30,932 (n=12466), 0.1: -33,068 (n=959), 0.2: -33,760 (n=575), 0.4: -34,229 (n=86), 0.3: -34,303 (n=171), 1.1: -34,978 (n=7), 0.5: -35,028 (n=51), 0.7: -36,163 (n=16), 0.6: -37,154 (n=43), 0.9: -37,347 (n=5), 1.0: -37,756 (n=24), 1.2: -39,081 (n=9), 0.8: -42,444 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,572 | 13 | 20 | 11 | 14418 | 4.89 | 13: -30,455 (n=36), 17: -30,923 (n=4668), 16: -31,042 (n=327), 19: -31,216 (n=716), 14: -31,233 (n=119), 18: -31,356 (n=687), 20: -31,535 (n=7716), 11: -32,310 (n=3), 15: -32,323 (n=123), 12: -34,282 (n=15), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,412 | 20 | 20 | 15 | 14418 | 7.43 | 20: -30,544 (n=8106), 19: -30,949 (n=4373), 18: -31,548 (n=326), 17: -34,307 (n=684), 16: -36,506 (n=131), 21: -36,507 (n=301), 15: -37,372 (n=65), 23: -37,585 (n=71), 22: -37,754 (n=156), 14: -38,304 (n=35), 26: -38,538 (n=39), 24: -38,986 (n=75), 25: -39,340 (n=21), 13: -39,593 (n=18), 12: -40,956 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,352 | 6 | 6 | 8 | 14418 | 6.12 | 6: -30,715 (n=12841), 5: -34,637 (n=638), 7: -36,401 (n=371), 4: -37,407 (n=362), 3: -37,765 (n=123), 8: -38,222 (n=57), 9: -40,761 (n=19), 10: -41,067 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,105 | 7 | 7 | 8 | 14418 | 6.11 | 7: -30,645 (n=12816), 6: -36,450 (n=814), 5: -36,485 (n=68), 8: -36,611 (n=463), 10: -36,840 (n=112), 9: -37,183 (n=96), 4: -38,262 (n=41), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,078 | 10 | 8 | 11 | 14418 | 8.28 | 10: -30,673 (n=12169), 7: -32,508 (n=442), 8: -34,716 (n=905), 9: -34,999 (n=523), 6: -35,401 (n=167), 5: -36,602 (n=24), 12: -37,858 (n=45), 4: -38,137 (n=22), 11: -38,544 (n=62), 14: -39,776 (n=29), 13: -40,750 (n=30) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,676 | 0 | 0 | 9 | 14418 | 7.15 | 0: -30,982 (n=13062), 1: -34,036 (n=713), 2: -34,582 (n=291), 3: -34,825 (n=223), 4: -35,634 (n=77), 7: -35,683 (n=6), 5: -35,863 (n=20), 6: -37,601 (n=23), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,653 | 0.55 | 0.5 | 15 | 14418 | 7.19 | 0.55: -30,242 (n=7870), 0.65: -31,700 (n=1169), 0.5: -31,822 (n=3639), 0.75: -31,984 (n=99), 0.7: -32,259 (n=234), 0.6: -33,106 (n=352), 0.8: -34,069 (n=47), 0.45: -34,625 (n=438), 0.9: -35,286 (n=10), 0.35: -35,955 (n=151), 0.4: -36,180 (n=162), 0.85: -37,161 (n=14), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,895 (n=223) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +9,331 | 14 | 13 | 9 | 14418 | 4.35 | 14: -30,756 (n=2252), 11: -31,250 (n=746), 13: -31,282 (n=8570), 12: -31,398 (n=1990), 15: -31,716 (n=439), 16: -33,469 (n=245), 10: -33,521 (n=114), 9: -37,129 (n=44), 8: -40,087 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,834 | 6 | 18 | 21 | 14418 | 9.31 | 6: -29,796 (n=17), 21: -30,551 (n=2518), 22: -30,815 (n=7077), 14: -30,920 (n=19), 20: -31,251 (n=651), 23: -31,299 (n=652), 16: -32,328 (n=86), 17: -32,440 (n=727), 25: -32,467 (n=1187), 18: -32,940 (n=580), 24: -33,156 (n=405), 12: -33,342 (n=11), 19: -33,540 (n=185), 15: -33,546 (n=49), 13: -33,826 (n=24), 9: -33,993 (n=50), 10: -34,716 (n=67), 11: -36,049 (n=34), 5: -36,198 (n=53), 7: -36,441 (n=21), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,504 | 2 | 2 | 4 | 14418 | 2.84 | 2: -31,060 (n=13843), 1: -36,934 (n=466), 3: -38,373 (n=39), 0: -39,564 (n=70) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,150 | 13 | 12 | 11 | 14417 | 7.46 | 13: -30,870 (n=1076), 14: -31,141 (n=12198), 11: -32,777 (n=204), 12: -32,786 (n=617), 6: -34,434 (n=3), 9: -34,938 (n=27), 10: -35,303 (n=249), 7: -35,686 (n=10), 8: -36,973 (n=30), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,619 | frontier | frontier | 2 | 14418 | 0.92 | frontier: -30,990 (n=13811), v312: -38,610 (n=607) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,535 | 2 | 2 | 3 | 14418 | 1.82 | 2: -30,916 (n=13567), 1: -37,550 (n=798), 3: -38,451 (n=53) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,280 | 34 | 40 | 30 | 14418 | 7.49 | 34: -30,307 (n=250), 38: -30,388 (n=3156), 43: -30,620 (n=4079), 49: -30,650 (n=422), 27: -30,679 (n=10), 33: -30,822 (n=53), 44: -30,928 (n=384), 30: -31,104 (n=65), 47: -31,134 (n=242), 37: -31,150 (n=521), 45: -31,284 (n=557), 39: -31,445 (n=503), 28: -31,842 (n=15), 32: -31,859 (n=60), 26: -32,075 (n=48), 46: -32,503 (n=96), 40: -32,756 (n=2664), 29: -32,779 (n=17), 35: -32,794 (n=222), 42: -32,961 (n=215), 31: -32,984 (n=39), 50: -33,039 (n=369), 36: -33,164 (n=180), 25: -33,175 (n=7), 41: -33,237 (n=100), 20: -34,641 (n=40), 48: -34,714 (n=69), 24: -35,776 (n=24), 23: -36,212 (n=6), 22: -37,587 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2711)
- (9, 3, 6): -16,578 (n=1808)
- (10, 3, 6): -16,840 (n=2343)
- (8, 3, 5): -16,866 (n=260)
- (12, 4, 6): -17,058 (n=465)
- (8, 3, 6): -17,552 (n=732)
- (10, 4, 6): -17,975 (n=2052)
- (11, 3, 6): -18,175 (n=495)
- (11, 4, 6): -19,867 (n=506)
- (17, 3, 6): -20,013 (n=60)
- (8, 4, 6): -21,051 (n=678)
- (13, 4, 6): -21,868 (n=185)
- (8, 3, 4): -22,126 (n=74)
- (13, 3, 6): -22,174 (n=269)
- (10, 3, 5): -22,188 (n=58)

_Generated 2026-09-09 03:13. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 5186 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=5186); harvest_min=1–3 (n=5186); wheat_tiles=0–8 (n=5186); wheat_stock=0–40 (n=5186); min_hands=3–6 (n=5186); load_per_hand=12–26 (n=5186); geese=0–2 (n=5186); open_melons=4–14 (n=5186)
- **Evidence:** 5186 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 65 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=65); harvest_min=1–3 (n=65); wheat_tiles=0–2 (n=65); wheat_stock=0–4 (n=65); min_hands=3–6 (n=65); load_per_hand=15–22 (n=65); geese=0–2 (n=65); open_melons=7–13 (n=65)
- **Evidence:** 65 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 37 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=37); harvest_min=1–3 (n=37); wheat_tiles=0; wheat_stock=0–39 (n=37); min_hands=3–6 (n=37); load_per_hand=12–26 (n=37); geese=0–1 (n=37); open_melons=4–13 (n=37)
- **Evidence:** 37 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 24 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=24); harvest_min=1–3 (n=24); wheat_tiles=0–8 (n=24); wheat_stock=0–39 (n=24); min_hands=3–6 (n=24); load_per_hand=12–23 (n=24); geese=0–2 (n=24); open_melons=8–14 (n=24)
- **Evidence:** 24 candidates, multiple seeds. Confidence: high

### None (observed in 12 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=12); harvest_min=1–3 (n=12); wheat_tiles=0; wheat_stock=0–11 (n=12); min_hands=3–6 (n=12); load_per_hand=12–18 (n=12); geese=0–2 (n=12); open_melons=7–14 (n=12)
- **Evidence:** 12 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-09 03:13. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._