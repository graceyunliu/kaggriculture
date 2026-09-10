# Closing the architectural gap to the frontier tapes — plan for review (Sep 9, late)

Starting point: `O12_EVENING_DEPOSIT` (current frontier). Residual on the 4 real ladder tapes (n=30, both seats): −$19.9k / −$27.3k / −$19.3k / −$20.0k per game, 2-28 to 6-24. Everything below is measured with `tools/move_ledger.py`, `tools/gap_profile.py`, `tools/action_mix.py`, `tools/layout_probe.py`.

## What the instruments established

1. **Per-hand throughput, not moves, is the gap.** Same unit-turns per game (≈6.6k). Tape: 3,141 work actions with 10-11 hands (≈285/hand); ours: 2,382 with 13-14 hands (≈170/hand). Tape PASS 469, ours 840 (675 of them at h18-23; ~6/game mid-day on days 9-27 → our hands are saturated h0-17 and unemployed after).
2. **Where our extra moves go** (433/game): task-to-task walking (+387). Long legs (≥4): FEED 190 vs 8 (routes are built for whichever unit comes first in index order, wherever it stands), WATER 736 vs 342 (post-first-sweep dispersal at h6-8; evening slack watering is free). Spawn walks +139 (more hand-days). We make *fewer* shed trips than the tape.
3. **Layout explains the walking but not the throughput.** Giving O12 the tape's layout (17 animals in the inner ring, 32-tile strawberry band, wheat far — `L2`) makes our task-walk moves equal the tape's (2,025 vs 2,023) but work stays 2,350 vs 3,141, PASS rises to 1,005, and money drops −$21k on the panel: the obligation set never materializes (35-40 plants vs 57, 2.3 quads vs 3 — buying 17 animals early starves land and seeds), and per-hand throughput doesn't move. Same for daily service (`L3`, −$23k).
4. **The tape's per-hand throughput comes from structure, not speed:** 72% of its task legs are 1 step (ours 57%), it does 3-4 actions per animal visit (chain hist 3:241 4:229 vs ours 3:188 4:106), it waters daily in contiguous rows, and it spreads work to h19-23.
5. **Prior "expert executor" (P6) never achieved this in full games** — its travel 1.01 was on a bench replaying expert-supplied days; in full games it ran travel 1.16, idle 41%, weeds 38. The execution block is unsolved at full-game scale, not closed.
6. Everything piecewise-ported from the tape loses on our dispatcher (herd, wheat, layout, opening, allocation — 4 separate confirmations this week). Everything execution-only on our plan gains ≤ $3k. They are coupled: the tape's plan only pays at the tape's throughput.

## Design: a throughput-first dispatcher, then a plan sized to it

Replace the `sweep` + `animal_routing` blocks of O12 (keep economy/market/endgame/evening-deposit as is). Three layers:

**A. Herder loops (animals).** 2-3 dedicated units per day own the inner ring. At h1 (after the wheat order lands) one pickup of the day's wheat, then a fixed loop over the ring doing the full chain at each animal — FEED, CARE, COLLECT_FERTILIZER, HARVEST — with no re-planning mid-loop, and a single DROP at the end. Herders never take crop work; crop hands never take animal routes. Target from the ledger: FEED long legs 190 → <20, animal chain length 3-4, animal actions/game ≈ tape's.

**B. Block sweeps (crops).** At h0 partition the day's crop tiles into contiguous blocks (row/column runs of adjacent tiles, ≤8 tiles) and assign one block per crop hand for the whole day; the hand walks the block tile-to-adjacent-tile doing every due action at each tile in one visit (WATER + HARVEST + replant + FERTILIZE), then a second pass in the afternoon for tiles that became harvest-ready, then the O12 evening deposit. Target: ≥70% 1-step legs, moves/work ≤ 0.95, mid-day PASS unchanged, evening PASS reduced.

**C. Plan sized to measured capacity.** Hands = number of blocks + herders (expect 10-11, not 14); seeds/land/herd targets come from a capacity model calibrated on the ledger's actual actions-per-hand of the new dispatcher (not `_load_model`'s 20 load units). Only after A+B pass their ledger gates is C tuned; until then keep O12's economy untouched so the execution change is measured in isolation.

## Acceptance gates (in order; none skipped)

1. Ledger gates on A and B in full games vs `tape_alaylm`, seeds 1-6: moves/work ≤ 0.95; FEED long legs < 20; animal chain 3-4; PASS ≤ 550; missed_water and weeds not worse than O12. If a gate fails, fix the mechanism — do not proceed to money.
2. Paired money vs O12 (self-play), dev 1-10 and held-out 11-30, both seats, t ≥ 2 on held-out.
3. Tape panel (`evolve/batch_vs_o8.py` with `BASE=candidates/O12_EVENING_DEPOSIT.py`), n ≥ 30 seeds, 5-opponent mean — this is the ladder-relevant number; per-opponent deltas at n=10 are RNG-path noise (±$15k).
4. Only then C (plan resizing), each change re-gated by 1-3.

## Size of the prize and the risk

If A+B reach the tape's throughput at O12's obligation set, the direct saving is ~3-4 hand-days of fib hire cost (~$300-400/day) plus ~200 currently-missed obligations/game; the real prize is that C then becomes viable (a 17-animal / 57-plant / 3-quad plan is what actually pays — L2 showed the layout is executable at the tape's move count once the obligations exist). Risk: block assignment is a rewrite of the load-bearing block (v10 found global dispatch load-bearing 4 times); pinned crews lost on v10's plan — the difference here is that the ledger gates catch a throughput regression before any money test, and C is sequenced after, not with, A+B.

## Not on this plan (already refuted this week)

Ring reservation alone (−$1.8k to −$6.1k), proximity ownership rules (held-out t ≤ 1.06), water-tier pacing (−$2.2k to −$5.9k), herd/wheat/hands/late-filler levers on the current dispatcher (all lose on the panel), fertilizer/wool/rot/early-idle probes (null).


## Build log — layer A (herder loops), Sep 9 late

Implementation: `evolve/gen_herders.py` → `candidates/H1_HERDERS_PER3.py` (herder loops, 3 animals each, max 5 herders, built at h1 from all pending animals split into angular arcs, full wheat need reserved so the loop waits at the shed until the h1 order lands; ordinary route-building gated until h14), `H2_SPAWN_CHAINS[_R3]` (additionally every free hand at h1 chains the nearest unclaimed pending animal within 2/3 steps before going to crops). Also fixed a real bug in `_route_step`: when the shed had no wheat at h1 the route's pickup was reset to 1 unit, which is what forced the mid-loop refill trips.

Two build mistakes caught by the ledger/trace before any money test: (1) assigning at h0 — hands do not exist at h0 (re-hired at h0, spawn at h1), so only the farmer was ever a herder and loops ran past h23 → 48 escapes/game; (2) `HERD_PER=7` — a chain is 4 actions per animal (FEED, CARE, COLLECT, HARVEST) plus walking, so one loop covers ~4-5 animals a day, not 7.

Ledger vs `tape_alaylm`, seeds 1-6 (O12 baseline → variant):
- H1 PER4: FEED long legs 205 → 50; PASS 850 → 781; work 2,268 → 2,372; moves/work 1.39 → 1.37; escapes 0; money 82.7k → 74.5k. Animal work shifted LATER (h14-23: 129 → 216 actions) — loops are slow.
- H1 PER3: paired vs O12 dev +$468 (t=0.34) — neutral. PER4 −$1,595 (t=−1.68). PER5 −$6,957 (t=−4.72).
- H2 spawn chains: spawn_walk 660 → 444 as intended, but task_walk 2,121 → 2,637, missed_water 400 → 541, money → 64k. Hands that chain an animal at spawn start their crop sweep late and the crop day compresses.

**Gate status: not met** (moves/work 1.37 vs ≤0.95; FEED long legs 50 vs <20; PASS 781 vs ≤550). No money promotion.

**What the build taught:** the tape's animal efficiency is not a routing policy we can bolt on — it is a consequence of (a) animals sited on the ring at the shed so the spawn walk *is* the animal visit, and (b) a crop set small and compact enough (32 strawberries at dist 3.8) that the crop day still fits after the animal chain. On O12's obligation set (60-80 plants, animals at 2.4) either ordering loses: animals-first compresses crops (H2), crops-first leaves animals late (H1). The ring layout on its own lost (B12) because it pushes 60+ strawberries outward. So layer A cannot pass its gates independently of layer C (a plan sized to the crew): the sequencing in this plan was wrong — layout+plan and dispatcher have to be built and gated together, with the ledger as the readout, starting from a deliberately smaller crop set (≈32 strawberries) so the ring is affordable. That is the next build, and it is a bigger one.


## Build log — global orchestrator (Sep 9 night) — FOR REVIEW, not promoted

Grace's framing: workers self-select the next highest-priority task with no view of where the other 13 are; replace that with an orchestrator that computes a decision matrix each turn. Built on O12 as `evolve/gen_orchestrator.py` → `candidates/X1_ORCH_FLATPRIO.py`: every turn, for every free unit × every open crop task, cost = distance + priority weight (urgent 0, harvest/fert/wwater 0.5, plant/water 1.0, weeds 1.5, slack 6 after h14) − 0.75 commitment bonus for the task the unit is already heading to; assign by global minimum cost (greedy over the sorted matrix, one task per unit). Execution at the tile is unchanged (`_crop_step` chains); animal routes/setup untouched.

Ledger vs tape_alaylm, seeds 1-6 (O12 → X1): spawn_walk 660 → 474, long WATER legs 674 → 499, legs ≥8 steps essentially gone, PASS 850 → 716, work 2,268 → 2,370, moves/work 1.39 → 1.34, money 82.7k → 89.7k.

Paired self-play vs O12: dev +$5,655 (t=6.59, 10-0); held-out +$3,911 (t=8.15, 19-1); seeds 31-80 +$4,493 (t=7.26, 42-8); 81-105 +$4,629 (t=6.15); 106-130 +$3,956 (t=5.58). Consistent +$4-5.7k over 130 seeds. Commitment bonus matters: without it +$2,372 (t=1.55). Fixed benchmarks (dev): vs C1 +$23,961 (t=11.7, 10-0; O8 was +$14,800), vs V3_15 +$25,976 (t=17.5), vs O9_MELON_LATEFERT +$10,938 (t=4.9).

Tape panel: **null.** Own-money metric over 130 seeds ≈ −$100/game; switched the harness to paired MARGIN (cand−tape vs O12−tape; `PANEL_METRIC=margin`, now default — the ladder scores margins and both players in a game share the shop draw, so margin is far less exposed to the RNG-path lottery: per-opponent t's went from ±2 to ±0.5): −$451/game (t=−0.39, n=30). Resolution at n=30 is about ±$1.2k, so the true tape effect is between −$3k and +$2k.

Why self-play and tapes disagree (measured): X1 sells 32% more strawberries vs the tape (186 → 245 units/game) and more of everything, but final money barely moves — the extra volume goes into a shop-limited market. In self-play that volume takes share from the O12 opponent dumping at the same hours (zero-sum), vs a tape it only depresses our own price. **Self-play margins overstate gains that come from volume of glut-prone goods.** Redirecting the orchestrator's capacity to glut-resistant products did not help either: wheat 0.5/animal −$2.3k (t=−1.8), herd schedule 17 −$9.9k (t=−6.8) on the margin panel.

Extensions tried: animals inside the matrix (`X3`, 1-stop routes) — spawn walks 304 but a wheat trip per animal and 5 escapes; multi-stop animal routes seeded from the matrix with day-progress urgency (`X4`) — escapes 0, work 2,489 (+10% over O12) but missed waterings 390 → 544 and money down (self-play −$1.0k, panel −$2.6k): animal urgency pulls hands off watering. Crop-only orchestrator stays best.

Zip for review: `submissions/X1_ORCH_FLATPRIO.zip`. Verdict: the orchestrator is the first change that moves the ledger the right way (walking, idle, throughput all improve) and it dominates every O-family and C1-era benchmark; against the frontier tapes it is neutral because the throughput lands on saturated products. The tape's remaining +$20k is therefore not a throughput problem any more — it is what the throughput is spent on, in a demand-limited market. Note the panel resolution problem for anything ≤$2k: use margin metric, n ≥ 100.
