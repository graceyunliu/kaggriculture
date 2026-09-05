# Evolution run 20260905-063632

Frontier opponent: `H32.py` · clone: `tape_jessebullard_105739218.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_79463721d15c.py` (sha `79463721d15c`)
Elapsed 2.11 h · candidates evaluated this run: 1385 · games 30,776 (14,578/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 81 | 162 |
| dead_pattern | 323 | 646 |
| dead_smoke | 428 | 3424 |
| alive | 553 | 26544 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 553 · held-out evaluated: 0 · held-out PASS: 0

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
| `d661997d96d0` | queue | mutate | -20,685 | -3.7 | 2-8 | -19,557 | alive | melon_floor 150→200, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→3, demand_share 0.5→0.65, wheat_cap 18→20, wheat_sell_price 30→25, labor_reserve_buffer 50→48, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `170a01ee902c` | queue | archive_crossover:crossover_g001125_20260905-081159_1 | -21,356 | -5.1 | 2-8 | -18,923 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, demand_share 0.5→0.65, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `f69ed515c1c6` | queue | archive_crossover:crossover_g000750_20260905-073920_1 | -21,646 | -4.6 | 0-10 | -23,057 | alive | load_per_hand 20→17, open_melons 8→10, demand_share 0.5→0.55, wheat_per_animal 0.0→0.1, wheat_cap 18→22, wheat_sell_price 30→25, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→6, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_CAP 5→4 |
| `df62a383f60d` | v312 | crossover | -21,737 | -4.4 | 1-9 | -21,515 | alive | load_per_hand 20→17, open_melons 8→10, fert_carry 3→2, demand_share 0.5→0.55, max_animals 20→17, wheat_per_animal 0.0→0.1, wheat_cap 18→22, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→6, STRAW_CUTOFF 17→16, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, SPREAD_CAP 5→4 |
| `69eb191aec38` | queue | archive_crossover:crossover_g000900_20260905-075354_0 | -21,820 | -4.5 | 1-9 | -21,398 | alive | load_per_hand 20→19, open_melons 8→10, wheat_per_animal 0.0→0.2, wheat_cap 18→22, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→3 |
| `6d3f139e0f72` | queue | mutate | -21,856 | -4.9 | 1-9 | -23,546 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, fert_carry 3→2, demand_share 0.5→0.65, wheat_cap 18→22, CROP_SWEEP_RADIUS 4→5, MELON_MAX_TILES 40→43, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, SPREAD_W 1.0→1.5 |
| `52edba67ea74` | queue | archive_crossover:crossover_g000300_20260905-070145_0 | -22,757 | -4.8 | 1-9 | -26,486 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, wheat_cap 18→22, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→4, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.25 |
| `e81e1271b054` | v312 | crossover | -23,056 | -5.3 | 1-9 | -19,349 | alive | load_per_hand 20→17, open_melons 8→10, fert_keep 0→1, fert_buy 0→2, wheat_per_animal 0.0→0.1, wheat_cap 18→22, labor_reserve_buffer 50→42, CROP_SWEEP_RADIUS 4→6, MELON_PRICE_CUSHION 100→112, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.0, MAX_SHEEP 12→14, OPENING_MELONS 10→11, SPREAD_W 1.0→1.5, SPREAD_CAP 5→4 |
| `f695982d396a` | queue | archive_crossover:crossover_g001025_20260905-080425_0 | -23,059 | -4.5 | 1-9 | -20,923 | alive | load_per_hand 20→17, open_melons 8→10, wheat_per_animal 0.0→0.1, wheat_sell_price 30→25, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→6, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_CAP 5→4 |
| `e787484ce0b4` | queue | mutate | -23,136 | -4.5 | 1-9 | -20,459 | alive | wheat_stock 0→9, load_per_hand 20→19, open_melons 8→10, demand_share 0.5→0.55, max_animals 20→18, wheat_per_animal 0.0→0.1, wheat_cap 18→22, wheat_sell_price 30→25, labor_reserve_buffer 50→42, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.5, MAX_SHEEP 12→14, FERT_RADIUS 2→3, SPREAD_CAP 5→4 |
| `1c2073a3bd53` | queue | crossover | -23,224 | -4.4 | 2-8 | -24,035 | alive | load_per_hand 20→19, open_melons 8→10, early_hire_days 5→4, feed_spare_poor 0→2, wheat_cap 18→22, wheat_sell_price 30→25, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→4, MAX_SHEEP 12→14, SPREAD_W 1.0→1.25, SPREAD_CAP 5→7 |
| `66c0d3f05a80` | queue | archive_crossover:crossover_g000100_20260905-064607_0 | -23,351 | -4.5 | 2-8 | -32,221 | alive | wheat_per_animal 0.0→0.2, wheat_cap 18→22, CROP_SWEEP_RADIUS 4→5, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.1, MAX_SHEEP 12→14, FERT_RADIUS 2→1 |
| `eeafe5b568f4` | queue | mutate | -23,507 | -4.6 | 1-9 | -20,648 | alive | harvest_min 2→3, wheat_stock 0→9, load_per_hand 20→19, open_melons 8→10, demand_share 0.5→0.55, max_animals 20→18, wheat_per_animal 0.0→0.1, wheat_cap 18→22, wheat_sell_price 30→25, labor_reserve_buffer 50→28, MAX_HANDS 13→12, CROP_SWEEP_RADIUS 4→5, STRAW_CUTOFF 17→16, NEAR_RADIUS 3→5, OPP_GROWTH 1.3→1.6, MAX_SHEEP 12→13, FERT_RADIUS 2→3, SPREAD_CAP 5→4 |
| `ae063f3003b1` | queue | archive_crossover:crossover_g000575_20260905-072400_0 | -23,554 | -5.3 | 1-9 | -21,529 | alive | load_per_hand 20→17, open_melons 8→10, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 4→6, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, SPREAD_CAP 5→4 |
| `55d23edcab8d` | v312 | crossover | -23,611 | -5.3 | 1-9 | -32,874 | alive | melon_floor 150→0, load_per_hand 20→17, geese 0→1, open_melons 8→10, fert_keep 0→1, wheat_per_animal 0.0→0.1, CROP_SWEEP_RADIUS 4→6, MELON_MAX_TILES 40→36, MELON_PRICE_CUSHION 100→112, NEAR_RADIUS 3→5, MAX_SHEEP 12→14, OPENING_MELONS 10→11 |

## Islands (best dev margin, population size)

- c1: best -25,794 (`9d7f0ca26f3d`), n=137
- queue: best -20,685 (`d661997d96d0`), n=189
- v312: best -21,737 (`df62a383f60d`), n=144
- wide: best -24,044 (`44ffe249de02`), n=83

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| labor_reserve_buffer | 15,404 | 33 | 50 | 33: -27,624 (3), 28: -28,776 (2), 129: -31,269 (3), 4: -31,777 (19), 93: -32,204 (3), 0: -32,278 (6), 42: -32,369 (58), 82: -32,391 (2), 36: -32,506 (2), 84: -32,988 (2), 50: -33,339 (216), 100: -33,398 (6), 99: -33,529 (21), 69: -33,925 (5), 46: -34,352 (7), 40: -34,858 (7), 73: -35,102 (2), 13: -35,114 (2), 81: -35,636 (11), 77: -35,742 (69), 83: -35,813 (7), 145: -36,108 (2), 94: -37,023 (2), 16: -37,111 (2), 47: -37,194 (6), 101: -37,913 (6), 55: -37,941 (43), 32: -37,968 (2), 87: -38,060 (2), 65: -38,221 (5), 11: -38,509 (4), 150: -40,154 (4), 66: -43,029 (2) |
| MELON_PRICE_CUSHION | 14,261 | 66 | 100 | 66: -27,337 (2), 111: -27,467 (2), 112: -31,419 (18), 129: -32,180 (4), 102: -32,381 (5), 91: -33,036 (5), 88: -33,268 (18), 89: -33,275 (31), 100: -33,619 (281), 71: -34,064 (2), 110: -34,437 (2), 109: -34,974 (2), 75: -35,033 (11), 96: -35,115 (5), 97: -35,221 (5), 124: -35,278 (5), 115: -35,488 (3), 83: -35,666 (3), 77: -35,742 (2), 104: -35,825 (78), 95: -35,835 (7), 135: -36,345 (21), 54: -37,506 (2), 106: -37,579 (4), 50: -37,876 (2), 150: -38,507 (4), 98: -39,730 (2), 72: -39,898 (3), 108: -41,598 (3) |
| wheat_stock | 11,959 | 9 | 0 | 9: -29,552 (14), 6: -30,600 (2), 10: -32,940 (4), 13: -33,943 (2), 7: -34,148 (5), 0: -34,222 (483), 1: -34,645 (15), 3: -35,153 (5), 5: -35,455 (6), 23: -36,136 (2), 2: -36,991 (6), 20: -41,511 (2) |
| MELON_MAX_TILES | 11,878 | 32 | 40 | 32: -31,033 (2), 43: -32,028 (13), 46: -32,763 (3), 39: -32,941 (7), 24: -33,198 (5), 47: -33,272 (11), 41: -33,347 (4), 40: -34,095 (438), 36: -34,119 (7), 35: -34,510 (19), 33: -35,846 (3), 50: -35,909 (11), 44: -36,471 (5), 45: -37,078 (12), 34: -37,147 (4), 42: -41,083 (3), 48: -42,911 (2) |
| early_hire_days | 11,512 | 4 | 5 | 4: -32,915 (111), 7: -33,218 (14), 5: -33,752 (284), 2: -34,453 (6), 3: -35,397 (33), 6: -35,620 (29), 8: -36,498 (65), 0: -41,044 (9), 1: -44,427 (2) |
| demand_share | 10,593 | 0.55 | 0.5 | 0.55: -32,405 (71), 0.75: -33,525 (2), 0.5: -33,816 (381), 0.65: -34,879 (19), 0.6: -35,087 (13), 0.45: -36,823 (24), 0.35: -38,478 (31), 0.7: -39,880 (4), 0.3: -42,998 (6) |
| max_animals | 10,544 | 13 | 20 | 13: -29,698 (2), 18: -32,328 (25), 20: -34,150 (432), 17: -35,067 (67), 19: -35,374 (10), 16: -35,723 (11), 14: -36,080 (2), 12: -40,242 (2) |
| wheat_cap | 10,082 | 9 | 18 | 9: -29,829 (2), 22: -32,945 (254), 18: -33,664 (97), 16: -33,866 (7), 20: -35,371 (22), 24: -35,570 (22), 21: -35,698 (4), 17: -35,838 (10), 10: -36,086 (9), 23: -36,152 (11), 25: -36,350 (82), 15: -36,537 (3), 5: -37,059 (2), 19: -37,757 (11), 11: -37,918 (15), 13: -39,911 (2) |
| fert_carry | 9,689 | 3 | 3 | 3: -33,990 (476), 2: -34,707 (43), 4: -35,969 (17), 1: -37,755 (14), 5: -43,679 (3) |
| load_per_hand | 9,369 | 19 | 20 | 19: -32,891 (170), 18: -33,071 (10), 17: -33,220 (73), 21: -33,706 (28), 20: -34,952 (230), 15: -36,734 (5), 14: -37,204 (3), 16: -37,494 (2), 22: -37,631 (10), 25: -37,987 (4), 23: -38,253 (8), 26: -40,255 (6), 13: -42,260 (2) |
| open_melons | 9,310 | 10 | 8 | 10: -32,489 (183), 9: -34,516 (54), 8: -34,888 (279), 7: -36,840 (19), 6: -37,245 (8), 11: -37,895 (4), 12: -41,799 (4) |
| wheat_per_animal | 9,156 | 0.1 | 0.0 | 0.1: -31,495 (83), 0.2: -33,686 (118), 0.0: -34,761 (319), 0.7: -36,344 (2), 0.5: -36,859 (2), 1.0: -37,741 (9), 0.4: -38,932 (5), 0.3: -38,943 (12), 1.2: -40,651 (2) |
| wheat_sell_price | 9,068 | 26 | 30 | 26: -33,094 (3), 30: -33,328 (201), 38: -33,351 (5), 25: -33,366 (126), 35: -34,288 (61), 37: -34,383 (5), 32: -34,846 (7), 31: -35,500 (11), 28: -36,260 (107), 33: -36,990 (17), 29: -37,069 (4), 36: -42,162 (3) |
| MAX_HANDS | 9,022 | 12 | 13 | 12: -32,923 (44), 13: -33,998 (447), 10: -34,597 (7), 14: -36,207 (8), 15: -36,259 (14), 11: -37,140 (18), 16: -38,804 (11), 9: -41,945 (3) |
| open_wheat | 7,738 | 7 | 7 | 7: -33,926 (482), 10: -34,474 (6), 5: -34,487 (5), 6: -36,188 (41), 8: -36,468 (11), 4: -39,287 (3), 9: -41,664 (5) |
| wheat_tiles | 7,684 | 1 | 0 | 1: -33,618 (41), 0: -34,097 (476), 2: -35,840 (16), 3: -37,253 (16), 4: -41,301 (3) |
| HERD_LAST_DAY | 6,478 | 18 | 19 | 18: -33,028 (28), 19: -33,481 (366), 22: -34,444 (20), 21: -34,885 (12), 20: -35,264 (19), 17: -36,149 (15), 16: -36,241 (64), 14: -38,696 (26), 15: -39,506 (3) |
| CROP_SWEEP_LEN | 6,419 | 6 | 6 | 6: -33,703 (425), 5: -35,015 (14), 7: -35,558 (76), 4: -36,643 (15), 3: -37,458 (15), 8: -38,913 (5), 9: -40,122 (3) |
| open_sheep | 6,182 | 2 | 2 | 2: -33,986 (507), 1: -36,633 (34), 3: -38,434 (9), 0: -40,168 (3) |
| opening | 6,028 | frontier | frontier | frontier: -33,884 (519), v312: -39,912 (34) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (10, 3, 6): -20,685 (n=64)
- (10, 4, 6): -21,646 (n=44)
- (12, 4, 6): -21,820 (n=56)
- (11, 4, 6): -21,856 (n=9)
- (8, 3, 5): -22,757 (n=25)
- (9, 3, 6): -23,351 (n=63)
- (8, 4, 6): -24,378 (n=26)
- (9, 4, 6): -25,794 (n=77)
- (8, 3, 6): -27,109 (n=52)
- (9, 4, 5): -27,783 (n=2)
- (13, 3, 6): -27,920 (n=20)
- (13, 4, 6): -28,108 (n=9)
- (14, 4, 6): -28,498 (n=7)
- (12, 3, 6): -28,500 (n=23)
- (11, 3, 6): -28,572 (n=6)

_Generated 2026-09-05 08:43. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._