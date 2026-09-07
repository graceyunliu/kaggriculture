# RNG Path-Dependence Audit — Reproduction Instructions

This directory contains a **minimal analogue** experiment, not the production
Kaggriculture engine. It demonstrates the exact RNG-coupling mechanism found
by code inspection in
`vendor/kaggle_environments_engine_master/kaggriculture.py::_end_of_day()`
(lines ~869-891): weed-spawn rolls and the periodic town-shop-unlock draw
share one `random.Random` object per day, and the weed-spawn roll only fires
on empty board tiles — so the number of draws consumed before the shop draw
depends on how many tiles a policy has occupied, i.e. it is policy-dependent.

**This script does not import or execute the real game engine.** It
reimplements the same code shape (same short-circuit condition, same
per-day reseeding formula `(seed * 1_000_003) ^ day`, same draw order:
weeds first, then shop-unlock) in isolation, so the mechanism can be
inspected without needing a full running episode. See
`artifacts/rng_path_dependence_audit/REPORT.md` for the full audit,
including why this distinction (minimal analogue vs. production engine)
matters for how much weight to put on the result.

## Files

- `repro_rng_path_dependence.py` — the experiment. Self-contained, stdlib only.
- `rng_path_dependence_results.json` — generated on run; full per-day data for both synthetic policies.

## How to run

Requires only Python 3 standard library (`random`, `copy`, `json`) — no
project dependencies, no need to activate any virtualenv or install
anything.

```bash
cd experiments/RNG_PATH_DEPENDENCE_AUDIT
python3 repro_rng_path_dependence.py
```

## What it does

1. Defines two synthetic "policies" that differ only in what fraction of a
   10x10 board is occupied by end of day: `POLICY_SPARSE` (10% occupied,
   ~90 empty tiles/day) and `POLICY_DENSE` (90% occupied, ~10 empty
   tiles/day) — standing in for two real policies that plant/build at
   different rates.
2. Runs both policies for 30 simulated days under the **identical seed**
   (`12345`), using the same per-day RNG construction formula as production:
   `rng = random.Random((seed * 1_000_003) ^ day)`.
3. Each day, spawns weeds tile-by-tile with the same short-circuited
   condition as production (`if tile is None: draw = rng.random()`),
   counting how many draws were consumed.
4. On town-shop-unlock-interval days (every 3rd day, matching the
   production default `townShopUnlockInterval`), draws
   `rng.choice(sorted(SHOPS))` from the **same** rng object, immediately
   after the weed loop — exactly mirroring production's call order.
5. Prints, and writes to `rng_path_dependence_results.json`, a day-by-day
   comparison of weed-draws-consumed and the resulting shop pick for both
   policies, plus a summary of how many of the 10 shop-unlock checkpoints
   diverged between the two policies despite the identical seed.

## Expected output (recorded from an actual run this session)

```
Total shop-unlock checkpoints: 10
Diverged (different shop unlocked despite identical seed): 7
Same pick despite different draw counts: 3
```

Because `random.Random` is deterministic given its seed and call sequence,
re-running this script produces byte-identical output every time — there is
no run-to-run variance to worry about when reproducing these numbers.

## Relationship to the production engine

This is explicitly a **minimal analogue**: it is a faithful structural copy
of the relevant ~15 lines of production logic, run in isolation, not a run
of the actual multi-thousand-line Kaggriculture interpreter with two real
competing agent policies. It demonstrates that the mechanism identified by
code inspection is real and produces the predicted divergence; it does not
by itself prove that this mechanism explains any specific previously-observed
score gap between two real policies (that would require instrumenting the
actual engine run(s) in question — see the Limitations section of the
REPORT.md for what would be needed to close that gap).

---

## eval_protocol.py — the RNG-controlled evaluation protocol

`repro_rng_path_dependence.py` above (the Phase 2 analogue) only shows the
mechanism is real in isolation. `eval_protocol.py`, in this same directory,
is the follow-on tooling: it runs the **actual production engine** (via
`mini_engine.py`'s existing, already-used-elsewhere shim — no synthetic
reimplementation of game rules) and gives future strategy comparisons
(evolve/, TDAS, ladder tests, ad hoc A/B tests) a reusable way to run a
paired/common-seed comparison that also tells you whether a measured $ delta
is confounded by this specific RNG-coupling mechanism, instead of just
reporting "A beat B by $X".

### What it does, and why each piece exists

| Component | What it does | Why (ties back to the audit finding) |
|---|---|---|
| **Real-engine instrumentation** | Monkeypatches the loaded engine module's `_end_of_day` / `_spawn_weeds` function references (same pattern `mini_engine.py` already uses for `_commit_unit` — not a new/riskier technique) to log, per day: how many weed-spawn draws each farm consumed, and whether/what shop unlocked that day. Restored before the function returns; nothing is written to disk. | The report's coupling is specifically "draw count before the shop-unlock draw depends on board occupancy" — you cannot see this without counting draws where they actually happen, in the real engine, not a re-implementation. |
| **Common-seed / paired design** (`compare_paired`) | For each seed, runs `candidate_a vs opponent` and `candidate_b vs opponent` — same seed, same opponent, same engine/config — and reports the per-seed money delta. | Common random numbers: controls for seed variance so any distribution of deltas reflects the *candidates* differing (report's Phase 3 "Paired-seed evaluation" row), while keeping the exact same-day/same-seed conditions the coupling needs to be checkable. |
| **Trajectory divergence checkpoint** | For each paired game, checks whether the two arms' `town["unlocked_shops"]` sequences ever diverge (`trajectory_diverged`, with the first day it happened), and separately whether the candidate's own weed-draw count differed that day (`action_diverged`). | Directly implements the report's Phase 4 vocabulary: ACTION DIFFERENCE (did the candidate's occupancy actually change?) vs. TRAJECTORY DIFFERENCE (did the shop-unlock state actually change as predicted?) vs. OUTCOME DIFFERENCE (the $ delta) — so a $ delta on a trajectory-diverged seed is flagged, not silently trusted. |
| **Paired distribution report** | Reports mean delta, sample stdev, t-stat, win/loss/tie counts across the seed set — not a single trajectory. | Matches the ROBUST CAUSAL MECHANISM bar in the report's Phase 4: a single-seed "A beat B" is exactly the shape of claim the audit shows can be RNG-path luck. |

### How to run it

```bash
cd /path/to/Kaggriculture
python3 experiments/RNG_PATH_DEPENDENCE_AUDIT/eval_protocol.py \
    CANDIDATE_A.py CANDIDATE_B.py OPPONENT.py \
    --seeds 1 2 3 4 5 6 --engine master --both-seats \
    --out results.json
```

`CANDIDATE_A.py` / `CANDIDATE_B.py` / `OPPONENT.py` must each define a
top-level `agent(obs, config)` function, exactly the format `mini_engine.py`
already expects — any existing candidate/opponent file works unchanged. Add
`--both-seats` to also run each seed with candidate/opponent seats swapped
(doubles the sample). Programmatic use:

```python
from eval_protocol import compare_paired
report = compare_paired("A.py", "B.py", "OPPONENT.py", seeds=range(1, 11))
report["mean_delta"], report["t"], report["seeds_trajectory_diverged"]
```

### How to interpret the output

- **`mean_delta` / `t` / `wins`-`losses`-`ties`** — the paired-seed distribution.
  Per the report's Phase 4, treat a result from a small seed set as
  PRELIMINARY, not confirmatory; re-check on a fresh, disjoint seed set before
  calling it robust.
- **`n_action_diverged` / `action_divergence_first_day`** — confirms the
  intervention actually changed board occupancy (a prerequisite the report
  calls "cheap to check, catches no-op interventions early").
- **`n_trajectory_diverged` / `seeds_trajectory_diverged`** — the RNG-coupling
  fingerprint from the audit: a shop-unlock outcome that differed between the
  two arms **despite identical seed and identical opponent**. A $ delta on a
  seed flagged `trajectory_diverged: true` is NOT yet safe to call a policy
  effect — it may be entirely explained by which shop happened to unlock,
  unrelated to the candidates' intended mechanism. Cross-check: does the
  delta's sign/magnitude still hold on the seeds that did NOT diverge? If not,
  that is itself evidence the effect is path-dependent luck (per the report's
  recommendation to classify such cases as PATH-DEPENDENT LUCK, not a robust
  policy effect, mirroring the project's existing M2-exploit-vs-general
  precedent).
- **What counts as "robust"**: an effect that (1) shows up as `action_diverged`
  where expected, (2) has a consistent-sign delta across BOTH diverged and
  non-diverged seeds, and (3) survives a fresh seed sample disjoint from
  whatever it was discovered on.
- **What counts as "just path-dependent luck"**: a mean delta driven mostly or
  entirely by the seeds flagged `trajectory_diverged`, with inconsistent or
  reversed sign on the non-diverged seeds.

### Validated example run (this session, real engine, `--engine master`)

Ran once against the actual vendored engine (not the analogue) with three
throwaway demo agents built only to exercise the harness —
`demo_agents/agent_planter.py` (sweeps the board, plants WHEAT wherever it
lands → occupies many tiles) vs. `demo_agents/agent_passive.py` (always PASS,
occupies zero tiles) — both against a fixed `demo_agents/agent_opponent.py`
(carrot loop copied from the engine's own `starter_agent` reference), 6 seeds,
one seat each:

```
agent_planter.py vs agent_passive.py  (common opponent: agent_opponent.py, engine=master)
n=6 paired games   mean delta $-47   stdev $5   t=-22.14
wins 0  losses 6  ties 0
action-diverged (candidate's own board occupancy differed that day): 6/6 games
trajectory-diverged (shop-unlock state ever differed between arms): 6/6 games  seeds: [1, 2, 3, 4, 5, 6]
```

This is a real, end-to-end confirmation that (a) the harness runs against the
actual production engine without errors, (b) `action_diverged` correctly
fires (the planter genuinely occupies more tiles than the passive agent, from
day 1), and (c) `trajectory_diverged` fires on every seed here — expected,
since these two demo agents were deliberately built to maximize occupancy
contrast, so they are close to a worst-case for this specific coupling. The
demo agents are throwaway validation fixtures only (not strategy candidates,
not evaluated for game quality) — do not use them for anything beyond
confirming the harness works.

### Known limitations / TODO

- `compare_paired` currently assumes a fixed third-party `opponent` policy in
  the non-candidate seat; it does not (yet) support a direct candidate-vs-
  candidate paired game (no common opponent). That would need its own
  divergence semantics since both farms in a single game already share one
  day's rng object — left as a TODO if a future comparison needs it.
- The trajectory-divergence check only inspects `town["unlocked_shops"]`
  (the one coupling mechanism this audit found). It will not flag any other,
  currently-unknown RNG coupling if one exists elsewhere in the engine.
- `t`-statistic uses a simple one-sample-vs-0 paired t-test on the deltas; no
  multiple-comparison correction is applied if you run many candidate pairs.
- Not yet wired into evolve/'s loop.py or any existing regression harness —
  it is standalone tooling, meant to be imported/invoked by hand or from a
  future harness, per the task's read-only-w.r.t.-evolve/ constraint.
- Validated only against the small throwaway demo agents above, on 6 seeds,
  single seat. Has not yet been run on any real champion/candidate pair at
  scale — that is an intentional scope boundary (this task is eval
  methodology tooling, not a request to re-run or re-judge any existing
  strategy comparison).
