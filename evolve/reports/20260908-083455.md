# Evolution run 20260908-083455

Frontier opponent: `H32.py` · clone: `tape_ymgaq_106415741.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1218 · games 24,400 (12,198/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 372 | 744 |
| dead_pattern | 212 | 424 |
| dead_smoke | 180 | 1440 |
| alive | 454 | 21792 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 10842 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1217
- M2: best -16,461 (`0c25e1226b27`), n=1263
- c1: best -16,310 (`23734cef4da1`), n=2001
- queue: best -15,412 (`fe4745b56024`), n=2754
- v312: best -15,275 (`52b3d5cc236e`), n=1904
- wide: best -16,047 (`512e53fe15bc`), n=1703

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +15,196 | 141 | 50 | 143 | 10829 | 62.88 | 141: -24,735 (n=4), 118: -25,349 (n=2), 143: -26,636 (n=2), 19: -27,075 (n=13), 8: -27,428 (n=2), 72: -27,761 (n=5), 35: -27,782 (n=7), 112: -28,098 (n=12), 5: -28,694 (n=42), 71: -28,726 (n=20), 27: -29,195 (n=34), 92: -29,279 (n=252), 26: -29,341 (n=6), 58: -29,544 (n=72), 56: -29,717 (n=11), 18: -29,846 (n=598), 63: -29,851 (n=145), 49: -29,893 (n=61), 89: -30,198 (n=22), 61: -30,297 (n=89), 150: -30,335 (n=92), 65: -30,450 (n=105), 74: -30,531 (n=112), 51: -30,565 (n=12), 50: -30,675 (n=5321), 80: -30,758 (n=11), 48: -30,770 (n=471), 33: -30,789 (n=18), 66: -30,842 (n=157), 86: -30,882 (n=7), 14: -31,012 (n=13), 42: -31,124 (n=650), 144: -31,182 (n=2), 85: -31,279 (n=9), 60: -31,327 (n=26), 45: -31,426 (n=103), 40: -31,514 (n=84), 9: -31,680 (n=12), 2: -31,685 (n=2), 57: -31,735 (n=82), 93: -31,753 (n=7), 96: -31,788 (n=6), 70: -31,835 (n=26), 69: -32,107 (n=20), 39: -32,172 (n=50), 84: -32,266 (n=11), 110: -32,277 (n=4), 59: -32,292 (n=14), 36: -32,316 (n=88), 25: -32,369 (n=7), 94: -32,464 (n=14), 103: -32,559 (n=8), 52: -32,609 (n=10), 73: -32,619 (n=13), 76: -32,628 (n=10), 24: -32,730 (n=13), 115: -32,792 (n=6), 98: -32,797 (n=8), 88: -32,815 (n=9), 109: -32,844 (n=3), 21: -32,882 (n=6), 62: -32,965 (n=16), 136: -33,034 (n=30), 83: -33,226 (n=86), 55: -33,252 (n=459), 31: -33,261 (n=10), 104: -33,266 (n=4), 6: -33,331 (n=10), 119: -33,340 (n=2), 95: -33,358 (n=3), 106: -33,360 (n=4), 0: -33,395 (n=167), 4: -33,399 (n=36), 13: -33,499 (n=7), 23: -33,511 (n=11), 78: -33,580 (n=6), 38: -33,610 (n=16), 111: -33,648 (n=6), 97: -33,659 (n=18), 41: -33,660 (n=28), 43: -33,691 (n=18), 7: -33,733 (n=5), 90: -33,822 (n=7), 22: -33,829 (n=14), 28: -33,832 (n=18), 30: -33,882 (n=12), 46: -33,900 (n=25), 68: -33,901 (n=9), 54: -34,024 (n=13), 82: -34,040 (n=33), 44: -34,096 (n=17), 81: -34,121 (n=23), 10: -34,299 (n=13), 102: -34,320 (n=4), 108: -34,334 (n=4), 99: -34,411 (n=68), 1: -34,413 (n=5), 134: -34,464 (n=2), 79: -34,751 (n=12), 34: -34,920 (n=51), 107: -34,996 (n=4), 113: -35,064 (n=5), 77: -35,126 (n=206), 91: -35,175 (n=7), 32: -35,252 (n=7), 20: -35,382 (n=5), 16: -35,406 (n=11), 100: -35,412 (n=36), 53: -35,427 (n=20), 11: -35,563 (n=13), 87: -35,609 (n=8), 129: -35,876 (n=73), 47: -35,882 (n=17), 101: -36,126 (n=10), 37: -36,131 (n=9), 15: -36,386 (n=7), 64: -36,496 (n=16), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 114: -37,370 (n=3), 12: -37,385 (n=10), 67: -37,399 (n=16), 29: -37,790 (n=18), 75: -38,372 (n=7), 140: -38,489 (n=3), 17: -38,658 (n=4), 131: -38,847 (n=2), 132: -39,931 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +13,193 | 3 | 3 | 4 | 10842 | 2.61 | 3: -30,695 (n=9781), 2: -35,947 (n=761), 4: -36,678 (n=288), 5: -43,888 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,134 | 25 | 30 | 25 | 10838 | 9.01 | 25: -30,618 (n=5166), 26: -30,771 (n=321), 30: -30,777 (n=3488), 31: -31,627 (n=93), 29: -31,938 (n=93), 27: -32,444 (n=183), 28: -33,608 (n=971), 35: -34,733 (n=167), 32: -34,815 (n=102), 38: -35,300 (n=15), 33: -35,686 (n=100), 37: -36,073 (n=20), 34: -36,089 (n=53), 39: -36,508 (n=9), 44: -37,771 (n=4), 40: -38,324 (n=9), 36: -38,389 (n=30), 46: -39,707 (n=2), 50: -40,579 (n=6), 43: -42,029 (n=4), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +12,748 | 6 | 6 | 8 | 10842 | 6.09 | 6: -30,609 (n=9609), 5: -34,657 (n=489), 7: -36,178 (n=310), 4: -37,265 (n=260), 3: -37,883 (n=102), 8: -38,309 (n=51), 9: -41,174 (n=16), 10: -43,357 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +12,681 | 14 | 20 | 11 | 10842 | 5.25 | 14: -30,493 (n=93), 17: -30,670 (n=3199), 16: -31,045 (n=254), 13: -31,069 (n=25), 18: -31,254 (n=510), 19: -31,315 (n=494), 20: -31,508 (n=6163), 11: -32,310 (n=3), 15: -32,515 (n=86), 12: -35,464 (n=10), 10: -43,175 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +11,852 | 1 | 0 | 33 | 10839 | 25.04 | 1: -30,675 (n=511), 0: -30,954 (n=9410), 9: -31,146 (n=77), 2: -32,355 (n=95), 6: -32,690 (n=56), 19: -32,857 (n=3), 4: -33,386 (n=63), 8: -33,488 (n=58), 17: -33,644 (n=10), 5: -34,084 (n=97), 11: -34,405 (n=52), 3: -34,745 (n=141), 13: -35,630 (n=28), 7: -35,691 (n=59), 12: -36,258 (n=23), 28: -36,361 (n=2), 18: -36,506 (n=19), 16: -36,564 (n=7), 14: -36,586 (n=16), 15: -36,621 (n=19), 23: -36,694 (n=6), 20: -36,836 (n=5), 10: -37,066 (n=36), 24: -37,504 (n=4), 21: -38,157 (n=5), 39: -39,673 (n=7), 26: -40,268 (n=3), 40: -41,262 (n=6), 29: -41,395 (n=17), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,792 | 138 | 100 | 100 | 10841 | 61.43 | 138: -28,049 (n=2), 130: -28,802 (n=10), 92: -28,949 (n=12), 69: -29,128 (n=4), 62: -29,494 (n=4), 80: -29,664 (n=68), 85: -29,937 (n=81), 86: -29,955 (n=443), 81: -29,973 (n=59), 65: -30,099 (n=5), 94: -30,112 (n=26), 113: -30,212 (n=15), 93: -30,308 (n=282), 100: -30,583 (n=6836), 91: -30,703 (n=68), 120: -30,726 (n=13), 111: -30,738 (n=30), 114: -30,784 (n=20), 84: -30,886 (n=49), 115: -30,905 (n=21), 78: -31,050 (n=44), 70: -31,108 (n=14), 141: -31,181 (n=2), 125: -31,267 (n=82), 136: -31,307 (n=5), 83: -31,307 (n=102), 66: -31,331 (n=11), 82: -31,462 (n=17), 64: -31,589 (n=8), 133: -31,605 (n=8), 107: -31,707 (n=18), 129: -31,735 (n=13), 147: -31,811 (n=6), 103: -31,813 (n=22), 132: -31,873 (n=8), 63: -31,882 (n=9), 109: -31,931 (n=22), 102: -31,968 (n=36), 57: -31,969 (n=5), 123: -32,019 (n=24), 149: -32,176 (n=3), 101: -32,265 (n=25), 53: -32,281 (n=4), 90: -32,317 (n=52), 99: -32,348 (n=29), 68: -32,513 (n=7), 87: -32,517 (n=15), 67: -32,542 (n=6), 104: -32,573 (n=454), 95: -32,623 (n=28), 105: -32,647 (n=65), 128: -32,669 (n=13), 122: -32,768 (n=31), 71: -32,801 (n=19), 56: -32,821 (n=2), 112: -33,135 (n=188), 127: -33,219 (n=23), 76: -33,313 (n=15), 88: -33,376 (n=56), 97: -33,384 (n=48), 98: -33,515 (n=29), 79: -33,581 (n=35), 119: -33,644 (n=12), 89: -33,651 (n=133), 135: -33,677 (n=406), 96: -33,746 (n=35), 117: -33,872 (n=42), 116: -33,882 (n=48), 59: -33,898 (n=4), 124: -34,000 (n=20), 143: -34,012 (n=11), 121: -34,263 (n=9), 110: -34,415 (n=17), 134: -34,482 (n=7), 74: -34,483 (n=26), 108: -34,741 (n=22), 144: -34,772 (n=2), 55: -34,785 (n=2), 126: -34,796 (n=18), 75: -34,875 (n=52), 106: -35,055 (n=33), 150: -35,336 (n=154), 137: -35,375 (n=3), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 77: -36,373 (n=12), 148: -36,528 (n=3), 50: -36,637 (n=29), 58: -36,674 (n=4), 131: -36,786 (n=11), 73: -37,212 (n=8), 51: -37,500 (n=2), 118: -37,501 (n=12), 72: -37,976 (n=8), 140: -38,416 (n=3), 54: -39,448 (n=3), 60: -39,580 (n=7), 145: -39,842 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,636 | 0.0 | 0.0 | 13 | 10842 | 10.03 | 0.0: -30,793 (n=9202), 0.1: -32,954 (n=823), 0.2: -33,929 (n=500), 0.4: -34,381 (n=65), 0.3: -34,750 (n=127), 0.5: -34,761 (n=39), 1.1: -35,241 (n=6), 0.7: -36,679 (n=15), 0.6: -36,825 (n=26), 0.9: -37,063 (n=4), 1.0: -37,910 (n=22), 1.2: -39,109 (n=8), 0.8: -42,428 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +11,095 | 20 | 20 | 15 | 10842 | 6.76 | 20: -30,325 (n=5608), 19: -30,973 (n=3691), 18: -31,591 (n=255), 17: -34,209 (n=600), 21: -36,467 (n=223), 16: -36,565 (n=105), 23: -37,162 (n=49), 15: -37,458 (n=52), 22: -37,705 (n=106), 14: -38,260 (n=25), 25: -38,485 (n=16), 24: -38,829 (n=54), 26: -39,006 (n=31), 13: -39,668 (n=15), 12: -41,420 (n=12) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +10,683 | 6 | 18 | 21 | 10842 | 9.02 | 6: -29,449 (n=15), 14: -29,940 (n=16), 21: -30,348 (n=1728), 22: -30,660 (n=5173), 20: -31,110 (n=555), 23: -31,333 (n=491), 17: -32,322 (n=612), 25: -32,330 (n=958), 16: -32,695 (n=62), 18: -32,798 (n=480), 24: -33,162 (n=340), 12: -33,209 (n=9), 9: -33,807 (n=43), 19: -33,862 (n=148), 15: -34,112 (n=41), 13: -34,158 (n=18), 10: -34,521 (n=63), 5: -36,101 (n=35), 11: -36,828 (n=31), 7: -36,889 (n=20), 8: -40,131 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +10,348 | 14 | 13 | 9 | 10842 | 4.45 | 14: -30,244 (n=1402), 13: -31,249 (n=6570), 11: -31,311 (n=626), 12: -31,371 (n=1625), 15: -31,587 (n=311), 16: -33,270 (n=176), 10: -34,143 (n=85), 9: -37,455 (n=34), 8: -40,592 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,242 | 7 | 7 | 8 | 10842 | 6.06 | 7: -30,508 (n=9565), 6: -36,448 (n=682), 5: -36,507 (n=58), 8: -36,812 (n=341), 10: -36,887 (n=92), 9: -37,314 (n=68), 4: -38,314 (n=28), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,190 | 10 | 8 | 11 | 10842 | 8.15 | 10: -30,508 (n=9023), 7: -32,598 (n=326), 8: -34,871 (n=785), 9: -34,886 (n=417), 6: -35,413 (n=128), 5: -36,337 (n=12), 12: -38,044 (n=38), 4: -38,603 (n=19), 11: -38,941 (n=50), 14: -39,191 (n=25), 13: -40,698 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +10,065 | 0.55 | 0.5 | 15 | 10842 | 6.45 | 0.55: -29,916 (n=5387), 0.65: -31,687 (n=1054), 0.5: -31,883 (n=3078), 0.75: -31,949 (n=73), 0.7: -32,142 (n=180), 0.6: -32,857 (n=267), 0.8: -33,440 (n=35), 0.45: -34,687 (n=335), 0.9: -34,927 (n=9), 0.85: -35,798 (n=11), 0.35: -36,104 (n=119), 0.4: -36,323 (n=124), 0.95: -37,209 (n=3), 1.0: -39,813 (n=6), 0.3: -39,981 (n=161) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,789 | 0 | 0 | 9 | 10842 | 7.1 | 0: -30,869 (n=9763), 1: -34,123 (n=579), 2: -34,655 (n=228), 3: -34,985 (n=182), 4: -35,757 (n=52), 5: -36,586 (n=17), 7: -36,592 (n=4), 6: -37,226 (n=14), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +9,576 | 30 | 40 | 30 | 10842 | 7.53 | 30: -29,507 (n=43), 38: -29,983 (n=2085), 33: -30,378 (n=45), 34: -30,474 (n=182), 43: -30,485 (n=3081), 49: -30,510 (n=325), 37: -30,893 (n=347), 39: -31,060 (n=344), 44: -31,113 (n=266), 45: -31,115 (n=363), 26: -31,185 (n=29), 47: -31,396 (n=161), 28: -31,551 (n=12), 32: -31,797 (n=52), 46: -32,121 (n=69), 31: -32,144 (n=32), 29: -32,367 (n=13), 27: -32,492 (n=7), 35: -32,582 (n=168), 40: -32,680 (n=2402), 42: -33,081 (n=180), 36: -33,131 (n=160), 41: -33,205 (n=72), 50: -33,205 (n=288), 25: -34,303 (n=4), 20: -34,974 (n=27), 48: -35,089 (n=56), 24: -35,630 (n=22), 23: -36,850 (n=4), 22: -39,083 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +9,080 | 2 | 2 | 4 | 10842 | 2.84 | 2: -30,976 (n=10408), 1: -37,010 (n=349), 3: -38,625 (n=33), 0: -40,056 (n=52) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,906 | frontier | frontier | 2 | 10842 | 0.91 | frontier: -30,896 (n=10374), v312: -38,802 (n=468) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,507 | 2 | 2 | 3 | 10842 | 1.82 | 2: -30,841 (n=10199), 1: -37,466 (n=605), 3: -38,348 (n=38) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,487 | 14 | 12 | 10 | 10842 | 7.46 | 14: -30,945 (n=9176), 13: -31,636 (n=728), 12: -32,964 (n=497), 11: -33,157 (n=162), 6: -34,434 (n=3), 9: -35,295 (n=23), 10: -35,455 (n=219), 7: -35,898 (n=8), 8: -36,937 (n=24), 5: -38,432 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2053)
- (10, 3, 6): -16,840 (n=1690)
- (8, 3, 5): -16,866 (n=215)
- (9, 3, 6): -16,959 (n=1279)
- (8, 3, 6): -17,804 (n=596)
- (12, 4, 6): -17,899 (n=382)
- (10, 4, 6): -17,975 (n=1498)
- (11, 3, 6): -18,175 (n=387)
- (11, 4, 6): -19,867 (n=423)
- (17, 3, 6): -20,013 (n=47)
- (8, 4, 6): -21,051 (n=531)
- (13, 4, 6): -21,868 (n=134)
- (8, 3, 4): -22,126 (n=62)
- (13, 3, 6): -22,174 (n=204)
- (10, 3, 5): -22,188 (n=46)

_Generated 2026-09-08 10:34. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 2221 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=2221); harvest_min=1–3 (n=2221); wheat_tiles=0–8 (n=2221); wheat_stock=0–40 (n=2221); min_hands=3–6 (n=2221); load_per_hand=12–26 (n=2221); geese=0–2 (n=2221); open_melons=4–14 (n=2221)
- **Evidence:** 2221 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 25 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=25); harvest_min=1–3 (n=25); wheat_tiles=0–2 (n=25); wheat_stock=0–4 (n=25); min_hands=3–6 (n=25); load_per_hand=19–21 (n=25); geese=0–2 (n=25); open_melons=7–13 (n=25)
- **Evidence:** 25 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 12 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=12); harvest_min=1–3 (n=12); wheat_tiles=0; wheat_stock=0–29 (n=12); min_hands=3–6 (n=12); load_per_hand=12–20 (n=12); geese=0–1 (n=12); open_melons=9–10 (n=12)
- **Evidence:** 12 candidates, multiple seeds. Confidence: moderate

### LABOR_FAILURE (observed in 11 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=11); harvest_min=1–3 (n=11); wheat_tiles=0–8 (n=11); wheat_stock=0–20 (n=11); min_hands=3–6 (n=11); load_per_hand=12–17 (n=11); geese=0–2 (n=11); open_melons=8–14 (n=11)
- **Evidence:** 11 candidates, multiple seeds. Confidence: moderate

### None (observed in 7 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=7); harvest_min=1–2 (n=7); wheat_tiles=0; wheat_stock=0–11 (n=7); min_hands=3–6 (n=7); load_per_hand=12–18 (n=7); geese=0–2 (n=7); open_melons=10–14 (n=7)
- **Evidence:** 7 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 10:34. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._