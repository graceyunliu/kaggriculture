# O5_ENDGAME: end-of-game conversion fixes on O4 (Sep 9)

Candidate: `candidates/O5_ENDGAME.py` (submission zip: `submissions/O5_ENDGAME.zip`).
Diff base: `candidates/O4_PRODUCTIVE_SERVICE.py` (the submitted best own-code candidate).
Variant: `candidates/O6_SHED4.py` = O5 + route shed trips to all four access tiles (see §4).
Port: `candidates/O9_O8_ENDGAME.py` = the same fixes on O8_PURE_ANIMAL_THROTTLE, which became the
frontier the same day (see §5). Submission zip: `submissions/O9_O8_ENDGAME.zip`.

Provenance: a Codex session found this lead and reported +$332/game (20 dev seeds, 16 paired wins)
and +$292/game on 100 fresh seeds (89-11, t=7.59) before being rate-limited. Its candidate file was
never saved to the repo, so this is an independent rebuild from the description, re-measured from
scratch on the cascade harness (`evolve/cascade.py::evaluate`, paired, both seats, master engine).

## 1. The leak

The engine processes unit actions before market orders every turn (`interpreter`: `_apply_unit_action`
loop, then `_process_market`). `episodeSteps` is 720 and DONE fires at `step >= 718`, so the last
action the engine processes is day 29 hour 22; the day-29 end-of-day auto-drop never runs. Anything a
unit is still carrying after h22 is worth $0, and anything dropped into the shed at h22 is only worth
something if a SELL for it lands in that same turn.

O4 built its market orders from the observation's shed snapshot before dispatching units, so product
DROPped at h22 was never sold, and its day-29 return rule (go home only when carrying >= 3 units)
left 1-2 unit remainders in hand. `evolve/endgame_leak.py` (seat 0 vs C1, seeds 1-10) measures what
O4 ends the game holding: **~$519/game of product at list price** (range $0-$1,470), plus dead
final-hour work (DIG / WATER on ongoing crops at h22).

## 2. The three changes (all gated on day 29 unless noted)

1. **Same-turn deposit sells.** `_agent` now dispatches units first, sums the product carried by every
   unit whose action is DROP on a shed-access tile, and passes it to `economy()` as `pending_drop`,
   which adds it to the sellable shed count. Over-asking a SELL is a harmless no-op in the engine.
   Knob `EG["same_turn_sell"]`: 2 = day 29 only (default), 1 = all game, 0 = off.
2. **Deadline return.** Any unit carrying >= 1 unit of non-animal product heads for the nearest shed
   tile once `hour + dist >= 22` and DROPs on arrival. Overrides animal routes.
3. **Final-day work filter.** `_crop_pools` / `_task_valid` drop plant, dig, fertilize and
   ongoing-crop watering on day 29 (their payoff is at an end-of-day refresh that never comes); keep
   HARVEST and WATER of a non-ongoing crop inside its yield window (WATER raises `yield_units`
   immediately in the engine, so water-then-harvest still pays). `_crop_step` and `_build_route` also
   require `hour + travel + actions + distance-home <= 22` before committing to a task.

O5 ends every one of the 10 leak-check games with $0 carried and $0 unsold.

## 3. Results (paired, both seats, master engine, zero agent errors everywhere)

Head-to-head vs O4, fresh seeds 101-200 (100 seeds, 200 games):

| variant | margin/game | t | seeds won-lost |
|---|---|---|---|
| **O5 (all three, day-29 sell)** | **+$372** | **9.63** | **97-3** |
| same-turn sell only | +$142 | 6.82 | 85-14 |
| sell + deadline return | +$317 | 8.95 | 98-2 |
| sell + work filter | +$147 | 5.08 | 79-21 |
| deadline return + filter, O4 selling | -$7 (dev 1-20) | -0.07 | 11-9 |
| all three, same-turn sell ALL game | -$10 | -0.05 | 49-51 |

Reading: the same-turn SELL is the enabling piece (returning cargo without it changes nothing, because
the h22 drop is never sold), the deadline return roughly doubles it, the work filter adds ~$55.
Selling deposits one hour earlier throughout the game is a wash and just adds trajectory noise that
buries the endgame gain, so the default is day 29 only.

Dev seeds 1-20 vs O4: +$522/game, t=2.06, 20-0 (every paired total positive; the low t is one $9.9k
outlier seed, not sign disagreement).

Held-out seeds 11-30 vs the usual opponents (O4's own numbers reproduce exactly on this harness):

| opponent | O5 | O4 (recorded) | delta |
|---|---|---|---|
| C1 | +$13,438 (t=14.91, 20-0) | +$13,164 | +$274 |
| V3_15 | +$15,370 (t=14.47, 20-0) | +$15,065 | +$305 |
| real clone (opp_scenario_v14) | +$32,566 (t=10.22, 20-0) | +$32,084 | +$482 |

No regression anywhere; the gain is the same order of magnitude against every opponent, as expected
for a pure end-of-game conversion fix that does not touch strategy.

## 4. Codex's pending question: use all four shed-access tiles? (O6_SHED4)

The engine accepts DROP/PICKUP from any of the four inner-corner tiles whether or not that quadrant is
LOCKED (shed ops resolve before the LOCKED guard; movement onto LOCKED tiles is legal), and
`_spawn_hand` puts new hands on all four tiles (NWSE, least-occupied) from day 0. O4/O5 only route to
unlocked tiles, so a hand spawning on (5,4)/(4,5)/(5,5) with one quadrant owned walks to (4,4) before
every PICKUP/DROP. `EG["all_shed_tiles"]=1` routes to all four.

O6 (O5 + all four tiles) vs O5, fresh seeds:

| seeds | n | margin/game | t | won-lost |
|---|---|---|---|---|
| 101-200 | 100 | +$358 | 1.10 | 60-40 |
| 201-400 | 200 | +$801 | 2.89 | 113-87 |
| 401-500 | 100 | -$36 | -0.09 | 50-50 |
| 501-800 | 300 | +$308 | 1.50 | 161-139 |
| dev 1-30 | 30 | +$524 | 0.60 | 20-10 |

**Pooled over all 700 fresh seeds (1,400 games, per-seed paired totals): +$407/game, t=2.94, 384-316 (55%), median +$308, per-seed SD $3.7k.** That clears the project's t >= 2 bar, but only on the pooled sample.

Reading: lean-positive but small relative to the trajectory noise it introduces (it changes early-game
movement, so the whole game diverges and per-seed SD is ~$3.5k). Any single 100-seed set can read
anywhere from a wash to +$800. Unlike the endgame fix it is not a near-deterministic gain.
O6 vs O4 directly on seeds 401-500: +$321/game (t=0.85, 55-45), i.e. on that set the added noise
swamped the clean +$372 endgame gain.

## 5. Port onto O8 and recommendation

While this was running, a parallel session promoted **O8_PURE_ANIMAL_THROTTLE** (O4 + the
`animal_claim` throttle raised from <2/<1 to <4/<2; +$1,905/game held-out vs O4) to frontier, and
separately tried an all-game same-turn drop-to-sell top-up (`O5_SAMETURN_SELL.py`) and found it null
(dev +$23, held -$169). That null and this doc agree: selling a deposit one hour earlier mid-game is
worth nothing (§3, all-game variant -$10). The whole value is in the final processed hour, and only
when cargo is actively brought home for it. The two results are not in conflict; the earlier test
measured the wrong hour.

The endgame fixes are orthogonal to the throttle change, so they were ported as **O9_O8_ENDGAME**
(diff vs O8 = exactly the O5 changes):

| matchup | seeds | margin/game | t | won-lost |
|---|---|---|---|---|
| O9 vs O8 | fresh 101-200 (n=100) | **+$389** | **10.40** | **91-9** |
| O9 vs O8 | held-out 11-30 | +$377 | 3.84 | 20-0 |
| O9 vs O4 | held-out 11-30 | +$2,193 | 3.86 | 17-3 |

O9 vs O4 is O8's own gain plus the endgame gain, i.e. the two are additive. O9 ends every leak-check
game with $0 carried.

**Recommendation: ship O9_O8_ENDGAME** (frontier + endgame conversion). O5 is the same fix on O4 if O8
is ever rolled back. The four-tile routing (§4) is left as a knob: ~+$0.4k pooled over 700 seeds at
t=2.94 but noisy enough that a single 100-seed set can read as a wash.

None of this changes the ladder picture: these candidates still lose to the tape-hybrid line
(H32/M2/M4) the way every own-code candidate does; a ~$0.4k endgame gain is two orders of magnitude
below that gap, and the real-ladder check on O4 (18-20) says the local C1/V3_15 margins do not predict
ladder win rate anyway.

## 6. Files

- `candidates/O5_ENDGAME.py`, `candidates/O6_SHED4.py` (differ only in the `all_shed_tiles` knob and header), `candidates/O9_O8_ENDGAME.py` (O5 fixes on O8)
- `submissions/O5_ENDGAME.zip`, `submissions/O6_SHED4.zip`, `submissions/O9_O8_ENDGAME.zip` (main.py = the candidate byte-for-byte)
- `evolve/endgame_leak.py` (carried / unsold value at game end, final-hours action dump)
- `evolve/o5_eval.py` (paired head-to-head runner with `--variant k=v` EG knob overrides, `--per-seed`)
