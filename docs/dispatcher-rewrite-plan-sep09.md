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
