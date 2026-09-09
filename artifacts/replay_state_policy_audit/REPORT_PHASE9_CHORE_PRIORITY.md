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

---

## Addendum: scaled statistical confirmation (Phase 9b) -- FAILS to confirm

Per the coordinator's request to scale this lead to the proper Phase-4A
statistical bar, a much larger, more standard test was run: **direct
head-to-head evaluation** (`mini_engine.evaluate()`, the same harness
`evolve/cascade.py` uses for real candidate scoring) of the variant
against the baseline itself, rather than each measured separately against
external opponents. This is a more statistically powerful and more
standard design (both-seats, seed-matched, direct competitive margin) than
the 4-test external-opponent comparison Phase 9's original result was
based on.

| sample | seeds | n (both seats) | mean margin/game (variant-baseline) | t | wins-losses |
|---|---|---|---|---|---|
| batch 1 | 1-50 | 100 | -$389.86 | -2.34 | 19-31 |
| batch 2 | 51-100 | 100 | -$10.79 | -0.05 | 22-28 |
| **combined** | 1-100 | **200** | **-$200.33** | **-1.53** | **41-59** |

**Result: the effect does not replicate.** At 200 games (25x the original
n=160 across a different, more direct design), the direction reverses
(negative, not positive) and the earlier marginal positive signal
(t=1.97) does not hold up. The first 100-game batch alone was actually
significantly *negative* (t=-2.34); the full 200-game sample lands at
t=-1.53, not significant but clearly not supporting a positive effect
either.

**Reading this honestly:** the original Phase 9 result (positive-signed
across 4 external-opponent tests, pooled t=1.97) was based on absolute
money against third-party opponents, which conflates "did both agents do
better against a given opponent" with "does this change actually make the
variant competitively stronger than the baseline." The direct
head-to-head test is the correct question for "is this a real
improvement," and it does not confirm one -- if anything it leans the
opposite direction. This is exactly the kind of premature-positive trap
the audit's promotion-criteria doc warns against, caught here by scaling
to a proper confirmatory design rather than stopping at the smaller,
indirect signal.

**Revised verdict: FAILS statistical confirmation. NOT CONFIRMED, and not
worth further causal-intervention testing** (a causal intervention step
would be testing a manipulation that already failed to show a positive
effect at a much larger, more direct sample). Lead 4 is closed as a
negative/inconclusive-leaning-negative finding, on par with Lead 1.
