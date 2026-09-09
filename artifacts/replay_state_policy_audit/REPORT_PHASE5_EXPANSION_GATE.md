# Phase 5: EXPANSION (BUY_LAND) opportunity reconstruction

**Verdict: PARTIAL_EVIDENCE.** A large, statistically robust distributional
finding was confirmed; the mechanism behind it is well-motivated but was not
causally isolated in this round. Not promoted to CONFIRMED. Diagnostic only.

## Executive summary

TDAS (`arch_search/`, dormant since 2026-09-07) tested and **falsified**
hypothesis H1: pulling the champion's labor-scale timing earlier
(`early_labor/floor_v2`) did achieve an earlier LABOR_SCALE and
DENSIFICATION as predicted, but EXPANSION still fired *later* than target
(day 15 vs. the day-13 prediction) -- the causal chain broke at step 3.
TDAS's own report flags its `EXPANSION_READY` state as too circular
(defined mostly by "the day before an EXPANSION jump") to trust as a
diagnostic tool on its own.

This phase reconstructs EXPANSION opportunity directly from the engine's
real eligibility rule for the underlying action (`BUY_LAND`), the same way
Phase 3 reconstructed HIRE/MELON opportunity, instead of relying on TDAS's
state machine.

**Finding:** across 150 mined games from `Replays/Auto/mine/` (the only
directory with paired mine-vs-opponent games per Phase 4A's provenance
correction), the champion's seat ever buys the first extra land quadrant in
only **89/150 games (59.3%, 95% CI 51.3-66.9%)**, versus **135/150 (90.0%,
95% CI 84.2-93.9%)** for the paired opponent seat in the *same* games
(two-proportion z = 6.11). The confidence intervals do not overlap.

The engine's actual eligibility gate for `BUY_LAND`
(`kaggriculture.py:688-700`) has **no RNG and no hidden prerequisite** --
only cash-on-hand and remaining-quadrant count. So this gap cannot be an
externally-timed or RNG-coupled "opportunity arrives later" effect in the
sense TDAS's EXPANSION state implied. The most consistent explanation is a
**within-policy cash-allocation choice**: the champion's policy routes
earned cash toward other goods (fertilizer, animals, seeds) in a
substantially larger share of games than the paired opponents do, rather
than committing the $1000+ needed for the first land purchase.

This is **compatible with, and explains,** TDAS's own falsification of H1:
if labor-scale timing was never the actual bottleneck for land purchases,
accelerating it had no reason to move EXPANSION earlier -- which is exactly
what TDAS observed. It is also compatible with Phase 3's hire-opportunity
parity finding (5.76% vs. 6.97%): that finding was about *labor* allocation
specifically and doesn't speak to *land* allocation, which is what this
phase newly measures.

**This causal explanation (cash routed elsewhere rather than to land) is
PLAUSIBLE_BUT_UNPROVEN, not causally isolated.** No Phase-4B-style
single-knob intervention was run this round to test it directly. Per the
audit's standing discipline, it is reported as ASSOCIATED and not promoted
further. A follow-on causal-intervention phase is the natural next step but
was not run in this pass.

## 1. The eligibility gate, from source

`vendor/kaggle_environments_engine/kaggriculture.py:688-700` (`_do_buy_land`):

```python
def _do_buy_land(farm, board_size):
    n_unlocked_extra = len(farm["unlocked_quadrants"]) - 1  # NW is always there
    if n_unlocked_extra >= len(LAND_ORDER):
        return
    cost = LAND_PRICES[n_unlocked_extra]
    if farm["money"] < cost:
        return
    farm["money"] -= cost
    quadrant = LAND_ORDER[n_unlocked_extra]
    farm["unlocked_quadrants"].append(quadrant)
    ...
```

`LAND_ORDER = ["NE", "SW", "SE"]`, `LAND_PRICES = [1000, 2000, 4000]`
(lines 82-83). The only gate is remaining-quadrant count and cash. No RNG
call anywhere in this function or its callers for this action.
**Classification: RNG_INDEPENDENT.**

This is structurally identical in kind to Phase 3's HIRE gate
(`_do_hire`: `farm["money"] >= _hire_cost(...)`, also RNG_INDEPENDENT) --
same style of reconstruction applies directly.

## 2. Opportunity reconstruction and a real methodological complication

`BUY_LAND` is committed in the engine as an "atomic order," processed once
per player per tick *after* the tick's incremental `SELL`/`BUY_PRODUCT`
order loop resolves (`kaggriculture.py`'s per-day commit sequence,
`# Atomic orders (HIRE, BUY_LAND): handle once, in player order`). This
means a common "sell a crop, then buy land with the proceeds, same tick"
pattern is real and was observed directly in spot-checked replays -- e.g.
`Replays/Auto/mine/episode-105524413-replay.json`, where the champion's
seat shows pre-tick money of $10 immediately before a tick whose action
list is `[SELL WOOL, SELL FERTILIZER, ..., BUY_LAND, ...]` and which
succeeds.

Two day-boundary money snapshots were tried (first-step-of-day, and the
prior day's last step) as proxies for "opportunity as of day start" -- both
undercount true intra-tick liquidity, because sale proceeds realized
*within* the same tick as the `BUY_LAND` order aren't visible in either
snapshot. **The day-level first-opportunity/first-action timing numbers
and the tier-1 opportunity-conditioned action rate (mine: 7/507, opp:
56/525) are therefore flagged as OPPORTUNITY_UNRECONSTRUCTABLE for the
fine-grained timing question** and are reported in
`FINDINGS_PHASE5_EXPANSION_GATE.json` for transparency but not relied on.

**The reach-rate statistic (89/150 vs. 135/150) does not have this
problem** -- it only asks whether land tier 2+ was EVER reached by the end
of the game, which doesn't depend on identifying the exact triggering
tick. That is the statistic this phase's conclusion rests on.

## 3. Statistical confirmation

- N = 150 games (seeded shuffle, seed 42, same convention as Phase 3/4A),
  all from `Replays/Auto/mine/` per Phase 4A's provenance finding (the only
  directory with paired mine-vs-opponent data).
- Reach-rate (land tier >= 2 reached at any point): mine 89/150 = 59.3%
  (Wilson 95% CI [51.3%, 66.9%]); opp 135/150 = 90.0% (Wilson 95% CI
  [84.2%, 93.9%]). Two-proportion z = 6.11 (non-overlapping CIs).
- This was not additionally broken out by per-opponent cohort in this
  round (time/scope-bounded); the 150-game sample already spans whichever
  distinct opponents appear in the shuffled sample, consistent with prior
  phases' sampling convention.

## 4. Causal diagnostic split (per the assigned methodology)

**Does the opportunity arrive later (upstream gate), or arrive comparably
but get deferred (decision-policy issue)?**

Neither cleanly maps onto TDAS's framing, because the engine has no
upstream timing gate to arrive late *or* on time -- eligibility is pure
cash-on-hand. The real split is: **is cash simply less available to the
champion's policy overall, or does the champion's policy choose to spend
available cash on other things instead of land?** This phase's data
(reach-rate, not fine timing) cannot fully distinguish these two without a
controlled intervention, but the qualitative pattern across all 150 games
(no RNG involved, deterministic cost schedule, same opponent-cohort mix
for both seats) is more consistent with an allocation-priority difference
than with the champion's policy simply earning less money overall (which
would be a distinct, checkable finding this phase did not test).

## 5. What was NOT done in this round, and why

Per the coordinator's latitude and the instruction to stop rather than
"keep fishing" once a valuable stopping point is reached: a Phase-4B-style
isolated causal intervention (a single-knob variant that changes cash
priority toward land, tested with pre-registered predictions, a
baseline verified to actually represent the champion's real spending
behavior -- learning from Phase 4B's own documented mistake of defaulting
to C1 without checking representativeness first -- matched+fresh seeds,
and an RNG/side-effect audit) is the natural next step but was not run
this round. This finding is reported as PARTIAL_EVIDENCE, not CONFIRMED,
specifically because that step is missing. No champion, submission,
`evolve/cascade.py`, or parent-selection files were touched. No
destructive git operations were used.

## 6. RNG classification summary

| Finding | RNG classification |
|---|---|
| BUY_LAND eligibility gate (cash + quadrant count) | RNG_INDEPENDENT |
| Reach-rate difference (89/150 vs 135/150) | Confirmed on RNG_INDEPENDENT-gated data; no RNG-coupled mechanism involved |
| Day-level timing/opportunity-conditioned action rate | OPPORTUNITY_UNRECONSTRUCTABLE (methodological, not RNG-related) |
