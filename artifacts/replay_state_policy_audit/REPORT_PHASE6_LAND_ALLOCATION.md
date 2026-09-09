# Phase 6: causal test of the land-allocation hypothesis

**Verdict: NO_ROBUST_SIGNAL — test could not proceed on valid footing.**
No intervention variant was built. The baseline representativeness check
(mandated by this phase's own methodology, as the explicit fix for Phase
4B's documented mistake) **failed** for both plausible current-champion
candidates, so proceeding to build a "cash-priority" variant against either
would have repeated exactly the mistake this phase was designed to avoid.

## Executive summary

Phase 5 measured, from real gameplay (`Replays/Auto/mine/`, 150 games), that
the champion's seat ever buys past the starting land quadrant in 59.3%
(89/150) of games, versus 90.0% for paired opponents. Phase 6's job was to
test, causally, whether this gap is explained by a cash-allocation-priority
choice in the policy.

Before building any variant, this phase's methodology required verifying
that whatever baseline candidate stands in for "the champion's real
behavior" actually reproduces something near that 59.3% reach rate. It does
not:

| candidate | opponents tested | seeds | games | BUY_LAND reach rate |
|---|---|---|---|---|
| `candidates/V3_12.py` (TDAS's "champion under test") | 8 real opponent tapes | 1,2,3, both seats | 48 | **100.0%** |
| `candidates/V3_15.py` (latest submitted, Sep 8 — supersedes V3_12 per commit `86b4735`) | 8 real opponent tapes | 1,2,3, both seats | 40 | **100.0%** |
| Phase 5's real-replay measurement | (whatever agent actually played) | (real games) | 150 | **59.3%** |

Both candidates buy the first extra quadrant in *every single simulated
game* against 8 different real opponent tapes — a rate nowhere near the
measured 59.3%. This is not sampling noise (48 and 40 games, 0/48 and 0/40
misses respectively).

**Explanation, evidenced, not guessed:** the `Replays/Auto/mine/` corpus
used by Phase 5 spans a very wide episode-ID range (89,895,943 to
106,840,046; median 103,520,461) — Kaggle episode IDs increase
monotonically over time, so roughly half the mined games are from
substantially earlier in the project's history than the current V3_12/V3_15
chassis. A spot-check of 3 games where the champion's seat never expanded
(episodes 90705157, 97456908, 90568571) confirms these are from the
lower/older end of that range. **The 59.3% figure Phase 5 measured is a
mixture across the whole history of chassis versions Grace has played, not
a property of the current champion specifically** — so it is not a valid
target for a baseline-representativeness check against today's candidates,
and no current candidate can be expected to reproduce it.

## Why this stops the phase here, per the assigned methodology

The instructions were explicit that this check is "the single most
important process fix relative to Phase 4B," and that if the baseline's
reach rate doesn't land near 59.3%, we should "not proceed with it as the
baseline; find or construct one that actually matches Grace's measured
real behavior." Two things follow from what was found:

1. **No available candidate matches.** Both plausible current-champion
   candidates reach 100%, a full 40 points off. There is no reason to
   expect an older/different chassis lying around would do better, and
   reconstructing one from a mid-history commit that happens to match
   59.3% would be curve-fitting a baseline to the outcome metric itself —
   backwards, and exactly the kind of unfounded-proxy mistake this
   check exists to prevent.
2. **The 59.3% figure is not actually a property of "the champion's
   current policy."** It is a mixture statistic over Grace's entire play
   history. Phase 5's finding — the *existence* of a real-replay reach-rate
   gap versus paired opponents — stands on its own and is unaffected (it
   was never claimed to be a single-chassis property). But a *causal test
   of the current policy's allocation behavior* cannot be meaningfully
   anchored to a mixture-history number. The right baseline for such a test
   is simply the current champion's own reach rate (100%, measured above) —
   which leaves **no gap left to explain in the current policy**: today's
   candidates already buy land in every tested game.

## Conclusion

**NO_ROBUST_SIGNAL for a live causal effect in the current policy.** The
land-allocation-priority mechanism proposed after Phase 5 cannot be tested
against the current champion because there is no reach-rate gap to test
against the current champion — the gap Phase 5 found lives in the
historical mixture of past chassis versions, not in `V3_12`/`V3_15` today.
Building and evaluating a "raise land-purchase priority" variant against
either candidate would have no possible effect to detect (the reach rate is
already saturated at 100%), so it was not built. This is reported as a
complete, valuable stopping point, not a gap to be papered over with a
constructed baseline.

## What this means for Phase 5's own finding

Phase 5's PARTIAL_EVIDENCE verdict is **not weakened** by this — the
real-replay reach-rate gap it measured (89/150 vs 135/150) is a genuine,
statistically robust historical fact about games Grace has actually played,
and the RNG_INDEPENDENT engine-gate finding stands unchanged. What Phase 6
adds is a scope correction: that finding describes Grace's play history as
a whole (spanning many chassis versions over the project's life), not a
live behavioral gap in the current champion that a present-day intervention
could move. If land-allocation timing is still of interest, the correct
next step would be a *forward-looking* replay-mining pass restricted to
games played by the current champion specifically (once enough such games
exist), not a causal intervention against a stale mixture baseline.

## Standing constraints honored

No champion, submission, `evolve/cascade.py`, or parent-selection files
modified. No intervention variant was built or run (none was needed to
reach this conclusion). No adoption recommendation made. Diagnostic only.

## RNG classification

Not applicable to this phase's conclusion — the stopping point is a
baseline-representativeness failure, established from deterministic
reach-rate measurements (BUY_LAND's gate is RNG_INDEPENDENT per Phase 5;
this phase's own measurements did not depend on any RNG-sensitive
downstream mechanism).
