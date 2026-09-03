# Sep 3 — two candidates that beat V3.11 and V3.12

All numbers: `mini_engine.py`, master (ladder) engine, both seats, paired margin per game. Dev seeds 1–10 were used for search; **held-out seeds 11–30 were touched only for the final rows below.**

## C1 — V3.12 chassis + frontier opening (`candidates/C1.py`, `submissions/C1_FRONTIER_OPENING.zip`)

Knobs on `candidates/K.py`: `opening=frontier` (day 0: 5 HIRE, 2 COW, 2 SHEEP, 8 MELON seed, 7 WHEAT seed, 5 WHEAT feed — $2,815 of $3,000), `early_hire_days=5` (hires are paid before the feed reserve on days 0–5), `feed_spare_poor=0` (no +3 spare feed when cash < $300), `open_melons=8`.

| opponent | seeds | C1 mean | opp mean | margin/game | t | wins |
|---|---|---|---|---|---|---|
| V3.11 | 11–30 | $91.9k | $79.2k | **+$12.7k** | 8.6 | 19-1 |
| V3.12 | 11–30 | $87.3k | $82.5k | **+$4.8k** | 3.6 | 16-4 |
| V3.11 | 1–10 | $99.4k | $88.3k | +$11.1k | 3.2 | 8-2 |
| V3.12 | 1–10 | $92.0k | $83.2k | +$8.8k | 3.5 | 10-0 |
| opp_scenario_v14 (Aug clone) | 1–10 | $90.2k | $78.7k | +$11.4k | 4.2 | 9-1 |
| opp_soil_v25 | 1–10 | $82.8k | $88.9k | −$6.1k | −1.9 | 2-8 |
| tape_yuan800 (Sep frontier) | 1–10 | $68.7k | $102.0k | −$33.3k | −6.5 | 1-9 |

Why it works: the raw frontier opening on this chassis lost **−$77k** — day-1 cash of $19 with a feed-reserve guard on hiring meant zero hands for three days and the herd escaped. Letting the $12 of hires go first and dropping the spare-feed buffer turned the same opening into +$8.8k. Eight melons (not 12) keeps ~$300 of buffer; that beat 6, 10 and 12.

## H10 — frontier tape for days 0–9, then C1 (`candidates/H10.py`, `submissions/H10_TAPE_HYBRID.zip`)

Replays the recorded action stream of Yuan800's seat in ladder episode 104892947 for steps 0–239, then hands control to the C1 policy (which rebuilds its state from perception each day).

| opponent | seeds | H10 mean | opp mean | margin/game | t | wins |
|---|---|---|---|---|---|---|
| V3.11 | 11–30 | $100.7k | $68.3k | **+$32.4k** | 15.7 | 20-0 |
| V3.12 | 11–30 | $88.7k | $70.4k | **+$18.4k** | 16.1 | 20-0 |
| opp_soil_v25 | 11–30 | $88.3k | $76.3k | +$12.0k | 7.5 | 20-0 |
| C1 | 1–10 | $87.5k | $68.9k | +$18.6k | 7.8 | 10-0 |
| tape_yuan800 | 11–30 | $62.6k | $89.6k | −$27.1k | −12.2 | 0-20 |
| tape_atakan | 11–30 | $62.5k | $82.0k | −$19.5k | −9.7 | 0-20 |

Switch-day sweep vs C1 (seeds 1–10): day 5 +$4.9k, day 8 +$10.6k, **day 10 +$18.6k**, day 12 +$5.6k. Days 5–10 of the tape's *execution* (intraday fertilizer sales funding just-in-time feed, 5 wheat tiles planted per day, cows bought at hour 16–17 from the day's proceeds, 8–11 hands) are worth ~$14k over our executor doing the same days with the same opening — the executor-conditional point in the rollout critique, measured directly.

**Decision for Grace:** H10 contains 240 steps of another player's public replay. That is what most of the top-30 does (the "2900+", V16, V14-clone notebooks are 720-step tapes), but it is not our code. C1 is entirely ours.

## What did not work on this chassis (all vs C1, seeds 1–10, both seats)

Wheat-tile floor 5: +$2.8k dev but −$2.1k held-out → rejected. Wheat 8/12: −$3k to −$15k. Holding wheat for the late price: negative. Buying/keeping fertilizer to apply: −$1k to −$4.5k. More hands (min 5/6, load 12/15): flat to −$3k. Bigger herd (demand share 0.75/1.0): −$6k to −$17k. Geese: −$4.4k. Melon floor 0, harvest every yield: noise. Every scaling lever loses because the dispatcher can't convert it — the same finding as Round 10, now with the frontier's own days 0–9 as the counterfactual.

## Remaining gap to the frontier tapes (H10 vs tape_yuan800, ~−$27k)

From `decompose.py`: wheat sales (−$15k; tape sells ~400 units from continuous 5-tile planting), melon timing (tape sells 72 melons on day 10 at $242; we sell later at $166), fertilizer volume (14 animals vs 10), eggs. Closing it means the executor: same-day deposit-and-sell, wheat cadence, and a herd the labor model can actually service.

## Tooling added today

`mini_engine.py` (no-install engine runner, traces, cache, both-seats; cache seat bug fixed — seat is now taken from the job, never from cached paths), `replay_verify.py`, `make_tape_agent.py`, `search.py` (knob factorials with a 3-seed screen), `decompose.py` (per-item revenue/price/timing diff), `candidates/K.py` (knobbed chassis), `candidates/round*.json` (all results).

## Sep 3, later — feed self-supply attempt (REJECTED, no new zip)

Motivation: H10's one ladder loss (Shirabe, reproduced exactly; systematic 6-14 vs `tape_shirabe`) and every frontier-tape decomposition put WHEAT at −$16k to −$22k: H10 buys ~440 feed units at $37 avg for its 18-animal herd and sells ~150; the tapes grow ~460 and sell late at $45–48.

Implemented on K.py: wheat rotation sized to the herd (`wheat_per_animal`, cap 18), a dedicated wheat-window watering tier ahead of harvest/water (`wheat_water_tier`), late selling (`wheat_sell_price`, `wheat_hold_days`, `wheat_stock`). 16-variant factorial vs C1, then the best as H10 hybrids on held-out seeds 11–30:

| variant | vs H10 | vs tape_shirabe | vs tape_yuan800 | vs V3.12 |
|---|---|---|---|---|
| H10 (reference) | — | −$6.9k (6-14) | −$27.1k (0-20) | +$18.4k (20-0) |
| H10w10 (1.0 tile/animal, tier, hold 2) | **−$2.4k (3-17)** | −$5.0k (6-14) | −$22.8k (0-20) | +$14.9k (19-1) |
| H10w07 | −$1.2k (3-17) | −$5.0k (6-14) | | |
| H10w05 | −$1.5k | −$7.8k | −$23.7k | |
| H10w10h0 (no hold) | −$2.3k | −$3.7k | | |
| + wheat_stock 40 | identical to H10w10 — the hold never engages | | | |

Verdict: a trade, not a gain — +$2–4k against tapes, −$1–4k against everything else, and no tape matchup flips (still 0-20 / 6-14). Not shipped.

Why it fails on this chassis (from `decompose.py`): post-day-10 wheat sales stay ~0 — the 18-tile target never gets land (3 quadrants ≈ 71 tiles vs 18 animals + 38 strawberry + 14 melon + 18 wheat), so feed purchases fall only 440→350 units; grown wheat that does exist is sold early at $35 because the reserve logic sells surplus the morning it lands, and the shed-capacity guard (100 units, all products) prevents stockpiling for the late price. Strawberry (−$9k, sold at $78 vs $93) is the other residual. Closing this needs the allocator to trade strawberry tiles for wheat when the herd is large, and a sale rule keyed to the wheat price trend rather than a floor — allocator/executor changes, not knobs.

## Sep 3, night — ladder pull #2 and H11 (`submissions/H11_TAPE_HYBRID_GUARDED.zip`)

`pull_ladder.py` (new; lists episodes via EpisodeService, fetches replays from kaggleusercontent, fingerprints opponents, verifies exact reproduction): H10 at 16 games, **10-5 real**, score 1143.5. All 16 reproduce exactly.

Losses: Shirabe (basin B, analyzed above), kiro and yuki #2 (hour-0 all-in variant, close games: −$8k, −$4k), Antigone_duckduck (V16 "8C/4S" tape, −$19k), and **straw hats — the first 53/48-cluster draw: $54k vs $175k**.

The straw-hats game exposed a failure mode, not a strength gap: its 43/38 wheat round-trip ran in lockstep with our tape's 53/48, prices moved, the recorded SELL revenue didn't arrive, the day-1 hires failed for lack of $7, and our tape kept executing feed/care actions for animals that were never placed. Herd 2→1→1 through day 9; the policy inherited $733 and 3 animals on day 10. Locally H10 vs `tape_strawhats`: **−$98k/game, 0-20** — far worse than C1's −$33k against the same cluster. Every 53/48 opponent on the ladder would do this to H10.

**H11** = H10 with two changes (`make_hybrid.py`):
1. Cycle-free opening: the tape's turn-0 "buy 53 wheat / sell 48" (a $133 no-op) is replaced by buying the 5 feed units directly; the rest of the tape is untouched.
2. Divergence guard: per-step signatures (money, hands, animals owned, shed wheat) from the source replay are embedded; if live animals-owned or hands differ from the recording by more than 1 (or cash falls >$800 and >50% below it), the tape is abandoned and the C1 policy takes over at once.

Held-out seeds 11–30, both seats:

| opponent | H10 | H11 |
|---|---|---|
| H10 (head-to-head) | — | −$5 (identical play when nothing diverges) |
| tape_strawhats (53/48 cluster) | **−$98.4k (0-20)** | **−$24.2k (0-20)** |
| tape_antigone (V16 8C/4S) | −$10.4k (4-16) | −$7.3k (5-15) |
| tape_kiro | +$3.4k (7-13) | −$4.4k (5-15) |
| tape_yuan800 | −$27.1k | −$28.3k |
| tape_atakan | −$19.5k | −$18.6k |
| tape_shirabe | −$6.9k (6-14) | −$6.9k (6-14) |
| V3.12 | +$18.4k (20-0) | +$18.0k (20-0) |

Same agent against everything H10 already handled; removes the $75k-per-game collapse against the opponents it will meet as it climbs. Ship H11 in place of H10.

Note on `tape_strawhats`: it was recorded against a collapsed H10, so its late-game sales assume an empty market; treat its absolute numbers as pessimistic for us and optimistic for it.

## Sep 3, late night — cluster best-response round → H30 (`submissions/H30_FULL_TAPE_GUARDED.zip`)

Knob search on the H11 chassis against the cluster tapes (`search_hybrid.py`: herd cap 14/18 × wheat tiles 0/8/12 × hold 0/2, seeds 1–8): every variant −$22k to −$26k cluster average. The post-day-10 policy cannot close the gap with any of these levers.

Then the switch day itself, with the divergence guard in place (seeds 1–8):

| switch day | vs tape_yuan800 | vs tape_strawhats | vs V3.12 | vs H11 |
|---|---|---|---|---|
| 10 (H11) | −$28k | −$25k | +$18k | 0 |
| 12 | −$24.0k | −$21.3k | +$7.3k | −$2.9k |
| 15 | −$15.8k | −$15.9k | +$21.8k | +$7.1k |
| 20 | −$11.4k | −$12.5k | +$28.1k | +$10.1k |
| **30 (full tape + guard)** | **−$0.4k** | **−$2.0k** | **+$41.3k** | **+$23.5k** |

Without the guard (H10 sweep) longer prefixes got worse after day 10; with it they get monotonically better. Held-out seeds 11–30, three source recordings (all cycle-free, guard money_tol 800):

| opponent | H30_yuan (ep 104892947 s1) | H30_atakan (ep 104893687 s1) | **H30_icelemon (ep 104892947 s0)** |
|---|---|---|---|
| tape_yuan800 | −$1.5k (0-20*) | −$5.3k (7-13) | −$1.8k (9-11) |
| tape_strawhats | −$3.9k (4-16) | −$7.7k (3-17) | −$3.0k (6-14) |
| tape_atakan | +$0.1k (7-13) | −$2.0k (1-19) | **+$3.1k (14-6)** |
| tape_shirabe | +$16.0k (20-0) | +$17.6k (20-0) | +$19.4k (20-0) |
| tape_antigone (V16) | +$11.5k (20-0) | +$13.5k (20-0) | +$13.1k (19-1) |
| V3.12 | +$37.6k (20-0) | +$34.8k (19-1) | +$38.9k (20-0) |
| H11 | +$26.4k (20-0) | +$19.1k (20-0) | +$24.5k (20-0) |

*many exact ties (mirror). **Shipped: H30 = H30_icelemon.** Guard fires rarely (late, money-based, on low-demand seeds) and falls back to the C1 policy; 0.5 s/game.

Provenance, stated plainly: H30 is a full 720-step replay of icelemon2004's seat in ladder episode 104892947, with our C1 policy only as the fallback when the live state diverges. It is the same construction as the public "2900+" / V16 / V14-clone notebooks that make up the cluster. It ties the cluster and beats everything else; it is not our farming logic playing.

## Sep 3 — ladder check: H10 vs H11, and H12

Ladder at pull time: H10 61 games, 33-27 real, 1205; H11 49 games, 25-23, 1041. The guard never fired in any of H11's 49 games (all 240 tape steps executed in every replay), so H11 played H10's days 0–9 exactly, minus the wheat round-trip. Per opponent class:

| class | H10 | H11 |
|---|---|---|
| basin B (1c/4s/5 melon) | 18-19, −$2.8k | 5-8, −$0.5k |
| "other" (weak) | 10-5, +$21k | 12-2, +$28k |
| frontier-variant (hour-0 all-in) | 5-2, +$10.7k | 7-11, −$0.9k |
| 53/48 cluster | 0-1, −$121k | 0-2, −$21.6k |

Mostly opponent mix and small samples — except the frontier-variant class, where the cycle-free opening costs a real ~$3k/game (fresh seeds 31–50 vs `tape_kiro`: H10 −$5.5k, H11 −$8.6k). The guard did what it was built for (cluster −$21.6k instead of −$121k).

**H12** (`submissions/H12_H10_PLUS_GUARD.zip`) = H10's opening kept verbatim + the divergence guard (money_tol 800). Seeds 31–50: **+$0 vs H10 (identical play)**, same vs kiro, and vs `tape_strawhats` −$28.7k instead of H10's −$86.4k. Strictly ≥ H10. Recommended over H11.

## P.py — day-planner executor (build log)

Built per `docs/SPEC-day-planner-executor.md` on the `candidates/K.py` chassis (`candidates/P.py`). `economy()`, `_setup_step`, `_fert_eligible`, endgame deposit rule, and the crash guard kept unchanged; `_build_route`/`_route_step`/`_build_sweep`/`_crop_step`/`_crop_pools` replaced with `enumerate_chores()` + `_build_plan()` (nearest-insertion + load-balanced greedy assignment, hard chores scheduled before optional ones, per-route hard/soft nearest-neighbor reordering) + `_plan_step()` (executes a unit's route stop by stop, lazy WHEAT/FERTILIZER pickup only when a stop actually needs an uncarried item). Replans at hours {0,1,6,14,20} or on a new day, capped well under the spec's 4/day. All decision logic is computed from `obs` each call — no recorded action log or tape data anywhere in the file (grepped: no references to any `tape_*`/`Opponents` file, no hardcoded action sequences).

**Test 1 (no-op sanity)** — PASS. `python3 mini_engine.py candidates/P.py candidates/V3_12.py --seeds 1 2 3` runs clean, `errors=[0,0]`, no `GUARD` on stderr.

**Test 2/3 debugging (2 rounds, per the stop rule)**:
- Round 1 bug found via `decompose.py`: animal counts were collapsing mid-game (day 15->29: 11->9->6->5 vs C1's flat 11) -- a starvation bug. `_plan_step`'s lazy pickup marked a `feed`/`fertilize` chore **permanently done** (`chore_done.add`) whenever the unit reached the shed and stock was 0 (e.g. before the hour-1 WHEAT order lands), instead of just skipping it for that pass. Fixed: on empty stock, drop the chore from the current route without marking it done, so the next replan re-enumerates it if the animal is still unfed. Confirmed fix: animal counts stabilized to 13/12/11/11 (seeds 1-3), matching C1.
- Round 2 bug found the same way: STRAWBERRY/MILK output stayed far below C1's (units, not just price) even with matched herd size. Root cause: `_reorder()` did a single nearest-neighbor pass over a route's hard+soft chores together, so a cheap `care` chore (`hard=False` per spec table) frequently landed far down the queue behind many higher-value water/harvest stops, missing same-day care and losing the daily RATE bonus that MILK/WOOL yield accrual depends on. Fixed: reorder hard chores first (nearest-neighbor among themselves), then soft chores after; also promoted `care` to `hard=True` (spec section 4 already flags it as "cheap; bundle with feed" -- this makes that literal instead of advisory). This closed a large chunk of the gap: seeds 1-3 mean margin went from -62.9k -> -46.6k -> -26.2k (both-seats, vs C1) across the two fixes.

**Test 3 (head-to-head, seeds 1-10, both seats) -- FAILS.** After both fixes: `python3 mini_engine.py candidates/P.py candidates/C1.py --seeds 1..10 --both-seats` gives **mean margin -$35,532/game (t=-5.09), 0 wins / 10 losses**, decisively negative (spec requires >= 0). Per-seed range -$23.6k to -$185.5k.

**Stopping here per the task's 2-failed-rounds rule.** Two structural bugs were found and fixed (each a genuine, sizable improvement -- starvation eliminated, care-bundling fixed, gap cut ~58% from -62.9k to -26.2k on the 3-seed decompose sample), but the 10-seed head-to-head is still decisively losing and a third debugging pass would need to characterize a new failure mode from scratch rather than iterate on a known one.

**Hypothesis for what's still wrong** (not yet root-caused): the greedy nearest-insertion assignment in `_build_plan` has no real ETA/deadline check (spec section 6 step 2 calls for `eta_end <= deadline` gating; the shipped version only sorts hard-before-soft and picks min `distance + load*1.5`, with no route-length cap and no rejection when a route is already overloaded) and no 2-opt pass (spec section 6 step 5). This likely means: (a) individual units get overloaded with long chore lists that only *look* balanced by count, not by actual walking time, so late-route stops (including water/harvest, not just care) slip past their effective completion time even though nothing enforces the deadline explicitly; (b) `enumerate_chores`'s plant-tile selection is uncapped by any route-length/capacity awareness, so plant chores can pile onto already-busy units. `decompose.py` on seeds 1-3 still shows STRAWBERRY units 115 vs C1's 165 and MILK 170 vs 227 even with animal counts now matched, consistent with (a): the crop/animal chores exist and get enumerated but aren't finishing before their tiles' next state change (unwatered->weed grace period, or simply losing a day of yield accrual). A next attempt should add real per-route ETA tracking (cumulative distance+action-turns vs `23-hour`) with rejection/reassignment when a route would blow its budget, plus instrumenting per-day hard-chore-completion-rate and per-route stop counts directly (as spec test 2 asks for) rather than inferring from sales decomposition alone.

**Not shipped.** `submissions/P1_DAY_PLANNER.zip` was not created; test 3 must pass before test 4 (scale test) or test 5 (held-out) are meaningful, so those were not run.

Files: `candidates/P.py` (new, ~730 lines, K.py chassis + new dispatcher).
