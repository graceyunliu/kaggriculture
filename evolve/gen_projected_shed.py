#!/usr/bin/env python3
"""Generate the minimal projected-overflow wheat-relief candidate from O33."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "candidates" / "O33_FERT_DENIAL4.py").read_text()

old = '''        w = shed.get("WHEAT", 0)
        if day >= 29:
            if w > 0:
                orders.append(["SELL", "WHEAT", int(w)])
        elif prices.get("WHEAT", 0) >= (KNOBS["wheat_sell_price"] if day < 27 else 30):
            hold = KNOBS["wheat_stock"] if day < 27 else 0
            reserve_feed = (n_total + 3) + (n_total * KNOBS["wheat_hold_days"] if day < 27 else 0)
            surplus = int(w - reserve_feed - hold)
            if shed_load > 80:
                surplus = int(w - (n_total + 3))
            if surplus > 0:
                orders.append(["SELL", "WHEAT", surplus])
                revenue_est += surplus * prices.get("WHEAT", 0) * 0.9
'''

new = '''        w = shed.get("WHEAT", 0)
        # PROJECTED_OVERFLOW_WHEAT_RELIEF: at the final evening decision window,
        # include every shed and carried item because the engine's 100-unit cap does.
        # Liquidate only wheat above tomorrow's feed buffer, and only enough to make
        # room for the predictable overnight auto-drop.
        projected_load = sum(max(0, n) for n in shed.values()) + sum(
            max(0, n) for bag in inv for n in bag.values())
        overflow_relief = 0
        if 20 <= hour <= 23 and day < 29 and projected_load > 100:
            overflow_relief = min(max(0, w - (n_total + 3)), projected_load - 100)
        if day >= 29:
            if w > 0:
                orders.append(["SELL", "WHEAT", int(w)])
        elif prices.get("WHEAT", 0) >= (KNOBS["wheat_sell_price"] if day < 27 else 30) or overflow_relief > 0:
            hold = KNOBS["wheat_stock"] if day < 27 else 0
            reserve_feed = (n_total + 3) + (n_total * KNOBS["wheat_hold_days"] if day < 27 else 0)
            surplus = int(w - reserve_feed - hold)
            if shed_load > 80:
                surplus = int(w - (n_total + 3))
            surplus = max(surplus, int(overflow_relief))
            if surplus > 0:
                orders.append(["SELL", "WHEAT", surplus])
                revenue_est += surplus * prices.get("WHEAT", 0) * 0.9
'''

if source.count(old) != 1:
    raise SystemExit("expected O33 wheat-sale block exactly once")
candidate = source.replace(old, new)

route_marker = '''    if i in S["routes"]:
        op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
'''
recall = '''    # Under visible overnight capacity pressure, leave at the last feasible hour
    # and convert carried product before the engine's destructive auto-drop. This sits
    # ahead of persistent routes because waiting one more action makes the loss unavoidable.
    projected_eod = sum(max(0, n) for n in shed.values()) + sum(
        max(0, n) for bag in (obs["private"].get("inventories") or []) for n in bag.values())
    if day < 29 and projected_eod > 100 and prod_carried > 0 and carry.get("WHEAT", 0) >= 3:
        hd = _home_dist(pos, unlocked_shed)
        if hour + hd == 23:
            S["routes"].pop(i, None)
            if hd == 0:
                return ["DROP"]
            return [_step(pos, _nearest(pos, unlocked_shed))]
    if i in S["routes"]:
        op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
'''
if candidate.count(route_marker) != 1:
    raise SystemExit("expected O33 route dispatch marker exactly once")
candidate = candidate.replace(route_marker, recall)
candidate = candidate.replace(
    "# O22_MELON_MORNING:",
    "# O39_PROJECTED_SHED_RELIEF: O33 plus projected end-of-day wheat relief.\n# O22_MELON_MORNING:",
    1,
)
(ROOT / "candidates" / "O39_PROJECTED_SHED_RELIEF.py").write_text(candidate)

# The broad trigger pays a recall cost even for one-unit pressure. Preserve it as
# O39 and generate the preregistered severity-gated refinement separately.
severe = candidate.replace(
    "projected_eod > 100 and prod_carried > 0",
    "projected_eod >= 110 and prod_carried > 0",
    1,
).replace("O39_PROJECTED_SHED_RELIEF", "O40_SEVERE_SHED_RELIEF", 1)
(ROOT / "candidates" / "O40_SEVERE_SHED_RELIEF.py").write_text(severe)
