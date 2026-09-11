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

Priority order (Sep 11, current): the melon family is closed on every proposed axis -- entry-state adaptive cutoff
(ABANDON, 2,240-game sweep), urgent-exemption triggers (ABANDON, O30/O31/O32 negative on all four tapes at 1,440 games),
and deferred-pickup recoverability (ABANDON, tools/melon_trace.py: no lost sales, the unit delta is a d10-11 replant count,
money does not track melon units). `hire_gate_output_loss` is closed too (ABANDON: the fertilizer + weed-recovery
accounting bridge covers <20% of the $504 residual with no concentrated class, N=165 unbiased weed sample; keep
HIRE_MAX_MARGINAL=144). `investment_readiness_threshold` resolved SWITCH: BUY_ANIMAL's marginal sign is unmeasurable at
32 cells (flips between two independent seed sets, matching the pre-registered would_abandon condition) and stays a
hand threshold; BUY_LAND's marginal sign is stable and significant through day 10, decaying to noise by day 12 -- real
but observational, not yet a tested intervention. `land_deadline_horizon` was then tested and ABANDONed: pulling the hand-tuned LAND_DEADLINE (14/17/18 by quad tier)
in to track the marginal-value decay (O33_LAND_DEADLINE_TIGHT, {2:11,3:13,4:14}) lost on both own and margin, on
all four tapes on the stronger seed set. Lesson: the marginal counterfactual measured the value of the LAST land
unit under the unchanged policy; it did not see the option value of completing a quad early enough to use the extra
tile-days for the rest of the game, and tightening the deadline threw that away too. Ledger is now DO 5 / DELAY 0 /
ABANDON 14 / SWITCH 4 -- every inherited direction from the O12-O26 programme is closed. Keep the ledger current --
a direction that is not in it has not been decided -- and the loop now moves to open-ended candidate discovery from
the K_SELFMODEL chassis.

Durable rule from the melon programme: a protected block (the h<=8 convoy) tolerates EDGE TRIMMING (h7 vs h8, +$250)
but not INTERIOR INTERRUPTION (every urgency-shaped hole lost on all four tapes). Champion record: O26_CARROT_SIZING is
the verified champion with a "weakest pass" annotation; O25-vs-O26 for the ladder is an explicit deployment-risk decision,
not a redefinition of the champion.

## AGE-363 — gene pool and crossbreeding (portfolio, not single winner)

The ledger above (AGE-361/362) governs how one direction gets tested and closed. This section governs what
happens *after* a direction reaches a terminal state: how validated mechanisms combine. The champion is not "the
best single idea" — it is the best-tested composition of independently validated mechanisms. Do not assume there
can be only one winning candidate; think in terms of a candidate portfolio.

### The operational default this creates

**A small validated positive is not required to justify submission alone; it is required to justify preservation
and future combination testing.** This is the practical rule the four labels above exist to enforce. It heads off
both failure modes at once: discarding a modest positive gene because it isn't ladder-worthy by itself (it still
enters the pool and gets tested for combination), and randomly stacking every historical idea together and
calling the resulting pile innovation (only genes with a plausible interaction get crossbred, per the discipline
below).

### Four labels (do not conflate them)

A DO or ABANDON in the ledger is not automatically a "gene." Use these four labels, and keep them distinct:

* **🧬 positive gene** — a DO'd mechanism that is a genuine reusable component: it can be combined with other
  positive genes and tested for interaction. Eligible for crossbreeding.
* **⛔ negative constraint** — an ABANDON'd mechanism/intervention. Valuable in the knowledge base because it
  constrains future search (don't re-try this without new evidence), but it is NOT a component — it is never
  crossbred into anything. Every negative constraint carries a stated reopen condition (a new instrument or
  changed premise, per AGE-361's ABANDON rule), never "try it again later."
* **🔬 candidate family** — a direction currently under isolation/validation (roughly: DELAY, or a DO-in-progress
  Stage-1 variant set like buy-alone/sell-alone/combined). Not yet eligible for crossbreeding either way; it
  graduates to a positive gene or drops to a negative constraint.
* **🏆 champion composition** — the current best validated combination of positive genes running as the actual
  submitted policy. Framed as a composition, not as "the winning idea," so a later gene can be added to it without
  implying the old champion was wrong.

The failure mode this guards against: a future session reads "goose_animal_class" or "land_deadline_horizon" in
the pool and treats it as an ingredient available for crossbreeding because it's a "validated mechanism." It is
validated, but validated-negative — a constraint, not a gene. Only 🧬 positive genes go into Stage 2 crossbreeding
below.

### Three outcomes when positive genes combine

Two positive genes A and B combine one of three ways:

1. **Additive** (ideal) — A and B touch separate parts of the economy; combined gain ≈ gain(A) + gain(B).
2. **Redundant** — A and B fix the same underlying mechanism; combined gain ≈ gain(A) alone (or B alone,
   whichever is larger). Not a failure — it tells you the two "different" ideas were one mechanism wearing two
   names.
3. **Interactive** — A changes the state B operates on (e.g. capacity-aware selling frees shed headroom, which
   changes when a harvest-cutoff policy should stop growing). Combined gain can beat A+B, or come in below either
   alone. Neither was designed around the other; the interaction is discovered, not assumed.

All three are legitimate findings and get recorded next to the two genes in the ledger, not just as a combined
number.

### Crossbreeding discipline — don't combine everything with everything

Combinatorial testing of all positive-gene subsets is combinatorial chaos and destroys the evidence discipline
AGE-362 exists to protect. The rule:

> Validate mechanisms individually first (full AGE-361/362 lifecycle to DO, i.e. to 🧬 positive gene). Crossbreed
> only positive genes that have a plausible interaction — one plausibly changes the state the other reads or acts
> on. Never crossbreed a ⛔ negative constraint into anything. Do not crossbreed two positive genes with no causal
> story for why they'd interact; that pair stays two separate genes in the pool, run together only as part of the
> eventual full champion composition.

Worked shape, e.g. for a shed-capacity 🔬 candidate family with a buy-side gate and a sell-side override that are
part of one causal chain (buy gate controls inflow, sell override controls outflow, both act on the same shed-load
state — a plausible interaction by construction):

```
Stage 1 — mechanism isolation: buy gate alone / sell override alone / combined
Stage 2 — promotion: compare combined vs sum of the two alone
  additive-or-better (e.g. buy +500, sell +2,000, combined +3,500) -> combined is a candidate positive gene
  destructive (e.g. buy +500, sell +2,000, combined +1,800)        -> keep as two separate positive genes,
                                                                       record the interference in the ledger
```

### Six-stage pipeline (supersedes "one idea wins")

1. **Discovery** — why is money being lost? (self-model questions: produce/cost/arrive/displace/market)
2. **Isolation** — build the minimal candidate variant for one mechanism at a time (🔬 candidate family).
3. **Validation** — AGE-362 evidence contract, real panel, held-out seeds. Promotes to 🧬 positive gene (DO) or
   ⛔ negative constraint (ABANDON, with a stated reopen condition).
4. **Gene pool** — 🧬 positive genes and ⛔ negative constraints both accumulate as a reusable library. Only the
   positive genes are combination material; the negative constraints exist purely to stop re-deriving dead ends.
5. **Crossbreeding** — combine only compatible 🧬 positive genes (plausible interaction, both survived DO
   independently). Test whether A+B beats A and B, and classify the result additive / redundant / interactive.
6. **Champion selection** — the 🏆 champion composition is the best-tested combination of positive genes, not the
   single highest-h2h idea. A 🔬 candidate family that resolves to a ⛔ negative constraint is still a healthy,
   recorded output, not a failure to force into the champion.

### Why this matters here specifically

Recent closed directions are ⛔ negative constraints, not genes — exactly the "healthy discoveries that didn't
produce candidates" this framework expects: `goose_animal_class` (dead knob, reopen condition: none stated, code
path would need to change), `weed-recovery`/hire-gate bridge (mechanically real, economically not recoverable;
reopen: a new accounting instrument), `land_deadline_horizon` (real marginal signal, but the intervention built
around it lost; reopen: an instrument that captures quad-completion option value, not another deadline sweep).
None of these three are eligible for crossbreeding under any circumstance.

`shed_overflow` (as of the Sep 12 correction) is currently a 🔬 candidate family (DELAY) with a concrete next
mechanism to isolate on the buy/sell axis described above, and O33 is the first clean test of whether the project
can compound small validated positives (crossbreeding two positive genes) rather than only hunting single dramatic
breakthroughs. Run its eventual buy-gate and sell-override variants through the Stage-1 isolation pattern above —
Discovery -> mechanism confirmed -> isolate buy / sell -> test buy+sell interaction -> validate survivors ->
promote successful mechanism(s) into the 🧬 positive gene pool — not as three competing standalone ladder
candidates.

### Naming collision found while writing this section — fix before crossbreeding

`candidates/` currently holds two unrelated things both called O33: `O33_LAND_DEADLINE_TIGHT.py` (the
land-deadline direction, ABANDONed -- a ⛔ negative constraint, ledger-recorded) and
`submissions/O33_FERT_DENIAL4.zip` (a fertilizer-denial change, not found in `evolve/directions.yaml` at all --
unknown label until it's run through AGE-362). Before shed_overflow survivors are tested against "O33" as an
existing positive gene, resolve which O33 is meant and, if it's the fertilizer-denial one, give it a ledger entry
and a DO/ABANDON verdict first -- an unlogged candidate is not yet a 🧬 positive gene no matter how promising it
looks, and reusing the O-number for two different mechanisms will silently corrupt any future crossbreeding note
that just says "interacts with O33."

### When to touch the ledger schema

Leave `evolve/directions.yaml` / `directions.py` unchanged until there are at least a couple of real positive-gene
combinations recorded by hand in ledger notes. Structured interaction fields (e.g. an explicit `interacts_with:`
list, or an `additive|redundant|interactive` classification field) should be designed from what those first real
combinations actually need, not speculatively. Until then, the practical hook is: when writing a DO's ledger entry,
note in free text which existing 🧬 positive genes it plausibly interacts with (shares state with, or touches the
same subsystem), so future crossbreeding candidates are easy to spot without re-deriving the causal story from
scratch.
