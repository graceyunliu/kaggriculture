# Decision Bottleneck Map

Status: descriptive measurement only. O42 and the audited provenance tracer were not
modified. No policy, causal, or intervention conclusion is authorized by this map.

## Cohort and validation gate

- Fixed-shop canonical panel: seeds 301–340, four opponents, both seats, 320 games.
- Strong: positive final opponent-relative margin (52 games). Weak: negative margin
  (268 games). There were no ties.
- Every traced game passed paired money, step, error, action-stream SHA256, and
  terminal-observation SHA256 parity.
- Comparisons residualize each metric within opponent × seat.
- A divergence is called reproducible only when full-panel BH-adjusted q <= 0.05,
  its direction repeats in both reciprocal seed halves (301–320 and 321–340), and
  repeats in every leave-one-opponent-out check with adequate strong-game support.
- Counts are means per game unless explicitly described as per invocation.

## Map

| Decision family | Actual choice-set size, strong / weak | Dominant real rejection path, strong / weak | Reproducible divergence | Seed halves | Opponent robustness | Earliest reproducible day |
|---|---:|---:|---|---|---|---:|
| Seed crop ranking | 5.000 / 5.000 reached candidates per ranking round | zero feasible quantity: 18.58 / 15.72; demand-room guard: 11.29 / 14.10 | Choice-set size and selected-best count do not differ. Weak games record more submitted ranked seed orders (27.94 vs 26.33) and more committed seed units overall (163.71 vs 147.56). Room rejection is higher in weak games; zero-quantity rejection is higher in strong games. | Pass for those four path/stage differences | Pass | 8 (zero quantity and committed units); 9 submitted; 10 room |
| Crop-task orchestration | 27.03 / 28.09 real tasks per orchestration call | unreachable unit-task pair: 30,878 / 30,669; no fertilizer carried: 21,844 / 26,779 | Weak games expose larger task pools, more feasible unit-task pairs, and more assignments. No-fertilizer pair rejection is also higher in weak games. Unreachable rejection does not diverge reproducibly. | Pass for pool, feasible-pair, assignment, and fertilizer-path differences | Pass | 8 pool/pairs; 9 assignments; 12 fertilizer path |
| Animal route composition | 0.226 / 0.161 pending, unclaimed candidates per route-build invocation | Individual removals inside the pending/claimed comprehension are not emitted; no rejection path may be inferred | Strong games expose more real route candidates (980.0 vs 716.5 total per game) and select more stops (353.0 vs 292.3). These are exposure/selection distributions, not evidence that a route guard caused the outcome. | Pass | Pass | 7 selected stops; 8 candidate exposure |
| Site selection | 16.62 / 15.89 feasible sites per actual site-selection call | no-candidate return: 0 observed in this panel | Per-call choice-set size does not pass the reproducibility gate (q=0.0575). Strong games invoke site selection more often and therefore have higher total candidate exposure and more empty-site selections. This is scale of site-placement demand, not a demonstrated rejection bottleneck. | Pass for invocation/selection totals, not per-call choice size | Pass for invocation/selection totals | 10 invocation/selection totals |
| Task stealing | 6.159 / 6.134 reached urgent+general candidates per steal invocation | general candidate rejected for time: 641.17 / 620.28 | Choice-set size, time rejection, and actual transfer count do not differ reproducibly. Some intermediate best/score events differ, but the submitted transfer endpoint does not pass the full gate (q=0.0575). | Transfer direction repeats, but full gate fails | Transfer direction repeats, but full gate fails | None for a completed transfer bottleneck |

## Stage accounting

### Seed crop ranking

| Stage | Strong | Weak | Reproducible? |
|---|---:|---:|---|
| Candidate reached | 265.87 | 254.76 | No |
| Best selected | 44.90 | 43.66 | No |
| Ranked order recorded/submitted | 26.33 | 27.94 | Yes, weak higher |
| Seed units committed by engine, including non-ranking seed paths | 147.56 | 163.71 | Yes, weak higher |
| Engine commit rejected | 0 | 0 | No observed events |
| Executed after commit | Unobserved | Unobserved | Not inferable |

The trace does not label crops as globally unavailable. It observes five real crop
loop candidates whenever a ranking round runs and records only the real guards those
candidates reach. No ungenerated alternative is added to the denominator.

### Crop-task orchestration

| Stage | Strong | Weak | Reproducible? |
|---|---:|---:|---|
| Actual task-pool entries accumulated across calls | 19,432 | 20,196 | Yes, weak higher |
| Feasible unit-task pairs | 87,174 | 97,553 | Yes, weak higher |
| Selected assignments | 3,830 | 3,992 | Yes, weak higher |
| Submitted/committed/executed task | Unobserved | Unobserved | Not inferable |

Pair-level guards use a different denominator from task counts: the same task can be
tested against multiple free units. Collision rejection happens after feasible pairs
are sorted and means that the unit or task was already consumed by an earlier pair;
it is not an independent unavailable opportunity.

### Animal routes, sites, and stealing

- Route candidates are already filtered by O42's real pending and claimed tests when
  captured. Phase 1 does not emit each pre-filtered animal, so it cannot attribute
  candidate absence to one of those guards.
- Site selection observed no `site_no_candidate` return. Higher total site-selection
  exposure in strong games comes from more calls; the feasible choice-set size per
  call did not robustly differ.
- Stealing reached many alternatives, but almost all general candidates were removed
  by the actual remaining-time guard. That path is frequent in both cohorts and does
  not diverge reproducibly. The actual transfer endpoint also does not diverge.

## Descriptive conclusion

The strongest reproducible differences are not a single rejection bottleneck shared
across families. They form three distinct provenance patterns:

1. Seed ranking starts with the same five-candidate choice set and similar best
   selection counts, then differs at quantity rejection, order recording, and commit.
2. Weak games present more crop tasks and feasible unit-task pairs and receive more
   assignments; the divergence is workload scale plus a higher no-fertilizer pair
   rejection count, not an unreachable-task bottleneck.
3. Strong games present more already-pending/unclaimed animal route candidates and
   more site-selection calls. Phase 1 cannot identify which upstream guard formed
   that route candidate difference.

Task stealing provides a negative result: a large, real time-rejection bottleneck is
present, but neither that rejection nor completed transfers separates strong and weak
games robustly.

These are observed decision-path distributions only. The chronology does not show
that any rejection caused the later result, and the map makes no strategy recommendation.
