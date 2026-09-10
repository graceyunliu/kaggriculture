# Evolution run 20260910-080950

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_himanshukumar_107290180.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.14 h · candidates evaluated this run: 9 · games 1,266 (9,356/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 0 | 0 |
| dead_pattern | 1 | 2 |
| dead_smoke | 0 | 0 |
| alive | 7 | 896 |
| held_fail | 1 | 368 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 53 · held-out evaluated: 2 · held-out PASS: 0

## Reference points

| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |
|---|---:|---:|---:|---:|---:|---:|---:|
| V3_12 (K defaults) | +0 | 0.0 | 0-0 | -19,577 | — | — | —-— |
| C1 | -235 | -0.2 | 4-6 | -25,557 | — | — | —-— |

## Held-out results (the only numbers that count)

| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| `7ec902ce836b` | queue | crossover | **+4,545** | 3.6 | 15-5 | -24,608 | +4,836 | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -2,334 -> final -12,991); days 14-21 drivers: sales_rev -17,712, work_turns -252, water_hour +0.41. Hands 7 vs 14, animals 8 vs 11, plants 66 vs 84. |
| `db96e76075e4` | H32 | crossover | **+2,011** | 1.4 | 14-6 | -26,235 | +2,565 | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |  | cand falls behind C1 from day 23 (gap -2,691 -> final -16,764); days 21-28 drivers: sales_rev -21,522, work_turns -134, water_hour +0.56, idle_turns +8. Hands 7 vs 9, animals 10 vs 11, plants 19 vs 33 |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `7a0b60c391c7` | wide | mutate | +1,686 | 0.8 | 5-5 | -23,482 | alive | melon_floor 0→150, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `842eaa9dcc6d` | v312 | crossover | +1,121 | 2.1 | 6-4 | -23,619 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→10, early_hire_days 5→3, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→35 |
| `02327af9eddf` | queue | llm:llm_20260910-075250_2 | +440 | 0.3 | 7-3 | -26,586 | alive |  · blocks: hiring |
| `cbe25df47407` | queue | crossover | +395 | 0.3 | 6-4 | -24,578 | alive | wheat_stock 0→4, load_per_hand 20→19, open_wheat 7→4, feed_spare_poor 0→1, wheat_per_animal 0.0→0.3, wheat_sell_price 30→26, HERD_LAST_DAY 17→14, MAX_SHEEP 14→12, FERT_RADIUS 3→1, SPREAD_CAP 3→4 · blocks: hiring |
| `6192b1ec5e53` | c1 | mutate | +381 | 0.3 | 7-3 | -23,199 | alive | setup_capital_share 0.25→0.35, CROP_SWEEP_RADIUS 5→6 |
| `8f240e8b2141` | wide | block_pair | +352 | 0.3 | 6-4 | -21,751 | alive | melon_floor 0→100, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→11 · blocks: hiring |
| `379821284ab8` | queue | mutate | +308 | 0.3 | 5-5 | -21,643 | alive | load_per_hand 20→19, open_wheat 7→4, feed_spare_poor 0→1, HERD_LAST_DAY 17→18, OPP_GROWTH 1.4→1.3, FERT_RADIUS 3→1 · blocks: hiring |
| `e56c8491addc` | wide | paired | +206 | 0.2 | 6-4 | -20,957 | alive | melon_floor 0→100, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→1, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12 · blocks: hiring |
| `ed9035317440` | queue | llm:llm_20260910-075250_3 | +169 | 0.2 | 6-4 | -26,345 | alive |  · blocks: hiring |
| `ef03d0ea01e0` | v312 | mutate | +60 | 0.1 | 8-2 | -19,967 | alive | open_melons 8→10, early_hire_days 5→3, MAX_HANDS 14→12 |
| `1c41343ee0de` | wide | mutate | +23 | 0.0 | 4-6 | -22,634 | alive | melon_floor 0→100, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, CROP_SWEEP_LEN 6→3, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→12 · blocks: hiring |
| `4b523741abfd` | v312 | seed:base | +0 | 0.0 | 0-0 | -19,577 | alive | open_melons 8→10, early_hire_days 5→3 |
| `d9342e7e5120` | v312 | mutate | -37 | -0.0 | 5-5 | -23,719 | alive | melon_floor 0→100, open_melons 8→10, early_hire_days 5→3, wheat_per_animal 0.0→0.2, wheat_sell_price 30→28, CROP_SWEEP_RADIUS 5→3, OPP_GROWTH 1.4→1.0 |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=8
- M2: best -3,630 (`f443671ed6df`), n=5
- c1: best +381 (`6192b1ec5e53`), n=9
- queue: best +4,836 (`7ec902ce836b`), n=17
- v312: best +1,121 (`842eaa9dcc6d`), n=6
- wide: best +1,686 (`7a0b60c391c7`), n=8

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| wheat_cap | +6,742 | 13 | 22 | 6 | 52 | 2.46 | 13: +363 (n=5), 22: -1,571 (n=36), 25: -1,746 (n=3), 18: -2,532 (n=5), 23: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,474 | 10 | 8 | 5 | 51 | 1.12 | 10: -141 (n=13), 8: -2,134 (n=36), 5: -6,615 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +6,466 | 3 | 6 | 3 | 53 | 1.55 | 3: +87 (n=5), 6: -1,768 (n=45), 7: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +6,044 | 39 | 38 | 7 | 50 | 1.88 | 39: +2,377 (n=2), 34: -605 (n=10), 38: -2,457 (n=36), 43: -3,667 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +5,162 | 2 | 3 | 3 | 53 | 1.43 | 2: -56 (n=4), 3: -1,552 (n=43), 4: -5,218 (n=6) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_PRICE_CUSHION | +4,994 | 100 | 100 | 5 | 50 | 0.92 | 100: -1,615 (n=48), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +4,817 | 0.65 | 0.55 | 5 | 51 | 1.24 | 0.65: +1,546 (n=3), 0.55: -1,731 (n=38), 0.5: -3,271 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,307 | 19 | 20 | 4 | 52 | 1.37 | 19: -1,271 (n=7), 20: -1,538 (n=41), 21: -5,578 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_water_tier | +3,723 | 0 | 0 | 2 | 53 | 0.81 | 0: -1,503 (n=48), 1: -5,226 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPENING_MELONS | +3,654 | 14 | 14 | 4 | 51 | 0.8 | 14: -1,426 (n=46), 13: -5,080 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| geese | +3,600 | 0 | 0 | 2 | 53 | 0.81 | 0: -1,515 (n=48), 1: -5,114 (n=5) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| early_hire_days | +3,383 | 3 | 5 | 4 | 52 | 1.48 | 3: -951 (n=7), 5: -1,896 (n=43), 0: -4,334 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| max_animals | +3,130 | 15 | 17 | 4 | 53 | 2.02 | 15: -455 (n=2), 17: -1,509 (n=40), 18: -2,375 (n=2), 20: -3,585 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +2,805 | 11 | 92 | 3 | 52 | 0.92 | 11: +854 (n=2), 92: -1,950 (n=50) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +2,571 | 0.4 | 0.25 | 5 | 51 | 1.12 | 0.4: -1,355 (n=7), 0.25: -1,423 (n=36), 0.35: -3,926 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +2,515 | 19 | 19 | 4 | 52 | 1.71 | 19: -1,706 (n=47), 18: -3,779 (n=3), 20: -4,222 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| OPP_GROWTH | +2,487 | 1.3 | 1.4 | 5 | 51 | 1.47 | 1.3: +30 (n=6), 1.4: -2,056 (n=42), 1.0: -2,458 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_per_animal | +2,187 | 0.3 | 0.0 | 3 | 53 | 1.09 | 0.3: -565 (n=12), 0.0: -2,176 (n=37), 0.2: -2,752 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_SHEEP | +2,093 | 10 | 14 | 4 | 53 | 1.94 | 10: -73 (n=2), 12: -1,040 (n=10), 11: -1,640 (n=2), 14: -2,166 (n=39) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_hold_days | +2,085 | 2 | 0 | 3 | 53 | 1.49 | 2: -41 (n=3), 1: -772 (n=6), 0: -2,126 (n=44) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=5)
- (9, 3, 5): +2,565 (n=2)
- (7, 3, 4): +1,686 (n=8)
- (11, 3, 6): +1,121 (n=1)
- (9, 3, 4): +440 (n=4)
- (7, 3, 3): +395 (n=6)
- (10, 4, 6): +381 (n=5)
- (12, 3, 5): -465 (n=2)
- (13, 3, 5): -468 (n=1)
- (13, 4, 6): -755 (n=2)
- (5, 3, 5): -1,056 (n=1)
- (10, 3, 6): -1,409 (n=2)
- (16, 4, 6): -1,832 (n=1)
- (10, 3, 4): -3,165 (n=1)
- (14, 4, 6): -3,175 (n=1)

_Generated 2026-09-10 08:18. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 31 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–150 (n=31); harvest_min=1–2 (n=31); wheat_tiles=0–2 (n=31); wheat_stock=0–12 (n=31); min_hands=3–4 (n=31); load_per_hand=12–21 (n=31); geese=0–1 (n=31); open_melons=6–12 (n=31)
- **Evidence:** 31 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 08:18. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._