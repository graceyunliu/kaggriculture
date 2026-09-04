# SPEC — Day-planner executor for the K chassis (candidate "P1")

Status: design, ready to implement. Target: `candidates/K.py` (copy to `candidates/P.py` first; keep K.py as the control). Written so a smaller model can implement it mechanically and verify with the existing tools. Every number below is engine-verified against `vendor/kaggle_environments_engine_master/kaggriculture.py`.

## 0. Why (one paragraph)

The current dispatcher assigns each worker the nearest pending chore every hour (routes of ≤3 animal stops, crop "sweeps" of ≤6 nearby tiles, rebuilt hourly, no daily plan). When chores exceed what nearest-first can reach, the remainder silently doesn't happen — nobody counts it. Every economy lever that adds chores (12 melons, wheat tiles, a bigger herd, fertilizing) has lost on this dispatcher for that reason (see `docs/candidates-C1-H10-sep03.md`). The frontier tape services 12 melons + 5 new wheat tiles/day + 8–13 animals with 5–11 workers and misses nothing. P1 replaces nearest-first with a plan made at hour 0 for the whole day, sized so every chore fits, and hires exactly enough workers to make it fit.

## 1. Engine facts the planner relies on (do not re-derive; these are checked)

- 24 turns/day, 30 days, 720 steps. `obs["day"]`, `obs["hour"]`. Board 10×10; NW quadrant unlocked at start; land unlocks NE ($1000), SW ($2000), SE ($4000) in that order.
- **Workers.** Farmer (unit 0) persists; hands are hired per day (`HIRE` market order, cost = fib(n-th hire today): $1,1,2,3,5,8,13,21,34,55,89,144…), spawn on a shed-access tile, and are dismissed at end of day with their inventories auto-dropped into the shed (capacity 100 total units; overflow is destroyed). Hire orders placed at hour h produce hands at hour h+1. Max 10 market orders per turn.
- **Shed access tiles**: (4,4), (5,4), (4,5), (5,5); three start LOCKED but a unit may still stand on them for shed ops. `PICKUP item n` / `DROP` (drops *everything* carried) / `PLACE item n` (product deposit) require standing on one.
- **Movement**: one orthogonal step per turn. Manhattan distance = turns.
- **Crops.** `PLANT crop` on an empty owned tile (seeds bought via `BUY_SEED`). A plant not watered for 2 consecutive days becomes a WEED (planting day counts as unwatered day 1 → **must be watered the day it is planted or the next day**, and then every other day at minimum to survive). `WATER` once per tile per day.
  - One-time crops (WHEAT 2–4, CARROT 2–3, MELON first 10 / max 12): `yield_units` starts at 1; each watering on a day with `window_start ≤ age ≤ max_yield_day` (window_start = (max_yield_day+1)//2, so WHEAT 2–4, CARROT 2–3, MELON 6–12) adds +1 (+2 if fertilized), capped at max_yield (WHEAT 6, CARROT 4, MELON 6). `HARVEST` allowed once `age ≥ first_yield_day`; it takes all units and clears the tile. MELON reaches 6 units by day 10 only if watered on all of days 6,7,8,9,10 (or fewer with fertilizer).
  - Ongoing crops (STRAWBERRY first 10, interval 2, 4 productions; TOMATO first 8, interval 1, 4 productions): at end of day, if `days_since_first % interval == 0`, +1 unit (+2 if watered that day and fertilized). Watering is only needed for survival (every other day) and for the fertilizer bonus; it does not add units otherwise.
  - `FERTILIZE` consumes 1 carried FERTILIZER; active for day, day+1, day+2.
- **Animals.** Bought via `BUY_ANIMAL` → shed; a unit must `PICKUP` it, walk to an empty tile, `BUILD_PASTURE` (COW/SHEEP) or `BUILD_COOP` (GOOSE), then `PLACE`. Each day an animal needs `FEED` (consumes 1 carried WHEAT) and `CARE` (no item). Unfed 2 consecutive days → animal escapes (lost). Products: COW milk every 2 days from day 8 after placement, SHEEP wool every 3 days from day 6, GOOSE egg daily from day 4; `HARVEST` on the tile takes them. `COLLECT_FERTILIZER` when `fertilizer_available`.
- **Market**: `SELL item n` sells from the shed only (not from carried inventory). Prices move with shared inventory; first seller gets the higher price.

## 2. Scope: what changes, what stays

Keep unchanged: `economy()` (opening, herd/seed/land purchases, selling, feed buying — with two small hooks below), `_setup_step` (animal install), `_fert_eligible`, the endgame deposit rule (day ≥ 28), the crash guard.

Replace: `_build_route`, `_route_step`, `_build_sweep`, `_crop_step`, `_crop_pools`, the "steal tail task" logic, `S["routes"]`, `S["sweep"]`, `S["wheat_budget"]`, and steps 3, 5, 6 of `_unit_action`. Replace `_load_model` (hiring) with the planner's headcount.

## 3. Data model

```
Chore = {
  "id": str,            # e.g. "water:3,7", "feed:2,2", "care:2,2", "harvest:3,7", "plant:4,1", "collect:2,2", "dig:6,6"
  "kind": str,          # water | feed | care | harvest_crop | harvest_animal | collect | plant | dig | fertilize
  "pos": (x, y),
  "deadline": int,      # last hour today by which it must be done (23 = end of day); hard chores have priority
  "value": float,       # $ estimate of doing it today (see §5)
  "needs": str|None,    # "WHEAT" (feed), "FERTILIZER" (fertilize), or a crop name (plant) — must be carried
  "hard": bool,         # True = survival/yield-critical (urgent water, feed, in-window melon water)
}
Route = {"unit": i, "stops": [Chore,...], "pickup": {"WHEAT": n, "FERTILIZER": n, "SEED:MELON": n, ...}, "eta_end": hour}
S["plan"] = {"day": d, "routes": {unit_index: Route}, "unassigned": [Chore], "chore_done": set(ids)}
```

Chore ids are position-based so they survive re-perception. Hands are re-indexed daily (0 = farmer, 1..n = hands in `me["hands"]` order); hands hired mid-morning append to the end.

## 4. Chore enumeration — `enumerate_chores(obs, v, day, hour)`

Run at hour 0 (after the economy's hour-0 orders are known) and on every replan (§7). Produce, for each tile:

| tile state | chore(s) | deadline | hard |
|---|---|---|---|
| plant, `consecutive_unwatered ≥ 1`, not watered today | water | 23 | yes |
| one-time crop in its water window, `yield_units < max`, not watered today | water | 23 | yes for MELON days 6–10; else no |
| ongoing crop fertilized (`fertilized_until_day ≥ day`), not watered today | water | 23 | no |
| ongoing crop, not watered today, no other reason | none (skip; it survives one unwatered day) — **exception**: if tomorrow would be its 2nd unwatered day, water = hard | | |
| crop `_harvest_ready` (existing rule; keep `melon_rush` option: MELON age ≥ 10 and units ≥ 5) | harvest_crop | 23 (MELON: 12 → sell same day) | no |
| crop fert-eligible and fertilizer available (shed or carried) | fertilize (needs FERTILIZER) | 23 | no |
| animal not fed today | feed (needs WHEAT) | 23 | yes |
| animal not cared today (day < 28) | care | 23 | no (but cheap; bundle with feed) |
| animal `fertilizer_available` | collect | 23 | no |
| animal `yield_units > 0` | harvest_animal | 23 | no |
| weed | dig | 23 | no |
| empty tile and seeds in hand | plant (needs SEED:crop, chosen by existing `_plant_choice`) | 21 (must be watered same day → creates a hard water chore on completion) | no |

Values (§5) are used only to *order* optional chores and to decide headcount; hard chores are always scheduled first.

## 5. Chore values (rough is fine; used for ordering and the hire decision)

- feed/care an animal: product price × units per day ≈ COW $milk/2, SHEEP $wool/3, GOOSE $egg; plus fertilizer $fert per day. Use live `obs["market"]["prices"]`.
- water one-time crop in window: (price × 1 unit) — MELON ≈ $200, WHEAT ≈ $40, CARROT ≈ $40. Fertilized: ×2.
- water survival: value of the whole remaining tile (≥ $300 for strawberry/melon) — hard anyway.
- harvest: units × price (MELON at day 10: units × price; delayed a day costs ≈ 25% of price).
- plant: crop value / cycle (existing `CROP_SPECS` val).
- dig weed: $10 (frees a tile).
- collect: fertilizer price.

## 6. Planner — `plan_day(chores, units, hour, shed)`

Goal: assign every hard chore and as many optional chores as possible to routes that finish by their deadlines, minimizing walking. Simple, deterministic, fast (< 50 ms):

1. **Seed routes.** Every unit starts at its current position (hour 0: all on shed tiles). Each route begins with a pickup step if it will need items (computed after assignment; see 4 below).
2. **Assign hard chores first**, in order of deadline then value, each to the unit with the smallest *insertion cost* (extra walking when inserted at the best position in its current stop list), subject to `eta_end ≤ deadline`. ETA = current hour + Σ(steps between stops + 1 action per stop) (+ pickup detour if needed).
3. **Then optional chores** by value/cost ratio, same insertion rule, while `eta_end ≤ 23`.
4. **Pickups.** For each route: WHEAT needed = number of feed stops; FERTILIZER = fertilize stops; SEED:crop = plant stops. If the unit is not on a shed tile, prepend a shed visit (cost = distance). Cap wheat pickups by shed stock; unfilled feed stops go back to the unassigned pool (a second route may pick them up after the morning wheat order lands at hour 1 — see §7).
5. **Route ordering**: after assignment, 2-opt each route (cheap: routes are ≤ ~12 stops).
6. Return routes + `unassigned` (chores that didn't fit).

Headcount: `hands_needed(chores)` = smallest N such that running steps 1–3 with N units leaves no *hard* chore unassigned and the total unassigned optional value < $150. Try N = current hands … 13. Cost of the N-th hand is fib; accept while marginal value assigned > 3 × marginal hire cost. This replaces `_load_model`; `economy()` calls it at hour 0 (and 1–2 for top-ups) to emit HIRE orders. Minimum 3 hands days 0–2 (the opening's own labor), never fewer than hard chores / 8.

## 7. Execution — `unit_action_planned(i, pos, carry, ...)`

Order of precedence per unit per hour:

1. Carrying an animal → `_setup_step` (unchanged).
2. Day ≥ 28 endgame deposit rule (unchanged).
3. Route step: if the route has a pending pickup and the unit is on a shed tile → `PICKUP`; else walk to the shed. Otherwise take the first stop: if not on it, step toward it; if on it, do the action (`WATER`/`FEED`/`CARE`/`HARVEST`/`COLLECT_FERTILIZER`/`FERTILIZE`/`DIG`/`PLANT crop`), mark the chore id done, pop it. A `plant` completion appends `water:pos` (hard, deadline 23) to the same route's front.
4. Route empty → if `unassigned` non-empty, take the cheapest reachable one (insertion cost, deadline respected); else if carrying ≥ 4 products and shed_dist ≤ 2 → deposit (`DROP` only if carrying no WHEAT/animal; else `PLACE` each product); else `PASS`.

Skip rules (the world changes): before acting on a stop, re-check it is still valid (tile still a plant needing water / animal still unfed, etc.) — if not, pop and continue. This is the only per-hour perception the executor needs; it does not re-plan.

**Replan triggers** (call `enumerate_chores` + `plan_day` again for the *remaining* hours, keeping done ids): hour 1 (morning purchases landed: new seeds, wheat, animals; new hands), and any hour where `len(unassigned_hard) > 0 and a unit is idle`. Cap replans at 4/day.

Feed wheat: routes carry exactly what they need; `economy()`'s feed order at hour 0/1 stays as is (it buys `n_animals + spare − shed`), and the hour-1 replan distributes it.

## 8. Economy hooks (small)

- `economy()` calls `hands_needed()` instead of `_load_model()` for HIRE counts at hours 0–2.
- Keep `sell_hourly=1` and the drop-on-shed rule (C2) — they are complementary to the planner (products now arrive at the shed during the day).
- Optional knob `plan_melons_first=1`: on days 6–10 MELON water chores get value ×1.5 (protects the day-10 full yield).

## 9. Acceptance tests (in this order; stop and fix at the first failure)

1. **No-op sanity**: `python3 mini_engine.py candidates/P.py candidates/V3_12.py --seeds 1 2 3` runs with `errors=[0,0]` and no GUARD prints (the crash guard in `agent()` swallows exceptions — grep stderr for "GUARD").
2. **Chore completion metric** (add to `mini_engine` trace or a new `trace_chores.py`): per day, count hard chores enumerated at hour 0 vs. completed by hour 23, and animals with `consecutive_unfed ≥ 1` at end of day. Targets on seeds 1–5 vs V3.12: **0 escaped animals, 0 weeds from unwatered crops (`_daily_refresh_plants` converts them), ≥ 95% of hard chores done**. C1's current numbers are the baseline to print alongside.
3. **Head-to-head**: `P vs C1`, seeds 1–10 both seats: must be ≥ 0. If negative, decompose with `decompose.py` — the usual culprits will be (a) pickup detours (too many shed trips: cap to one pickup per route per plan), (b) over-hiring (check hands_eod vs C1), (c) planting without same-day water.
4. **Scale test** (the point of the build): `P` with `open_melons=12` and `wheat_per_animal=0.5` vs C1, seeds 1–10. C1 loses money with these settings; P should not.
5. **Held-out**: seeds 11–30 vs C1, V3.12, `tape_shirabe`, `tape_yuan800`, `tape_atakan`. Ship if ≥ C1 everywhere and tape margins improve by ≥ $5k.

## 10. Implementation notes for a smaller model

- Work in `candidates/P.py`; never edit `K.py`, `C1.py`, or `V3_12.py`.
- Positions are `(x, y)` tuples; `tiles[y][x]`. Shed tiles list is `SHED_TILES`; use `v["shed_tiles"]` for the unlocked ones (all four are usable for shed ops even when LOCKED — the engine allows it — but walking onto a LOCKED tile is allowed only if it's a shed-access tile; treat all four as walkable).
- `carry` is `obs["private"]["inventories"][i]` (dict item→n); products in `PRODUCTS`, animals in `ANIMALS`.
- Deterministic tie-breaks everywhere (sort by (cost, pos)) — the evaluator's cache assumes determinism.
- Keep per-turn time under 50 ms; the ladder limit is 1 s and the whole game currently runs in 0.6 s.
- Do not remove the crash guard; do add `print(..., file=sys.stderr)` inside it during development.
- All rejected ideas and their numbers are in `docs/candidates-C1-H10-sep03.md`; do not re-test them.

## Addendum (Sep 4) — read `evolve/RULES.md` first

The autonomous loop in `evolve/` (Grace, Sep 3) measured two things this spec must respect:

1. **Routing alone is ≈ 0** (`evolve/oracle.py`): making travel free on C1 changes money by −$63k…+$25k per seed, mean ≈ 0, because C1's economy does not generate enough obligations to use freed labor. So the planner (§6–7) is necessary but not sufficient; it must ship *paired* with allocation that raises work per hand-day (herd 13–14, ~5 wheat tiles planted daily, harvest batching). §9.4 (the scale test) is therefore not optional — it is the primary acceptance test, and §9.3 (≥ C1 with C1's allocation) is only a sanity floor.
2. **The frontier's execution numbers to hit**: travel per work action 0.97–1.05 (C1: 1.5–1.6); missed plant-days ~330–400 (C1: 430–560); deliberate skipped feeding on non-production days (cows every 2nd day, sheep every 3rd — an animal only escapes after 2 consecutive unfed days). Add "skip feed on non-production day if fed yesterday" as an optional chore rule in §4, and report travel-per-action in the §9.2 metric.

Baseline to beat is no longer C1: the loop's best own-code candidate (banded-siting `crop_admission` block + knobs; `candidates/E1.py`) is +$6.5k vs C1 and +$9.7k vs V3.12 on fresh seeds 31–50. Build P on top of E1's knobs and block.
