# AGE-333 adversarial diagnostic scenarios -- population results

Suite `v1`, opponent `Opponents/tape_mtn_105853290.py` (the frontier as of 55d6b6d), 3 seeds per
scenario, every agent in `candidates/`. Produced by:

    python3 evolve/run_scenarios.py --agent candidates/*.py --md docs/AGE-333-scenario-suite-results.md

These are **diagnostics, not grades**. They do not enter cascade ranking, promotion or parent
selection, and a FAIL here says nothing about dev or held-out margin -- it says the candidate makes
one specific economic mistake when the world is arranged so that mistake is the only thing that
matters. Scenario definitions and thresholds: `evolve/scenarios/README.md`.

## Per-candidate

| agent | unsupported_livestock | idle_labor | late_expansion | land_pressure | execution_overload | pass |
|---|---|---|---|---|---|---|
| C1 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| C2 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| E1 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| E_block | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| E_c956 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| E_daba | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| E_e4a4 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| E_fert1_block | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| H10 | PASS | PASS | PASS | **FAIL** | **FAIL** | 3/5 |
| H11 | PASS | PASS | PASS | **FAIL** | **FAIL** | 3/5 |
| H12 | PASS | PASS | PASS | **FAIL** | **FAIL** | 3/5 |
| H30 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| H31 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| H32 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| K | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| M1_k1 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| M1_k2 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| M1_k4 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| M1_k8 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| M2 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| M3_GENERAL_SIZING | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| M4 | **FAIL** | PASS | PASS | **FAIL** | PASS | 3/5 |
| P | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| P5 | **FAIL** | PASS | PASS | PASS | **FAIL** | 3/5 |
| P6_baseline | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| P7b | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| P_pre_tape | **FAIL** | PASS | PASS | PASS | **FAIL** | 3/5 |
| V3_11 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| V3_12 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |
| V3_29 | **FAIL** | PASS | PASS | PASS | PASS | 4/5 |

## What the population does

**`unsupported_livestock` -- 3 pass / 27 fail.** With no town shop unlocking all season, animal
products have only the town center's one-unit-a-day pull behind them: roughly 30 units of MILK
demand for the whole season, against a herd of six cows that alone makes three a day. Nearly the
whole population still builds a 6-9 animal herd and clears about $350 per animal across 30 days --
less than the purchase price, before feed. Only the H10/H11/H12 line keeps the herd inside what the
market supports and is exempted.

**`land_pressure` -- 17 pass / 13 fail.** The mirror image: eight shop instances by day 8 consuming
twice as often as normal, $12k in hand, and expansion is the right answer. Every failure trips
`early_cash_trough`, not `land_at_midgame` -- the H30-H32 and M1-M4 lines do buy land, but never
let their cash fall below ~$9,000 through days 3-12 while demand outruns their supply. C1 in the
same world spends down to $29 and finishes with roughly four times the money.

**`execution_overload` -- 25 pass / 5 fail.** Hires cost 200*fib(n), so the crew is a budget
decision. H10/H11/H12 fail on `missed_feed`, P5 and P_pre_tape on `chore_completion`.

**`idle_labor` and `late_expansion` -- 30 pass / 0 fail.** A real property of this lineage rather
than an inert test: the chassis sizes its crew from servicing load rather than from cash, so free
hires and $40k do not make it over-hire; and `LAND_DEADLINE` (last land purchase day 18) plus
`HERD_LAST_DAY` close expansion well before day 23, so there is no late capital to commit. Both
FAIL paths are exercised by the control agents in `evolve/scenarios/controls.py` and asserted in
`tests/test_scenarios.py`, so a future candidate that does over-hire or does expand late will be
caught.

## Triggering metric, by frequency

| scenario | triggering metric | fails |
|---|---|---|
| unsupported_livestock | `animal_revenue_per_animal` | 27 |
| land_pressure | `early_cash_trough` | 13 |
| execution_overload | `missed_feed` | 3 |
| execution_overload | `chore_completion` | 2 |

## Caveat

A scenario world is not the ladder. `unsupported_livestock` deliberately removes the town shops
that most of this population's crop revenue depends on, and `land_pressure` deliberately inflates
demand far past anything the real game produces. Read a FAIL as "this candidate would make this
mistake if the world looked like this", never as a prediction of ladder placement.
