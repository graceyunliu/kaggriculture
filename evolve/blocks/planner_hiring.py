def _hire_plan(target, have, hires_today, cash):
    """Return number of HIRE orders affordable now toward `target` hands."""
    n = 0
    spent = 0
    while have + n < target:
        c = _fib(hires_today + n)
        if spent + c > cash:
            break
        spent += c
        n += 1
    return n, spent


def _load_model(v, seeds_planned, n_animals_total, n_setup, day):
    load = LOAD_ANIMAL * n_animals_total
    load += LOAD_CROP_TASK * (len(v["urgent"]) + len(v["water"]) + len(v.get("wwater", [])) + len(v["harvest"]) + len(v["weeds"]) + seeds_planned)
    load += LOAD_SETUP * n_setup
    tgt = int(math.ceil(load / KNOBS["load_per_hand"]))
    floor = KNOBS["hands_early"] if (KNOBS["hands_early"] and day <= 10) else KNOBS["min_hands"]
    tgt = max(floor, min(MAX_HANDS, tgt))
    if day >= 29:
        tgt = min(tgt, 6)
    return tgt

