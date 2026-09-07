# Evolution run 20260906-225007

Frontier opponent: `H32.py` · clone: `tape_mengfeili_105887030.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.05 h · candidates evaluated this run: 1303 · games 30,780 (15,003/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 249 | 498 |
| dead_pattern | 285 | 570 |
| dead_smoke | 180 | 1440 |
| alive | 589 | 28272 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 5874 · held-out evaluated: 0 · held-out PASS: 0

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
| `fe4745b56024` | queue | archive_crossover:crossover_g000675_20260905-224724_0 | -15,412 | -3.3 | 2-8 | -17,273 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `a3436012d4f9` | queue | archive_crossover:crossover_g000725_20260906-214654_0 | -15,590 | -3.3 | 2-8 | -16,712 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `667332b39bf5` | queue | archive_crossover:crossover_g000850_20260905-205857_1 | -15,738 | -3.0 | 3-7 | -27,827 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `97e03be128cb` | queue | archive_crossover:crossover_g000400_20260906-211828_1 | -15,791 | -3.5 | 2-8 | -16,760 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `2286322870c4` | v312 | mutate | -15,854 | -3.0 | 3-7 | -14,497 | alive | harvest_min 2→3, open_melons 8→10, early_hire_days 5→8, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→21, setup_capital_share 0.25→0.2, labor_reserve_buffer 50→42, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5 |
| `a442a9ceb68e` | queue | archive_crossover:crossover_g000075_20260906-225544_1 | -15,885 | -3.6 | 2-8 | -17,122 | alive | melon_floor 150→200, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→14, SPREAD_W 1.0→1.25 |
| `5b63d512ad81` | queue | archive_crossover:crossover_g000775_20260906-215507_0 | -15,896 | -3.3 | 2-8 | -15,996 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `081b43704bb8` | queue | archive_crossover:crossover_g000125_20260905-215729_0 | -15,916 | -3.1 | 2-8 | -28,354 | alive | harvest_min 2→1, geese 0→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→2, fert_carry 3→1, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_PRICE_CUSHION 100→86, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→7, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `165447af42cc` | queue | mutate | -15,936 | -3.5 | 2-8 | -16,892 | alive | melon_floor 150→200, open_melons 8→10, early_hire_days 5→0, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3 |
| `512e53fe15bc` | wide | paired | -16,047 | -3.7 | 1-9 | -15,964 | alive | melon_floor 150→100, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→37, HERD_LAST_DAY 19→18, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `12753350f904` | queue | archive_crossover:crossover_g000200_20260906-230552_0 | -16,054 | -3.2 | 2-8 | -14,640 | alive | open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.5 |
| `7eb169e63774` | queue | archive_crossover:crossover_g000800_20260905-205431_1 | -16,091 | -3.4 | 2-8 | -16,982 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→38, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `a71aba279a14` | queue | archive_crossover:crossover_g000125_20260905-195057_1 | -16,104 | -3.6 | 1-9 | -16,325 | alive | melon_floor 150→100, harvest_min 2→1, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, wheat_sell_price 30→25, setup_capital_share 0.25→0.05, labor_reserve_buffer 50→18, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |
| `15f5884d814c` | queue | crossover | -16,128 | -3.3 | 2-8 | -14,148 | alive | open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→22, wheat_sell_price 30→25, setup_capital_share 0.25→0.1, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→18, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.4, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.25 |

## Islands (best dev margin, population size)

- H32: best -15,269 (`0c3989f7d742`), n=435
- M2: best -17,604 (`97ba0a0f33e3`), n=463
- c1: best -16,310 (`23734cef4da1`), n=1205
- queue: best -15,412 (`fe4745b56024`), n=1638
- v312: best -15,854 (`2286322870c4`), n=1194
- wide: best -16,047 (`512e53fe15bc`), n=939

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| labor_reserve_buffer | 18,968 | 86 | 50 | 86: -20,673 (2), 112: -25,153 (3), 71: -25,418 (6), 72: -26,442 (3), 92: -27,460 (30), 5: -27,631 (10), 49: -27,834 (17), 35: -28,345 (3), 58: -28,654 (33), 9: -28,701 (6), 27: -28,856 (26), 89: -28,859 (4), 85: -28,921 (4), 18: -29,632 (272), 63: -29,847 (24), 65: -30,247 (63), 61: -30,254 (66), 59: -30,471 (8), 48: -30,522 (313), 90: -30,728 (2), 56: -30,766 (5), 50: -30,821 (2828), 36: -31,113 (20), 33: -31,139 (15), 144: -31,182 (2), 24: -31,352 (11), 93: -31,438 (4), 115: -31,553 (4), 136: -31,602 (10), 60: -31,644 (16), 80: -31,689 (8), 26: -31,811 (2), 42: -31,826 (386), 51: -31,859 (8), 25: -31,865 (4), 74: -31,891 (25), 38: -31,920 (10), 57: -31,943 (68), 40: -31,962 (67), 45: -31,980 (63), 103: -32,034 (4), 62: -32,239 (12), 14: -32,290 (5), 39: -32,359 (46), 73: -32,529 (7), 52: -32,588 (6), 28: -32,609 (14), 104: -32,627 (3), 44: -32,692 (10), 83: -32,717 (70), 88: -32,733 (7), 78: -32,765 (5), 43: -32,792 (12), 84: -32,873 (9), 70: -32,995 (13), 76: -33,125 (5), 4: -33,260 (34), 119: -33,340 (2), 7: -33,417 (3), 111: -33,417 (5), 0: -33,620 (111), 55: -33,672 (333), 19: -33,712 (4), 94: -33,747 (11), 6: -33,882 (8), 13: -34,071 (4), 69: -34,177 (9), 34: -34,198 (26), 21: -34,457 (4), 134: -34,464 (2), 91: -34,507 (4), 99: -34,708 (58), 30: -34,984 (3), 41: -34,984 (15), 54: -34,988 (5), 82: -35,067 (17), 77: -35,080 (182), 81: -35,147 (18), 29: -35,175 (7), 32: -35,252 (7), 129: -35,288 (60), 100: -35,349 (27), 53: -35,382 (12), 47: -35,398 (11), 22: -35,414 (11), 10: -35,579 (10), 46: -35,599 (17), 87: -35,642 (6), 79: -35,703 (3), 31: -35,716 (4), 107: -35,804 (3), 97: -36,084 (9), 106: -36,115 (2), 3: -36,144 (4), 101: -36,200 (7), 66: -36,266 (16), 110: -36,353 (3), 23: -36,562 (7), 16: -36,603 (10), 109: -36,655 (2), 68: -36,942 (4), 145: -36,990 (7), 11: -36,993 (11), 15: -37,056 (3), 64: -37,278 (10), 114: -37,370 (3), 150: -37,520 (15), 1: -37,771 (3), 12: -37,835 (6), 102: -38,189 (3), 67: -39,416 (12), 37: -39,641 (3) |
| ROUTE_LEN | 14,236 | 3 | 3 | 3: -31,093 (5276), 2: -36,268 (442), 4: -36,921 (152), 5: -45,329 (4) |
| wheat_stock | 14,012 | 0 | 0 | 0: -31,293 (5196), 9: -31,450 (55), 6: -32,213 (28), 17: -32,496 (4), 1: -32,889 (165), 19: -32,920 (2), 8: -33,671 (33), 4: -33,786 (33), 16: -33,966 (3), 2: -34,282 (42), 5: -34,419 (45), 11: -34,929 (20), 3: -35,003 (103), 21: -35,375 (2), 13: -36,032 (14), 7: -36,206 (36), 10: -36,295 (19), 28: -36,361 (2), 15: -36,461 (11), 14: -36,808 (11), 23: -37,081 (5), 12: -37,525 (12), 18: -38,529 (8), 20: -38,590 (4), 39: -38,737 (3), 29: -40,076 (6), 40: -41,450 (5), 33: -42,526 (4), 26: -45,305 (2) |
| load_per_hand | 13,334 | 20 | 20 | 20: -30,534 (2193), 19: -31,176 (2657), 18: -32,806 (131), 17: -34,235 (490), 21: -36,089 (141), 16: -36,917 (60), 15: -37,016 (31), 23: -37,039 (32), 22: -37,358 (51), 24: -38,020 (19), 14: -38,136 (16), 25: -38,910 (13), 26: -39,342 (20), 13: -40,253 (12), 12: -43,869 (8) |
| max_animals | 12,944 | 14 | 20 | 14: -30,185 (48), 17: -30,964 (1273), 16: -31,455 (161), 20: -31,765 (3854), 18: -31,822 (277), 19: -32,616 (196), 13: -34,262 (16), 15: -35,083 (36), 12: -37,278 (8), 10: -43,129 (4) |
| MELON_PRICE_CUSHION | 12,880 | 63 | 100 | 63: -28,660 (4), 65: -28,869 (3), 69: -29,694 (3), 130: -29,707 (9), 64: -29,716 (6), 85: -29,751 (45), 66: -29,765 (8), 93: -30,083 (133), 86: -30,148 (163), 94: -30,484 (7), 62: -30,527 (2), 70: -30,641 (11), 100: -30,716 (3489), 114: -30,980 (16), 141: -31,181 (2), 111: -31,226 (21), 92: -31,252 (8), 129: -31,340 (10), 120: -31,382 (7), 125: -31,412 (55), 105: -31,439 (42), 76: -31,633 (9), 81: -31,733 (11), 132: -31,783 (3), 83: -31,875 (59), 123: -31,910 (11), 147: -31,970 (4), 133: -32,096 (5), 149: -32,176 (3), 102: -32,186 (24), 115: -32,225 (13), 95: -32,256 (20), 68: -32,262 (5), 127: -32,351 (15), 113: -32,399 (5), 57: -32,707 (4), 122: -32,756 (25), 136: -32,828 (4), 107: -32,870 (8), 79: -32,875 (10), 91: -33,031 (27), 78: -33,040 (13), 71: -33,052 (13), 97: -33,069 (37), 104: -33,078 (284), 87: -33,122 (9), 90: -33,285 (12), 119: -33,289 (10), 82: -33,299 (7), 89: -33,375 (98), 67: -33,385 (2), 99: -33,442 (14), 112: -33,448 (166), 59: -33,500 (3), 74: -33,503 (15), 135: -33,595 (329), 53: -33,612 (2), 108: -33,612 (13), 80: -33,670 (5), 109: -33,765 (12), 103: -33,858 (12), 88: -33,860 (38), 96: -33,998 (23), 143: -34,119 (9), 101: -34,252 (13), 124: -34,377 (19), 116: -34,676 (26), 126: -34,779 (13), 150: -34,796 (116), 137: -35,004 (2), 128: -35,152 (7), 106: -35,167 (22), 84: -35,174 (11), 75: -35,327 (45), 110: -35,350 (13), 98: -35,577 (15), 117: -35,669 (28), 121: -35,829 (6), 77: -36,010 (9), 134: -36,023 (6), 118: -36,177 (6), 52: -36,201 (4), 142: -36,268 (7), 148: -36,528 (3), 51: -37,500 (2), 72: -37,708 (6), 131: -37,838 (9), 73: -37,893 (4), 139: -38,005 (6), 50: -38,020 (15), 54: -39,448 (3), 60: -39,567 (5), 140: -40,282 (2), 145: -40,643 (10), 58: -41,540 (2) |
| wheat_cap | 11,706 | 14 | 18 | 14: -28,132 (10), 21: -30,407 (846), 20: -30,964 (386), 22: -30,966 (2455), 23: -31,883 (233), 17: -32,120 (451), 25: -32,806 (626), 12: -32,981 (6), 16: -33,094 (41), 18: -33,293 (324), 9: -33,622 (35), 24: -33,737 (213), 19: -34,121 (83), 15: -34,161 (30), 10: -34,594 (57), 13: -35,733 (10), 11: -36,937 (29), 7: -37,056 (19), 5: -38,364 (15), 6: -38,904 (2), 8: -39,838 (3) |
| CROP_SWEEP_LEN | 11,677 | 6 | 6 | 6: -30,926 (5072), 5: -35,025 (288), 7: -35,843 (253), 4: -37,148 (147), 3: -37,671 (62), 8: -38,689 (35), 9: -41,396 (14), 10: -42,603 (3) |
| wheat_tiles | 11,607 | 0 | 0 | 0: -31,264 (5246), 1: -34,199 (344), 7: -34,992 (2), 2: -35,339 (122), 3: -35,417 (116), 4: -35,617 (22), 5: -36,410 (14), 6: -37,473 (6), 8: -42,871 (2) |
| MAX_HANDS | 11,511 | 14 | 13 | 14: -30,597 (353), 12: -31,530 (1144), 13: -31,606 (3645), 11: -31,697 (464), 15: -31,840 (128), 10: -35,091 (54), 16: -35,293 (68), 9: -38,115 (10), 8: -42,108 (8) |
| wheat_per_animal | 11,481 | 0.0 | 0.0 | 0.0: -31,073 (4683), 0.1: -33,081 (632), 0.2: -33,985 (376), 1.1: -34,046 (2), 0.5: -34,490 (14), 0.4: -35,621 (43), 0.3: -36,184 (69), 0.7: -37,260 (13), 0.6: -37,263 (10), 1.0: -37,474 (20), 0.9: -39,381 (2), 1.2: -39,783 (7), 0.8: -42,554 (3) |
| MELON_MAX_TILES | 10,898 | 38 | 40 | 38: -29,189 (601), 43: -30,337 (1791), 33: -30,647 (30), 37: -30,811 (113), 34: -30,866 (73), 46: -31,148 (40), 49: -31,356 (140), 32: -31,640 (23), 31: -31,945 (18), 44: -32,148 (103), 28: -32,158 (7), 35: -32,265 (120), 45: -32,277 (181), 40: -32,821 (1930), 36: -33,003 (118), 47: -33,211 (77), 50: -33,442 (160), 41: -33,540 (40), 42: -33,815 (125), 39: -34,038 (84), 30: -34,211 (11), 48: -35,061 (28), 29: -35,270 (9), 20: -35,462 (15), 24: -36,058 (20), 23: -36,659 (3), 27: -37,083 (3), 22: -39,119 (2), 26: -40,087 (8) |
| wheat_sell_price | 10,552 | 25 | 30 | 25: -30,769 (2564), 30: -31,080 (1879), 26: -31,257 (186), 27: -32,667 (111), 29: -33,425 (58), 31: -33,827 (54), 28: -34,023 (662), 44: -34,154 (3), 35: -34,433 (141), 50: -34,765 (2), 38: -35,517 (12), 40: -35,635 (5), 34: -35,931 (30), 32: -36,151 (57), 37: -36,385 (15), 33: -36,389 (61), 39: -36,586 (8), 36: -39,255 (18), 46: -39,707 (2), 43: -41,320 (3) |
| demand_share | 10,363 | 0.55 | 0.5 | 0.55: -29,793 (2035), 0.65: -31,649 (860), 0.75: -32,144 (32), 0.5: -32,191 (2241), 0.6: -32,536 (172), 0.7: -33,628 (81), 0.9: -33,980 (6), 0.8: -34,064 (19), 0.45: -35,058 (176), 0.85: -36,289 (8), 0.35: -36,359 (85), 0.4: -36,494 (67), 0.95: -37,587 (2), 1.0: -39,830 (5), 0.3: -40,156 (85) |
| open_melons | 9,786 | 10 | 8 | 10: -30,691 (4584), 7: -33,665 (161), 9: -34,524 (304), 8: -34,917 (630), 6: -35,205 (84), 5: -37,023 (7), 11: -38,458 (31), 4: -38,631 (14), 12: -38,759 (25), 14: -39,129 (20), 13: -40,478 (14) |
| open_wheat | 9,260 | 7 | 7 | 7: -30,850 (5069), 5: -36,185 (38), 6: -36,259 (468), 8: -36,876 (172), 10: -36,933 (67), 9: -38,411 (37), 4: -39,233 (18), 3: -40,110 (5) |
| open_sheep | 8,355 | 2 | 2 | 2: -31,346 (5592), 1: -37,024 (222), 3: -38,952 (27), 0: -39,701 (33) |
| setup_capital_share | 8,010 | 0.05 | 0.25 | 0.05: -29,792 (526), 0.1: -31,290 (166), 0.2: -31,619 (297), 0.25: -31,622 (4158), 0.15: -31,709 (168), 0.0: -32,335 (162), 0.4: -32,750 (77), 0.3: -33,503 (127), 0.45: -33,905 (26), 0.35: -34,516 (124), 0.5: -37,802 (43) |
| open_cows | 7,779 | 2 | 2 | 2: -31,239 (5490), 1: -37,316 (362), 3: -39,019 (22) |
| opening | 7,611 | frontier | frontier | frontier: -31,262 (5580), v312: -38,873 (294) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=946)
- (10, 3, 6): -16,840 (n=848)
- (8, 3, 5): -17,352 (n=159)
- (11, 3, 6): -18,175 (n=228)
- (9, 3, 6): -18,255 (n=593)
- (12, 4, 6): -18,258 (n=257)
- (8, 3, 6): -18,403 (n=414)
- (11, 4, 6): -19,867 (n=301)
- (17, 3, 6): -20,338 (n=42)
- (10, 4, 6): -20,442 (n=738)
- (8, 4, 6): -21,051 (n=312)
- (13, 4, 6): -21,868 (n=64)
- (10, 3, 5): -22,188 (n=20)
- (13, 3, 6): -22,519 (n=138)
- (9, 3, 5): -23,138 (n=67)

_Generated 2026-09-07 00:53. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._