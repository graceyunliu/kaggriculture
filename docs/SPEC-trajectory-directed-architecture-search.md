# SPEC: Trajectory-Directed Architecture Search (TDAS)

A search lane for discovering alternative economic *architectures*, not better parameters of the current chassis. Runs alongside `evolve/loop.py` without modifying it.

---

## 1. OBSERVED CURRENT SYSTEM FACTS

These are facts about the existing pipeline, gathered by inspection, not proposals.

- **Evolutionary loop (`evolve/loop.py`)** optimizes a fixed 36-parameter space: `evolve/space.py` (24 `KNOBS`) + 12 numeric constants, rendered onto one frozen chassis (`evolve/base/K_<sha>.py`, derived from `candidates/K.py`). Mutation (`evolve/operators.py`) pairs one econ knob with one exec/labor knob; crossover recombines knob values across two parents. **Every candidate this loop can produce shares K.py's control flow.** It cannot represent a different sequence of economic states — only different constants inside the same sequence.
- **Evaluator (`mini_engine.py`)** is architecture-agnostic: it takes two arbitrary agent files (`A.py B.py`), runs them on the vendored engine, scores by final cash, and caches by content hash. It does not care whether `A.py` is a knob-rendered K.py variant or something structurally different. This means the evaluator can already score architecture-level candidates with zero changes.
- **Cascade (`evolve/cascade.py`)** is a 5-stage funnel (fingerprint → pattern-death → smoke → dev-seed → held-out-seed) built to cheaply kill bad candidates before expensive full evaluation. It is representation-agnostic in the same way `mini_engine.py` is.
- **Tracing is already built and rich.** `evolve/trace.py` computes per-day-per-player metrics (cash, net worth, sales, hands, animal/plant counts, chores, travel/idle/work turn splits) directly from engine state — no game-code changes needed to get a trajectory. `mini_engine.py --trace out.json` emits raw per-day JSON. `tools/tape_days.py` produces `day_00.json … day_29.json` + `summary.json` per game. **This is exactly the substrate a trajectory-comparison methodology needs, and it exists today.**
- **Opponent/frontier evidence already exists as data, not just belief.** `Opponents/*.py` (opp_scenario_v14, opp_frontier_v12, opp_kaito_v21, opp_soil_v25, opp_replay_shield_v15) plus ~20 `tape_*.py` agents replaying real observed trajectories, backed by `Opponents/tapes.json` and `Replays/*.json`. Prior memory work (H32/M2, M3 generalization failure) shows the frontier's edge has already been *partially* reverse-engineered for specific windows (turn-1 wheat round-trip) but a full-game causal account does not exist, and a naive port of frontier *policy* onto the current engine (`main_v_clonereplica1.py`, memory: "clone-replica") **lost decisively** (-$68k vs chassis, -$126k vs the real opponent) — so copying observed frontier actions is a known dead end; something about *why* those actions work, not the actions themselves, is missing.
- **No existing infrastructure classifies *why* two trajectories diverge, generates architecture-level hypotheses, or protects a structurally different candidate family from being crossed back into the K.py knob population.** This is the actual gap TDAS fills.

---

## 2. PROPOSED DESIGN

### 2.1 Architecture search specification

TDAS is a separate top-level directory, `arch_search/`, sibling to `evolve/`. It reuses `mini_engine.py`, `evolve/cascade.py`, `evolve/trace.py`, `tools/tape_days.py`, and `Opponents/` unmodified. It adds only what's missing: state-transition reconstruction, divergence detection, mechanism classification, causal-prediction-tested hypothesis generation, novelty gating, and a separate lineage archive. It does not touch `evolve/db.py`, `evolve/space.py`, or `candidates/K.py`.

**The center of the system is state-transition reconstruction and comparison, not raw-field divergence detection.** A first version that only diffs per-day scalar fields (§2.3's `DayState`) will surface things like "12 hands instead of 10 on day 7" — true, but not the level at which architectural differences live. What actually distinguishes one economic architecture from another is *which condition-triggered state a trajectory is in and when it transitions*, independent of the exact day or exact knob values that transition happened to occur at. `arch_search/state_machine.py` (§2.3a) sits between trajectory extraction and divergence detection for this reason.

Loop, matching the required concept:

```
frontier + candidate trajectories (tape_*.py agents, real replays, V3_12)
  -> extract_trajectory()            [reuse trace.py / tape_days.py]
  -> extract_state_sequence()        [new: arch_search/state_machine.py — condition-based, not day-indexed]
  -> find_convergent_transitions()   [new: arch_search/state_machine.py — across MULTIPLE references, not one]
  -> find_first_divergence()         [new: arch_search/divergence.py — on the STATE sequence first, raw fields second]
  -> classify_mechanism()            [new: arch_search/classify.py, human-in-loop assisted]
  -> generate_hypotheses()           [new: arch_search/hypothesize.py, each with a falsifiable multi-step prediction]
  -> instantiate_candidate()         [new: arbitrary Python agent file, any control flow]
  -> novelty_gate()                  [new: arch_search/novelty.py]
  -> evaluate()                      [reuse mini_engine.py + cascade.py]
  -> test_causal_prediction()        [new: arch_search/predict_check.py — did steps 2-4 of the prediction also occur?]
  -> update_knowledge()              [new: arch_search/ledger.db + a written finding, memory-style]
  -> repeat, seeded by the best-diverging survivor
```

### 2.2 Candidate representation

A candidate is **an agent file plus a manifest**, not a parameter vector:

```
arch_search/candidates/<family>/<id>/
  agent.py          # arbitrary Python — a state machine, phase-gated planner, etc.
  manifest.json      # {family, parent_id, hypothesis_id, mechanism_class, generation}
```

`manifest.json` is what makes candidates comparable without forcing them into a shared schema. It records *what economic mechanism this candidate instantiates* (from §2.6's taxonomy) and *which hypothesis it tests*, not its internal parameters. Two candidates in the same family may share zero lines of code.

Concretely, `agent.py` is expected (not required) to expose an explicit **phase/state variable** it transitions through (e.g. `PHASE = {"bootstrap", "scale_labor", "diversify_production", "harvest_wind_down"}`) so `extract_trajectory()` can read *declared* phase transitions in addition to *inferred* ones from raw state — this is what lets classify_mechanism() distinguish "this candidate changed its opening capital sequencing" from "this candidate just has different constants."

### 2.3 State-machine / trajectory representation

A trajectory is a sequence of day-snapshots, built entirely from existing tracer output (`trace.py` fields), not a new engine hook:

```
Trajectory = [DayState_0, DayState_1, ..., DayState_29]

DayState = {
  day, cash, net_worth,
  production_composition: {crop/animal -> count/rate},
  labor_allocation: {task_type -> turn_share},   # travel/idle/work/chore split, already traced
  investment_flow: {land, hands, animals, seed}, # deltas this day
  spatial_layout: {siting summary if available},
  declared_phase: str | None                      # from manifest-aware agents, else None
}
```

This is a thin wrapper over `evolve/trace.py` + `tools/tape_days.py` output — no new simulation instrumentation required for phase 1.

### 2.3a State-transition graph reconstruction (the center of the system)

`arch_search/state_machine.py` converts a raw `Trajectory` into a **condition-triggered state sequence**, not a day-indexed one. States are defined by economic conditions holding, not by calendar day — the same taxonomy applies whether a trajectory reaches a state on day 4 or day 9:

```
BOOTSTRAP            capital constrained, production capacity near zero
LABOR_SCALE           worker capacity growing faster than production throughput
PRODUCTION_ACTIVATION crops/animals transitioning to productive/sellable
DENSIFICATION         existing land approaching high utilization
EXPANSION_READY       production infra saturated AND cash available AND labor has slack
EXPANSION              land/animal/crop capacity increases
THROUGHPUT_SCALE       production system generating accelerating cash
ENDGAME_CONVERSION     remaining-horizon changes investment value (late-game only)
```

This taxonomy is a **starting hypothesis, not a fixed ontology** — Phase 1 step 3 (§2.10) exists specifically to test whether these conditions actually separate real trajectories cleanly, and the state list should be revised from that evidence rather than treated as given. Each state's entry condition is a boolean function over `DayState` fields (e.g. `EXPANSION_READY := land_utilization > 0.85 and cash > next_land_cost and labor_slack_turns > threshold`), so `extract_state_sequence()` can be applied uniformly to any trajectory — reference tape or candidate — without needing declared phases (§2.2's `declared_phase` is a helpful cross-check when present, not a requirement).

Output is a **state-transition graph**: an ordered list of `(state, entry_day, exit_day, trigger_conditions_at_entry)`, per trajectory. This — not the raw per-day field diff — is what gets compared across trajectories in §2.4-2.5.

### 2.4 Frontier comparison methodology: convergent transitions, not single-reference imitation

Comparing one candidate against one reference tape and imitating whatever differs is the failure mode that already sank the clone-replica attempt (§1) and the M2→M3 generalization collapse: an edge that comes from fingerprinting one opponent's exact behavior does not transfer.

TDAS instead requires a **reference panel** (the shared-clone-fingerprint tape, the budget-fork tape, and 2-3 divergent tape_*.py agents that are independently judged strong — memory's frontier evidence gives at least this many candidates) and asks, for every transition in the taxonomy: **does it appear, in roughly the same relative order, across most or all of the panel, even though the exact triggering day and exact actions differ?**

```
Transition                                          Tape A  Tape B  Tape C
LABOR_SCALE reaches capacity before EXPANSION          ✓       ✓       ✓
DENSIFICATION precedes next EXPANSION                  ✓       ✓       ?
PRODUCTION_ACTIVATION (mixed) precedes THROUGHPUT_SCALE ✓       ✓       ✓
exact crop/animal sequence                              ✗       ✗       ✗
```

Transitions that hold across the panel are treated as **candidate architecture-level invariants** — these are what a hypothesis should target. Fields that vary freely across the panel (like exact crop sequence) are treated as implementation detail, not architecture, and are explicitly *not* hypothesis material. This directly implements the "convergent transitions" check requested for TDAS and is the guard against re-deriving a fingerprint-specific exploit.

### 2.5 First-divergence detection methodology

Divergence detection runs at the **state-transition level first**, raw-field level second:

1. Compare the candidate's state-transition graph (§2.3a) against the convergent-transition set (§2.4). Find the first transition, in trajectory order, where the candidate's graph either (a) never reaches a state the panel converges on, (b) reaches it through a different entry condition than the panel's shared trigger, or (c) reaches states in a different relative order than the panel. This is "the first meaningful divergence" — an architectural one, not a parameter one.
2. Only if no state-level divergence is found (candidate's state sequence matches the panel) does the system fall back to per-`DayState`-field statistical divergence (the original method: 1.5 MAD tolerance band, ≥2 consecutive days) as a secondary, finer-grained signal.

Rank divergences by trajectory order (earlier transition = more likely upstream) but do not assume this ordering is proof of causality — it is a prioritization heuristic for a human/LLM to inspect, and §2.6's falsifiable-prediction step exists precisely because this heuristic can be wrong.

### 2.6 Causal hypothesis generation methodology

This is where the spec's core causal rule applies: a correlated metric (e.g. low travel-per-task, or "expansion happens later") must not be treated as the cause. `classify.py` forces every divergence through an explicit **mechanism taxonomy** before any hypothesis is generated:

- **Structural/architectural** — a different state-transition graph: different entry conditions, different transition order, a state the panel converges on that the candidate skips or reaches via a different trigger (e.g. reference enters EXPANSION_READY via land-utilization saturation; candidate enters an EXPANSION-like state via a fixed day-10 rule instead).
- **Consequential/derived** — a downstream effect of an upstream divergence already found earlier in the state sequence (e.g. lower travel *because* DENSIFICATION was entered earlier, which was itself caused by an earlier LABOR_SCALE divergence).

Only divergences classified as structural become hypothesis seeds. For each structural divergence, `hypothesize.py` (LLM-assisted, similar in spirit to `evolve/propose.py` but prompted with the taxonomy in §2.2's candidate categories: state machines, phase transitions, investment sequencing, production-chain systems, spatial architectures, value-per-worker-action dispatch, alternative openings) generates 2-4 competing architectural hypotheses. **Each hypothesis must state a causal claim as a multi-step, falsifiable prediction — not a single endpoint metric:**

```
Hypothesis: the reference delays EXPANSION until DENSIFICATION saturates
            (not because land is expensive, but because idle land compounds
            worse than idle capital early game).

Prediction, in order:
  1. delay land acquisition relative to the current chassis
  2. land utilization on existing plots should rise measurably before the delayed purchase
  3. the EXPANSION day itself should shift later, not just utilization
  4. production density (and eventually net worth) should improve versus the chassis

A candidate that shows step 1 but not steps 2-4 falsifies this hypothesis —
its "later expansion" was coincidental, not caused by the claimed mechanism.
```

This is what `test_causal_prediction()` (§2.1, run post-evaluation) checks: it re-runs `extract_state_sequence()` on the evaluated candidate's actual trajectory and verifies steps 2-4 occurred, not just step 1 and the final score. A hypothesis that only produces its first predicted step is logged to the ledger as **falsified**, not promising — this is the mechanism that stops the search from generating endless plausible-sounding stories that only ever get "the score went up" as evidence, which is exactly how a correlated metric gets mistaken for a cause.

### 2.7 Trajectory novelty gate

Before expensive full-game evaluation (which dominates compute cost per `evolve/cascade.py`'s design), a cheap trajectory-distance check against **the candidate's own parent**, not other families:

- Run a short simulation (day 0-10, reusing `tools/planner_bench.py`-style cheap partial execution where possible) or a single full seed.
- Compute per-field trajectory distance (§2.4's method) between candidate and parent.
- Require the distance to exceed a threshold on **at least one** of: investment sequence, production composition, or labor allocation by day 10 — mirroring the required novelty dimensions. Source-code similarity is explicitly *not* a gate criterion (per spec: don't reject on resemblance to another candidate, judge on realized trajectory) — a rewritten-from-scratch candidate whose trajectory is a near-copy of its parent is rejected here; a candidate with a small code diff whose trajectory diverges structurally passes.
- Candidates that fail this gate are logged (for pattern-tracking — repeated failure to diverge is itself informative) but not sent to `mini_engine.py`.

### 2.8 Isolation / diversity strategy

- Separate SQLite archive, `arch_search/ledger.db`, distinct from `evolve/evolve.db`. Separate `arch_search/families/` directory tree instead of `evolve/base/`.
- **No automatic crossover or migration** between an arch_search family and the `evolve/` knob population in phase 1. A family is promoted to `evolve/`'s parameter space manually, only after a human (Grace) reviews the ledger and decides a family's architecture is worth turning into a new chassis snapshot (`evolve/base/K_<new_sha>.py`) for the existing loop to then tune — i.e., TDAS *feeds* evolve/loop.py new chassis candidates, it doesn't merge into it automatically.
- Within `arch_search/`, families are isolated from each other too by default (each family's mutations/hypotheses only spawn children within that family) unless a later finding explicitly justifies cross-family recombination — this is a manual `ledger.db` flag (`cross_family_approved`), not a default behavior.

### 2.9 Integration with existing evaluator

No changes to `mini_engine.py` or `evolve/cascade.py`. TDAS candidates are plain agent files, so:
- `mini_engine.py arch_search/candidates/<family>/<id>/agent.py Opponents/opp_scenario_v14.py --seeds ... --both-seats` works unmodified.
- `evolve/cascade.py`'s 5-stage funnel is reused as-is for cheap-to-expensive filtering, called from `arch_search/` orchestration rather than `evolve/loop.py`.
- `evolve/trace.py` and `tools/tape_days.py` are imported directly by `arch_search/trajectory.py`, not reimplemented.
- `gh_push.py` is reused for pushing results, since it's already known to bypass the local git lock issue in this sandbox.

### 2.10 Minimal first implementation plan

**Phase 0 (before generating a single new candidate): reconstruct and compare economic state-transition graphs from existing trajectories.** The entire value of §2.3a-2.6 depends on the state taxonomy actually separating real trajectories — this must be checked against data before any compute is spent generating candidates against a taxonomy that might not describe the game.

0. `arch_search/trajectory.py` — wraps `trace.py`/`tape_days.py` output into `Trajectory`/`DayState` (§2.3). No new tracing.
0. `arch_search/state_machine.py` — implement `extract_state_sequence()` with the §2.3a taxonomy as a first draft, and `find_convergent_transitions()` (§2.4).
0. Run state extraction on V3_12 and the reference panel (shared-clone-fingerprint tape, budget-fork tape, 2-3 divergent tape agents). Read the resulting state-transition graphs **by hand**. Answer explicitly, before writing any more code:
   - Do the condition-based entry rules actually fire at sensible points, or does the taxonomy need different conditions / different states entirely?
   - Do the panel's trajectories actually converge on a shared transition order, or is the panel too heterogeneous for "convergent transitions" to mean anything?
   - Where does V3_12's graph first diverge from the panel's convergent set, and does that match what memory / prior investigation (three-quadrant timing, densification, etc.) already suspected?
   This manual pass is the actual deliverable of Phase 0 — its output is a validated (or revised) state taxonomy plus a first hand-identified structural divergence, written up as a ledger finding before Phase 1 begins.

Phase 1 (only after Phase 0 produces a taxonomy that holds up against real data):

1. `arch_search/divergence.py` — state-level-first divergence detection (§2.5), plus the raw-field fallback.
2. Manual classification pass (structural vs. consequential, §2.6) on the divergences Phase 0 surfaced, before building `classify.py` automation.
3. Hand-write 2-3 candidate agents (not LLM-generated yet) instantiating the most promising structural hypothesis, each with an explicit multi-step falsifiable prediction (§2.6) written down *before* the candidate is built.
4. `arch_search/novelty.py` — gate (§2.7), run on these hand-built candidates.
5. Evaluate survivors through existing `mini_engine.py` + `cascade.py`.
6. `arch_search/predict_check.py` — `test_causal_prediction()`: re-extract the state sequence of each evaluated candidate and check whether the predicted steps 2-N actually occurred, not just the final score.
7. Write findings (including falsified hypotheses, not just wins) to `arch_search/ledger.db` + a memory-style markdown note, same as current practice.

Only after step 7 produces at least one hypothesis whose full multi-step prediction was confirmed (not just the endpoint score) should `classify.py`/`hypothesize.py` be automated (LLM-in-the-loop) to scale hypothesis generation — building the automation before validating the taxonomy and the causal-prediction check on real data risks automating a bad taxonomy at scale.

---

## 3. OPEN QUESTIONS REQUIRING EXPERIMENTATION

- **Whether the §2.3a state taxonomy (BOOTSTRAP → LABOR_SCALE → ... → ENDGAME_CONVERSION) actually separates real trajectories, or is a plausible-sounding ontology that doesn't match how the game's economy actually moves.** This is the single biggest risk in the whole spec and is exactly why Phase 0 is a manual, human-read validation step before any automation — the taxonomy above is a hypothesis, not a given.
- **Whether entry conditions for each state can be written as clean boolean functions of `DayState` fields, or whether state boundaries are fuzzier than the taxonomy assumes** (e.g. a trajectory that's simultaneously densifying one quadrant and expanding into another). If states overlap or blur, `extract_state_sequence()` may need to represent partial/concurrent state membership rather than one state at a time.
- **How many reference tapes are enough for `find_convergent_transitions` (§2.4) to be meaningful, and how much disagreement across the panel is tolerable before a transition is dropped as non-convergent.** Starting with ~5 tapes is a guess; too few risks re-deriving a single opponent's fingerprint (the exact failure mode that sank M2/M3), too strict a convergence bar may throw out real architecture-level invariants that only 3 of 5 tapes happen to exhibit at observable resolution.
- **Tolerance bands for the raw-field fallback in divergence detection (§2.5):** 1.5 MAD over ≥2 days is a starting guess, not validated, and seed variance in this game is large (memory notes ladder margins ≈ seat-bias-sized) — the band may need per-field calibration against the tapes' own seed-to-seed spread.
- **Whether declared-phase instrumentation (§2.2) is necessary or whether inferred phases from raw state (§2.3a) are sufficient on their own.** Inference is cheaper to bootstrap; explicit self-reported phases are a useful cross-check but require hand-authoring every candidate with self-reporting logic, which may bias candidate design toward the taxonomy prematurely.
- **Cost of "cheap" partial-trajectory evaluation for the novelty gate.** `planner_bench.py`-style day-0-10 partial runs exist for execution benchmarking, not full economic-state comparison; whether they're accurate enough as a novelty proxy, or whether state-sequence extraction even resolves meaningfully on a 10-day partial run, needs a direct comparison against full single-seed games.
- **Where the structural/consequential classification line actually falls in practice**, even after moving the divergence check to the state-transition level — many divergences will still look ambiguous (e.g. "reaches LABOR_SCALE earlier" could be upstream cause or downstream consequence of a land-timing decision). Phase 0/Phase 1's manual passes are designed specifically to surface this before automating it, but the decision rule that will actually work is unknown until that data exists.
- **How strict `test_causal_prediction()` (§2.6) should be about partial confirmation.** A hypothesis that confirms steps 1-2 of a 4-step prediction but not 3-4 is "falsified" as written — but it may instead indicate the prediction chain itself was incompletely specified rather than the underlying mechanism being wrong. Whether the ledger should distinguish "falsified" from "partially confirmed, prediction chain needs revision" is unresolved.
- **Promotion criterion from `arch_search/` into `evolve/`'s chassis (§2.8).** "A human reviews and decides" is deliberately vague; what statistical bar (e.g. beats V3_12 across N seeds by margin M, both seats) should gate turning a family into a new `evolve/base/K_<sha>.py` chassis is not yet defined and should probably mirror `evolve/cascade.py`'s existing held-out-seed bar rather than inventing a new one.
