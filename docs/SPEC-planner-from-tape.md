# SPEC — Teaching the day-planner from the tapes (addendum 2 to SPEC-day-planner-executor.md)

Status: design, ready to implement. Written for Codex/Sonnet. Everything here uses only files under `/Users/graceliu/Claude/Projects/Kaggriculture`; do not read the other Kaggriculture folders. Python 3.10+, no installs.

## 0. What this fixes

`docs/planner-results.md`: P meets the routing target (1.16 travel/work action) but loses −$44k to E1 with 469 missed waters, 38 weeds, 41% idle turns. Its failures are *coverage* failures, and today they are diagnosed from whole-game aggregates. We have something far better: every frontier tape is a 720-step expert trajectory that reproduces exactly, with per-step cash, shed, hand positions and actions. This addendum turns those trajectories into (a) a per-hand, per-hour diff, (b) a deterministic per-day planner test that needs no full games, and (c) fitted constants for hiring and bundling. The M2 opening switch is ported separately (§6) because it lives in the decision layer and doesn't depend on the executor.

Why this doesn't make the planner a tape: a tape is `f(step)`; the planner is `f(state)`. The tests below fix the value of `f` on 30 real daily states so that it is also sensible on states the tape never saw. Overfitting guard: §4.3.

## 1. Inputs

- Tapes: `candidates/H32.py` (our full tape; use this as the primary expert, it is the best-scoring stream), `Opponents/tape_yuan800_104892947.py`, `Opponents/tape_atakan_104893687.py`, `Opponents/tape_strawhats_105080848.py`. All expose `_TAPE` (or `_ACTIONS`): a list of per-step `{"farmer": [...], "hands": [[...],...], "market": [...]}`.
- Runner: `mini_engine.py` (`run_game`, `load_agent`). Wrap an agent to record per-step observations — pattern in `tools/sell_shift.py::shed_trace` (monkeypatch `mini_engine.load_agent` so the sentinel path returns the wrapped function). Record for seat 0: `obs["farms"][0]` (tiles, money, farmer, hands), `obs["private"]` (shed, inventories, seeds), `obs["market"]`, `obs["town"]`, plus the action the tape returned. Use a benign opponent (`candidates/V3_12.py`) so the expert's trajectory is uncontested, and seed 1; then seeds 2–3 for §4.3.
- Engine facts: SPEC-day-planner-executor.md §1 (verified). Chore vocabulary: its §3–§4.

## 2. Tool 1 — `tools/tape_days.py`: expert trajectory → per-day chore ledger

```
python3 tools/tape_days.py candidates/H32.py --seed 1 --out evolve/expert/H32_s1/
```

For each day d writes `day_{d:02d}.json`:

```
{
  "day": d,
  "state_h0": <obs at hour 0, seat 0, verbatim>,
  "hands_hired": [(hour, n_hired_this_hour)],             # from market HIRE orders
  "actions": {unit_index: [(hour, pos_before, action, chore_id|null), ... 24 entries]},
  "chores_done": {chore_id: (hour, unit_index)},            # first completion
  "chores_available_h0": [chore_id,...],                    # what enumerate_chores(state_h0) returns (see §3)
  "market": [(hour, order), ...],
  "money": [24 values], "shed": [24 dicts],
  "eod": {"escaped": n, "new_weeds": n, "unfed": n, "unwatered_plants": n}
}
```

`chore_id` classification of an action, given the unit's position and the tile there: `WATER`→`water:x,y`, `FEED`→`feed:x,y`, `CARE`→`care:x,y`, `HARVEST` on plant→`harvest:x,y`, on animal→`harvest_animal:x,y`, `COLLECT_FERTILIZER`→`collect:x,y`, `PLANT c`→`plant:x,y`, `DIG`→`dig:x,y`, `FERTILIZE`→`fertilize:x,y`, `PICKUP/DROP/PLACE/BUILD_*`→`shed:`/`place:` (logistics, not chores), moves→null. An action counts as done only if the engine applied it: compare the tile/inventory before and after the step (e.g. `watered_today` flipped, animal `fed_today` flipped, plant removed on harvest). Record attempted-but-failed actions separately in `"failed": [(hour, unit, action, reason)]` — the tape has some (feed with no wheat carried); the count is part of the ground truth.

Also write `summary.json`: per day, hands, chores done by kind, moves, moves/work action, idle turns, failed actions, hires and their cost, money at h0/h23.

## 3. Tool 2 — `tools/planner_bench.py`: per-day planner test without full games

The planner blocks (`evolve/blocks/planner_*.py`) expose `enumerate_chores(obs, v, day, hour)` and `plan_day(chores, units, hour, shed)` (spec §4, §6). This bench calls them directly on `state_h0` of each ledger day and executes the resulting plan **in a copy of the engine for that one day** — 24 steps, then stop — using the engine's own `interpreter` on a two-player state where seat 1 is `PASS`. Steps:

1. Build the engine state from `state_h0` (structify; seat 1 gets an empty farm copy; market/town from the snapshot). Helper: `mini_engine.load_engine("master")`.
2. Hires: the bench issues the same HIRE orders the tape did that day (`hands_hired`), so hand count is controlled; §5 tests hiring separately.
3. Run the candidate agent for 24 steps from this state (the block-rendered agent, `S` reset). Record the same ledger fields.
4. Score the day:
   - `coverage_hard` = hard chores (spec §4 table) done by P ÷ done by the tape, on the tape's `chores_available_h0` ∩ hard.
   - `coverage_all` likewise for all chores.
   - `travel` = moves ÷ work actions. `idle` = PASS or blocked turns ÷ unit-turns.
   - `eod` deltas: escaped, new weeds, unfed, unwatered (P minus tape).
   - `failed` actions count.
5. Print one row per day and a total; exit non-zero if any day has `coverage_hard < 0.95` or `new_weeds > tape`.

A full bench run is 30 × 24 steps ≈ 1 game's cost — seconds. Run it after every planner change before any full game.

## 4. What to fix, in order (each has a bench target)

### 4.1 Coverage on the tape's states (target: `coverage_hard ≥ 0.95` on all 30 days, `new_weeds ≤ tape`)
The results doc names the causes; the ledger localizes them:
- Days where P's `chores_done` is missing chores the tape did → print the missing ids with tile state. Expect two clusters: same-day water after plant (spec §4 row "plant"), and survival water on ongoing crops (`consecutive_unwatered == 1`) — P currently skips these as "optional".
- Replan: spec §7 says replan when a route empties while unassigned chores remain. Not implemented (results doc). Implement as: at any hour, a unit whose route is empty takes the nearest unassigned chore whose deadline is still reachable (insertion cost from its position). Deterministic tie-break `(cost, pos)`.
- Bundles: the tape does feed+care+collect+harvest on one animal tile in consecutive hours by one hand. Enforce: an animal tile's chores are one bundle assigned to one route (bundle cost = walk + k actions). Verify with the ledger: count animal tiles visited by >1 unit per day (tape ≈ 0).
- Pickup accounting: reserve carried WHEAT per route at plan time; a feed stop with no wheat reserved is invalid at plan time, not at execution.

### 4.2 Hiring fitted to the expert (target: P's hand count within ±1 of the tape's each day, hire cost within 20%)
From `summary.json` fit `hands_needed(day)` ≈ ceil(hard_chores × a + optional_chores × b) with (a, b) least-squares on the 30 days of H32_s1, subject to the hire-cost (fib) and cash constraints. Expect ≈ 8–10 planned actions per hand-day (results doc guessed 10). Report the fit and the residuals; put (a, b) in the hiring block as constants.

### 4.3 Overfitting guard (target: no regression)
Repeat the bench on three other state sources: H32 on seeds 2–3 (different shops/weeds), E1's own daily states (`tools/tape_days.py candidates/E1.py`), and perturbed H32 states (delete 3 random plants, add 2 weeds, remove one hand — deterministic seed). P must not lose coverage on E1's states relative to E1 itself, and must recover from the perturbations (no escape, weeds dug within the day if idle capacity exists).

### 4.4 Full games (only after 4.1–4.3 pass)
The acceptance ladder in `docs/PROMPT-codex-planner-blocks.md` §"Acceptance ladder" steps 3–5, unchanged: sanity floor vs E1 (seeds 1–10), the coupled scale test, held-out 11–30 vs E1/V3_12/three tapes.

## 5. Deliverables

1. `tools/tape_days.py`, `tools/planner_bench.py`, `evolve/expert/` (ledgers for H32 s1–3 and E1 s1; gitignore nothing — they're small JSON).
2. Updated `evolve/blocks/planner_*.py` with the fixes in §4.1–4.2.
3. `docs/planner-results.md` appended: the bench table before/after per fix, the hiring fit, the §4.3 tables, then §4.4 if reached. If a fix regresses the bench and the cause isn't found in two rounds, leave it out and say so.

## 6. Separately: port the M2 opening switch to the K chassis

`candidates/M2.py::_m2_class` reads `obs["market"]["inventory"]["WHEAT"]` at step 1 and infers the opponent's turn-0 wheat purchase. Add to K.py `economy()` a knob `open_roundtrip=(n, m_big, m_mid, m_other)` (default None = off): at step 0 `BUY_PRODUCT WHEAT n`; at step 1 `SELL WHEAT m_class` placed *before* the opening's animal/seed buys and *after* HIRE orders (engine processes HIRE first anyway). Then grid n ∈ {20,30,40}, m ∈ n−{4,6,8,10,12} vs the three cluster tapes on seeds 1–6 both seats (`docs/opening-grid-sep04.txt` is the H32-chassis result to compare against; the interaction depends on our own day-1 cash, which differs on C1/E1). Keep it only if some row is ≥ +$20k on a cluster tape with no row < −$2k elsewhere. This is independent of §2–§5 and can run first.

## 7. Rules

Same as the planner brief: work on branch `codex/planner-tape`, don't touch `vendor/`, `candidates/K.py` except for §6, `evolve/chassis.py`, `evolve/space.py`, `RULES.md`. Bench before games. Two debugging rounds per regression, then write it up and stop.
