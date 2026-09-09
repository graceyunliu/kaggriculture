# Phase 10: Lead 5 -- fertilizer target-tile eligibility timing (CONFIRMED)

Phase 2 explicitly flagged fertilizer target-tile eligibility as never
reconstructed ("FERTILIZER stock > 0 used as a coarse proxy... likely
over-counts true opportunities"). The real eligibility gate is
`_fert_eligible()` (`candidates/V3_15.py:157`), which requires
`age >= c["first"] - 1` (crop must be within 1 day of its first
fertilizable age) among other conditions.

`variant_fert_earlier.py`: single-line change, `age >= c["first"] - 1` ->
`age >= c["first"] - 3` (tiles become fertilizer-eligible 2 days earlier
in their growth cycle), otherwise byte-identical to `baseline_V3_15.py`
(a plain copy of `candidates/V3_15.py`).

Tested with the direct head-to-head harness (`mini_engine.evaluate()`,
the same one `evolve/cascade.py` uses) from the start this time, per the
lesson from Lead 4's failed indirect-design confirmation.

Result: **CONFIRMED**. Positive, statistically significant, and replicated
across two independent 200-game seed batches (t=2.45 then t=2.97 on a
fresh batch; pooled t=3.84, n=400) and consistent in direction against an
external opponent tape as well (+$2,246/game vs tape_kwa). See
`REPORT_PHASE10_FERTILIZER_TIMING.md`.
