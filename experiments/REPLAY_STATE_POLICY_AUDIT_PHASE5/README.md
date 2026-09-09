# Phase 5: EXPANSION (BUY_LAND) opportunity reconstruction

Investigates TDAS's falsified H1 (early_labor/floor_v2) by applying the audit's
Phase-3-style OBSERVED_ACTION/OBSERVED_ABSTENTION/OPPORTUNITY_UNRECONSTRUCTABLE
opportunity reconstruction directly to the EXPANSION (BUY_LAND) decision,
instead of trusting TDAS's own EXPANSION_READY state (which TDAS's own report
flags as circular/lookahead-based).

## Eligibility gate (ground truth, cited from source)

`vendor/kaggle_environments_engine/kaggriculture.py:688-700` (`_do_buy_land`):
only gate is `n_unlocked_extra < len(LAND_ORDER)` (3 extra quadrants max) AND
`farm["money"] >= LAND_PRICES[n_unlocked_extra]` (prices $1000/$2000/$4000,
NE/SW/SE in order). No RNG, no capacity/tile-state prerequisite anywhere in
`_do_buy_land`. Classification: **RNG_INDEPENDENT**.

## Scripts

- `mine_phase5.py`: mines `Replays/Auto/mine/` (per Phase 4A's provenance
  finding, the only directory with paired mine-vs-opp games), 150 files,
  seeded shuffle (seed 42, same convention as prior phases). Reconstructs
  day-boundary opportunity/action rows per seat per land tier.
- `aggregate_phase5.py`: computes reach-rate (land tier >= 2 reached at all
  in-game) with Wilson 95% CIs and a two-proportion z-test, plus the tier-1
  opportunity-conditioned action rate (raw, not cluster-adjusted -- see
  REPORT_PHASE5's limitations section for why this sub-statistic is
  reported but not leaned on).

## A real methodological complication (documented, not glossed over)

`BUY_LAND` is processed in the engine as an "atomic order" within the same
tick as `SELL`/`BUY_PRODUCT` orders (`kaggriculture.py`'s per-day order loop
commits incremental market orders first, then atomic HIRE/BUY_LAND once per
tick, in player order). A same-tick "sell crop, then buy land with the
proceeds" pattern means pre-tick cash snapshots understate true intra-tick
liquidity. Both a first-step-of-day and a corrected prior-step-boundary
money snapshot were tried (`mine_phase5.py` uses the latter); neither fully
captures intra-tick sell-financed purchases. This means the **day-level
first-opportunity/first-action timing numbers are unreliable** for BUY_LAND
specifically (unlike Phase 3's HIRE/MELON reconstruction, where this
same-tick-financing pattern is far less material). The **reach-rate
statistic (does land tier 2+ ever get reached in the game) is NOT affected**
by this -- it only requires knowing final land state, not the exact
triggering tick -- and is the statistic Phase 5's conclusion relies on.
