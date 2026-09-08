"""Scenario 1 -- unsupported livestock (AGE-333).

Question: does the agent expand livestock when there is no buyer capacity for animal products?

World
-----
`townShopUnlockInterval: 30` means no town shop ever unlocks, so the *only* buyer of MILK, WOOL
and EGG is the town center, which pulls one unit of each per day. That is the whole animal-product
demand of the season: roughly 30 units per product, against a herd of six cows that alone produces
three MILK a day.

The headline price is deliberately generous -- 2.5x the standard base -- and, because market price
is a pure function of inventory, that is exactly what the agent sees on days 0-3 when it decides
how big a herd to buy, before a single animal has produced anything. The glut curve underneath it
is brutal (`T: 10`, linear): ten units above the starting inventory takes the price to the floor,
and only the town center's one-a-day pull ever brings it back. So the bait is real and the capacity
behind it is not.

Crops are held at a flat, fair price (huge `T`, no scarcity or glut term) so the alternative
allocation is unambiguously available and the scenario tests livestock sizing rather than general
market savvy.

Verdict
-------
PASS if the herd stays inside what the market supports (<= 3 animals), or if the herd it did build
earned back its carry cost. FAIL if it built a herd whose products the market could not absorb --
the feed and capital are then trapped in animals that produce inventory nobody buys.
"""
from __future__ import annotations

from spec import Criterion, Scenario
from metrics import ANIMAL_UNIT_COST

CROPS = ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")
ANIMAL_BASE = {"MILK": 160, "WOOL": 200, "EGG": 50}   # kaggriculture.MARKET_PARAMS bases
PRICE_BAIT = 2.5          # headline animal-product price, as a multiple of the standard base
ABSORPTION_UNITS = 10     # units above the opening inventory that take the price to the floor

# An animal has to clear more than its purchase price to be worth owning: it also eats about one
# WHEAT a day. 700 is the purchase price plus a token contribution to feed -- a low bar on purpose,
# so a FAIL means the herd was clearly unsupported rather than merely marginal.
MIN_REVENUE_PER_ANIMAL = 700
SUPPORTED_HERD = 3        # town-center demand is ~1 unit/product/day; that sustains about this many


def _flat_crops():
    """Crop price pinned at base: the market absorbs any volume without scarcity or glut."""
    return {c: {"T": 100000, "below_target": 0.0, "above_target": 0.0} for c in CROPS}


def _baited_animals():
    return {k: {"base": int(b * PRICE_BAIT), "T": ABSORPTION_UNITS,
                "below_func": "linear", "below_target": 0.0,
                "above_func": "linear", "above_target": 1.0}
            for k, b in ANIMAL_BASE.items()}


def scenario():
    return Scenario(
        name="unsupported_livestock",
        question="Does the agent expand livestock when there is no buyer capacity?",
        description=(f"No town shops unlock all season, so animal products have only the town "
                     f"center's one-unit-a-day pull behind them. Their headline price is "
                     f"{PRICE_BAIT}x base to tempt an early herd; {ABSORPTION_UNITS} units of glut "
                     f"floors it. Crops sell at a flat fair price."),
        config={
            "townShopUnlockInterval": 30,          # 30-day season: no shop instance ever unlocks
            "marketParams": {**_flat_crops(), **_baited_animals()},
        },
        seeds=(1, 2, 3),
        exempt_when=(
            Criterion("peak_animals", "<=", SUPPORTED_HERD,
                      f"herd stayed inside the ~{SUPPORTED_HERD} animals town-center demand supports"),
        ),
        fail_when=(
            Criterion("animal_revenue_per_animal", "<", MIN_REVENUE_PER_ANIMAL,
                      f"each animal earned less than its ${ANIMAL_UNIT_COST} purchase price plus feed, "
                      f"so the herd trapped capital in products the market could not absorb"),
        ),
        report_metrics=("peak_animals", "animal_revenue", "crop_revenue", "final_cash"),
        notes=("The ticket's 'milk/wool shops removed or drawn very late' is implemented by "
               "suppressing town shop unlocks entirely -- the engine draws shops at random and "
               "offers no per-shop control, so removing all of them is the only deterministic way "
               "to guarantee no animal-product buyer appears."),
    )
