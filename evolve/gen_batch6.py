#!/usr/bin/env python3
"""Batch 6 (Sep 9): cost-structure hypotheses from losing-seed replay mining
(hands re-hired daily at fib cost; wheat self-supply; feed-cost-aware feeding)."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

# hands cap: the 13th/14th hire cost fib(12)+fib(13) = $377/day
write("B6_01_HANDS12", rep(src, "MAX_HANDS = 14", "MAX_HANDS = 12"))
write("B6_02_HANDS11", rep(src, "MAX_HANDS = 14", "MAX_HANDS = 11"))
write("B6_03_HANDS10", rep(src, "MAX_HANDS = 14", "MAX_HANDS = 10"))

# marginal-value hiring: stop hiring when the next hire's fib cost exceeds what a hand-day is worth
# (estimated from yesterday's realized sales revenue per hand, tracked in S)
c = rep(src, '''    target = _load_model(v, seeds_on_hand, n_total, pending_place, day)
    S["hires_target"] = target
    n, _ = _hire_plan(target, n_hands, me["hires_today"], max(0.0, cash + revenue_est - wheat_cost))''',
'''    target = _load_model(v, seeds_on_hand, n_total, pending_place, day)
    # marginal-value cap: a hand-day is worth ~ (today's expected sales) / hands; don't pay a fib cost above that
    per_hand_value = (revenue_est + 200.0) / max(1, target)
    cap = 0
    while cap < target and _fib(cap) <= per_hand_value * 0.5:
        cap += 1
    if day >= 2:
        target = max(KNOBS["min_hands"], min(target, cap))
    S["hires_target"] = target
    n, _ = _hire_plan(target, n_hands, me["hires_today"], max(0.0, cash + revenue_est - wheat_cost))''')
write("B6_04_MARGINAL_HIRE", c)

# wheat self-supply for feed: grow ~0.5 tile per animal instead of buying feed at $30-50/unit
write("B6_05_WHEAT_SELF_05", rep(src, "'wheat_per_animal': 0.0", "'wheat_per_animal': 0.5"))
write("B6_06_WHEAT_SELF_10", rep(src, "'wheat_per_animal': 0.0", "'wheat_per_animal': 1.0"))

# feed-cost-aware: skip feeding an animal whose product price is below the wheat price (negative-margin animal)
c = rep(src, '''def _feed_useful(t,day):
    if t.get("fed_today",False) or day>=29:return False''',
'''def _feed_useful(t,day):
    if t.get("fed_today",False) or day>=29:return False
    pr = S.get("prices") or {}
    prod = PRODUCT_OF.get(t.get("animal"))
    if prod and pr.get(prod, 999) < pr.get("WHEAT", 0) * 1.2 and day >= 12:
        return False  # product is worth less than its feed: let it lapse''')
c = rep(c, '''    prices = obs["market"]["prices"]
    cash = me["money"]
    quads = len(me["unlocked_quadrants"])''', '''    prices = obs["market"]["prices"]
    S["prices"] = dict(prices)
    cash = me["money"]
    quads = len(me["unlocked_quadrants"])''')
write("B6_07_FEED_COST_AWARE", c)
