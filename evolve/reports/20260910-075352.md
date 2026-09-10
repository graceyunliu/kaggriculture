# Evolution run 20260910-075352

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.02 h · candidates evaluated this run: 4 · games 260 (13,874/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 2 | 4 |
| dead_smoke | 0 | 0 |
| alive | 2 | 256 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 4 · held-out evaluated: 0 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

None reached held-out this run.

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `02327af9eddf` | queue | llm:llm_20260910-075250_2 | +440 | 0.3 | 7-3 | -26,586 | alive |  · blocks: hiring |
| `4b523741abfd` | v312 | seed:base | +0 | 0.0 | 0-0 | -19,577 | alive | open_melons 8→10, early_hire_days 5→3 |
| `492cf9a2665a` | c1 | seed:c1 | -235 | -0.2 | 4-6 | -25,557 | alive |  |
| `cc7e0368d411` | H32 | seed:H32 | -2,094 | -1.7 | 2-8 | -28,451 | alive | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→20, wheat_cap 22→18 |

## Islands (best dev margin, population size)

- H32: best -2,094 (`cc7e0368d411`), n=1
- c1: best -235 (`492cf9a2665a`), n=1
- queue: best +440 (`02327af9eddf`), n=1
- v312: best +0 (`4b523741abfd`), n=1

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.


## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 4): +440 (n=1)
- (10, 4, 6): +0 (n=2)
- (8, 3, 4): -2,094 (n=1)

_Generated 2026-09-10 07:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 2 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0; harvest_min=1; wheat_tiles=0; wheat_stock=0; min_hands=3; load_per_hand=20; geese=0; open_melons=8
- **Evidence:** 2 candidates, multiple seeds. Confidence: low

_Generated 2026-09-10 07:55. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._