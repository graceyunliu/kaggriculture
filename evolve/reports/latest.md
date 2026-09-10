# Evolution run 20260910-075707

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.18 h · candidates evaluated this run: 20 · games 1,558 (8,704/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 1 | 2 |
| dead_pattern | 6 | 12 |
| dead_smoke | 1 | 8 |
| alive | 12 | 1536 |
| held_fail | 0 | 0 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 32 · held-out evaluated: 1 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `842eaa9dcc6d` | v312 | crossover | +1,121 | 2.1 | 6-4 | -23,619 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→35 |
| `02327af9eddf` | queue | llm:llm_20260910-075250_2 | +440 | 0.3 | 7-3 | -26,586 | alive |  · blocks: hiring |
| `cbe25df47407` | queue | crossover | +395 | 0.3 | 6-4 | -24,578 | alive | wheat_stock 0→4, load_per_hand 20→19, open_wheat 7→4, feed_spare_poor 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→26, HERD_LAST_DAY 17→14, MAX_SHEEP 14→12, FERT_RADIUS 3→1, SPREAD_CAP 3→4 · blocks: hiring |
| `6192b1ec5e53` | c1 | mutate | +381 | 0.3 | 7-3 | -23,199 | alive | setup_capital_share 0.25→0.35, CROP_SWEEP_RADIUS 5→6 |
| `379821284ab8` | queue | mutate | +308 | 0.3 | 5-5 | -21,643 | alive | load_per_hand 20→19, open_wheat 7→4, feed_spare_poor 0→1, HERD_LAST_DAY 17→18, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1 · blocks: hiring |
| `ed9035317440` | queue | llm:llm_20260910-075250_3 | +169 | 0.2 | 6-4 | -26,345 | alive |  · blocks: hiring |
| `ef03d0ea01e0` | v312 | mutate | +60 | 0.1 | 8-2 | -19,967 | alive | open_melons 8→10, early_hire_days 5→3, MAX_HANDS 14→12 |
| `4b523741abfd` | v312 | seed:base | +0 | 0.0 | 0-0 | -19,577 | alive | open_melons 8→10, early_hire_days 5→3 |
| `d9342e7e5120` | v312 | mutate | -37 | -0.0 | 5-5 | -23,719 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→3, wheat_per_animal 0.0→0.2, wheat_sell_price 30→28, CROP_SWEEP_RADIUS 5→3, OPP_GROWTH 1.4→1.0 |
| `a9ba8dc84102` | wide | crossover | -79 | -0.1 | 6-4 | -22,691 | alive | melon_floor 0→100, wheat_stock 0→4, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12 · blocks: hiring |
| `2be7ac28aaaf` | queue | crossover | -81 | -0.1 | 4-6 | -20,632 | alive | open_wheat 7→4, demand_share 0.55→0.65, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→18, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `492cf9a2665a` | c1 | seed:c1 | -235 | -0.2 | 4-6 | -25,557 | alive |  |
| `2d41259213c4` | wide | block_pair | -425 | -0.3 | 5-5 | -24,308 | alive | wheat_stock 0→4, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→26, MELON_MAX_TILES 38→34, MAX_SHEEP 14→12 · blocks: hiring |
| `4f7df7e31806` | c1 | migrate | -465 | -0.4 | 5-5 | -28,966 | alive | melon_floor 0→100, early_hire_days 5→3, wheat_per_animal 0.0→0.2, wheat_sell_price 30→28, setup_capital_share 0.25→0.4, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→18, OPP_GROWTH 1.4→1.0 |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=5
- M2: best -3,630 (`f443671ed6df`), n=3
- c1: best +381 (`6192b1ec5e53`), n=5
- queue: best +440 (`02327af9eddf`), n=11
- v312: best +1,121 (`842eaa9dcc6d`), n=5
- wide: best -79 (`a9ba8dc84102`), n=3

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| wheat_cap | +6,902 | 13 | 22 | 6 | 31 | 2.39 | 13: +286 (n=2), 22: -1,134 (n=21), 25: -1,746 (n=3), 18: -1,776 (n=3), 23: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,722 | 10 | 8 | 4 | 31 | 1.23 | 10: +106 (n=6), 8: -1,760 (n=23), 5: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +6,521 | 2 | 3 | 3 | 32 | 1.53 | 2: +905 (n=2), 3: -1,426 (n=27), 4: -5,616 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +6,215 | 19 | 20 | 4 | 31 | 1.32 | 19: -401 (n=5), 20: -1,429 (n=24), 21: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +5,272 | 6 | 6 | 2 | 32 | 0.88 | 6: -1,344 (n=30), 7: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +5,268 | 100 | 100 | 3 | 31 | 0.87 | 100: -1,342 (n=29), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +4,527 | 14 | 14 | 4 | 30 | 0.8 | 14: -1,089 (n=27), 13: -5,616 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| geese | +4,418 | 0 | 0 | 2 | 32 | 0.75 | 0: -1,121 (n=28), 1: -5,539 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_water_tier | +3,866 | 0 | 0 | 2 | 32 | 0.75 | 0: -1,190 (n=28), 1: -5,056 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +3,821 | 0.4 | 0.25 | 3 | 32 | 1.34 | 0.4: -272 (n=2), 0.25: -1,301 (n=25), 0.35: -4,094 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_RADIUS | +2,880 | 3 | 5 | 4 | 31 | 0.94 | 3: +38 (n=4), 5: -1,522 (n=20), 6: -2,842 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| melon_floor | +2,302 | 100 | 0 | 3 | 32 | 0.97 | 100: -401 (n=6), 0: -1,791 (n=21), 150: -2,703 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +1,932 | 3 | 5 | 4 | 30 | 0.6 | 3: +35 (n=6), 5: -1,897 (n=24) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| harvest_min | +1,885 | 1 | 1 | 2 | 32 | 0.5 | 1: -1,202 (n=24), 2: -3,087 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| FERT_RADIUS | +1,780 | 3 | 3 | 2 | 32 | 0.69 | 3: -1,395 (n=27), 1: -3,175 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +1,688 | 17 | 17 | 3 | 31 | 0.61 | 17: -1,483 (n=25), 20: -3,171 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +1,670 | 1.0 | 1.4 | 4 | 31 | 1.42 | 1.0: -251 (n=2), 1.3: -1,136 (n=4), 1.4: -1,921 (n=25) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_sell_price | +1,669 | 28 | 30 | 4 | 31 | 1.42 | 28: -251 (n=2), 26: -1,239 (n=4), 30: -1,920 (n=25) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +1,569 | 0.3 | 0.0 | 3 | 32 | 1.34 | 0.3: -351 (n=4), 0.2: -1,379 (n=3), 0.0: -1,920 (n=25) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +1,445 | 12 | 14 | 3 | 31 | 0.74 | 12: -351 (n=4), 14: -1,796 (n=27) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (9, 3, 5): +2,565 (n=2)
- (11, 3, 6): +1,121 (n=1)
- (9, 3, 4): +440 (n=2)
- (7, 3, 3): +395 (n=5)
- (10, 4, 6): +381 (n=5)
- (7, 3, 4): +308 (n=3)
- (12, 3, 5): -465 (n=2)
- (13, 3, 5): -468 (n=1)
- (13, 4, 6): -755 (n=1)
- (10, 3, 6): -1,409 (n=2)
- (8, 3, 4): -2,094 (n=3)
- (9, 4, 6): -3,633 (n=1)
- (12, 3, 6): -5,576 (n=1)
- (12, 4, 6): -6,510 (n=2)
- (10, 4, 5): -6,815 (n=1)

_Generated 2026-09-10 08:07. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 20 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–150 (n=20); harvest_min=1–2 (n=20); wheat_tiles=0–2 (n=20); wheat_stock=0–12 (n=20); min_hands=3–4 (n=20); load_per_hand=12–21 (n=20); geese=0–1 (n=20); open_melons=6–10 (n=20)
- **Evidence:** 20 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 08:07. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._