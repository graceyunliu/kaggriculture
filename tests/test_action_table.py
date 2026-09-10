"""Measurement contract for the AGE-359 action timing table.

The action table is the substrate the marginal-consequence work will reason from, so
its extraction rules need to be pinned rather than rediscovered. These tests are a
smoke test, not coverage: they fix the contract for the pieces later analysis depends
on, using hand-built traces whose expected output can be computed by hand.

Epistemic note, deliberately encoded here as well as in the module docstring: the
action table is OBSERVATIONAL. These tests assert that extraction is faithful to the
trace. They assert nothing about whether a timing correlation is causal.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

import evolve.chassis as chassis  # noqa: E402
from evolve.action_table import (  # noqa: E402
    action_table_from_trace,
    compute_postponement,
    optimal_day_for_sell,
)


def _trace(n_days=6, **over):
    """A minimal well-formed trace: flat, no events, then override the series you care about."""
    base = {
        "cash": [1000] * n_days,
        "networth": [1000] * n_days,
        "sales_rev": [0] * n_days,
        "buys_cost": [0] * n_days,
        "sales_by_product": [{} for _ in range(n_days)],
        "animals": [0] * n_days,
        "plants": [0] * n_days,
        "land": [1] * n_days,
        "shed_units": [0] * n_days,
        "carried_units": [0] * n_days,
        "missed_water": [0] * n_days,
        "missed_feed": [0] * n_days,
        "hands": [1] * n_days,
        "escapes": [0] * n_days,
        "weeds_new": [0] * n_days,
    }
    base.update(over)
    return base


class TestEmptyAndDegenerate(unittest.TestCase):
    def test_empty_trace_returns_empty_shape(self):
        out = action_table_from_trace({})
        self.assertEqual(out, {"action_table": {}, "context": {}})

    def test_flat_trace_produces_no_events(self):
        out = action_table_from_trace(_trace())
        self.assertEqual(out["action_table"], {})
        self.assertIn("final_networth", out["context"])

    def test_output_is_json_round_trippable(self):
        """The table is persisted via db.update(...) and re-read by export_archive."""
        out = action_table_from_trace(
            _trace(
                land=[1, 1, 2, 2, 2, 2],
                sales_by_product=[{}, {}, {}, {"MELON": 5}, {}, {}],
                sales_rev=[0, 0, 0, 400, 0, 0],
                missed_feed=[0, 0, 1, 0, 0, 0],
            )
        )
        self.assertEqual(json.loads(json.dumps(out)), out)


class TestBuyLand(unittest.TestCase):
    def test_event_extracted_on_the_delta_day(self):
        out = action_table_from_trace(_trace(land=[1, 1, 2, 2, 2, 2]))
        events = out["action_table"]["BUY_LAND"]
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["day"], 2)
        self.assertEqual(events[0]["count"], 1)

    def test_cumulative_cost_uses_the_price_ladder(self):
        """Two quadrants bought at once must cost the sum of the next two rungs, not 2x one."""
        out = action_table_from_trace(_trace(land=[1, 1, 3, 3, 3, 3]))
        ev = out["action_table"]["BUY_LAND"][0]
        expected = chassis.LAND_PRICES[0] + chassis.LAND_PRICES[1]
        self.assertEqual(ev["cost"], expected)

    def test_price_ladder_is_indexed_off_land_already_owned(self):
        """A later purchase is dearer than an earlier one: cost must depend on owned_before."""
        early = action_table_from_trace(_trace(land=[1, 2, 2, 2, 2, 2]))
        late = action_table_from_trace(_trace(land=[2, 2, 2, 3, 3, 3]))
        self.assertLess(
            early["action_table"]["BUY_LAND"][0]["cost"],
            late["action_table"]["BUY_LAND"][0]["cost"],
        )

    def test_purchase_beyond_the_ladder_does_not_raise(self):
        out = action_table_from_trace(_trace(land=[1, 9, 9, 9, 9, 9]))
        self.assertEqual(len(out["action_table"]["BUY_LAND"]), 1)

    def test_land_loss_is_not_an_event(self):
        out = action_table_from_trace(_trace(land=[3, 3, 2, 2, 2, 2]))
        self.assertNotIn("BUY_LAND", out["action_table"])


class TestSell(unittest.TestCase):
    def test_products_are_extracted_with_quantities(self):
        out = action_table_from_trace(
            _trace(
                sales_by_product=[{}, {}, {}, {"MELON": 5, "WHEAT": 3}, {}, {}],
                sales_rev=[0, 0, 0, 400, 0, 0],
            )
        )
        events = out["action_table"]["SELL"]
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["day"], 3)
        self.assertEqual(events[0]["items"], {"MELON": 5, "WHEAT": 3})

    def test_revenue_comes_from_sales_rev_not_from_summing_quantities(self):
        """Quantities and revenue are different units; revenue must be the cash figure."""
        out = action_table_from_trace(
            _trace(
                sales_by_product=[{}, {}, {}, {"MELON": 5, "WHEAT": 3}, {}, {}],
                sales_rev=[0, 0, 0, 400, 0, 0],
            )
        )
        self.assertEqual(out["action_table"]["SELL"][0]["revenue"], 400)

    def test_animal_products_survive_extraction(self):
        out = action_table_from_trace(
            _trace(
                sales_by_product=[{}, {"MILK": 4, "WOOL": 2}, {}, {}, {}, {}],
                sales_rev=[0, 300, 0, 0, 0, 0],
            )
        )
        self.assertEqual(
            out["action_table"]["SELL"][0]["items"], {"MILK": 4, "WOOL": 2}
        )

    def test_empty_day_is_not_a_sell_event(self):
        out = action_table_from_trace(_trace(sales_rev=[0, 0, 99, 0, 0, 0]))
        self.assertNotIn("SELL", out["action_table"])


class TestMissedSignals(unittest.TestCase):
    def test_missed_feed_and_water_recorded_per_day_with_counts(self):
        out = action_table_from_trace(
            _trace(missed_feed=[0, 2, 0, 1, 0, 0], missed_water=[0, 0, 3, 0, 0, 0])
        )
        feed = out["action_table"]["FEED_MISSED"]
        water = out["action_table"]["WATER_MISSED"]
        self.assertEqual([(e["day"], e["count"]) for e in feed], [(1, 2), (3, 1)])
        self.assertEqual([(e["day"], e["count"]) for e in water], [(2, 3)])


class TestPostponement(unittest.TestCase):
    """Single source of truth: report.py must not re-derive any of this inline."""

    def test_known_input_gives_known_output(self):
        self.assertEqual(compute_postponement("BUY_LAND", 10), 4)
        self.assertEqual(compute_postponement("BUY_ANIMAL", 5), 3)
        self.assertEqual(compute_postponement("BUY_SEED", 5), 3)

    def test_never_negative_when_action_is_early(self):
        for atype in ("BUY_ANIMAL", "BUY_SEED", "BUY_LAND"):
            self.assertEqual(compute_postponement(atype, 0), 0, atype)

    def test_missed_days_are_their_own_postponement(self):
        self.assertEqual(compute_postponement("FEED_MISSED", 7), 7)
        self.assertEqual(compute_postponement("WATER_MISSED", 7), 7)

    def test_sell_defers_to_optimal_day_for_sell(self):
        self.assertEqual(compute_postponement("SELL", 20), 0)

    def test_unknown_action_type_is_penalty_free(self):
        self.assertEqual(compute_postponement("NOT_AN_ACTION", 12), 0)

    def test_optimal_sell_day_splits_melon_from_the_rest(self):
        self.assertEqual(optimal_day_for_sell({"MELON": 5}), 10)
        self.assertEqual(optimal_day_for_sell({"WHEAT": 3}), 5)
        self.assertEqual(optimal_day_for_sell({"WHEAT": 3, "MELON": 1}), 10)
        self.assertEqual(optimal_day_for_sell({}), 5)


class TestContext(unittest.TestCase):
    def test_whole_game_context_reports_the_slicing_keys(self):
        out = action_table_from_trace(
            _trace(n_days=30, animals=[0] * 15 + [11] * 15, networth=[1000] * 29 + [50000])
        )
        ctx = out["context"]
        for key in ("animals_d15", "final_networth", "game_day"):
            self.assertIn(key, ctx)
        self.assertEqual(ctx["animals_d15"], 11)
        self.assertEqual(ctx["final_networth"], 50000)

    def test_per_event_context_is_attached(self):
        out = action_table_from_trace(_trace(land=[1, 1, 2, 2, 2, 2]))
        self.assertIsInstance(out["action_table"]["BUY_LAND"][0]["context"], dict)


if __name__ == "__main__":
    unittest.main()
