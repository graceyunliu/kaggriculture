# Evolution run sandbox-test5

Frontier opponent: `V3_12.py` · clone: `opp_scenario_v14.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_c38b582a1380.py` (sha `c38b582a1380`)
Elapsed 0.01 h · candidates evaluated this run: 6 · games 190 (12,833/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 2 | 2 |
| dead_smoke | 0 | 0 |
| alive | 4 | 188 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 6 · held-out evaluated: 1 · held-out PASS: 1

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | inf | 0-0 | +13,510 | — | — | —-— |
| C1 | +8,847 | 3.5 | 10-0 | +11,447 | +4,793 | 3.6 | 16-4 |

## Held-out results (the only numbers that count)

| key | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 |
|---|---|---:|---:|---:|---:|---:|---|
| `fc180bdf9f5c` | seed:C1 | **+4,793** | 3.6 | 16-4 | +14,637 | +8,847 |  |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---:|---:|---:|---:|---|---|
| `fc180bdf9f5c` | seed:C1 | +8,847 | 3.5 | 10-0 | +11,447 | held_pass |  |
| `08d743bd6116` | crossover | +2,023 | 1.6 | 7-3 | +10,722 | alive | opening frontier→v312, STRAW_CUTOFF 17→18 |
| `4a8752a35e18` | crossover | +1,652 | 1.2 | 6-4 | +12,662 | alive | opening frontier→v312, early_hire_days 5→0 |
| `b75f6ea6245f` | seed:V3_12 | +0 | inf | 0-0 | +13,510 | alive | opening frontier→v312, open_melons 8→12, early_hire_days 5→0, feed_spare_poor 0→3 |
| `22e99bc0cd2b` | mutate | -386 | -0.2 | 3-7 | +9,480 | alive | load_per_hand 20→19, open_cows 2→3, demand_share 0.5→0.45, wheat_sell_price 30→31, ROUTE_LEN 3→2, STRAW_CUTOFF 17→18, NEAR_RADIUS 3→2, OPENING_MELONS 10→9 |
| `2d93f998db84` | mutate | -4,641 | -3.6 | 0-10 | +15,962 | alive | opening frontier→v312, geese 0→1, open_sheep 2→3, max_animals 20→17, wheat_cap 18→14, wheat_hold_days 0→1, MAX_HANDS 13→14, CROP_SWEEP_LEN 6→5, MELON_MAX_TILES 40→49, HERD_LAST_DAY 19→20, MAX_SHEEP 12→14 |

## Where the signal is (mean dev margin by parameter value, all runs)

| param | spread | best value | C1 value | means (value: $, n) |
|---|---:|---|---|---|
| opening | 4,472 | frontier | frontier | frontier: +4,231 (2), v312: -241 (4) |
| STRAW_CUTOFF | 646 | 17 | 17 | 17: +1,464 (4), 18: +819 (2) |
| early_hire_days | 635 | 5 | 5 | 5: +1,461 (4), 0: +826 (2) |

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 3): +8,847 (n=1)
- (6, 3, 4): +2,023 (n=2)
- (9, 4, 6): +0 (n=1)
- (11, 4, 6): -386 (n=2)

_Generated 2026-09-03 15:40. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._