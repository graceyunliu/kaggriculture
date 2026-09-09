# Mining Campaign Summary (Phases 8-9): honest final accounting

**Bar requested: 2+ CONFIRMED candidates from 5 leads. Result: 0 CONFIRMED,
1 FALSIFIED, 1 PARTIAL_EVIDENCE (promising, unresolved), 3 leads not
reached this round.** Reported plainly per the standing instruction to
report honestly rather than lower the bar or pad results.

## Lead-by-lead status

| Lead | Status | Report |
|---|---|---|
| 1. Labor headcount (opponent-vs-opponent correlation) | **FALSIFIED_AS_CAUSAL** | [REPORT_PHASE8_LABOR_HEADCOUNT.md](REPORT_PHASE8_LABOR_HEADCOUNT.md) |
| 2. TDAS THROUGHPUT_SCALE weakness | Not tested this round | -- |
| 3. Melon admission-window timing | Not tested this round | -- |
| 4. Chore-type priority ordering (weeds vs. harvest) | **PARTIAL_EVIDENCE** (promising, not yet CONFIRMED) | [REPORT_PHASE9_CHORE_PRIORITY.md](REPORT_PHASE9_CHORE_PRIORITY.md) |
| 5. Fertilizer target-tile eligibility | Not tested this round | -- |

## Lead 1 (Phase 8): FALSIFIED_AS_CAUSAL

Opponent-vs-opponent natural experiment found `max_hands` correlates with
score (r=0.187, t=3.79, n=400, zero Grace participants). The coordinator's
named cash-affordability confound was directly tested: forcing +3 hands
from the champion's own budget produced no score effect across 4
independent seed/opponent tests (t=0.01, 1.01, -0.99, 0.52). The
correlation does not survive a direct causal manipulation designed
specifically to isolate it from the confound.

Byproduct: melon-hold rate showed zero correlation with score in the same
opponent-vs-opponent population (r=0.016, n=167) -- independent
corroboration, from a different data source, of Phases 4B/7's causal
nulls on melon.

## Lead 4 (Phase 9): PARTIAL_EVIDENCE -- the strongest surviving lead

Reordering `_build_sweep()`'s chore tier list (weeds moved ahead of
harvest, a two-line change) showed a **positive-signed effect in all 4**
independent seed/opponent tests run (matched + 3 fresh-seed/opponent
cohorts), pooled t=1.97 (n=160, right at conventional p~0.05). This is
meaningfully stronger and more consistent than Lead 1's flat null, but
falls short of this audit's own established bar for CONFIRMED (every prior
CONFIRMED-tier finding in this chain, e.g. Phase 4A's melon-existence
finding, cleared p<0.001 at much larger scale). Not promoted; reported as
the best remaining candidate for a future confirmation-scale pass.

## Leads 2, 3, 5: not reached

TDAS's THROUGHPUT_SCALE weakness, melon admission-window timing (price-
window-dependent accept/hold, distinct from the already-tested
sell/hold-threshold question), and fertilizer target-tile eligibility
were each grounded in real evidence at the checkpoint-1 stage (TDAS's own
report; Phase 2's explicit "not reconstructed this pass" flags) but did
not receive statistical confirmation or causal testing this round --
session time constraints, reported plainly rather than rushed or
fabricated.

## Recommendation

The requested 2-CONFIRMED bar was not reached. Of the leads actually
tested, Lead 4 (chore priority) is the one worth prioritizing in any
follow-on round: a larger-scale confirmation pass (Phase-4A-style, more
seeds and opponents, cluster-bootstrap CIs) on the weeds-first reordering
is the most likely single next step to produce a genuine CONFIRMED
candidate, given the consistent positive signal already found. Leads 2, 3,
and 5 remain open and untested, in no particular priority order relative
to each other. No adoption/promotion of anything from this campaign;
standing constraints (no champion, submission, `evolve/cascade.py`, or
parent-selection changes) were honored throughout.
