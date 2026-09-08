"""Derived scenario metrics (AGE-333).

Turns one per-day trace from `evolve/trace.py` (the seat-0 player of a traced game) into a flat
dict of whole-game scalars that scenario criteria can threshold. Everything here is arithmetic
over trace.METRICS plus the `sales_by_product` side-channel run_traced already records -- no new
engine instrumentation, no LLM.

Window constants are module-level and named, because every scenario's verdict depends on them and
the ticket asks for definitions that stay readable and editable.
"""
from __future__ import annotations

ANIMAL_PRODUCTS = ("MILK", "WOOL", "EGG")

# Windows. Day indices are 0-based, matching the trace.
LATE_GAME_START = 23      # "only 7 days remain" -- days 23..29 of a 30-day season
EARLY_TROUGH = (3, 13)    # days the opening is paid for; cash left idle here is capacity not bought
MIDGAME_DAY = 15          # by here a land-constrained farm should have expanded

# Whole-season carry cost of one animal: purchase (GOOSE 300 / COW 400 / SHEEP 500) plus roughly
# one WHEAT per animal-day at ~$25. Used to price late-game purchases and to ask whether a herd
# paid for itself; deliberately conservative (the cheap end of the range).
ANIMAL_UNIT_COST = 400
LAND_PRICES = (1000, 2000, 4000)   # kaggriculture.LAND_PRICES, mirrored so metrics.py stays standalone


def _sum(t, key, lo=0, hi=None):
    xs = t.get(key) or []
    hi = len(xs) if hi is None else min(hi, len(xs))
    return sum((xs[d] or 0) for d in range(min(lo, hi), hi))


def _at(t, key, day, default=None):
    xs = t.get(key) or []
    if not xs:
        return default
    return xs[min(day, len(xs) - 1)]


def _rises(xs, lo, hi=None):
    """Sum of the day-over-day increases of a count series inside [lo, hi). Animals and land only
    grow by purchase, so this is 'units acquired in the window' without needing per-item buy logs."""
    hi = len(xs) if hi is None else min(hi, len(xs))
    return sum(max(0, xs[d] - xs[d - 1]) for d in range(max(1, lo), hi))


def _land_spend(land_series, lo, hi=None):
    """Cash committed to quadrants unlocked inside [lo, hi). The n-th extra quadrant costs
    LAND_PRICES[n-1], so the spend depends on where in the sequence the purchase happened."""
    hi = len(land_series) if hi is None else min(hi, len(land_series))
    spend = 0
    for d in range(max(1, lo), hi):
        for n in range(land_series[d - 1], land_series[d]):   # n = quadrants owned before this one
            if 1 <= n <= len(LAND_PRICES):
                spend += LAND_PRICES[n - 1]
    return spend


def scenario_metrics(t):
    """Flat whole-game metric dict for one player trace."""
    n = len(t.get("cash") or [])
    if n == 0:
        return {}
    animals = [x or 0 for x in t["animals"]]
    plants = [x or 0 for x in t["plants"]]
    land = [x or 0 for x in t["land"]]
    cash = [x or 0 for x in t["cash"]]
    hands = [x or 0 for x in t["hands"]]

    unit_turns = _sum(t, "unit_turns")
    idle_turns = _sum(t, "idle_turns")
    work_turns = _sum(t, "work_turns")
    move_turns = _sum(t, "move_turns")
    hand_days = sum(hands)
    animal_days = sum(animals)
    plant_days = sum(plants)

    sbp = t.get("sales_by_product") or []
    animal_rev = sum(sum(d.get(k, 0) for k in ANIMAL_PRODUCTS) for d in sbp)
    total_rev = _sum(t, "sales_rev")
    crop_rev = total_rev - animal_rev

    peak_animals = max(animals) if animals else 0
    late_animals = _rises(animals, LATE_GAME_START)
    late_land_spend = _land_spend(land, LATE_GAME_START)

    ce, cc = _sum(t, "chores_enumerated"), _sum(t, "chores_completed")
    lo, hi = EARLY_TROUGH
    trough = min(cash[lo:hi]) if len(cash) > lo else cash[-1]

    return {
        # outcome
        "final_cash": cash[-1],
        "final_networth": _at(t, "networth", n - 1),
        "total_revenue": total_rev,
        "total_buys": _sum(t, "buys_cost"),

        # livestock
        "peak_animals": peak_animals,
        "animal_days": animal_days,
        "animal_revenue": animal_rev,
        # What one animal earned across the whole season. Compared against ANIMAL_UNIT_COST-scale
        # thresholds, this answers "did the herd pay for itself?" without needing per-species logs.
        "animal_revenue_per_animal": round(animal_rev / peak_animals, 1) if peak_animals else 0.0,
        "crop_revenue": crop_rev,

        # labor
        "max_hands": max(hands) if hands else 0,
        "hand_days": hand_days,
        "unit_turns": unit_turns,
        "idle_share": round(idle_turns / unit_turns, 4) if unit_turns else 0.0,
        "move_share": round(move_turns / unit_turns, 4) if unit_turns else 0.0,
        # Productive actions per hand-day. A hand that never finds work drags this toward 0; a farm
        # whose footprint matches its labor keeps it near the farmer-only baseline.
        "work_per_hand_day": round(work_turns / hand_days, 2) if hand_days else 0.0,
        "work_turns": work_turns,

        # execution
        "chores_enumerated": ce,
        "chores_completed": cc,
        "chore_completion": round(cc / ce, 4) if ce else 1.0,
        "escapes": _sum(t, "escapes"),
        "missed_feed": _sum(t, "missed_feed"),
        "missed_water": _sum(t, "missed_water"),
        "missed_water_per_plant_day": round(_sum(t, "missed_water") / plant_days, 4) if plant_days else 0.0,
        "weeds_new": _sum(t, "weeds_new"),

        # capacity / land
        "land_final": land[-1],
        "land_at_midgame": _at(t, "land", MIDGAME_DAY, land[-1]),
        "peak_plants": max(plants) if plants else 0,
        "plant_days": plant_days,
        # Deepest the farm ever let its cash fall in the opening window. High means capital was
        # never converted into capacity -- the "leaves money on the table" signature.
        "early_cash_trough": trough,
        "mean_cash_early": round(sum(cash[lo:hi]) / max(1, len(cash[lo:hi])), 1),

        # remaining-game value
        "late_animals_added": late_animals,
        "late_land_spend": late_land_spend,
        # Cash sunk after LATE_GAME_START into assets that cannot return inside the remaining days
        # (a COW first yields 8 days after placement; a quadrant bought on day 23 is pure loss).
        "late_capital_committed": late_land_spend + late_animals * ANIMAL_UNIT_COST,
        "shed_units_final": _at(t, "shed_units", n - 1, 0),
    }


def aggregate(rows):
    """Mean each metric across per-seed metric dicts. Scenario criteria are applied to this."""
    if not rows:
        return {}
    keys = set()
    for r in rows:
        keys |= set(r)
    out = {}
    for k in sorted(keys):
        vals = [r[k] for r in rows if r.get(k) is not None]
        if not vals:
            out[k] = None
        elif all(isinstance(v, int) for v in vals) and len(set(vals)) == 1:
            out[k] = vals[0]
        else:
            out[k] = round(sum(vals) / len(vals), 4)
    return out
