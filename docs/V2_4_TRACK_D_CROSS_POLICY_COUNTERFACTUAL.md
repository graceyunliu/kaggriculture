# V2.4 Track D — Cross-Policy Counterfactual Search

**Classification: `NO_LARGE_OPPORTUNITY_FOUND`.** No candidate was built or run.

## Setup verified

- V10.6 (primary control): `experiments/V2_3B_V10_6_SELF_CONTAINED/candidate/main.py`,
  SHA-256 `f6abd7f066685bf43a797d468b0694eefa15956375850e68b8f76174d45c907e` — verified before
  and after this work, unchanged.
- V9.3 (historical reference): `experiments/V2_3B_V9_3_SELF_CONTAINED/candidate/main.py`,
  SHA-256 `9d2703faf8e58c55697dc3948d06c3a1f4caac52927a38358e131d9b0344bf0b` — verified before
  and after this work, unchanged.
- Engine: `/tmp/v23p_env` has Python 3.11.15 and `kaggle_environments==1.32.3` importable — no
  new venv was needed.
- Neither frozen file was edited in place at any point; no copies were mutated into a candidate
  because no candidate was justified (see below).

## Prior evidence read

Read in full: `docs/V2_3F_V93_V106_DIFFERENTIAL_AUDIT.md` and
`artifacts/v2_3f/v93_v106_differential.json`, plus the summary docs for every "already-rejected"
track named in the assignment: V2_3R (global worker/task assignment — routing), V2_3J (joint
production-chain / gross-value ranking), V2_3H (deadline-aware cross-domain arbitration), V2_3G
and V2_3S Track A (static/dynamic animal service capacity), V2_3I (production-event-aware
fertilizer scheduling — fertilizer collection-vs-application target ordering), V2_3L (production
cohort synchronization), V2_3S Track B (generic movement-time-share reduction).

The differential audit's central finding: V9.3 and V10.6 have **exactly one** source-level
behavioral difference (radius-3 near/far crop siting). It states explicitly that "all economic
targets, seed quantities, animal gates, labor rules, fertilizer rules, land rules, selling,
routing, and opponent observation code are otherwise byte-identical." Every other measured
difference (sales mix, WATER/HARVEST/FERTILIZE counts, movement totals, MILK/WOOL/FERTILIZER
sale deltas) is a downstream, path-dependent *consequence* of the siting change, not evidence of
a second independently-triggerable rule, and the audit explicitly warns against decomposing per-
category cash contributions from it.

## Seams considered

1. **Fertilizer collection-vs-application sequencing.** This is the exact territory V2_3I already
   tested: it froze a "minimum (days-to-next-production-event, distance, y, x)" targeting rule for
   in-transit fertilizer among V10.6's already-eligible targets, using a real, generous
   pre-implementation bound (24 missed events / seed 920, $4,896 upper bound, $67,932 across 16
   seeds). It lost the mandatory seed-920 gate by **-$9,686** and was frozen as `REJECTED`
   immediately per fail-fast contract. Re-running the same seam under a different name would
   violate the "do not retest already-rejected mechanisms" instruction.

2. **Animal-product (MILK/WOOL) collection timing.** Read `animal_maintenance_action` and
   `_pasture_priority` in V10.6 directly (lines ~1544-1610 of
   `experiments/V2_3B_V10_6_SELF_CONTAINED/candidate/main.py`). This code — pasture selection by
   minimum priority tuple, feed/care/harvest/fertilizer-collect branching, wheat restock and
   product-deposit gating — is confirmed byte-identical between V9.3 and V10.6 by the differential
   audit's own "otherwise byte-identical" statement (also directly re-confirmed by inspection: no
   siting-radius logic touches this function; it operates purely on `view["my_pastures"]` and
   worker position). Because it is unchanged between the two policies, it cannot be the source of
   any V9.3-vs-V10.6 divergence — the MILK +103 / WOOL -73 sale deltas reported in the audit are a
   consequence of siting-driven worker-position and crop-mix shifts changing *when* workers pass
   near pastures, not of a distinct collection-order rule that differs between the policies. Any
   new priority formula introduced here would be a fresh, hindsight-fitted heuristic layered onto
   already-closed territory (service-reservation/routing, V2_3G/V2_3H/V2_3R), which the assignment
   explicitly excludes.

3. **Sales-timing / reinvestment behavior.** Read the `market_price` / `_sell_priority` / SELL
   dispatch code (lines ~726-1350). This too is confirmed byte-identical between V9.3 and V10.6
   by the audit ("selling... otherwise byte-identical"). The reported sale-mix shift (995 more
   MELON, 292 more CARROT, 424 more FERTILIZER, 103 more MILK sold; 501 fewer STRAWBERRY, 415
   fewer TOMATO) is exactly the shape you'd expect from planting more one-time crops and fewer
   ongoing crops — it is fully explained as a downstream consequence of the one controlled siting
   change, not a second, independently controllable sales-timing rule. There is no online-feasible
   rule to freeze here that is distinct from siting itself.

4. **Production-cohort / planting-day synchronization** and **deadline-aware arbitration** were
   both explicitly considered as candidate seams and are already closed by V2_3L and V2_3H
   respectively, both `REJECTED`/`LOW_VALUE` with real trace gates showing no addressable
   opportunity.

## Why no seam qualifies

Every downstream behavioral difference documented in the differential audit traces back to code
that is byte-identical between V9.3 and V10.6 (animal maintenance, selling/market logic, land,
labor, opponent observation). A "genuinely separate mechanism" requires a controllable rule that
is not simply a restatement of the one already-frozen siting change and not a re-run of a
seam this project has already tested to a decisive result (V2_3I, V2_3L, V2_3H, V2_3G/S-A, V2_3R,
V2_3S-B). No such seam was found: the two remaining candidates (animal-product collection order,
sales-timing) are both operating on code paths proven identical across the two policies, meaning
any new rule there would not be "cross-policy" in origin at all — it would be a fresh heuristic
invented purely from hindsight correlation with V10.6's win, which the assignment explicitly
forbids ("Do NOT optimize terminal cash retrospectively").

## Bound

No candidate mechanism was frozen, so no online-feasible bound was computed for a build (Phase 2
is contingent on Phase 1 producing a frozen hypothesis). The one directly relevant real bound
already on record is V2_3I's: 24 missed fertilizer-timing events on seed 920, upper bound $4,896
(seed 920) / $67,932 (16 seeds), which measured a **loss** of $9,686 against that bound when
tested — reinforcing that the fertilizer-sequencing seam is closed, not merely under-bounded.

## Classification

**NO_LARGE_OPPORTUNITY_FOUND.** No candidate was built (Phase 4 not entered), no seed-920 test was
run (Phase 5 not entered), no package was produced (Phase 6 not entered). Both frozen source files
were read-only for the duration of this track and their hashes are unchanged.
