# Evolution run 20260907-005650

Frontier opponent: `H32.py` · clone: `tape_mengfeili_105887030.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.09 h · candidates evaluated this run: 1374 · games 30,714 (14,668/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 321 | 642 |
| dead_pattern | 272 | 544 |
| dead_smoke | 199 | 1592 |
| alive | 582 | 27936 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 6456 · held-out evaluated: 0 · held-out PASS: 0

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
| `12753350f904` | queue | archive_crossover:crossover_g000200_20260906-230552_0 | -16,054 | -3.2 | 2-8 | -14,640 | alive | open_melons 8→10, early_hire_days 5→3, fert_buy 0→3, fert_carry 3→2, demand_share 0.5→0.55, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→19, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_W 1.0→1.5 |

## Islands (best dev margin, population size)

- H32: best -15,269 (`0c3989f7d742`), n=530
- M2: best -16,932 (`8aea624a62b9`), n=535
- c1: best -16,310 (`23734cef4da1`), n=1293
- queue: best -15,412 (`fe4745b56024`), n=1785
- v312: best -15,854 (`2286322870c4`), n=1279
- wide: best -16,047 (`512e53fe15bc`), n=1034

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| labor_reserve_buffer | 14,981 | 71 | 50 | 71: -24,623 (8), 72: -26,442 (3), 5: -27,446 (12), 92: -27,492 (46), 26: -27,805 (3), 112: -28,023 (5), 86: -28,304 (3), 35: -28,345 (3), 49: -28,431 (21), 58: -28,526 (35), 27: -28,672 (30), 9: -28,701 (6), 63: -29,024 (39), 96: -29,425 (4), 90: -29,514 (3), 18: -29,782 (303), 65: -30,014 (66), 61: -30,208 (67), 136: -30,224 (16), 85: -30,266 (6), 89: -30,502 (9), 33: -30,650 (16), 48: -30,662 (346), 50: -30,725 (3127), 56: -30,766 (5), 36: -30,825 (29), 59: -31,138 (9), 144: -31,182 (2), 73: -31,318 (9), 24: -31,352 (11), 60: -31,419 (18), 93: -31,438 (4), 74: -31,509 (34), 40: -31,550 (70), 115: -31,553 (4), 80: -31,689 (8), 42: -31,726 (415), 45: -31,840 (69), 51: -31,859 (8), 25: -31,865 (4), 57: -31,948 (71), 62: -32,239 (12), 14: -32,290 (5), 38: -32,370 (11), 39: -32,417 (47), 70: -32,434 (16), 52: -32,588 (6), 28: -32,609 (14), 30: -32,622 (5), 104: -32,627 (3), 76: -32,720 (7), 88: -32,733 (7), 78: -32,765 (5), 44: -32,810 (11), 84: -32,873 (9), 83: -32,882 (73), 43: -32,937 (14), 4: -33,260 (34), 150: -33,324 (22), 119: -33,340 (2), 111: -33,417 (5), 103: -33,494 (5), 0: -33,553 (115), 66: -33,633 (25), 6: -33,635 (9), 55: -33,653 (347), 19: -33,712 (4), 94: -33,747 (11), 13: -34,071 (4), 34: -34,164 (27), 69: -34,177 (9), 21: -34,457 (4), 134: -34,464 (2), 54: -34,486 (9), 91: -34,507 (4), 31: -34,821 (6), 99: -34,830 (59), 22: -35,000 (12), 7: -35,029 (4), 82: -35,067 (17), 41: -35,071 (16), 77: -35,073 (186), 100: -35,121 (28), 47: -35,128 (12), 29: -35,175 (7), 81: -35,249 (19), 32: -35,252 (7), 53: -35,432 (14), 46: -35,449 (18), 129: -35,513 (65), 10: -35,579 (10), 87: -35,642 (6), 79: -35,703 (3), 107: -35,804 (3), 97: -36,084 (9), 106: -36,115 (2), 101: -36,200 (7), 110: -36,353 (3), 98: -36,464 (2), 3: -36,531 (5), 23: -36,562 (7), 16: -36,603 (10), 109: -36,655 (2), 145: -36,990 (7), 11: -36,993 (11), 15: -37,056 (3), 114: -37,370 (3), 68: -37,515 (5), 64: -37,573 (11), 1: -37,771 (3), 12: -37,835 (6), 67: -37,954 (14), 102: -38,189 (3), 37: -39,604 (4) |
| wheat_stock | 14,125 | 0 | 0 | 0: -31,180 (5713), 9: -31,260 (61), 6: -31,765 (35), 17: -32,496 (4), 1: -32,647 (182), 19: -32,857 (3), 4: -33,551 (36), 8: -33,749 (35), 2: -33,802 (45), 16: -33,966 (3), 5: -34,265 (50), 11: -34,871 (25), 3: -34,985 (109), 13: -36,032 (14), 7: -36,079 (37), 28: -36,361 (2), 15: -36,498 (13), 10: -36,565 (21), 14: -36,808 (11), 20: -36,836 (5), 23: -37,081 (5), 12: -37,341 (13), 18: -38,053 (9), 21: -38,105 (3), 39: -38,737 (3), 29: -40,147 (7), 40: -41,450 (5), 33: -42,526 (4), 26: -45,305 (2) |
| load_per_hand | 13,494 | 20 | 20 | 20: -30,375 (2595), 19: -31,144 (2781), 18: -32,476 (142), 17: -34,306 (506), 21: -36,083 (151), 16: -36,869 (64), 23: -37,026 (34), 15: -37,232 (33), 22: -37,527 (54), 14: -38,359 (18), 24: -38,427 (23), 25: -38,453 (14), 26: -39,363 (21), 13: -40,253 (12), 12: -43,869 (8) |
| MELON_PRICE_CUSHION | 12,880 | 63 | 100 | 63: -28,660 (4), 65: -29,086 (4), 85: -29,384 (58), 69: -29,694 (3), 130: -29,707 (9), 86: -30,070 (189), 93: -30,241 (144), 94: -30,349 (8), 62: -30,527 (2), 100: -30,613 (3886), 70: -30,641 (11), 67: -30,734 (4), 66: -30,750 (10), 111: -30,770 (23), 64: -30,911 (7), 125: -30,969 (62), 114: -30,980 (16), 141: -31,181 (2), 92: -31,252 (8), 113: -31,254 (8), 115: -31,291 (15), 129: -31,340 (10), 105: -31,381 (43), 120: -31,382 (7), 78: -31,683 (17), 132: -31,783 (3), 83: -31,800 (64), 82: -31,945 (10), 147: -31,970 (4), 133: -32,096 (5), 95: -32,110 (22), 149: -32,176 (3), 71: -32,246 (14), 68: -32,262 (5), 102: -32,287 (25), 127: -32,373 (16), 76: -32,386 (10), 90: -32,536 (13), 122: -32,575 (26), 57: -32,707 (4), 109: -32,815 (14), 136: -32,828 (4), 81: -32,850 (19), 123: -32,877 (13), 91: -32,916 (30), 79: -33,029 (13), 74: -33,033 (16), 97: -33,041 (38), 103: -33,047 (13), 104: -33,094 (300), 87: -33,122 (9), 119: -33,267 (11), 89: -33,311 (102), 88: -33,375 (41), 99: -33,442 (14), 112: -33,445 (167), 53: -33,612 (2), 108: -33,612 (13), 135: -33,655 (344), 143: -33,776 (10), 107: -33,843 (9), 59: -33,898 (4), 116: -34,177 (30), 96: -34,296 (26), 101: -34,359 (16), 124: -34,377 (19), 98: -34,658 (16), 126: -34,779 (13), 150: -34,839 (122), 80: -34,941 (7), 137: -35,004 (2), 106: -35,074 (24), 117: -35,142 (30), 128: -35,152 (7), 84: -35,174 (11), 75: -35,327 (45), 110: -35,350 (13), 121: -35,638 (7), 134: -36,023 (6), 52: -36,201 (4), 142: -36,268 (7), 77: -36,455 (10), 148: -36,528 (3), 118: -36,866 (8), 51: -37,500 (2), 72: -37,708 (6), 50: -37,796 (16), 131: -37,838 (9), 73: -37,893 (4), 139: -38,005 (6), 54: -39,448 (3), 60: -39,567 (5), 140: -40,282 (2), 145: -40,643 (10), 58: -41,540 (2) |
| max_animals | 12,714 | 14 | 20 | 14: -30,460 (54), 17: -30,763 (1508), 16: -31,473 (168), 18: -31,653 (301), 20: -31,709 (4117), 19: -32,006 (237), 13: -34,262 (16), 15: -34,759 (41), 12: -37,278 (8), 10: -43,175 (5) |
| ROUTE_LEN | 11,920 | 3 | 3 | 3: -30,963 (5810), 2: -36,280 (473), 4: -36,997 (166), 5: -42,883 (7) |
| CROP_SWEEP_LEN | 11,803 | 6 | 6 | 6: -30,800 (5600), 5: -35,076 (312), 7: -35,877 (260), 4: -37,323 (161), 3: -37,783 (70), 8: -38,530 (36), 9: -41,396 (14), 10: -42,603 (3) |
| wheat_cap | 11,706 | 14 | 18 | 14: -28,132 (10), 21: -30,419 (945), 22: -30,828 (2766), 20: -30,885 (403), 23: -31,484 (265), 17: -32,085 (477), 25: -32,687 (673), 16: -32,945 (45), 12: -32,981 (6), 18: -33,228 (341), 24: -33,760 (228), 9: -34,020 (38), 19: -34,243 (89), 15: -34,244 (31), 10: -34,594 (57), 13: -35,733 (10), 5: -36,721 (19), 11: -36,937 (29), 7: -37,056 (19), 6: -38,904 (2), 8: -39,838 (3) |
| wheat_per_animal | 11,610 | 0.0 | 0.0 | 0.0: -30,944 (5205), 0.1: -33,139 (656), 1.1: -34,046 (2), 0.2: -34,065 (395), 0.5: -34,966 (21), 0.4: -35,329 (48), 0.3: -35,817 (73), 0.7: -37,204 (14), 0.6: -37,263 (10), 1.0: -37,474 (20), 0.9: -39,381 (2), 1.2: -39,783 (7), 0.8: -42,554 (3) |
| MAX_HANDS | 11,045 | 14 | 13 | 14: -30,489 (452), 13: -31,479 (4012), 12: -31,492 (1206), 11: -31,708 (481), 15: -31,831 (144), 16: -33,945 (82), 10: -34,510 (59), 9: -37,889 (11), 8: -41,534 (9) |
| MELON_MAX_TILES | 10,843 | 38 | 40 | 38: -29,244 (771), 43: -30,306 (1960), 34: -30,313 (89), 33: -30,370 (33), 37: -30,455 (144), 28: -30,859 (10), 49: -31,172 (160), 46: -31,461 (42), 31: -31,670 (20), 44: -31,748 (119), 32: -32,199 (28), 25: -32,322 (3), 45: -32,384 (198), 35: -32,553 (128), 40: -32,797 (1989), 30: -32,915 (13), 36: -33,053 (120), 39: -33,163 (106), 47: -33,322 (81), 50: -33,325 (173), 42: -33,543 (132), 41: -33,579 (45), 20: -35,056 (16), 29: -35,270 (9), 48: -35,290 (31), 24: -36,058 (20), 23: -36,659 (3), 27: -37,083 (3), 22: -39,119 (2), 26: -40,087 (8) |
| wheat_sell_price | 10,643 | 25 | 30 | 25: -30,677 (2875), 30: -30,947 (2071), 26: -31,189 (200), 27: -32,872 (122), 29: -33,261 (62), 31: -33,562 (58), 28: -33,996 (688), 44: -34,154 (3), 35: -34,550 (147), 50: -35,422 (3), 38: -35,517 (12), 32: -35,767 (64), 34: -35,947 (32), 33: -36,277 (63), 40: -36,568 (6), 39: -36,586 (8), 37: -36,820 (16), 36: -39,255 (18), 46: -39,707 (2), 43: -41,320 (3) |
| demand_share | 10,277 | 0.55 | 0.5 | 0.55: -29,716 (2414), 0.65: -31,634 (881), 0.5: -32,135 (2347), 0.75: -32,217 (35), 0.6: -32,445 (184), 0.7: -33,029 (97), 0.8: -34,064 (19), 0.9: -34,710 (7), 0.45: -35,066 (193), 0.85: -36,289 (8), 0.4: -36,332 (80), 0.35: -36,396 (88), 0.95: -37,587 (2), 1.0: -39,830 (5), 0.3: -39,993 (96) |
| open_melons | 9,655 | 10 | 8 | 10: -30,597 (5100), 7: -33,113 (179), 9: -34,587 (313), 8: -35,005 (655), 6: -35,264 (92), 5: -36,987 (8), 12: -38,385 (27), 11: -38,431 (33), 4: -38,631 (14), 14: -39,129 (20), 13: -40,252 (15) |
| wheat_tiles | 9,525 | 0 | 0 | 0: -31,133 (5780), 1: -34,274 (361), 2: -35,194 (141), 3: -35,406 (121), 4: -35,698 (27), 5: -36,410 (14), 7: -36,854 (3), 6: -37,473 (6), 8: -40,658 (3) |
| open_wheat | 9,374 | 7 | 7 | 7: -30,736 (5600), 5: -36,185 (38), 6: -36,370 (500), 8: -36,754 (185), 10: -36,883 (69), 9: -38,236 (41), 4: -39,233 (18), 3: -40,110 (5) |
| open_sheep | 8,881 | 2 | 2 | 2: -31,227 (6157), 1: -37,013 (234), 3: -38,976 (28), 0: -40,108 (37) |
| setup_capital_share | 7,993 | 0.05 | 0.25 | 0.05: -29,779 (642), 0.2: -31,210 (344), 0.15: -31,326 (202), 0.1: -31,507 (192), 0.25: -31,543 (4472), 0.0: -32,019 (189), 0.4: -32,832 (78), 0.3: -33,452 (131), 0.45: -34,200 (27), 0.35: -34,239 (134), 0.5: -37,772 (45) |
| opening | 7,714 | frontier | frontier | frontier: -31,147 (6143), v312: -38,861 (313) |
| open_cows | 7,571 | 2 | 2 | 2: -31,116 (6041), 1: -37,342 (391), 3: -38,687 (24) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 4, 6): -15,269 (n=1095)
- (10, 3, 6): -16,840 (n=939)
- (8, 3, 5): -17,352 (n=166)
- (12, 4, 6): -17,899 (n=279)
- (10, 4, 6): -17,975 (n=823)
- (11, 3, 6): -18,175 (n=244)
- (9, 3, 6): -18,255 (n=664)
- (8, 3, 6): -18,383 (n=439)
- (11, 4, 6): -19,867 (n=311)
- (17, 3, 6): -20,338 (n=43)
- (8, 4, 6): -21,051 (n=340)
- (13, 4, 6): -21,868 (n=66)
- (10, 3, 5): -22,188 (n=24)
- (13, 3, 6): -22,519 (n=147)
- (9, 3, 5): -23,138 (n=74)

_Generated 2026-09-07 03:02. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._