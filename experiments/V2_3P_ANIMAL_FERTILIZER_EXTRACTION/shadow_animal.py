"""V2_3P shadow reimplementation of V9.3's animal setup/maintenance and
fleet-expansion-gate logic.

HARD RULE: this module must NEVER import or call any *decision* function
from main_v9.3_fertilize.py (animal_setup_action, animal_maintenance_action,
animal_reconcile, _pasture_priority, _animal_expansion_feasible,
_sheep_expansion_feasible, economy, _agent). It is a from-scratch
transcription, built only by reading the source and the game README, so
that comparing its output turn-by-turn against instrumented oracle calls is
an independent check, not a tautology.

It MAY reuse static, non-decision constants (cost tables, thresholds) that
are just data, not control flow -- these are imported explicitly and
listed in CONSTANTS_IMPORTED_FROM_ORACLE in the extraction report.
"""
import math


# =====================================================================
# Track A: animal maintenance (_pasture_priority + animal_maintenance_action)
# =====================================================================

def pasture_priority(pos, farmer_pos, tile, dist_fn):
    fed = tile.get("fed_today", True)
    urgent = (not fed) and tile.get("consecutive_unfed", 0) >= 1
    if urgent:
        rank = 0
    elif not fed:
        rank = 1
    elif tile.get("yield_units", 0) > 0:
        rank = 2
    elif not tile.get("cared_today", True):
        rank = 3
    elif tile.get("fertilizer_available", False):
        rank = 4
    else:
        rank = 5
    return (rank, dist_fn(pos, farmer_pos))


def animal_maintenance_action(pos, view, shed, carry, day, hour, exclude, critical_only,
                               *, dist_fn, step_toward_fn, nearest_center_fn,
                               animal_products, product_deposit_at, feed_carry_target,
                               center_tiles, liquidate_day):
    candidates = [(p, t) for p, t in view["my_pastures"] if p not in exclude]
    if critical_only:
        candidates = [(p, t) for p, t in candidates if not t.get("fed_today", True)]
    if not candidates:
        return None, None
    (ppos, tile) = min(candidates, key=lambda pt: pasture_priority(pt[0], pos, pt[1], dist_fn))

    needs_feed = not tile.get("fed_today", True)
    needs_care = (not critical_only) and (not tile.get("cared_today", True))
    has_yield = (not critical_only) and tile.get("yield_units", 0) > 0
    has_fert = (not critical_only) and tile.get("fertilizer_available", False)
    urgent_feed = needs_feed and tile.get("consecutive_unfed", 0) >= 1
    claim = ppos if (needs_feed or needs_care or has_yield or has_fert) else None

    carry_wheat = carry.get("WHEAT", 0)
    carry_products = {} if critical_only else {i: carry.get(i, 0) for i in animal_products if carry.get(i, 0) > 0}
    deposit_due = sum(carry_products.values()) >= product_deposit_at or (
        carry_products and (needs_feed and carry_wheat == 0))
    fetch_wheat_due = needs_feed and carry_wheat == 0 and shed.get("WHEAT", 0) > 0

    if pos == ppos:
        if needs_feed and carry_wheat > 0:
            return ["FEED"], claim
        if has_yield:
            return ["HARVEST"], claim
        if needs_care:
            return ["CARE"], claim
        if has_fert:
            return ["COLLECT_FERTILIZER"], claim

    if pos in center_tiles:
        if fetch_wheat_due and urgent_feed:
            return ["PICKUP", "WHEAT", min(feed_carry_target, shed.get("WHEAT", 0))], claim
        if carry_products:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]], claim
        if fetch_wheat_due:
            return ["PICKUP", "WHEAT", min(feed_carry_target, shed.get("WHEAT", 0))], claim

    if fetch_wheat_due and urgent_feed:
        return [step_toward_fn(pos, nearest_center_fn(pos))], claim
    if fetch_wheat_due or deposit_due:
        return [step_toward_fn(pos, nearest_center_fn(pos))], claim
    if (needs_feed and carry_wheat > 0) or has_yield or needs_care or has_fert:
        return [step_toward_fn(pos, ppos)], claim

    if day >= liquidate_day and carry_products:
        if pos in center_tiles:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]], claim
        return [step_toward_fn(pos, nearest_center_fn(pos))], claim

    return None, None


# =====================================================================
# Track A: animal setup (multi-turn build state machine)
# =====================================================================

def animal_setup_action(pos, view, shed, farmer_carry, plan, day, hour, reserved_sites, exclude_sites,
                         *, dist_fn, step_toward_fn, nearest_center_fn, center_tiles):
    species = plan["species"]
    stage = plan["stage"]
    if stage in ("NONE", "ORDERED", "ABANDONED", "ACTIVE"):
        return None

    carrying = farmer_carry.get(species, 0) > 0
    site = plan.get("site")
    if site is None or (site not in view["empty"] and site not in view["empty_pastures"]):
        candidates = [t for t in (view["empty_pastures"] or view["empty"])
                      if t not in center_tiles and t not in exclude_sites]
        if not candidates:
            return None
        pool = [t for t in reserved_sites if t in candidates] or candidates
        site = min(pool, key=lambda p2: dist_fn(p2, nearest_center_fn(p2)))
        plan["site"] = site  # NOTE: shadow mutates its OWN plan copy only

    if site not in view["empty_pastures"]:
        if pos != site:
            return [step_toward_fn(pos, site)]
        return ["BUILD_PASTURE"]

    if not carrying:
        if shed.get(species, 0) == 0:
            return None
        center = nearest_center_fn(pos)
        if pos not in center_tiles:
            return [step_toward_fn(pos, center)]
        return ["PICKUP", species, 1]

    if pos != site:
        return [step_toward_fn(pos, site)]
    return ["PLACE", species]


# =====================================================================
# Track D upstream: fleet-expansion gates (species/target selection input)
# =====================================================================

def pending_animal_work(view):
    return sum(1 for _pos, t in view["my_pastures"]
               if (not t.get("fed_today", True)) or t.get("yield_units", 0) > 0
                  or (not t.get("cared_today", True)) or t.get("fertilizer_available", False))


def animal_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads, day,
                               *, live_price_fn, reserved_sites,
                               experiment_max_fleet, feed_carry_target,
                               expansion_wheat_budget_frac, animal_work_weight,
                               hand_target_max, crop_neglect_tasks_per_hand,
                               expansion_min_crop_tiles_per_quad):
    if n_animals >= experiment_max_fleet:
        return False
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return False
    next_target_wheat = (n_animals + 1) * 2 + feed_carry_target
    have = shed.get("WHEAT", 0)
    shortfall = max(0, next_target_wheat - have)
    shortfall_cost = shortfall * live_price_fn(obs, "WHEAT")
    if shortfall_cost > expansion_wheat_budget_frac * max(budget, 1):
        return False
    animal_work = pending_animal_work(view)
    neglect_work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"])
    crop_work = neglect_work + len(view["empty"])
    projected_work = crop_work + (animal_work + 1) * animal_work_weight
    if math.ceil(projected_work / 5) > hand_target_max:
        return False
    if neglect_work > n_hands * crop_neglect_tasks_per_hand:
        return False
    available_for_crops = len(view["empty"]) - len(reserved_sites) - 1
    if available_for_crops < expansion_min_crop_tiles_per_quad * quads:
        return False
    return True


def sheep_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads, day,
                              *, live_price_fn, reserved_sites, i0,
                              experiment_max_fleet, feed_carry_target,
                              expansion_wheat_budget_frac, animal_work_weight,
                              hand_target_max, sheep_hand_headroom,
                              crop_neglect_tasks_per_hand, expansion_min_crop_tiles_per_quad):
    if n_animals >= experiment_max_fleet:
        return False
    if obs["market"]["inventory"].get("WOOL", i0) >= i0 + 30:
        return False
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return False
    next_target_wheat = (n_animals + 1) * 2 + feed_carry_target
    have = shed.get("WHEAT", 0)
    shortfall = max(0, next_target_wheat - have)
    shortfall_cost = shortfall * live_price_fn(obs, "WHEAT")
    if shortfall_cost > expansion_wheat_budget_frac * max(budget, 1):
        return False
    animal_work = pending_animal_work(view)
    neglect_work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"])
    crop_work = neglect_work + len(view["empty"])
    projected_work = crop_work + (animal_work + 1) * animal_work_weight
    if math.ceil(projected_work / 5) > hand_target_max + sheep_hand_headroom:
        return False
    if neglect_work > n_hands * crop_neglect_tasks_per_hand:
        return False
    available_for_crops = len(view["empty"]) - len(reserved_sites) - 1
    if available_for_crops < expansion_min_crop_tiles_per_quad * quads:
        return False
    return True
