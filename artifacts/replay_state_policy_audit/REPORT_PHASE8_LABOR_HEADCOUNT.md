# Phase 8: Lead 1 -- labor headcount vs. score (FALSIFIED as causal)

**Verdict: FALSIFIED (as a causal claim). The confound the coordinator
flagged was not ruled out in headcount's favor -- it appears confirmed.**

## Executive summary

An opponent-vs-opponent natural experiment (200 `Replays/Auto/leaderboard-*`
files, 400 seat-rows, verified zero `graceyunliu` participants) found
`max_hands` (peak headcount reached in-game) correlates with final money:
r=0.187, t=3.79, n=400 (p<0.001). `max_land` showed a weaker correlation
(r=0.105, t=2.10). Melon-hold rate showed **no** correlation (r=0.016) --
consistent with, and corroborating, Phases 4B/7's causal nulls on melon.

The coordinator specifically flagged the obvious confound: richer/better
play could independently generate both more cash *and* more hands, with
headcount contributing nothing causally. This phase's causal test was
designed explicitly to isolate that: `variant_labor_boost.py` forces the
champion's own hire-target computation (`_load_model()` in
`candidates/V3_15.py`) up by +3 hands above whatever the policy's own
workload-based logic already decided, funded from the **same cash
trajectory** the policy already has (not free hands) -- a single-line,
otherwise byte-identical change.

**Result: no significant score effect, in any direction, across 4
independent tests** (matched seeds 1-20 vs. one opponent: t=0.01; fresh
seeds 101-120 vs. 3 different opponents: t=1.01, -0.99, 0.52). Forcing
extra hands, paid for from the policy's own budget, does not reliably
help or hurt.

## Interpretation

This is exactly the negative result the confound-check was designed to
surface: **headcount does not appear to have independent causal value**
once the champion's policy is forced to buy more of it from the same
budget it already has. The opponent-vs-opponent correlation is better
explained by the confound the coordinator named -- successful play
generates cash, and cash happens to buy hands as a side effect, without
hands themselves driving the extra score. This does not prove the
confound with certainty (a null causal result cannot fully "prove" the
absence of an effect, only fail to detect one at this sample size), but it
gives no support to promoting headcount to a causal lead, and the
methodology's own discipline says not to promote ASSOCIATED evidence
without positive causal support.

## Standing constraints honored

`variant_labor_boost.py` and `baseline_V3_15.py` are experiment-only
copies under `experiments/`. No champion, submission, `evolve/cascade.py`,
or parent-selection files touched. No adoption recommendation.
