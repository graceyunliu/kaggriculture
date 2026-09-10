# Evolution run 20260909-194943

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1361 · games 22,172 (11,082/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 524 | 1048 |
| dead_pattern | 242 | 484 |
| dead_smoke | 198 | 1584 |
| alive | 397 | 19056 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 18195 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2380
- M2: best -16,102 (`8b77b3e994bc`), n=2466
- c1: best -16,310 (`23734cef4da1`), n=3225
- queue: best -15,412 (`fe4745b56024`), n=4282
- v312: best -15,275 (`52b3d5cc236e`), n=2969
- wide: best -16,047 (`512e53fe15bc`), n=2873

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 147 | 18185 | 65.78 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 5: -28,735 (n=56), 143: -28,964 (n=3), 27: -29,419 (n=39), 26: -29,468 (n=9), 112: -29,479 (n=14), 8: -29,645 (n=7), 19: -30,031 (n=19), 110: -30,105 (n=5), 89: -30,144 (n=31), 106: -30,222 (n=41), 18: -30,360 (n=1227), 97: -30,398 (n=43), 92: -30,490 (n=495), 74: -30,510 (n=403), 63: -30,541 (n=311), 56: -30,589 (n=23), 58: -30,637 (n=147), 70: -30,648 (n=71), 71: -30,666 (n=30), 35: -30,680 (n=18), 48: -30,689 (n=565), 108: -30,721 (n=8), 150: -30,747 (n=278), 80: -30,783 (n=17), 49: -30,791 (n=94), 65: -30,792 (n=163), 72: -30,839 (n=13), 50: -30,928 (n=8864), 60: -30,958 (n=36), 30: -31,099 (n=59), 44: -31,108 (n=48), 14: -31,145 (n=33), 40: -31,312 (n=113), 61: -31,389 (n=123), 144: -31,452 (n=10), 86: -31,454 (n=10), 42: -31,486 (n=922), 66: -31,487 (n=352), 94: -31,527 (n=22), 51: -31,529 (n=22), 85: -31,546 (n=13), 36: -31,626 (n=149), 53: -31,675 (n=93), 73: -31,689 (n=22), 38: -31,706 (n=24), 104: -31,742 (n=6), 45: -31,852 (n=126), 57: -31,994 (n=88), 9: -32,055 (n=20), 25: -32,083 (n=10), 59: -32,226 (n=25), 113: -32,418 (n=15), 17: -32,418 (n=11), 84: -32,503 (n=17), 115: -32,512 (n=8), 39: -32,533 (n=61), 96: -32,630 (n=8), 33: -32,644 (n=26), 54: -32,651 (n=28), 55: -32,652 (n=729), 41: -32,727 (n=57), 62: -32,741 (n=24), 87: -32,742 (n=19), 109: -32,944 (n=4), 52: -32,951 (n=23), 125: -33,009 (n=2), 4: -33,017 (n=39), 103: -33,035 (n=10), 88: -33,112 (n=12), 98: -33,151 (n=21), 0: -33,181 (n=236), 68: -33,247 (n=19), 93: -33,297 (n=10), 78: -33,339 (n=17), 21: -33,400 (n=13), 2: -33,419 (n=4), 95: -33,449 (n=5), 69: -33,518 (n=31), 28: -33,526 (n=21), 31: -33,560 (n=19), 24: -33,583 (n=24), 83: -33,599 (n=114), 76: -33,609 (n=19), 22: -33,631 (n=18), 43: -33,631 (n=22), 1: -33,664 (n=8), 102: -33,689 (n=6), 81: -33,694 (n=29), 119: -33,699 (n=3), 6: -33,709 (n=13), 13: -33,976 (n=8), 64: -34,024 (n=25), 90: -34,046 (n=8), 111: -34,111 (n=8), 47: -34,167 (n=33), 82: -34,211 (n=50), 20: -34,227 (n=10), 99: -34,375 (n=76), 15: -34,394 (n=12), 10: -34,451 (n=15), 140: -34,453 (n=4), 134: -34,464 (n=2), 37: -34,547 (n=15), 46: -34,592 (n=40), 79: -34,624 (n=23), 11: -34,632 (n=18), 101: -34,712 (n=13), 12: -34,899 (n=15), 7: -34,904 (n=9), 107: -35,073 (n=7), 3: -35,105 (n=7), 77: -35,242 (n=242), 34: -35,375 (n=74), 136: -35,375 (n=52), 16: -35,385 (n=19), 32: -35,436 (n=12), 100: -35,484 (n=57), 91: -35,887 (n=10), 129: -36,013 (n=89), 23: -36,202 (n=20), 75: -36,461 (n=15), 67: -36,486 (n=20), 128: -36,508 (n=3), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,554 (n=60), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,901 | 26 | 30 | 25 | 18195 | 11.21 | 26: -30,852 (n=649), 25: -30,863 (n=8884), 30: -31,085 (n=5942), 31: -31,601 (n=146), 29: -31,927 (n=151), 27: -32,368 (n=270), 28: -33,472 (n=1396), 32: -33,949 (n=177), 41: -34,307 (n=3), 35: -34,985 (n=196), 45: -35,319 (n=2), 33: -35,541 (n=146), 34: -35,815 (n=74), 37: -35,822 (n=29), 39: -36,046 (n=13), 38: -36,219 (n=25), 36: -36,806 (n=43), 42: -36,946 (n=4), 46: -38,521 (n=3), 43: -38,819 (n=7), 40: -39,082 (n=16), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,586 (n=9), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,320 | 1 | 0 | 35 | 18191 | 24.49 | 1: -30,206 (n=1597), 9: -30,918 (n=109), 0: -31,149 (n=14957), 22: -31,572 (n=3), 2: -32,605 (n=202), 6: -33,009 (n=136), 8: -33,118 (n=91), 4: -33,291 (n=128), 3: -34,404 (n=210), 19: -34,452 (n=9), 11: -34,840 (n=74), 17: -34,944 (n=17), 5: -35,258 (n=193), 20: -35,341 (n=7), 13: -35,395 (n=54), 7: -35,397 (n=112), 28: -35,676 (n=3), 12: -35,732 (n=36), 16: -36,073 (n=18), 14: -36,160 (n=27), 15: -36,357 (n=36), 23: -36,978 (n=7), 18: -36,999 (n=24), 10: -37,017 (n=58), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,635 (n=13), 26: -40,268 (n=3), 29: -40,719 (n=37), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,886 | 3 | 3 | 4 | 18195 | 2.61 | 3: -30,862 (n=16421), 2: -35,722 (n=1267), 4: -36,352 (n=486), 5: -42,748 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,528 | 61 | 100 | 101 | 18195 | 62.21 | 61: -27,918 (n=2), 80: -29,833 (n=390), 130: -29,880 (n=14), 138: -30,059 (n=5), 93: -30,131 (n=439), 120: -30,212 (n=21), 81: -30,251 (n=91), 85: -30,517 (n=101), 86: -30,546 (n=983), 62: -30,676 (n=9), 91: -30,774 (n=105), 100: -30,947 (n=11388), 90: -30,993 (n=172), 50: -31,005 (n=175), 123: -31,076 (n=56), 78: -31,095 (n=163), 66: -31,131 (n=18), 125: -31,190 (n=95), 111: -31,285 (n=45), 92: -31,397 (n=31), 65: -31,427 (n=7), 107: -31,427 (n=29), 115: -31,483 (n=36), 94: -31,491 (n=37), 129: -31,500 (n=21), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,619 (n=123), 117: -31,656 (n=125), 99: -31,689 (n=45), 133: -31,740 (n=10), 84: -31,854 (n=92), 103: -31,860 (n=32), 113: -31,873 (n=25), 119: -31,933 (n=22), 87: -31,948 (n=25), 95: -32,108 (n=44), 70: -32,188 (n=20), 71: -32,191 (n=22), 132: -32,285 (n=12), 53: -32,306 (n=5), 102: -32,311 (n=45), 63: -32,321 (n=11), 114: -32,336 (n=31), 149: -32,426 (n=4), 88: -32,448 (n=77), 104: -32,458 (n=650), 105: -32,470 (n=132), 127: -32,523 (n=36), 82: -32,585 (n=23), 109: -32,589 (n=49), 128: -32,619 (n=33), 59: -32,721 (n=5), 67: -32,782 (n=11), 110: -32,812 (n=30), 98: -32,817 (n=66), 69: -32,894 (n=13), 76: -33,090 (n=21), 112: -33,190 (n=223), 97: -33,298 (n=60), 57: -33,366 (n=7), 122: -33,424 (n=41), 68: -33,466 (n=12), 141: -33,486 (n=4), 89: -33,490 (n=178), 101: -33,500 (n=47), 134: -33,531 (n=8), 116: -33,536 (n=80), 126: -33,677 (n=28), 135: -33,750 (n=503), 55: -33,777 (n=5), 96: -33,961 (n=49), 108: -33,977 (n=31), 136: -34,218 (n=7), 74: -34,234 (n=37), 72: -34,325 (n=14), 124: -34,455 (n=28), 75: -34,520 (n=60), 143: -34,578 (n=12), 79: -34,613 (n=62), 106: -34,783 (n=48), 121: -34,908 (n=18), 137: -35,119 (n=6), 144: -35,500 (n=3), 131: -35,641 (n=18), 150: -35,782 (n=182), 56: -35,940 (n=6), 52: -36,201 (n=4), 139: -36,227 (n=9), 142: -36,242 (n=8), 118: -36,871 (n=16), 73: -37,385 (n=15), 77: -37,410 (n=29), 148: -37,549 (n=4), 58: -37,611 (n=6), 146: -37,838 (n=2), 140: -38,416 (n=3), 54: -38,470 (n=4), 51: -38,935 (n=5), 145: -39,395 (n=13), 60: -39,446 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,302 | 6 | 6 | 8 | 18195 | 6.13 | 6: -30,766 (n=16217), 5: -34,704 (n=809), 7: -36,551 (n=442), 4: -37,531 (n=472), 3: -37,667 (n=151), 8: -38,033 (n=70), 9: -40,277 (n=26), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,299 | 13 | 20 | 11 | 18195 | 4.64 | 13: -30,728 (n=44), 17: -31,017 (n=6159), 16: -31,034 (n=391), 19: -31,313 (n=986), 18: -31,423 (n=939), 14: -31,507 (n=144), 20: -31,575 (n=9336), 15: -32,079 (n=164), 11: -32,310 (n=3), 12: -33,505 (n=21), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,147 | 10 | 8 | 11 | 18195 | 8.35 | 10: -30,768 (n=15466), 7: -32,431 (n=599), 8: -34,734 (n=1047), 9: -35,172 (n=626), 6: -35,276 (n=193), 5: -35,645 (n=30), 12: -37,855 (n=54), 11: -38,000 (n=80), 4: -38,304 (n=26), 14: -39,848 (n=32), 13: -40,915 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,143 | 7 | 7 | 8 | 18195 | 6.13 | 7: -30,720 (n=16217), 6: -36,368 (n=954), 5: -36,415 (n=79), 8: -36,642 (n=613), 10: -36,736 (n=130), 9: -37,355 (n=122), 4: -37,826 (n=71), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,664 | 20 | 20 | 15 | 18195 | 7.79 | 20: -30,669 (n=10661), 19: -30,918 (n=5153), 18: -31,530 (n=425), 17: -34,321 (n=751), 16: -36,343 (n=171), 21: -36,667 (n=386), 15: -37,298 (n=86), 23: -37,704 (n=108), 22: -37,861 (n=204), 26: -38,575 (n=46), 14: -38,583 (n=42), 13: -39,249 (n=19), 24: -39,298 (n=96), 25: -39,454 (n=24), 12: -40,333 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,562 | 0.0 | 0.0 | 13 | 18195 | 10.36 | 0.0: -31,021 (n=15894), 0.1: -33,125 (n=1111), 0.2: -33,772 (n=665), 0.4: -33,856 (n=106), 0.3: -34,083 (n=222), 0.5: -34,544 (n=63), 1.1: -34,978 (n=7), 0.7: -35,518 (n=19), 0.6: -36,854 (n=60), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -39,081 (n=9), 0.8: -40,582 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,331 | 0.55 | 0.5 | 15 | 18195 | 7.61 | 0.55: -30,410 (n=10449), 0.5: -31,762 (n=4232), 0.65: -31,762 (n=1313), 0.75: -32,206 (n=133), 0.7: -32,431 (n=311), 0.6: -33,313 (n=443), 0.45: -34,690 (n=540), 0.8: -34,777 (n=65), 0.9: -35,790 (n=13), 0.35: -35,958 (n=177), 0.4: -36,102 (n=210), 0.85: -36,532 (n=16), 0.95: -36,836 (n=4), 1.0: -38,525 (n=8), 0.3: -39,741 (n=281) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +8,875 | 0 | 0 | 9 | 18195 | 7.17 | 0: -31,057 (n=16527), 1: -34,000 (n=865), 2: -34,278 (n=365), 3: -34,855 (n=275), 7: -35,103 (n=7), 4: -35,104 (n=101), 5: -35,503 (n=24), 6: -37,768 (n=27), 8: -39,932 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,582 | 14 | 13 | 9 | 18195 | 4.26 | 14: -30,961 (n=3171), 11: -31,184 (n=857), 13: -31,335 (n=10639), 12: -31,426 (n=2405), 15: -31,629 (n=571), 10: -32,931 (n=146), 16: -33,361 (n=323), 9: -36,758 (n=61), 8: -39,543 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,518 | 2 | 2 | 4 | 18195 | 2.84 | 2: -31,100 (n=17446), 1: -37,052 (n=614), 3: -38,514 (n=47), 0: -39,618 (n=88) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,194 | 13 | 12 | 11 | 18195 | 8.25 | 13: -30,826 (n=1506), 14: -31,242 (n=15307), 11: -32,356 (n=244), 12: -32,527 (n=756), 9: -33,432 (n=33), 6: -34,388 (n=4), 7: -34,770 (n=11), 10: -35,311 (n=293), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,527 | frontier | frontier | 2 | 18195 | 0.91 | frontier: -31,038 (n=17415), v312: -38,565 (n=780) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 18195 | 9.52 | 6: -30,481 (n=23), 21: -30,783 (n=3342), 22: -30,881 (n=9117), 23: -31,332 (n=810), 14: -31,338 (n=27), 20: -31,367 (n=723), 16: -31,877 (n=116), 17: -32,370 (n=863), 25: -32,571 (n=1436), 18: -32,913 (n=676), 24: -33,143 (n=466), 13: -33,252 (n=31), 15: -33,303 (n=60), 19: -33,374 (n=230), 12: -33,945 (n=13), 9: -34,193 (n=54), 10: -34,840 (n=70), 11: -36,391 (n=38), 7: -36,543 (n=22), 5: -36,694 (n=72), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,285 | 2 | 2 | 3 | 18195 | 1.83 | 2: -30,980 (n=17158), 1: -37,615 (n=970), 3: -38,265 (n=67) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,733 | 34 | 40 | 31 | 18195 | 7.72 | 34: -30,258 (n=337), 21: -30,358 (n=2), 49: -30,677 (n=486), 38: -30,717 (n=4260), 43: -30,731 (n=5117), 33: -30,758 (n=69), 44: -30,760 (n=531), 47: -30,968 (n=326), 45: -31,211 (n=794), 30: -31,213 (n=77), 27: -31,404 (n=12), 37: -31,443 (n=708), 39: -31,519 (n=670), 26: -31,940 (n=67), 28: -32,046 (n=21), 25: -32,256 (n=9), 50: -32,451 (n=494), 32: -32,459 (n=68), 40: -32,761 (n=2922), 42: -32,929 (n=241), 35: -33,009 (n=252), 29: -33,024 (n=18), 31: -33,049 (n=48), 41: -33,066 (n=146), 36: -33,117 (n=212), 46: -33,171 (n=133), 48: -34,182 (n=79), 20: -34,580 (n=56), 23: -35,631 (n=7), 24: -36,135 (n=26), 22: -36,991 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3374)
- (9, 3, 6): -16,461 (n=2367)
- (12, 4, 6): -16,525 (n=555)
- (10, 3, 6): -16,840 (n=2974)
- (8, 3, 5): -16,866 (n=314)
- (8, 3, 6): -17,552 (n=870)
- (10, 4, 6): -17,975 (n=2642)
- (11, 3, 6): -18,175 (n=635)
- (11, 4, 6): -19,867 (n=609)
- (17, 3, 6): -20,013 (n=69)
- (8, 4, 6): -21,051 (n=826)
- (13, 4, 6): -21,564 (n=234)
- (14, 3, 6): -21,679 (n=263)
- (13, 3, 6): -21,783 (n=352)
- (8, 3, 4): -22,126 (n=93)

_Generated 2026-09-09 21:49. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 8583 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=8583); harvest_min=1–3 (n=8583); wheat_tiles=0–8 (n=8583); wheat_stock=0–40 (n=8583); min_hands=3–6 (n=8583); load_per_hand=12–26 (n=8583); geese=0–2 (n=8583); open_melons=4–14 (n=8583)
- **Evidence:** 8583 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 107 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=107); harvest_min=1–3 (n=107); wheat_tiles=0–2 (n=107); wheat_stock=0–6 (n=107); min_hands=3–6 (n=107); load_per_hand=15–23 (n=107); geese=0–2 (n=107); open_melons=7–13 (n=107)
- **Evidence:** 107 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 56 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=56); harvest_min=1–3 (n=56); wheat_tiles=0–3 (n=56); wheat_stock=0–39 (n=56); min_hands=3–6 (n=56); load_per_hand=12–26 (n=56); geese=0–2 (n=56); open_melons=4–13 (n=56)
- **Evidence:** 56 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 42 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=42); harvest_min=1–3 (n=42); wheat_tiles=0–8 (n=42); wheat_stock=0–39 (n=42); min_hands=3–6 (n=42); load_per_hand=12–23 (n=42); geese=0–2 (n=42); open_melons=6–14 (n=42)
- **Evidence:** 42 candidates, multiple seeds. Confidence: high

### None (observed in 21 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=21); harvest_min=1–3 (n=21); wheat_tiles=0; wheat_stock=0–11 (n=21); min_hands=3–6 (n=21); load_per_hand=12–18 (n=21); geese=0–2 (n=21); open_melons=7–14 (n=21)
- **Evidence:** 21 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 21:49. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._