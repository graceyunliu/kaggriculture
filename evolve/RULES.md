# Constitution for candidate generators

Read before proposing. Everything here was measured on the ladder engine, both seats, paired seeds.

**Build vs. benchmark, don't conflate them.** "Diff against X" (the frontier — **currently `candidates/O9_MELON_LATEFERT.py`** = O8 + the O9 endgame fixes + melon late-fertilization; see below) means X is the architecture new proposals should be built as a minimal patch on top of. "Test against X" (C1, V3_15, the real clone `opp_scenario_v14`, and the opponent tapes) means X is a fixed, non-evolving opponent used to measure a candidate's margin — keep testing against these even after they stop being competitive, because they're what makes results comparable across the whole project history (e.g. O8's +$14,800/game vs C1 is directly comparable to O4's own +$12,668 and V3_15's own +$2,160 against that same fixed opponent). Never replace a benchmark opponent with the current frontier — a moving target only tells you "better than my last self," not progress against a fixed yardstick.

**Measurement mode — `KAGG_FIXED_SHOPS=1` (Sep 10). READ THIS BEFORE JUDGING ANY CANDIDATE ON THE TAPE PANEL.** The engine draws each day's shop unlock from the same per-day RNG that `_spawn_weeds` has already consumed once per empty tile on both farms, so any policy change that alters empty-tile count re-rolls which shop unlocks (the Sep 7 coupling). Shop identity swings a game's money by $25k–$160k, which is why every tape-panel comparison this week at n≤30 came out "null" with ±$15k per-opponent swings that flipped sign between seed sets. `mini_engine.load_engine` now accepts `KAGG_FIXED_SHOPS=1` (patched `_end_of_day` draws the shop from its own seeded stream; cache keys carry `_fs`), and `evolve/batch_vs_o8.py` inherits it. Under it the tape panel resolves to about ±$300 at n=30 instead of ±$1.2k. **Use it for every paired comparison; it is NOT for absolute ladder-truth numbers** (the real ladder has the coupling — but that re-roll is zero-mean noise, so the expected margin gain under coupling equals the fixed-shops estimate). First result: the orchestrator's tape gain was always there — see O16 below. Second tool from the same idea: `tools/delay_counterfactual.py` (fork a real game, force one unit to PASS once, play on, read final money) is now clean too; its first value-at-risk table (O16 vs alaylm, seed 1) ranks a one-hour delay at −$247 for fertilizer COLLECT (fertilizer_available resets daily — a missed collect is a lost unit), −$234 FEED of an already-unfed animal, −$172 daytime DROP, −$151 animal-product HARVEST, −$121 near-weed WATER, −$63 melon HARVEST, and +$237 for delaying an *unnecessary* feed. Previously-"null" candidates (B4_01 melon, X1) should be re-read under this mode before being called null.

## Engine facts (vendor/kaggle_environments_engine_master/kaggriculture.py — the ladder engine)
- 30 days × 24 hours = 720 turns. Money at day 30 decides the game; opponents are fixed replay tapes.
- Two sellers share one market: prices move with inventory, so our sales change the opponent's revenue too.
- Shops are drawn with replacement; town center sells at a flat rate per `townCenterSellInterval`.
- Hands respawn at the shed every morning; hires cost fib(n) for the n-th hire of the day; 10 market orders/turn.
- Animals need daily FEED + CARE; missed days lose production; an unfed animal escapes after 2 days.
- STRAWBERRY/TOMATO are recurring (water daily, harvest repeatedly); WHEAT/CARROT/MELON are one-shot.
- Land: 3 extra quadrants at $1k/$2k/$4k with purchase deadlines by day 14/17/18.
- Crash guard: an exception in `agent()` returns PASS for the turn. A candidate with any agent error is discarded.
- Turn order: unit actions (farmer, then hands) are applied BEFORE market orders, so a DROP and a SELL of the same goods in one turn both land. Last processed action is day 29 h22 (DONE at step 718); there is no day-29 end-of-day auto-drop — cargo still carried after h22 is worth $0. Goods above the 100-item shed cap at any end-of-day auto-drop are discarded. (Sep 9, O5/O12.)
- Market: price = f(inventory − I0) per item, premium below I0, steep decline above (MILK linear −$2.1/unit, STRAWBERRY −$1.92/unit, WOOL/MELON quadratic, FERTILIZER linear −$0.2/unit with NO consumer). Both players' SELL orders in one turn are matched per unit in lockstep, so a unit sold in the same hour as the opponent's batch faces their interleaved units. Shops consume 1 unit per instance every 4 hours (2 for single-product shops), town center 1/day of everything but fertilizer. (Sep 9, O12.)

## What is closed (do not re-propose as a bare knob change)
- More crop coverage of any single crop (tomato scale-up, more strawberry/melon tiles): lost 4 times.
- Geese / EGG as a third species: lost 3 ways (revenue per service-day below cow/sheep).
- Bigger herd via demand_share 0.75–1.0: −$6k to −$17k. Bigger fleet caps alone: no-op or loss.
- More hands via min_hands 5–6 or load_per_hand 12–15: flat to −$3k.
- Wheat-tile floor 5+ and wheat 8/12 tiles: −$3k to −$15k (never gets land; sold early at $35).
- Holding wheat/fertilizer for late prices: negative. Buying fertilizer to apply: −$1k to −$4.5k.
- NEAR_RADIUS above 4 for siting: decisive loss. Radius growing with land: decisive loss.
- Suppressing crops days 0–9 to fund land/animals: −$96k to −$116k.
- Copying the opponent's land/herd/crop timing onto our dispatcher: −$68k. Allocation without execution loses.
- CROP_SWEEP_LEN/RADIUS or ROUTE_LEN nudges on the V3_13/15 dispatcher (Sep 8): every direction tried (sweep chain 6→8, sweep radius 4→6, both combined, route length 3→5, 3→2) lost vs C1, one decisively (route_len=5: −$28.7k/game). These constants are already near their local optimum; re-tuning them without a structural change is wasted effort.
- Fertilizer reserve/buy/pickup on the V3_13/15 dispatcher (Sep 8): porting chassis.py's `fert_keep`/`fert_buy`/opportunistic-shed-pickup mechanism (previously credited with +$5.4k on an older C1 run) regressed on this lineage in all 3 tested configurations — full port −$2,239/game vs itself, reserve+pickup alone −$1,833 (the fetch trip costs more in movement than the doubled yield is worth), shop-buy alone ≈ wash (−$50, not practically meaningful). The old finding doesn't transfer as-is; don't re-port it without isolating why the interaction changed.
- Animal opening split away from 2 COW/2 SHEEP on the C1-ported opening (Sep 8): 3/1, 1/3, 2/3, 3/2 all tested, none beat the 2/2 baseline; 2/3 was catastrophic (−$23.3k/game, likely an affordability/load-model interaction from the extra unit). 2/2 stays the answer here.
- Melon count on the same opening: 10 instead of C1's 8 was worse across every matchup tested (C1, V3_12, clone). 8 stays the answer.

- Adaptive/forecast-driven sale timing on the market ledger (Sep 10): the reconstruction layer is excellent (388,260 checks, zero incorrect bounds, 99.65% exact supply reconstruction, forecasts improved at 12 turns) but using it to defer sales lost -$578/game (t=-3.34). Better price prediction is not better market decisions: any policy that recommends waiting for a better price walks into the mechanism O13 already closed (holding/metering late sales loses $1.8k-$4.7k) and gives up O12's confirmed +$5.6-6.7k edge from selling ahead of the opponent's h0 dump. Do not re-propose forecast-then-hold. The ledger itself is validated infrastructure and should be reused for other questions.
- Compact siting and spatial route batching as tested (Sep 10): clean factorial found compact siting has little physical effect, spatial routing saved <1% of travel, and the combination produced no promotable economic evidence. Note the correct conclusion: this does NOT establish that walking more is why O15 loses, only that the interventions tested were too weak or too confounded to explain the gap. Do not rebuild the policy around permanent herders or route batching until a stronger intervention shows the travel bottleneck is dominant.

## What worked
- C1 opening: day 0 = 5 HIRE, 2 COW, 2 SHEEP, 8 MELON seed, 7 WHEAT seed, 5 WHEAT feed; hires paid before the feed reserve on days 0–5; no spare feed buffer when poor. +$4.8k held-out vs V3.12.
- Movement-aware crop siting (recurring crops near shed, one-shot far): the biggest single win in the v10 lineage.
- Demand-coupled herd/crop sizing (V3.9): +$50k over its predecessor.
- fert_buy 1 on C1: +$5.4k held-out (first evolution-run finding, Sep 3).
- **V3_13_WEED_AND_FEED (Sep 8), on top of V3_12** — two execution-layer fixes, both directly targeting the labor-per-obligation gap below: (1) moved the "weeds" sweep tier ahead of harvest/water — a weeded tile is a 100% capacity loss until dug, worse than an unwatered crop, and the old order checked it dead last; (2) alternate-day feed/care via `consecutive_unfed == 0` — base animal production isn't gated by feeding at all (only the care bonus is, and it still accrues on a skipped day), so feeding every animal every day was pure wasted movement; skip is safe against the 2-consecutive-day escape rule. Held-out (20 seeds) vs the real clone opponent: **+$13,467/game, t=8.49, 20-0**. Consistently better or equal against every other opponent spot-checked (frontier, soil, andrey); ~even against tape_antigone (both lose there already). Confirms the RULES.md execution-gap diagnosis was directionally right and gives a first concrete win from it — see `candidates/V3_13_WEED_AND_FEED.py` header for full numbers.
- **V3_15 (Sep 8)** — V3_13's fixes + C1's frontier opening (5 HIRE/2 COW/2 SHEEP/8 MELON/7 WHEAT/5 feed, all at hour 0 day 0) + C1's labor-first early-hire ordering (days ≤5: hire before feed). Closes the V3_13-vs-C1 gap from a decisive −$8.8k/game loss to a genuine statistical tie (30-seed combined dev+held-out: +$512/game, 15-15 wins) while still beating V3_12 (+$7.4k dev) and the real clone decisively (+$18.4k held-out, t=9.41, 19-1). Best own-code candidate as of Sep 8; see `candidates/V3_15.py`.
- **O4 (Sep 9, separate task) — CONFIRMED NEW BEST OWN-CODE CANDIDATE, cross-tested Sep 9.** A from-scratch reactive policy (no copied turn schedule) built on top of O2, adding: (1) shared-resource reservation within a turn for fertilizer/wheat pickups, not just animals — O2 let concurrent workers race for the same fertilizer and lose 19 pickups to no effect in one instrumented game; (2) care scheduling that accounts for an animal's stored care bonus, first-yield day, production interval, and feed history — care given on a production day pays off on the *next* harvest, not that day's (an off-by-one here was caught and fixed in lifecycle tests before shipping); (3) intra-day cash release/reinvestment — sell what route-completing workers deposit during the day rather than only at fixed hours, and allow bounded extra capital decisions after an observed cash bump. Original report (frozen seeds 5001–5050, both seats, 100 games/matchup): +$15,299/game vs C1 (50-0), −$28,900/game vs H32 (1-49), −$14,167/game vs a real Mengfei replay (9-41).
  Independently cross-tested against V3_15 (this file's prior best) on this repo's cascade harness: **O4 beats V3_15 decisively too** — dev (10 seeds) +$13,938/game (t=5.55, 9-1), held-out (20 seeds) **+$15,065/game (t=14.42, 20-0)**; re-confirms the C1 win on this repo's own C1.py (held-out +$13,164/game, t=14.41, 20-0); and vs the real clone (opp_scenario_v14), held-out **+$32,084/game (t=10.24, 20-0)** — roughly double V3_15's own +$18.4k edge over the same opponent. All t-values here are far past the usual ≥2 promotion bar; this is not a marginal result.
  Still loses badly to the tape-hybrid line (H32/M2/M4), same pattern as every other own-code candidate in this file — a real win against a reactive/own-code baseline does not transfer to beating a replay-wrapped tape. Zero agent errors across every test. Submission zip at `submissions/O4_PRODUCTIVE_SERVICE.zip`; candidate at `candidates/O4_PRODUCTIVE_SERVICE.py`; detail in `docs/O4-original-candidate-sep09.md`. **This supersedes V3_15 as the frontier for future own-code proposals — diff against O4, not V3_15 or C1, going forward.**

- **O8_PURE_ANIMAL_THROTTLE (Sep 9, same day) — CONFIRMED NEW BEST OWN-CODE CANDIDATE, supersedes O4.** Found by applying the confirmed Pillar-1 "coordination" lens (from the O4 architecture audit above) to a part of the dispatcher never previously tested: `S["animal_claim"]`, the throttle limiting how many hands may simultaneously pursue animal pickup-and-placement, was hardcoded at `< 2` (movement-commit gate) / `< 1` (further-movement gate) since O2's original design — an arbitrary cap unrelated to how large the actual shed backlog of unplaced animals is. Raised to `< 4` / `< 2`. This is a one-concept, two-line diff against O4 (see `candidates/O8_PURE_ANIMAL_THROTTLE.py`, diff is exactly the two threshold numbers, nothing else touched).
  Behaviorally verified before trusting the margin (seed 1 vs C1): `max_animals` rises 9→11, `sales` rises $97,427→$129,639, unit_turns/idle_share roughly unchanged (6,127→6,273 / 0.123→0.116) — i.e. the extra output comes from actually placing more animals, not from working harder or idling less; a genuine capacity unlock, not noise.
  Paired same-seed margin vs O4 (`evolve/o5_ablation.py o8pure`): **dev +$1,060/game (t=1.07, 7-3, not independently significant) — held-out +$1,905/game (t=3.33, 17-3), past the ≥2 bar.** This is exactly the small-dev/clear-held-out pattern the standing rule warns about — trust the held-out number. Also decisively ahead of the earlier baselines directly: vs C1 dev +$14,800/game (t=9.39, 10-0), vs V3_15 dev +$14,787/game (t=10.77, 10-0), vs the real clone dev +$24,879/game (t=7.38, 10-0) and held-out +$30,385/game (t=12.52, 20-0) — all comparable to or ahead of O4's own numbers against the same opponents.
  **Search process, for the record (per the explicit instruction not to re-climb already-tested hills):** three other architecture-grounded ideas were generated from the same three-pillar framework, each built as a minimal patch, behaviorally verified as genuinely firing, and margin-tested against O4 before being set aside as null: (1) same-turn drop→sell top-up (`O5_SAMETURN_SELL.py` — closes the residual 1-hour DROP-then-SELL lag the C×D causal-chain audit left unverified; confirmed firing but economically negligible, dev +$23/game t=0.07, held -$169/game t=-1.44 — the drop events are too infrequent, ~4-7/game, for the timing shift to matter); (2) activating the dormant `melon_rush` knob (inherited from the pre-O2 chassis, targets the documented day-10 melon price-timing gap; confirmed firing, 3x more mid-route drops in days 10-14, but dev -$1,106/game t=-1.13, held -$320/game t=-0.37 — moving melons to shed faster didn't matter because the standard sell path already captures them adequately); (3) making the wheat SELL-side reserve use B's lifecycle-aware `due_feed` instead of the stale `n_total` (the SELL reserve was inconsistent with the BUY-side fix B already made; confirmed firing, +35% more wheat sold on a spot-check seed, but dev +$8/game t=0.02, held +$76/game t=0.33 — wheat's low unit price means even a real quantity change barely moves total money). **Takeaway: not every mechanism the three-pillar lens suggests is economically load-bearing — verify AND margin-test before promoting, exactly as this file's own methodology already insists.**
  Submission zip at `submissions/O8_PURE_ANIMAL_THROTTLE.zip`; candidate at `candidates/O8_PURE_ANIMAL_THROTTLE.py`. **This supersedes O4 as the frontier for future own-code proposals — diff against O8, not O4, going forward.**
  **Real-ladder check (Sep 9, sub 56117587, score 870.9, 39 games including 1 self-mirror):** real record is **18-20 (≈47%) across 38 non-mirror games** — far below the near-clean-sweep margins local sim showed vs C1/V3_15/clone. Zero agent errors across every game (engine port is solid; this is a genuine performance gap, not a crash). Breaking the 38 games down by opponent fingerprint: **≈21 of 38 (55%) share one near-identical opening fingerprint** (`HIR×5, BUY_ANIMAL 2/2, BUY_WHEAT 7, BUY_MELON 12`, order-swapped variants) matching the previously-documented shared-clone cluster (`kaggriculture-opponent-detection-identifiers`, 93.2% of replay instances) — against exactly this fingerprint O4 goes **9-10**, a coin flip. This matches the standing "mirror regime" finding: near-identical openings turn the game into a seed lottery, not a skill contest, so O4's local edge over C1/V3_15 (neither of which resembles this fingerprint closely) doesn't transfer here. The remaining ~17 non-fingerprint games are **7-7**, also roughly even, including one confirmed real replay-tape opponent (`jasonstillchasin`, flagged TAPE53 by the harness) which O4 lost, consistent with the standing tape-hybrid weakness. **Conclusion: O4's decisive local-sim wins over C1/V3_15/clone are real but don't predict ladder win rate, because the real opponent pool is dominated by a near-mirror clone cluster (seed-decided) and by tape-style opponents (a known, separate weakness) — neither resembles the C1/V3_15 profile O4 was benchmarked against.** This doesn't retract the local findings; it recontextualizes what "beats C1 decisively" is worth on the real ladder specifically.

- **O4's ~$3.1k "bundle" gain (O2→O3, minus shared-stock) is NOT one mechanism and NOT simply additive — it is dominated by one solo effect plus a real two-way interaction (Sep 9 factorial ablation, `evolve/factorial_ablation.py` + `factorial_heldout_check.py`, paired same-seed DEV_SEEDS 1-10 and HELD_SEEDS 11-30, all three sub-mechanisms behaviorally verified before trusting any margin — see below).**
  The bundle decomposes into three sub-mechanisms, each built as a minimal patch against O2: **B = lifecycle-aware care/feed timing** (skip a feed/care visit when the production calendar and stored bonus say it isn't due yet), **C = intraday capital-event timing** (sell every hour instead of only at hour 0/day 28+, and allow off-schedule BUY/HIRE after an observed same-day cash jump), **D = mid-route product release** (drop carried product at a nearby shed mid-route instead of waiting to finish the route).
  Solo effects vs O2 (dev/held-out): **B alone +$2,457/game (t=2.38, 8-2) / +$2,457 (t=2.19, 12-8) — real and the only mechanism that stands on its own.** C alone +$124 (t=0.76, 3-2) / +$183 (t=0.92, 7-5) — negligible alone. D alone **−$2,043 (t=-1.21, 4-6) / −$1,291 (t=-1.25, 9-11) — a wash-to-mild-loss alone**, releasing product mid-route without also selling it faster just moves inventory around.
  Naive sum of solo effects: 2,457 + 124 − 2,043 ≈ **$538/game**. Actual measured bundle (BCD vs O2): **+$3,101 (t=3.50, 8-2) dev, +$3,392 (t=4.42, 17-3) held-out** — the combined bundle materially outperforms what the standalone effects alone would predict. (Don't over-read the ratio between these two numbers as a stable quantity — one input to it, D's solo effect, is itself a weak/noisy negative, so "naive sum vs actual" is a useful descriptive signal that an interaction exists, not a mechanistic multiplier to reuse elsewhere.) The gap is a genuine, directly-confirmed C×D interaction: **CD vs D alone = +$2,864 to +$3,304/game (t=2.97-3.23, both seed sets, 9-1 / 15-5)** and **CD vs C alone = +$1,048 to +$2,160 (t=0.80-1.87, weaker but same direction on held-out)**. Mechanism hypothesis: mid-route release creates intraday-sellable inventory; intraday selling is what converts that availability into usable capital — neither half realizes the full benefit alone. B (lifecycle) sits mostly outside this interaction — its marginal add on top of C+D (BCD vs CD) is +$3,018/game (t=1.77, dev only, not independently re-confirmed held-out), consistent with its solo effect, i.e. lifecycle looks close to additive on top of the C×D pair.
  Verification method note: the first attempt at verifying C used an instrumentation proxy that only counted off-hour BUY/HIRE actions and saw zero difference from O2 on 9 of 10 seeds — an apparent silent no-op, essentially a miniature repeat of the earlier proposal/render-pipeline bug (`kaggriculture-evolve-pipeline-bugs-sep07`). The proxy was missing the mechanism's actual dominant effect (SELL orders firing every hour instead of only hour 0); once SELL was added to the tally, O2_capital showed 9-13 off-schedule sells/game on every seed tested versus 0 for O2 baseline. **Lesson for future verification: confirm the instrumentation covers every order type the patch touches, not just the ones assumed most likely to move — a "no difference found" result can be a broken probe, not a broken mechanism.**

  **Frozen mechanism structure (do not split C and D apart in future proposals — treat as a coupled pair):**
  ```
  O4 bundle decomposition
  B — lifecycle-aware care/feed
      Status: independently beneficial
      Evidence: dev + held-out (+$2,457/game both, t=2.38 / t=2.19)
  C — intraday capital timing
      Status: insufficient/weak alone (+$124 to +$183, not significant)
  D — mid-route product release
      Status: insufficient/negative alone (-$1,291 to -$2,043, not significant)
  C × D
      Status: strongly supported positive interaction (+$1,048 to +$3,304 over either solo, t up to 3.23)
      Mechanism hypothesis: release creates intraday sellable inventory;
      intraday selling converts that availability into usable capital.
  B + (C × D)
      Status: explains the bundle substantially better than an additive three-mechanism model.
  ```
  Practical takeaway for future proposals: don't credit "the bundle" as a black box, and don't assume future timing-mechanism combinations are additive — test the pair directly. Lifecycle-aware feed/care timing is independently valuable and portable on its own. A component that looks harmful or neutral in isolation (C or D alone) can still be essential to a validated interaction — don't reject C or D individually from a future proposal without checking what it's paired with.

- **Follow-up (Sep 9, same day): B is additive with the C×D pair — no B×(C×D) interaction found.** Direct per-seed paired test (`evolve/bcd_interaction.py`: interaction = margin(BCD vs O2) − margin(B vs O2) − margin(CD vs O2), computed seed-by-seed from the SAME per-seed simulation runs, not from subtracted means) gives mean interaction −$1,772/game (t=−0.87, n=10 dev) and −$200/game (t=−0.11, n=20 held-out) — both indistinguishable from zero. So the mechanism map is: **B is a standalone additive contributor; C and D form a separate, tightly coupled interacting pair; the two subsystems don't interact with each other.** This is a clean two-level structure (one additive term + one interaction term), not a three-way tangle — future proposals can treat "lifecycle timing" and "capital+release timing" as independently addable levers.

- **Follow-up (Sep 9): causal chain for the C×D interaction — the D→C link is directly demonstrated, the C→cash→reinvestment link is not (proxy was confounded).** Instrumented single-game traces (`evolve/cd_causal_chain.py`, seed 1 vs C1) logging, per day, the hour of D's first mid-route DROP and the hour of the first SELL after it: in **D-alone, `sell_after_drop` is `None` on every single day** — the released product sits until the next scheduled sell window (hour 0/day 28+), confirming D alone creates availability it cannot itself act on. In **CD combined, a SELL reliably follows the DROP 1 hour later on every day a drop occurs** — directly demonstrating the proposed mechanism (D creates intraday-sellable inventory; C's expanded sell window is what converts it to cash same-day). The second half of the proposed chain (cash arrives earlier → reinvestment happens earlier) was NOT cleanly demonstrated: the "cash bump" instrumentation (cash ≥ day's opening + $500) fired at hour 1 in nearly every day for every variant including plain O2 baseline, i.e. it was picking up routine daily cash flow already present without the mechanism, not a bump specifically attributable to the earlier sale. **This proxy needs to be rebuilt (e.g. attribute the specific SELL's revenue and check whether a BUY/HIRE follows within N hours that wouldn't otherwise fit that day's cash trajectory) before the "earlier reinvestment" half of the causal story can be claimed as demonstrated** — right now only "D creates supply, C monetizes it same-day" is proven; "and that unlocks earlier reinvestment" remains a plausible but unverified extension.

- **Follow-up (Sep 9): B's mechanism looks like waste-avoidance, not clean reallocation-to-more-output (single-seed, illustrative — not independently margin-tested per sub-channel).** Comparing `evolve/trace.py` output for O2 vs O2_lifecycle (seed 1 vs C1): unit-turns spent drops 6,688→5,938 (−750) and chores_enumerated/completed both drop ~19% (1,588→1,288 / 1,449→1,162), consistent with genuinely skipping unnecessary feed/care visits (skipped_feed_not_due 1→13). Production is preserved or improved despite fewer visits — escapes actually drop 1→0, final networth is flat-to-slightly-up (70,155→70,808) — so nothing is being sacrificed for the savings. But `idle_share` barely moves (0.109→0.121, if anything slightly up) rather than dropping, so the freed-up worker-turns are not visibly being redirected into extra harvesting/watering/other revenue-generating work in this trace — the win reads as **fewer wasted actions**, not **the same actions completed faster so more get done**. (Caveat: this is one seed, one opponent, read qualitatively — it is not a claim that this pattern holds on average; the aggregate margin evidence for B's value stands on its own from the factorial ablation above regardless of which of these channels explains it.)

- **Experiment 4 (Sep 9): mechanism portability panel — B and CD are broadly portable, but the C×D edge is opponent-dependent, not universal.** `evolve/robustness_panel.py` (DEV_SEEDS, 4 opponents) + `evolve/robustness_panel_heldout.py` (HELD_SEEDS confirmation) ran O2/B/CD/BCD/O4 each against the SAME fixed opponent on the same seeds, then took the paired same-seed delta (candidate's own money − O2's own money vs that opponent) — this measures whether each mechanism's edge holds when the opponent's architecture changes, not just whether O4 wins overall.
  Held-out results (n=20, mean $/game, t in parens):
  ```
  Environment   B-O2              CD-O2             BCD-O2            O4-O2
  Clone         +15,142 (t=3.21)  +9,450 (t=2.40)   +7,879 (t=1.63)   +12,420 (t=3.04)
  TapePeter     +10,901 (t=2.35)  +6,399 (t=1.47)   +10,172 (t=2.50)  +4,465  (t=1.09)
  C1            +2,214  (t=0.94)  -4,565 (t=-1.08)  +2,513 (t=0.47)   -5,012  (t=-1.40)
  V3_15         +5,596  (t=1.06)  +5,572 (t=1.19)   +3,606 (t=0.64)   +3,531  (t=0.65)
  ```
  Against the real clone and a real ladder-loss tape (TapePeter), every variant's edge over O2 is positive, and for B and O4 vs Clone it's decisive (t>3) — this is the portable case: the mechanisms generalize to genuinely different, non-C1-family opponent architectures. Against C1 specifically, B stays positive but weak (t=0.94), while CD and O4 both turn mildly negative (t=-1.08, -1.40) — not statistically decisive at n=20, but a consistent directional flip worth flagging: whatever C1's play style does (it doesn't create the same intraday product-release/sell opportunities, or its cash cycle doesn't reward faster selling as much), the timing/release pair's edge specifically doesn't transfer there, even though O4 and O2 both still crush C1 in their own separate head-to-head margins (established earlier: O4 vs C1 held-out +$13,164/game, t=14.41). **These are different questions — "does O4 beat C1" (yes, decisively) vs "does the O2→O4 upgrade specifically help against C1" (unclear, maybe mildly negative) — don't conflate them.** V3_15 shows no environment-specific flip but also nothing decisive either way (all t<1.2) — inconclusive rather than negative.
  A dev-seed-only pass (n=10) on the same panel had shown an apparent sharp O4-vs-TapePeter reversal (-$10,546); held-out seeds (n=20) contradict this (+$4,465) — this is itself a re-confirmation of the standing rule not to trust small independently-varying samples for these margins.
  RNG-path check: single-game traces of O2 vs O4 (both vs Clone, seed 1) show weeds_new 2 vs 5 — occupancy/board-state did shift between the two policies on the same seed, consistent with the Sep 7 partial-coupling finding that a policy's own action pattern can change the weed-spawn draw count and downstream shop-unlock RNG path. This is a single-seed spot check, not a stratified measurement — treat it as confirmation that the coupling channel is live here too, not as a quantified correction to any margin above.
  **Practical takeaway: promote B and the C×D pair as generally portable architecture, but don't assume the C×D edge specifically transfers to every opponent — check any new target opponent's play style (does it create/benefit from mid-day product flow?) before expecting the same gain there, and prefer held-out-seed confirmation over any single dev-seed panel result before trusting a direction change.**

- **Third pillar identified and quantified (Sep 9): O2's own worker-coordination fix (site-claim) is independently valuable, same rigor as B and C×D.** O2's name comes from its own state-ownership/coordination layer over whatever preceded it: `S["claimed_sites"]`/`S["pending_sites"]` stop two of our own units from targeting the same empty tile for animal-pasture siting or crop planting within a single turn (`_pick_site`, `_setup_step`, `_crop_pools`, `_task_valid` in `candidates/O2_STATE_OWNERSHIP.py`). Built a minimal reversion patch, `candidates/O2_no_siteclaim.py` (strips the claim filters, leaves the bookkeeping as an inert no-op), and tested it the same way as B/C/D: paired same-seed margin vs O2, plus direct behavioral verification rather than trusting the margin alone.
  Margin (`evolve/siteclaim_ablation.py`): removing site-claim costs **-$2,956/game dev (t=-2.30, 2-8)** and **-$3,310/game held-out (t=-2.11, 6-14)** — both past the ≥2 significance bar, so O2's own coordination fix carries real, independent value, same class of finding as B. A single-seed anecdote (`evolve/trace.py`, seed 1 vs C1) initially pointed the *opposite* direction (O2_no_siteclaim scored higher, 92,230 vs 67,292) — yet another confirmation that a single seed cannot be trusted for these margins, exactly the standing rule from the O3-vs-O4 anomaly earlier.
  Behavioral verification (`tools/verify_siteclaim.py`, monkey-patches `_pick_site` to log every (day, hour, site) it returns): O2 baseline shows **zero** turns where two calls return the same site (0 duplicates across 9 calls, seed 1 vs C1); O2_no_siteclaim shows **1 duplicate-target turn out of 12 calls** on the same seed/opponent — direct, if small-sample, confirmation that removing the filter causes exactly the collision it was built to prevent. (This instrumentation only covers the animal-siting path through `_pick_site`; the separate crop-planting collision path through `_crop_pools`/`_task_valid` was not independently instrumented — treat the behavioral confirmation as covering one of the two channels the patch touches, not both.)
  This sits alongside, but is distinct from, mechanism A (shared-stock/pickup accounting, O2→O3, +$999/game dev t=3.14, already documented above) — both are "coordination" fixes in the sense the user's synthesis describes (a worker's decision made aware of what other workers have already claimed), but they operate on different resource layers: site-claim governs *where* a unit places something (spatial contention), shared-stock governs *how much* of a consumable remains (accounting contention). **Revised three-pillar architecture map for the O2→O4 lineage:**
  ```
  Pillar 1 — WORKER COORDINATION (avoid duplicate/stale local decisions)
    site-claim (O2 itself):      +$2,956 to +$3,310/game, confirmed causally
    shared-stock (O2->O3, mech A): +$999/game dev (t=3.14), confirmed causally
  Pillar 2 — OPERATIONAL EFFICIENCY (B, lifecycle-aware care/feed)
    +$2,457/game dev+held, additive with Pillar 3, waste-avoidance not reallocation
  Pillar 3 — TEMPORAL CONVERSION (C x D, intraday sell + mid-route release)
    interaction-driven, +$2,864-3,304/game over either half alone
  ```
  Pillars 2 and 3 are confirmed additive with each other (B×CD interaction ≈ 0, see above).

- **Follow-up (Sep 9): Coordination × B / Coordination × CD tested — CD is additive with coordination, B shows a suggestive but not fully confirmed positive interaction.** `evolve/coordination_interaction.py` built the missing no-siteclaim variants of B, CD, and BCD (same strip-patch as `O2_no_siteclaim.py`, applied to `O2_lifecycle.py`/`O2_capital_release.py`/`O2_plus_bundle.py` — all three contain the siting block unmodified, confirmed before patching) and measured, per seed, coordination's own effect (with-coordination minus without) inside each context, then took interaction = coord_effect(X) − coord_effect(O2):
  ```
              coord effect within context (mean $/game, t)          Coord x X interaction (t)
              DEV (n=10)         HELD (n=20)                        DEV        HELD
  O2 alone    +2,956  (t=2.30)   +3,310  (t=2.11)                     —          —
  B           +5,790  (t=7.72)   +7,532  (t=5.19)                  +2,835 (1.89) +4,223 (1.55)
  CD          +1,240  (t=1.39)   +2,329  (t=2.33)                  -1,716 (-1.16) -981 (-0.50)
  BCD         +4,244  (t=3.32)   +5,059  (t=2.97)                  +1,289 (0.73) +1,750 (0.59)
  ```
  **Coordination × CD looks genuinely additive** — the interaction term is small and flips sign between dev and held-out (both not remotely significant), consistent with noise around zero, matching the B×CD result.
  **Coordination × B: CONFIRMED as a real positive interaction (Sep 9 follow-up, resolved).** The dev-only and held-only reads were each suggestive but individually below the t≥2 bar (t=1.89, t=1.55). Rather than reconstruct a pooled statistic from those two summary results (which would have manufactured false precision), re-ran the same two contrasts as single direct `cascade._eval` calls over the full pooled seed set (seeds 1-30 together, not two separate calls combined after the fact), then computed the interaction from the true per-seed pairing: coordination's own effect is **+$3,192/game within plain O2 (t=2.85, n=30)** vs **+$6,952/game within the B context (t=6.94, n=30)** — and the interaction term itself, per-seed paired, is **+$3,760/game (t=2.01, n=30)**, clearing the project's own significance bar. **So B doesn't just add to coordination's value, it roughly doubles it** — when animals aren't being over-serviced (B active), correctly avoiding site collisions apparently matters more, plausibly because B's freed-up worker-turns increase how often multiple units would otherwise have converged on the same siting decision in a given turn (more animal-placement attempts per unit time without B's throttling → more opportunities for the coordination fix to matter). This is the one confirmed non-additive edge in the mechanism graph.
  Practical takeaway: **Model A (independent, additive pillars) holds for Coordination×CD and for B×CD, but NOT for Coordination×B — that pair should be treated and proposed together going forward** (the same rule already established for C and D: don't split a confirmed interacting pair apart in future proposals). Revised summary: three pillars, four of five tested pairwise relationships additive, one real synergy (Coordination×B) — a mostly-modular architecture with a single confirmed exception, not a purely additive one.

## Sep 9 (late) — 45-candidate search on top of O8, with replay mining against the real ladder tapes

**Ground truth first (this changes what "beating the frontier" means):** on the 4 real ladder-loss tapes (`tape_peterparker/alaylm/bahaenes/yangkuang2`, all the same shared-clone family), O8 loses **2-28 to 5-25 per tape, −$19k to −$30k/game** (`evolve/o8_vs_tapes.py`, n=30). It beats `opp_scenario_v14` (the "clone") 30-0 by +$28.5k — **the clone is not a proxy for the current ladder; use the 4 tapes.** Absolute money against the *same deterministic tape* ranges $25k–$160k across seeds — the shop-unlock lottery (which shops unlock decides strawberry/milk demand; no shop consumes MELON or FERTILIZER at all) dominates outcomes, and because a policy change perturbs board occupancy → weed-draw count → shop-draw RNG path, **per-opponent deltas at n=10 swing ±$15k and flip sign between seed sets** (e.g. B4_01 vs yangk: −$15.1k on seeds 1-10, +$4.6k on 11-30). Only the 5-opponent average over ≥30 seeds means anything. Harness: `evolve/batch_vs_o8.py` (paired margin vs O8 + own-money delta vs O8 across the tape panel, same seeds; O8 panel cached in `evolve/_o8_panel_cache.json`). Mining tools: `tools/replay_mine.py` (per-day sells/prices/state for both players), `tools/gap_profile.py` (seed-averaged per-day gap + per-item revenue), `tools/action_mix.py` (action-type counts both players), `tools/fert_flow.py`.

**The one candidate that clears the paired-vs-frontier bar: `candidates/B4_01_MELON_LATEFERT.py`.** Fertilizer eligibility extended to MELON only, late in its watering window (age 7-8), so the remaining window waterings count double and the tile reaches 6 units by age 9; plus an `age >= first` gate on one-shot harvest (engine: HARVEST before first_yield_day is a silent no-op — without the gate the fertilized tiles would be visited uselessly for two days). Paired vs O8, three independent seed sets: **dev +$4,224 (t=3.12, 9-1); held-out +$2,327 (t=2.57, 13-7); fresh 31-50 +$2,443 (t=2.90, 16-4)** — ~+$2.8k/game over n=50. **But on the tape panel it is null-to-slightly-negative (≈−$1.1k/game averaged over n=50, not significant).** The self-play gain comes from selling more melons in the day-11 h0 interleaved dump than O8 does; against tapes that dump 60 melons at day 10 h8-9 it buys nothing. It meets the same promotion evidence O8 was promoted on, so it's packaged (`submissions/B4_01_MELON_LATEFERT.zip`) — but do not expect a ladder gain from it; it is an O-family-vs-O-family improvement.

**Ported onto O9 (the endgame-fix frontier from the other Sep 9 session): `candidates/O9_MELON_LATEFERT.py` = O9 + the B4_01 melon late-fert patch.** B4_01 alone also beats O9 head-to-head (+$3,945 dev, t=2.99, 9-1). O10 vs O9, paired, three seed sets: **dev +$4,086 (t=3.09, 9-1); held-out +$2,313 (t=2.51, 13-7); fresh 31-50 +$2,316 (t=2.79, 14-6)** — the melon gain is additive with O9's endgame gain. Zip: `submissions/O9_MELON_LATEFERT.zip`. Same caveat as B4_01: this is an O-family-vs-O-family gain; expect no change on the tape panel.

**Melon economics, measured (closes the "melon timing" line in the gap list below):** the tapes dump 60 at day 10 h8-9 at $272; the post-dump price is ~$213 (sq curve, 60 units), not the $166 assumed earlier — O8 already sells 12@$272 (day 10 h5) + 36@$213 + 12@$133. The whole first-mover prize is ~$2-3k/game, and our own 84-unit dump depresses our price more than theirs does. Fertilizing melons in the early window (age 5-7, `B2_01/B2_02`) is catastrophic (−$10k panel): it steals labor on days 5-7 when hands are 4-7 and cascades into a smaller herd. Fertilized one-shot tiles hit max yield, leave the watering pool, and become weeds if not harvested within 2 days — any early-harvest scheme must keep visiting them. Harvest-at-4/5 units on day 10 (`B3_*`) gains first-mover on ~24 units but loses 2 units/tile: null. `melon_rush` knob: null/negative. Fertilizing WHEAT/CARROT with $100 fertilizer: −$3.7k (my own bug in `B1_01`, don't repeat).

**Closed again, this time on the panel too (the closed list above was right; replay mining re-derived and re-refuted each):**
- Herd not capped by milk/yarn shop presence, or a frontier-style herd schedule floor (14/17 by day ~13): self-play −$4k to −$17k, **panel −$8k to −$14k (t≈−2.4 to −3.5)** — even though every placed animal yields 1 fertilizer/day unconditionally (engine) and the tapes run 17 regardless of demand. Our dispatcher can't service them; the tape's can.
- Wheat floors / wheat-per-animal 0.5–1.5 / cap 40: self-play −$2.8k to −$12.5k, **panel −$7k to −$22k**. One seed (24 vs alaylm) showed +$8k — an exception, not a signal. Late-game wheat filler (cutoff 26-27, day-29 hands 12, min_val bypass): no-op — the labor model (`_load_model >= MAX_HANDS`) zeroes late seed orders; forcing it through doesn't pay either.
- Fewer hands (MAX_HANDS 12/11/10): −$0.7k to −$2.9k self-play, −$1.9k panel — the 13th/14th hands cost $144+$233/day in fib re-hire (hands are cleared nightly) and *still* earn it under this dispatcher. Marginal-value hiring estimator: −$39k (broken calibration; direction refuted by the cap tests anyway).
- Weeds-first sweep tier (V3_13's win, ported): −$645 (t=−2.10) on the O lineage — weeds are rare here (2-6/game) and the reorder just delays watering.
- Same-turn DROP→SELL top-up (`O5`): null (drops are ~4-7/game). Wheat sell-reserve using `due_feed`: null (wheat is cheap). Feed-cost-aware skip (don't feed when product price < 1.2× wheat): +$1.0k self-play (t=0.75), panel +$0.1k — null. Fertilizer retention (`fert_keep 6`) null; with `fert_carry 4` −$2.3k. Angular-sector zone dispatch (each hand owns a wedge around the shed): travel/task 1.26→1.51, worse — thin wedges force center-to-tip walks.

**Four follow-up probes from the melon method (Sep 9, `tools/four_probes.py`, O9_MELON_LATEFERT vs alaylm, 6 seeds), all closed:** (1) Fertilizer timing — both sides average $45/unit; ours goes out as a 213-unit h0 batch (overnight auto-drop), the tape's as h0-h1 batches; no per-product lever beyond the generic evening-deposit fix. (2) Wool — we already realize $170/unit vs the tape's $108 (154 units at h0 @ $173); nothing to fix. (3) Rot — 10 one-shot yield units/game lost to decay and 3.8 tiles rot into weeds; a "harvest rotting tiles first" tier (`B11_01`) cuts that to 4 units / 1.3 tiles but is money-neutral-to-negative (−$44, t=−0.08 paired; slightly worse on the 6-seed tape sample) because it pulls harvests ahead of urgent watering. Sized correctly at ~$400/game before building — not worth the priority cost. (4) Early idle — hands are idle 78%/37%/49%/35%/38%/31% on days 1-6 (4-7 units), but it's a cash constraint, not a labor one: the only free work is BUILD_PASTURE, and pre-building pastures for incoming animals (`B11_02/03`) fires ~30 times/game and is a wash (+$310, t=0.18). Fib re-hire savings from fewer early hands are ~$5-20/day. **Lesson: the melon method (engine rule → real-opponent replay → curve arithmetic → sized patch) works, but it also correctly predicts when a lever is too small to matter — size the prize before building.**

**What the gap actually is, quantified head-to-head on the same seed/game (`tools/action_mix.py`, seed 24 vs alaylm, equal 17-animal herds, we lose by $55k):** the tape makes **900 fewer moves and 430 fewer PASS turns** yet does more of every productive action (harvest 474 vs 414, care 387 vs 268, feed 367 vs 299, plant 236 vs 184, pickup 201 vs 155) with **3-4 fewer hands** (10-11 vs 13-14). Per hand-day: tape ~15 work actions at 0.6-0.8 moves each; O8 ~11 at 1.1-1.5. Our excess idle is concentrated on days 1-8 (~250 PASS turns — the tape keeps 19-36 plants then, we sit at 14-18) and our hands criss-cross the board. This is the same execution diagnosis as Sep 3, now measured against the actual ladder opponent rather than C1: **every allocation lever tried in this search lost because the dispatcher can't service it, and the ~$25k/game ladder gap is dispatch efficiency (moves per work action), not what to buy.** The next real candidate has to come from the `sweep`/`dispatch` design, and it must be judged on the 4-tape panel at n≥30, not on self-play vs O8.

## Sep 9 (night) — O12_EVENING_DEPOSIT: sell before the opponent's morning batch. CONFIRMED on the tape panel. New frontier; diff against O12.

**Found by auditing engine effects, not by proposing a strategy** (`evolve/action_audit.py`: wraps `_apply_unit_action`, counts no-op actions, PASS turns by hour, end-of-day shed overflow, DROP hours). O9 has zero no-op actions, but 12-14% of unit-turns are PASS and **74% of that idle is in hours 19-23** — the crew stands around while the day's harvest rides in their pockets until the end-of-day auto-drop, then gets sold at h0 in per-unit lockstep with the opponent's h0 dump. The market is a shared reservoir with steep price curves above I0 (MILK −$2.1/unit, STRAWBERRY −$1.92/unit, WOOL/MELON quadratic), so every unit sold in that collision faces the opponent's interleaved units. (Overflow past the 100-item shed cap is also discarded at the auto-drop: ~5 units/game, 64 on one bad day — real but minor.)

**The fix (on O9, `candidates/O12_EVENING_DEPOSIT.py`, zip `submissions/O12_EVENING_DEPOSIT.zip`):** (a) from h18 an IDLE unit carrying product walks to the shed and DROPs; (b) from h20 EVERY unit carrying ≥3 product heads home and DROPs (animal routes excepted); (c) same-turn SELL of those drops (`same_turn_sell=3`). The labor is free (it was idle); the goods are sold the evening before, alone in the market.
- **Vs O9, paired both seats: fresh 101-200 +$5,600/game (t=11.74, 94-6); fresh 201-300 +$6,714 (t=14.17, 94-6); held-out 11-30 +$6,709 (t=5.79, 19-1).** ~3× O8's throttle gain, ~15× the endgame fix.
- **Tape panel, held-out 11-30 (own margin vs the tape, O12 minus O9): peterparker +$5.8k, alaylm +$3.2k, yangkuang2 +$5.0k, bahaenes −$1.1k → mean +$3.2k/game across the 4 real ladder tapes**; C1 +$3.2k, clone +$2.1k. Still loses to every tape (−$19.5k to −$30k) but the gap shrinks 15-25% — the first own-code change in this file to move the tape gap at all. Zero agent errors everywhere.
- Sweep (idle rule at h18 throughout): force hour 16 −$3.9k, 17 −$0.2k, 18 +$3.7k, 19 +$5.4k, **20 +$5.6k**, 21 +$4.4k, 22 +$3.8k; force threshold 1/3/6 at h20 all +$5.1-5.7k. Idle-rule start hour 14-21 all +$1.9-2.8k (18 best). Idle rule without the evening same-turn sells: +$1.5k — **the SELL timing is the lever, not the drop.** Forcing everyone home before ~h18 destroys real work.
- Mechanism check: total revenue and quantities sold are near-identical (O12 $90.7k vs O9 $91.0k over 10 games) — the gain is price-per-unit and its compounding through earlier hires/animals; per-seat margins are often equal to the dollar in both seats (a pricing effect, not seat order). Reconciles with the `O5_SAMETURN_SELL` null above: a same-turn top-up on the few daytime drops is nothing; moving the whole overnight batch ahead of the opponent's h0 dump is the prize.
- Market state seen in one O-vs-O game: MILK $13-53 (base 160) days 15-24, WOOL $5-31 days 18-24 until a YARN_STORE unlocks, STRAWBERRY $164-203 days 9-20 then $11-43 from day 21, MELON +100 units ($140-158; only the town center consumes melon, 1/day), FERTILIZER has no consumer and only drifts down. **Next lead drafted, untested: `candidates/O13_HOLD.py` — hold MILK/WOOL in the shed from day 20 and release on day 29 (a unit sold later faces inventory lower by future consumption minus the opponent's future sales; never hold FERTILIZER or MELON).**
- Naming: this was called O10 while being built; renamed O12 because `O10_O9_MELON_LATEFERT` already existed.
- **O12 + melon late-fert (`candidates/O14_EVENING_MELON.py`) — TESTED, DECLINED for the ladder.** Self-play vs O12: fresh 101-200 +$1,519 (t=3.75, 68-32), held-out 11-30 +$194 (t=0.17). Tape panel held-out 11-30, O14 minus O12: peterparker −$10.2k, alaylm +$6.4k, bahaenes ≈0, yangkuang2 −$6.5k → **mean −$2.6k/game**; C1 +$0.5k. Same verdict the melon patch got on O8/O9 above: an O-vs-O gain (more melons into the day-11 h0 dump against another O agent) that does nothing or worse against tapes that already dumped at day 10. Don't stack it onto the ladder entry; O12 stays the submission.
- **Holding / metering late-game product (`candidates/O13_HOLD.py`, Sep 9 night) — CLOSED, decisively.** Theory: a unit sold later faces inventory lower by (future consumption − opponent's future sales), so hold drained-market products and release late. Measured vs O12, fresh 101-200: hold MILK+WOOL from day 20 and dump on day 29 h≥16: **−$4,272/game (t=−10.5, 18-82)**; metered selling (each hour sell only the units that keep the quoted price ≥ floor×base, using an exact replica of the engine curve, MILK/WOOL/STRAWBERRY from day 20, clear-out day 29): floor 0.5 **−$1,786** (22-78), 0.7 **−$3,411** (15-85), 0.85 **−$4,736** (6-94) — monotonically worse the more we hold. Tape panel (0.7): −$0.4k to −$1.9k on every tape, C1 −$4.7k. Why: the opponent (O12 or tape) keeps selling into the room we leave, so the market never drains for us; our withheld units then go out concentrated (own price impact) and the held cash was also missing from day 20-24 reinvestment. Same conclusion as the older "holding wheat/fertilizer for late prices: negative" line, now for the high-value products too. **Sell everything as soon as it is in the shed; the only timing lever that works is going ahead of the opponent's batch (O12), not waiting.** `_mprice`/`_meter_units` in O13 are a verified exact replica of the engine's `market_price` (0 mismatches over ±300 units, all items) if a future proposal needs to price a batch before selling it.

## Move ledger (Sep 9, late) — the 433-move gap attributed by phase; nothing promoted, review first

Instrument: `tools/move_ledger.py` cuts every unit-day into legs (a run of moves ending in an action) and attributes each to spawn_walk / task_walk / shed_trip / dead_walk, for both players in the same game, plus long-leg (≥4) breakdown by verb and hour, same-tile chain lengths, and PASS by (day band, hour band). Run on O9_MELON_LATEFERT vs tape_alaylm, seeds 1-6 (mean money 84.5k vs 106.8k):
```
phase        ours  moves/leg   tape  moves/leg   diff
spawn_walk    666    3.31       527    3.03     +139   (more hand-days, not longer walks)
task_walk    2410    1.95      2023    1.43     +387   <- the gap
shed_trip     106    2.62       149    2.66      -43   (we make FEWER shed trips)
dead_walk      33    3.70        83    1.63      -50
work actions 2382 (42% with no move) vs 3141 (51% with no move); PASS 840 vs 469; unit-turns equal (6.6k)
```
Long legs (≥4 moves), moves/game: ours WATER 736 / FEED 190 / PLANT 117 / FERTILIZE 100 / HARVEST 96; tape WATER 342 / HARVEST 89 / PLACE 80 / FEED 8. **The tape almost never walks 4+ tiles to feed; we do it ~40×/game** — `_build_route` runs for every unit every hour and the first unit in index order with pending animals takes the route from wherever it is. Our long WATER legs cluster at h6-8 (after the first sweep, when the nearest remaining top-tier task is far) and h19-23 (slack watering by otherwise-idle hands — free, not a real cost). PASS: ours is 675/840 in h18-23 and ~6/game mid-day on days 9-27 — **hands are saturated h0-17 and unemployed after; the tape's PASS is spread and only 101 in the evening; it waters later (water_hour 14.7 vs 13.4)**. The tape's 760 extra work actions/game are mostly animal service (+120 CARE, +68 FEED, +49 COLLECT on 17 vs 13 animals) and harvest/plant (+60/+52), done in same-tile chains of 3-4 (its chain hist 3:241 4:229 vs ours 3:188 4:106).

Tested against this attribution (all on O9_MELON_LATEFERT, paired self-play; none promoted):
- Inner-ring pasture reservation (shed dist ≤2 kept for animals, `B12_*`): animals 2.4→2.2 only (the ring is mostly LOCKED until land unlocks — 5 usable tiles with one quadrant) and strawberries pushed to 4.9: −$1.8k to −$6.1k. Closed.
- Sweep ownership (take a task only if no other free hand is closer, `B13_01/04`) and route ownership (skip an animal route if a free hand is ≥2 closer, `B13_02/05`), both (`B13_03`): FEED long legs 190→142, total moves −34; dev +$1.3k (t=1.48) / +$2.7k (t=1.98), **held-out +$347 (t=0.57) / +$709 (t=1.06)** — suggestive, below the bar. With 13 hands almost every task has *some* closer competitor, so the rule mostly falls through to the old behaviour.
- Pacing: defer the "water" tier to h≥10 / h≥14 (`B14_*`): −$5.9k / −$2.2k — that tier contains the yield-raising window waterings of one-shot crops; they must not wait. Maintenance watering is already alternate-day, so there is little left to pace.

**Reading for review:** the move gap is real but is mostly a symptom; the binding constraint is that our day's work is front-loaded into h0-17 and the evening is empty, while the tape spreads a larger obligation set across the whole day with fewer hands. Adding obligations (herd, crops) saturates our morning and loses; shifting work later naively loses because the deferrable set is small. The design question that follows is whether a day-plan that assigns time-critical work (feed at wheat pickup, harvest, window watering) to the morning and everything else to a paced afternoon can carry a larger obligation set — that is a dispatcher rewrite, not a patch, and should be judged on the 4-tape panel. The other session's O12_EVENING_DEPOSIT already monetises the evening idle directly (+$3.2k on the tapes) and is the current frontier per memory.

## Move ledger (Sep 9, late) — the 433-move gap attributed by phase; nothing promoted, review first

Instrument: `tools/move_ledger.py` cuts every unit-day into legs (a run of moves ending in an action) and attributes each to spawn_walk / task_walk / shed_trip / dead_walk, for both players in the same game, plus long-leg (≥4) breakdown by verb and hour, same-tile chain lengths, and PASS by (day band, hour band). Run on O9_MELON_LATEFERT vs tape_alaylm, seeds 1-6 (mean money 84.5k vs 106.8k):
```
phase        ours  moves/leg   tape  moves/leg   diff
spawn_walk    666    3.31       527    3.03     +139   (more hand-days, not longer walks)
task_walk    2410    1.95      2023    1.43     +387   <- the gap
shed_trip     106    2.62       149    2.66      -43   (we make FEWER shed trips)
dead_walk      33    3.70        83    1.63      -50
work actions 2382 (42% with no move) vs 3141 (51% with no move); PASS 840 vs 469; unit-turns equal (6.6k)
```
Long legs (≥4 moves), moves/game: ours WATER 736 / FEED 190 / PLANT 117 / FERTILIZE 100 / HARVEST 96; tape WATER 342 / HARVEST 89 / PLACE 80 / FEED 8. **The tape almost never walks 4+ tiles to feed; we do it ~40×/game** — `_build_route` runs for every unit every hour and the first unit in index order with pending animals takes the route from wherever it is. Our long WATER legs cluster at h6-8 (after the first sweep, when the nearest remaining top-tier task is far) and h19-23 (slack watering by otherwise-idle hands — free, not a real cost). PASS: ours is 675/840 in h18-23 and ~6/game mid-day on days 9-27 — **hands are saturated h0-17 and unemployed after; the tape's PASS is spread and only 101 in the evening; it waters later (water_hour 14.7 vs 13.4)**. The tape's 760 extra work actions/game are mostly animal service (+120 CARE, +68 FEED, +49 COLLECT on 17 vs 13 animals) and harvest/plant (+60/+52), done in same-tile chains of 3-4 (its chain hist 3:241 4:229 vs ours 3:188 4:106).

Tested against this attribution (all on O9_MELON_LATEFERT, paired self-play; none promoted):
- Inner-ring pasture reservation (shed dist ≤2 kept for animals, `B12_*`): animals 2.4→2.2 only (the ring is mostly LOCKED until land unlocks — 5 usable tiles with one quadrant) and strawberries pushed to 4.9: −$1.8k to −$6.1k. Closed.
- Sweep ownership (take a task only if no other free hand is closer, `B13_01/04`) and route ownership (skip an animal route if a free hand is ≥2 closer, `B13_02/05`), both (`B13_03`): FEED long legs 190→142, total moves −34; dev +$1.3k (t=1.48) / +$2.7k (t=1.98), **held-out +$347 (t=0.57) / +$709 (t=1.06)** — suggestive, below the bar. With 13 hands almost every task has *some* closer competitor, so the rule mostly falls through to the old behaviour.
- Pacing: defer the "water" tier to h≥10 / h≥14 (`B14_*`): −$5.9k / −$2.2k — that tier contains the yield-raising window waterings of one-shot crops; they must not wait. Maintenance watering is already alternate-day, so there is little left to pace.

**Reading for review:** the move gap is real but is mostly a symptom; the binding constraint is that our day's work is front-loaded into h0-17 and the evening is empty, while the tape spreads a larger obligation set across the whole day with fewer hands. Adding obligations (herd, crops) saturates our morning and loses; shifting work later naively loses because the deferrable set is small. The design question that follows is whether a day-plan that assigns time-critical work (feed at wheat pickup, harvest, window watering) to the morning and everything else to a paced afternoon can carry a larger obligation set — that is a dispatcher rewrite, not a patch, and should be judged on the 4-tape panel. The other session's O12_EVENING_DEPOSIT already monetises the evening idle directly (+$3.2k on the tapes) and is the current frontier per memory.

**Tape-plan-on-our-dispatcher diagnostic (Sep 9, late, on O12; `evolve/gen_batch15.py`, NOT candidates):** herd 17 in the inner ring (`L1`) −$12.3k on the tape panel; + 32-tile strawberry band and wheat far (`L2`) −$21.2k; + daily service (`L3`) −$22.9k. The ledger shows why: with the tape's layout our task-walk moves equal the tape's (2,025 vs 2,023) but work stays 2,350 vs 3,141 and PASS rises to 1,005 — the obligation set never materializes (35-40 plants vs 57, 2.3 quads vs 3; early animals starve land/seeds) and per-hand throughput stays ~170 vs ~285 actions/hand/game. Fourth confirmation that the plan only pays at the tape's throughput. Note P6's "expert execution" (travel 1.01) was a bench on expert-supplied days; in full games it ran travel 1.16 / idle 41% / weeds 38 — no dispatcher of ours has reached tape throughput in a full game. **Plan for review: `docs/dispatcher-rewrite-plan-sep09.md`** (herder loops + block sweeps with ledger acceptance gates before any money test, then a plan sized to measured capacity).
- **O15_SALE_PRIORITY (Sep 9 night, supplied by Grace) = O12 + reorder the turn's SELL orders by (local price sensitivity × batch²) descending. Vs O12 paired: fresh 101-200 +$4,081/game (t=19.9, 100-0); held-out 11-30 +$3,524 (t=13.3, 20-0). Tape panel held-out 11-30, change vs O12: peterparker +$0.4k, alaylm +$0.3k, bahaenes +$0.3k, yangkuang2 +$0.2k; C1 +$0.9k.** Mechanism: market orders are matched against the opponent's list position by position, so the order only matters when the opponent sells the same items in the same turn — an O-family opponent does, a tape mostly doesn't. Hence a huge O-vs-O edge and a few-hundred-dollar ladder edge. Free and never lost a seed, so it is the submission (`submissions/O15_SALE_PRIORITY.zip`); read the tape numbers, not the +$4k, as the ladder expectation.

**Global orchestrator (Sep 9 night, `candidates/X1_ORCH_FLATPRIO.py`, FOR REVIEW):** replace per-hand self-selection (nearest task of the top tier) with a per-turn cost matrix over free units × open crop tasks (distance + priority − commitment bonus), assigned by global minimum cost. Ledger: PASS −16%, spawn walks −28%, long legs down, work +4%. Paired self-play vs O12 **+$4-5.7k/game at t 5.6-8.2 on every chunk of 130 seeds**; vs C1 +$24k (O8: +$14.8k). Tape panel (paired margin, n=30): null (−$451, t=−0.39) — the extra output is strawberries into a shop-limited market; in self-play it takes share from the O12 opponent, vs a tape it only depresses our price. **Lesson: self-play overstates volume gains in glut-prone goods; judge ladder candidates on the tape panel with the MARGIN metric (now the harness default) at n ≥ 100.** Animals-in-matrix (X3/X4) and capacity-to-wheat/herd (X2) were worse. Full log: `docs/dispatcher-rewrite-plan-sep09.md`.
- **Evolve loop re-based onto O15 (Sep 10, early).** `evolve/chassis.py` is now the frozen copy of `candidates/O15_SALE_PRIORITY.py` (blocks.py `K_LIVE` points there; the build strips the inherited block markers; the `sweep` block now lists `_steal_task`, which the O lineage keeps between `_build_sweep` and `_crop_step`). `space.render(base_params())` reproduces O15 to the dollar (seed 1 vs C1: 69,932 both). 24 K.py-era KNOB_SPACE names (spec_*, seed_orders_cap, land_deadline_shift, sell_order, herd_species_bias) are not in O15's KNOBS and are skipped with a one-line warning; 41 live params. The old chassis is kept as `evolve/chassis_K_legacy.py`. `loop.py` defaults: `--frontier candidates/O15_SALE_PRIORITY.py` (selection yardstick), `--clone` = the 4 real ladder tapes as a comma-separated panel (cascade `eval_panel` reports the mean paired margin; the old clone `opp_scenario_v14` is gone from the default because it is not a ladder proxy), and **held-out promotion now requires the candidate's mean panel margin >= the frontier's own (`--panel-floor`, default 0)** — the frontier's panel baseline is computed once per run and stored in cfg. Smoke run (3 candidates, scratch DB): base params score dev +0 / panel delta +0 against O15, exactly as they should; C1-preset and H32-preset islands score −$0.2k/−$2.1k self-play and −$5k/−$8.9k on the panel. tests/test_complexity_gate.py and test_render_contract.py pass on the new chassis. The supervisor on the Air has been stopped since Sep 3 — restart it with the new defaults from a terminal (`python3 evolve/loop.py --hours N`) when wanted.

**O16_ORCH_ON_O15 (Sep 10) = O15_SALE_PRIORITY + the X1 global crop orchestrator — FOR REVIEW.** The two changes are orthogonal (O15 reorders SELL orders by price pressure; X1 changes which hand takes which crop task). Paired vs O15: dev +$4,213 (t=5.22, 9-1), held-out +$3,653 (t=9.27, 20-0), fresh 31-50 +$3,772 (t=3.67, 16-4). Fixed benchmarks (dev): vs C1 +$26,034 (t=12.0, 10-0), vs O12 +$7,800 (t=7.6), vs X1 +$5,508 (t=7.5) — i.e. the O15 and X1 gains stack. Tape margin panel n=30 under the lottery: −$325 (t=−0.28) — **but under `KAGG_FIXED_SHOPS=1` (see top): +$3,216/game, t=11.21, positive on every tape (peter +$2,873 t=3.5, alaylm +$2,759 t=5.6, bahaen +$3,387 t=6.3, yangk +$3,388 t=5.9, clone +$3,673 t=4.9).** The orchestrator transfers to the ladder opponents; the earlier null was lottery noise. Zip: `submissions/O16_ORCH_ON_O15.zip`. Generator: `ORCH_BASE=<file> ORCH_OUT=<name> python3 evolve/gen_orchestrator.py`.
- **O16_CAPITAL_CHECKPOINT (Sep 10, supplied by Grace) = O15 + capital-event trigger measured against the cash at the last checkpoint (reset daily and after each event) instead of the previous hour's cash — so many small evening/same-turn sales add up to one mid-day reinvestment decision. Vs O15 paired: fresh 101-200 +$2,830/game (t=7.3, 77-23); held-out 11-30 +$1,936 (t=2.4, 14-6); C1 +$22,768 vs O15's +$19,180 (+$3.6k). Tape panel: seeds 11-30 mean −$0.9k (noise, ±5k per tape); seeds 31-70 (n=40) all four tapes positive, mean +$1.9k (peterparker +3.8k, alaylm +1.6k, bahaenes +1.5k, yangkuang2 +0.6k); pooled 60 seeds ≈ +$1.0k/game.** Submission (`submissions/O16_CAPITAL_CHECKPOINT.zip`); O15 stays the loop frontier until a segment confirms O16 on the panel gate. Lesson: a 20-seed tape panel cannot resolve a ~$1k effect — use n≥40 per tape before calling a panel result.
- **O17_ORCH_CAPITAL (Sep 10 night) = O16_ORCH_ON_O15 + O16_CAPITAL_CHECKPOINT's cumulative capital trigger — the two O16 lines merged; NEW SUBMISSION.** All numbers under `KAGG_FIXED_SHOPS=1`, paired both seats. Head-to-head, fresh 101-200 (n=100): O16_CAPITAL vs O16_ORCH −$1,016 (t=−2.6, 38-62) — the orchestrator is the stronger of the two O16s; O17 vs O16_ORCH +$1,209 (t=3.4, 65-35); O17 vs O16_CAPITAL +$2,143 (t=4.5, 62-38). Tape panel, seeds 31-70 (n=40/tape), mean paired margin: O15 −$21,998; O16_CAPITAL −$20,420 (+$1.6k vs O15); O16_ORCH −$18,960 (+$3.0k); **O17 −$19,054 (+$2.9k, i.e. equal to ORCH within noise)**. **Read this as: O17 is the strongest integrated candidate in the controlled parent-vs-merge test and approximately matches O16_ORCH on the current four-tape panel — not as a demonstrated ladder improvement over the orchestrator.** The three layers act at different points of the chain (orchestrator: what workers do → capital checkpoint: when cash triggers investment → O15 ordering: how competing sales execute), which is why they stack head-to-head; the tape panel says the orchestrator carries the ladder-relevant part. Retain O16_ORCH as the control benchmark and O16_CAPITAL as the ablation. Zip: `submissions/O17_ORCH_CAPITAL.zip`. Seed-budget rule: use enough seed-level observations to resolve the effect you are distinguishing — 20 seeds for cheap mechanism screens, ≥40/tape (here 100 h2h) when the expected effect (~$1-2k) sits inside the tape-lottery noise band; neither 20 nor 100 is a universal answer. **REVISED (Sep 11, after the capital-events instrumentation below): the capital checkpoint's margin gain is an input-price attack (extra h2 wheat/fertilizer buys raise the price the fixed-quantity tape pays; own money −$1,032 vs O15 while margin +$711). O17's +$1.2k h2h edge over O16_ORCH is that same effect applied to an O-family opponent, and its panel parity hides lower own money. Live opponents adapt quantities (M2/M3 precedent), so this does not transfer. SUBMIT O16_ORCH_ON_O15, NOT O17; O17 stays in the repo as a documented negative example. Add an own-money floor to any promotion gate (margin alone would climb this hill).**
- **Two-axis promotion gate + gain taxonomy (Sep 11, `evolve/cascade.py` `eval_panel`/`classify_gain`, `loop.py --own-floor`).** The tape panel now reports OWN money per game alongside the paired margin, both as deltas vs the frontier's own panel baseline. Held-out promotion requires all three: beats the frontier head-to-head (t≥2), panel margin delta ≥ `--panel-floor` (0), panel own-money delta ≥ `--own-floor` (0). Every candidate is classified by why it wins: **architecture** (margin↑, own↑ → promote), **exploit** (margin↑, own↓ → recorded as `held_exploit`, never core; the capital checkpoint is the type specimen), **economic** (own↑, margin flat → investigate/widen panel), **failure** (both↓), neutral. Reasoning: a policy can win the matchup while losing the underlying game — margin alone would have promoted the input-price attack. Mechanism classes to keep apart: farm mechanisms (time→actions→production→inventory→cash; lifecycle care, coordination, orchestrator, evening/endgame conversion — these generalize), market mechanisms (timing × opponent behaviour × price formation — opponent-specific), evaluation artifacts (fixed tapes, correlated RNG, seat effects, shop lottery, small n). Smoke run: base params classify neutral (+0/+0); a +$3.6k h2h candidate came back panel −$1.0k / own −$4.1k → HELD_FAIL, exactly the case the gate exists for. Known pre-existing test failures: `tests/test_complexity_gate.py` expects `propose.PARAM_BLOCK`/`BLOCK_FAILURE_CLASSES` to know the new `orchestrator` block (11 failures before and after this change) — the orchestrator-chassis owner should add it.

## Where the gap is
- Frontier tapes bank $130–175k where we bank $85–100k. Decomposition: wheat sales (−$15k; tapes plant ~5 wheat tiles/day continuously and sell ~400 units late), melon timing (tapes sell 72 melons on day 10 at $242; we sell later at $166), fertilizer volume, strawberry price ($78 vs $93).
- Our labor per obligation is ~2× the winners' (11.3 vs 6.6 unit-turns per animal-day). Every scaling knob loses because the dispatcher cannot convert extra capacity into serviced obligations. Changes to `sweep`, `dispatch`, `animal_routing`, `crop_admission` are where the remaining value is; `economy` knob changes are mostly exhausted.

## Measured execution gap (process traces, seed 1, Sep 3) — the numbers to move
- **travel per work action: C1 1.5–1.6 vs frontier tapes 0.97–1.05.** Same hand count (12–13). That is the whole
  labor-efficiency gap in one number: the tapes do ~250 more work actions in days 8–15 with fewer moves.
- **The tapes skip feeding on non-production days**: missed_feed 37 (Milan Leonard) / 12 (Yuan800) vs C1's 13/7 — an
  animal only escapes after 2 consecutive unfed days, and cows produce every 2 days, sheep every 3. C1 feeds everything
  daily. Deliberate alternate-day feeding of animals not due to produce frees ~10–15 unit-turns/day.
- Tapes water later in the day (water_hour 14.2–14.3 vs 13.1) but miss fewer plant-days (334–407 vs 430–564): they
  batch watering into fewer, fuller sweeps instead of scattering it.
- Tapes carry more idle (13% vs 8%) and still win: idle is not the problem, wasted movement is.
- Net-worth divergence starts at **day 10** in both tape matchups — the days-8–15 window (second land quadrant,
  herd at 10–14, 50–60 plants) is where the sweep/dispatch design decides the game.

## Routing oracle (evolve/oracle.py, Sep 3 night) — routing alone is NOT the lever
- Counterfactual executor with travel made free (every relocation = 1 turn) on C1 vs the Yuan800 tape, seeds 1–8:
  own money changes between **−$63k and +$25k per seed, mean ≈ 0**. Idle unit-turns explode (3–10× the base).
  With travel free, C1 does not have enough work to give its hands, and its economy does not scale production
  to use the freed labor (hires and seed purchases are driven by load and morning cash, not by capacity).
- Halving travel ("speed2") is also ≈ 0 on average. Conclusion: **a better router bolted onto C1's allocation
  is worth little.** The frontier's edge is *paired*: it generates more obligations (13–14 animals, ~5 wheat tiles
  planted every day, 400 wheat units sold) AND services them at 1.0 moves per action.
- So proposals must couple the two: raise the work available per hand-day (herd size, continuous wheat/one-shot
  planting cadence, harvest batching) together with the execution change that makes it serviceable. Execution-only
  or allocation-only changes have both been measured to fail.

## Rules for proposals
- Propose mechanisms, not knob nudges; each proposal should change behaviour in a way visible in the per-day trace.
- Prefer execution-layer blocks. Batching, alternate-day watering of low-yield tiles, fertilize-from-carry, same-day deposit-and-sell, wheat cadence, fewer reversals, route merging.
- A block replacement must define exactly the same top-level functions, use only names already in the chassis, and be valid Python 3.9 (no match statements, no `X | Y` type unions).
- Never touch the crash guard, the engine constants, or `perceive`.
- Make proposals materially different from each other and from what is already in the archive.

### H_GATE144: hiring's marginal fibonacci price — CONFIRMED on both axes (Sep 11, AGE-360 follow-through)

**Engine fact that drives it.** `farm["hands"] = []` at the end of every day (engine ~line 881), and the
n-th hire of a day costs `_fib(n)`: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233. Labour is therefore
re-bought daily on a CONVEX curve, and the 13th hire of a day costs 233 against the 9th at 34.

**The leak.** `_hire_plan` tops up toward a workload-derived target and stops only on affordability. It
never asks whether the NEXT hire is worth its own fibonacci price. Measured wage bill on O17: **$6,698/game,
9.5% of final money**, concentrated in the tail — days 18-28 pay 144-233 for the last hire of the day
(hires/day peaks at 13.3). `tools/horizon_roi.py --mode marginal` priced that last hire at **-$361 to
-$2,108/game** (t=-2.6 to -10.4), replicated on held-out seeds at **0% of 32 cells positive**. The wage
arithmetic matches the counterfactual almost exactly: removing one hire/day saves $804 in wages over days
24-29 against a measured net gain of $361, i.e. the marginal hand produces ~$443 for an $804 wage.

**The fix is one line, at the single choke point** (`evolve/gen_hire_gate.py` generates it): refuse a hire
whose own marginal price exceeds `HIRE_MAX_MARGINAL`. Inert on cheap early hires (days 0-7 place 5-8 hires,
marginal cost <= 8), binds only on the steep tail. M maps to an effective cap: 55->10, 89->11, 144->12,
233->13 hands/day.

**Dose-response, held-out seeds 21-40, vs frontier `O16_ORCH_ON_O15`, `KAGG_FIXED_SHOPS=1`:**

| M | cap | h2h margin | t | w-l | panel OWN | t |
|---|---|---|---|---|---|---|
| 233 | 13 | +435 | 3.09 | 14-5 | +745 | 8.39 |
| **144** | **12** | **+1,018** | **3.41** | **16-4** | **+1,334** | **9.58** |
| 89 | 11 | -21 | -0.03 | 13-7 | +1,893 | 7.82 |
| 55 | 10 | -905 | -0.72 | 11-9 | +1,792 | 4.95 |

A clean interior optimum at M=144. Own money rises monotonically as the cap tightens (more wages saved)
while h2h peaks and then falls (production lost) — the two curves crossing is the tradeoff, and h2h is the
discriminator. M=144 panel margin: **+877 (t=5.21), positive on all four tapes AND the clone.**

**Classification: own-economy gain, but NOT "we gain what they lose" — CORRECTED Sep 11.** The first
reading of this table said panel own (+1,334) exceeding panel margin (+877) meant we gain more than the
opponent loses. Direct both-sides measurement on peterparker, seeds 21-40, says the opponent does not lose
at all:

| candidate | our money | tape's money | margin |
|---|---:|---:|---:|
| O16_ORCH (base) | 171,962 | 210,110 | -38,148 |
| H_GATE233 | +1,415 | +266 | +1,149 |
| H_GATE144 | +2,664 | +873 | +1,791 |
| H_GATE89 | +4,217 | +1,482 | +2,735 |
| H_GATE55 | +4,480 | +2,846 | +1,634 |

**Both sides gain, and the spillover grows as the cap tightens.** Hypothesis (NOT yet verified): fewer hands
means less production, so we sell less into the shared pool and prices rise for everyone, including the tape.
That is a supply-side price spillover, the mirror image of the capital checkpoint's input-price attack. It is
not an exploit -- our own money rises strongly and it rises for a real reason (we stop overpaying for labour)
-- but part of the margin gain is a price effect, and against a field that adapts its quantities the
spillover need not behave the same way. The margin optimum is where our gain still outruns theirs; at M=55
theirs has grown to 64% of ours and the margin collapses. Treat the third gain class as
**own-up/opponent-up** rather than forcing it into architecture-vs-exploit.

**Which M to ship is UNSETTLED.** The two baselines disagree and the disagreement is systematic:

| M | self-play h2h vs base | 4-tape panel margin (excl. clone) | clone |
|---|---:|---:|---:|
| 144 | **+1,018 (t=3.41, 16-4)** | +903 | +773 (t1.7) |
| 89 | -21 (t=-0.03, 13-7) | **+1,238** | +208 (t0.3) |

M=89 is better on every one of the four real ladder tapes and worse in self-play and against the clone.
M=144 is the safer pick if the field plays like us or like the shared clone script (see the
opponent-detection note: 93.2% of sampled ladder opponents match one clone fingerprint); M=89 is the better
pick if the tapes are the right proxy. This project has said both "judge ladder candidates on the 4-tape
margin panel" and "the clone is not a ladder proxy", and those two rules point opposite ways here. Grace's
call; do not let a later session read the earlier M=144 recommendation as settled.

**Caution.** M=89 looked best in dev h2h (+1,072, t=2.60, 15-5 on seeds 1-20) and collapsed to -21 on
held-out seeds 21-40. Selection data is not confirmation data; the dev ranking of the M values was wrong.

## Evidence rules — the three ways this project has fooled itself

Each of these was discovered the expensive way. Check a result against all three before promoting it.

1. **A margin gain is not a gain until own money confirms it.** The promotion gate is margin-only, and a
   fixed tape can be attacked through input prices: `O16_CAPITAL_CHECKPOINT` showed +711 margin (t=2.4) and
   **-1,032 own money** (t=-2.8) — the extra h2 wheat/fertilizer buying raised the prices the tape paid for
   its fixed quantities, so our money fell and theirs fell more. A live opponent adapts (M3 netted -2.4k vs
   never-touched opponents), so gains of this shape do not transfer. Always report the own-money panel
   beside the margin panel. See "Capital-timing gains on the tapes are input-price attacks" below.

2. **Small panels manufacture findings, especially for lumpy interventions.** The 12-cell panel (4 tapes x 3
   seeds) is adequate for *paired* policy comparisons, where most game variance cancels. It is not adequate
   when the intervention changes the trajectory wholesale. AGE-360 produced two convincing results at 12
   cells — animals after day 6 negative at t=-2.03, and deferring the opening animal buy worth +$6.4k at
   t=-4.64 — and **both dissolved at 24-32 cells, one with a sign flip.** Rule: lumpy capital classes
   (2-3 orders/game at $400-500/unit) need >=24-32 cells before their sign is readable; flow classes
   (hundreds of orders/game) are stable at 12.

3. **Class ablation is not marginal ROI.** Removing a whole investment class measures the value of the
   *subsystem*. It estimates the value of the *last unit* only when the intervention approximates a one-unit
   change — which is true for lumpy capital (`BUY_LAND`: ~2 orders/game) and false for anything the policy
   replenishes continuously. `HIRE` is the case: ~267 orders/game topping up to a target, so blocking the
   class from day 26 removes the workforce, not the marginal hire. **The two signs are opposite:** class
   ablation +$12,805 (t=9.78) says labour is essential; the marginal test at -1 hire/day says the last hire
   each day is worth **-$361 to -$2,108** (t=-2.6 to -10.4, replicated on held-out seeds at 0% of cells
   positive). Before reading any cutoff row as a threshold, check the class's orders-per-day. Use
   `tools/horizon_roi.py --mode marginal --reduce 1` for the threshold question.

## Lessons from O4 (Sep 9) — apply to every future proposal, not just the reactive-policy family
- **Fix resource conflicts before adding more work.** If two workers can claim the same fertilizer/wheat/site in one turn, more hands or more crops just means more collisions, not more output. Check for un-reserved shared resources (anything pulled from a shared shed/pool without decrementing it for the rest of that turn's dispatch) before proposing capacity increases.
- **Useful work matters more than raw activity.** More care/feed/watering isn't automatically more production — check the actual payoff timing (e.g. a care bonus earned today may only pay off on a *later* scheduled production day, not today's). Verify off-by-one timing assumptions against the engine source, not against intuition.
- **Small, familiar seed sets mislead.** A margin measured on a handful of dev seeds can vanish or reverse on a larger frozen, paired, held-out set (this file's own M5/M6 and V3_16/19 results are the same lesson from the other direction). Keep selection data separate from confirmation data, pair both seats, and freeze the exact seed range and candidate SHA before trusting a result.
- **Audit the actual entrypoint and engine effects, not just error counts.** A wrapper (e.g. a tape-hybrid fallback path) can bypass code you think you changed. Zero Python errors does not mean zero wasted/ineffective actions — a legal-looking action that doesn't actually change engine state (like a fertilizer pickup that loses a race) won't raise an exception; it just does nothing. Instrument for state-change, not just crash-freedom.
- **Economic plausibility isn't sufficient evidence.** "This should help the economy" isn't a substitute for a measured, paired-seed result — several plausible-sounding ideas (competitive herd sizing, anticipatory fertilizer buying) have been built, tested, and rejected in this project (see "What is closed" above); a new plausible-sounding idea needs the same bar, not a lower one.
- **A win over a reactive/own-code baseline is not a ladder win.** Beating C1, V3_12, or V3_15 decisively is real progress but does not mean beating a replay-wrapped tape (H32/M2/M4) or the real ladder field — those categories have been shown repeatedly to require a different kind of edge (see the M2-adaptive-opening doc). Always state which baseline a result is against.

## Sep 10 — systemic read after the spatial factorial and the market-ledger experiment. Nothing promoted; this is framing plus one open causal question.

**Observational, not causal — do not promote as mechanisms.** The top-five opponent diagnostic produced two hypotheses that remain unconfirmed: (a) opponents apply substantially more fertilizer, (b) some opponents run wheat as a genuine cash crop. Four of the opponent reconstructions behind these were ad hoc. Both also sit near families already in "What is closed" (wheat-as-cash-crop, fertilizer buy/apply), so a proposal in either direction needs a mechanism that explains why the old rejections do not apply, not just a fresh margin.

**The three layers the project is now working across.**
1. Execution — can the farm physically perform its intended strategy efficiently? Strong evidence for worker coordination (no site/resource collisions), lifecycle waste reduction (B), and product movement/release. Spatial routing is unresolved, not refuted.
2. Production architecture — what should the farm produce? Currently only observational hypotheses (above).
3. Economic conversion — given production, when and how does it become cash? O15's sale ordering works strongly against policies with competing sale-order behaviour but only modestly against tape opponents. The adaptive timing policy failed despite better forecasting.

**The pattern that keeps repeating: local optimization is usually insufficient; the wins came from improving a CONNECTION between stages.** More workers do not help if coordination is poor. Releasing product does not help unless selling can happen. Selling at a predicted better price does not help if holding creates other costs. Better geometry does not matter if the routing intervention barely changes routes. C x D is the cleanest case: neither mechanism was strong alone, the coupling was what paid. Treat Kaggriculture as a coupled flow system — labor to actions to production to inventory to market to cash to reinvestment to more production — and prefer proposals that join two adjacent stages over proposals that tune one stage.

**Highest-leverage unanswered causal question: inventory-to-cash accounting.** For every meaningful production event, track produced, carried, dropped, stored, sold, cash received, and what that cash enabled. Then compare sell-now vs hold while explicitly accounting for realized future price, opponent supply bursts, incoming own production, storage pressure, missed sale-order position, and delayed expansion/hiring/purchases. The objective should not be price; it should be closer to *incremental final farm value caused by this inventory decision*. That would separate "delayed selling is bad because forecasting errs" from "cash timing itself is strategically valuable".

Two caveats on that programme, recorded before anyone starts building it:
- The -$578 loss may already be explained by the O12/O13 collision described in the closed list above. Before building anything, check whether the timing policy's losses concentrate in the turns where it deferred a sale that O12 would have made. That is a cheap query against data already collected and could close the question outright.
- "Incremental final farm value caused by this decision" is a counterfactual, not an accounting column. It requires replaying from the decision point with the other choice. Budget for the rollout harness, not just tracking columns — otherwise the result is correlational and will not survive the promotion gate.

## Sep 10 (evening) — the promotion pipeline. AGE-359's action table is a hypothesis generator, not a policy source.

The action timing table (evolve/action_table.py, report section "Action timing patterns") is now measuring. Read this before using anything in it.

**The discipline, in one line: observation tables discover patterns; experiments establish mechanisms; only validated mechanisms become policy.**

**Do not encode action-table correlations as chassis.py rules.** Signals like "FEED_MISSED mid +$1,045" or "BUY_ANIMAL mid +$924" are observational correlations across candidate history, not marginal causal estimates. The candidates that missed feed in mid-game differ from those that did not in every other way too. This project has already paid for that confusion in five separate places — spatial travel, worker routing, market timing, single-seed anecdotes, and raw vs opportunity-normalized melon behaviour. AGE-359's scope note argues runtime encoding is safe because reversion is cheap (candidate swap, 5 submissions/day); cheap reversion makes a bad *submission* recoverable, it does not make a confounded correlation safe to encode, and the ladder is the slowest and least attributable signal available for finding out.

**The pipeline every action-table signal must travel:**
action-table signal → proposer hypothesis → isolated intervention → paired test → held-out validation → chassis rule. No step skipped, and the promotion gate is unchanged.

**Rank hypotheses, not rules.** The archive should carry a status per observation, e.g.:
- FEED_MISSED mid correlates positively — hypothesis
- BUY_ANIMAL mid correlates positively — hypothesis
- SELL timing affects investment timing — causally supported in a specific study (O12/the wool study)
- worker matching saves ~26 tiles — deprioritized
This lets the loop accumulate institutional knowledge without a correlation quietly becoming a policy.

**Sample-quality metadata before interpretation.** Any signal shown in the report needs candidate count, seed coverage, number of independent candidates, context frequency, and whether the observation is averaged. Without those, an n=2 signal reads like a discovery. Note that SELL/BUY item quantities are averaged across the 5 trajectory seeds, not raw per-game events — the caveat is on the totals line; keep it there.

**Why this layer is worth building anyway.** Every mechanism so far was hand-discovered: O2 coordination, O4 lifecycle waste plus coupled product flow and selling, O12 endgame conversion, O15 sale ordering, and the market study's finding that a sale's value is not its price but the investment its cash unlocks. The action table is the first reusable empirical memory of decisions of that kind, and the right next layer above it is decision counterfactuals — at this state, do it now vs delay vs skip, measured on immediate cash, downstream inventory, investment timing, capacity, and final outcome. The table can point at where to run those; it cannot substitute for running them.

**Measurement contract.** tests/test_action_table.py pins extraction: BUY_LAND event day and cumulative cost off the price ladder, SELL product extraction, revenue sourced from sales_rev rather than summed quantities, missed-water/feed day and count, postponement known-input/known-output, and JSON round-trip. Change the extraction rules and update that file in the same commit.


## Sep 10 (late): islands re-seeded on the O16K chassis

- `candidates/O16K_ORCH_KNOBBED.py` (gen: `evolve/gen_orch_knobbed.py`) = O16_ORCH_ON_O15 with `ORCH_ON` gate and the
  orchestrator priorities / commit bonus / slack hour as top-level constants (in `space.CONST_SPACE`). Verified
  byte-behaviour: ORCH_ON=0 == O15 and ORCH_ON=1 == O16 on 6 seeds each (`evolve/orch_knobbed_check.py`).
  It is the chassis source (`blocks.K_LIVE`); new typed block `orchestrator` = `_orch_prio`, `_orchestrate`.
- Islands now: `o15` (chassis, ORCH_ON=0 -- exactly the frontier), `orch` (chassis defaults -- exactly O16),
  `wide` (sigma 0.5), `queue`. Dropped `v312`, `c1`, `H32`, `M2`: all four were V3/C1-era knob values overlaid on
  the O15 chassis (H32/M2's mechanisms lived in K.py code that never ported; M2 is fingerprinting and excluded;
  `c1_params()` re-applied C1's opening knobs on top of O15). 159 H32/M2 + 107 v312 candidates, 0 held passes.
- `space.o15_params()` is the archive/report diff reference (was `c1_params`). Report's action-context table crash
  (dict.items() unpacked as 3-tuples) fixed.
- Chassis sha changed, so the loop's archive filter (`k_sha`) starts a fresh population; first segment re-seeds.
  Smoke run: seed:orch passed held-out on the loop (+4,376 t=7.2, panel delta vs frontier +3,148), as expected.
- Island gate reads (fixed shops, margin panel vs O15):
  - `O17_MELON_ON_O15` (B4_01 melon late-fert ported to O15, gen `evolve/gen_melon_on_o15.py`): -85 (t=-0.2, seeds 11-30),
    +199 (t=0.5, seeds 31-45) -> null on the tapes even without the shop lottery. No melon island. (h2h vs O15 +1.4k/+0.8k.)
  - `O16_CAPITAL_CHECKPOINT` (other session; changes only `economy`): +711 (t=2.4) and +1,091 (t=2.4), every tape
    positive -> `capital` island added, seeded via the new `{"candidate": file, "block": name}` block reference
    (`blocks.from_candidate`; verified the lifted block renders byte-identical behaviour, 4 seeds).
  - Stacking test `O18_CAPITAL_ORCH` (orchestrator + capital block): vs O15 panel +2,881 (t=8.6) but vs O16 panel
    **-177 (t=-1.0), negative on all 4 real tapes** (clone +1.3k) over seeds 11-40, while h2h vs O16 is +1.5k (t=2.4, 21-9).
    The two gains do not add on the tapes; another h2h-vs-panel divergence. `capital` island therefore seeds with ORCH_ON=0.

### Capital-timing gains on the tapes are input-price attacks (Sep 10, late) -- `capital` island removed

`tools/capital_events.py` (wraps `economy`, logs capital-window turns and totals all BUY/HIRE orders): the checkpoint fires
~1x/day d7-20 at h2-3 and the ONLY totals that change are BUY_PRODUCT WHEAT (+26-40/game) and FERTILIZER (+8-10);
hires, animals, land, seeds are identical. It is a second feed/fert top-up window, i.e. what `KNOBS["capital_hour2"]` does.

| candidate (fixed shops, seeds 11-30, 4 tapes+clone) | margin panel vs O15 | OWN-money panel vs O15 |
|---|---|---|
| O16_CAPITAL_CHECKPOINT | +711 (t=2.4) | **-1,032 (t=-2.8)** |
| O16_ORCH_ON_O15 | +3,104 (t=9.5) | +1,672 (t=5.2) |
| X5 O16 + capital_hour2=2, vs O16 | +1,605 (own -2,595, t=-6.0); fresh 31-50 margin +2,255 (t=5.2) | |
| X5 O15 + capital_hour2=2 | +325 (t=0.9) | |

Reading: the extra h2 buying of wheat/fertilizer raises the input prices the tape pays for its fixed BUY quantities; our own
money falls and the tape's falls more. The orchestrator's gain is own-economy (+1.7k own). "Capital + orchestrator don't
stack" was the wrong question -- the capital gain was never ours. A live opponent adapts its quantities (M3: general
price-impact rule netted -2.4k vs never-touched opponents), so this is excluded like M2. Actionable: the loop's held-out/panel
gate is margin-only and would happily climb this hill -> consider adding an own-money floor to the promotion gate.

## Sep 10 (night): Phase 1 of value-at-risk -- the delay-consequence signal does NOT replicate

`tools/delay_panel.py` (resumable, `--budget-s`; the sandbox kills background processes so long panels run in
150 s chunks). O16 vs 3 tapes x 6 seeds, fixed shops, 17 state buckets x 30 events x delays {1,2,4} h x horizons
{final money, 48-step net worth} = 3,060 counterfactuals (`evolve/delay_panel_O16.jsonl`, summary `..._summary.txt`).

- Horizon 0: every bucket's 95% CI includes zero (means -360..+180, CIs +-200..900). Per-seed sign agreement is
  3-4 of 6 for almost every bucket (coin flip); per-tape 1-2 of 3. Delay curves are not monotone (e.g. WATER/oneshot/cu0
  -34 / +86 / +136 at 1/2/4 h).
- Horizon 48: effects are tens of dollars, all CIs include zero, no bucket consistently negative.
- The single-seed table that motivated the programme (COLLECT -247, FEED/cu1 -234 ...) does not survive: FEED/cu1 is
  +180 here, COLLECT -279+-448.

Reading: in O16 a one-hour delay of one action has no measurable consequence -- the dispatcher re-plans next turn,
another unit or the same unit does it an hour later, and the game has enough slack that the loss is below the seed noise
floor. There is therefore no per-task "value at risk per hour" to encode; V1/V2 (consequence-weighted assignment) and
the animals-in-shared-currency step are moot at 1-4 h granularity, and X1_ORCH ~ X1_ORCH_FLATPRIO is explained.
What could still carry value is systematic under-capacity (a task class that is chronically late by many hours or a
whole day), which is a capacity/allocation question, not a priority-ordering one. FEED/cu0: the engine ignores FEED on
an already-fed-today animal and O16's `_feed_useful` already gates feeding, so there is no "redundant feed" to prohibit.

**Rule (Sep 10):** do not promote an observational importance ranking (action table, one-seed counterfactual) into a
decision weight without first demonstrating marginal consequence under intervention on a multi-seed, multi-opponent
panel. Per-action 1-4 h VaR weighting is REJECTED at the tested timescale, not "needs tuning".

## Sep 11: service-debt ledger -- O16 has no chronic lateness either

`tools/service_ledger.py` derives every obligation from engine tile state each step, for BOTH farms (so the tape's own
service quality is measured on the same games): feed / feed_prod / care / fert / collect(at cap) / water_ongoing /
water_prod / water_window / harvest_ready(rot deadline) / harvest_cap / weed, plus crop deaths (PLANT -> WEED) by
crop/age/day. O16 vs yangk and bahaen tapes, seeds 11-14, fixed shops:

| class | O16 missed | yangk | bahaen | note |
|---|---|---|---|---|
| feed (per animal-day) | 9.2% | 13.3% | 14.5% | O16 misses are placement days + d27-28 endgame (deliberate) |
| feed on production night | 6.4% | 8.7% | 11.9% | |
| care | 15.5% | 6.9% | 4.2% | O16's misses: 126 of 145 on d26-28 or placement days -> deliberate (`_care_useful`) |
| fert collect | 1% | 9% | 5% | |
| collect at cap: prod-days lost | 0 | 0 | 16/game | bahaen leaves capped animals |
| water on production night | 28-30% | 2.3% | 3.1% | HARMLESS: engine accrues ongoing yield whether watered or not; water only matters for the fertilizer bonus (2.2 lost/game = $260) and the 2-day death counter |
| one-shot water in window | 3.9% | 2.1% | 9.9% | |
| harvest_ready | 0.3% missed, 1/game past rot (0 steps) | 0 | 1% | |
| strawberry deaths | 36.5/game, 134/146 at age 17 | 18.5, all age 15-17 | 22.5 | age-17 = end of the 4-unit production life, deliberate abandonment on both farms; O16 simply runs 2x the strawberry tiles |
| overnight carry, all classes | ~0% | ~0% | ~0% (collect 38%) | |

Reading: no obligation class is chronically late or under-served in O16; where it differs from the tapes it is at par or
better, and its extra misses are policy-intended endgame/placement skips. The 17k gap to yangk on these games is not
service debt -- yangk earns more with FEWER crop obligations (567 vs 797 ongoing-water obligations/game). Together with
the delay panel: labour execution (ordering, matching, lateness) is closed as a lever on O16; what remains is what is
planted/bought and when (allocation, commitment timing, cash-enabled transitions).

## Sep 11: Production Allocation Matrix -- where the tapes' money comes from (stable across 3 tapes)

`tools/allocation_matrix.py` (exact market accounting by wrapping the engine's `_commit_unit`; per production line and
farm: asset-days, plantings, obligations, work actions, output units, units sold, revenue, direct cost, net, $/obligation,
$/action, $/asset-day, action share, revenue share; totals + realised unit prices) and `tools/straw_life.py` (per
planting-day: units/planting, production nights, fertilized+watered nights). O16 vs yangk/bahaen/alaylm, seeds 11-14,
fixed shops. O16 money 95-98k vs tapes 89-112k. Stable structural differences:

| item | O16 | tapes (3) | $/game |
|---|---|---|---|
| MELON realised price (same 12 plantings, 69-72 units) | $171-172 | $231 on all three | ~4.2k |
| STRAWBERRY units per planting | 5.5 (47 plantings, 800 actions, $7k seed) | 7.5 (33 plantings, 520 actions, $5k seed) -- same ~250 units | seed 1.4k + 280 labour-hours |
| STRAWBERRY fertilized+watered production nights / planting | 1.9 (1.2 fert/planting) | 3.5 (1.85 fert/planting; fert at ages 9 and 13 exactly) | |
| STRAWBERRY realised price | $84-90 | $100-111 | ~4-5k (shared market: whoever sells more/later gets less) |
| WHEAT | 52 plantings, buys 256-273 units @$40 ($10.5k) | 160 plantings (31% of its labour), buys 111-155 ($4.5k), sells 285-344 | ~6k purchases |
| SHEEP | 12 (306 wool units, $68-73k) | 5-10 (122-247 units) | O16 +15-30k -- our edge |
| labour+land (implied = revenue - purchases - money delta) | 12.5-12.8k | 6.6-8.3k | ~4.5k, same hire counts (280 vs 260-279) -- unexplained |
| action share vs revenue share, STRAWBERRY | 31% of actions -> 17% of revenue | 18% -> 19-22% | |

Interventions read so far (all fixed shops, vs O16, margin AND own-money panels):
- `O19_FERT_PHASE` (fertilize ongoing crops only on production days so each fert covers 2 nights): coverage per fert
  2.07 -> 2.2 nights (O16 was already mostly in phase); h2h +336 (t1.3). Neutral alone.
- `O19_FERT_PHASE_FB8` (fert_buy 3 -> 8; SPACE caps fert_buy at 3, so the loop could never try this): coverage 2.7
  nights/planting, 6.6 u/planting; h2h +1.9k (10-0); **margin panel +1,525 (t6.8) but own-money +287 (t1.6) and +59
  (t0.4) on fresh seeds -> the extra strawberries only shift price share in the demand-limited strawberry market.
  Fails the own-money gate.** The tape's advantage is not more strawberries; it is the same units from fewer plantings.
- STRAW_CUTOFF 19 -> 12/14: identical games (does not control the planting count). wheat_per_animal 0.6/1.0, wheat_tiles 6:
  -1.6 to -1.9k h2h (as in the C1 era) -- the tape's wheat line does not port as a knob.

Open, in order: (1) melon sale timing (who sells first at the $231 price -- an own-money gain if we do, and the one
line where O16 and the tapes have identical production); (2) a real strawberry planting-count control (same units
from ~33 fully-fertilized plantings, freeing 280 labour-hours and $1.4k seed); (3) the $4.5k labour/land cost gap.

## Sep 11 — O12 to O18 synthesis. The search target has moved from worker efficiency to production cycles.

Read this before proposing anything in the execution family. Most of the individual results below already
have their own sections above; this is the through-line they add up to, plus the two findings that were
not yet written down anywhere.

**The central claim.** The remaining advantage is not in making workers generally more efficient. It is in
choosing economically valuable production cycles and protecting the specific obligations those cycles
depend on. The project began by asking "how do we make workers work better"; the evidence now says the
open question is "what economic commitments should we create, and which of their obligations must
execution protect so the payoff actually arrives".

**Three layers, in the order they now matter.**
1. Economic allocation. What to invest in: crops, animals, land, labour, inputs.
2. Production-cycle planning. What downstream cycle does that commitment create? For wheat:
   seed -> crop care -> one-shot preservation -> harvest -> feed substitution or sale -> cash recovery.
3. Execution protection. When tasks compete, which obligations must survive for the cycle to pay off?

Layer 3 is where execution work still earns its keep, and only there. Generic efficiency in layer 3 is
closed (next paragraph); cycle-protecting choices in layer 3 are where O18 found its gain.

**The broad worker-execution hypothesis is closed.** Three independent probes, three nulls:
- Worker matching. With tasks, priorities, eligibility and claims all frozen, perfect reassignment saves
  about 26 travel tiles per game, roughly 0.8% of O15's travel. Choosing a different eligible worker is
  not where the gains are. (See also the X1 audit: ~100 extra state-changing actions, ~28 tiles saved, no
  margin; and the compact-siting/routing factorial, <1% travel saved, in the Sep 10 section.)
- Short-term ordering. The value-at-risk panel (3,060 counterfactuals across seeds, tapes, delays and
  horizons) found no action bucket with a consequence distinguishable from zero. The single-seed ranking
  of COLLECT/FEED/WATER/HARVEST was noise. Mechanism: delaying one action 1-4 hours makes the
  orchestrator replan and another worker services it.
- Chronic lateness. The service-debt ledger found O16 carries essentially no economically meaningful
  chronic service debt; overnight carry near zero. Tapes that earn much more do so with fewer
  obligations at similar service quality.
Taken together: the farm executes its chosen obligations successfully, so the gap is in which obligations
it chooses to create. Do not propose another generic dispatch, routing or matching improvement without
first showing why these three nulls do not apply to it.

**Cash is a state-transition trigger, not just a resource.** The causal study that matters most here:
delaying one small sale cost about $85 in immediate proceeds and changed final money by more than
$10,000. The sale moved when cash thresholds were crossed, which moved when the policy reconsidered
purchases and expansions. This is the mechanism behind O12's evening deposit, behind the capital
checkpoint, and behind why O17 and O18 do not stack. It is also why action-level correlations are
dangerous here: a $85 local effect and a $10k downstream effect are the same event, and only the
counterfactual separates them.

**O18_HARVEST_ONESHOT: execution choices matter when they preserve a production cycle. Mechanism
identified: wheat self-supply.** It harvests before routine watering and planting, moderately favours one-shot watering,
and recalculates assignments from the live board every turn. Paired vs O16 it finishes about $746/game
richer. The attribution chain, not the policy description, is the finding:
  +4.2 wheat seeds ordered -> +17.4 wheat harvested -> +9.5 wheat sold -> -7.2 feed wheat purchased,
  plus a small melon increase and more fertilizer sold with fewer fertilizer applications.
The cash trajectory shows it is a delayed-payback mechanism, not an efficiency gain: about $1,111 behind
on day 15, $859 behind on day 20, recovered around day 22, ahead about $643 by day 25, finishing +$746.
It is explicitly NOT a general efficiency win: movement rises slightly, PASS rises, animal output falls
slightly, daily hand counts are unchanged. The gain comes from preserving a one-shot wheat cycle so the
farm feeds itself instead of buying feed, and sells the surplus.

**Which file is which.** The wheat self-supply result above belongs to `O18_HARVEST_ONESHOT`.
`candidates/O18_CAPITAL_ORCH.py` is a DIFFERENT, EARLIER candidate that also carries an O18 prefix: the
orchestrator + capital-block stacking test, recorded in the Sep 10 (late) island section as vs O16 panel
-177 (t=-1.0), negative on all four real tapes. Do not read one's numbers onto the other. The two share
a prefix and have opposite verdicts, so cite the full name every time, and consider renaming
`O18_CAPITAL_ORCH` out of the O18 slot since it predates the harvest candidate that now owns the name.

**Why O17 and O18_HARVEST_ONESHOT do not stack: mechanisms are not Lego bricks.** The wheat mechanism requires a
specific trajectory: greater crop investment, temporarily lower cash, preserved wheat production,
delayed recovery through harvest, then feed substitution and surplus sales. O17's capital checkpoint
changes exactly that midgame cash and investment trajectory, so adding it back disrupts the conditions
O18_HARVEST_ONESHOT's gain depends on, and the straightforward merge loses most of it. Generalise this: because cash
timing changes future decisions, a mechanism that helps in one policy regime can interfere with the
trajectory another regime needs. Always test a merge against BOTH parents, never only against the weaker
one, and treat a merge that loses as evidence about trajectory interference rather than as a bad
implementation.

**Marginal mode, corrected. Labour was over-provisioned; planting was not.** Class ablation is not
marginal value (see the Sep 11 H_GATE144 section for the full argument). Under the corrected marginal
tests:
- Roughly one fewer hire per day is an improvement, with dose-response confirming a local optimum:
  -1 unit/day helps meaningfully, -2 units/day gives the gain back.
- An additional marginal planting commitment stays valuable well into the game.
- Marginal feed is near break-even. Fertilizer remains a weak or null lever.
This reverses the older "high movement share means we are overcommitted on work" intuition. The farm did
not have too much work for its labour; it had too much labour for its economically valuable workload.

**Measurement, prediction and profit are three different questions.** The market ledger was an excellent
instrument (388,260 validation checks, zero incorrect bounds, nearly all inferred transitions exact) and
improved forecasting at 12 turns, yet the first adaptive selling policy lost about $578/game and
forecasting got worse at short horizons. Always answer these separately: can we measure the state, can we
predict the future, and does acting on the prediction make money. A yes to the first two implies nothing
about the third.

**Promotion gate, restated.** Margin alone is not sufficient and has already been climbed the wrong way:
the capital checkpoint's margin gain was an input-price attack on a fixed-quantity opponent (own money
-$1,032 vs O15 while margin +$711). Every promotion needs both a relative margin result and an own-money
result, and a candidate whose own money falls is not promoted whatever its margin does.

## Sep 11: O22_MELON_MORNING -- melon sale timing is a real own-money gain (for review, not promoted)

`tools/sale_timeline.py` (every committed SELL unit with day/hour/price + harvest hour, both farms): the tapes harvest all
60-72 melons by d10 h9 (5 hands on melon tiles at h5-h6) and sell them h9-h15 at $217-260; O16 harvests one tile every
~2 h through day 10, 30+ units sit in hands until the nightly auto-drop and sell at the d11 h0 dump ($121-166).
`melon_rush` alone changes nothing (the melons are not harvested early enough); melon late-fert alone (O20) is null.

O22 = O16 + melon late-fert (age 7-8, so tiles are at 6 units on d10 morning) + "melon morning": days 9-14, hours <= 8,
units not on an animal route take the nearest unclaimed 6-unit melon tile, HARVEST, and carry it straight to the shed.
Fixed shops, vs O16, 4 tapes + clone:

| seeds | margin panel | own-money panel |
|---|---|---|
| 11-30 | +1,233 (t3.4), all 5 positive | +372 (t1.0) |
| 31-50 | +899 (t2.4) | +1,258 (t3.2), all 5 positive |
| 51-70 | +2,502 (t6.5), all 5 positive | +1,798 (t4.2), all 5 positive |

Both gates pass on 60 seeds (mean margin ~+1.5k, own ~+1.1k). h2h vs O16 is noisy (+1.4k / -0.8k / +1.9k) as expected
for a timing mechanism against a self-play opponent. Variants that lose: melon morning until h12 (own +127, h2h -1.5k) and
harvesting 5-unit tiles (both displace the h1-h12 animal routes; O16 carries 12-16 animals on d10, the tapes 10-11).
Zip: `submissions/O22_MELON_MORNING.zip`. Stacks on O16 (which is itself pending review vs O15).

## Sep 11: O24_STRAW_SIZING -- the strawberry planting count (for review; biggest own-money gain of the O line)

Following the allocation matrix (tapes: same ~250 strawberry units from 33 plantings; O16: 47). The seed allocator
sizes strawberry plantings as demand_pool / CROP_SPECS["STRAWBERRY"]["units"] with units = 4.5, but the farm actually
gets 5.5-7.5 units per planting, so it over-plants by ~40%: 47 plantings, 800 actions, $7k seed, and the extra volume
depresses its own strawberry price ($89 vs the tapes' $108). O24 = O22 with `STRAW_UNITS = 7.5` (new top-level const so
the loop can tune it). Effect (yangk, seeds 11-14): plantings 47 -> 31, units 258 -> 195, strawberry price $89 -> $111,
seed -$1.6k, 222 labour-hours freed (-> wheat +12, carrot +6, melon +2 plantings), labour+land -$1.3k. Fixed shops:

| vs | seeds | margin | own money |
|---|---|---|---|
| O22 | 11-30 | +5,826 (t14) | +5,483 (t10), all 5 positive |
| O22 | 31-50 | | +4,736 (t8.8) |
| O15 (ladder entry) | 11-30 | **+7,271 (t12.3)** | **+5,953 (t9.3)**, every tape +5.0-7.6k |
| O15 | 31-50 | **+8,918 (t13.8)** | |

Sweep of STRAW_UNITS (own vs O22, s11-30): 6.0 +3.5k, 7.5 +5.5k, 9.0 +3.3k, 12.0 +1.7k, 20.0 -0.9k -> optimum at the
true yield per planting (an accurate self-model, not a hold-back). `submissions/O24_STRAW_SIZING.zip` (contains O22).

Also read, and set aside: `O23_FERT_COURIER` (phase rule + free units fetch fertilizer + fertilizer excluded from the
"cargo to deposit" count -- PRODUCTS includes FERTILIZER, so units carrying >=3 fert walked it straight back to the
shed; fixed, coverage 1.9 -> 2.7 fertilized nights/planting) raises units/planting to 6.3 but own money is +0 (margin
+1.3k): strawberry volume is demand-limited; the courier is worth revisiting only as a way to cut plantings further.

## Sep 11: wheat line closed at knob level (third time); O25 = O24 + H_GATE144

Remaining matrix gaps after O24 (yangk, s11-14): purchases 25.6k vs 18.7k (wheat: we buy 260 u/$10k, sell 144 at $41 --
a daily round-trip because `reserve_feed` keeps one day of feed; tape grows 515 and buys 111), labour+land 11.3k vs 8.0k,
melon price $175 vs $219. Own-money panel vs O24 (fixed shops, s11-20 / s21-40):
- wheat_sell_price 40/45/50 (stop selling feed wheat): own **+1.45k (t4.5) / +1.24k / +0.76k**, but margin panel **-635**
  and h2h -2.1k..-3.3k (4-16): the tapes are net wheat SELLERS (287 u), so our withheld supply raises the price they get
  by more than it saves us. Own gate passes, margin gate fails -> rejected. (Mirror image of the price-attack case.)
- wheat_per_animal 0.5/1.0, wheat_tiles 8 (grow feed): own +0.2..+0.7k (t<1.2), h2h -4.2..-4.6k (0-10). Closed.
- wheat_hold_days 2-3 / wheat_stock 10: own +0.4-0.5k (t0.9). Null.

**O25_STRAW_HIREGATE** = O24 + `HIRE_MAX_MARGINAL = 144` in `_hire_plan` (the other session's H_GATE144). vs O24: own
+1,568 (t12.4, s11-30) / +1,352 (t11.2, s31-50), margin +1,397 (t9.5), all 5 positive. **vs O15: margin +8,669 (t14.6),
own +7,522 (t11.9), every tape +6.5-9.0k.** `submissions/O25_STRAW_HIREGATE.zip`. Lineage: O15 + orchestrator (O16) +
melon convoy (O22) + strawberry sizing (O24) + hire gate (O25); each step passed both gates.

## Sep 11: crop self-model sweep on O25 (own-money panel vs O25, fixed shops)

The allocator's `CROP_SPECS[c]["units"]` (expected sellable units per planting) vs measured: STRAWBERRY 4.5 vs 5.5-7.5,
WHEAT 5.0 vs 3.9, CARROT 4.0 vs 3.0, MELON 6.0 vs 5.9, TOMATO 5.0 (never planted).
- STRAW_UNITS 6.5 / 7.5 / 8.5: -0.8k / 0 / -0.2k -> 7.5 stays.
- WHEAT 5.0 -> 3.9 (true): **-2.0k (t-7.5)** -- plants more wheat, loses. Not applied (wheat line: fourth negative read).
- CARROT 4.0 -> 3.0 (true): own **+1.6k (t2.6, s11-20) / +1.4k (t4.6, s21-40)**; margin +0.8k / +0.2k / +1.5k (s11-30/31-50/51-70),
  real tapes >= 0 on all sets (peter +2-4k, bahaen +2k, alaylm +0.3-0.6k, yangk -0.1..+0.8k), clone -0.1..-3.4k. Mechanism:
  with true units the carrot `val < min_val` test fails more often, carrots drop 34 -> 12 plantings and the labour goes to
  wheat (64 -> 90 plantings; wheat bought 260 -> 203), labour+land 11.3k -> 8.5k. Adopted as **O26_CARROT_SIZING**
  (`submissions/O26_CARROT_SIZING.zip`) -- weakest gate pass of the line; margin is real-tape-only.
Rule of thumb from the day: an accurate self-model (units per planting) beats both optimism and pessimism, but only
where the freed resource has a paying use; the allocator then decides.

## Sep 11: melon remainder closed (O26 standing: own money 102-107k vs yangk 111k, bahaen 89k, alaylm 100k, s11-14)

Remaining melon gap ($175 vs $221) = 2-4 tiles one watering short of 6 units on d10 morning (harvested h15-23, sold at
the d11/d12 dump) + the second melon wave (d20-21, sold at $63-134 into an empty pool). Reads vs O26, fixed shops:
- O27_MELON_WATER_FIRST (convoy waters 5-unit tiles then harvests): own -94, **margin -1,792 (t-4.1), h2h -4.1k (1-19)**. Rejected.
- MELON cutoff 16 -> 8 (no second wave): own -1,176 (t-4.2). The late wave pays despite the price. Rejected.
- harvest at 5 units in the convoy: own -608. Rejected.
Melon line is closed at this level; what is left there is the tape's ordering of animals after melons on d10, which we
cannot copy without losing feeds (O16 runs 12-16 animals on d10).
