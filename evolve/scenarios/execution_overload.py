"""Scenario 5 -- execution overload (AGE-333).

Question: does expansion outrun the labour available to service it?

World
-----
`startingMoney: 25000` funds a large crop and animal footprint from the opening, while
`farmHandCostMult: 200` turns the hire ladder from pocket change into a real budget line: the
n-th hire of a day costs 200*fib(n), so a fifth hand costs $1000 and an eighth $4200. Hands stay
available but stop being free, which is exactly the "capped hands" of the ticket -- the agent can
still buy a big crew, it just has to decide to.

Verdict
-------
PASS if the agent either scales its crew to match the footprint it builds, or keeps the footprint
inside what its crew can service. FAIL on the marks of a farm that outgrew its labour: day-start
FEED/CARE/WATER/HARVEST obligations going unserviced, animals starving, animals escaping.
"""
from __future__ import annotations

from spec import Criterion, Scenario

# Baseline for this chassis on a normal season is chore_completion ~0.93 with 0 escapes
# (evolve/scenarios/README.md records the measurement). These thresholds allow real slippage under
# a genuine labour squeeze and fire only when service is actually breaking down.
MIN_CHORE_COMPLETION = 0.75
MAX_ESCAPES = 3
MAX_MISSED_FEED = 20


def scenario():
    return Scenario(
        name="execution_overload",
        question="Does expansion cause watering/feeding/harvesting failures?",
        description=("$25k of opening capital funds a large footprint while farmHandCostMult 200 "
                     "makes the hire ladder expensive (a fifth hand costs $1000, an eighth $4200). "
                     "Full 30-day season."),
        config={
            "startingMoney": 25000,
            "farmHandCostMult": 200,               # hire n of the day costs 200 * fib(n)
        },
        seeds=(1, 2, 3),
        fail_when=(
            Criterion("chore_completion", "<", MIN_CHORE_COMPLETION,
                      "a quarter of the day-start FEED/CARE/WATER/HARVEST obligations went "
                      "unserviced: the footprint outran the crew"),
            Criterion("escapes", ">=", MAX_ESCAPES,
                      "animals escaped, which only happens after repeated missed care"),
            Criterion("missed_feed", ">=", MAX_MISSED_FEED,
                      "animal-days spent unfed: feeding lost to the servicing backlog"),
        ),
        report_metrics=("max_hands", "peak_plants", "peak_animals", "missed_water",
                        "chore_completion", "final_cash"),
    )
