# Mining Campaign Summary: honest final accounting

**Bar requested: 2+ CONFIRMED candidates from 5 leads. Result: 0
CONFIRMED.** Two leads received full testing (both closed negative);
three leads remain unexplored. Reported plainly, per standing instruction,
rather than lowering the bar.

## Lead-by-lead status

| Lead | Status | Report |
|---|---|---|
| 1. Labor headcount (opponent-vs-opponent correlation) | **FALSIFIED_AS_CAUSAL** | [REPORT_PHASE8_LABOR_HEADCOUNT.md](REPORT_PHASE8_LABOR_HEADCOUNT.md) |
| 2. TDAS THROUGHPUT_SCALE weakness | Not tested | -- |
| 3. Melon admission-window timing | Not tested | -- |
| 4. Chore-type priority ordering (weeds vs. harvest) | **FAILED_CONFIRMATION** | [REPORT_PHASE9_CHORE_PRIORITY.md](REPORT_PHASE9_CHORE_PRIORITY.md) |
| 5. Fertilizer target-tile eligibility | Not tested | -- |

## Lead 1 (Phase 8): FALSIFIED_AS_CAUSAL

Opponent-vs-opponent natural experiment found `max_hands` correlates with
score (r=0.187, t=3.79, n=400). A confound-isolating causal test (forcing
+3 hands from the champion's own budget) produced no score effect across
4 independent tests (t=0.01, 1.01, -0.99, 0.52). Melon-hold rate showed
zero correlation in the same data (r=0.016), independently corroborating
Phases 4B/7's causal nulls.

## Lead 4 (Phase 9): FAILED_CONFIRMATION -- a genuine lesson in scaling up

A two-line reorder of `_build_sweep()`'s chore tier list (weeds ahead of
harvest) showed a promising positive-signed effect in an initial 4-test
design (matched + fresh seeds vs. 3 external opponents, pooled t=1.97,
n=160). Per the coordinator's explicit instruction to scale this to a
proper Phase-4A-grade confirmation, a direct head-to-head test was run
(`mini_engine.evaluate()`, the same harness `evolve/cascade.py` uses,
200 seed-matched both-seat games against the baseline itself, not a third
party). **The effect did not replicate**: the first 100-game batch alone
was significantly *negative* (t=-2.34); the full 200-game sample landed
at t=-1.53, negative-leaning, not significant. The original positive
signal was an artifact of measuring absolute money against external
opponents rather than direct competitive margin -- exactly the kind of
premature-positive trap this methodology exists to catch, caught here by
following through on the scaling instruction rather than stopping at the
smaller, indirect result.

## Leads 2, 3, 5: not reached

TDAS's THROUGHPUT_SCALE weakness, melon admission-window timing (distinct
from the already-tested sell/hold threshold), and fertilizer target-tile
eligibility were each grounded in real evidence at the checkpoint-1 stage
but received no statistical confirmation or causal testing this
session -- a genuine time-budget limitation across this multi-round
campaign, reported honestly.

## What this campaign actually found, net of everything

Across every dimension tested this session with full statistical rigor
(melon-sell threshold in Phases 4B and 7, land-expansion allocation in
Phase 6, labor headcount in Phase 8, chore priority ordering in Phase 9),
**none has produced a robust, scale-confirmed positive score effect.**
The strongest surviving *behavioral* findings from the whole audit chain
remain the ones established earlier and never causally reopened
successfully: the melon-hold divergence's *existence* (Phase 4A,
CONFIRMED as a real behavioral fact, not as a score-improving lever) and
Phase 5's land-expansion reach-rate gap (also a real historical fact, not
a live current-policy lever per Phase 6). No new CONFIRMED
performance-improving candidate was produced by this mining campaign.

## Recommendation

The 2-CONFIRMED target was not reached. Two substantive, real negative/
non-replicating results were produced and are valuable in their own
right (each closes off a plausible-seeming lead with genuine evidence
rather than leaving it open on a hunch). Leads 2, 3, and 5 remain
legitimate starting points for a future round, unprioritized relative to
each other. No adoption/promotion of anything from this campaign;
standing constraints (no champion, submission, `evolve/cascade.py`, or
parent-selection changes) were honored throughout.
