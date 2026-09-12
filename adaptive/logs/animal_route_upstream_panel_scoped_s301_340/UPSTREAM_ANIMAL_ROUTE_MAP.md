# Upstream Animal-Route Provenance Map

Status: **stopped at upstream entry**. This is measurement only. O42 strategy logic
was not modified, and no policy, intervention, or species recommendation is made.

## Validation

- Foundation commit: `27069c65b04fd6270eed346de85f994cf2c7e6c8`.
- Canonical panel: fixed shops, seeds 301–340, four opponents, both seats, 320 games.
- Cohorts: 52 positive-margin strong games and 268 negative-margin weak games.
- All 320 instrumented/baseline pairs passed money, steps, errors, full action-stream
  SHA256, and terminal-observation SHA256 parity.
- All source bindings use fail-closed AST node and structural-context matching.
- Per-call conservation checks require:
  - raw candidates = claim removals + actual `_animal_pending` calls;
  - helper-accepted candidates = post-pending candidate list;
  - day-29 filtering cannot add candidates;
  - selected stops = stops in the returned route.
- Comparisons are opponent × seat residualized, BH-FDR corrected, and must repeat in
  both reciprocal seed halves and every leave-one-opponent-out check.

## Stop result

**The strong/weak divergence is already present in the raw `v["animals"]` input,
before any newly traced claim or pending-work filter executes.**

| Raw entry exposure | Strong | Weak | Difference |
|---|---:|---:|---:|
| Raw animal candidates accumulated across route calls, mean/game | 56,248.44 | 47,570.32 | +8,678.13 |
| Raw candidates per route call | 12.83 | 10.40 | +2.43 |

The opponent × seat residualized difference is +8,664.25, `t=8.49`,
`q_BH=7.92e-17`. Direction repeats in seeds 301–320 (+8,839.11), seeds 321–340
(+9,372.44), and all four leave-one-opponent-out checks (+6,737.71 to +11,477.92).
The earliest day on which the raw-entry difference itself passes the complete daily
replication gate is day 9.

This satisfies the required stopping rule. The added trace therefore cannot establish
an O42-controlled route-filtering stage as the origin of the route-candidate gap.

## Actual filter chain

Counts below are mean candidate exposures per game. They describe the real execution
path, but downstream differences are not promoted as origins after the stop trigger.

| Actual lifecycle stage | Strong | Weak | What the real code establishes |
|---|---:|---:|---|
| Raw `v["animals"]` candidates | 56,248.44 | 47,570.32 | Candidate exists before route filtering |
| Removed by existing-route claim guard | 22,637.54 | 19,962.15 | Tile position is already in `claimed` |
| Reaching `_animal_pending` | 33,610.90 | 27,608.16 | Candidate survived claim short-circuit |
| Rejected by `_animal_pending` | 32,630.87 | 26,891.62 | No useful feed, care, fertilizer, or yield condition is true |
| Remaining after pending guard | 980.04 | 716.54 | Actual post-comprehension `cands` |
| Removed by day-29 work filter | 0 | 0 | No removal observed in this panel |
| Added by late route-transfer fallback | 1.62 | 0.96 | Candidate taken from another real route |
| Reaching route construction | 981.65 | 717.50 | Actual `cands` before empty guard/pool construction |
| Stops selected | 353.00 | 292.28 | Actual nearest-stop append events |
| Routes returned | 131.62 | 111.46 | Non-null final route dictionaries |

For scale only, not causal interpretation:

- Claim removal rate is approximately 40.2% in strong games and 42.0% in weak games.
- Pending rejection among evaluated candidates is approximately 97.1% versus 97.4%.
- Pending acceptance is approximately 2.92% versus 2.60%.
- Selected stops per construction candidate are approximately 36.0% versus 40.7%.

These normalized rates do not support a story in which the traced route filters create
the large raw exposure advantage. The absolute downstream differences primarily carry
forward the already-existing difference in candidates entering the route function.

## Real helper paths captured

For every `_animal_pending` evaluation, the trace records the actual return plus the
real `_feed_useful` and `_care_useful` terminal paths where reached:

- already fed or day 29;
- feed final condition;
- already cared;
- next yield due tomorrow and its actual return;
- yield beyond horizon;
- pending-care bonus cap;
- care considered too early;
- care accepted;
- fertilizer availability;
- positive stored yield.

Accepted reasons can overlap because O42's final pending expression is an OR. A rejected
candidate has all four final reasons false. Raw helper-path counts are higher in strong
games because strong games enter the helper with more candidates; after the upstream
stop, they are not interpreted as independent bottlenecks.

## Boundary of the result

This trace begins at the real `v["animals"]` list supplied to `_build_route`. It does
not explain how that list acquired more animal tiles in strong games. Establishing that
would require a separately authorized measurement phase farther upstream of routing.

The statistically earlier day-7 difference in selected-stop counts does not override
the within-call provenance ordering: every selected stop descends from a raw candidate.
Daily significance can emerge at different times because counts have different variance.
The first robust raw-entry difference is day 9.

No strategy conclusion follows from this map.
