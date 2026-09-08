# Replay Mining Phase 3: Counterfactual Opportunity Reconstruction

> **Provenance correction (added after Phase 4A):** "opponent" / "opp"
> throughout this report means the opposing seat observed inside Grace's
> own replay history (`Replays/Auto/mine/`), not an independently sampled
> leaderboard/ladder reference population. See [INDEX.md](INDEX.md) for
> the full correction and what it does and doesn't affect. Numbers and
> verdicts below are unchanged.

Date: 2026-09-08. Follow-on to `REPORT.md` (Phase 1) and `REPORT_PHASE2.md`
(Phase 2) - read those first. Reuses the replay format and RNG-coupling code
citation already established
(`vendor/kaggle_environments_engine/kaggriculture.py`, `_end_of_day`,
lines ~837-867) without re-deriving it.

**Final status: PARTIAL_EVIDENCE.**

## Problem being fixed

Phase 2 could only observe "an action happened" (a hire occurred, a melon
sale occurred), which is selection bias: it compares actions conditional on
acting, not conditional on an opportunity existing. Phase 3 reconstructs the
true opportunity gate for HIRE and MELON from engine code, so abstention
(an opportunity existed and the policy declined it) becomes visible
alongside action.

## Eligibility/opportunity rules recovered from engine code

### HIRE - fully reconstructed, no unrecoverable component

`vendor/kaggle_environments_engine/kaggriculture.py`:
- `_hire_cost(n_already_today, mult)` (lines 674-675): `cost = mult *
  fib(n_already_today)`, where `fib` is 1-indexed Fibonacci
  (`_fib(0)=1, _fib(1)=1, _fib(2)=2, _fib(3)=3, _fib(4)=5, ...`,
  lines 666-671) and `mult = configuration.farmHandCostMult`
  (default `FARM_HAND_COST_MULT = 1`, line 87). `n_already_today` is the
  farm's `hires_today` counter at the moment of the hire (resets to 0 each
  day in `_end_of_day`, line 858 - a deterministic, non-RNG reset).
- `_do_hire(farm, private, board_size, mult)` (lines 678-683): the **only**
  eligibility gate is `farm["money"] >= cost`. There is no capacity/board/
  slot gate - `_spawn_hand` is called unconditionally once the money check
  passes.
- **Reconstruction used**: at every hourly step, opportunity exists iff
  `money >= hire_cost(hires_today, farmHandCostMult)` (using that step's
  `hires_today` and the replay's `configuration.farmHandCostMult`, read
  directly from the replay file, not assumed). If an opportunity existed,
  tag `OBSERVED_ACTION` when a `["HIRE", ...]` entry appears in that step's
  `market` action list, else `OBSERVED_ABSTENTION`.
- **Known simplification, not unreconstructable**: multiple `HIRE` orders
  can appear in a single step's `market` list (up to `maxMarketOrdersPerTurn`
  = 10 per `configuration`), each with an escalating Fibonacci cost as
  `hires_today` increments mid-step. This script checks eligibility for only
  the *first* hire of the step (using `hires_today` as observed at step
  start) - it does not verify eligibility for a hypothetical 2nd/3rd hire
  within the same step. This is flagged as a limitation, not a reason to
  mark any row unreconstructable, since the primary opportunity (can the
  policy hire at all this step) is fully determined.

### MELON admission - fully reconstructed, no unrecoverable component

Same file, `_commit_unit` (lines 626-635, `SELL` branch): the **only**
eligibility gate for selling one unit is `private["shed"].get(item, 0) > 0`.
Price (`market_price()`, line 177) is a deterministic function of current
market inventory and configured params - no RNG draw, consistent with the
already-established finding that market price/demand is deterministic.
- **Reconstruction used**: at every hourly step where `shed.MELON > 0`
  (private inventory, read directly from `observation.private.shed`), an
  admission opportunity exists. Tag `OBSERVED_ACTION` if a
  `["SELL", "MELON", ...]` entry appears in that step's `market` list, else
  `OBSERVED_ABSTENTION`.
- No component of this rule was unreconstructable - unlike Phase 2's
  cautious framing ("MELON admission opportunity could not be
  distinguished from ordinary hold"), the engine code shows there is no
  additional gate beyond stock > 0, so this phase resolves that open
  question directly rather than needing an `OPPORTUNITY_UNRECONSTRUCTABLE`
  fallback for MELON.

### What remained genuinely unreconstructable

Nothing for HIRE or MELON at the opportunity-existence level - both gates
are single, deterministic, cash/stock conditions fully visible in the
replay's own `observation`/`configuration` fields, so **zero rows were
tagged `OPPORTUNITY_UNRECONSTRUCTABLE`** in this phase's output. This is
reported plainly per the task's own acceptance that either outcome
(mostly-reconstructable or mostly-unreconstructable) is a valid result -
here it turned out fully reconstructable given the engine code available in
`vendor/kaggle_environments_engine/kaggriculture.py`.

## Sampling

Same 175-file, 15-directory ballpark as Phase 2 (not scaled up, per
instruction), all hourly steps, using new script `mine_phase3.py`
(built on the same file-selection logic as `mine_phase2.py`).

**HIRE-opportunity-tagged snapshots: 20,977** (mine: 603 `OBSERVED_ACTION`
+ 9,870 `OBSERVED_ABSTENTION` = 10,473; opp: 732 `OBSERVED_ACTION` + 9,772
`OBSERVED_ABSTENTION` = 10,504). Every one of these 20,977 rows carries a
definite opportunity tag - none unreconstructable.

**MELON-opportunity-tagged snapshots: 1,576** (mine: 7 `OBSERVED_ACTION` +
1,103 `OBSERVED_ABSTENTION` = 1,110; opp: 17 `OBSERVED_ACTION` + 449
`OBSERVED_ABSTENTION` = 466). All definite tags, none unreconstructable.

## Evidence tables

### HIRE: opportunity-conditioned action rate

| cohort | opportunities | acted (OBSERVED_ACTION) | abstained (OBSERVED_ABSTENTION) | action rate |
|---|---|---|---|---|
| mine | 10,473 | 603 | 9,870 | 5.76% |
| opp (pooled) | 10,504 | 732 | 9,772 | 6.97% |

Global action-rate gap is small (5.76% vs 6.97%). **One state bucket**
passed the >=8-per-side + >=40%-modal divergence filter:

| state (day, cash, land, labor) | mine | opp | mine n | opp n | seeds (mine/opp) | rng |
|---|---|---|---|---|---|---|
| (26, 40k+, land3, 5-8 hands) | OBSERVED_ABSTENTION (0.78) | OBSERVED_ACTION (1.00) | 27 | 8 | 6/8 | RNG_INDEPENDENT |

### MELON: opportunity-conditioned action rate

| cohort | opportunities | acted (OBSERVED_ACTION) | abstained (OBSERVED_ABSTENTION) | action rate |
|---|---|---|---|---|
| mine | 1,110 | 7 | 1,103 | 0.63% |
| opp (pooled) | 466 | 17 | 449 | 3.65% |

No individual state bucket passed the >=8-per-side support filter for
MELON (action events are too rare per bucket: 7 and 17 total across the
whole sample). The **global** opportunity-conditioned rate gap (0.63% vs
3.65%, ~5.8x) is now a real, opportunity-normalized number - unlike Phase
2's raw-hold-count version of this same signal, this is no longer
confounded by unequal opportunity counts between cohorts (mine had 1,110
opportunities vs opp's 466, so raw hold/sell counts were not directly
comparable in Phase 2; the rate is).

## RNG classification (Phase 1-2 four-value taxonomy, applied here)

Both HIRE and MELON opportunity gates are **RNG_INDEPENDENT**: hire cost is
a pure function of `hires_today` and a configured multiplier (no RNG
input); the `hires_today` reset itself happens in `_end_of_day` but is an
unconditional zeroing, not an RNG draw; melon eligibility is a pure shed
count check; melon price is a deterministic function of market inventory
(confirmed by code, consistent with the existing established finding that
market price/demand is deterministic). **Every finding and every aggregate
rate in this report is tagged `RNG_INDEPENDENT`** - none are `RNG_EXPOSED`,
`RNG_COUPLED`, or `UNKNOWN`. This is a genuinely stronger position than
Phase 1's crop-mix finding (which remains `RNG_EXPOSED`/`RNG_COUPLED` and
is not touched by this phase).

## Findings by confidence tier

- **DIRECTLY_OBSERVED**: The HIRE opportunity-conditioned action-rate gap
  (5.76% mine vs 6.97% opp, global) and the MELON opportunity-conditioned
  action-rate gap (0.63% mine vs 3.65% opp, global) are both directly
  observed, RNG_INDEPENDENT frequency differences. The single HIRE
  state-bucket divergence in the evidence table is also DIRECTLY_OBSERVED.
- **STRONGLY_SUPPORTED**: none promoted - per the hard constraints, a
  frequency divergence (even RNG_INDEPENDENT) does not by itself establish
  a performance or causal claim, and none is made here.
- **PLAUSIBLE_BUT_UNPROVEN**: that the MELON action-rate gap reflects a
  real, consistent difference in admission willingness rather than sampling
  noise from a small opportunity count (mine: 1,110 opportunities, only 7
  taken) - the direction is now opportunity-normalized and RNG_INDEPENDENT
  (a meaningfully cleaner signal than Phase 2's), but no significance test
  was run and no state-bucket-level support was found, so this stays
  unproven rather than promoted.

## Negative findings

- HIRE opportunity-conditioned action rate is **close** between cohorts
  (5.76% vs 6.97%) at the global level - no large, robust divergence, in
  contrast to the strong MELON gap. Only one state bucket showed a
  qualifying divergence, with thin opponent-side support (n=8).
- No `OPPORTUNITY_UNRECONSTRUCTABLE` rows were produced for either decision
  type - the reconstruction was fully successful for both HIRE and MELON
  given the engine code available; this itself is worth recording as a
  negative result for the *methodology* question ("is opportunity
  reconstruction actually possible here") - it is.

## Fertilizer / chore / crop-mix status (unchanged, not re-opened)

Fertilizer and chore remain **closed** per Phase 2's genuine parity
finding - not re-examined this phase, and nothing in this phase's data
contradicts that finding (fertilizer/chore were not touched by
`mine_phase3.py`). The strawberry-vs-wheat crop-mix finding's epistemic
status is unchanged: **"observed, repeatable, RNG-exposed, not causal"** -
not in scope this phase, mentioned only for context.

## Limitations

1. HIRE eligibility is checked only for the *first* hire opportunity per
   step; multi-hire-per-step escalating cost is not fully modeled (see
   "Known simplification" above).
2. MELON action-rate gap is a global (not state-bucketed) finding due to
   thin per-bucket action counts (24 total SELL events across the whole
   175-file sample) - a larger, targeted sample (Phase 3's own
   recommendation from Phase 2) would be needed to get bucket-level
   support.
3. Replay population held at the same ~175-file ballpark as Phase 2, per
   explicit instruction not to scale up this phase.
4. No significance/hypothesis testing (e.g. binomial test) was run on the
   global rate gaps - they are reported as observed frequencies only.

## Recommended next steps (not acted on this phase)

1. If a Phase 4 (or a scale-up phase) is pursued, the MELON
   opportunity-conditioned action-rate gap (0.63% vs 3.65%, RNG_INDEPENDENT,
   fully opportunity-normalized) is the single most promising thread
   surfaced across all three phases so far for a targeted scale-up - it is
   the cleanest (RNG_INDEPENDENT) divergence found, but currently has too
   few action events (24 total) for bucket-level or statistical confidence.
2. Extending `mine_phase3.py` to model multi-hire-per-step escalating cost
   would tighten the HIRE reconstruction, though the current global-rate
   result does not suggest HIRE is a promising lead.
3. A formal significance test (e.g. Fisher's exact test on the MELON
   7/1110 vs 17/466 contingency table) would sharpen the
   PLAUSIBLE_BUT_UNPROVEN tier finding above without requiring more replay
   data - a compute-only next step, not a sampling one.
