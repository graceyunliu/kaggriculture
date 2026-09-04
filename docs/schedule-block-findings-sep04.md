# Scheduled-opening block — findings (Sep 4, 02:00)

Goal: an all-our-code candidate beating H10 (tape d0–9 → C1). Yardstick: seeds 11–20, both seats, vs `candidates/H10.py`.

| candidate | vs H10 | note |
|---|---|---|
| C1 | −13.9k (0-10) | baseline |
| a65aa7a26283 (best Air candidate) | −6.1k (2-8) | crop-heavy, herd 6→10 |
| **H10A** = tape d0–9 → a65aa economy | −2.1k (2-8) | a65aa's post-day-10 economy is *not* better than C1's; its +6k over C1 comes from its own opening |
| S11 schedule block (8 melons) | −25k | |
| S12 (12 melons) | −33k | cash trap: animals escape days 1–3 |
| S12 + feed rotation | −24k | rotation fixes the trap (12 melons now viable) |
| S12 + rotation + idle-deposit | −21.6k | |
| C1 + sweep-steal (idle hands take other sweeps' tasks) | −18.6k | worse than C1 |
| C1 + sell_hourly / drop_min / capital_hour2 / melon_rush | −14k to −27k | no-op or worse |
| C1 + idle-deposit | −14.2k | no-op |
| schedule on a65aa params | −50k | cash trap (open_cows 3) |

## Blocks written (evolve/blocks/, uncommitted)
- `economy_schedule.py` / `economy_schedule_full.py` — Yuan800 d0–11 schedule as a policy over targets (hands, animals, seeds, land, JIT feed).
- `animal_routing_rotation.py` — when wheat is short, animals fed yesterday skip a day; at-risk (1 unfed day) fed first. **Keep** — this is what lets a 12-melon opening survive on $30 cash, and it is the frontier's measured behaviour.
- `sweep_steal.py` / `sweep_steal2.py` — rejected.
- `dispatch_idledrop.py` — idle units carry products to the shed and DROP (with sell_hourly). Neutral on C1; small gain on the schedule block.

## What the per-hour traces showed (seed 11, S12rot vs H10)
- Days 1–6 our hands idle 50–120 unit-turns/day: the chassis waters one-shot crops alternate days (correct — weeds only after 2 unwatered days, yield only counts in the second half of life). H10's daily watering is waste. Early idle is not the loss.
- Day 6: 10 wool + 5 fertilizer sit in hands from h15 to h23; sold at day-7 dawn → cows bought day 7 not day 6. Idle-deposit fixes the mechanism but is worth ~0 on C1 because C1 buys capital at hour 0 anyway.
- Melons: ours reach yield 6 one day later than H10's (missed waterings in the day-6–10 window while 3 hands idle: sweeps of 6 tasks are claimed by 3 units, others find empty pools and PASS; the steal path in `_crop_step` is only reachable after finishing a sweep). Sweep-steal fixed the idling but lost money anyway (hands walk across the map for one task).
- Head-to-head melon dump: H10 sells 60 at $272 at day-11 h0, we sell 30 at the same tick and 24 the next day at $189, then $122.
- After day 12 the stock economy with 15–17 animals plants only 46–58 tiles (a65aa: 82–89) — load model vs MAX_HANDS starves crops. H10 (13–16 animals, C1 economy) nets +60k days 12–30; S12rot +50k; a65aa +67k from 8–10 animals.

## Conclusion
The tape's value is a *coupled* days-0–11 state (13 animals + 72 perfect melons + 2 quadrants + $15k at day 12). Reproducing it piecewise with our executor loses each piece to a side effect (cash trap, price crash, crop starvation). The isolated mechanisms (steal, drop, sell-hourly) are all ≈0 or negative on C1 — consistent with the routing-oracle result: execution-only changes don't pay on this economy. Next step is not more knob shots; it is the planner (docs/SPEC-day-planner-executor.md) or an ES run over `SCHED` numbers *with* rotation + idle-deposit as the base, on the Air, with H10 as the yardstick.
