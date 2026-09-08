"""Scenario 3 -- late-game expansion (AGE-333).

Question: does the agent understand remaining-game value?

World
-----
`startingMoney: 60000` means capital is never the reason an expansion does not happen, and
`townShopUnlockInterval: 8` pushes the town's demand -- and therefore the season's revenue -- into
the back half, so the agent is at its richest exactly when the payback window has closed. Land is
still unbought or half-bought, the herd is still under its cap, and everything is affordable. The
only argument against buying is that there is nothing left to earn it back.

Verdict
-------
FAIL if capital is committed on day 23 or later to assets that cannot return inside the remaining
seven days: a quadrant (LAND_PRICES 1000/2000/4000, and empty tiles still have to be planted and
grown), or animals (a GOOSE first yields 4 days after placement, a COW 8). PASS otherwise.

Deviation from the ticket
-------------------------
The ticket describes a day-23 start. The engine has no day-offset override and the scope of this
ticket is explicitly "not a modification to the main engine", so the scenario plays the full season
and evaluates only the day-23..29 window -- the same question about the same seven days, reached by
playing to them instead of by starting there. The cost is that the candidate arrives at day 23 with
a farm it built itself rather than a fixed handed-over position; the benefit is that no engine
change is needed and the measured behaviour is the behaviour the candidate would really exhibit.
"""
from __future__ import annotations

from spec import Criterion, Scenario
from metrics import ANIMAL_UNIT_COST, LATE_GAME_START

# One goose bought on day 23 (300, first yield day 27) is a defensible marginal call; a quadrant
# (>= 1000) or a second animal is not. The threshold sits between those two cases.
MAX_LATE_CAPITAL = 800


def scenario():
    return Scenario(
        name="late_expansion",
        question="Does the agent understand remaining-game value?",
        description=(f"Capital is abundant ($60k) and the town's demand arrives late "
                     f"(townShopUnlockInterval 8), so the agent is richest when the payback window "
                     f"has closed. Measured on days {LATE_GAME_START}-29 only."),
        config={
            "startingMoney": 60000,
            "townShopUnlockInterval": 8,           # shops unlock on days 8, 16 and 24 only
        },
        seeds=(1, 2, 3),
        fail_when=(
            Criterion("late_capital_committed", ">", MAX_LATE_CAPITAL,
                      f"cash sunk on day {LATE_GAME_START}+ into land or animals "
                      f"(${ANIMAL_UNIT_COST}/animal) that cannot pay back in the days remaining"),
        ),
        report_metrics=("late_land_spend", "late_animals_added", "land_final", "peak_animals",
                        "final_cash"),
        notes=("Full 30-day season with a day-23..29 evaluation window; see the module docstring "
               "for why this replaces the ticket's literal day-23 start."),
    )
