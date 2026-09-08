"""Scenario 2 -- idle labor (AGE-333).

Question: does the agent hire workers that will sit idle?

World
-----
`startingMoney: 40000` removes the cash constraint that normally paces hiring, and
`farmHandCostMult: 0` makes every hire free, so nothing but the agent's own judgement limits the
size of the crew. Against that, the work available is capped: no town shop unlocks all season and
every price is flat, so the only demand is the town center's one unit per product per day and
there is no scarcity spike to chase by planting more. Capital is abundant, labor is free, and the
productive footprint the world can actually reward is small.

Verdict
-------
PASS if the crew stays small, or if the hands it did hire found work. FAIL if a large share of
unit-turns is PASS, or if productive actions per hand-day collapse -- both are the signature of
hands hired past the point where the farm has anything for them to do.
"""
from __future__ import annotations

from spec import Criterion, Scenario

CROPS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")
ANIMAL_BASE = {"MILK": 160, "WOOL": 200, "EGG": 50}

# Baseline for this chassis on a normal season is idle_share ~0.09-0.16 and ~9 work-turns per
# hand-day (evolve/scenarios/README.md records the measurement). The thresholds sit outside that
# band so an ordinary crew passes and only a genuinely over-staffed one trips them.
MAX_IDLE_SHARE = 0.25
MIN_WORK_PER_HAND_DAY = 6.0
SMALL_CREW = 4            # a farmer plus this many hands is never "over-hired"


def _flat_market():
    m = {c: {"T": 100000, "below_target": 0.0, "above_target": 0.0} for c in CROPS}
    m.update({k: {"base": b, "T": 20, "below_func": "linear", "below_target": 0.0,
                  "above_func": "linear", "above_target": 1.0} for k, b in ANIMAL_BASE.items()})
    return m


def scenario():
    return Scenario(
        name="idle_labor",
        question="Does the agent hire workers that will sit idle?",
        description=("Cash is abundant ($40k) and hires are free (farmHandCostMult 0), but no town "
                     "shop unlocks and every price is flat, so the footprint worth servicing is "
                     "small. Nothing except the agent's own sizing limits the crew."),
        config={
            "startingMoney": 40000,
            "farmHandCostMult": 0,                 # hire cost = 0 * fib(n) = free, all season
            "townShopUnlockInterval": 30,
            "marketParams": _flat_market(),
        },
        seeds=(1, 2, 3),
        exempt_when=(
            Criterion("max_hands", "<=", SMALL_CREW,
                      f"never ran more than {SMALL_CREW} hands, so no crew was over-hired"),
        ),
        fail_when=(
            Criterion("idle_share", ">=", MAX_IDLE_SHARE,
                      "a quarter or more of all unit-turns were PASS: units with nothing to do"),
            Criterion("work_per_hand_day", "<", MIN_WORK_PER_HAND_DAY,
                      "productive actions per hand-day fell below what one hand can be expected to "
                      "return, so the marginal hire was not earning its place"),
        ),
        report_metrics=("max_hands", "hand_days", "work_turns", "peak_plants", "peak_animals"),
    )
