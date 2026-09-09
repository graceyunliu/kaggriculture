# Evolution run 20260909-031651

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1321 · games 23,262 (11,627/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 481 | 962 |
| dead_pattern | 230 | 460 |
| dead_smoke | 186 | 1488 |
| alive | 424 | 20352 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 14842 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=1850
- M2: best -16,461 (`0c25e1226b27`), n=1916
- c1: best -16,310 (`23734cef4da1`), n=2655
- queue: best -15,412 (`fe4745b56024`), n=3603
- v312: best -15,275 (`52b3d5cc236e`), n=2491
- wide: best -16,047 (`512e53fe15bc`), n=2327

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +20,931 | 120 | 50 | 144 | 14833 | 65.55 | 120: -20,837 (n=6), 118: -25,349 (n=2), 143: -26,636 (n=2), 8: -27,592 (n=3), 19: -27,891 (n=15), 141: -28,023 (n=6), 5: -28,817 (n=52), 112: -29,479 (n=14), 27: -29,531 (n=36), 89: -29,645 (n=29), 35: -29,650 (n=12), 108: -29,670 (n=7), 26: -29,760 (n=7), 58: -29,870 (n=115), 92: -29,986 (n=383), 18: -30,096 (n=904), 80: -30,197 (n=15), 74: -30,372 (n=259), 63: -30,382 (n=242), 49: -30,513 (n=81), 71: -30,611 (n=29), 48: -30,636 (n=533), 61: -30,735 (n=102), 51: -30,780 (n=17), 56: -30,810 (n=16), 50: -30,815 (n=7312), 65: -30,834 (n=140), 106: -30,877 (n=18), 150: -30,962 (n=193), 86: -31,018 (n=9), 72: -31,109 (n=10), 70: -31,184 (n=48), 42: -31,320 (n=806), 66: -31,329 (n=266), 97: -31,347 (n=29), 40: -31,414 (n=101), 60: -31,435 (n=30), 85: -31,513 (n=11), 33: -31,521 (n=22), 45: -31,616 (n=116), 25: -31,648 (n=9), 9: -31,659 (n=17), 2: -31,685 (n=2), 73: -31,693 (n=18), 96: -31,865 (n=7), 57: -31,948 (n=84), 113: -32,112 (n=13), 36: -32,136 (n=118), 144: -32,144 (n=4), 14: -32,158 (n=22), 110: -32,277 (n=4), 39: -32,284 (n=56), 103: -32,462 (n=9), 30: -32,495 (n=30), 115: -32,512 (n=8), 54: -32,587 (n=25), 62: -32,601 (n=18), 84: -32,611 (n=14), 59: -32,680 (n=21), 38: -32,687 (n=18), 94: -32,712 (n=20), 41: -32,774 (n=43), 109: -32,844 (n=3), 98: -32,926 (n=20), 69: -32,929 (n=24), 55: -32,940 (n=597), 93: -32,999 (n=9), 53: -33,009 (n=46), 4: -33,088 (n=38), 52: -33,102 (n=19), 21: -33,189 (n=10), 104: -33,266 (n=4), 31: -33,271 (n=15), 6: -33,331 (n=10), 76: -33,355 (n=15), 0: -33,419 (n=210), 95: -33,449 (n=5), 81: -33,458 (n=26), 83: -33,462 (n=107), 13: -33,499 (n=7), 43: -33,575 (n=20), 1: -33,664 (n=8), 119: -33,699 (n=3), 28: -33,719 (n=20), 68: -33,803 (n=17), 24: -33,814 (n=20), 90: -33,822 (n=7), 88: -33,874 (n=11), 22: -33,894 (n=17), 32: -33,992 (n=9), 20: -34,103 (n=7), 111: -34,111 (n=8), 102: -34,126 (n=5), 17: -34,184 (n=7), 10: -34,204 (n=14), 99: -34,244 (n=72), 82: -34,251 (n=45), 78: -34,276 (n=13), 44: -34,396 (n=21), 140: -34,453 (n=4), 134: -34,464 (n=2), 15: -34,489 (n=10), 7: -34,621 (n=7), 136: -34,658 (n=42), 37: -34,726 (n=12), 16: -34,787 (n=16), 46: -34,818 (n=35), 64: -34,931 (n=21), 107: -34,965 (n=5), 11: -35,182 (n=14), 77: -35,190 (n=232), 79: -35,212 (n=15), 101: -35,278 (n=11), 87: -35,325 (n=12), 34: -35,371 (n=62), 47: -35,513 (n=22), 100: -35,517 (n=50), 129: -35,839 (n=81), 91: -35,887 (n=10), 23: -36,214 (n=13), 128: -36,508 (n=3), 3: -36,531 (n=5), 105: -36,563 (n=3), 117: -36,604 (n=2), 12: -36,634 (n=11), 145: -36,990 (n=7), 67: -37,049 (n=18), 75: -37,231 (n=10), 114: -37,341 (n=4), 127: -38,268 (n=2), 29: -38,272 (n=36), 131: -38,847 (n=2), 132: -39,931 (n=2), 124: -39,994 (n=3), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +13,194 | 26 | 30 | 25 | 14841 | 10.64 | 26: -30,558 (n=503), 25: -30,783 (n=7199), 30: -30,981 (n=4813), 31: -31,524 (n=129), 27: -32,350 (n=231), 29: -32,380 (n=122), 28: -33,525 (n=1202), 32: -34,139 (n=142), 41: -34,307 (n=3), 35: -34,777 (n=177), 33: -35,524 (n=122), 39: -35,574 (n=12), 37: -35,771 (n=26), 38: -35,824 (n=21), 34: -36,054 (n=61), 42: -36,946 (n=4), 36: -37,464 (n=36), 46: -38,521 (n=3), 40: -39,180 (n=12), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -41,174 (n=5), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,238 | 1 | 0 | 34 | 14839 | 25.12 | 1: -30,288 (n=1023), 0: -31,069 (n=12501), 9: -31,108 (n=97), 22: -31,539 (n=2), 2: -32,353 (n=150), 4: -33,017 (n=95), 6: -33,073 (n=101), 8: -33,276 (n=82), 19: -34,158 (n=6), 3: -34,336 (n=176), 17: -34,402 (n=14), 5: -34,721 (n=153), 11: -34,776 (n=66), 7: -35,585 (n=86), 16: -35,592 (n=13), 13: -35,812 (n=45), 12: -35,841 (n=33), 14: -36,151 (n=22), 20: -36,357 (n=6), 28: -36,361 (n=2), 15: -36,705 (n=27), 18: -36,728 (n=20), 23: -36,978 (n=7), 24: -37,048 (n=7), 10: -37,219 (n=45), 39: -37,389 (n=10), 21: -37,766 (n=7), 40: -39,508 (n=8), 26: -40,268 (n=3), 29: -41,294 (n=28), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,838 | 3 | 3 | 4 | 14842 | 2.61 | 3: -30,790 (n=13398), 2: -35,834 (n=1024), 4: -36,500 (n=400), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 14842 | 62.85 | 61: -27,918 (n=2), 138: -27,990 (n=3), 130: -29,311 (n=13), 80: -29,764 (n=223), 120: -29,850 (n=16), 85: -30,074 (n=93), 93: -30,083 (n=382), 65: -30,157 (n=6), 81: -30,271 (n=81), 91: -30,471 (n=89), 62: -30,511 (n=7), 86: -30,559 (n=721), 114: -30,605 (n=24), 100: -30,788 (n=9383), 113: -30,885 (n=18), 115: -30,929 (n=33), 64: -30,996 (n=12), 123: -31,024 (n=46), 125: -31,090 (n=92), 94: -31,179 (n=33), 133: -31,210 (n=9), 129: -31,219 (n=18), 111: -31,233 (n=39), 78: -31,376 (n=100), 63: -31,414 (n=10), 55: -31,425 (n=4), 141: -31,447 (n=3), 107: -31,458 (n=26), 92: -31,528 (n=25), 90: -31,554 (n=100), 147: -31,607 (n=7), 67: -31,660 (n=9), 83: -31,680 (n=113), 117: -31,717 (n=99), 69: -31,788 (n=9), 84: -31,858 (n=74), 99: -31,903 (n=35), 103: -31,936 (n=28), 57: -31,969 (n=5), 87: -31,970 (n=20), 132: -31,971 (n=11), 95: -32,077 (n=39), 105: -32,084 (n=108), 109: -32,096 (n=34), 70: -32,127 (n=19), 102: -32,153 (n=43), 149: -32,176 (n=3), 53: -32,281 (n=4), 66: -32,339 (n=13), 71: -32,513 (n=20), 82: -32,550 (n=22), 128: -32,572 (n=25), 119: -32,612 (n=15), 104: -32,613 (n=564), 110: -32,680 (n=25), 127: -32,908 (n=31), 88: -33,015 (n=66), 122: -33,107 (n=37), 76: -33,119 (n=19), 97: -33,188 (n=54), 112: -33,194 (n=203), 101: -33,357 (n=37), 98: -33,434 (n=43), 68: -33,455 (n=11), 134: -33,531 (n=8), 89: -33,649 (n=157), 135: -33,759 (n=455), 96: -33,780 (n=41), 116: -33,883 (n=66), 59: -33,898 (n=4), 126: -33,966 (n=25), 143: -34,012 (n=11), 74: -34,126 (n=33), 121: -34,194 (n=13), 136: -34,218 (n=7), 50: -34,251 (n=57), 79: -34,426 (n=45), 124: -34,451 (n=23), 75: -34,489 (n=59), 108: -34,512 (n=27), 137: -34,596 (n=5), 144: -34,772 (n=2), 106: -34,924 (n=43), 56: -35,056 (n=5), 150: -35,711 (n=170), 131: -35,872 (n=13), 72: -36,061 (n=11), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 148: -36,528 (n=3), 118: -36,824 (n=14), 77: -37,246 (n=21), 51: -37,500 (n=2), 58: -37,611 (n=6), 73: -37,735 (n=11), 146: -37,838 (n=2), 140: -38,416 (n=3), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +11,510 | 0.0 | 0.0 | 13 | 14842 | 10.26 | 0.0: -30,934 (n=12858), 0.1: -33,075 (n=970), 0.2: -33,783 (n=585), 0.4: -34,128 (n=90), 0.3: -34,267 (n=175), 1.1: -34,978 (n=7), 0.5: -35,074 (n=52), 0.7: -36,163 (n=16), 0.6: -37,020 (n=45), 0.9: -37,347 (n=5), 1.0: -37,756 (n=24), 1.2: -39,081 (n=9), 0.8: -42,444 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,535 | 13 | 20 | 11 | 14842 | 4.85 | 13: -30,492 (n=37), 17: -30,913 (n=4847), 16: -30,931 (n=335), 19: -31,224 (n=746), 14: -31,265 (n=120), 18: -31,443 (n=715), 20: -31,536 (n=7892), 15: -32,278 (n=124), 11: -32,310 (n=3), 12: -34,282 (n=15), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,360 | 20 | 20 | 15 | 14842 | 7.49 | 20: -30,553 (n=8399), 19: -30,941 (n=4456), 18: -31,535 (n=342), 17: -34,311 (n=689), 21: -36,512 (n=308), 16: -36,530 (n=138), 15: -37,330 (n=68), 23: -37,517 (n=76), 22: -37,789 (n=158), 14: -38,304 (n=35), 26: -38,538 (n=39), 24: -38,950 (n=77), 25: -39,340 (n=21), 13: -39,593 (n=18), 12: -40,913 (n=18) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +10,352 | 6 | 6 | 8 | 14842 | 6.13 | 6: -30,715 (n=13230), 5: -34,643 (n=653), 7: -36,465 (n=380), 4: -37,393 (n=370), 3: -37,788 (n=125), 8: -38,179 (n=58), 9: -40,761 (n=19), 10: -41,067 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,105 | 7 | 7 | 8 | 14842 | 6.11 | 7: -30,645 (n=13193), 6: -36,438 (n=837), 5: -36,485 (n=68), 8: -36,560 (n=481), 10: -36,812 (n=115), 9: -37,183 (n=96), 4: -38,060 (n=44), 3: -40,750 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,090 | 10 | 8 | 11 | 14842 | 8.3 | 10: -30,672 (n=12546), 7: -32,523 (n=452), 8: -34,732 (n=918), 9: -35,009 (n=535), 6: -35,476 (n=172), 5: -36,602 (n=24), 12: -37,659 (n=46), 4: -38,193 (n=23), 11: -38,454 (n=65), 14: -39,776 (n=29), 13: -40,762 (n=32) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,681 | 0 | 0 | 9 | 14842 | 7.15 | 0: -30,977 (n=13448), 1: -34,084 (n=730), 2: -34,549 (n=300), 3: -34,859 (n=229), 7: -35,103 (n=7), 4: -35,604 (n=81), 5: -35,723 (n=21), 6: -37,601 (n=23), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,674 | 0.55 | 0.5 | 15 | 14842 | 7.25 | 0.55: -30,247 (n=8161), 0.65: -31,731 (n=1187), 0.5: -31,805 (n=3700), 0.75: -31,927 (n=104), 0.7: -32,262 (n=246), 0.6: -33,173 (n=359), 0.8: -34,368 (n=50), 0.45: -34,637 (n=454), 0.9: -35,286 (n=10), 0.35: -35,955 (n=151), 0.4: -36,171 (n=165), 0.85: -37,161 (n=14), 0.95: -37,209 (n=3), 1.0: -38,830 (n=7), 0.3: -39,921 (n=231) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,979 | 14 | 13 | 9 | 14842 | 4.34 | 14: -30,773 (n=2357), 11: -31,240 (n=763), 13: -31,280 (n=8803), 12: -31,396 (n=2033), 15: -31,670 (n=454), 16: -33,481 (n=251), 10: -33,486 (n=118), 9: -37,129 (n=44), 8: -39,752 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +8,647 | 6 | 18 | 21 | 14842 | 9.34 | 6: -29,983 (n=18), 21: -30,572 (n=2618), 14: -30,694 (n=21), 22: -30,816 (n=7308), 20: -31,267 (n=656), 23: -31,288 (n=673), 16: -32,363 (n=88), 17: -32,447 (n=739), 25: -32,464 (n=1214), 18: -32,918 (n=589), 24: -33,192 (n=410), 15: -33,275 (n=50), 12: -33,342 (n=11), 19: -33,516 (n=190), 13: -33,925 (n=25), 9: -33,993 (n=50), 10: -34,716 (n=67), 11: -36,049 (n=34), 5: -36,140 (n=54), 7: -36,543 (n=22), 8: -38,629 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,550 | 2 | 2 | 4 | 14842 | 2.84 | 2: -31,058 (n=14255), 1: -36,953 (n=475), 3: -38,375 (n=41), 0: -39,608 (n=71) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,178 | 13 | 12 | 11 | 14841 | 7.44 | 13: -30,842 (n=1136), 14: -31,145 (n=12533), 11: -32,606 (n=208), 12: -32,772 (n=632), 6: -34,388 (n=4), 9: -34,839 (n=28), 10: -35,257 (n=254), 7: -35,686 (n=10), 8: -37,181 (n=33), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,632 | frontier | frontier | 2 | 14842 | 0.92 | frontier: -30,989 (n=14222), v312: -38,621 (n=620) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,537 | 2 | 2 | 3 | 14842 | 1.82 | 2: -30,914 (n=13968), 1: -37,551 (n=821), 3: -38,451 (n=53) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +7,302 | 34 | 40 | 30 | 14842 | 7.49 | 34: -30,285 (n=265), 38: -30,397 (n=3272), 43: -30,615 (n=4198), 49: -30,615 (n=428), 27: -30,617 (n=11), 33: -30,877 (n=55), 44: -30,964 (n=398), 47: -30,996 (n=254), 30: -31,104 (n=65), 37: -31,189 (n=542), 45: -31,378 (n=586), 39: -31,474 (n=523), 28: -31,842 (n=15), 32: -31,859 (n=60), 26: -32,036 (n=50), 46: -32,680 (n=99), 40: -32,764 (n=2700), 29: -32,779 (n=17), 35: -32,784 (n=224), 42: -32,980 (n=216), 41: -32,987 (n=105), 50: -33,001 (n=379), 31: -33,011 (n=41), 25: -33,175 (n=7), 36: -33,177 (n=184), 48: -34,677 (n=70), 20: -34,713 (n=43), 24: -35,776 (n=24), 23: -36,212 (n=6), 22: -37,587 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=2778)
- (9, 3, 6): -16,578 (n=1865)
- (10, 3, 6): -16,840 (n=2415)
- (8, 3, 5): -16,866 (n=264)
- (12, 4, 6): -17,058 (n=475)
- (8, 3, 6): -17,552 (n=747)
- (10, 4, 6): -17,975 (n=2133)
- (11, 3, 6): -18,175 (n=508)
- (11, 4, 6): -19,867 (n=519)
- (17, 3, 6): -20,013 (n=63)
- (8, 4, 6): -21,051 (n=695)
- (13, 3, 6): -21,783 (n=281)
- (13, 4, 6): -21,868 (n=193)
- (8, 3, 4): -22,126 (n=75)
- (10, 3, 5): -22,188 (n=60)

_Generated 2026-09-09 05:16. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 5595 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=5595); harvest_min=1–3 (n=5595); wheat_tiles=0–8 (n=5595); wheat_stock=0–40 (n=5595); min_hands=3–6 (n=5595); load_per_hand=12–26 (n=5595); geese=0–2 (n=5595); open_melons=4–14 (n=5595)
- **Evidence:** 5595 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 69 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=69); harvest_min=1–3 (n=69); wheat_tiles=0–2 (n=69); wheat_stock=0–4 (n=69); min_hands=3–6 (n=69); load_per_hand=15–22 (n=69); geese=0–2 (n=69); open_melons=7–13 (n=69)
- **Evidence:** 69 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 39 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=39); harvest_min=1–3 (n=39); wheat_tiles=0; wheat_stock=0–39 (n=39); min_hands=3–6 (n=39); load_per_hand=12–26 (n=39); geese=0–1 (n=39); open_melons=4–13 (n=39)
- **Evidence:** 39 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 25 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=25); harvest_min=1–3 (n=25); wheat_tiles=0–8 (n=25); wheat_stock=0–39 (n=25); min_hands=3–6 (n=25); load_per_hand=12–23 (n=25); geese=0–2 (n=25); open_melons=8–14 (n=25)
- **Evidence:** 25 candidates, multiple seeds. Confidence: high

### None (observed in 12 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=12); harvest_min=1–3 (n=12); wheat_tiles=0; wheat_stock=0–11 (n=12); min_hands=3–6 (n=12); load_per_hand=12–18 (n=12); geese=0–2 (n=12); open_melons=7–14 (n=12)
- **Evidence:** 12 candidates, multiple seeds. Confidence: moderate

_Generated 2026-09-09 05:16. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._