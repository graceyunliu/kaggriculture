# Replay Mining Phase 2: Intra-Day Decision-Triggered State Audit

> **Provenance correction (added after Phase 4A):** "opponent" / "opp"
> throughout this report means the opposing seat observed inside Grace's
> own replay history (`Replays/Auto/mine/`), not an independently sampled
> leaderboard/ladder reference population. See [INDEX.md](INDEX.md) for
> the full correction and what it does and doesn't affect. Numbers and
> verdicts below are unchanged.

Date: 2026-09-08. Follow-on to `REPORT.md` (Phase 1) - read that first for the
replay format, engine RNG code (`vendor/kaggle_environments_engine/kaggriculture.py`,
`_end_of_day`, lines ~837-867), and the Phase 1 crop-mix finding, all reused
unchanged here rather than re-derived.

**Final status: PARTIAL_EVIDENCE.**

## Rationale for this phase (Grace's, preserved verbatim in spirit)

Phase 1 sampled state once per in-game day (hour==0, right after the
engine's end-of-day reset). That reset zeroes `hires_today` and clears
`hands`/`farmer` queues, so day-boundary snapshots structurally cannot see
hiring, chore-assignment, fertilizer-hold, or melon-admission decisions -
they had already been erased by the time of the snapshot. Phase 1's
NO_ROBUST_SIGNAL result for those decision types was therefore a
measurement-resolution artifact, not a real negative finding. This phase
fixes the sampling moment, not the sample size.

## Method: decision-triggered sampling

New script `experiments/REPLAY_STATE_POLICY_AUDIT/mine_phase2.py` scans
**every hourly step** (not just hour==0) of each replay and, per
player-slot per step, checks the actual `action` payload
(`{"farmer": [...], "hands": [[...],...], "market": [...]}`) plus
`private.shed` inventory for five decision types:

- **HIRE**: `market` list contains a `["HIRE", ...]` entry that step.
- **PLANT**: `farmer` or any hand's action list contains a `PLANT` token
  followed by a crop name - captures the *actual chosen crop at the moment
  of planting*, not a day-boundary tile-count proxy as in Phase 1.
- **FERTILIZE**: `shed.FERTILIZER > 0` that step (fertilizer available to
  apply) is the trigger; decision = `APPLY` if a `FERTILIZE` token appears
  in `farmer`/any hand list that step, else `HOLD`.
- **MELON**: `shed.MELON > 0` that step is the trigger; decision = `SELL`
  if `market` contains `["SELL", "MELON", ...]` that step, else `HOLD`.
- **CHORE**: whenever a player has `hands > 0`, decision =
  `IDLE_MAJORITY` if half or more of that step's per-hand action lists are
  empty, else `ASSIGNED_MAJORITY`.

State signature is unchanged from Phase 1 Level A:
`(day, cash_bucket, land_tier, labor_bucket)` - `day` is now the exact
in-game day (not `day//3`) since decision-triggered sampling no longer
needs day-bucketing for tractability.

## What was instrumented at decision-resolution vs what remained out of reach

**Instrumented successfully, at true decision-moment resolution:**
HIRE, PLANT (crop choice), FERTILIZE (apply vs hold), MELON (sell vs hold),
CHORE (idle vs assigned share of hands).

**Remained out of reach this phase, and why:**
- **True hire *opportunity* (hire vs deliberately-did-not-hire) could not
  be captured** - the script only logs steps where a HIRE action actually
  occurred; it does not yet establish "hiring was affordable/available and
  the agent chose not to," because that requires reconstructing the
  farmhand market's price/availability model, which is not directly present
  in the observation (`town`/`market` do not list a hand-hire price
  schedule inspected this pass). So HIRE findings below are
  actual-hire-moment snapshots only, not hire-vs-no-hire comparisons.
- **Melon "admission" (accept a sale opportunity vs let it expire) could
  not be distinguished from ordinary hold** - the data shows shed-MELON
  presence and whether a SELL action occurred, but does not capture whether
  a favorable price window was passing at that moment (would need
  `market.prices` time-series correlation, not attempted this pass).
- **Fertilizer target-tile eligibility** (which specific tiles could
  legally be fertilized right now) was not reconstructed from the board;
  `FERTILIZER` stock > 0 was used as a coarse proxy for "a fertilize
  decision was live," which likely over-counts true opportunities.
- Level C (exact/local per-tile context) was not needed for any finding
  below.

## Decision-triggered snapshots mined

175 replay files scanned (same ballpark as Phase 1's 265, intentionally not
scaled up per Grace's instruction) across the same 15 directories, all
hourly steps (up to 720/file). Raw event counts recorded (both cohorts
combined): **HIRE 1,361; PLANT 3,815; FERTILIZE 7,717; MELON 1,576;
CHORE 20,301** - a large increase in usable observations per decision type
versus Phase 1's day-boundary sampling, from the same replay population.

## Evidence tables per decision type

### PLANT (crop choice at the moment of planting)

19 state buckets (>=8 observations/side, modal action differs, each side's
mode >=40% within-bucket) survived the same divergence filter used in
Phase 1. Direction breakdown: **14/19 buckets** have opponents choosing
WHEAT while I choose a non-wheat crop (STRAWBERRY/CARROT/TOMATO/MELON);
**2/19 buckets reverse this** (I choose WHEAT while opponents choose
STRAWBERRY or MELON); **3/19** are other non-wheat-vs-non-wheat pairs. Full
table in `FINDINGS_PHASE2.json`. Support ranges from 8-90 observations/side,
3-8 distinct opponent identities per bucket.

This is **majority-consistent with, but not a clean uniform confirmation
of,** the Phase 1 day-boundary crop-mix finding - see the epistemic-status
note below.

### HIRE

749 opponent-side and 612 mine-side actual-hire events recorded. No state
bucket met the >=8-per-side-with-divergent-mode filter for HIRE specifically
in this sample - i.e. **no robust hire-moment divergence was found**, but
per the limitation above, this only compares *when hiring occurred*, not
hire-vs-abstain, so it is a weak test. Classified NO_ROBUST_SIGNAL for this
phase, with the true hire-opportunity question still open.

### FERTILIZE (apply vs hold, given `FERTILIZER` stock > 0)

Aggregate rates: mine HOLD 3301 / APPLY 299 (91.7% hold); opp HOLD 3815 /
APPLY 302 (92.7% hold). **Materially indistinguishable between cohorts.**
No state bucket produced a qualifying divergence. This is now a genuine,
decision-resolution **negative finding** (not a Phase-1-style measurement
artifact): both cohorts hold fertilizer roughly 9-in-10 times it's in
stock, at comparable rates.

### MELON (sell vs hold, given `MELON` stock > 0)

Aggregate rates: mine HOLD 1103 / SELL 7 (99.4% hold); opp HOLD 449 / SELL
17 (96.4% hold). Both cohorts overwhelmingly hold melon inventory rather
than selling in any given hourly snapshot (consistent with melon being
sold in occasional batches rather than continuously). The raw sell-rate
gap (0.6% vs 3.6%) is suggestive but **no individual state bucket had
enough SELL events to pass the >=8-per-side support filter** - flagged
PLAUSIBLE_BUT_UNPROVEN, explicitly not promoted further.

### CHORE (idle vs assigned share of hands, given hands > 0)

Aggregate: mine ASSIGNED_MAJORITY 10,092/10,092 (100% of qualifying
snapshots); opp ASSIGNED_MAJORITY 10,209/10,209 (100%). **No idle-majority
snapshots were observed for either cohort in this sample.** This is a
genuine negative finding at decision resolution: labor is kept
busy-assigned essentially always by both cohorts, at least at the
per-hand-empty-list granularity this script checks (it does not verify the
*chore itself was a good choice*, only whether hands were left with an
empty action queue that hour).

## RNG classification (new 4-value taxonomy)

Per Grace's instruction, findings use exactly: `RNG_INDEPENDENT /
RNG_EXPOSED / RNG_COUPLED / UNKNOWN`. `RNG_COUPLED` corresponds to what
Phase 1 called `RNG-CONFOUNDED` (the literal same-`random.Random`-object
chaining from weed-spawn draws into a shop-unlock `rng.choice` call, which
only happens on days where `(day+1) % 3 == 0`, i.e. `day % 3 == 2`).
`UNKNOWN` is used where this pass could not establish exposure either way.

Classification rule applied (see `aggregate_phase2.py:rng_class`):
- `HIRE`, `MELON`: **RNG_INDEPENDENT** - both are market/inventory decisions
  that do not read the day's `random.Random` object or depend on board-tile
  occupancy.
- `PLANT`, `FERTILIZE`: **RNG_COUPLED** if the bucket's `day % 3 == 2`
  (the literal weed-then-shop-unlock chained-draw day), else
  **RNG_EXPOSED** (board-tile occupancy that gates available plant/fertilize
  targets can still be shifted by policy-dependent weed-spawn draws on
  other days, per the Phase 1 mechanism, without the further shop-unlock
  chaining).
- `CHORE`: **UNKNOWN** - chore targets can include tending
  weed-affected/board-occupancy-affected tiles, but this pass did not trace
  chore-assignment logic against tile state closely enough to classify
  confidently either way.

Findings-by-class this phase: **RNG_EXPOSED: 12, RNG_COUPLED: 7,
RNG_INDEPENDENT: 0 findings surviving the support filter (though HIRE/MELON
events themselves are classified RNG_INDEPENDENT in FINDINGS_PHASE2.json
even where no qualifying divergence was found), UNKNOWN: 0 findings
surviving the filter (CHORE produced no qualifying divergence at all).**
All 19 PLANT-decision findings are RNG_EXPOSED or RNG_COUPLED - none are
claimed RNG_INDEPENDENT, and none are promoted to a causal conclusion.

## Findings by confidence tier

- **DIRECTLY_OBSERVED**: 19 state-conditioned PLANT-decision divergences
  (table above / FINDINGS_PHASE2.json), each RNG_EXPOSED or RNG_COUPLED.
  Also DIRECTLY_OBSERVED: FERTILIZE hold-rate parity (~92% both cohorts) and
  CHORE full-assignment parity (100% both cohorts) - i.e. two genuine
  negative findings, not measurement artifacts.
- **STRONGLY_SUPPORTED**: none promoted to this tier this phase, consistent
  with the hard constraint against upgrading RNG_EXPOSED/RNG_COUPLED
  findings to causal status.
- **PLAUSIBLE_BUT_UNPROVEN**: the melon sell-rate gap (0.6% mine vs 3.6%
  opp) - directionally suggestive, statistically under-supported at the
  per-state-bucket level this pass required.

## Strawberry-vs-wheat epistemic status (unchanged, per instruction)

**Carried forward unchanged: "Observed behavioral divergence, repeatable
across opponents/seeds, but RNG-exposed and not established as causal."**
This phase's decision-triggered PLANT data is **consistent with, and at the
same epistemic level as,** the Phase 1 finding - it is reported here as
corroborating evidence, not new causal support and not an upgrade in
confidence tier. Note for accuracy: the decision-triggered data is *more
mixed* than the clean day-boundary aggregate suggested (14/19 buckets favor
the original direction, 2/19 reverse it, 3/19 involve other crops) - this
phase does not claim the finding got stronger; if anything it surfaces that
the true picture is noisier at fine resolution, which is itself useful
input for a possible Phase 3 but is not treated as evidence either way here.

## Negative findings

- FERTILIZE apply/hold rates are statistically indistinguishable between
  cohorts (~92% hold, both) - genuine decision-resolution negative finding,
  supersedes Phase 1's measurement-artifact NO_ROBUST_SIGNAL.
- CHORE idle-vs-assigned share shows no divergence - both cohorts keep
  hands ~100% assigned at the per-hour-empty-queue granularity checked -
  genuine decision-resolution negative finding.
- HIRE: still no robust divergence found, but this remains an incomplete
  test (see Limitations) rather than a clean negative.

## Limitations

1. HIRE and MELON decisions are logged only at moments an action occurred
   (or stock was present), not against a reconstructed
   opportunity/eligibility baseline - true "did/didn't act on an available
   opportunity" comparisons need a hire-price and price-window model not
   built this pass.
2. FERTILIZER-stock > 0 and MELON-stock > 0 are coarse triggers; they do not
   verify a specific tile was actually eligible for fertilizing or that a
   specific melon lot was sellable at that instant.
3. CHORE classification (idle vs assigned share of hands) does not evaluate
   chore *quality* or *type*, only whether hands were left unassigned.
4. Replay population held at ~175-265 files (same ballpark as Phase 1, per
   explicit instruction not to scale up this phase) - state buckets with
   thin support (8-15 observations/side) should be treated cautiously.
5. RNG classification for CHORE is UNKNOWN because chore-assignment logic
   was not traced against board/weed state this pass.
6. No Phase 6 (Phase-1 numbering)/counterfactual testing was attempted here
   either - same infrastructure gap as Phase 1.

## Recommended next steps (for a possible Phase 3 scale-up)

A Phase 3 population increase, if pursued, should prioritize:
1. **PLANT decisions** at the specific state buckets in
   FINDINGS_PHASE2.json with thin support (n<20/side) - these are the
   buckets most likely to firm up or dissolve with more data.
2. Building a **hire-price/hire-opportunity reconstruction** so HIRE can get
   a true decision-vs-abstain test, not just decision-moment snapshots.
3. Building a **market price-window model** so MELON's suggestive
   0.6%-vs-3.6% sell-rate gap can be tested at real support levels - this is
   the single most promising thread this phase surfaced for a targeted
   (not blanket) scale-up.
4. FERTILIZE and CHORE do not need more data given this phase's already-firm
   parity findings; a Phase 3 scale-up should skip them.
