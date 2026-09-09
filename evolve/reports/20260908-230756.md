# Evolution run 20260908-230756

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1224 · games 23,576 (11,784/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 393 | 786 |
| dead_pattern | 243 | 486 |
| dead_smoke | 148 | 1184 |
| alive | 440 | 21120 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 13987 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1725
- M2: best -16,461 (`0c25e1226b27`), n=1769
- c1: best -16,310 (`23734cef4da1`), n=2505
- queue: best -15,412 (`fe4745b56024`), n=3419
- v312: best -15,275 (`52b3d5cc236e`), n=2374
- wide: best -16,047 (`512e53fe15bc`), n=2195

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +20,931 | 120 | 50 | 144 | 13977 | 65.19 | 120: -20,837 (n=6), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,592 (n=3), 19: -27,891 (n=15), 141: -28,093 (n=5), 5: -28,805 (n=47), 35: -28,918 (n=11), 112: -29,479 (n=14), 27: -29,531 (n=36), 89: -29,645 (n=29), 58: -29,743 (n=105), 26: -29,760 (n=7), 92: -29,951 (n=351), 74: -29,968 (n=224), 18: -30,074 (n=840), 51: -30,123 (n=16), 80: -30,197 (n=15), 56: -30,266 (n=15), 71: -30,289 (n=28), 63: -30,428 (n=231), 49: -30,575 (n=75), 72: -30,675 (n=9), 48: -30,681 (n=523), 50: -30,801 (n=6904), 61: -30,803 (n=98), 65: -30,836 (n=131), 108: -30,839 (n=6), 86: -31,018 (n=9), 60: -31,184 (n=29), 150: -31,195 (n=172), 30: -31,227 (n=21), 42: -31,243 (n=771), 70: -31,257 (n=39), 40: -31,347 (n=97), 97: -31,347 (n=29), 66: -31,434 (n=251), 85: -31,445 (n=10), 33: -31,521 (n=22), 45: -31,559 (n=113), 14: -31,674 (n=21), 2: -31,685 (n=2), 94: -31,729 (n=18), 144: -31,766 (n=3), 106: -31,771 (n=12), 73: -31,772 (n=16), 96: -31,865 (n=7), 59: -31,866 (n=19), 57: -31,878 (n=83), 9: -31,947 (n=16), 36: -31,963 (n=109), 113: -32,112 (n=13), 110: -32,277 (n=4), 69: -32,395 (n=23), 39: -32,408 (n=53), 103: -32,462 (n=9), 115: -32,512 (n=8), 93: -32,523 (n=8), 62: -32,601 (n=18), 84: -32,611 (n=14), 25: -32,636 (n=8), 52: -32,698 (n=15), 38: -32,804 (n=17), 20: -32,812 (n=6), 109: -32,844 (n=3), 98: -32,926 (n=20), 55: -33,002 (n=559), 31: -33,053 (n=13), 41: -33,062 (n=38), 68: -33,170 (n=16), 21: -33,189 (n=10), 104: -33,266 (n=4), 6: -33,331 (n=10), 119: -33,340 (n=2), 76: -33,355 (n=15), 4: -33,399 (n=36), 83: -33,443 (n=103), 95: -33,449 (n=5), 81: -33,458 (n=26), 0: -33,465 (n=199), 13: -33,499 (n=7), 22: -33,559 (n=15), 54: -33,612 (n=21), 43: -33,616 (n=19), 24: -33,814 (n=20), 90: -33,822 (n=7), 53: -33,858 (n=37), 88: -33,874 (n=11), 32: -33,992 (n=9), 111: -34,111 (n=8), 17: -34,184 (n=7), 10: -34,204 (n=14), 44: -34,233 (n=20), 99: -34,244 (n=72), 82: -34,251 (n=45), 102: -34,320 (n=4), 28: -34,350 (n=19), 1: -34,413 (n=5), 134: -34,464 (n=2), 15: -34,489 (n=10), 78: -34,492 (n=11), 7: -34,621 (n=7), 136: -34,622 (n=40), 23: -34,633 (n=12), 46: -34,633 (n=34), 64: -34,667 (n=20), 37: -34,726 (n=12), 16: -34,787 (n=16), 79: -34,930 (n=14), 107: -34,965 (n=5), 77: -35,183 (n=226), 101: -35,278 (n=11), 34: -35,328 (n=61), 100: -35,377 (n=48), 11: -35,563 (n=13), 129: -35,839 (n=81), 87: -35,852 (n=10), 91: -35,887 (n=10), 47: -36,381 (n=19), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 12: -36,634 (n=11), 145: -36,990 (n=7), 67: -37,049 (n=18), 114: -37,341 (n=4), 75: -37,579 (n=9), 29: -37,824 (n=30), 127: -38,268 (n=2), 140: -38,489 (n=3), 131: -38,847 (n=2), 132: -39,931 (n=2), 124: -39,994 (n=3), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,303 | 26 | 30 | 25 | 13986 | 10.63 | 26: -30,450 (n=458), 25: -30,766 (n=6775), 30: -30,965 (n=4529), 31: -31,538 (n=126), 29: -31,918 (n=113), 27: -32,348 (n=222), 28: -33,521 (n=1153), 41: -34,307 (n=3), 32: -34,520 (n=133), 35: -34,758 (n=175), 38: -35,532 (n=17), 33: -35,546 (n=116), 37: -35,709 (n=23), 34: -36,049 (n=59), 39: -36,441 (n=11), 42: -36,946 (n=4), 36: -37,791 (n=33), 40: -38,440 (n=11), 46: -38,521 (n=3), 44: -38,790 (n=5), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,302 | 1 | 0 | 34 | 13984 | 25.28 | 1: -30,224 (n=906), 9: -31,008 (n=92), 0: -31,055 (n=11855), 22: -31,539 (n=2), 2: -32,591 (n=137), 4: -32,939 (n=89), 6: -33,117 (n=88), 8: -33,389 (n=74), 19: -34,158 (n=6), 17: -34,402 (n=14), 3: -34,446 (n=168), 5: -34,639 (n=137), 11: -34,670 (n=64), 7: -35,662 (n=81), 13: -35,868 (n=41), 12: -35,897 (n=31), 16: -35,905 (n=11), 14: -36,151 (n=22), 20: -36,357 (n=6), 28: -36,361 (n=2), 18: -36,506 (n=19), 23: -36,694 (n=6), 15: -36,705 (n=27), 24: -37,048 (n=7), 10: -37,321 (n=43), 39: -37,389 (n=10), 21: -38,756 (n=6), 40: -39,508 (n=8), 26: -40,268 (n=3), 29: -41,407 (n=25), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +12,204 | 3 | 3 | 4 | 13987 | 2.61 | 3: -30,779 (n=12628), 2: -35,846 (n=972), 4: -36,465 (n=369), 5: -42,983 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,531 | 0.0 | 0.0 | 13 | 13987 | 10.22 | 0.0: -30,913 (n=12072), 0.1: -33,059 (n=943), 0.2: -33,719 (n=568), 0.4: -34,197 (n=84), 0.3: -34,399 (n=163), 1.1: -34,978 (n=7), 0.5: -35,028 (n=51), 0.7: -36,163 (n=16), 0.6: -37,126 (n=39), 0.9: -37,347 (n=5), 1.0: -37,756 (n=24), 1.2: -39,081 (n=9), 0.8: -42,444 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 13986 | 62.31 | 61: -27,918 (n=2), 138: -28,049 (n=2), 130: -28,649 (n=12), 80: -29,388 (n=182), 120: -29,534 (n=15), 65: -30,099 (n=5), 85: -30,100 (n=90), 93: -30,137 (n=362), 81: -30,320 (n=80), 91: -30,351 (n=86), 86: -30,399 (n=655), 69: -30,487 (n=8), 114: -30,605 (n=24), 129: -30,656 (n=17), 100: -30,761 (n=8855), 113: -30,885 (n=18), 111: -30,925 (n=36), 92: -30,954 (n=24), 115: -30,975 (n=30), 94: -31,179 (n=33), 125: -31,182 (n=89), 133: -31,210 (n=9), 123: -31,279 (n=41), 78: -31,357 (n=85), 90: -31,411 (n=89), 55: -31,425 (n=4), 141: -31,447 (n=3), 107: -31,477 (n=25), 83: -31,600 (n=110), 147: -31,607 (n=7), 64: -31,620 (n=10), 109: -31,654 (n=31), 67: -31,660 (n=9), 84: -31,791 (n=66), 63: -31,882 (n=9), 102: -31,919 (n=40), 70: -31,925 (n=18), 57: -31,969 (n=5), 132: -31,971 (n=11), 99: -31,977 (n=33), 95: -32,031 (n=36), 149: -32,176 (n=3), 105: -32,201 (n=101), 53: -32,281 (n=4), 66: -32,339 (n=13), 117: -32,360 (n=87), 103: -32,387 (n=26), 71: -32,513 (n=20), 104: -32,538 (n=545), 82: -32,550 (n=22), 87: -32,552 (n=18), 128: -32,572 (n=24), 62: -32,574 (n=6), 127: -32,871 (n=29), 76: -32,934 (n=18), 110: -32,958 (n=24), 119: -33,009 (n=14), 88: -33,086 (n=63), 112: -33,124 (n=198), 122: -33,181 (n=36), 97: -33,478 (n=52), 101: -33,529 (n=36), 134: -33,531 (n=8), 89: -33,613 (n=146), 68: -33,616 (n=10), 135: -33,752 (n=448), 96: -33,780 (n=41), 59: -33,898 (n=4), 126: -33,966 (n=25), 143: -34,012 (n=11), 121: -34,025 (n=11), 116: -34,072 (n=61), 74: -34,126 (n=33), 79: -34,147 (n=40), 98: -34,165 (n=40), 136: -34,218 (n=7), 124: -34,395 (n=21), 75: -34,479 (n=58), 108: -34,512 (n=27), 144: -34,772 (n=2), 137: -34,809 (n=4), 106: -35,003 (n=42), 150: -35,597 (n=168), 72: -35,612 (n=10), 56: -35,769 (n=4), 50: -35,778 (n=46), 131: -35,872 (n=13), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 118: -36,824 (n=14), 58: -36,875 (n=5), 77: -37,179 (n=19), 51: -37,500 (n=2), 73: -37,735 (n=11), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,842 | 13 | 20 | 11 | 13987 | 4.91 | 13: -30,185 (n=35), 17: -30,874 (n=4499), 16: -31,059 (n=319), 19: -31,225 (n=695), 14: -31,227 (n=115), 18: -31,443 (n=664), 20: -31,526 (n=7515), 15: -32,283 (n=120), 11: -32,310 (n=3), 12: -35,077 (n=14), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,670 | 20 | 20 | 15 | 13987 | 7.36 | 20: -30,510 (n=7795), 19: -30,944 (n=4289), 18: -31,559 (n=318), 17: -34,326 (n=675), 16: -36,429 (n=128), 21: -36,441 (n=296), 15: -37,228 (n=62), 23: -37,531 (n=70), 22: -37,731 (n=154), 14: -38,037 (n=34), 26: -38,591 (n=38), 24: -38,987 (n=74), 25: -39,340 (n=21), 13: -39,412 (n=17), 12: -41,180 (n=16) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,366 | 6 | 6 | 8 | 13987 | 6.13 | 6: -30,701 (n=12460), 5: -34,642 (n=617), 7: -36,361 (n=362), 4: -37,361 (n=344), 3: -37,765 (n=123), 8: -38,356 (n=55), 9: -40,761 (n=19), 10: -41,067 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,124 | 7 | 7 | 8 | 13987 | 6.11 | 7: -30,627 (n=12427), 6: -36,448 (n=802), 5: -36,532 (n=66), 8: -36,626 (n=446), 10: -36,764 (n=109), 9: -37,164 (n=90), 4: -38,293 (n=39), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,101 | 10 | 8 | 11 | 13987 | 8.27 | 10: -30,650 (n=11792), 7: -32,578 (n=427), 8: -34,706 (n=892), 9: -34,958 (n=509), 6: -35,461 (n=161), 5: -36,214 (n=20), 12: -37,961 (n=44), 4: -38,137 (n=22), 11: -38,544 (n=62), 14: -39,504 (n=28), 13: -40,750 (n=30) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,715 | 0.55 | 0.5 | 15 | 13987 | 7.13 | 0.55: -30,206 (n=7582), 0.65: -31,706 (n=1151), 0.5: -31,831 (n=3569), 0.75: -32,026 (n=98), 0.7: -32,262 (n=228), 0.6: -32,988 (n=336), 0.8: -33,852 (n=45), 0.45: -34,608 (n=427), 0.9: -35,286 (n=10), 0.35: -36,009 (n=149), 0.4: -36,218 (n=154), 0.85: -37,125 (n=13), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,921 (n=215) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,695 | 0 | 0 | 9 | 13987 | 7.15 | 0: -30,963 (n=12664), 1: -34,047 (n=701), 2: -34,584 (n=278), 3: -34,829 (n=218), 4: -35,563 (n=74), 7: -35,683 (n=6), 5: -35,863 (n=20), 6: -37,601 (n=23), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +9,288 | 14 | 13 | 9 | 13987 | 4.36 | 14: -30,712 (n=2142), 11: -31,256 (n=738), 13: -31,269 (n=8331), 12: -31,410 (n=1946), 15: -31,628 (n=421), 16: -33,388 (n=242), 10: -33,573 (n=107), 9: -37,206 (n=43), 8: -40,000 (n=17) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,834 | 6 | 18 | 21 | 13987 | 9.25 | 6: -29,796 (n=17), 21: -30,531 (n=2425), 22: -30,783 (n=6830), 14: -30,917 (n=18), 20: -31,233 (n=643), 23: -31,318 (n=635), 16: -32,203 (n=83), 17: -32,452 (n=715), 25: -32,468 (n=1167), 18: -32,906 (n=566), 24: -33,142 (n=401), 15: -33,314 (n=47), 12: -33,342 (n=11), 19: -33,587 (n=180), 13: -33,863 (n=23), 9: -33,993 (n=50), 10: -34,524 (n=66), 11: -36,049 (n=34), 7: -36,441 (n=21), 5: -36,496 (n=50), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,608 | 2 | 2 | 4 | 13987 | 2.84 | 2: -31,046 (n=13433), 1: -36,925 (n=447), 3: -38,354 (n=38), 0: -39,654 (n=69) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,068 | 13 | 12 | 11 | 13986 | 7.46 | 13: -30,953 (n=1027), 14: -31,112 (n=11838), 12: -32,797 (n=606), 11: -32,856 (n=198), 6: -34,434 (n=3), 9: -34,835 (n=26), 10: -35,226 (n=247), 7: -36,209 (n=9), 8: -37,176 (n=29), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,657 | frontier | frontier | 2 | 13987 | 0.92 | frontier: -30,974 (n=13398), v312: -38,632 (n=589) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,467 | 2 | 2 | 3 | 13987 | 1.82 | 2: -30,906 (n=13162), 1: -37,469 (n=774), 3: -38,373 (n=51) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,250 | 38 | 40 | 30 | 13987 | 7.5 | 38: -30,337 (n=3031), 34: -30,442 (n=240), 43: -30,584 (n=3962), 49: -30,606 (n=409), 33: -30,822 (n=53), 44: -30,909 (n=368), 30: -30,989 (n=61), 37: -31,182 (n=501), 47: -31,202 (n=236), 45: -31,263 (n=532), 27: -31,389 (n=8), 39: -31,508 (n=478), 28: -31,842 (n=15), 32: -31,859 (n=60), 26: -31,909 (n=47), 46: -32,344 (n=94), 31: -32,684 (n=38), 40: -32,727 (n=2630), 29: -32,779 (n=17), 35: -32,931 (n=217), 42: -32,960 (n=213), 50: -33,049 (n=355), 36: -33,089 (n=177), 25: -33,175 (n=7), 41: -33,231 (n=96), 48: -34,759 (n=68), 20: -34,957 (n=39), 24: -35,776 (n=24), 23: -36,212 (n=6), 22: -37,587 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2633)
- (10, 3, 6): -16,840 (n=2273)
- (8, 3, 5): -16,866 (n=256)
- (9, 3, 6): -16,909 (n=1745)
- (12, 4, 6): -17,058 (n=453)
- (8, 3, 6): -17,552 (n=714)
- (10, 4, 6): -17,975 (n=1981)
- (11, 3, 6): -18,175 (n=485)
- (11, 4, 6): -19,867 (n=493)
- (17, 3, 6): -20,013 (n=58)
- (8, 4, 6): -21,051 (n=659)
- (13, 4, 6): -21,868 (n=180)
- (8, 3, 4): -22,126 (n=72)
- (13, 3, 6): -22,174 (n=261)
- (10, 3, 5): -22,188 (n=57)

_Generated 2026-09-09 01:08. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 4797 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=4797); harvest_min=1–3 (n=4797); wheat_tiles=0–8 (n=4797); wheat_stock=0–40 (n=4797); min_hands=3–6 (n=4797); load_per_hand=12–26 (n=4797); geese=0–2 (n=4797); open_melons=4–14 (n=4797)
- **Evidence:** 4797 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 61 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=61); harvest_min=1–3 (n=61); wheat_tiles=0–2 (n=61); wheat_stock=0–4 (n=61); min_hands=3–6 (n=61); load_per_hand=15–21 (n=61); geese=0–2 (n=61); open_melons=7–13 (n=61)
- **Evidence:** 61 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 33 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=33); harvest_min=1–3 (n=33); wheat_tiles=0; wheat_stock=0–39 (n=33); min_hands=3–6 (n=33); load_per_hand=12–26 (n=33); geese=0–1 (n=33); open_melons=4–13 (n=33)
- **Evidence:** 33 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 21 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=21); harvest_min=1–3 (n=21); wheat_tiles=0–8 (n=21); wheat_stock=0–39 (n=21); min_hands=3–6 (n=21); load_per_hand=12–23 (n=21); geese=0–2 (n=21); open_melons=8–14 (n=21)
- **Evidence:** 21 candidates, multiple seeds. Confidence: high

### None (observed in 12 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=12); harvest_min=1–3 (n=12); wheat_tiles=0; wheat_stock=0–11 (n=12); min_hands=3–6 (n=12); load_per_hand=12–18 (n=12); geese=0–2 (n=12); open_melons=7–14 (n=12)
- **Evidence:** 12 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-09 01:08. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._