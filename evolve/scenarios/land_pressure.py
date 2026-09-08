"""Scenario 4 -- land pressure (AGE-333).

Question: does the agent recognise genuine capacity pressure?

World
-----
The mirror image of the other four: here expansion is the *right* answer and the failure is
timidity. `townShopUnlockInterval: 1` unlocks a shop instance every day until the engine's cap of
eight is reached on day 8, and `townShopSellInterval: 2` doubles how often each one consumes, so
town demand runs far ahead of anything one quadrant can grow. Prices spike accordingly (several
crops have hinge-shaped scarcity curves that run away once demand outstrips supply).
`startingMoney: 12000` puts three quadrants (1000 + 2000 + 4000) and a full crew inside reach from
day 1, so nothing but the agent's own reading of the situation stands between it and the demand.

Verdict
-------
FAIL if the farm is still on one quadrant at midgame, or if it sat on cash through the opening
window instead of converting it into capacity. Either is money left on the table: the demand and
the capital were both there and the agent under-produced anyway.
"""
from __future__ import annotations

from spec import Criterion, Scenario
from metrics import EARLY_TROUGH, MIDGAME_DAY

# The cheapest extra quadrant is $1000. A farm that never lets its cash fall below four times that
# through days 3-12, while demand is running away from it, is hoarding rather than investing.
MAX_IDLE_CAPITAL = 4000
MIN_LAND_AT_MIDGAME = 2


def scenario():
    return Scenario(
        name="land_pressure",
        question="Does the agent recognise genuine capacity pressure and expand to meet it?",
        description=("Eight town shop instances by day 8, each consuming twice as often as normal, "
                     "against $12k of opening capital. Demand outruns one quadrant immediately and "
                     "three quadrants are affordable from day 1."),
        config={
            "startingMoney": 12000,
            "townShopUnlockInterval": 1,           # a shop instance a day up to the engine's cap of 8
            "townShopSellInterval": 2,             # each instance consumes twice as often as default
        },
        seeds=(1, 2, 3),
        fail_when=(
            Criterion("land_at_midgame", "<", MIN_LAND_AT_MIDGAME,
                      f"still farming one quadrant on day {MIDGAME_DAY} with capital in hand and "
                      f"town demand running away"),
            Criterion("early_cash_trough", ">", MAX_IDLE_CAPITAL,
                      f"cash never fell below ${MAX_IDLE_CAPITAL} across days "
                      f"{EARLY_TROUGH[0]}-{EARLY_TROUGH[1] - 1}: capital held instead of turned into "
                      f"capacity while demand was unmet"),
        ),
        report_metrics=("land_at_midgame", "land_final", "peak_plants", "total_revenue",
                        "final_cash"),
    )
