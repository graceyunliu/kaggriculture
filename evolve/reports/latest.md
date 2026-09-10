# Evolution run 20260910-084834

Frontier opponent: `O15_SALE_PRIORITY.py` · clone: `tape_yangkuang2_106819729.py` · engine sha `bc8a54879ef0` · chassis snapshot `K_0df71adce97c.py` (sha `0df71adce97c`)
Elapsed 0.23 h · candidates evaluated this run: 25 · games 2,076 (8,898/h)

## Cascade counts (this run)

| status | candidates | games |
|---|---:|---:|
| noop | 1 | 2 |
| dead_pattern | 3 | 6 |
| dead_smoke | 4 | 32 |
| alive | 16 | 1728 |
| held_fail | 1 | 308 |
| held_pass | 0 | 0 |
| error | 0 | 0 |

Population (all runs, reached dev): 152 · held-out evaluated: 6 · held-out PASS: 0

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
| `891a7b9685a3` | queue | mutate | **+1,596** | 1.9 | 12-8 | -28,036 | +2,663 | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand pulls ahead of C1 from day 11 (gap +9,138 -> final +9,451); days 9-16 drivers: missed_water -41, sales_rev +728, feed_hour -0.45. Hands 6 vs 11, animals 11 vs 11, plants 64 vs 85. |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | **+1,448** | 1.7 | 14-6 | -22,347 | +3,920 | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |  | cand falls behind C1 from day 16 (gap -1,900 -> final -23,517); days 14-21 drivers: sales_rev -16,479, work_turns -300, idle_turns +13. Hands 6 vs 14, animals 7 vs 11, plants 68 vs 84. |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | **+888** | 0.9 | 13-7 | -23,349 | +3,066 | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -5,259 -> final -19,783); days 21-28 drivers: sales_rev -24,924, weeds_new +5, work_turns -48, missed_feed +2. Hands 9 vs 9, animals 14 vs 11, plants 26 vs 33. |
| `5fd05605827b` | c1 | crossover | **+299** | 0.3 | 9-11 | -24,173 | +2,683 | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |  | cand falls behind C1 from day 23 (gap -2,136 -> final -9,553); days 21-28 drivers: sales_rev -10,734, weeds_new +15, work_turns -134, idle_turns +10. Hands 5 vs 9, animals 10 vs 11, plants 7 vs 33. |

## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)

| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |
|---|---|---|---:|---:|---:|---:|---|---|
| `7ec902ce836b` | queue | crossover | +4,836 | 4.6 | 10-0 | -21,491 | held_fail | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_cap 22→13, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `f573bfac39ea` | queue | archive_crossover:crossover_g000075_20260910-082933_1 | +3,920 | 3.9 | 8-2 | -18,577 | held_fail | load_per_hand 20→19, open_melons 8→10, wheat_cap 22→13, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39 · blocks: hiring |
| `c623d6f0b67a` | queue | archive_crossover:crossover_g000075_20260910-090023_0 | +3,066 | 2.5 | 8-2 | -22,071 | held_fail | melon_floor 0→150, open_melons 8→10, CROP_SWEEP_RADIUS 5→3, MELON_MAX_TILES 38→39, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `5fd05605827b` | c1 | crossover | +2,683 | 3.5 | 9-1 | -22,747 | held_fail | melon_floor 0→150, wheat_water_tier 0→1, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19 · blocks: hiring |
| `891a7b9685a3` | queue | mutate | +2,663 | 2.3 | 9-1 | -26,078 | held_fail | melon_floor 0→100, open_melons 8→11, demand_share 0.55→0.45, wheat_cap 22→25, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, MELON_PRICE_CUSHION 100→85, HERD_LAST_DAY 17→19 · blocks: hiring |
| `db96e76075e4` | H32 | crossover | +2,565 | 2.6 | 8-2 | -27,885 | held_fail | melon_floor 0→150, harvest_min 1→2, fert_buy 3→0, fert_carry 2→3, demand_share 0.55→0.5, max_animals 17→15, wheat_cap 22→13, ROUTE_LEN 3→2, CROP_SWEEP_RADIUS 5→6 |
| `7ca17c5483fc` | queue | archive_crossover:crossover_g000075_20260910-082933_0 | +2,293 | 2.0 | 7-3 | -21,234 | alive | melon_floor 0→100, open_melons 8→10, demand_share 0.55→0.45, wheat_sell_price 30→25, MAX_HANDS 14→12, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→17, MELON_MAX_TILES 38→35, HERD_LAST_DAY 17→19 · blocks: hiring |
| `be39051210fb` | c1 | block_pair | +2,143 | 0.3 | 2-8 | -28,277 | alive | geese 0→1, open_melons 8→6 · blocks: sweep |
| `362ca8604fb4` | c1 | paired | +2,033 | 1.6 | 7-3 | -24,144 | alive | MAX_HANDS 14→13, SPREAD_W 1.25→1.0 |
| `926d7668ad53` | queue | mutate | +1,769 | 1.9 | 8-2 | -28,807 | alive | melon_floor 0→100, load_per_hand 20→19, open_melons 8→11, feed_spare_poor 0→3, wheat_cap 22→25, wheat_water_tier 0→1, wheat_sell_price 30→25, CROP_SWEEP_RADIUS 5→3, STRAW_CUTOFF 19→20, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.2, FERT_RADIUS 3→4 |
| `7a0b60c391c7` | wide | mutate | +1,686 | 0.8 | 5-5 | -23,482 | alive | melon_floor 0→150, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, labor_reserve_buffer 92→11, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10 · blocks: hiring |
| `384684cbc0ec` | queue | mutate | +1,682 | 0.8 | 5-5 | -20,214 | alive | open_wheat 7→4, feed_spare_poor 0→1, demand_share 0.55→0.65, wheat_per_animal 0.0→0.3, wheat_cap 22→13, wheat_sell_price 30→25, labor_reserve_buffer 92→124, ROUTE_LEN 3→2, MELON_MAX_TILES 38→39, OPP_GROWTH 1.4→1.3 · blocks: hiring |
| `a1c2b0acfbad` | wide | crossover | +1,312 | 0.6 | 4-6 | -23,295 | alive | melon_floor 0→100, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_cap 22→25, wheat_sell_price 30→25, wheat_hold_days 0→2, setup_capital_share 0.25→0.4, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, MAX_SHEEP 14→10, FERT_RADIUS 3→4 · blocks: hiring |
| `e35b9263f480` | c1 | mutate | +1,225 | 0.7 | 7-3 | -22,169 | alive | open_melons 8→10, open_wheat 7→3, demand_share 0.55→0.6, wheat_cap 22→25, wheat_water_tier 0→1, labor_reserve_buffer 92→58, MAX_HANDS 14→13, CROP_SWEEP_RADIUS 5→6, MELON_MAX_TILES 38→34, MELON_PRICE_CUSHION 100→102 · blocks: hiring |
| `b2fcadbcb634` | wide | crossover | +1,217 | 0.6 | 6-4 | -26,721 | alive | melon_floor 0→100, load_per_hand 20→18, open_melons 8→10, wheat_per_animal 0.0→0.3, wheat_sell_price 30→25, wheat_hold_days 0→2, CROP_SWEEP_LEN 6→3, STRAW_CUTOFF 19→16, MELON_MAX_TILES 38→34, HERD_LAST_DAY 17→19, OPP_GROWTH 1.4→1.5, MAX_SHEEP 14→10 · blocks: hiring |

## Islands (best dev margin, population size)

- H32: best +2,565 (`db96e76075e4`), n=20
- M2: best -434 (`a70cecec4f5d`), n=12
- c1: best +2,683 (`5fd05605827b`), n=28
- queue: best +4,836 (`7ec902ce836b`), n=48
- v312: best +1,192 (`038351a768ec`), n=23
- wide: best +1,686 (`7a0b60c391c7`), n=21

## Where the signal is (observed outcome variation by parameter value, all runs)

**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'

Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.

| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |
|---|---:|---|---|---:|---:|---:|---|
| MELON_PRICE_CUSHION | +6,906 | 85 | 100 | 15 | 142 | 3.58 | 85: +297 (n=3), 100: -1,514 (n=130), 110: -4,899 (n=2), 92: -4,998 (n=5), 99: -6,609 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_melons | +6,528 | 9 | 8 | 7 | 151 | 2.22 | 9: +1,043 (n=3), 10: -837 (n=55), 11: -1,492 (n=7), 8: -2,252 (n=81), 4: -4,132 (n=2), 5: -5,485 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MELON_MAX_TILES | +5,924 | 39 | 38 | 11 | 148 | 2.07 | 39: +568 (n=12), 35: -394 (n=17), 34: -1,098 (n=40), 38: -2,360 (n=65), 41: -3,113 (n=2), 43: -3,218 (n=9), 46: -5,356 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_LEN | +5,732 | 3 | 6 | 6 | 151 | 2.94 | 3: -647 (n=23), 5: -1,019 (n=4), 6: -1,814 (n=119), 8: -1,921 (n=2), 7: -6,379 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| wheat_cap | +5,294 | 13 | 22 | 8 | 151 | 3.73 | 13: -297 (n=13), 25: -1,038 (n=15), 22: -1,522 (n=102), 18: -3,051 (n=11), 24: -3,782 (n=3), 20: -5,213 (n=3), 23: -5,591 (n=4) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_sheep | +5,093 | 2 | 2 | 4 | 152 | 2.45 | 2: -1,379 (n=131), 1: -3,224 (n=15), 0: -4,102 (n=4), 3: -6,471 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| load_per_hand | +4,982 | 18 | 20 | 8 | 150 | 3.16 | 18: +1,079 (n=3), 19: -1,127 (n=28), 20: -1,607 (n=104), 22: -2,577 (n=3), 23: -3,453 (n=2), 21: -3,903 (n=10) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| ROUTE_LEN | +4,816 | 2 | 3 | 3 | 152 | 1.49 | 2: -693 (n=13), 3: -1,410 (n=126), 4: -5,510 (n=13) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| MAX_HANDS | +4,794 | 12 | 14 | 6 | 152 | 3.62 | 12: +563 (n=16), 13: -465 (n=6), 14: -1,912 (n=117), 11: -2,486 (n=2), 15: -2,898 (n=8), 16: -4,231 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| setup_capital_share | +4,587 | 0.45 | 0.25 | 8 | 150 | 3.24 | 0.45: +296 (n=4), 0.2: -662 (n=3), 0.4: -1,318 (n=15), 0.25: -1,345 (n=106), 0.5: -3,672 (n=3), 0.35: -4,290 (n=19) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| labor_reserve_buffer | +4,229 | 124 | 92 | 18 | 142 | 5.37 | 124: +365 (n=4), 107: -752 (n=3), 11: -1,339 (n=12), 73: -1,731 (n=2), 92: -1,740 (n=113), 150: -1,877 (n=4), 76: -3,783 (n=2), 102: -3,863 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| STRAW_CUTOFF | +3,917 | 17 | 19 | 6 | 152 | 2.99 | 17: +481 (n=15), 16: -950 (n=12), 14: -1,730 (n=3), 19: -1,851 (n=101), 20: -2,650 (n=13), 18: -3,437 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_wheat | +3,685 | 4 | 7 | 7 | 150 | 2.93 | 4: -991 (n=23), 3: -1,303 (n=5), 7: -1,768 (n=118), 10: -3,113 (n=2), 6: -4,676 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| CROP_SWEEP_RADIUS | +3,626 | 3 | 5 | 5 | 152 | 1.96 | 3: -959 (n=26), 5: -1,414 (n=90), 2: -2,162 (n=3), 6: -2,916 (n=31), 4: -4,586 (n=2) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| opening | +3,559 | frontier | frontier | 2 | 152 | 0.89 | frontier: -1,512 (n=144), v312: -5,071 (n=8) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| min_hands | +3,522 | 3 | 3 | 3 | 152 | 1.88 | 3: -1,624 (n=146), 5: -1,910 (n=3), 4: -5,146 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| demand_share | +3,394 | 0.45 | 0.55 | 7 | 151 | 3.09 | 0.45: +61 (n=9), 0.65: -351 (n=12), 0.55: -1,626 (n=103), 0.6: -2,253 (n=3), 0.3: -3,235 (n=3), 0.5: -3,334 (n=21) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| open_cows | +2,739 | 2 | 2 | 3 | 152 | 1.86 | 2: -1,575 (n=145), 3: -4,235 (n=4), 1: -4,314 (n=3) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| HERD_LAST_DAY | +2,643 | 19 | 17 | 7 | 152 | 2.96 | 19: -603 (n=39), 16: -718 (n=2), 18: -1,407 (n=8), 17: -1,985 (n=86), 22: -2,551 (n=5), 20: -3,144 (n=3), 14: -3,246 (n=9) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__
| SPREAD_W | +2,635 | 1.25 | 1.25 | 5 | 150 | 1.78 | 1.25: -1,553 (n=139), 1.0: -2,056 (n=4), 1.5: -4,188 (n=7) |
  __Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only.__

## Behavioural cells (animals@d15, land, max hands) → best dev margin, n

- (8, 3, 4): +4,836 (n=10)
- (7, 3, 4): +3,920 (n=16)
- (14, 3, 6): +3,066 (n=3)
- (9, 3, 4): +2,683 (n=13)
- (11, 3, 5): +2,663 (n=9)
- (9, 3, 5): +2,565 (n=3)
- (6, 3, 3): +2,293 (n=1)
- (15, 3, 6): +2,143 (n=1)
- (10, 4, 6): +2,033 (n=12)
- (7, 3, 3): +1,682 (n=8)
- (12, 3, 4): +1,225 (n=1)
- (6, 3, 4): +1,192 (n=3)
- (11, 3, 6): +1,150 (n=6)
- (10, 3, 5): +1,108 (n=4)
- (8, 4, 6): +744 (n=3)

_Generated 2026-09-10 09:02. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._

## Recent failure observations (grouped by failure class)

**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'

### EXECUTION_FAILURE (observed in 77 recent candidates)

- **Observed outcome:** unknown
- **Associated parameter ranges (correlation, not cause):** melon_floor=0–200 (n=77); harvest_min=1–2 (n=77); wheat_tiles=0–5 (n=77); wheat_stock=0–19 (n=77); min_hands=3–4 (n=77); load_per_hand=12–23 (n=77); geese=0–1 (n=77); open_melons=4–12 (n=77)
- **Evidence:** 77 candidates, multiple seeds. Confidence: high

_Generated 2026-09-10 09:02. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._