# Adversarial diagnostic scenarios (AGE-333)

Five targeted economic worlds, each built so that exactly one failure mode decides the outcome, run
as a **diagnostic pass that is separate from the cascade**. Nothing here feeds ranking, promotion or
parent selection: `evolve/cascade.py` does not import this package, this package does not import
`evolve/cascade.py`, and the verdicts live in their own `scenario_results` table rather than in a
`candidates` column.

The question a scenario answers is not "is this candidate good?" -- that is what dev and held-out
margin are for -- but "does this candidate make a *specific* economic mistake when the world is
arranged so that mistake is the only thing that matters?"

```
python3 evolve/run_scenarios.py --list
python3 evolve/run_scenarios.py --agent candidates/C1.py
python3 evolve/run_scenarios.py --agent candidates/C1.py --only idle_labor land_pressure
python3 evolve/run_scenarios.py --from-db --frontier candidates/H32.py --md evolve/reports/scenarios.md
python3 -m scenarios --agent candidates/C1.py          # same CLI, with evolve/ on sys.path
```

## Layout

| file | what it is |
|---|---|
| `spec.py` | `Scenario` and `Criterion`: the definition vocabulary and the pass/fail rule |
| `metrics.py` | trace -> flat dict of whole-game scalars that criteria threshold |
| `registry.py` | the five scenario modules, in order, plus `SUITE_VERSION` |
| `runner.py` | plays the games, applies the criteria, CLI |
| `store.py` | `scenario_results` table: save / query / population view |
| `report.py` | markdown: per-candidate grid, per-scenario population view, fail analysis |
| `controls.py` | lab fixtures that inject one pathology, used to prove the FAIL paths fire |
| `unsupported_livestock.py`, `idle_labor.py`, `late_expansion.py`, `land_pressure.py`, `execution_overload.py` | one scenario each |

Each scenario module returns a `Scenario` carrying the engine configuration, the pass/fail criteria
and a description, so adding or retuning one is a single-file edit and the report can always print
the number that decided a verdict.

## Pass/fail

No LLM. Every verdict is a threshold on a metric derived arithmetically from the per-day trace that
`evolve/trace.py` already records. Evaluation order:

1. any `exempt_when` criterion true -> **PASS**, "the candidate never took the bait";
2. any `fail_when` criterion true -> **FAIL**, and the explanation names every criterion that fired
   with the value behind it;
3. otherwise **PASS**.

`exempt_when` exists because several of the ticket's pass conditions are disjunctive: "does not buy
cows beyond what the market supports; *or* buys but sells before they become a liability".

Each scenario runs 3 seeds (a diagnostic, not a held-out grade); metrics are averaged across seeds
and the criteria are applied once to the average. If the candidate raises inside a scenario world
the verdict is withheld as **inconclusive** rather than guessed -- an agent that stopped acting
scores like a cautious one on every metric here.

## The five scenarios

| scenario | world | fails when |
|---|---|---|
| `unsupported_livestock` | no town shop unlocks all season, so animal products have only the town center's one-a-day pull; headline animal prices are 2.5x base, glut floors them after 10 units; crops flat at base | `animal_revenue_per_animal < 700` (exempt at `peak_animals <= 3`) |
| `idle_labor` | $40k opening cash, free hires (`farmHandCostMult 0`), thin flat market so the footprint worth servicing is small | `idle_share >= 0.25` or `work_per_hand_day < 6` (exempt at `max_hands <= 4`) |
| `late_expansion` | $60k opening cash and demand that arrives late (`townShopUnlockInterval 8`), so the agent is richest after the payback window closes | `late_capital_committed > 800` on days 23-29 |
| `land_pressure` | 8 shop instances by day 8 consuming twice as often as normal, $12k opening cash: expansion is the *right* answer here | `land_at_midgame < 2` or `early_cash_trough > 4000` |
| `execution_overload` | $25k funds a large footprint while `farmHandCostMult 200` makes the hire ladder expensive | `chore_completion < 0.75`, `escapes >= 3` or `missed_feed >= 20` |

Every scenario is engine configuration only -- `startingMoney`, `farmHandCostMult`, the town
intervals and `marketParams` -- plus the standard frontier tape as the opponent. No engine change,
no custom opponent, no modification to the candidate.

### Deviations from the ticket's literal setup

* **`late_expansion` does not start on day 23.** The engine has no day-offset override and this
  ticket is explicitly not an engine change, so the scenario plays the full season and evaluates
  only the day-23..29 window. Same question, same seven days, reached by playing to them.
* **`unsupported_livestock` removes all town shops, not just the milk/wool ones.** Shops are drawn
  at random with replacement and the engine offers no per-shop control, so suppressing unlocks
  entirely is the only deterministic way to guarantee no animal-product buyer appears. Crop prices
  are pinned flat to compensate, so crops remain a real alternative allocation.
* **`boardSize` is not used anywhere.** It is the obvious lever for "small production footprint",
  but this chassis indexes tiles assuming a 10x10 board and raises on anything else -- a scenario
  built on it would measure a crash, not a decision.

## Calibration

Thresholds are set outside the band this chassis occupies on an ordinary season, measured on
C1/V3_12/H32 against `Opponents/frontier.txt` (default configuration, seeds 1-3):

| metric | ordinary-season range | threshold |
|---|---|---|
| `idle_share` | 0.09 - 0.16 | fail at 0.25 |
| `work_per_hand_day` | 9.0 - 9.5 | fail below 6.0 |
| `chore_completion` | 0.89 - 0.93 | fail below 0.75 |
| `escapes` | 0 | fail at 3 |
| `missed_feed` | 0 - 2 | fail at 20 |
| `animal_revenue_per_animal` | 1,200 - 5,200 | fail below 700 |

Retune by editing the constant at the top of the scenario module; the report prints the metric and
the threshold side by side, so a badly-placed threshold is visible in the output rather than buried.

## Do the scenarios discriminate?

Yes, in both directions.

* **On real candidates.** Across all 30 agents in `candidates/` (see
  `docs/AGE-333-scenario-suite-results.md`), three of the five scenarios split the population:
  `unsupported_livestock` 3 pass / 27 fail (only the H10/H11/H12 line keeps its herd inside what
  the market supports), `land_pressure` 17 pass / 13 fail (the H30-H32 and M1-M4 lines sit on
  ~$9,000 of cash through the opening while town demand runs away from them), and
  `execution_overload` 25 pass / 5 fail.
* **On controls.** The whole population passes `idle_labor` and `late_expansion` -- a real result
  about this lineage (its hire plan is driven by servicing load, and `LAND_DEADLINE`/`HERD_LAST_DAY`
  close expansion well before day 23) but only
  evidence about the population if the FAIL path is known to work. `controls.py` writes an agent
  that plays a base candidate with one pathology injected, and `tests/test_scenarios.py` asserts
  each scenario catches its own:

  | control | pathology | scenario | verdict |
  |---|---|---|---|
  | `hold_animal_products` | never sells MILK/WOOL/EGG | `unsupported_livestock` | FAIL (`animal_revenue_per_animal` 0) |
  | `no_livestock` | never buys an animal | `unsupported_livestock` | PASS (exempt) |
  | `overhire` | hires every turn regardless of work | `idle_labor` | FAIL (`idle_share` 0.68) |
  | `defer_expansion` | buys no land until day 23, then buys | `late_expansion` | FAIL (`late_capital_committed` $7,000) |
  | `hoard` | never buys land or hires | `land_pressure` | FAIL (`land_at_midgame` 1) |
  | `neglect_feeding` | drops every FEED/CARE action | `execution_overload` | FAIL (`chore_completion` 0.47) |
  | `starve_labor` | caps the crew at 2 hands | `execution_overload` | PASS -- the chassis plants less rather than breaking, which is the scenario's second pass condition |

  Control agents are lab fixtures. They are never candidates and nothing in the evolution loop reads
  them.

## Storage

`scenario_results` is created lazily in `evolve/evolve.db`; `evolve/db.py` is untouched and dropping
the table loses nothing the loop depends on.

```sql
SELECT key, scenario, passed, trigger FROM scenario_results WHERE suite_version = 'v1';
SELECT scenario, SUM(passed), COUNT(*) FROM scenario_results GROUP BY scenario;
```

`SUITE_VERSION` in `registry.py` is part of the primary key and of the trace cache key: bump it when
a world or a threshold changes, so verdicts taken under an older definition are never silently
compared against new ones.

## Cost

About 10-12 seconds per candidate for all five scenarios at 3 seeds (15 traced games), cached under
`evolve/scenarios/cache/` by (agent sha, opponent sha, engine, config, seed). `trace.traced()`'s own
cache is deliberately **not** reused: its key omits the engine configuration, so two scenarios with
different worlds would collide on it.
