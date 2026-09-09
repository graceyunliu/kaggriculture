# P8 — Reactive Allocation Policy on the P6 Executor

Status label convention (this project's existing convention, per RNG_PATH_DEPENDENCE_AUDIT):
**DIRECTLY_OBSERVED** = read straight off code or an engine run with no inference.
**SUPPORTED** = inferred from multiple directly-observed data points.
**PLAUSIBLE** = a reasonable read that wasn't independently confirmed.
**UNRESOLVED** = open question, flagged rather than guessed at.

## 0. Repo-state caveat (UNRESOLVED, load-bearing for everything below)

This working tree is in a partially-recovered git state (`git status` shows ~1,680
files as staged-added-but-missing-from-disk, an artifact of an earlier interrupted
`git reset` — see the user's own memory note "Kaggriculture git reset recovery +
branch consolidation"). `candidates/`, `experiments/RNG_PATH_DEPENDENCE_AUDIT/`,
and `Opponents/opp_scenario_v14.py` did not exist on disk at the start of this task;
they were restored read-only from the git index (`git show :<path>`, `git
checkout-index`) without touching the broken index/lock, so nothing about the
recovery mutated tracked state. **DIRECTLY_OBSERVED**: `candidates/P6_baseline.py`
and `candidates/P7b.py` were both added in one commit titled "Recover K chassis and
P7b region assignment work" (`3066a32`), and `P6_baseline.py`'s own first two lines
read `# evolve/chassis.py -- frozen copy of candidates/K.py with typed mutation
blocks.` — i.e. the file present in the repo under the name `P6_baseline.py` is,
by its own header comment, a copy of the K/V3.12 knob-chassis, not a literal
implementation of the `Chore`/`Route`/`plan_day()` planner data model described in
`docs/SPEC-day-planner-executor.md`. **UNRESOLVED**: whether a truer P6 (with the
spec's explicit chore-enumeration/route-planning objects) exists elsewhere and was
simply not recovered by that commit, or whether "P6" in this repo's history always
referred to this knob-chassis-plus-dispatcher file. This report proceeds with
`candidates/P6_baseline.py` as "P6" per the task's own instruction ("search
candidates/ for P6/P7b-named files") because it is the only P6-named artifact that
exists, runs cleanly, and matches the spec's description at the level that matters
for this task (a working per-hour executor with a separable allocation layer) —
but the exact match to the SPEC.md is caveated, not asserted.

## 1. What P6 (`candidates/P6_baseline.py`) actually does — DIRECTLY_OBSERVED

Reading the file's own function list: `perceive`, `_build_route`, `_route_step`,
`_build_sweep`, `_crop_step`, `_steal_task`, `_unit_action`, `_setup_step` implement
per-hour movement + task dispatch (the executor). `economy()` — a single ~270-line
function — implements hiring (`_load_model`), sell timing, herd purchases, crop/seed
mix, and land purchases (the allocation policy). So P6 is **not** allocation-free;
it already has an allocation layer. The concrete gap, read directly out of that
function:

1. **Every allocation threshold is a fixed constant** in a module-level `KNOBS` dict
   (`min_hands=3`, `load_per_hand=20`, `melon_floor=200`, `wheat_sell_price=30`,
   `max_animals=20`, `wheat_tiles=0`, ...) — tuned once, offline, against a fixed
   opening and a fixed opponent tape, and never re-derived from the game state the
   agent is actually in.
2. **The herd-purchase section reads the opponent's board directly**:
   `economy()`, "---- herd" section, builds `opp_counts` by iterating
   `obs["farms"][1 - p]["tiles"]` and counting the opponent's COW/SHEEP tiles, then
   folds that into its own animal-purchase decision via `_demand_room(...,
   opp_count)`. This is genuine opponent-state reads, not just self-state — which
   this task's hard rule ("no opponent fingerprinting") explicitly forbids reusing
   as-is.
3. Land purchases are gated by a **day-deadline table** (`LAND_DEADLINE = {2: 14, 3:
   17, 4: 18}`) rather than by how full the existing land actually is.

## 2. P8's reactive allocation rules — SUPPORTED (design tied to §1's findings)

`candidates/P8_reactive_allocation.py` imports `candidates/P6_baseline.py` by file
path at runtime (`importlib.util.spec_from_file_location`) and reuses its executor
functions (`perceive`, `_unit_action`, `_crop_pools`, `_hire_plan`, `_fib`) and pure
game-rule constants (`CROP_SPECS`, `ANIMALS`, `LAND_PRICES`, `MAX_HANDS`, `I0`, ...)
unchanged. `candidates/P6_baseline.py` itself is not edited. P8 replaces
`economy()` with a function that reads only: own cash, own land occupancy (fraction
of unlocked tiles non-empty), own herd-per-hand ratio, a live labor-load signal
(same load units P6 already computes: `LOAD_CROP_TASK`x pending chores +
`LOAD_ANIMAL`x active animals), and the shared market's price/inventory (public to
both players, not opponent-specific). No code path reads `obs["farms"][1 - p]`.

- **R1 Hiring** — target hands = `ceil(pending_load / LOAD_PER_HAND)`, clamped
  `[3, MAX_HANDS]` (`6` after day 29). Directly proportional to the live chore-load
  signal instead of P6's fixed `min_hands`/`load_per_hand` pair.
- **R2 Land** — buy the next quadrant once own tile occupancy >= `OCC_HIGH` (0.65)
  and cash covers price + a cash buffer; replaces P6's day-deadline table with a
  fullness trigger.
- **R3 Herd** — grow COW/SHEEP while herd-per-hand ratio < `HERD_RATIO_CAP` (1.1)
  and the item's own market price is at/above a floor (own-market signal, no
  opponent count read at all — this is the direct fix for §1.2).
- **R4 Crop mix** — same greedy value/cycle ranking P6 uses over the shared market
  (kept: it is a pure self+market calculation), but seed purchases are gated by
  whether the reactive hiring target (R1) has room left (`target_hands < MAX_HANDS`)
  instead of P6's fixed `min_hands` floor.
- **R5 Sell timing** — sell WHEAT/MELON once market price clears a floor expressed
  as a fraction of the item's own base price, or unconditionally once own shed
  occupancy is high (overflow risk, self-state) — same mechanism as P6's
  `melon_floor`/`wheat_sell_price` constants but expressed relative to the item's
  own price scale rather than as an absolute dollar figure.

Day-0/hour-0 is the one unavoidable fixed opening (there is no observed state yet
on turn 0); every subsequent hour is state-conditioned. No day-N branch after that
is copied from a specific opponent tape.

## 3. Build-time debugging — DIRECTLY_OBSERVED

The first working version of R1 pinned hands at a constant 3 for the entire game
(confirmed via a per-day `hands_eod` trace field: `[3, 3, 3, ..., 3]`), because the
hiring target formula floored `ceil(load/load_per_hand)` below the day's actual
hand count whenever `load_per_hand` was tuned too high relative to early-game chore
counts — a self-reinforcing "never grows" trap. Fixed by lowering `LOAD_PER_HAND`
and making the target purely load-proportional instead of hysteresis-based
(`n_hands +/- 1`), which had produced the opposite failure (runaway hiring to
`MAX_HANDS` by day 1 regardless of whether the load justified it). Two further bugs
found the same way: R4's labor throttle read `n_hands` at hour 0 — before that
day's HIRE orders land, hands are re-hired from 0 every day per the engine's own
rule — so it always saw "0 hands, infinitely busy" and permanently blocked further
planting; fixed by gating on the day's *target* hand count instead of the
instantaneous (pre-hire) count. R3's herd-room formula (`(I0 - inventory) x
demand_share`) returned ~0 the whole early game because market inventory for
MILK/WOOL sits near its `I0` ceiling until products actually start flowing (~day
6-8), so the herd never grew past its day-0 opening pair; replaced with a
price-floor check on the item's own market price. These are documented so the
numbers below are read against a policy that runs (0 agent errors / 0 GUARD prints
across every seed run, `mini_engine.py` seeds 1-25 both seats), not one still
silently broken.

## 4. Evaluation methodology — DIRECTLY_OBSERVED

All numbers below come from `experiments/RNG_PATH_DEPENDENCE_AUDIT/eval_protocol.py`
`compare_paired()` (common-random-numbers design: both arms of a comparison face
the identical fixed third-party opponent on the identical seed) run through
`mini_engine.py` against the real vendored engine
(`vendor/kaggle_environments_engine_master/kaggriculture.py`, `--engine master`),
`--both-seats`. No synthetic stand-in, no single-trajectory claim. Every
`compare_paired()` run below flags `trajectory_diverged=True` on effectively every
game — this is the RNG path-dependence mechanism the audit already characterized
(policy-dependent board occupancy shifts the same-day shop-unlock draw); it means a
given seed's exact dollar delta is not by itself a clean causal isolate, but with
n=40 paired games and a large, consistent-sign mean delta (see below), the
direction of the result is not plausibly explained by that confound alone — the
audit's own finding was that RNG-path effects are present but small relative to
big, decisive strategy gaps (see the RNG path-dependence audit memory note: "caveat
any day-14-divergence causal claim", which is a caveat on *attribution to a
specific mechanism*, not on whether the sign of a $50k/game gap is real).

## 5. Results — DIRECTLY_OBSERVED

**P8 vs P6-as-is** (common opponent `Opponents/opp_scenario_v14.py`, seeds 1-20,
both seats, n=40 paired games):
mean delta **-$48,450/game**, stdev $35,634, **t = -8.60**, wins 3 / losses 37 / ties 0.

**P8 vs C1** (strongest real baseline candidate found in this repo's working
tree/git index — see §6; same opponent, seeds, both-seats, n=40):
mean delta **-$50,496/game**, stdev $39,629, **t = -8.06**, wins 7 / losses 33 / ties 0.

**P8 vs opp_scenario_v14 directly** (`mini_engine.py --both-seats`, seeds 1-5, n=10
games): P8 mean $39,930, opponent mean $79,706, margin **-$39,776/game**, t=-5.51,
seed-wins 0-5.

Sample sizes are the actual number of games run in this session (40 + 40 + 10 = 90
games total across the three comparisons), not extrapolated. Runtime was ~50s per
20-seed/both-seats `compare_paired()` call, well inside the 10-15 minute budget, so
sample size was capped by task scope/time rather than engine speed — a further
100+ seeds could be run cheaply if this line of work continues.

## 6. Baseline-candidate note — DIRECTLY_OBSERVED

`candidates/` (as recovered into this working tree) contains: `C1.py`, `V3_12.py`,
`P5.py`, `P6_baseline.py`, `P7b.py`, `M2.py`, plus H-series files. Per the repo's
own memory notes, `H32`/`M2` post-date `C1`/`H10` and claim larger margins, but
those margins are documented as opponent-fingerprinting exploits ("M2 picks turn-1
sell from opponent's exact turn-0 buy") explicitly excluded by this task's hard
rule against opponent-tape replay/fingerprinting; `V3_12` is described elsewhere as
the frontier for the actual ladder engine config. `C1.py` was used as "the strongest
real baseline candidate" here because it is a general (non-opponent-fingerprinting)
policy with a documented track record in this repo (memory: "+$12.7k/$4.8k vs
V3.11/V3.12") and loaded/ran cleanly. This choice is **PLAUSIBLE** rather than
exhaustively verified against every candidate file in the repo's full history —
time budget did not allow re-benchmarking the entire candidate lineage.

## 7. Verdict

**REJECTED.** P8's reactive allocation policy loses decisively and consistently to
both P6-as-is and C1 across 40 paired games each (t ~ -8, well past any reasonable
significance bar, 3/40 and 7/40 win rates respectively), and to the real opponent
directly (0/5 seed-wins). The loss is not a rounding/noise result — it is large,
one-sided, and reproduced across seat swaps and multiple independent seeds.

Root cause, read off the per-day traces gathered during debugging (§3): P8's
reactive thresholds under-invest relative to P6/C1's tuned constants across the
whole game — land stays at 1-2 unlocked quadrants for most of the game where P6/C1
reach 3-4, and the herd-vs-crop labor split oscillates (crop tile count collapses
toward 0 by mid-game in at least one traced seed once herd purchases saturate the
reactive hand-count cap) rather than settling into the balanced allocation P6's
hand-tuned knobs encode. The general design direction (drop opponent-tile reads
from the herd rule; make hiring/land/sell thresholds state-proportional rather than
day-indexed constants) is still defensible on the grounds laid out in §1 and §2,
but this specific threshold set does not close the gap to either baseline and
should not go to the ladder as-is. **NEEDS_MORE_WORK** would apply to the general
approach; **REJECTED** applies to this specific implementation as evaluated.

## Files

- `candidates/P8_reactive_allocation.py` — the new candidate (imports
  `candidates/P6_baseline.py` unchanged; does not edit it).
- This report: `artifacts/reactive_allocation_p8/REPORT.md`.
