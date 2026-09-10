# Evolution run 20260909-215517

Frontier opponent: `H32.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.00 h · candidates evaluated this run: 1204 · games 22,598 (11,288/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 444 | 888 |
| dead_pattern | 175 | 350 |
| dead_smoke | 168 | 1344 |
| alive | 417 | 20016 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 18612 · held-out evaluated: 0 · held-out PASS: 0

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

- H32: best -15,269 (`0c3989f7d742`), n=2443
- M2: best -16,102 (`8b77b3e994bc`), n=2526
- c1: best -16,310 (`23734cef4da1`), n=3296
- queue: best -15,412 (`fe4745b56024`), n=4367
- v312: best -15,275 (`52b3d5cc236e`), n=3030
- wide: best -16,047 (`512e53fe15bc`), n=2950

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| labor_reserve_buffer | +19,398 | 120 | 50 | 147 | 18603 | 66.05 | 120: -22,370 (n=10), 118: -25,349 (n=2), 141: -28,023 (n=6), 5: -28,605 (n=57), 143: -28,964 (n=3), 26: -29,468 (n=9), 112: -29,479 (n=14), 8: -29,645 (n=7), 27: -29,845 (n=40), 19: -30,031 (n=19), 89: -30,259 (n=32), 18: -30,342 (n=1276), 97: -30,398 (n=43), 106: -30,406 (n=45), 63: -30,455 (n=326), 74: -30,483 (n=414), 92: -30,528 (n=506), 58: -30,675 (n=155), 35: -30,680 (n=18), 48: -30,683 (n=571), 60: -30,728 (n=39), 150: -30,762 (n=288), 70: -30,783 (n=80), 65: -30,784 (n=165), 72: -30,839 (n=13), 56: -30,874 (n=24), 50: -30,946 (n=9039), 49: -31,000 (n=98), 71: -31,030 (n=31), 44: -31,108 (n=48), 80: -31,115 (n=18), 51: -31,223 (n=23), 14: -31,247 (n=34), 61: -31,410 (n=125), 108: -31,413 (n=9), 42: -31,451 (n=941), 144: -31,452 (n=10), 86: -31,454 (n=10), 40: -31,482 (n=116), 30: -31,487 (n=62), 94: -31,527 (n=22), 66: -31,586 (n=360), 36: -31,626 (n=151), 73: -31,689 (n=22), 104: -31,742 (n=6), 53: -31,804 (n=96), 45: -31,852 (n=126), 85: -31,909 (n=14), 110: -31,921 (n=6), 38: -32,014 (n=26), 9: -32,055 (n=20), 57: -32,144 (n=90), 59: -32,226 (n=25), 33: -32,365 (n=27), 113: -32,418 (n=15), 17: -32,418 (n=11), 84: -32,503 (n=17), 115: -32,512 (n=8), 39: -32,529 (n=62), 28: -32,568 (n=23), 25: -32,593 (n=11), 55: -32,604 (n=750), 96: -32,630 (n=8), 54: -32,651 (n=28), 41: -32,701 (n=58), 62: -32,741 (n=24), 87: -32,742 (n=19), 52: -32,865 (n=24), 109: -32,944 (n=4), 125: -33,009 (n=2), 4: -33,017 (n=39), 103: -33,035 (n=10), 43: -33,057 (n=23), 88: -33,112 (n=12), 98: -33,151 (n=21), 0: -33,241 (n=242), 68: -33,247 (n=19), 93: -33,297 (n=10), 78: -33,339 (n=17), 6: -33,368 (n=14), 21: -33,400 (n=13), 2: -33,419 (n=4), 95: -33,449 (n=5), 69: -33,518 (n=31), 31: -33,560 (n=19), 83: -33,588 (n=115), 76: -33,609 (n=19), 22: -33,631 (n=18), 20: -33,653 (n=12), 1: -33,664 (n=8), 102: -33,689 (n=6), 81: -33,694 (n=29), 119: -33,699 (n=3), 24: -33,703 (n=25), 47: -33,773 (n=35), 13: -33,976 (n=8), 64: -34,024 (n=25), 90: -34,046 (n=8), 111: -34,111 (n=8), 82: -34,211 (n=50), 135: -34,236 (n=2), 99: -34,375 (n=76), 15: -34,394 (n=12), 79: -34,408 (n=25), 10: -34,451 (n=15), 140: -34,453 (n=4), 134: -34,464 (n=2), 11: -34,526 (n=19), 46: -34,592 (n=40), 101: -34,712 (n=13), 12: -34,899 (n=15), 7: -34,904 (n=9), 107: -35,073 (n=7), 3: -35,105 (n=7), 37: -35,173 (n=17), 16: -35,226 (n=20), 77: -35,236 (n=243), 34: -35,375 (n=74), 136: -35,375 (n=52), 32: -35,436 (n=12), 100: -35,556 (n=59), 91: -35,887 (n=10), 129: -36,031 (n=90), 75: -36,461 (n=15), 67: -36,486 (n=20), 128: -36,508 (n=3), 105: -36,563 (n=3), 117: -36,604 (n=2), 145: -36,990 (n=7), 23: -37,025 (n=21), 114: -37,341 (n=4), 124: -38,112 (n=4), 127: -38,268 (n=2), 29: -38,640 (n=61), 131: -39,532 (n=3), 132: -39,931 (n=2), 149: -41,502 (n=2), 133: -41,768 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +12,881 | 26 | 30 | 25 | 18612 | 11.21 | 26: -30,871 (n=668), 25: -30,881 (n=9091), 30: -31,087 (n=6077), 31: -31,662 (n=148), 29: -31,975 (n=153), 27: -32,333 (n=278), 28: -33,469 (n=1423), 32: -33,885 (n=184), 41: -34,307 (n=3), 35: -35,006 (n=197), 45: -35,319 (n=2), 33: -35,548 (n=147), 37: -35,822 (n=29), 34: -35,870 (n=79), 39: -36,046 (n=13), 38: -36,301 (n=27), 36: -36,731 (n=44), 42: -36,946 (n=4), 46: -38,521 (n=3), 43: -38,819 (n=7), 40: -39,082 (n=16), 44: -39,306 (n=6), 47: -39,384 (n=2), 50: -39,586 (n=9), 48: -43,753 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_stock | +12,305 | 1 | 0 | 35 | 18608 | 24.41 | 1: -30,221 (n=1674), 9: -30,860 (n=110), 0: -31,158 (n=15250), 22: -31,572 (n=3), 2: -32,659 (n=210), 6: -33,068 (n=138), 8: -33,091 (n=93), 4: -33,552 (n=134), 3: -34,355 (n=216), 19: -34,452 (n=9), 11: -34,779 (n=76), 17: -34,944 (n=17), 5: -35,232 (n=204), 20: -35,341 (n=7), 13: -35,381 (n=55), 7: -35,407 (n=114), 28: -35,676 (n=3), 12: -35,732 (n=36), 14: -35,954 (n=29), 16: -36,073 (n=18), 15: -36,357 (n=36), 23: -36,978 (n=7), 18: -36,999 (n=24), 10: -37,015 (n=60), 24: -37,048 (n=7), 39: -37,524 (n=12), 21: -37,766 (n=7), 40: -37,938 (n=14), 26: -40,268 (n=3), 29: -40,770 (n=38), 33: -42,526 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +11,875 | 3 | 3 | 4 | 18612 | 2.61 | 3: -30,873 (n=16804), 2: -35,725 (n=1285), 4: -36,361 (n=502), 5: -42,748 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +11,528 | 61 | 100 | 101 | 18612 | 62.13 | 61: -27,918 (n=2), 130: -29,880 (n=14), 80: -29,919 (n=416), 138: -30,059 (n=5), 93: -30,150 (n=441), 120: -30,212 (n=21), 81: -30,288 (n=93), 86: -30,490 (n=1018), 85: -30,616 (n=102), 62: -30,676 (n=9), 91: -30,774 (n=105), 50: -30,868 (n=195), 64: -30,928 (n=14), 100: -30,964 (n=11634), 90: -30,968 (n=179), 78: -31,066 (n=168), 123: -31,076 (n=56), 66: -31,131 (n=18), 59: -31,163 (n=6), 125: -31,190 (n=95), 107: -31,246 (n=30), 111: -31,285 (n=45), 129: -31,300 (n=22), 65: -31,427 (n=7), 115: -31,483 (n=36), 92: -31,526 (n=34), 117: -31,551 (n=127), 147: -31,607 (n=7), 94: -31,629 (n=38), 99: -31,689 (n=45), 133: -31,740 (n=10), 83: -31,745 (n=126), 103: -31,837 (n=34), 113: -31,873 (n=25), 119: -31,933 (n=22), 87: -31,948 (n=25), 84: -32,047 (n=97), 95: -32,108 (n=44), 71: -32,191 (n=22), 102: -32,238 (n=46), 132: -32,285 (n=12), 53: -32,306 (n=5), 63: -32,321 (n=11), 114: -32,336 (n=31), 149: -32,426 (n=4), 88: -32,448 (n=77), 70: -32,455 (n=21), 104: -32,456 (n=658), 109: -32,574 (n=51), 82: -32,585 (n=23), 105: -32,629 (n=136), 127: -32,632 (n=38), 128: -32,775 (n=34), 110: -32,812 (n=30), 98: -32,833 (n=68), 67: -32,961 (n=12), 76: -33,068 (n=22), 112: -33,133 (n=224), 97: -33,298 (n=60), 57: -33,366 (n=7), 122: -33,424 (n=41), 68: -33,466 (n=12), 141: -33,486 (n=4), 69: -33,501 (n=14), 89: -33,512 (n=183), 116: -33,536 (n=80), 101: -33,544 (n=48), 126: -33,677 (n=28), 135: -33,766 (n=514), 55: -33,777 (n=5), 134: -33,870 (n=9), 108: -33,977 (n=31), 96: -34,154 (n=51), 136: -34,218 (n=7), 74: -34,234 (n=37), 72: -34,325 (n=14), 124: -34,455 (n=28), 75: -34,520 (n=60), 143: -34,578 (n=12), 79: -34,679 (n=64), 106: -34,783 (n=48), 121: -34,821 (n=19), 137: -35,119 (n=6), 144: -35,500 (n=3), 131: -35,641 (n=18), 150: -35,843 (n=184), 56: -35,940 (n=6), 52: -36,201 (n=4), 139: -36,227 (n=9), 142: -36,242 (n=8), 118: -37,178 (n=17), 73: -37,334 (n=16), 77: -37,410 (n=29), 148: -37,549 (n=4), 51: -37,583 (n=6), 58: -37,611 (n=6), 146: -37,838 (n=2), 140: -38,416 (n=3), 54: -38,470 (n=4), 145: -39,395 (n=13), 60: -39,446 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +11,294 | 6 | 6 | 8 | 18612 | 6.13 | 6: -30,773 (n=16587), 5: -34,721 (n=830), 7: -36,589 (n=448), 4: -37,530 (n=488), 3: -37,662 (n=153), 8: -38,188 (n=72), 9: -40,277 (n=26), 10: -42,068 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +10,299 | 13 | 20 | 11 | 18612 | 4.62 | 13: -30,728 (n=44), 16: -30,957 (n=404), 17: -31,025 (n=6331), 19: -31,305 (n=1012), 18: -31,396 (n=960), 14: -31,551 (n=146), 20: -31,593 (n=9512), 15: -32,181 (n=170), 11: -32,310 (n=3), 12: -33,699 (n=22), 10: -41,027 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +10,133 | 10 | 8 | 11 | 18612 | 8.35 | 10: -30,782 (n=15822), 7: -32,408 (n=620), 8: -34,743 (n=1061), 9: -35,153 (n=642), 6: -35,265 (n=197), 5: -35,660 (n=31), 12: -37,822 (n=56), 4: -37,932 (n=28), 11: -38,000 (n=80), 14: -39,724 (n=33), 13: -40,915 (n=42) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +10,131 | 7 | 7 | 8 | 18612 | 6.13 | 7: -30,732 (n=16596), 5: -36,371 (n=80), 6: -36,386 (n=977), 8: -36,660 (n=622), 10: -36,674 (n=132), 9: -37,352 (n=123), 4: -37,756 (n=73), 3: -40,864 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +9,638 | 20 | 20 | 15 | 18612 | 7.82 | 20: -30,695 (n=10942), 19: -30,907 (n=5251), 18: -31,553 (n=434), 17: -34,291 (n=756), 16: -36,368 (n=173), 21: -36,664 (n=394), 15: -37,365 (n=89), 23: -37,800 (n=110), 22: -37,877 (n=208), 26: -38,510 (n=48), 14: -38,583 (n=42), 13: -39,211 (n=20), 24: -39,357 (n=98), 25: -39,454 (n=24), 12: -40,333 (n=23) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +9,549 | 0.0 | 0.0 | 13 | 18612 | 10.36 | 0.0: -31,033 (n=16264), 0.1: -33,100 (n=1131), 0.4: -33,708 (n=109), 0.2: -33,821 (n=677), 0.3: -34,016 (n=231), 0.5: -34,509 (n=64), 1.1: -34,978 (n=7), 0.7: -35,518 (n=19), 0.6: -37,016 (n=61), 0.9: -37,320 (n=6), 1.0: -37,880 (n=25), 1.2: -38,901 (n=10), 0.8: -40,582 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +9,298 | 0.55 | 0.5 | 15 | 18612 | 7.65 | 0.55: -30,430 (n=10727), 0.5: -31,747 (n=4300), 0.65: -31,797 (n=1330), 0.75: -32,363 (n=137), 0.7: -32,461 (n=323), 0.6: -33,327 (n=453), 0.8: -34,631 (n=67), 0.45: -34,689 (n=549), 0.9: -35,790 (n=13), 0.35: -35,956 (n=181), 0.4: -36,071 (n=215), 0.85: -36,532 (n=16), 0.95: -36,836 (n=4), 1.0: -38,742 (n=9), 0.3: -39,728 (n=288) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_tiles | +8,864 | 0 | 0 | 9 | 18612 | 7.18 | 0: -31,068 (n=16912), 1: -34,021 (n=880), 2: -34,235 (n=373), 3: -34,899 (n=281), 4: -35,053 (n=103), 7: -35,103 (n=7), 5: -35,479 (n=25), 6: -37,768 (n=27), 8: -39,932 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +8,553 | 14 | 13 | 9 | 18612 | 4.25 | 14: -30,990 (n=3284), 11: -31,174 (n=865), 13: -31,334 (n=10852), 12: -31,445 (n=2457), 15: -31,674 (n=588), 10: -33,006 (n=150), 16: -33,431 (n=333), 9: -36,758 (n=61), 8: -39,543 (n=22) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +8,481 | 2 | 2 | 4 | 18612 | 2.83 | 2: -31,108 (n=17844), 1: -37,073 (n=628), 3: -38,393 (n=49), 0: -39,589 (n=91) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +8,164 | 13 | 12 | 11 | 18612 | 8.24 | 13: -30,857 (n=1564), 14: -31,255 (n=15642), 11: -32,290 (n=246), 12: -32,475 (n=772), 9: -33,069 (n=34), 6: -34,388 (n=4), 7: -34,770 (n=11), 10: -35,346 (n=298), 8: -36,607 (n=36), 4: -38,244 (n=2), 5: -39,020 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +7,562 | frontier | frontier | 2 | 18612 | 0.91 | frontier: -31,043 (n=17807), v312: -38,605 (n=805) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +7,365 | 6 | 18 | 21 | 18612 | 9.54 | 6: -30,481 (n=23), 21: -30,785 (n=3430), 22: -30,899 (n=9343), 23: -31,337 (n=831), 20: -31,377 (n=732), 14: -31,530 (n=28), 16: -31,757 (n=118), 17: -32,324 (n=885), 25: -32,604 (n=1457), 18: -32,940 (n=685), 24: -33,144 (n=475), 13: -33,252 (n=31), 15: -33,303 (n=60), 19: -33,347 (n=234), 9: -34,193 (n=54), 12: -34,545 (n=14), 10: -34,840 (n=70), 11: -36,391 (n=38), 7: -36,543 (n=22), 5: -36,773 (n=76), 8: -37,846 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +7,293 | 2 | 2 | 3 | 18612 | 1.83 | 2: -30,993 (n=17561), 1: -37,627 (n=983), 3: -38,286 (n=68) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,724 | 34 | 40 | 31 | 18612 | 7.73 | 34: -30,268 (n=344), 21: -30,358 (n=2), 49: -30,613 (n=500), 43: -30,739 (n=5243), 38: -30,756 (n=4386), 33: -30,758 (n=69), 44: -30,809 (n=543), 47: -30,911 (n=332), 45: -31,260 (n=815), 30: -31,296 (n=78), 27: -31,404 (n=12), 37: -31,467 (n=728), 39: -31,634 (n=690), 26: -31,918 (n=68), 25: -32,256 (n=9), 28: -32,296 (n=22), 50: -32,363 (n=507), 32: -32,459 (n=68), 40: -32,760 (n=2946), 42: -32,888 (n=245), 41: -33,000 (n=152), 36: -33,013 (n=215), 29: -33,024 (n=18), 35: -33,048 (n=256), 31: -33,049 (n=48), 46: -33,143 (n=136), 48: -34,090 (n=82), 20: -34,685 (n=58), 23: -35,631 (n=7), 24: -36,135 (n=26), 22: -36,991 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=3453)
- (9, 3, 6): -16,461 (n=2425)
- (12, 4, 6): -16,525 (n=570)
- (10, 3, 6): -16,840 (n=3056)
- (8, 3, 5): -16,866 (n=318)
- (8, 3, 6): -17,253 (n=884)
- (10, 4, 6): -17,975 (n=2699)
- (11, 3, 6): -18,175 (n=648)
- (11, 4, 6): -19,867 (n=623)
- (17, 3, 6): -20,013 (n=69)
- (8, 4, 6): -21,051 (n=841)
- (13, 4, 6): -21,564 (n=240)
- (14, 3, 6): -21,679 (n=268)
- (13, 3, 6): -21,783 (n=360)
- (8, 3, 4): -22,126 (n=93)

_Generated 2026-09-09 23:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 8916 recent candidates)

- **Observed outcome:** sales=110,524; missed_water=504; idle_share=0.11
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=8916); harvest_min=1–3 (n=8916); wheat_tiles=0–8 (n=8916); wheat_stock=0–40 (n=8916); min_hands=3–6 (n=8916); load_per_hand=12–26 (n=8916); geese=0–2 (n=8916); open_melons=4–14 (n=8916)
- **Evidence:** 8916 candidates, multiple seeds. Confidence: high

### CAPITAL_FAILURE (observed in 112 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=112); harvest_min=1–3 (n=112); wheat_tiles=0–2 (n=112); wheat_stock=0–6 (n=112); min_hands=3–6 (n=112); load_per_hand=15–23 (n=112); geese=0–2 (n=112); open_melons=7–13 (n=112)
- **Evidence:** 112 candidates, multiple seeds. Confidence: high

### CAPACITY_FAILURE (observed in 59 recent candidates)

- **Observed outcome:** sales=68,251; missed_water=424; idle_share=0.14
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=59); harvest_min=1–3 (n=59); wheat_tiles=0–3 (n=59); wheat_stock=0–39 (n=59); min_hands=3–6 (n=59); load_per_hand=12–26 (n=59); geese=0–2 (n=59); open_melons=4–13 (n=59)
- **Evidence:** 59 candidates, multiple seeds. Confidence: high

### LABOR_FAILURE (observed in 44 recent candidates)

- **Observed outcome:** sales=52,598; missed_water=288; idle_share=0.34
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=44); harvest_min=1–3 (n=44); wheat_tiles=0–8 (n=44); wheat_stock=0–39 (n=44); min_hands=3–6 (n=44); load_per_hand=12–23 (n=44); geese=0–2 (n=44); open_melons=6–14 (n=44)
- **Evidence:** 44 candidates, multiple seeds. Confidence: high

### None (observed in 21 recent candidates)

- **Observed outcome:** sales=88,830; missed_water=152; idle_share=0.17
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=21); harvest_min=1–3 (n=21); wheat_tiles=0; wheat_stock=0–11 (n=21); min_hands=3–6 (n=21); load_per_hand=12–18 (n=21); geese=0–2 (n=21); open_melons=7–14 (n=21)
- **Evidence:** 21 candidates, multiple seeds. Confidence: high

_Generated 2026-09-09 23:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._