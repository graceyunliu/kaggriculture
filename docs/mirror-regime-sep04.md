# Sep 4 — H31 ladder pull and the mirror regime

## Ladder pull (sub 56019923, score 1658.7)

15 games, 13-1 real plus one self-match vs our other submission. All reproduce exactly. **The divergence guard never fired: every game is the tape verbatim for all 719 steps.** Final money $53k–$152k depending on seed and opponent.

| opponent | steps differing from our tape | shared SELL steps (of 213) | result |
|---|---:|---:|---|
| graceyunliu (self) | 0 | 213 | LOSS $57.0k vs $57.7k |
| 12 mid-ladder agents | 717–719 | 1–4 | all WIN |
| Yang Kuang Ou | 702 | 22 | WIN $122k vs $118k |
| iamlonely | 583 | 50 | LOSS $58.5k vs $62.5k |

H31's tape is not Yuan800's (698/719 steps differ) and shares only ~80 SELL steps with any cluster tape.

## Mirror decomposition (H31 vs H31, seeds 1–10)

Same units both sides; contested prices: strawberry $149→$96, milk $108→$52, melon $242→$198, fertilizer $50→$42 — ≈$28k less sales than uncontested (vs V3_12). The engine quotes both players the same pre-commit price per unit within a step, so there is no seat edge inside a step.

## Sell-shift specialist (`tools/sell_shift.py`)

Moves every SELL k steps earlier, bounded by a per-step shed trace of the mirror so nothing over-sells. Held-out seeds 11–30, both seats:

| candidate | vs H31 (exact mirror) | vs strawhats | vs yuan800 | vs atakan | vs shirabe | vs V3_12 |
|---|---|---|---|---|---|---|
| H31 | 0 | −$131 (10-10) | +$1,601 | +$5,751 | +$21,401 | +$38,916 |
| M1_k1 | **+$4,811 (20-0)** | +$173 (11-9) | +$1,702 | +$5,524 | +$20,506 | +$38,254 |

Only pays against a byte-identical tape — on the ladder that is our own other submission. Not shipped. (`candidates/M1_k{1,2,4,8}.py` kept for reference.)

## The loss was a seed lottery

`Opponents/tape_iamlonely_105603965.py`, `Opponents/tape_yangkuang_105603038.py` built from the replays. Held-out 11–30 both seats:

| | margin | t | seed W-L |
|---|---|---|---|
| H31 vs iamlonely | +$6,288 | 2.4 | 12-8 |
| H31 vs yangkuang | +$8,232 | 3.8 | 16-4 |

In every matchup seat-0 wins == seat-1 wins: the seed decides, not the seat. A fixed tape cannot react to the seed.

## Conclusion

Opponent detection is free (`obs["farms"]` shows both farms from step 1), but "detect and switch" has nothing to switch to: near-mirror games are decided within-game by market state and weeds at ~$5k margins. That needs a runtime-adaptive policy within ~$5k of the tapes — the planner line — before a per-regime objective or a router is worth building.
