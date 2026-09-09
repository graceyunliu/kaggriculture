# Phase 10: Lead 5 -- fertilizer target-tile eligibility timing

**Verdict: CONFIRMED.** A real, statistically robust, replicated,
causally-isolated positive score effect. This is the first CONFIRMED
result from the mining campaign. Still not promoted anywhere -- diagnostic
only, per standing constraints.

## Executive summary

Phase 2 explicitly flagged fertilizer target-tile eligibility as never
properly reconstructed: it used `FERTILIZER stock > 0` as a coarse proxy
for "a fertilize decision was live," noting this likely over-counts real
opportunities. This phase found and manipulated the actual eligibility
gate: `_fert_eligible()` (`candidates/V3_15.py:157`), which requires
(among other conditions) `age >= c["first"] - 1` -- a crop tile only
becomes fertilizer-eligible once it's within 1 day of its first
fertilizable growth stage.

**Baseline verification:** `baseline_V3_15.py` is a plain, unmodified copy
of the current champion (confirmed current per Phases 6/8/9's checks) --
no separate representativeness check needed, since this test compares
the current champion directly against a minimal, isolated change to its
own logic.

**Variant:** `variant_fert_earlier.py` -- single-line change,
`age >= c["first"] - 1` -> `age >= c["first"] - 3` (tiles become eligible
2 days earlier in their growth cycle). Otherwise byte-identical.

## Methodology -- applying Lead 4's lesson from the start

Per the coordinator's explicit instruction after Lead 4's false-positive
scare, this test used the **direct head-to-head harness**
(`mini_engine.evaluate()`, the same tool `evolve/cascade.py` uses for real
candidate scoring) as the primary and first test, rather than an indirect
vs-external-opponent design that could produce a misleading absolute-money
signal.

| test | seeds | n (both seats) | mean margin/game (variant-baseline) | t |
|---|---|---|---|---|
| batch 1 | 1-100 | 200 | +$478.42 | 2.45 |
| batch 2 (fresh) | 201-300 | 200 | +$623.17 | 2.97 |
| **pooled** | -- | **400** | **+$550.80** | **3.84** |

Both independent batches are individually significant (t > 2.4, n=200
each) and land in the same direction and similar magnitude -- this is a
real replication, not a single lucky draw (which is exactly what Lead 4's
first batch turned out to be).

**Cross-design corroboration:** re-tested both agents against an external
opponent tape (`Opponents/tape_kwa_105860490.py`, 25 seeds, both seats):
variant scored $95,989/game vs. baseline's $93,743/game (+$2,246/game,
consistent direction). Unlike Lead 4, where the external-opponent design
and the head-to-head design *disagreed*, here both designs agree.

## Pre-registered predictions (checked separately)

1. **Does the intervention change fertilizer-application timing/rate?**
   By construction, yes -- the eligibility window opens 2 days earlier per
   tile, mechanically increasing the number of fertilize-eligible
   tile-days. Not separately re-measured via trace mining this round
   (the score result below is the decision-relevant outcome); this is a
   direct, deterministic consequence of the code change, not something
   that needed a stochastic check.
2. **Does realized fertilizer application / production increase in the
   expected direction?** Not separately decomposed into a production
   metric this round -- folded into the final-money outcome (prediction
   4), consistent with how Phase 7 treated its analogous prediction 2.
3. **Downstream cash/inventory consequence?** Not separately decomposed.
4. **Does the score effect survive fresh seeds?** **CONFIRMED** -- see
   table above; batch 2 (fresh seeds 201-300) replicates batch 1's effect
   with even larger magnitude and significance.

## RNG/side-effect audit

`_fert_eligible()` is a pure function of crop age, growth-stage constants,
and `fertilized_until_day` -- no RNG call anywhere in it or its only
caller (`_build_sweep`'s "fert" tier target selection). `FERTILIZE`
itself is a deterministic engine action (no RNG in its commit path). No
RNG-path contamination possible from this change by direct code
inspection -- **RNG_INDEPENDENT**, matching the discipline established in
every prior phase.

## Why this is different from Lead 4's false positive

Lead 4 showed a marginal, non-replicating signal from an indirect design
that the direct head-to-head test overturned. Lead 5 was tested with the
direct head-to-head design as the PRIMARY test from the start (per your
explicit instruction after Lead 4), replicated across two independent
200-game batches with consistent sign and magnitude, and corroborated
under a second, different design (vs. external opponent) that agrees with
rather than contradicts the head-to-head result. This is the pattern the
audit's promotion-criteria doc actually asks for.

## Standing constraints honored

`variant_fert_earlier.py` and `baseline_V3_15.py` are experiment-only
copies under `experiments/`. No champion, submission,
`evolve/cascade.py`, or parent-selection files touched or modified in any
way. **This CONFIRMED result is diagnostic evidence only -- it is
explicitly NOT an adoption recommendation and has not been promoted,
merged, or wired into the evolution pipeline in any way**, per the
standing constraint that a CONFIRMED finding from this investigation
remains "validated diagnostic evidence," not something committed into
`evolve/`.
