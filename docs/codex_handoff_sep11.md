# Kaggriculture handoff brief — Sep 11 discovery-phase workstreams

Context for whoever picks this up cold: this is a Kaggle competition agent project (farming-sim game,
two-seller economy). The project has a hard-won governance framework that every workstream below must
follow. Read this whole brief before writing any code — the framework exists specifically because two
earlier leads (SHEEP herd-gate, shed-overflow pricing) looked like real signal from correlation/decomposition
alone and both died when actually causally probed. Don't repeat that.

Full canonical source: project memory file `kaggriculture-research-sequence-sep11-v2.md` (read via
`project_memory_read` if you have access to it; otherwise this brief is a faithful condensation).

## The hard rule (applies to every workstream below, no exceptions)

**A residual, correlation, worst/best split, or decomposition may NOMINATE a mechanism, but cannot
itself NOMINATE A CANDIDATE.** A candidate (a new O-number / submission) requires a separately specified
causal probe showing that changing the proposed lever changes the relevant mechanism. Do not write a new
candidate file off any of the workstreams below without a causal probe result to back it.

## The four-layer funnel (apply to every knob/assumption before it can become a candidate)

1. **Binding** — does the knob/assumption actually determine decisions, and how often, across a
   REPRESENTATIVE decision population (not just a few traced cases)?
2. **Sensitivity/error** — when it binds, how different would the decision be under a pre-defined,
   explicitly justified comparator? (Never invent the comparator casually — justify it before using it to
   declare the current value "wrong.")
3. **Economic exposure** — how much downstream inventory/revenue/capital allocation is exposed by the
   layer-2 decision delta? Quantify before any panel test.
4. **Probe tractability** — can the suspected error be isolated with a clean causal intervention,
   independent of exposure size?

If a knob fails layer 1 (rarely binds) or layer 2 (binds but the delta is economically trivial), STOP —
report that and move on. Don't proceed to layers 3-4 on something that already failed.

## Pre-registered sampling standard (use this for every Layer-1 measurement, don't invent your own)

- **Population:** 4 real opponent tapes (`Opponents/tape_peterparker_106816877.py`,
  `Opponents/tape_alaylm_106813359.py`, `Opponents/tape_bahaenes_106828159.py`,
  `Opponents/tape_yangkuang2_106819729.py`) x both seats x two independent 20-seed sets (so 40 seeds total)
  x `KAGG_FIXED_SHOPS=1` x full game horizon (29 days) = 320 games per full Layer-1 measurement.
- **Report decision coverage, not game coverage:** eligible decisions -> bound decisions ->
  counterfactual-different decisions -> economically material decisions (state your materiality threshold
  explicitly). Never report only "bound in N% of games."
- **Phase slices:** always break results into early (day 0-9) / mid (10-19) / late (20-29) as diagnostics
  for regime dependence, in addition to the full-horizon headline number.
- **Pilot before full population:** verify instrumentation on a small sample (2-4 games) first. A pilot
  result CANNOT be used to promote a knob past Layer 1 — only the full 320-game population can.
- Deviating from this population requires a stated mechanism-specific reason, not convenience.

## Current champion / baseline

`candidates/O26_CARROT_SIZING.py` is the baseline policy every trace should run as CAND. Don't use an
older lineage file (K.py, V3_*, etc.) — those are historical.

## Workstream 1: evidence-normalization pass for the three flagged dormant knobs

**Status: not started. Fully independent of the DEMAND_SHARE work, safe to run in parallel.**

Knobs: `melon_rush` (see `candidates/O6_MELON_RUSH.py` for original lineage before reusing the name),
`wheat_water_tier`, `straw_delay`. All three live as `KNOBS[...]` overrides in `O26_CARROT_SIZING.py` and
are gated in named functions: `_harvest_ready` / `_unit_action` (melon_rush), `perceive` (wheat_water_tier),
`economy` (straw_delay, gated on `obs["day"]` vs `CROP_SPECS["STRAWBERRY"]["cutoff"]`).

An existing tool, `tools/dormant_knob_engagement.py`, already instruments these three via monkeypatching
(NOT sys.settrace -- these are separate named functions, unlike DEMAND_SHARE's inline block, so the
simpler monkeypatch pattern already used in that file is the right one; don't rebuild with settrace). It
was run on a small sample and found all three "engaged" (branch reachable, behavior changes in traced
cases).

**The task:** that existing result is WEAKER than this funnel's Layer 1 bar. Layer 1 asks "how often does
it bind across the representative population" — the existing tool only checked reachability/behavior
change on a handful of games. Do NOT treat "engaged" as "Layer-1 passed." Concretely:

1. Read `tools/dormant_knob_engagement.py` in full and map exactly what each of its counters
   (`melon_rush_dispatch_opportunities`, `wheat_water_tier_opportunities`,
   `straw_delay_window_turns`, etc.) actually measures against the Layer-1 definition above.
2. Extend or rerun it (or write a new small tool following its exact non-invasive monkeypatch style —
   it explicitly avoids reimplementing engine/dispatch logic, keep that discipline) across the full
   pre-registered 320-game population, with results split by phase and reported as eligible -> bound ->
   (if feasible) counterfactual-different.
3. For each of the three knobs, report a clear verdict: PASSES LAYER 1 (proceed to layer 2) or FAILS
   LAYER 1 (rarely binds at representative scale — stop, log as such).
4. Do not proceed to layer 2 (sensitivity) for a knob until its layer-1 verdict is in.

Output: update (or create) a project-memory-style writeup with per-knob layer-1 verdicts. Do not write
any candidate/O-number file from this workstream — that requires layers 2-4 first.

## Workstream 2: triage the four remaining engaged-but-untriaged knobs

**Status: not started, one tier behind workstream 1.**

Knobs: `wheat_tiles` + `wheat_per_animal` (treat as one lever, they interact), `wheat_stock`,
`wheat_hold_days`, `fert_carry`. These were flagged as "reachable/engaged" in the original dormant-knob
audit but not yet confirmed as "substantial engagement" the way the three in Workstream 1 were.

**The task:** run the same evidence-normalization pass as Workstream 1 for these four (or three, given
wheat_tiles+wheat_per_animal is one lever) — first establish what evidence already exists for each, then
run/extend `dormant_knob_engagement.py`-style instrumentation to get real Layer-1 verdicts at
representative scale. Report which of these clear Layer 1 and are worth carrying to layer 2.

## Workstream 3: cross-gene state-read/state-write interaction map

**Status: not started. Independent, low-risk, explicitly time-boxed in the plan — do not let this expand.**

Goal: for each already-DO'd "gene" (validated mechanism currently folded into `O26_CARROT_SIZING.py`'s
lineage — check `docs/research-governance.md` and the AGE-363 gene-pool framework for the list), record
what game state it reads and what state it writes/changes, and which subsystem/time-window it operates in.
Then flag pairs where gene A changes state that gene B reads — those are the only pairs worth considering
for future crossbreeding/combination candidates (per the gene-pool framework already in project memory,
`kaggriculture-gene-pool-crossbreeding-framework-sep11.md`).

**Strict budget: this is code-archaeology, cap it at a half-day-equivalent of effort.** If
`O26_CARROT_SIZING.py`'s architecture makes a clean read/write map expensive to produce (deeply
interleaved state, no separable functions per gene), STOP and report that finding — do not keep digging.
Deferring with a clear reason is a valid, useful outcome here, not a failure.

Output: a table (gene -> state read -> state written -> subsystem -> time window) plus a short list of
flagged interaction-worth pairs, or a documented reason for deferring.

## What NOT to touch (currently owned, do not duplicate or conflict)

- **DEMAND_SHARE Layer-1 trace** (Thread B, `tools/demand_share_binding_trace.py`) — pilot already run
  and verified (4 games), full 320-game population run is queued next. Don't rerun or modify this without
  checking in first; a second agent running it concurrently against the same `kaggriculture.db` risks
  write contention.
- **Yield constants (WHEAT/TOMATO/MELON) Layer-1 trace** — intentionally NOT started yet. The plan
  explicitly sequences this after DEMAND_SHARE finishes, so its funnel can be validated as a reusable
  template first. Don't start this without checking whether that sequencing still holds.

## Memory / write discipline

- Never quote a naked money or game-count figure without stating policy/opponent/seeds/shops/seats/metric
  alongside it (established project convention — see
  `kaggriculture-governance-panel-qualified-numbers-and-memory-writes-sep11.md`).
- If you use `project_memory_write`, read the target file (or `MEMORY.md`) immediately before writing —
  there's no version guard, and a stale overwrite is a known failure mode on this project.
