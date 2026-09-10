"""Action timing table: extract per-day action timing from trace data.

Infers what actions were taken each day (sell, buy animal, buy seed, buy land,
hire, water, feed, harvest, fertilize) from the per-day trace metrics, and
computes the outcome associated with each action timing decision.

This is OBSERVATIONAL — it measures correlations between action timing and
outcome, not causal effects. Same epistemic caveats as param_exploration.

Output shape (one per candidate trace, JSON-able):
{
  "action_table": {
    "SELL": [
      {"day": 10, "items": {"MELON": 5}, "revenue": 400, "context": {...}},
      {"day": 11, "items": {"WHEAT": 3}, "revenue": 90, "context": {...}},
      ...
    ],
    "BUY_ANIMAL": [
      {"day": 2, "items": {"COW": 2, "SHEEP": 2}, "cost": 1800, "context": {...}},
      ...
    ],
    "BUY_SEED": [...],
    "BUY_LAND": [...],
    "BUY_PRODUCT": [...],   # feed, fertilizer
    "HIRE": [...],
    "WATER_MISSED": [...],   # days where water was missed (postponement signal)
    "FEED_MISSED": [...],    # days where feed was missed (postponement signal)
  },
  "context": {
    "game_day": 30,
    "animals_d15": <animals on day 15>,
    "land_final": <land on final day>,
    "hands_max": <max hands>,
    "money_d10": <cash on day 10>,
    "final_networth": <final networth>,
    "total_revenue": <total sales_rev>,
    "total_buys": <total buys_cost>,
    "missed_water_total": <sum missed_water>,
    "missed_feed_total": <sum missed_feed>,
  }
}

The action_table is the input for the decision matrix (AGE-359) and the
remaining-horizon ROI analysis (AGE-360).
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

# Import chassis constants for inferring action types from trace data
# These are read from the chassis module at call time to stay in sync
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))  # evolve/ parent = repo root

import evolve.chassis as chassis


def action_table_from_trace(trace: dict[str, Any]) -> dict[str, Any]:
    """Extract per-day action timing from a single-player trace (seat 0).

    Args:
        trace: per-day trace dict from run_traced()[trace][0], with keys:
            cash, networth, sales_rev, buys_cost, sales_by_product,
            animals, plants, land, shed_units, carried_units,
            missed_water, missed_feed, hands, escapes, weeds_new

    Returns:
        dict with:
          - action_table: {action_type: [day_events]}
          - context: whole-game context dict for matrix slicing
    """
    n_days = len(trace.get("cash") or [])
    if n_days == 0:
        return {"action_table": {}, "context": {}}

    A = trace.get("animals") or []
    P = trace.get("plants") or []
    L = trace.get("land") or []
    H = trace.get("hands") or []
    CASH = trace.get("cash") or []
    NW = trace.get("networth") or []
    SV = trace.get("sales_rev") or []
    BV = trace.get("buys_cost") or []
    SBP = trace.get("sales_by_product") or []
    SU = trace.get("shed_units") or []
    CU = trace.get("carried_units") or []
    MW = trace.get("missed_water") or []
    MF = trace.get("missed_feed") or []
    ES = trace.get("escapes") or []
    WN = trace.get("weeds_new") or []

    actions: dict[str, list[dict[str, Any]]] = defaultdict(list)

    # --- SELL events (from sales_by_product) ---
    for day in range(n_days):
        sbp = SBP[day] if day < len(SBP) and SBP[day] else {}
        if not sbp:
            continue
        items = {}
        revenue = 0
        for item, qty in sbp.items():
            items[item] = qty
            # Price inference: use CROPS/PRODUCT prices from chassis
            if item in ("MILK", "WOOL", "EGG"):
                # Animal products — price not directly known, infer from revenue/qty
                pass
            elif item == "MELON":
                items[item] = qty
            elif item in chassis.CROPS:
                seed_cost = chassis.CROPS[item]["seed"]
                items[item] = qty
            revenue += sum(sbp.values())
        actions["SELL"].append({
            "day": day,
            "items": items,
            "revenue": SV[day] if day < len(SV) else 0,
            "context": _context_on_day(trace, day),
        })

    # --- BUY_ANIMAL events (from animals delta + buys_cost) ---
    for day in range(1, n_days):
        delta_animals = A[day] - A[day - 1]
        if delta_animals > 0:
            # Infer which animals from typical opening: COW + SHEEP
            # This is approximate — exact species mix not in trace
            cost = BV[day] if day < len(BV) else 0
            # Separate animal cost from feed cost (approximate: animal buys on days with large BV spike)
            actions["BUY_ANIMAL"].append({
                "day": day,
                "count": delta_animals,
                "cost": cost,
                "context": _context_on_day(trace, day),
            })

    # --- BUY_SEED events (from plants delta + buys_cost) ---
    for day in range(1, n_days):
        delta_plants = P[day] - P[day - 1]
        if delta_plants > 0:
            cost = BV[day] if day < len(BV) else 0
            # Infer crop type from typical planting patterns
            # MELON planted days 0-12, WHEAT days 0-24, etc.
            actions["BUY_SEED"].append({
                "day": day,
                "count": delta_plants,
                "cost": cost,
                "context": _context_on_day(trace, day),
            })

    # --- BUY_LAND events (from land delta) ---
    for day in range(1, n_days):
        delta_land = L[day] - L[day - 1]
        if delta_land > 0:
            # Land price depends on how many already owned
            owned_before = int(L[day - 1]) if day > 0 else 0
            cost = 0
            for n in range(owned_before, owned_before + int(delta_land)):
                if 1 <= n <= len(chassis.LAND_PRICES):
                    cost += chassis.LAND_PRICES[n - 1]
            actions["BUY_LAND"].append({
                "day": day,
                "count": delta_land,
                "cost": cost,
                "context": _context_on_day(trace, day),
            })

    # --- BUY_PRODUCT events (feed + fertilizer, from buys_cost - animal/seed/land costs) ---
    for day in range(n_days):
        bv = BV[day] if day < len(BV) else 0
        if bv > 0:
            # Approximate: if missed_feed > 0 that day, some of bv was feed
            mw = MW[day] if day < len(MW) else 0
            mf = MF[day] if day < len(MF) else 0
            # Feed cost ~ wheat_price * feed_units * 1.15 (from chassis)
            # This is approximate — exact feed vs fertilizer split not in trace
            actions["BUY_PRODUCT"].append({
                "day": day,
                "cost": bv,
                "missed_feed_that_day": mf,
                "missed_water_that_day": mw,
                "context": _context_on_day(trace, day),
            })

    # --- HIRE events (from hands delta) ---
    for day in range(1, n_days):
        delta_hands = H[day] - H[day - 1]
        if delta_hands > 0:
            # Hire cost is fib(hires_today + n) — approximate from cash drop
            # Not directly measurable from trace; infer from hands delta
            actions["HIRE"].append({
                "day": day,
                "count": delta_hands,
                "context": _context_on_day(trace, day),
            })

    # --- WATER_MISSED (postponement signal: water not done when needed) ---
    for day in range(n_days):
        mw = MW[day] if day < len(MW) else 0
        if mw > 0:
            actions["WATER_MISSED"].append({
                "day": day,
                "count": mw,
                "context": _context_on_day(trace, day),
            })

    # --- FEED_MISSED (postponement signal: feed not done when needed) ---
    for day in range(n_days):
        mf = MF[day] if day < len(MF) else 0
        if mf > 0:
            actions["FEED_MISSED"].append({
                "day": day,
                "count": mf,
                "context": _context_on_day(trace, day),
            })

    # --- Context (whole-game, for matrix slicing) ---
    return {
        "action_table": dict(actions),
        "context": _whole_game_context(trace),
    }


def _context_on_day(trace: dict[str, Any], day: int) -> dict[str, Any]:
    """Context snapshot on a given day, for matrix slicing."""
    A = trace.get("animals") or []
    P = trace.get("plants") or []
    L = trace.get("land") or []
    H = trace.get("hands") or []
    CASH = trace.get("cash") or []
    SU = trace.get("shed_units") or []

    def _at(arr, d, default=0):
        if d < len(arr) and arr[d] is not None:
            return arr[d]
        return default

    # Crop readiness: what's planted, what's ripe
    crops_in_field = P[day] if day < len(P) else 0
    return {
        "day": day,
        "days_remaining": max(0, 29 - day),
        "animals": _at(A, day),
        "plants": _at(P, day),
        "land": _at(L, day),
        "hands": _at(H, day),
        "cash": _at(CASH, day),
        "shed_units": _at(SU, day),
        "animals_d15": _at(A, 15),
        "land_final": _at(L, -1),
        "hands_max": max(H) if H else 0,
        "money_d10": _at(CASH, 10),
    }


def _whole_game_context(trace: dict[str, Any]) -> dict[str, Any]:
    """Whole-game context for matrix slicing."""
    A = trace.get("animals") or []
    P = trace.get("plants") or []
    L = trace.get("land") or []
    H = trace.get("hands") or []
    CASH = trace.get("cash") or []
    NW = trace.get("networth") or []
    SV = trace.get("sales_rev") or []
    BV = trace.get("buys_cost") or []
    MW = trace.get("missed_water") or []
    MF = trace.get("missed_feed") or []

    return {
        "game_day": len(CASH),
        "animals_d15": A[15] if len(A) > 15 else (A[-1] if A else 0),
        "land_final": L[-1] if L else 0,
        "hands_max": max(H) if H else 0,
        "money_d10": CASH[10] if len(CASH) > 10 else (CASH[-1] if CASH else 0),
        "final_networth": NW[-1] if NW else 0,
        "total_revenue": sum(SV),
        "total_buys": sum(BV),
        "missed_water_total": sum(MW),
        "missed_feed_total": sum(MF),
        "peak_animals": max(A) if A else 0,
        "peak_plants": max(P) if P else 0,
    }


def compute_postponement(action_type: str, day: int) -> int:
    """Approximate postponement: how many days later than 'optimal' this action was taken.

    Optimal days are rough heuristics per action type. Same logic used by both
    action_table_summary (aggregation) and action_table_to_matrix_rows (row-level).
    """
    if action_type == "SELL":
        return 0  # SELL postponement computed from items, not here
    if action_type == "BUY_ANIMAL":
        return max(0, day - 2)
    if action_type == "BUY_SEED":
        return max(0, day - 2)
    if action_type == "BUY_LAND":
        return max(0, day - 6)
    if action_type in ("WATER_MISSED", "FEED_MISSED"):
        return day  # optimal = 0 (never miss)
    return 0  # unknown: no postponement penalty


def optimal_day_for_sell(items: dict[str, Any]) -> int:
    """Optimal day for a SELL event, based on what's being sold."""
    if "MELON" in str(items):
        return 10
    return 5


if __name__ == "__main__":
    # Self-test: parse a trace and print action_table summary
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("trace_json", help="path to trace JSON file")
    args = ap.parse_args()

    trace = json.loads(Path(args.trace_json).read_text())
    result = action_table_from_trace(trace[0] if isinstance(trace, list) else trace)
    print(f"Context: {json.dumps(result['context'], indent=2)}")
    print(f"\nAction table:")
    for atype, events in result["action_table"].items():
        print(f"\n  {atype}: {len(events)} events")
        for ev in events[:5]:
            print(f"    day {ev['day']}: {ev}")
        if len(events) > 5:
            print(f"    ... and {len(events) - 5} more")
