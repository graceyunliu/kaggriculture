# Research governance: direction lifecycle (AGE-361) and evidence contract (AGE-362)

Written from what the O12 → O26 programme actually did by hand, so the loop stops rediscovering it. Two artifacts:

* `evolve/directions.yaml` — the ledger: every direction as DO / DELAY / ABANDON / SWITCH with the evidence that
  produced the state. `evolve/directions.py` validates it and renders it into the proposer prompt and the run report.
* `EVIDENCE_CONTRACT` in `evolve/directions.py` — how much evidence a claim of each intervention type needs before
  anyone (loop or person) may move it to DO or ABANDON.

Neither pretends the loop invents research strategy. They preserve the decisions and the reasons, and they gate what
counts as enough evidence.

## AGE-361 — the direction lifecycle

```
direction
  ↓ hypothesised mechanism        (which of the five self-model questions does it correct? produce / cost / arrive / displace / market)
  ↓ cheapest discriminating measurement   (an instrument, run on both farms where possible)
  ↓ evidence state                (see the contract below)
  ↓ DO / DELAY / ABANDON / SWITCH
```

### DO — pursue now
Required fields: `mechanism`, `intervention`, `evidence` (own money AND margin, ≥2 seed sets), `held_out`.
A direction graduates when the mechanism is specific and measurable, the measurement confirms it, one narrow
intervention produces a reproducible gain on both metrics, and fresh seeds agree.
Examples: `strawberry_yield_sizing` (measured yield 6–7.5 vs assumed 4.5 → one constant → own +5.5k, replicated),
`hire_marginal_price`, `melon_arrival_vs_pool`, `crop_orchestrator`, `carrot_yield_sizing` (the weakest).

### DELAY — plausible, but the information needed to choose the intervention is missing
Required: `unknown`, `resolving_measurement`, `would_do`, `would_abandon`, `cost`.
This is the most valuable state now. It is not "we don't know" — it names the measurement that would settle it and
the outcome that would move it either way.
Examples: `adaptive_melon_timing` (sweep h6–h10 segmented by state before building adaptation — a cheap
measurement that may save an architecture), `investment_readiness_threshold` (lumpy capital needs ≥32 cells before
its sign is readable), `strawberry_early_death` (needs a single-tile trace, not another courier).

### ABANDON — the premise was tested and failed, at a stated scope
Required: `hypothesis`, `measurement`, `negative_evidence`, `scope`, `reopen`.
An ABANDON closes a *mechanism at a scope*, never a topic forever. `per_task_delay_var` is not "VaR V1 didn't
work"; it is "within-day per-action urgency has no measurable consequence on the O16+ dispatcher (3,060
counterfactuals, all CIs through zero) and the service ledger finds no chronic debt". The only thing that reopens
it is a new instrument or a changed premise — never a new parameter value.
Also abandoned: `worker_matching`, `chronic_service_debt`, `fertilizer_output_maximisation`,
`tape_wheat_portfolio_knobs`, `speculative_inventory_holding`, `capital_timing_input_price_attack`.

### SWITCH — the question survived, the mechanism changed
Required: `original_hypothesis`, `failed_assumption`, `became`, `evidence`.
Examples: `late_game_roi_thresholds` → `hire_marginal_price` (class cutoff measured the subsystem, not the marginal
unit; the marginal instrument found the fibonacci wage tail). `more_strawberry_output` → `strawberry_yield_sizing`
(the tapes' advantage was fewer plantings at the same output, not more output).

### Override
A person may move any record with a comment in the ledger. Two rules bind people too: a DO needs the contract depth
below, and an ABANDON is reopened only by a new instrument. The loop never writes the ledger; it reads it (proposer)
and reports it (report).

## AGE-362 — the evidence contract

The last week's uncertainty failures, each of which cost a day: a 3-seed animal result flipped; a 12-cell lumpy-capital
result dissolved at 32 cells (with a sign flip); M=89 won dev seeds and lost held-out; a one-seed VaR table vanished
across the panel; a +margin capital candidate was −own money; O18 stacking looked additive and wasn't. The common
cause: the amount of evidence a claim needs depends on the *kind* of intervention, and we were applying one depth.

Reframed from the ticket: this is **research option value** — when should the loop spend another experiment to reduce
uncertainty rather than commit to (or close) a direction? Not runtime game-policy option value.

| intervention type | min depth (seeds × independent sets) | metrics | extra requirement | guards against |
|---|---|---|---|---|
| calibration (a corrected constant) | 20 × 2 | margin + own | positive on every tape | tape-specific "calibrations" |
| knob | 20 × 2 | margin + own | parameter chosen on held-out | dev-set selection (M=89) |
| threshold | 20 × 2 | margin + own | dose-response with interior optimum | monotone artefacts |
| nonlinear / adaptive threshold | 20 × 2 | margin + own | fixed-cutoff sweep segmented by state *before* adaptation | building a scheduler for a constant |
| lumpy capital (animals, land) | **32 × 2** | margin + own | marginal caps, not class ablation | sign flips at 12–24 cells |
| architecture | 20 × 2 | margin + own | compare to the immediate parent | h2h-vs-frontier as a ranking |
| market interaction | 20 × **3** | margin + own | classify: both up = core; margin up/own down = exploit; own up/margin flat = spillover | price attacks, wheat-hold spillover |

Universal rules: development and confirmation panels are separate and both recorded; a one-seed or one-tape
observational table is a hypothesis, never a weight; noise floor $250 per metric (`cascade.classify_gain`).
`python3 evolve/directions.py --check <type> <seeds> <sets>` answers "is this enough to decide?".

## How the two fit together

```
candidate direction
   ↓ mechanism hypothesis (self-model question)
   ↓ cheapest discriminating measurement
   ↓ enough evidence for this type?   (contract)
        no  → DELAY, with the resolving measurement named
        yes → test one narrow intervention on both panels
                 ↓
              DO / SWITCH / ABANDON   (ledger)
```

Priority order agreed Sep 11: (1) resolve the open DELAYs that are attached to the next candidate (adaptive melon
timing sweep; strawberry early-death trace); (2) keep the ledger current — a direction that is not in it has not been
decided; (3) only then return to open-ended candidate discovery.
