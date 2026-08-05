# v8.1 Build Spec — Order-Slot Allocation (Stage 1)

**Base:** `main_v8.py` (Phase 1 foundation, verified no-op vs `main_v7.6.py`)
**Target file:** `main_v8.1.py`
**Scope:** two changes, behind independent flags, both aimed at the same measured bottleneck.
**Explicitly out of scope:** changing `HAND_TARGET_MAX`, any EV/scoring formula, any selling logic.

---

## 0. The problem this fixes

Measured on seed 42 vs `opp_frontier_v12` ($57,764 vs $136,495):

- The hiring rule computes `work` of 101–112, so `target` pins to the `HAND_TARGET_MAX = 18` cap on **17 of 29 days**, and issues up to 18 `HIRE` orders.
- Actual hands held (sampled hour 12) are **5–9, declining to 5 by day 28**.
- Budget is *not* the limit — the hire loop reports $23,558 / $34,933 / $41,183 unspent on days 24 / 26 / 28.
- Live trace, day 5: hour 0 requests 18 hires; hour 1 shows `hires_today = 7`. **Eleven requests evaporated**, and nothing further is attempted that day.
- Frontier hires in hours **{1, 2}** and lands 324 hires (10.8/day) to our 207 (6.9/day), holding 12 hands to our 5–9.

Everything downstream — watering, planting, weeding, harvest, wheat output — is gated by that.

---

## 1. Ground truth (verified against `vendor/kaggle_environments_engine/kaggriculture.py`)

Build against these, not against assumptions.

| Fact | Source | Why it matters |
|---|---|---|
| `queues.append(q[:max_orders])` — the engine **truncates your list to the first 10 and silently discards the rest** | `_process_market`, ~line 536 | Slots are awarded by **position in the list you submit**. Sorting is allocation. |
| `maxMarketOrdersPerTurn = 10`, `turnsPerDay = 24`, `farmHandCostMult = 1` | live config dump | Confirmed defaults. |
| `_hire_cost(n) = mult * _fib(n)` where `n = farm["hires_today"]` | `_hire_cost` / `_do_hire`, ~line 674 | Cost escalates **within the day**, not per turn. |
| `_fib(0)=1, _fib(1)=1, _fib(2)=2, _fib(3)=3, _fib(4)=5, …` | `_fib`, ~line 666 | Marginal cost: 10th hand $55, 12th $144, 14th $377, 15th $610, 18th **$2,584**. |
| `farm["hands"] = []` and `farm["hires_today"] = 0` at end of day | `_end_of_day`, ~line 857 | Hands are re-bought daily. A missed hire is a lost hand-**day**, not a lost asset. |
| **`hires_today` is exposed to the agent** as `me["hires_today"]` | verified live; farm keys are `['farmer','hands','hires_today','money','tiles','unlocked_quadrants']` | This is what makes correct cross-turn hire costing possible. |
| No engine cap on hand count | absence in `_do_hire` | The only ceiling is cost. |
| `_do_hire` silently no-ops if `money < cost` | `_do_hire` | Over-ordering is safe, never an error. |

---

## 2. Change A — spread hiring across the start of the day

### 2.1 Location

`main_v8.py`, inside `economy()`, the block beginning:

```python
    # --- Hiring: real Fibonacci cost, counts animal maintenance workload
    if hour == 0 and day < 29:
```

### 2.2 New constants (near the other hand constants, ~line 90)

```python
SPREAD_HIRES = True        # Change A master flag
HIRE_WINDOW_HOURS = 3      # hire during hours 0,1,2 of each day
```

### 2.3 The change

```python
    _hire_window = HIRE_WINDOW_HOURS if SPREAD_HIRES else 1
    if hour < _hire_window and day < 29:
        animal_work = _pending_animal_work(view)
        work = (len(view["water"]) + len(view["urgent_water"]) +
                len(view["harvest"]) + len(view["empty"]) +
                animal_work * ANIMAL_WORK_WEIGHT)
        target = max(HAND_TARGET_MIN, min(HAND_TARGET_MAX, math.ceil(work / 5)))
        need = max(0, target - len(me["hands"]))
        # REQUIRED with spreading: the engine charges _fib(hires_today), and
        # hires_today persists across turns within a day. Starting the fib
        # index at 0 on hour 1 would under-price every hire and overspend.
        hires_today = me.get("hires_today", 0)
        n = 0
        while n < need and len(hire_orders) < MAX_HIRE_SLOTS:
            cost = FARM_HAND_COST_MULT * _fib(hires_today + n)
            if budget < cost:
                break
            hire_orders.append(["HIRE"])
            budget -= cost
            n += 1
```

### 2.4 Notes

- **`_fib(hires_today + n)` is not optional.** It is a correctness fix that spreading *requires*, not a second change. Ship them together.
- **No carry-forward state is needed.** `need` is derived from `len(me["hands"])`, which is the true current count, so each turn self-corrects: hour 0 asks for 18 and gets ~7; hour 1 sees 7 hands and asks for 11; hour 2 sees ~16 and asks for 2. Do **not** add a module-level pending-order queue — `economy()` already re-derives everything from live state each turn, and stale queued orders would be priced against stale money.
- `HIRE_WINDOW_HOURS = 3` costs the last batch 2/24 of a working day. Do not widen it much further; hiring at hour 12 buys half a hand-day at full price.

---

## 3. Change B — rank orders by cost-of-delay before submitting

### 3.1 Principle

Rank by **what is lost if this order waits one turn**, not by gross value. Our mean is 0.74 orders/turn across 720 turns, so almost everything can wait. Three consequences that invert the current ordering:

- **Ordinary sells are nearly worthless in slot terms** — goods keep, our realized prices are above base — yet they currently get first claim.
- **`BUY_LAND` is worth ~zero while ~40 tiles sit idle** — it buys land we have no labor to work.
- **Feed wheat for an at-risk animal is the most valuable order in the game** (an escape costs $400–500 plus all future yield) and currently sits mid-bucket.

### 3.2 New constants

```python
RANK_ORDERS = True         # Change B master flag
CHEAP_HIRE_LIMIT = 12      # hires at fib index >= this drop below ordinary sells
                            # (_fib(11)=144, _fib(12)=233, _fib(13)=377)
LAND_IDLE_TILE_THRESHOLD = 10   # above this many idle plantable tiles, land is low priority
SHED_CRITICAL_FREE = 5     # shed_load >= SHED_CAP - this  => overflow is imminent
```

### 3.3 Priority table (lower number = earlier position = safer from truncation)

| Tier | Order | Condition |
|---|---|---|
| 0 | `BUY_PRODUCT WHEAT` | any owned animal is at risk (see 3.4) |
| 1 | `SELL` | `day >= LIQUIDATE_DAY` **or** shed critical |
| 2 | `HIRE` | fib index `< CHEAP_HIRE_LIMIT` |
| 3 | `BUY_SEED` | crop is within 2 days of its `CUTOFF` **and** idle plantable tiles exist |
| 4 | `BUY_LAND` | idle plantable tiles `< LAND_IDLE_TILE_THRESHOLD` |
| 5 | `BUY_ANIMAL` | always |
| 6 | `BUY_PRODUCT` | ordinary feed restock |
| 7 | `SELL` | ordinary |
| 8 | `HIRE` | fib index `>= CHEAP_HIRE_LIMIT` |
| 9 | `BUY_SEED` | ordinary |
| 10 | `BUY_LAND` | idle plantable tiles `>= LAND_IDLE_TILE_THRESHOLD` |

Land appears twice deliberately. Pinning it at the bottom unconditionally risks never buying it — the quadrant rules have hard day cutoffs (`quads==2` needs `day<=18`, `quads==3` needs `day<=16`), and a permanently-truncated land order would silently cost a quadrant. The conditional form keeps the "don't buy land you can't work" insight without that failure mode. **If you only keep one guard from this spec, keep this one.**

### 3.4 Context needed

Compute once, before the merge:

```python
    animal_at_risk = any(
        (not t.get("fed_today", True)) and t.get("consecutive_unfed", 0) >= 1
        for _pos, t in view["my_pastures"]
    )
    shed_critical = shed_load >= SHED_CAP - SHED_CRITICAL_FREE
    _plantable = plantable_crops(seeds, day)
    idle_plantable = min(len(view["empty"]),
                         sum(seeds.get(c, 0) for c in _plantable))
    near_cutoff = {c for c in CROPS if 0 <= CUTOFF.get(c, -1) - day <= 2}
```

`idle_plantable` intentionally counts tiles we could *actually* plant (tiles **and** seeds), not raw empty tiles, so land priority reflects real capacity.

### 3.5 Replacing the merge

Delete the existing two-loop merge block at the end of `economy()` (the one ending in the `for i in range(len(orders)-1, -1, -1)` SELL-overwrite) and replace with:

```python
    if not RANK_ORDERS:
        # v7.6 original merge -- keep verbatim for the flag-off no-op check
        orders = []
        for bucket in (strategic_orders, feed_orders, sell_orders):
            for order in bucket:
                if len(orders) >= MAX_MARKET_ORDERS:
                    break
                orders.append(order)
        for bucket in (hire_orders, seed_orders):
            for order in bucket:
                if len(orders) < MAX_MARKET_ORDERS:
                    orders.append(order)
                else:
                    for i in range(len(orders) - 1, -1, -1):
                        if orders[i][0] == "SELL":
                            orders[i] = order
                            break
                    break
        return orders

    scored = []
    for o in strategic_orders:
        if o[0] == "BUY_LAND":
            scored.append((4 if idle_plantable < LAND_IDLE_TILE_THRESHOLD else 10, o))
        else:                                  # BUY_ANIMAL
            scored.append((5, o))
    for o in feed_orders:
        scored.append((0 if animal_at_risk else 6, o))
    for i, o in enumerate(hire_orders):
        fib_index = me.get("hires_today", 0) + i
        scored.append((2 if fib_index < CHEAP_HIRE_LIMIT else 8, o))
    for o in seed_orders:
        crop = o[1]
        urgent = crop in near_cutoff and idle_plantable > 0
        scored.append((3 if urgent else 9, o))
    for o in sell_orders:
        urgent = day >= LIQUIDATE_DAY or shed_critical
        scored.append((1 if urgent else 7, o))

    scored.sort(key=lambda t: t[0])            # stable: ties keep insertion order
    return [o for _p, o in scored[:MAX_MARKET_ORDERS]]
```

**`sort` must be called with `key=` only.** Python's sort is stable, so equal tiers preserve the order the rules produced them in — which is how the existing within-bucket ordering (e.g. sells already sorted by descending price) survives untouched.

---

## 4. Flags and test matrix

Both flags default `True` in the shipped file, but every configuration must be run:

| Config | `SPREAD_HIRES` | `RANK_ORDERS` | Purpose |
|---|---|---|---|
| **v8.1-off** | False | False | **Must be a bit-exact no-op vs `main_v7.6.py`.** Regression guard on the refactor itself. |
| **v8.1-A** | True | False | Change A alone |
| **v8.1-B** | False | True | Change B alone |
| **v8.1-AB** | True | True | Combined |

Testing A and B separately is not optional. The v7.1 round shipped three individually-sensible fixes that cancelled each other out and lost 2.5× to the version they were meant to improve; the cause was only visible by isolating them.

---

## 5. Test protocol

```bash
# 0. no-op guard (both flags off) -- must be exactly 0.0
python3 seeded_h2h.py main_v8.1.py main_v7.6.py --seeds 1 42 202 --both-seats

# 1. each config vs the champion
python3 seeded_h2h.py main_v8.1.py main_v7.6.py \
    --seeds 1 7 42 99 123 202 --both-seats

# 2. vs the strong fixed bots -- RECORD BOTH SIDES' MONEY
python3 seeded_h2h.py main_v8.1.py Opponents/opp_frontier_v12.py \
    --seeds 1 7 42 99 123 202 --both-seats
python3 seeded_h2h.py main_v8.1.py Opponents/opp_scenario_v14.py \
    --seeds 1 7 42 99 123 202 --both-seats

# 3. stability
python3 smoke_test.py main_v8.1.py --opponent starter
python3 smoke_test.py main_v8.1.py --opponent pass
python3 smoke_test.py main_v8.1.py --opponent starter --turns 48
```

**Always `--both-seats`, never `--swap-half`.** `--swap-half` does not cancel the engine's seat bias; an agent against itself scores mean −$2,772 on the 11-seed set under it, which is how v7.7 came to be rejected on noise (D62).

**Never use `random` as an A/B opponent** — its RNG is unseeded and unreachable by `env.info["seed"]`; v7.6 against it varies ~$2,150 across identical repeated runs (D66). Stability check only.

---

## 6. Mechanism checks (do not judge on money alone)

v8.1 inherits v8's decision log (`DECISION_LOG = True`). After a seeded run, confirm the fix worked *by its intended mechanism*:

```python
sink = mod.DECISION_LOG_SINK
turns = sink.by_kind("turn")
# hands held at hour 12, by day -- target: 5-9 rising toward 11-13
# hires per day from the action stream -- target: 6.9 rising toward ~10
# turns at the 10-order cap -- target: 23 falling toward ~0
```

Baselines to beat (seed 42 vs frontier): hands at day 12/16/20/24/28 = 8, 9, 6, 8, 5; hires/day 6.9; 23 turns at cap; total units sold 731.

The v7.6 round is the precedent for why this matters: it produced objectively fewer weeds and healthier watering in every trace yet still lost 2 of 3 sampled seeds on money. Mechanism and money are separate questions and both need answering.

---

## 7. Success and kill criteria

**Promote if:** paired margin vs `main_v7.6.py` is positive with |t| > 2 across ≥6 seeds, **and** mean hands/day rises, **and** no animal deaths appear, **and** all smoke tests return DONE.

**Diagnostic branch — if hands rise but money does not:** that is the fib-cost overpay, and it is the expected failure mode. The 15th hand costs $610 and the 18th $2,584 against a hand-day worth very roughly $300–500. Do **not** patch it inside v8.1. Test it as its own change (Stage 1c): lower `HAND_TARGET_MAX` from 18 toward 13–15 and re-run. Keeping the ceiling question separate is the whole reason it was excluded from this spec.

**Reject Change B if** it wins nothing on its own *and* config AB is no better than config A — that would mean spreading alone already emptied the congested turns and ranking is redundant at current volumes. Even then it may be worth keeping as insurance for when the fleet grows, but that should be a deliberate call, not an accident.

---

## 8. Pitfalls

1. **Do not start the fib index at 0 on hours 1–2.** The single most likely bug in this build. Symptom: hands rise but money falls sharply, because the agent believes hires cost $1, $1, $2 when it is actually paying $21, $34, $55.
2. **Do not build a carry-forward order queue.** Re-derivation from live state each turn is simpler and cannot go stale. The `need` calculation already handles it.
3. **Do not change `HAND_TARGET_MAX` in this version.** Separate variable, separate test.
4. **Do not reorder within a tier.** Sells arrive pre-sorted by descending price; a stable sort preserves that. An unstable sort or a custom comparator would silently undo it.
5. **Verify the flag-off no-op first**, before running any performance test. If config `v8.1-off` is not exactly 0.0 against `main_v7.6.py`, the refactor itself has a bug and every downstream number is meaningless.
6. **`BUY_LAND` must keep its conditional tier.** Unconditional bottom priority can permanently cost a quadrant via the day cutoffs.
