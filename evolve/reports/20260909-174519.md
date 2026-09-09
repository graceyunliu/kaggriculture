# Evolution run 20260909-174519

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105876759.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1243 · games 22,384 (11,190/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 475 | 950 |
| dead_pattern | 205 | 410 |
| dead_smoke | 150 | 1200 |
| alive | 413 | 19824 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 17798 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2311
- M2: best -16,102 (`8b77b3e994bc`), n=2397
- c1: best -16,310 (`23734cef4da1`), n=3175
- queue: best -15,412 (`fe4745b56024`), n=4195
- v312: best -15,275 (`52b3d5cc236e`), n=2917
- wide: best -16,047 (`512e53fe15bc`), n=2803

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 147 | 17788 | 65.91 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 5: -28,703 (n=55), 143: -28,964 (n=3), 27: -29,422 (n=38), 112: -29,479 (n=14), 8: -29,645 (n=7), 19: -30,031 (n=19), 106: -30,093 (n=39), 110: -30,105 (n=5), 89: -30,144 (n=31), 18: -30,267 (n=1188), 35: -30,299 (n=17), 26: -30,432 (n=8), 97: -30,457 (n=41), 58: -30,464 (n=140), 92: -30,465 (n=483), 74: -30,466 (n=384), 63: -30,509 (n=306), 70: -30,640 (n=64), 48: -30,648 (n=561), 56: -30,652 (n=21), 71: -30,666 (n=30), 49: -30,671 (n=93), 108: -30,721 (n=8), 80: -30,783 (n=17), 150: -30,798 (n=267), 65: -30,833 (n=162), 72: -30,839 (n=13), 60: -30,911 (n=34), 50: -30,917 (n=8688), 14: -30,941 (n=32), 44: -30,973 (n=46), 30: -31,292 (n=57), 40: -31,332 (n=109), 61: -31,389 (n=120), 86: -31,454 (n=10), 66: -31,482 (n=341), 42: -31,496 (n=906), 94: -31,527 (n=22), 85: -31,546 (n=13), 51: -31,555 (n=21), 53: -31,667 (n=87), 36: -31,688 (n=140), 38: -31,706 (n=24), 104: -31,742 (n=6), 45: -31,821 (n=124), 33: -31,832 (n=25), 57: -31,994 (n=88), 144: -32,007 (n=8), 25: -32,083 (n=10), 73: -32,208 (n=20), 59: -32,226 (n=25), 9: -32,230 (n=19), 62: -32,340 (n=23), 113: -32,418 (n=15), 17: -32,418 (n=11), 84: -32,503 (n=17), 115: -32,512 (n=8), 39: -32,533 (n=61), 96: -32,630 (n=8), 54: -32,651 (n=28), 55: -32,687 (n=712), 41: -32,727 (n=57), 87: -32,906 (n=18), 109: -32,944 (n=4), 52: -32,951 (n=23), 125: -33,009 (n=2), 4: -33,017 (n=39), 103: -33,035 (n=10), 88: -33,112 (n=12), 98: -33,151 (n=21), 0: -33,171 (n=232), 68: -33,247 (n=19), 76: -33,276 (n=18), 93: -33,297 (n=10), 78: -33,339 (n=17), 21: -33,400 (n=13), 95: -33,449 (n=5), 69: -33,518 (n=31), 28: -33,526 (n=21), 31: -33,577 (n=18), 24: -33,583 (n=24), 83: -33,599 (n=114), 22: -33,631 (n=18), 43: -33,631 (n=22), 1: -33,664 (n=8), 102: -33,689 (n=6), 81: -33,694 (n=29), 119: -33,699 (n=3), 6: -33,709 (n=13), 2: -33,749 (n=3), 90: -33,822 (n=7), 47: -33,938 (n=31), 13: -33,976 (n=8), 20: -34,021 (n=9), 64: -34,110 (n=24), 111: -34,111 (n=8), 11: -34,164 (n=17), 82: -34,211 (n=50), 99: -34,375 (n=76), 15: -34,394 (n=12), 10: -34,451 (n=15), 140: -34,453 (n=4), 134: -34,464 (n=2), 37: -34,547 (n=15), 46: -34,592 (n=40), 79: -34,772 (n=22), 12: -34,899 (n=15), 7: -34,904 (n=9), 101: -34,988 (n=12), 107: -35,073 (n=7), 3: -35,105 (n=7), 77: -35,228 (n=241), 34: -35,375 (n=74), 136: -35,375 (n=52), 16: -35,385 (n=19), 32: -35,436 (n=12), 100: -35,487 (n=56), 91: -35,887 (n=10), 129: -35,962 (n=88), 23: -36,084 (n=19), 75: -36,461 (n=15), 67: -36,486 (n=20), 128: -36,508 (n=3), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,534 (n=58), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,921 | 26 | 30 | 25 | 17798 | 11.21 | 26: -30,832 (n=636), 25: -30,847 (n=8692), 30: -31,060 (n=5793), 31: -31,679 (n=145), 29: -31,897 (n=149), 27: -32,460 (n=267), 28: -33,480 (n=1374), 32: -33,990 (n=168), 41: -34,307 (n=3), 35: -34,930 (n=193), 45: -35,319 (n=2), 33: -35,541 (n=146), 37: -35,822 (n=29), 34: -35,882 (n=72), 39: -36,046 (n=13), 38: -36,219 (n=25), 36: -36,911 (n=42), 42: -36,946 (n=4), 46: -38,521 (n=3), 43: -38,819 (n=7), 40: -39,082 (n=16), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,586 (n=9), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,340 | 1 | 0 | 35 | 17794 | 24.57 | 1: -30,186 (n=1517), 9: -30,931 (n=108), 0: -31,136 (n=14678), 22: -31,572 (n=3), 2: -32,632 (n=197), 6: -33,020 (n=132), 8: -33,153 (n=90), 4: -33,313 (n=125), 3: -34,349 (n=206), 19: -34,452 (n=9), 11: -34,890 (n=73), 17: -34,944 (n=17), 5: -35,120 (n=187), 20: -35,341 (n=7), 13: -35,446 (n=53), 7: -35,463 (n=108), 28: -35,676 (n=3), 12: -35,786 (n=35), 16: -35,808 (n=17), 14: -36,160 (n=27), 15: -36,357 (n=36), 18: -36,826 (n=23), 23: -36,978 (n=7), 10: -37,034 (n=54), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -38,654 (n=12), 26: -40,268 (n=3), 29: -40,719 (n=37), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,900 | 3 | 3 | 4 | 17798 | 2.61 | 3: -30,848 (n=16063), 2: -35,733 (n=1234), 4: -36,351 (n=480), 5: -42,748 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,530 | 61 | 100 | 101 | 17798 | 62.31 | 61: -27,918 (n=2), 80: -29,763 (n=360), 130: -29,880 (n=14), 93: -30,120 (n=435), 81: -30,168 (n=90), 138: -30,186 (n=4), 120: -30,371 (n=19), 85: -30,517 (n=101), 86: -30,581 (n=957), 62: -30,676 (n=9), 91: -30,725 (n=102), 90: -30,884 (n=159), 100: -30,921 (n=11156), 50: -31,001 (n=164), 123: -31,002 (n=55), 78: -31,107 (n=157), 66: -31,131 (n=18), 111: -31,184 (n=44), 125: -31,236 (n=94), 94: -31,381 (n=36), 92: -31,397 (n=31), 65: -31,427 (n=7), 141: -31,447 (n=3), 115: -31,483 (n=36), 129: -31,500 (n=21), 107: -31,506 (n=28), 99: -31,517 (n=43), 117: -31,595 (n=123), 147: -31,607 (n=7), 64: -31,616 (n=13), 83: -31,619 (n=123), 133: -31,740 (n=10), 103: -31,860 (n=32), 113: -31,873 (n=25), 84: -31,874 (n=88), 87: -31,948 (n=25), 95: -32,108 (n=44), 119: -32,154 (n=20), 70: -32,188 (n=20), 132: -32,285 (n=12), 53: -32,306 (n=5), 102: -32,311 (n=45), 63: -32,321 (n=11), 114: -32,336 (n=31), 105: -32,422 (n=129), 149: -32,426 (n=4), 109: -32,506 (n=48), 104: -32,507 (n=638), 71: -32,523 (n=21), 82: -32,585 (n=23), 128: -32,619 (n=33), 127: -32,621 (n=35), 88: -32,627 (n=76), 110: -32,699 (n=27), 59: -32,721 (n=5), 67: -32,782 (n=11), 98: -32,804 (n=64), 76: -33,090 (n=21), 69: -33,103 (n=12), 112: -33,211 (n=218), 97: -33,237 (n=59), 57: -33,366 (n=7), 122: -33,424 (n=41), 101: -33,466 (n=46), 68: -33,466 (n=12), 89: -33,516 (n=174), 134: -33,531 (n=8), 116: -33,611 (n=78), 126: -33,677 (n=28), 135: -33,775 (n=498), 55: -33,777 (n=5), 108: -33,839 (n=30), 96: -33,961 (n=49), 136: -34,218 (n=7), 74: -34,234 (n=37), 72: -34,325 (n=14), 124: -34,455 (n=28), 75: -34,489 (n=59), 143: -34,578 (n=12), 79: -34,753 (n=59), 106: -34,783 (n=48), 121: -34,908 (n=18), 137: -35,119 (n=6), 144: -35,500 (n=3), 131: -35,641 (n=18), 150: -35,753 (n=181), 56: -35,940 (n=6), 52: -36,201 (n=4), 139: -36,227 (n=9), 142: -36,242 (n=8), 77: -36,825 (n=27), 118: -36,871 (n=16), 73: -37,385 (n=15), 148: -37,549 (n=4), 58: -37,611 (n=6), 146: -37,838 (n=2), 140: -38,416 (n=3), 51: -38,935 (n=5), 145: -39,395 (n=13), 60: -39,446 (n=8), 54: -39,448 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,312 | 6 | 6 | 8 | 17798 | 6.13 | 6: -30,755 (n=15868), 5: -34,705 (n=788), 7: -36,528 (n=436), 4: -37,496 (n=456), 3: -37,711 (n=147), 8: -38,065 (n=69), 9: -40,277 (n=26), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,299 | 13 | 20 | 11 | 17798 | 4.67 | 13: -30,728 (n=44), 16: -30,976 (n=381), 17: -30,985 (n=6001), 19: -31,361 (n=953), 18: -31,381 (n=920), 14: -31,506 (n=141), 20: -31,573 (n=9166), 15: -32,081 (n=160), 11: -32,310 (n=3), 12: -33,505 (n=21), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,159 | 7 | 7 | 8 | 17798 | 6.13 | 7: -30,705 (n=15859), 6: -36,370 (n=942), 5: -36,466 (n=77), 8: -36,631 (n=598), 10: -36,779 (n=127), 9: -37,372 (n=118), 4: -37,996 (n=68), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +9,870 | 10 | 8 | 11 | 17798 | 8.34 | 10: -30,751 (n=15117), 7: -32,422 (n=581), 8: -34,738 (n=1034), 9: -35,124 (n=617), 6: -35,283 (n=190), 5: -35,947 (n=29), 12: -37,855 (n=54), 11: -38,058 (n=77), 4: -38,304 (n=26), 14: -39,848 (n=32), 13: -40,621 (n=41) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,821 | 20 | 20 | 15 | 17798 | 7.77 | 20: -30,656 (n=10400), 19: -30,921 (n=5073), 18: -31,516 (n=415), 17: -34,308 (n=744), 16: -36,331 (n=168), 21: -36,570 (n=369), 15: -37,197 (n=83), 23: -37,661 (n=103), 22: -37,892 (n=200), 14: -38,521 (n=41), 26: -38,575 (n=46), 24: -39,325 (n=92), 25: -39,454 (n=24), 13: -39,593 (n=18), 12: -40,477 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +9,614 | 0 | 0 | 9 | 17798 | 7.17 | 0: -31,044 (n=16163), 1: -33,986 (n=850), 2: -34,293 (n=356), 3: -34,815 (n=269), 7: -35,103 (n=7), 4: -35,193 (n=99), 5: -35,503 (n=24), 6: -37,768 (n=27), 8: -40,658 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,578 | 0.0 | 0.0 | 13 | 17798 | 10.35 | 0.0: -31,005 (n=15533), 0.1: -33,120 (n=1094), 0.2: -33,767 (n=653), 0.4: -33,962 (n=104), 0.3: -34,036 (n=220), 0.5: -34,628 (n=61), 1.1: -34,978 (n=7), 0.7: -35,656 (n=18), 0.6: -36,854 (n=60), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -39,081 (n=9), 0.8: -40,582 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,382 | 0.55 | 0.5 | 15 | 17798 | 7.58 | 0.55: -30,381 (n=10176), 0.65: -31,763 (n=1298), 0.5: -31,764 (n=4168), 0.75: -32,194 (n=131), 0.7: -32,305 (n=303), 0.6: -33,320 (n=433), 0.45: -34,711 (n=532), 0.8: -34,866 (n=62), 0.9: -35,790 (n=13), 0.35: -35,979 (n=173), 0.4: -36,105 (n=205), 0.85: -36,511 (n=15), 0.95: -37,209 (n=3), 1.0: -38,525 (n=8), 0.3: -39,763 (n=278) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,589 | 14 | 13 | 9 | 17798 | 4.27 | 14: -30,953 (n=3075), 11: -31,180 (n=848), 13: -31,315 (n=10429), 12: -31,435 (n=2353), 15: -31,625 (n=554), 10: -32,943 (n=145), 16: -33,371 (n=314), 9: -36,789 (n=58), 8: -39,543 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,504 | 2 | 2 | 4 | 17798 | 2.84 | 2: -31,088 (n=17064), 1: -37,023 (n=603), 3: -38,514 (n=47), 0: -39,593 (n=84) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,237 | 13 | 12 | 11 | 17798 | 8.26 | 13: -30,784 (n=1461), 14: -31,228 (n=14986), 12: -32,524 (n=739), 11: -32,526 (n=238), 9: -34,169 (n=31), 6: -34,388 (n=4), 7: -34,770 (n=11), 10: -35,306 (n=287), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,521 | frontier | frontier | 2 | 17798 | 0.91 | frontier: -31,028 (n=17038), v312: -38,549 (n=760) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 17798 | 9.51 | 6: -30,481 (n=23), 21: -30,754 (n=3256), 22: -30,864 (n=8905), 14: -31,065 (n=26), 20: -31,345 (n=715), 23: -31,355 (n=790), 16: -31,842 (n=114), 17: -32,396 (n=848), 25: -32,532 (n=1413), 18: -32,954 (n=664), 13: -33,010 (n=30), 15: -33,093 (n=58), 24: -33,150 (n=460), 19: -33,488 (n=223), 12: -33,945 (n=13), 9: -34,073 (n=53), 10: -34,840 (n=70), 11: -36,391 (n=38), 7: -36,543 (n=22), 5: -36,703 (n=71), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,323 | 2 | 2 | 3 | 17798 | 1.83 | 2: -30,967 (n=16781), 1: -37,611 (n=954), 3: -38,291 (n=63) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,755 | 34 | 40 | 31 | 17798 | 7.75 | 34: -30,236 (n=330), 21: -30,358 (n=2), 38: -30,652 (n=4136), 49: -30,672 (n=475), 43: -30,710 (n=5024), 33: -30,758 (n=69), 44: -30,818 (n=515), 47: -30,972 (n=321), 30: -31,213 (n=77), 45: -31,267 (n=761), 37: -31,391 (n=691), 27: -31,404 (n=12), 39: -31,517 (n=649), 28: -32,036 (n=20), 26: -32,243 (n=64), 25: -32,406 (n=8), 32: -32,433 (n=66), 50: -32,505 (n=482), 40: -32,763 (n=2897), 29: -32,779 (n=17), 42: -32,956 (n=238), 35: -32,966 (n=248), 41: -33,079 (n=142), 36: -33,123 (n=209), 46: -33,132 (n=126), 31: -33,289 (n=47), 48: -34,282 (n=78), 20: -34,876 (n=54), 23: -35,631 (n=7), 24: -36,135 (n=26), 22: -36,991 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3297)
- (9, 3, 6): -16,461 (n=2303)
- (12, 4, 6): -16,525 (n=546)
- (10, 3, 6): -16,840 (n=2922)
- (8, 3, 5): -16,866 (n=306)
- (8, 3, 6): -17,552 (n=854)
- (10, 4, 6): -17,975 (n=2585)
- (11, 3, 6): -18,175 (n=613)
- (11, 4, 6): -19,867 (n=603)
- (17, 3, 6): -20,013 (n=66)
- (8, 4, 6): -21,051 (n=814)
- (13, 4, 6): -21,564 (n=228)
- (14, 3, 6): -21,679 (n=256)
- (13, 3, 6): -21,783 (n=346)
- (8, 3, 4): -22,126 (n=91)

_Generated 2026-09-09 19:45. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 8156 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=8156); harvest_min=1–3 (n=8156); wheat_tiles=0–8 (n=8156); wheat_stock=0–40 (n=8156); min_hands=3–6 (n=8156); load_per_hand=12–26 (n=8156); geese=0–2 (n=8156); open_melons=4–14 (n=8156)
- **Evidence:** 8156 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 101 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=101); harvest_min=1–3 (n=101); wheat_tiles=0–2 (n=101); wheat_stock=0–6 (n=101); min_hands=3–6 (n=101); load_per_hand=15–23 (n=101); geese=0–2 (n=101); open_melons=7–13 (n=101)
- **Evidence:** 101 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 52 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=52); harvest_min=1–3 (n=52); wheat_tiles=0–3 (n=52); wheat_stock=0–39 (n=52); min_hands=3–6 (n=52); load_per_hand=12–26 (n=52); geese=0–2 (n=52); open_melons=4–13 (n=52)
- **Evidence:** 52 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 40 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=40); harvest_min=1–3 (n=40); wheat_tiles=0–8 (n=40); wheat_stock=0–39 (n=40); min_hands=3–6 (n=40); load_per_hand=12–23 (n=40); geese=0–2 (n=40); open_melons=6–14 (n=40)
- **Evidence:** 40 candidates, multiple seeds. Confidence: high

### None (observed in 20 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=20); harvest_min=1–3 (n=20); wheat_tiles=0; wheat_stock=0–11 (n=20); min_hands=3–6 (n=20); load_per_hand=12–18 (n=20); geese=0–2 (n=20); open_melons=7–14 (n=20)
- **Evidence:** 20 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 19:45. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._