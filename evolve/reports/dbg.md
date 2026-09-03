# Evolution run dbg

Frontier opponent: `V3_12.py` · clone: `opp_scenario_v14.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_c38b582a1380.py` (sha `c38b582a1380`)
Elapsed 0.01 h · candidates evaluated this run: 2 · games 174 (12,174/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_smoke | 0 | 0 |
| alive | 1 | 47 |
| held_fail | 0 | 0 |
| held_pass | 1 | 127 |
| error | 0 | 0 |

Population (all runs, reached dev): 2 · held-out evaluated: 1 · held-out PASS: 1

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
| `b75f6ea6245f` | seed:V3_12 | +0 | inf | 0-0 | +13,510 | alive | opening frontier→v312, open_melons 8→12, early_hire_days 5→0, feed_spare_poor 0→3 |

## Where the signal is (mean dev margin by parameter value, all runs)


## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 3): +8,847 (n=1)
- (9, 4, 6): +0 (n=1)

_Generated 2026-09-03 15:38. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._