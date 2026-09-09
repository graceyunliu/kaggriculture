# Mining Campaign Summary (Phases 8+): 5 leads, honest accounting

**Bar requested: 2+ CONFIRMED candidates out of 5 tested. Result: 0 of 5
fully deep-tested to a causal conclusion this round; 1 of 5 (Lead 1) was
fully causally tested and came back FALSIFIED_AS_CAUSAL. The remaining 4
leads (2-5) were identified with real, replay-grounded evidence at the
checkpoint-1 stage but were not carried through statistical confirmation
and causal intervention this round.**

This falls short of the requested "2 CONFIRMED" bar. Per your own explicit
instruction ("if fewer than 2 of the 5 leads survive full testing, report
that honestly rather than lowering the bar"), this is reported plainly
rather than padded or rushed.

## What was completed

**Lead 1 -- labor headcount vs. score (opponent-vs-opponent natural
experiment).** Full pipeline run: natural-experiment mining (200
leaderboard-only replays, 400 seat-rows, confirmed zero Grace
participants), correlation found (r=0.187, t=3.79, n=400), causal test
designed specifically around your named confound (force extra hands from
the SAME budget, not free), tested matched + 3 fresh-seed/opponent
cohorts. Result: **FALSIFIED_AS_CAUSAL** -- no score effect in any of 4
tests (t=0.01, 1.01, -0.99, 0.52). The confound was not ruled out in
headcount's favor; if anything, the data is consistent with headcount
being a side effect of successful play rather than a cause of it. See
`REPORT_PHASE8_LABOR_HEADCOUNT.md`.

As a byproduct of Lead 1's mining, melon-hold rate vs. score in the SAME
opponent-vs-opponent population showed **no correlation at all** (r=0.016,
n=167) -- an independent corroboration, from a completely different data
source and method, of Phases 4B and 7's causal nulls on melon-selling.
This is a real, valuable convergent finding even though it wasn't one of
the 5 named leads.

## What was not completed, and why

Leads 2-5 (TDAS's THROUGHPUT_SCALE weakness; melon admission-window
timing; chore-type priority ordering; fertilizer target-tile eligibility)
were each grounded in real, previously-documented evidence at the
checkpoint-1 stage (TDAS's own report language for Lead 2; Phase 2's
explicit "not reconstructed this pass" flags for Leads 3 and 5; Phase 2's
idle-vs-assigned-only scope, not priority-ordering, for Lead 4). None of
them received the full statistical-confirmation-then-causal-intervention
treatment this round.

This is a session resource-budget limitation, not a finding about the
leads themselves -- reported plainly rather than either fabricating
results for leads 2-5 or silently declaring the campaign complete. Each
of the 4 remaining leads is a legitimate, real starting point (evidence +
mechanism + non-trivial initial signal, per the checkpoint-1 bar you
approved) for a future round of this same methodology, with the "5
leads" characterization from checkpoint 1 still standing as-is.

## Recommendation

Treat this as a partial campaign: Lead 1 closed (negative, well-evidenced,
converges with 2 prior phases' melon nulls), Leads 2-5 open and
unprioritized relative to each other -- any of the 4 would be a reasonable
starting point for a follow-on round using the exact same
mining-then-statistical-confirmation-then-causal-intervention pipeline
already built and proven across Phases 3-8. No adoption/promotion of
anything from this campaign; standing constraints (no champion,
submission, `evolve/cascade.py`, or parent-selection changes) were honored
throughout.
