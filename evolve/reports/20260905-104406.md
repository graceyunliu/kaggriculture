# Evolution run 20260905-104406

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105739218.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.23 h · candidates evaluated this run: 1380 · games 30,770 (13,803/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 126 | 252 |
| dead_pattern | 319 | 638 |
| dead_smoke | 375 | 3000 |
| alive | 560 | 26880 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 1678 · held-out evaluated: 0 · held-out PASS: 0

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
| `8c1ad3488ef5` | queue | archive_crossover:crossover_g000650_20260905-093236_0 | -18,175 | -3.5 | 2-8 | -18,665 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→1, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→48, MAX_HANDS 13→11, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `bbd280ca046a` | queue | mutate | -18,881 | -4.2 | 1-9 | -22,986 | alive | harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, fert_buy 0→1, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `7bce39e0e86b` | queue | archive_crossover:crossover_g001175_20260905-121607_1 | -19,105 | -4.0 | 1-9 | -20,572 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, fert_buy 0→1, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `746fcc05fb48` | queue | archive_crossover:crossover_g000850_20260905-114845_1 | -19,426 | -5.2 | 1-9 | -18,299 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, feed_spare_poor 0→1, fert_buy 0→1, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25 |
| `51907bbad59d` | queue | archive_crossover:crossover_g000625_20260905-113010_0 | -19,697 | -4.1 | 1-9 | -25,273 | alive | melon_floor 150→200, harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_buy 0→1, wheat_cap 18→21, labor_reserve_buffer 50→48, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `f7948c8a5256` | queue | mutate | -19,867 | -4.8 | 1-9 | -24,035 | alive | melon_floor 150→0, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, fert_carry 3→2, demand_share 0.5→0.65, wheat_cap 18→17, wheat_sell_price 30→26, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5 |
| `0daaee1d5f3c` | queue | archive_crossover:crossover_g000875_20260905-115023_0 | -20,005 | -4.8 | 1-9 | -20,306 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, fert_carry 3→2, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `56d7c3b42124` | queue | crossover | -20,035 | -5.5 | 1-9 | -22,963 | alive | melon_floor 150→200, harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_buy 0→1, wheat_cap 18→21, labor_reserve_buffer 50→48, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `d5c7f1c7464c` | v312 | migrate | -20,119 | -5.5 | 1-9 | -18,203 | alive | load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→1, demand_share 0.5→0.65, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→11, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, OPENING_MELONS 10→8, SPREAD_W 1.0→1.5 |
| `db7241c2664f` | queue | mutate | -20,121 | -4.3 | 1-9 | -25,275 | alive | harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_buy 0→1, wheat_cap 18→21, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `ae85c94c987f` | queue | crossover | -20,169 | -4.5 | 1-9 | -11,036 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_buy 0→1, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→48, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→2, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `11f9cc8d7153` | queue | mutate | -20,235 | -4.4 | 1-9 | -12,360 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, fert_buy 0→2, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→48, CROP_SWEEP_RADIUS 4→5, MELON_PRICE_CUSHION 100→97, NEAR_RADIUS 3→2, OPP_GROWTH 1.3→1.2, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `981b986c4959` | queue | crossover | -20,440 | -5.2 | 1-9 | -20,890 | alive | melon_floor 150→0, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, demand_share 0.5→0.65, wheat_cap 18→22, wheat_sell_price 30→25, labor_reserve_buffer 50→48, MAX_HANDS 13→11, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `fc62e8b054d1` | c1 | migrate | -20,522 | -4.6 | 2-8 | -17,498 | alive | harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→2, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→61, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `9c957ee08e31` | c1 | mutate | -20,545 | -4.8 | 1-9 | -17,981 | alive | melon_floor 150→100, harvest_min 2→1, load_per_hand 20→19, open_melons 8→10, feed_spare_poor 0→2, fert_buy 0→1, fert_carry 3→1, demand_share 0.5→0.65, wheat_cap 18→22, labor_reserve_buffer 50→40, MAX_HANDS 13→14, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, HERD_LAST_DAY 19→17, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.5, MAX_SHEEP 12→14, OPENING_MELONS 10→8, SPREAD_W 1.0→1.5 |

## Islands (best dev margin, population size)

- c1: best -20,522 (`fc62e8b054d1`), n=411
- queue: best -18,175 (`8c1ad3488ef5`), n=557
- v312: best -20,119 (`d5c7f1c7464c`), n=440
- wide: best -23,805 (`fb31312e8e07`), n=270

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| labor_reserve_buffer | 15,237 | 85 | 50 | 85: -26,525 (2), 33: -28,143 (10), 61: -29,045 (16), 62: -29,901 (6), 48: -29,980 (92), 111: -30,231 (2), 88: -30,658 (3), 18: -30,924 (12), 34: -31,122 (3), 39: -31,409 (16), 93: -31,438 (4), 6: -31,439 (3), 94: -31,624 (7), 58: -31,625 (10), 28: -31,730 (8), 36: -31,854 (6), 38: -31,919 (3), 50: -32,310 (610), 70: -32,348 (3), 45: -32,432 (4), 42: -32,689 (229), 4: -32,840 (31), 40: -32,881 (9), 44: -32,898 (7), 60: -33,246 (4), 84: -33,292 (5), 15: -33,504 (2), 100: -33,529 (16), 30: -33,586 (2), 69: -33,614 (8), 0: -33,762 (33), 56: -33,903 (2), 46: -33,996 (10), 13: -34,125 (3), 73: -34,175 (3), 83: -34,426 (18), 77: -34,464 (135), 31: -34,481 (3), 27: -34,688 (2), 99: -34,805 (44), 29: -34,858 (2), 110: -34,863 (2), 82: -34,938 (8), 43: -34,954 (3), 24: -35,284 (3), 68: -35,578 (2), 81: -35,646 (15), 129: -35,671 (27), 47: -35,770 (8), 21: -35,947 (2), 55: -36,136 (110), 65: -36,217 (6), 3: -36,240 (2), 16: -36,576 (9), 49: -36,602 (2), 10: -36,663 (2), 76: -36,709 (2), 64: -36,899 (4), 11: -36,900 (10), 66: -36,978 (6), 97: -37,411 (5), 101: -37,913 (6), 32: -37,968 (2), 145: -38,218 (4), 14: -38,347 (2), 87: -38,817 (3), 67: -39,139 (3), 12: -39,255 (3), 150: -40,588 (8), 23: -40,650 (3), 57: -41,762 (2) |
| wheat_stock | 13,360 | 6 | 0 | 6: -29,931 (3), 9: -30,453 (34), 4: -31,556 (6), 0: -32,980 (1446), 8: -33,547 (10), 1: -33,873 (76), 10: -34,526 (8), 23: -35,381 (3), 5: -35,400 (16), 7: -35,436 (11), 3: -35,574 (15), 11: -35,612 (6), 13: -36,660 (5), 2: -36,715 (10), 18: -38,354 (3), 15: -38,394 (5), 20: -38,590 (4), 29: -38,803 (2), 12: -39,982 (3), 14: -40,160 (2), 40: -41,450 (5), 33: -43,291 (2) |
| MELON_PRICE_CUSHION | 13,309 | 93 | 100 | 93: -26,930 (2), 74: -27,233 (4), 86: -27,522 (2), 65: -28,144 (2), 66: -29,961 (6), 76: -29,967 (6), 92: -30,429 (2), 111: -30,438 (8), 105: -30,665 (4), 122: -30,869 (2), 94: -31,525 (2), 99: -31,620 (4), 147: -31,965 (2), 100: -32,106 (879), 129: -32,284 (6), 130: -32,409 (4), 126: -32,523 (4), 85: -32,947 (3), 112: -32,992 (77), 71: -33,131 (8), 97: -33,158 (13), 83: -33,331 (10), 119: -33,429 (2), 102: -33,572 (15), 106: -33,676 (7), 89: -33,783 (71), 88: -33,922 (28), 95: -34,003 (12), 87: -34,189 (3), 113: -34,211 (2), 103: -34,228 (5), 116: -34,243 (6), 104: -34,313 (169), 114: -34,320 (2), 70: -34,423 (2), 91: -34,513 (12), 125: -34,802 (6), 135: -35,038 (100), 117: -35,100 (3), 80: -35,199 (2), 143: -35,339 (5), 78: -35,528 (2), 150: -35,534 (36), 75: -35,586 (27), 124: -35,762 (10), 84: -36,147 (3), 96: -36,305 (9), 134: -36,723 (3), 128: -36,829 (3), 90: -36,910 (4), 110: -37,011 (5), 115: -37,245 (4), 109: -37,488 (5), 108: -37,596 (4), 98: -37,717 (7), 72: -38,136 (5), 123: -38,340 (2), 101: -38,340 (2), 73: -38,377 (3), 50: -38,424 (5), 120: -38,552 (2), 77: -38,646 (5), 54: -39,448 (3), 121: -40,006 (2), 139: -40,238 (2) |
| CROP_SWEEP_LEN | 12,874 | 6 | 6 | 6: -32,548 (1361), 5: -34,881 (61), 7: -35,153 (163), 4: -37,264 (42), 3: -37,399 (31), 8: -39,622 (13), 9: -39,769 (5), 10: -45,422 (2) |
| load_per_hand | 12,597 | 19 | 20 | 19: -31,416 (768), 18: -33,201 (47), 17: -33,706 (255), 20: -34,589 (430), 21: -34,746 (76), 24: -36,879 (3), 23: -37,057 (18), 15: -37,416 (12), 14: -37,543 (8), 22: -37,624 (20), 16: -37,688 (19), 25: -37,987 (4), 26: -39,397 (9), 13: -40,334 (3), 12: -44,013 (6) |
| wheat_sell_price | 10,168 | 26 | 30 | 26: -29,733 (70), 25: -32,459 (589), 30: -32,474 (497), 27: -32,636 (26), 38: -33,351 (5), 29: -33,849 (16), 31: -33,874 (27), 35: -34,338 (114), 28: -35,356 (240), 32: -35,726 (20), 37: -36,328 (9), 33: -36,611 (37), 39: -37,281 (4), 34: -37,374 (10), 36: -39,137 (9), 43: -39,901 (2) |
| MELON_MAX_TILES | 10,123 | 43 | 40 | 43: -30,746 (337), 46: -31,196 (4), 49: -31,495 (9), 38: -32,448 (21), 47: -33,028 (41), 36: -33,155 (41), 33: -33,243 (7), 35: -33,328 (41), 40: -33,527 (942), 41: -33,623 (18), 30: -33,652 (4), 32: -34,148 (4), 24: -34,472 (14), 37: -34,774 (7), 48: -35,065 (7), 45: -35,116 (53), 34: -35,233 (13), 50: -35,268 (42), 23: -36,041 (2), 39: -36,115 (31), 44: -36,455 (19), 26: -37,145 (4), 42: -38,509 (10), 20: -40,868 (3) |
| open_melons | 9,880 | 10 | 8 | 10: -31,774 (939), 9: -33,891 (166), 8: -34,885 (453), 6: -35,361 (40), 7: -35,778 (41), 11: -37,638 (11), 14: -38,518 (9), 4: -40,296 (6), 13: -40,512 (5), 12: -41,654 (8) |
| demand_share | 9,634 | 0.65 | 0.5 | 0.65: -31,120 (284), 0.55: -31,966 (271), 0.6: -33,164 (70), 0.5: -33,432 (865), 0.75: -33,755 (11), 0.8: -33,973 (4), 0.85: -34,959 (4), 0.45: -35,862 (65), 0.4: -36,396 (11), 0.7: -36,790 (16), 0.35: -37,892 (53), 1.0: -38,636 (2), 0.3: -40,755 (20) |
| MAX_HANDS | 7,935 | 12 | 13 | 12: -31,642 (368), 11: -32,169 (120), 13: -33,543 (1074), 14: -33,615 (38), 15: -35,492 (24), 10: -35,561 (21), 16: -38,486 (25), 8: -39,449 (3), 9: -39,577 (5) |
| wheat_per_animal | 7,456 | 0.1 | 0.0 | 0.1: -32,673 (334), 0.0: -32,819 (1018), 0.2: -33,951 (242), 0.6: -35,774 (5), 0.3: -36,933 (25), 0.7: -36,937 (7), 1.0: -37,205 (17), 0.5: -37,542 (5), 0.4: -38,205 (17), 0.9: -39,381 (2), 1.2: -40,129 (4) |
| wheat_cap | 7,054 | 21 | 18 | 21: -30,555 (80), 20: -30,880 (154), 16: -32,453 (17), 22: -32,617 (700), 17: -33,115 (100), 18: -33,731 (166), 23: -33,937 (31), 15: -34,253 (5), 24: -34,771 (55), 25: -34,833 (243), 19: -35,104 (28), 10: -35,569 (34), 9: -36,105 (8), 7: -36,199 (11), 13: -36,717 (7), 12: -36,832 (2), 11: -37,390 (24), 5: -37,609 (10) |
| HERD_LAST_DAY | 6,968 | 17 | 19 | 17: -31,628 (78), 19: -32,442 (1073), 18: -33,007 (132), 20: -34,666 (69), 21: -34,740 (28), 22: -34,812 (96), 16: -35,592 (146), 14: -38,300 (49), 15: -38,596 (7) |
| open_wheat | 6,870 | 7 | 7 | 7: -32,636 (1417), 6: -35,333 (147), 5: -36,534 (12), 8: -36,757 (53), 10: -36,894 (29), 4: -39,272 (7), 9: -39,506 (13) |
| STRAW_CUTOFF | 6,851 | 16 | 17 | 16: -32,352 (209), 17: -32,962 (1190), 14: -33,297 (12), 18: -33,727 (151), 19: -33,962 (32), 15: -35,883 (32), 13: -36,329 (3), 20: -37,643 (38), 12: -39,203 (11) |
| max_animals | 6,630 | 19 | 20 | 19: -32,903 (43), 18: -32,932 (73), 20: -32,997 (1265), 16: -33,512 (24), 17: -33,831 (243), 14: -33,846 (6), 13: -35,569 (5), 15: -36,991 (14), 12: -39,533 (4) |
| opening | 6,598 | frontier | frontier | frontier: -32,780 (1575), v312: -39,378 (103) |
| open_sheep | 6,402 | 2 | 2 | 2: -32,888 (1564), 1: -36,725 (88), 3: -38,925 (18), 0: -39,291 (8) |
| wheat_tiles | 6,327 | 0 | 0 | 0: -32,870 (1449), 1: -33,505 (120), 2: -36,165 (48), 5: -37,371 (4), 3: -37,378 (45), 6: -37,574 (5), 4: -39,197 (5) |
| MAX_SHEEP | 6,251 | 14 | 12 | 14: -32,592 (1277), 13: -33,335 (62), 12: -34,311 (152), 6: -34,621 (2), 11: -35,303 (39), 10: -36,333 (113), 7: -36,696 (5), 8: -36,985 (21), 9: -38,843 (6) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (11, 3, 6): -18,175 (n=69)
- (8, 3, 6): -18,881 (n=149)
- (8, 3, 5): -19,697 (n=58)
- (11, 4, 6): -19,867 (n=106)
- (10, 3, 6): -20,169 (n=196)
- (17, 3, 6): -21,132 (n=10)
- (10, 4, 6): -21,203 (n=210)
- (12, 4, 6): -21,695 (n=123)
- (13, 3, 6): -22,519 (n=57)
- (9, 3, 6): -22,897 (n=147)
- (14, 3, 6): -23,164 (n=19)
- (8, 3, 4): -23,525 (n=22)
- (8, 4, 6): -23,823 (n=77)
- (8, 4, 5): -23,880 (n=9)
- (9, 4, 6): -24,181 (n=167)

_Generated 2026-09-05 12:57. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._