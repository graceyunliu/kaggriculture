# O12_EVENING_DEPOSIT: sell before the opponent's morning batch (Sep 9, late)

Naming note: this candidate was called O10 while being built; it is O12 in the repo because the parallel
Sep 9 session had already used O10 for `O10_O9_MELON_LATEFERT` (O9 + melon late-fert). Same file, same numbers.

Candidate: `candidates/O12_EVENING_DEPOSIT.py` (zip: `submissions/O12_EVENING_DEPOSIT.zip`).
Diff base: `candidates/O9_O8_ENDGAME.py` (O8 throttle + O5 endgame). Only additions: the `EG` knobs
`evening_deposit`, `evening_force`, `evening_force_min`, `same_turn_sell=3`, and the two dispatch rules below.

## 1. How it was found

`evolve/action_audit.py` wraps the engine's `_apply_unit_action` and checks whether each of our unit
actions changed engine state. O9 has zero no-op actions (O2's shared-stock fixes hold), but 12-14% of
all unit-turns are PASS, and 74% of those idle turns fall in hours 19-23: the day's work is done and
the crew stands around. Meanwhile everything harvested that day rides in workers' pockets until the
end-of-day auto-drop puts it in the shed, where it is sold at hour 0 the next morning. Two costs:

1. Whatever exceeds the 100-item shed cap at the auto-drop is discarded (~5 units/game on average,
   64 units on one melon/wheat day of seed 5). Real, but small.
2. The hour-0 sale is in per-unit lockstep with the opponent's hour-0 sale. The engine's price curves
   are steep above I0 (MILK linear -$2.1/unit, STRAWBERRY -$1.92/unit, WOOL/MELON quadratic) and carry
   a premium below it, so every unit of ours sold in that collision faces the opponent's interleaved
   units. This is the dominant cost.

## 2. The rules

- **Idle deposit (from h18, days < 29):** a unit whose `_crop_step` returns nothing (it would PASS)
  and is carrying product walks to the nearest shed tile and DROPs. Free: it was idle.
- **Forced deposit (from h20, days < 29):** every unit carrying >= 3 units of product heads home and
  DROPs, overriding crop work (animal routes excepted).
- **Same-turn sells** for those drops (`same_turn_sell=3` = day 29 or hour >= 18), so the goods are
  sold the evening before, alone in the market, instead of at hour 0 in lockstep.

## 3. Results (paired both seats, master engine, zero agent errors throughout)

Vs O9, fresh seeds 101-200 (n=100), sweep of the forced-return hour (idle rule fixed at h18):

| variant | margin/game | t | won-lost |
|---|---|---|---|
| idle rule only (h18) | +$2,818 | 9.26 | 89-11 |
| + force h16 | -$3,941 | -5.29 | 32-68 |
| + force h17 | -$224 | -0.39 | 50-50 |
| + force h18 | +$3,683 | 6.34 | 77-23 |
| + force h19 | +$5,432 | 12.91 | 93-7 |
| **+ force h20, min 3 (shipped)** | **+$5,600** | **11.74** | **94-6** |
| + force h20, min 1 | +$5,102 | 10.40 | 89-11 |
| + force h20, min 6 | +$5,741 | 14.18 | 96-4 |
| + force h21, min 1 | +$4,374 | 9.62 | 87-13 |
| + force h22, min 1 | +$3,801 | 11.57 | 90-10 |

Idle-rule start hour alone: 14 +$2.3k, 16 +$2.1k, 17 +$2.1k, 18 +$2.8k, 19 +$2.6k, 21 +$1.9k.
Idle rule without evening same-turn sells: +$1,540 (the SELL timing is the point, not the drop).

Confirmation of the shipped configuration:

| matchup | seeds | margin/game | t | won-lost |
|---|---|---|---|---|
| O12 vs O9 | fresh 201-300 (n=100) | +$6,714 | 14.17 | 94-6 |
| O12 vs O9 | held-out 11-30 | +$6,709 | 5.79 | 19-1 |

Against real opponents, held-out 11-30, with O9's own margin on the same seeds for reference:

| opponent | O12 | O9 | delta |
|---|---|---|---|
| C1 | +$18,252 (20-0) | +$15,023 | +$3,229 |
| clone (opp_scenario_v14) | +$33,021 (20-0) | +$30,898 | +$2,123 |
| tape peterparker | -$19,955 (4-16) | -$25,735 | +$5,780 |
| tape alaylm | -$30,053 (0-20) | -$33,224 | +$3,171 |
| tape yangkuang2 | -$19,543 (2-18) | -$24,516 | +$4,973 |
| tape bahaenes | -$20,412 (1-19) | -$19,327 | -$1,085 |

The edge transfers to opponents that do not play our strategy (tapes sell on their own fixed
schedules), which is what the ladder needs. Still loses to every tape, but the gap to the tape line
shrinks 15-25% in one step, the first own-code change to move it at all.

## 4. Mechanism check

Revenue per item (10 paired games, O12 in seat 0 vs O9): total revenue is nearly identical
($90.7k vs $91.0k) while quantities are identical, so the gain is not "more stuff sold". Per-seat
margins are often equal to the dollar in both seats (seed 119: +$10,138 / +$10,138), consistent with a
deterministic pricing effect rather than a seat-order artifact. A traced day shows the divergence
starting the first day cash differs at a decision threshold (day 8, seed 119), i.e. the extra revenue
from better prices compounds through earlier hires/animals.

Market state observed in one game (both sides O-family): MILK glutted from day 9 (price $13-53 vs base
$160 during days 15-24), WOOL $5-31 days 18-24 until a YARN_STORE unlocks, STRAWBERRY scarce days 9-20
($164-203) then glutted from day 21 ($11-43), MELON +100 units (only the town center consumes melon,
1/day), FERTILIZER has no consumer at all and drifts down linearly. Those glut prices are the reason
timing matters so much, and they point at the next lead: holding drained-market products (milk, wool)
late and releasing them at the end, never holding fertilizer or melon. Drafted as `O13_HOLD.py`, untested.

## 5. Files

- `candidates/O12_EVENING_DEPOSIT.py`, `submissions/O12_EVENING_DEPOSIT.zip`
- `evolve/action_audit.py` (no-op / idle / overflow / drop-hour audit), `evolve/o5_eval.py` (`--variant`, `--per-seed`)
- `candidates/O13_HOLD.py` (next lead, not yet measured)
