# Evolution run 20260909-154429

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1267 · games 22,686 (11,341/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 475 | 950 |
| dead_pattern | 220 | 440 |
| dead_smoke | 154 | 1232 |
| alive | 418 | 20064 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 17385 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2246
- M2: best -16,102 (`8b77b3e994bc`), n=2322
- c1: best -16,310 (`23734cef4da1`), n=3104
- queue: best -15,412 (`fe4745b56024`), n=4113
- v312: best -15,275 (`52b3d5cc236e`), n=2863
- wide: best -16,047 (`512e53fe15bc`), n=2737

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 147 | 17375 | 65.9 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 5: -28,740 (n=53), 143: -28,964 (n=3), 27: -29,422 (n=38), 112: -29,479 (n=14), 8: -29,645 (n=7), 106: -29,819 (n=37), 19: -30,031 (n=19), 110: -30,105 (n=5), 89: -30,144 (n=31), 18: -30,218 (n=1154), 80: -30,353 (n=16), 74: -30,383 (n=365), 92: -30,416 (n=468), 26: -30,432 (n=8), 63: -30,450 (n=294), 58: -30,490 (n=139), 97: -30,508 (n=38), 49: -30,642 (n=92), 48: -30,652 (n=559), 71: -30,666 (n=30), 108: -30,721 (n=8), 14: -30,773 (n=31), 150: -30,819 (n=259), 70: -30,835 (n=59), 35: -30,835 (n=16), 56: -30,835 (n=17), 72: -30,839 (n=13), 65: -30,878 (n=160), 50: -30,910 (n=8485), 30: -31,115 (n=55), 60: -31,181 (n=33), 61: -31,285 (n=117), 44: -31,312 (n=41), 40: -31,329 (n=108), 86: -31,454 (n=10), 42: -31,473 (n=893), 66: -31,497 (n=333), 94: -31,527 (n=22), 85: -31,546 (n=13), 51: -31,555 (n=21), 38: -31,706 (n=24), 104: -31,742 (n=6), 45: -31,775 (n=123), 33: -31,832 (n=25), 36: -31,855 (n=137), 53: -31,941 (n=77), 57: -31,986 (n=87), 144: -32,007 (n=8), 25: -32,083 (n=10), 62: -32,130 (n=22), 73: -32,208 (n=20), 59: -32,226 (n=25), 9: -32,230 (n=19), 54: -32,394 (n=27), 113: -32,418 (n=15), 103: -32,462 (n=9), 84: -32,465 (n=16), 115: -32,512 (n=8), 39: -32,533 (n=61), 96: -32,630 (n=8), 55: -32,710 (n=697), 41: -32,727 (n=57), 87: -32,906 (n=18), 109: -32,944 (n=4), 52: -32,951 (n=23), 125: -33,009 (n=2), 4: -33,017 (n=39), 88: -33,112 (n=12), 98: -33,151 (n=21), 0: -33,230 (n=228), 68: -33,247 (n=19), 17: -33,269 (n=10), 76: -33,276 (n=18), 78: -33,288 (n=16), 93: -33,297 (n=10), 21: -33,400 (n=13), 69: -33,447 (n=30), 95: -33,449 (n=5), 28: -33,526 (n=21), 31: -33,577 (n=18), 24: -33,583 (n=24), 83: -33,599 (n=114), 22: -33,631 (n=18), 43: -33,631 (n=22), 1: -33,664 (n=8), 81: -33,694 (n=29), 119: -33,699 (n=3), 6: -33,709 (n=13), 2: -33,749 (n=3), 90: -33,822 (n=7), 13: -33,976 (n=8), 20: -34,021 (n=9), 111: -34,111 (n=8), 102: -34,126 (n=5), 11: -34,164 (n=17), 47: -34,169 (n=29), 82: -34,211 (n=50), 99: -34,286 (n=75), 15: -34,394 (n=12), 10: -34,451 (n=15), 140: -34,453 (n=4), 64: -34,455 (n=23), 134: -34,464 (n=2), 32: -34,544 (n=11), 46: -34,592 (n=40), 37: -34,598 (n=14), 12: -34,899 (n=15), 7: -34,904 (n=9), 79: -34,932 (n=19), 101: -34,988 (n=12), 107: -35,073 (n=7), 3: -35,105 (n=7), 136: -35,186 (n=49), 77: -35,231 (n=240), 34: -35,276 (n=72), 16: -35,385 (n=19), 23: -35,470 (n=17), 100: -35,487 (n=56), 91: -35,887 (n=10), 129: -35,962 (n=88), 75: -36,461 (n=15), 67: -36,486 (n=20), 128: -36,508 (n=3), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,596 (n=53), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,986 | 26 | 30 | 25 | 17385 | 11.2 | 26: -30,767 (n=619), 25: -30,826 (n=8487), 30: -31,080 (n=5659), 31: -31,748 (n=144), 29: -32,114 (n=145), 27: -32,495 (n=261), 28: -33,459 (n=1351), 32: -34,065 (n=162), 41: -34,307 (n=3), 35: -34,893 (n=188), 45: -35,319 (n=2), 33: -35,462 (n=141), 37: -35,762 (n=28), 34: -35,911 (n=71), 39: -36,046 (n=13), 38: -36,219 (n=25), 36: -36,822 (n=41), 42: -36,946 (n=4), 46: -38,521 (n=3), 40: -38,772 (n=14), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,693 (n=8), 43: -40,312 (n=6), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,311 | 1 | 0 | 35 | 17381 | 24.66 | 1: -30,215 (n=1443), 9: -31,006 (n=104), 0: -31,129 (n=14386), 22: -31,572 (n=3), 2: -32,636 (n=189), 4: -32,982 (n=118), 8: -33,119 (n=89), 6: -33,139 (n=127), 3: -34,212 (n=198), 19: -34,452 (n=9), 17: -34,501 (n=16), 11: -34,890 (n=73), 5: -35,019 (n=184), 13: -35,446 (n=53), 7: -35,543 (n=105), 28: -35,676 (n=3), 12: -35,786 (n=35), 16: -35,808 (n=17), 14: -36,160 (n=27), 20: -36,357 (n=6), 15: -36,483 (n=35), 18: -36,825 (n=22), 10: -36,945 (n=53), 23: -36,978 (n=7), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,654 (n=12), 26: -40,268 (n=3), 29: -40,917 (n=34), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,786 | 3 | 3 | 4 | 17385 | 2.61 | 3: -30,842 (n=15692), 2: -35,748 (n=1205), 4: -36,342 (n=468), 5: -42,629 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 17385 | 62.3 | 61: -27,918 (n=2), 80: -29,658 (n=335), 130: -29,880 (n=14), 93: -30,113 (n=434), 138: -30,186 (n=4), 81: -30,256 (n=87), 120: -30,270 (n=18), 85: -30,517 (n=101), 86: -30,612 (n=933), 62: -30,676 (n=9), 91: -30,725 (n=102), 100: -30,904 (n=10896), 50: -30,923 (n=150), 123: -31,002 (n=55), 66: -31,131 (n=18), 111: -31,163 (n=42), 90: -31,169 (n=149), 78: -31,219 (n=147), 125: -31,236 (n=94), 94: -31,336 (n=35), 92: -31,397 (n=31), 55: -31,425 (n=4), 65: -31,427 (n=7), 141: -31,447 (n=3), 115: -31,483 (n=36), 119: -31,499 (n=18), 129: -31,500 (n=21), 107: -31,506 (n=28), 99: -31,517 (n=43), 117: -31,544 (n=119), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,654 (n=121), 113: -31,720 (n=24), 103: -31,723 (n=31), 133: -31,740 (n=10), 67: -31,763 (n=10), 84: -31,871 (n=87), 87: -31,948 (n=25), 95: -32,102 (n=43), 70: -32,188 (n=20), 132: -32,285 (n=12), 109: -32,289 (n=45), 53: -32,306 (n=5), 102: -32,311 (n=45), 63: -32,321 (n=11), 114: -32,336 (n=31), 105: -32,350 (n=127), 149: -32,426 (n=4), 104: -32,511 (n=625), 71: -32,523 (n=21), 57: -32,552 (n=6), 82: -32,585 (n=23), 128: -32,619 (n=33), 127: -32,621 (n=35), 59: -32,721 (n=5), 88: -32,773 (n=75), 110: -32,999 (n=26), 76: -33,081 (n=20), 112: -33,208 (n=217), 97: -33,237 (n=59), 122: -33,237 (n=39), 98: -33,297 (n=61), 69: -33,454 (n=11), 101: -33,466 (n=46), 68: -33,466 (n=12), 89: -33,489 (n=173), 134: -33,531 (n=8), 116: -33,611 (n=78), 126: -33,677 (n=28), 135: -33,789 (n=495), 108: -33,936 (n=29), 96: -33,961 (n=49), 136: -34,218 (n=7), 74: -34,234 (n=37), 124: -34,315 (n=26), 72: -34,325 (n=14), 75: -34,489 (n=59), 143: -34,578 (n=12), 79: -34,678 (n=55), 144: -34,772 (n=2), 106: -34,783 (n=48), 121: -34,856 (n=17), 137: -35,119 (n=6), 150: -35,780 (n=178), 131: -35,881 (n=17), 56: -35,940 (n=6), 139: -36,068 (n=8), 52: -36,201 (n=4), 142: -36,242 (n=8), 77: -36,825 (n=27), 118: -36,871 (n=16), 73: -37,222 (n=14), 148: -37,549 (n=4), 58: -37,611 (n=6), 146: -37,838 (n=2), 140: -38,416 (n=3), 51: -38,935 (n=5), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,313 | 6 | 6 | 8 | 17385 | 6.13 | 6: -30,754 (n=15500), 5: -34,679 (n=768), 7: -36,444 (n=426), 4: -37,450 (n=446), 3: -37,707 (n=146), 8: -38,159 (n=66), 9: -40,170 (n=25), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +10,167 | 0.0 | 0.0 | 13 | 17385 | 10.33 | 0.0: -30,996 (n=15157), 0.1: -33,100 (n=1071), 0.2: -33,774 (n=647), 0.4: -33,949 (n=103), 0.3: -34,066 (n=216), 0.5: -34,628 (n=61), 1.1: -34,978 (n=7), 0.7: -35,656 (n=18), 0.6: -36,846 (n=58), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -39,081 (n=9), 0.8: -41,164 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,162 | 7 | 7 | 8 | 17385 | 6.13 | 7: -30,702 (n=15492), 5: -36,300 (n=74), 6: -36,369 (n=930), 8: -36,593 (n=577), 10: -36,708 (n=125), 9: -37,433 (n=114), 4: -38,044 (n=64), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,140 | 13 | 20 | 11 | 17385 | 4.69 | 13: -30,887 (n=42), 16: -30,925 (n=374), 17: -30,964 (n=5841), 19: -31,373 (n=927), 18: -31,375 (n=891), 14: -31,427 (n=139), 20: -31,575 (n=8985), 15: -32,149 (n=155), 11: -32,310 (n=3), 12: -33,484 (n=20), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,044 | 10 | 8 | 11 | 17385 | 8.34 | 10: -30,741 (n=14755), 7: -32,459 (n=564), 8: -34,707 (n=1023), 9: -35,115 (n=601), 6: -35,329 (n=187), 5: -35,947 (n=29), 12: -37,855 (n=54), 11: -38,114 (n=76), 4: -38,304 (n=26), 14: -39,848 (n=32), 13: -40,785 (n=38) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +10,017 | 20 | 20 | 15 | 17385 | 7.73 | 20: -30,648 (n=10117), 19: -30,916 (n=4995), 18: -31,526 (n=405), 17: -34,330 (n=736), 16: -36,303 (n=164), 21: -36,533 (n=359), 15: -37,285 (n=81), 23: -37,726 (n=97), 22: -37,881 (n=194), 14: -38,521 (n=41), 26: -38,575 (n=45), 24: -39,283 (n=91), 25: -39,407 (n=22), 13: -39,593 (n=18), 12: -40,665 (n=20) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,621 | 0 | 0 | 9 | 17385 | 7.17 | 0: -31,037 (n=15786), 1: -34,011 (n=832), 2: -34,288 (n=350), 3: -34,773 (n=261), 7: -35,103 (n=7), 4: -35,188 (n=97), 5: -35,653 (n=22), 6: -37,768 (n=27), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,427 | 0.55 | 0.5 | 15 | 17385 | 7.52 | 0.55: -30,364 (n=9878), 0.5: -31,765 (n=4115), 0.65: -31,786 (n=1280), 0.75: -32,163 (n=130), 0.7: -32,299 (n=297), 0.6: -33,286 (n=422), 0.8: -34,458 (n=60), 0.45: -34,669 (n=521), 0.9: -35,533 (n=12), 0.35: -36,038 (n=170), 0.4: -36,122 (n=204), 0.85: -36,511 (n=15), 0.95: -37,209 (n=3), 1.0: -38,525 (n=8), 0.3: -39,791 (n=270) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,586 | 14 | 13 | 9 | 17385 | 4.28 | 14: -30,957 (n=2990), 11: -31,193 (n=835), 13: -31,310 (n=10192), 12: -31,402 (n=2308), 15: -31,602 (n=543), 10: -33,003 (n=139), 16: -33,516 (n=302), 9: -36,684 (n=54), 8: -39,543 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,405 | 2 | 2 | 4 | 17385 | 2.84 | 2: -31,090 (n=16680), 1: -36,958 (n=577), 3: -38,514 (n=47), 0: -39,495 (n=81) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,263 | 13 | 12 | 11 | 17385 | 8.26 | 13: -30,757 (n=1420), 14: -31,218 (n=14636), 11: -32,482 (n=236), 12: -32,605 (n=724), 9: -34,169 (n=31), 6: -34,388 (n=4), 10: -35,328 (n=283), 7: -35,686 (n=10), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,512 | frontier | frontier | 2 | 17385 | 0.91 | frontier: -31,023 (n=16642), v312: -38,535 (n=743) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,387 | 2 | 2 | 3 | 17385 | 1.83 | 2: -30,962 (n=16392), 1: -37,599 (n=934), 3: -38,350 (n=59) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 17385 | 9.49 | 6: -30,481 (n=23), 21: -30,704 (n=3169), 14: -30,829 (n=25), 22: -30,868 (n=8688), 23: -31,304 (n=772), 20: -31,330 (n=703), 16: -31,999 (n=111), 17: -32,401 (n=827), 25: -32,549 (n=1377), 18: -32,929 (n=660), 13: -33,010 (n=30), 24: -33,155 (n=455), 15: -33,429 (n=56), 19: -33,450 (n=219), 12: -33,945 (n=13), 9: -34,073 (n=53), 10: -34,879 (n=69), 11: -36,391 (n=38), 7: -36,543 (n=22), 5: -36,607 (n=69), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,646 | 34 | 40 | 31 | 17384 | 7.47 | 34: -30,345 (n=323), 33: -30,619 (n=68), 38: -30,631 (n=4004), 49: -30,643 (n=470), 43: -30,687 (n=4906), 44: -30,899 (n=501), 47: -31,078 (n=312), 45: -31,161 (n=736), 30: -31,294 (n=76), 37: -31,372 (n=672), 27: -31,404 (n=12), 39: -31,516 (n=633), 28: -32,036 (n=20), 32: -32,251 (n=65), 26: -32,258 (n=62), 50: -32,514 (n=466), 40: -32,773 (n=2876), 29: -32,779 (n=17), 31: -32,822 (n=44), 35: -32,893 (n=244), 42: -32,956 (n=238), 46: -33,032 (n=120), 36: -33,133 (n=205), 25: -33,175 (n=7), 41: -33,203 (n=136), 48: -34,282 (n=78), 20: -34,876 (n=54), 24: -36,135 (n=26), 23: -36,212 (n=6), 22: -36,991 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3223)
- (9, 3, 6): -16,461 (n=2241)
- (12, 4, 6): -16,525 (n=536)
- (10, 3, 6): -16,840 (n=2855)
- (8, 3, 5): -16,866 (n=301)
- (8, 3, 6): -17,552 (n=842)
- (10, 4, 6): -17,975 (n=2528)
- (11, 3, 6): -18,175 (n=593)
- (11, 4, 6): -19,867 (n=592)
- (17, 3, 6): -20,013 (n=66)
- (8, 4, 6): -21,051 (n=802)
- (13, 4, 6): -21,564 (n=224)
- (14, 3, 6): -21,679 (n=248)
- (13, 3, 6): -21,783 (n=334)
- (8, 3, 4): -22,126 (n=88)

_Generated 2026-09-09 17:44. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 7806 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=7806); harvest_min=1–3 (n=7806); wheat_tiles=0–8 (n=7806); wheat_stock=0–40 (n=7806); min_hands=3–6 (n=7806); load_per_hand=12–26 (n=7806); geese=0–2 (n=7806); open_melons=4–14 (n=7806)
- **Evidence:** 7806 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 99 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=99); harvest_min=1–3 (n=99); wheat_tiles=0–2 (n=99); wheat_stock=0–6 (n=99); min_hands=3–6 (n=99); load_per_hand=15–23 (n=99); geese=0–2 (n=99); open_melons=7–13 (n=99)
- **Evidence:** 99 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 51 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=51); harvest_min=1–3 (n=51); wheat_tiles=0–3 (n=51); wheat_stock=0–39 (n=51); min_hands=3–6 (n=51); load_per_hand=12–26 (n=51); geese=0–2 (n=51); open_melons=4–13 (n=51)
- **Evidence:** 51 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 39 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=39); harvest_min=1–3 (n=39); wheat_tiles=0–8 (n=39); wheat_stock=0–39 (n=39); min_hands=3–6 (n=39); load_per_hand=12–23 (n=39); geese=0–2 (n=39); open_melons=6–14 (n=39)
- **Evidence:** 39 candidates, multiple seeds. Confidence: high

### None (observed in 19 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=19); harvest_min=1–3 (n=19); wheat_tiles=0; wheat_stock=0–11 (n=19); min_hands=3–6 (n=19); load_per_hand=12–18 (n=19); geese=0–2 (n=19); open_melons=7–14 (n=19)
- **Evidence:** 19 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 17:44. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._