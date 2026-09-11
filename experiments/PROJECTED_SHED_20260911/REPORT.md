# Projected end-of-day shed pressure

## Result

Closed as `rejected_not_a_gene`. Overflow is real and observable, but recalling
productive routes to recover it does not replicate as an economic improvement.

## Measurement

`tools/projected_shed_audit.py` records the complete shed and carried inventory at
hour 23, subtracts the policy's planned sales, and reproduces the engine's deterministic
per-item end-of-day truncation. O33 versus `tape_bahaenes`, seeds 151-170, both seats:

- 32 discard events in 40 games;
- 31 of 32 were visible after planned hour-23 sales;
- 346 units discarded: 270 wheat, 64 carrot, and 12 strawberry.

Thus the old `SHED_AT_CAP` tag understated the causal fact: pressure is mostly inventory
still carried by workers, not stock sitting at the shed. Selling additional shed wheat was
exactly neutral because O33 already sells every unit above its three-unit feed buffer when
the shed is full.

## Minimal intervention

`O39_PROJECTED_SHED_RELIEF` checks full shed plus carried load. A worker carrying at least
three wheat leaves its route at the last hour from which it can still reach a shed, but only
when projected overnight load exceeds 100. Deposited cargo is handled by the existing
`INTRADAY_RELEASE_AND_SELL` gene. This reduced seat-0 discard from 177 to 100 units on the
diagnostic block and initially looked positive against the four fresh Majkel streams:

| Seeds | Cells | Own | t | Margin | t |
| --- | ---: | ---: | ---: | ---: | ---: |
| 355-374 | 80 | +136 | 2.56 | +190 | 2.96 |
| 375-394 | 80 | +19 | 0.58 | +30 | 0.69 |

The fresh replication collapsed and three of four stream means were slightly negative.

`O40_SEVERE_SHED_RELIEF` restricted recall to projected load of at least 110. On the
selection block it was weaker: own +$30 (t=1.53), margin +$53 (t=1.87), 80 cells.

## Constraint learned

End-of-day overflow is predictable, but most threatened inventory is low-value wheat and
the final crop route still has option value. A broad or severity-gated carrier recall pays
too much in displaced work for the recovered sale. Do not revisit shed pressure using only
current/projected load or another threshold sweep. A future attempt needs a zero-displacement
mechanism or item-specific proof that high-value cargo, rather than wheat, will be destroyed.
