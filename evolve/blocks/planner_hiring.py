def _hire_plan(target, have, hires_today, cash):
    """Return the affordable hires needed to reach the planner's hand target."""
    n = 0
    spent = 0
    while have + n < target:
        cost = _fib(hires_today + n)
        if spent + cost > cash:
            break
        spent += cost
        n += 1
    return n, spent


def _load_model(v, seeds_planned, n_animals_total, n_setup, day):
    """Conservative headcount for a complete day route (farmer is included)."""
    hard = len(v["urgent"]) + len(v.get("wwater", [])) + n_animals_total
    optional = len(v["water"]) + len(v["harvest"]) + len(v["weeds"]) + seeds_planned
    # A routed hand normally completes 8-10 chores after travel.  Setup is more
    # expensive and planting reserves a second action for same-day watering.
    actions = hard * 2 + optional + seeds_planned + n_setup * 4
    target = max(int(math.ceil(hard / 8.0)), int(math.ceil(actions / 10.0)))
    floor = KNOBS["hands_early"] if KNOBS["hands_early"] and day <= 10 else KNOBS["min_hands"]
    target = max(floor, target)
    if day <= 2:
        target = max(3, target)
    if day >= 29:
        target = min(target, 6)
    return min(MAX_HANDS, target)
