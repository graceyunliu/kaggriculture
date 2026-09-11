#!/usr/bin/env python3
"""shed_capacity_margin_calibration -- final measurement pass before any candidate design.
Builds on shed_capacity_audit.py's mechanical finding (37/80 games, 362 units silently
discarded by _drop_inventories_to_shed). This pass:
  1. Prices every discarded unit at the ACTUAL market price at the moment of loss (not an
     average) -- also IS the zero-labor/zero-displacement upper bound (part 4): "what if the
     excess had simply been sold immediately at the available price" is exactly the market
     price of the destroyed inventory at that instant, no price-impact assumption needed for
     an upper bound.
  2. Replicates the engine's exact per-item drop order (vendor _drop_inventories_to_shed:
     iterates private["inventories"] in order, and within each hand's inv in dict-insertion
     order, deleting the WHOLE item once any of it doesn't fit) instead of a proportional
     estimate, so item-level dollar attribution is exact, not approximate.
  3. Traces the immediate cause of each event: same-day (DROP/PLACE) inflow by item vs
     same-day successful SELL outflow by item, to tell "policy failed to sell soon enough"
     apart from "inventory arrived too fast/late to react to".
"""
import sys, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me

CAND = str(ROOT / "candidates/O26_CARROT_SIZING.py")
TAPES = [
    str(ROOT / "Opponents/tape_alaylm_106813359.py"),
    str(ROOT / "Opponents/tape_bahaenes_106828159.py"),
    str(ROOT / "Opponents/tape_peterparker_106816877.py"),
    str(ROOT / "Opponents/tape_yangkuang2_106819729.py"),
]
SEEDS = list(range(11, 31))


def run_one(cand_path, opp_path, seed, cand_seat=0):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand_path), me.load_agent(opp_path)] if cand_seat == 0 else \
             [me.load_agent(opp_path), me.load_agent(cand_path)]

    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0

    tpd = int(cfg["turnsPerDay"])
    steps = int(cfg["episodeSteps"])
    shed_cap = int(mod.get(env.configuration, "shedCapacity", 100))

    # hook _commit_unit to log SELL/BUY_PRODUCT for the cand_seat farm only, by day
    farms_ref = [None]
    day_sell = {}   # day -> {item: qty}
    day_buy = {}    # day -> {item: qty}
    orig_commit = mod._commit_unit

    def logged(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok and farms_ref[0] is not None and farm is farms_ref[0]:
            d = state[0].observation.day
            if op == "SELL":
                day_sell.setdefault(d, {})[item] = day_sell.setdefault(d, {}).get(item, 0) + 1
            elif op == "BUY_PRODUCT":
                day_buy.setdefault(d, {})[item] = day_buy.setdefault(d, {}).get(item, 0) + 1
        return ok

    mod._commit_unit = logged

    events = []  # list of dicts: day, hour(=tpd-1), item, units, price, value
    day_inflow = {}  # day -> {item: qty} from DROP/PLACE (shed increases not from BUY_PRODUCT/BUY_ANIMAL)
    prev_shed = {}
    step = 0
    while True:
        obs0 = state[0].observation
        farms_ref[0] = obs0.farms[cand_seat]
        private = state[cand_seat].observation.private
        cur_shed = dict(private["shed"])
        d = obs0.day
        # attribute shed increases this turn not already explained by BUY_PRODUCT/BUY_ANIMAL to DROP/PLACE (harvest/animal-product/carry)
        for item, n in cur_shed.items():
            prev_n = prev_shed.get(item, 0)
            if n > prev_n:
                day_inflow.setdefault(d, {})[item] = day_inflow.setdefault(d, {}).get(item, 0) + (n - prev_n)
        prev_shed = cur_shed

        is_last_hour_of_day = (obs0.hour == tpd - 1)
        pre_carry_by_hand = [dict(inv) for inv in private["inventories"]] if is_last_hour_of_day else None
        pre_shed = dict(private["shed"]) if is_last_hour_of_day else None
        prices_now = dict(obs0.market["prices"]) if is_last_hour_of_day else None

        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act if isinstance(act, dict) else {}
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step

        if is_last_hour_of_day:
            # replicate _drop_inventories_to_shed's exact order to find real per-item discards
            shed_sim = dict(pre_shed)
            for inv in pre_carry_by_hand:
                for item, n in list(inv.items()):
                    if n <= 0:
                        continue
                    current = sum(shed_sim.values())
                    room = max(0, shed_cap - current)
                    take = min(n, room)
                    if take > 0:
                        shed_sim[item] = shed_sim.get(item, 0) + take
                    lost = n - take
                    if lost > 0:
                        price = prices_now.get(item, 0)
                        events.append({
                            "day": d, "item": item, "units": lost,
                            "price": price, "value": lost * price,
                        })

        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break

    mod._commit_unit = orig_commit

    # attach cause-trace to each event's day
    for ev in events:
        d = ev["day"]
        ev["day_sell"] = day_sell.get(d, {})
        ev["day_buy"] = day_buy.get(d, {})
        ev["day_inflow"] = day_inflow.get(d, {})
        ev["item_sold_same_day"] = ev["item"] in day_sell.get(d, {})
        ev["item_bought_same_day"] = ev["item"] in day_buy.get(d, {})

    return events


def main():
    all_events = []
    per_game_value = []
    for tape in TAPES:
        for seed in SEEDS:
            ev = run_one(CAND, tape, seed, cand_seat=0)
            for e in ev:
                e["tape"] = Path(tape).stem
                e["seed"] = seed
            all_events.extend(ev)
            per_game_value.append(sum(e["value"] for e in ev))

    n_games = len(TAPES) * len(SEEDS)
    total_value = sum(e["value"] for e in all_events)
    print(f"=== dollar-pricing pass: {len(all_events)} discard sub-events across {n_games} games ===")
    print(f"total lost $ (== zero-labor sell-immediately upper bound): {total_value:.0f}")
    print(f"mean $/game: {total_value/n_games:.1f}   median $/game (over ALL games, zeros included): {statistics.median(per_game_value):.1f}")
    nonzero = [v for v in per_game_value if v > 0]
    print(f"games with >0 loss: {len(nonzero)}/{n_games}   mean $/affected game: {statistics.mean(nonzero):.1f}   median: {statistics.median(nonzero):.1f}")

    # concentration
    values_sorted = sorted((e["value"] for e in all_events), reverse=True)
    def top_share(pct):
        k = max(1, int(len(values_sorted) * pct))
        return sum(values_sorted[:k]) / total_value * 100 if total_value else 0
    print(f"top 5% of events: {top_share(0.05):.1f}% of total $   top 10%: {top_share(0.10):.1f}%")
    print(f"largest single event: {values_sorted[0]:.0f}   n events total: {len(values_sorted)}")

    # item breakdown
    by_item = {}
    for e in all_events:
        by_item[e["item"]] = by_item.get(e["item"], 0.0) + e["value"]
    print("item-level $ breakdown:", {k: round(v, 0) for k, v in sorted(by_item.items(), key=lambda kv: -kv[1])})

    # cause trace summary
    sold_same_day = sum(1 for e in all_events if e["item_sold_same_day"])
    bought_same_day = sum(1 for e in all_events if e["item_bought_same_day"])
    print(f"\ncause trace: of {len(all_events)} sub-events, item WAS sold same day (some, but not enough) in {sold_same_day} "
          f"({sold_same_day/len(all_events)*100:.0f}%); item was ALSO purchased same day in {bought_same_day} ({bought_same_day/len(all_events)*100:.0f}%)")

    print("\n--- top 10 largest events, with cause trace ---")
    top = sorted(all_events, key=lambda e: -e["value"])[:10]
    for e in top:
        print(f"  {e['tape']} seed={e['seed']} day={e['day']} item={e['item']} units={e['units']} price={e['price']:.1f} value={e['value']:.0f}")
        print(f"      same-day sells: {e['day_sell']}   same-day buys: {e['day_buy']}   same-day shed-inflow(all items, DROP/PLACE): {e['day_inflow']}")


if __name__ == "__main__":
    main()
