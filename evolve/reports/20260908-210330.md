# Evolution run 20260908-210330

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1247 · games 23,632 (11,810/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 451 | 902 |
| dead_pattern | 193 | 386 |
| dead_smoke | 165 | 1320 |
| alive | 438 | 21024 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 13547 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1654
- M2: best -16,461 (`0c25e1226b27`), n=1698
- c1: best -16,310 (`23734cef4da1`), n=2432
- queue: best -15,412 (`fe4745b56024`), n=3329
- v312: best -15,275 (`52b3d5cc236e`), n=2309
- wide: best -16,047 (`512e53fe15bc`), n=2125

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +20,677 | 120 | 50 | 143 | 13538 | 65.31 | 120: -21,091 (n=5), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,592 (n=3), 19: -27,891 (n=15), 141: -28,093 (n=5), 5: -28,588 (n=46), 112: -28,796 (n=13), 35: -28,878 (n=10), 27: -29,531 (n=36), 89: -29,645 (n=29), 58: -29,760 (n=102), 26: -29,760 (n=7), 92: -29,829 (n=341), 71: -29,830 (n=26), 56: -29,949 (n=14), 74: -30,033 (n=210), 18: -30,085 (n=801), 51: -30,122 (n=13), 106: -30,376 (n=9), 63: -30,378 (n=217), 80: -30,487 (n=14), 49: -30,553 (n=74), 72: -30,675 (n=9), 48: -30,728 (n=518), 61: -30,784 (n=96), 50: -30,813 (n=6699), 108: -30,839 (n=6), 65: -30,958 (n=128), 150: -30,990 (n=164), 86: -31,018 (n=9), 60: -31,184 (n=29), 42: -31,251 (n=754), 85: -31,279 (n=9), 70: -31,301 (n=35), 40: -31,367 (n=93), 97: -31,444 (n=27), 66: -31,517 (n=231), 33: -31,521 (n=22), 45: -31,556 (n=112), 2: -31,685 (n=2), 57: -31,735 (n=82), 93: -31,753 (n=7), 144: -31,766 (n=3), 94: -31,771 (n=17), 73: -31,772 (n=16), 14: -31,806 (n=20), 96: -31,865 (n=7), 59: -31,866 (n=19), 36: -31,923 (n=108), 9: -31,947 (n=16), 113: -32,112 (n=13), 62: -32,220 (n=17), 110: -32,277 (n=4), 69: -32,395 (n=23), 39: -32,408 (n=53), 103: -32,462 (n=9), 68: -32,488 (n=14), 115: -32,512 (n=8), 84: -32,518 (n=13), 25: -32,636 (n=8), 76: -32,669 (n=12), 38: -32,804 (n=17), 52: -32,811 (n=14), 20: -32,812 (n=6), 109: -32,844 (n=3), 98: -32,926 (n=20), 55: -33,016 (n=540), 31: -33,053 (n=13), 21: -33,189 (n=10), 104: -33,266 (n=4), 6: -33,331 (n=10), 119: -33,340 (n=2), 41: -33,381 (n=37), 4: -33,399 (n=36), 83: -33,443 (n=103), 0: -33,444 (n=194), 95: -33,449 (n=5), 13: -33,499 (n=7), 22: -33,559 (n=15), 54: -33,612 (n=21), 43: -33,691 (n=18), 30: -33,763 (n=16), 24: -33,814 (n=20), 90: -33,822 (n=7), 81: -33,835 (n=24), 88: -33,874 (n=11), 32: -33,992 (n=9), 111: -34,111 (n=8), 10: -34,204 (n=14), 44: -34,233 (n=20), 99: -34,244 (n=72), 82: -34,317 (n=44), 102: -34,320 (n=4), 28: -34,350 (n=19), 1: -34,413 (n=5), 134: -34,464 (n=2), 15: -34,489 (n=10), 78: -34,492 (n=11), 7: -34,621 (n=7), 136: -34,622 (n=40), 23: -34,633 (n=12), 64: -34,667 (n=20), 37: -34,726 (n=12), 16: -34,787 (n=16), 46: -34,812 (n=33), 79: -34,930 (n=14), 107: -34,965 (n=5), 77: -35,141 (n=222), 100: -35,199 (n=46), 34: -35,231 (n=60), 101: -35,278 (n=11), 53: -35,297 (n=31), 17: -35,508 (n=6), 11: -35,563 (n=13), 91: -35,821 (n=9), 87: -35,852 (n=10), 129: -35,951 (n=77), 47: -36,381 (n=19), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 12: -36,634 (n=11), 145: -36,990 (n=7), 67: -37,049 (n=18), 75: -37,220 (n=8), 29: -37,270 (n=27), 114: -37,341 (n=4), 127: -38,268 (n=2), 140: -38,489 (n=3), 131: -38,847 (n=2), 124: -39,372 (n=2), 132: -39,931 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,197 | 26 | 30 | 25 | 13546 | 10.59 | 26: -30,556 (n=442), 25: -30,763 (n=6539), 30: -30,961 (n=4378), 31: -31,580 (n=123), 29: -31,918 (n=113), 27: -32,382 (n=219), 28: -33,526 (n=1130), 41: -34,307 (n=3), 32: -34,640 (n=129), 35: -34,706 (n=173), 38: -35,532 (n=17), 33: -35,541 (n=115), 37: -35,709 (n=23), 34: -36,049 (n=59), 39: -36,441 (n=11), 42: -36,946 (n=4), 36: -37,791 (n=33), 40: -38,440 (n=11), 46: -38,521 (n=3), 44: -38,790 (n=5), 47: -39,384 (n=2), 50: -40,198 (n=7), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,232 | 1 | 0 | 34 | 13544 | 25.38 | 1: -30,294 (n=850), 0: -31,060 (n=11526), 9: -31,136 (n=90), 22: -31,539 (n=2), 2: -32,481 (n=129), 4: -33,163 (n=83), 6: -33,231 (n=81), 8: -33,437 (n=70), 17: -33,768 (n=12), 19: -34,158 (n=6), 5: -34,471 (n=129), 11: -34,482 (n=60), 3: -34,550 (n=162), 7: -35,752 (n=78), 13: -35,868 (n=41), 12: -36,057 (n=28), 14: -36,151 (n=22), 20: -36,357 (n=6), 28: -36,361 (n=2), 18: -36,506 (n=19), 16: -36,588 (n=9), 23: -36,694 (n=6), 15: -36,705 (n=27), 24: -37,048 (n=7), 10: -37,321 (n=43), 39: -37,389 (n=10), 21: -38,756 (n=6), 40: -39,508 (n=8), 26: -40,268 (n=3), 29: -41,407 (n=25), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,199 | 3 | 3 | 4 | 13547 | 2.61 | 3: -30,784 (n=12224), 2: -35,877 (n=944), 4: -36,466 (n=361), 5: -42,983 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 13546 | 62.32 | 61: -27,918 (n=2), 138: -28,049 (n=2), 130: -28,649 (n=12), 80: -29,307 (n=158), 65: -30,099 (n=5), 93: -30,154 (n=357), 91: -30,178 (n=83), 120: -30,188 (n=14), 85: -30,197 (n=89), 81: -30,241 (n=77), 86: -30,434 (n=634), 69: -30,487 (n=8), 129: -30,493 (n=16), 114: -30,605 (n=24), 100: -30,747 (n=8577), 111: -30,789 (n=35), 113: -30,885 (n=18), 62: -30,897 (n=5), 92: -30,931 (n=21), 94: -31,054 (n=31), 115: -31,205 (n=29), 133: -31,210 (n=9), 78: -31,245 (n=78), 125: -31,258 (n=87), 84: -31,414 (n=63), 123: -31,416 (n=40), 141: -31,447 (n=3), 107: -31,477 (n=25), 83: -31,600 (n=110), 147: -31,607 (n=7), 64: -31,620 (n=10), 95: -31,833 (n=34), 99: -31,842 (n=32), 63: -31,882 (n=9), 102: -31,919 (n=40), 70: -31,925 (n=18), 57: -31,969 (n=5), 132: -31,971 (n=11), 90: -32,032 (n=79), 105: -32,120 (n=91), 109: -32,156 (n=29), 149: -32,176 (n=3), 53: -32,281 (n=4), 66: -32,339 (n=13), 103: -32,387 (n=26), 117: -32,501 (n=81), 71: -32,513 (n=20), 82: -32,550 (n=22), 87: -32,552 (n=18), 67: -32,561 (n=7), 104: -32,568 (n=534), 55: -32,666 (n=3), 76: -32,934 (n=18), 127: -32,961 (n=28), 119: -33,009 (n=14), 136: -33,061 (n=6), 112: -33,124 (n=198), 122: -33,164 (n=35), 88: -33,335 (n=61), 128: -33,341 (n=22), 101: -33,374 (n=35), 110: -33,465 (n=20), 97: -33,478 (n=52), 134: -33,531 (n=8), 68: -33,616 (n=10), 89: -33,684 (n=144), 135: -33,762 (n=441), 59: -33,898 (n=4), 96: -33,929 (n=39), 126: -33,969 (n=24), 74: -34,002 (n=31), 143: -34,012 (n=11), 116: -34,013 (n=58), 121: -34,025 (n=11), 79: -34,147 (n=40), 98: -34,361 (n=39), 124: -34,395 (n=21), 75: -34,479 (n=58), 108: -34,759 (n=26), 144: -34,772 (n=2), 137: -34,809 (n=4), 106: -34,885 (n=40), 150: -35,597 (n=168), 56: -35,769 (n=4), 131: -35,872 (n=13), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 50: -36,381 (n=44), 148: -36,528 (n=3), 58: -36,674 (n=4), 118: -36,824 (n=14), 77: -37,179 (n=19), 51: -37,500 (n=2), 72: -37,554 (n=9), 73: -37,735 (n=11), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,525 | 0.0 | 0.0 | 13 | 13547 | 10.21 | 0.0: -30,919 (n=11677), 0.1: -33,056 (n=917), 0.2: -33,759 (n=560), 0.4: -34,196 (n=82), 0.3: -34,447 (n=157), 1.1: -34,978 (n=7), 0.5: -35,043 (n=50), 0.7: -36,163 (n=16), 0.6: -36,955 (n=38), 0.9: -37,347 (n=5), 1.0: -37,742 (n=23), 1.2: -39,081 (n=9), 0.8: -42,444 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,873 | 6 | 6 | 8 | 13547 | 6.12 | 6: -30,712 (n=12065), 5: -34,673 (n=598), 7: -36,350 (n=358), 4: -37,306 (n=329), 3: -37,807 (n=117), 8: -38,356 (n=55), 9: -40,761 (n=19), 10: -41,585 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,797 | 13 | 20 | 11 | 13547 | 4.95 | 13: -30,230 (n=33), 17: -30,885 (n=4322), 16: -31,034 (n=305), 14: -31,147 (n=114), 19: -31,297 (n=668), 18: -31,370 (n=639), 20: -31,539 (n=7325), 15: -32,123 (n=116), 11: -32,310 (n=3), 12: -35,077 (n=14), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,678 | 20 | 20 | 15 | 13547 | 7.29 | 20: -30,502 (n=7487), 19: -30,968 (n=4199), 18: -31,613 (n=309), 17: -34,336 (n=666), 21: -36,382 (n=285), 16: -36,408 (n=126), 15: -37,228 (n=62), 23: -37,350 (n=67), 22: -37,703 (n=149), 14: -38,059 (n=33), 26: -38,591 (n=38), 24: -39,020 (n=72), 25: -39,340 (n=21), 13: -39,412 (n=17), 12: -41,180 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,115 | 7 | 7 | 8 | 13547 | 6.1 | 7: -30,635 (n=12029), 6: -36,422 (n=781), 5: -36,561 (n=65), 8: -36,657 (n=431), 10: -36,754 (n=104), 9: -37,164 (n=90), 4: -38,293 (n=39), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +9,872 | 10 | 8 | 11 | 13547 | 8.26 | 10: -30,656 (n=11405), 7: -32,542 (n=410), 8: -34,735 (n=874), 9: -34,969 (n=499), 6: -35,453 (n=160), 5: -36,214 (n=20), 12: -37,961 (n=44), 4: -38,137 (n=22), 11: -38,466 (n=59), 14: -39,326 (n=26), 13: -40,528 (n=28) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,767 | 0.55 | 0.5 | 15 | 13547 | 7.06 | 0.55: -30,191 (n=7281), 0.65: -31,741 (n=1132), 0.5: -31,865 (n=3499), 0.75: -31,990 (n=95), 0.7: -32,333 (n=220), 0.6: -32,842 (n=321), 0.8: -33,499 (n=43), 0.45: -34,626 (n=417), 0.9: -35,286 (n=10), 0.35: -36,029 (n=148), 0.4: -36,261 (n=152), 0.85: -36,343 (n=12), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,958 (n=207) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,687 | 0 | 0 | 9 | 13547 | 7.15 | 0: -30,971 (n=12262), 1: -34,034 (n=687), 2: -34,614 (n=268), 3: -34,933 (n=212), 4: -35,752 (n=69), 5: -35,863 (n=20), 7: -36,914 (n=5), 6: -37,732 (n=21), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +9,333 | 14 | 13 | 9 | 13547 | 4.36 | 14: -30,667 (n=2039), 13: -31,282 (n=8074), 11: -31,313 (n=726), 12: -31,450 (n=1900), 15: -31,495 (n=407), 16: -33,382 (n=238), 10: -33,795 (n=104), 9: -37,197 (n=42), 8: -40,000 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +9,232 | 6 | 18 | 21 | 13547 | 9.24 | 6: -29,398 (n=16), 21: -30,540 (n=2321), 22: -30,785 (n=6605), 14: -30,917 (n=18), 20: -31,267 (n=633), 23: -31,367 (n=614), 16: -32,244 (n=81), 17: -32,418 (n=700), 25: -32,453 (n=1141), 18: -32,947 (n=553), 24: -33,135 (n=390), 15: -33,257 (n=46), 12: -33,342 (n=11), 19: -33,564 (n=175), 13: -33,955 (n=22), 9: -34,042 (n=48), 10: -34,524 (n=66), 11: -36,402 (n=33), 7: -36,441 (n=21), 5: -36,511 (n=48), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,801 | 2 | 2 | 4 | 13547 | 2.84 | 2: -31,055 (n=13009), 1: -36,929 (n=434), 3: -38,436 (n=36), 0: -39,856 (n=68) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +7,970 | 13 | 12 | 11 | 13546 | 7.47 | 13: -31,051 (n=974), 14: -31,110 (n=11473), 12: -32,812 (n=590), 11: -32,856 (n=196), 6: -34,434 (n=3), 9: -34,835 (n=26), 10: -35,282 (n=243), 7: -36,209 (n=9), 8: -37,176 (n=29), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,665 | frontier | frontier | 2 | 13547 | 0.92 | frontier: -30,984 (n=12977), v312: -38,650 (n=570) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,454 | 2 | 2 | 3 | 13547 | 1.82 | 2: -30,916 (n=12744), 1: -37,451 (n=754), 3: -38,371 (n=49) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,256 | 38 | 40 | 30 | 13547 | 7.47 | 38: -30,308 (n=2916), 34: -30,571 (n=230), 43: -30,589 (n=3825), 49: -30,616 (n=402), 33: -30,694 (n=52), 30: -30,989 (n=61), 44: -31,048 (n=343), 37: -31,143 (n=481), 47: -31,153 (n=223), 39: -31,369 (n=457), 45: -31,373 (n=515), 27: -31,389 (n=8), 28: -31,842 (n=15), 32: -31,859 (n=60), 26: -32,308 (n=41), 46: -32,337 (n=90), 29: -32,637 (n=16), 31: -32,684 (n=38), 40: -32,735 (n=2606), 35: -32,809 (n=211), 42: -32,958 (n=211), 36: -33,123 (n=176), 50: -33,150 (n=344), 41: -33,288 (n=88), 25: -33,906 (n=6), 48: -34,954 (n=63), 20: -34,997 (n=36), 24: -35,533 (n=23), 23: -36,212 (n=6), 22: -37,564 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2554)
- (10, 3, 6): -16,840 (n=2182)
- (8, 3, 5): -16,866 (n=249)
- (9, 3, 6): -16,959 (n=1680)
- (12, 4, 6): -17,058 (n=441)
- (8, 3, 6): -17,552 (n=704)
- (10, 4, 6): -17,975 (n=1899)
- (11, 3, 6): -18,175 (n=472)
- (11, 4, 6): -19,867 (n=486)
- (17, 3, 6): -20,013 (n=56)
- (8, 4, 6): -21,051 (n=645)
- (13, 4, 6): -21,868 (n=177)
- (8, 3, 4): -22,126 (n=71)
- (13, 3, 6): -22,174 (n=256)
- (10, 3, 5): -22,188 (n=55)

_Generated 2026-09-08 23:03. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 4415 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=4415); harvest_min=1–3 (n=4415); wheat_tiles=0–8 (n=4415); wheat_stock=0–40 (n=4415); min_hands=3–6 (n=4415); load_per_hand=12–26 (n=4415); geese=0–2 (n=4415); open_melons=4–14 (n=4415)
- **Evidence:** 4415 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 56 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=56); harvest_min=1–3 (n=56); wheat_tiles=0–2 (n=56); wheat_stock=0–4 (n=56); min_hands=3–6 (n=56); load_per_hand=15–21 (n=56); geese=0–2 (n=56); open_melons=7–13 (n=56)
- **Evidence:** 56 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 33 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=33); harvest_min=1–3 (n=33); wheat_tiles=0; wheat_stock=0–39 (n=33); min_hands=3–6 (n=33); load_per_hand=12–26 (n=33); geese=0–1 (n=33); open_melons=4–13 (n=33)
- **Evidence:** 33 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 19 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=19); harvest_min=1–3 (n=19); wheat_tiles=0–8 (n=19); wheat_stock=0–39 (n=19); min_hands=3–6 (n=19); load_per_hand=12–23 (n=19); geese=0–2 (n=19); open_melons=8–14 (n=19)
- **Evidence:** 19 candidates, multiple seeds. Confidence: high

### None (observed in 10 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=10); harvest_min=1–3 (n=10); wheat_tiles=0; wheat_stock=0–11 (n=10); min_hands=3–6 (n=10); load_per_hand=12–18 (n=10); geese=0–2 (n=10); open_melons=7–14 (n=10)
- **Evidence:** 10 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-08 23:03. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._