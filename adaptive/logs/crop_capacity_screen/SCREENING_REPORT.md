# Early/Midgame Crop Capacity Formation — Screening Result

Status: **SUPERSEDED — verdict suspended pending independent audit**.

The original STOP assignment in this file must not be relied upon. See
`../crop_capacity_evidence_repair/AUDIT_HANDOFF.md` for the repaired evidence
chain and its narrower conclusions.

This is measurement-only synthesis of existing certified artifacts. No games were
run, no tracer was changed, and O42 was not modified. The screen reuses:

- accepted Decision Provenance / Choice-Set traces for the fixed-shop 320-game
  panel (seeds 301–340, four opponents, both seats), with exact paired action and
  terminal parity;
- the existing start-through-day-10 lifecycle ledger for the same games; and
- the previously declared strong/weak definitions and reciprocal seed-half plus
  opponent robustness gates.

The two accepted analyses use different predeclared descriptive cohorts. The
lifecycle analysis compares opponent-seat-demeaned top and bottom quartiles
(80/80); the provenance analysis compares positive and negative final margins
(52/268) after opponent-seat residualization. Numbers below retain their source
cohort rather than silently merging the definitions. A candidate would need to
survive, not merely exploit, this cohort change to merit promotion.

Using the complete existing panel is computationally cheaper than generating a
new screening sample and avoids introducing a second cohort definition. This is
not a new large-panel run.

## Lifecycle screen

| Lifecycle stage | Existing observation | Reproducible strong/weak difference? | Interpretation boundary |
|---|---|---|---|
| State / market availability | Lifecycle quartiles: all five seed types available for 264 observed hours per game in both cohorts | No | Shop availability does not explain the divergence |
| Candidate crops actually reached | Provenance win/loss cohort: five real loop candidates per ranking round; 265.87 strong vs 254.76 weak total candidate events | No | O42 does not begin with a smaller crop choice set in weak games |
| Best crop selected | Provenance win/loss cohort: 44.90 strong vs 43.66 weak | No | No reproducible ranking-choice divergence |
| Quantity/rejection guards | Zero-quantity rejection is higher in strong games; demand-room rejection is higher in weak games | Yes, from days 8 and 10 respectively | These guards consume already-formed free-capacity, cash/labor, committed production, and demand-room state; they are not clean upstream causes |
| Ranked seed order recorded | Provenance win/loss cohort: 26.33 strong vs 27.94 weak | Yes, weak higher; earliest day 9 | Direction is opposite a simple “weak games fail to buy seeds” bottleneck |
| Seed units committed | Provenance win/loss cohort: 147.56 strong vs 163.71 weak | Yes, weak higher; earliest day 8 | Engine recorded no seed commit rejection; weak games commit more, not fewer, seeds |
| Plant-task opportunities | Weak games expose larger real task pools and more feasible unit-task pairs | Yes, earliest day 8 | This is workload/state scale already present when orchestration runs |
| Plant-task assignments | Weak games receive more assignments | Yes, earliest day 9 | No evidence that weak crop capacity is caused by failure to assign available work |
| Crop placement / capacity creation | Strawberry, melon, wheat, carrot, and tomato show no reproducible capacity-created advantage for strong games through day 10 | No | The upstream ranking/order differences do not become a robust strong-capacity advantage |
| Productive occupancy | No crop has a reproducible strong advantage through day 10 in the lifecycle analysis | No | No early crop-capacity trajectory separates cohorts robustly |
| Watering/service | Existing ledger records successful water actions, but no crop-level robust upstream bottleneck was established | No promotable finding | Counts after task-pool scale diverges cannot be interpreted as causal |
| Harvest / production | Lifecycle quartiles: melon realized yield is higher in strong games by 3.59 units per game; other major crops do not show a robust yield advantage | Melon only, downstream | Melon candidate selection, purchase, capacity creation, and occupancy do not diverge robustly first; yield is a consequence-stage association |
| Sale/use | Engine commits can show product movement, but existing certified provenance does not link each sold/used unit back to a specific crop asset | Unresolved | Asset-level sale/use attribution would require new measurement and is not justified by this screen |

## Why the apparent differences do not pass promotion

The real seed-ranking choice set and best-selection endpoint do not differ
reproducibly. The first reproducible differences are state-conditioned quantity
guards and a *higher* number of seed orders and committed seed units in weak
games. At the same time, weak games already expose larger crop-task pools and
more feasible work beginning on day 8. This means the rejection/order differences
are entangled with an already-different workload, free-capacity, committed-output,
and demand-room state.

The downstream melon-yield association cannot repair that causal ordering:
strong games do not first diverge in melon availability, consideration, selection,
commitment, placement, or productive occupancy. The yield difference therefore
does not identify a reproducible O42-controlled decision bottleneck.

Wheat provides the opposite pattern: weak games submit and commit more wheat
seed, but this does not produce a robust difference in wheat capacity creation,
occupancy, or realized yield. It is not evidence that buying fewer or more seeds
causes the later trajectory.

## Promotion decision

The required promotion condition is not met. The screen finds no reproducible,
potentially O42-controlled crop decision divergence that precedes rather than
responds to already-diverged game state.

Accordingly:

- no new tracer or lifecycle extension was built;
- no validation smoke or Claude audit is requested;
- no new panel is authorized;
- no intervention or strategy recommendation follows from this result.

The hypothesis is not worth further investigation under the stated promotion
rule. Asset-linked sale/use remains unobserved, but filling that gap would move
farther downstream and cannot establish the missing upstream decision bottleneck.
