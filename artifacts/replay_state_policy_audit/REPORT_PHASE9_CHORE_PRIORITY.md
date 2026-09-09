# Phase 9: Lead 4 -- chore-type priority ordering (weeds vs. harvest)

**Verdict: PARTIAL_EVIDENCE -- consistently positive but not yet
statistically robust enough to call CONFIRMED.**

## Executive summary

Phase 2 measured chore *utilization* (idle vs. assigned hand share) and
found parity -- closed. It never measured chore *priority* -- which
specific task type wins when a hand has urgent/fert/harvest/weeds/water
all competing at once. `_build_sweep()` (`candidates/V3_15.py:724`)
chains tasks in a fixed tier order, currently
`["urgent", "harvest", "weeds", "water"]`. The chassis's own in-file
comment records that an earlier version moved weeds ahead of
harvest/water (weed spread compounds if left unchecked), circumstantial
evidence this exact ordering choice has mattered before.

**Baseline verification:** `baseline_V3_15.py` is a plain, unmodified copy
of the current champion (`candidates/V3_15.py`, confirmed current per
Phase 6/8's checks) -- no separate representativeness check was needed
here since the test compares the current champion directly against a
minimal reordering of its own logic, not against a historical replay
statistic.

**Variant:** `variant_weeds_first.py` -- two-line change, moving `weeds`
immediately after `urgent`/`fert`, ahead of `harvest`. Otherwise
byte-identical.

**Result:** the variant scored higher than baseline in **all four**
independent tests run:

| test | opponent | n | mean diff (variant-baseline) | t |
|---|---|---|---|---|
| matched seeds 1-20 | tape_mtn | 40 | +$209/game | 0.27 |
| fresh seeds 101-120 | tape_mtn | 40 | +$719/game | 1.13 |
| fresh seeds 101-120 | tape_kwa | 40 | +$671/game | 1.05 |
| fresh seeds 101-120 | tape_furina | 40 | +$1,201/game | 1.49 |
| **pooled (meta-analysis)** | 3 opponents | **160** | **+$700/game** | **1.97** |

No individual test reaches conventional significance alone, but the
consistent positive sign across 4 independent seed/opponent draws, and a
pooled t just at the ~p=0.05 threshold, is a real, non-trivial signal --
stronger than Lead 1's flat-zero, inconsistent-sign result.

## Why this is PARTIAL_EVIDENCE, not CONFIRMED

The audit's own standing bar (per `docs/replay-audit-promotion-criteria.md`
and every prior CONFIRMED-tier finding in this chain, e.g. Phase 4A's
p=7.1e-169) has required much stronger statistical margins than a t just
crossing ~1.96 on a pooled, not fully independent, sample. This result is
promising and, unlike Lead 1, was NOT ruled out -- but calling it
CONFIRMED at this sample size would repeat exactly the kind of premature
promotion this whole methodology exists to prevent. A larger seed/opponent
sample (a proper Phase-4A-scale confirmation pass) is the honest next
step before treating this as settled, and was not run this round due to
session time constraints.

## RNG/side-effect audit

The tier-order change only affects which task a hand's sweep visits next
within the same day; it does not touch `_spawn_weeds`'s or the shop-unlock
RNG stream directly. No RNG-path contamination identified from a code
read of the change's scope (`_build_sweep`'s tier list only), though a
full trace-level audit (as done for melon/land in earlier phases) was not
run this round.

## Standing constraints honored

`variant_weeds_first.py` and `baseline_V3_15.py` are experiment-only
copies under `experiments/`. No champion, submission,
`evolve/cascade.py`, or parent-selection files touched. No adoption
recommendation -- this is diagnostic evidence, not a promotion, even
though the direction is encouraging.
