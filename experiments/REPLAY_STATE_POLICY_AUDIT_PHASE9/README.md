# Phase 9: Lead 4 -- chore-type priority ordering (weeds vs. harvest)

`_build_sweep()` (candidates/V3_15.py:724) chains crop-tile tasks in tier
order `["urgent", "harvest", "weeds", "water"]` (or with fert:
`["urgent","fert","harvest","weeds","water"]`). Phase 2 only measured
idle-vs-assigned hand share (parity found, closed); which specific chore
type wins when multiple compete was never mined. The chassis's own
in-file comment history notes weeds were previously moved ahead of
harvest/water in an earlier version, then apparently reverted (current
order has harvest before weeds) -- itself circumstantial evidence this
ordering has mattered before.

`variant_weeds_first.py`: two-line change, `weeds` moved immediately
after `urgent`/`fert`, ahead of `harvest`, otherwise byte-identical to
`candidates/V3_15.py`.

Result: consistently positive-signed effect across 4 independent
seed/opponent tests (matched seeds vs. 1 opponent, fresh seeds vs. 3
opponents), pooled t=1.97 (n=160, borderline p~0.05). See
`REPORT_PHASE9_CHORE_PRIORITY.md` -- reported as PARTIAL_EVIDENCE, not
promoted to CONFIRMED at this sample size.
