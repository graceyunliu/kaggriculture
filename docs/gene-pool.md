# Gene-pool governance

The immutable reference and the experimental champion are different objects.
`candidates/O26_CARROT_SIZING.py` and `evolve/chassis.py` remain frozen so old
candidate identities and the O26 equivalence guard stay reproducible. New evolution
runs default to the experimental champion recorded in `evolve/gene_registry.json`.

## Status classes

- `validated_small_positive`: replicated and safe to inherit internally, but not by
  itself a reason to spend a ladder submission.
- `validated_inherited`: previously validated and already present in the immutable
  reference lineage.
- `validated_interaction_pair` or `validated_bundle`: reusable only as the recorded
  composition unless a new ablation proves that its parts stand alone.
- `candidate_gene`: promising but still selection-exposed or missing a population gate.
- `rejected`: retained as negative evidence and never inherited.

## Current experimental champion

O33 = O26 + `FERT_DENIAL4` (`fert_buy: 3 -> 4`). The effect is a market interaction,
not merely extra private production: on four fresh leader streams and seeds 295-314,
own money moved +$262/game, opponent money -$273/game, and margin +$535/game
(`t=2.57`, 80 opponent-seed cells). Historical blocks 235-294 were also directionally
positive, with significant pooled margin on two of three blocks.

The fertilizer family is frozen after adoption. The next independent positive mechanism
must be evaluated as a preregistered 2x2 composition:

| Cell | Policy |
| --- | --- |
| Base | O26 |
| Fert | O26 + FERT_DENIAL4 |
| New | O26 + new gene |
| Cross | O26 + FERT_DENIAL4 + new gene |

Report the main effects and the interaction (`Cross - Fert - New + Base`) for both own
money and margin. The cross becomes the experimental champion only when it preserves
the new gene's benefit on disjoint seeds and does not reverse either component's own-money
effect. Periodically rerun the full composition against current public ladder streams.

## Recovered lineage genes

A Sep 11 audit of project history recovered eight validated mechanisms that O33 already
inherits but the first registry draft omitted: lifecycle-aware husbandry, coupled intraday
release-and-sell, the O8 animal-claim throttle, the O16 crop orchestrator, the O22 melon
morning bundle, O24 strawberry sizing, O25's marginal hire cap, and O26 carrot sizing.
They are now explicit registry entries rather than implicit candidate ancestry.

Use `docs/PROMPT-history-gene-audit.md` when asking another agent to search its private task
history. The prompt requires source-level evidence and records rejected near-misses so the
gene pool does not become a collection of selection noise.
