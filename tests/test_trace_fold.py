"""fold_trace_to_summary must survive every field in SUMMARY_FIELDS, whatever its type.

Why this file exists. AGE-359 added `sales_by_product` to SUMMARY_FIELDS. That field is a
list of dicts, one per day, while fold_trace_to_summary averaged every field with
`sum(vals) / len(vals)`. So the fold raised

    TypeError: unsupported operand type(s) for +: 'int' and 'dict'

for every candidate. cascade.collect_trajectory_summary calls the fold for each alive
candidate, and the loop catches and logs the exception rather than stopping, so the only
symptom was one "trajectory/classify failed" line per candidate in the log. Between
9237323 and the fix, no candidate got a trajectory_summary or a failure_profile: AGE-331
and AGE-332 classification were entirely dead, and nothing failed loudly enough to notice.

The regression was cheap to make and expensive to spot, so the contract test that matters
is not "dicts work now" but `test_every_summary_field_folds`: it folds a trace carrying
EVERY name in SUMMARY_FIELDS and fails if any one of them raises. Add a field of a new
type to SUMMARY_FIELDS without teaching the fold about it and that test goes red, instead
of classification going quietly dark for a six-hour run.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

from evolve.trace import SUMMARY_FIELDS, fold_trace_to_summary  # noqa: E402


class TestNumericFields(unittest.TestCase):
    """Pre-existing behaviour. Pinned so the dict handling can't quietly change it."""

    def test_numeric_fields_are_averaged_day_by_day(self):
        a = {"cash": [10, 20, 30], "sales_rev": [0, 5, 10]}
        b = {"cash": [20, 40, 60], "sales_rev": [0, 15, 20]}
        out = fold_trace_to_summary([a, b], seeds=[1, 2], fields=["cash", "sales_rev"])
        self.assertEqual(out["cash"], [15.0, 30.0, 45.0])
        self.assertEqual(out["sales_rev"], [0.0, 10.0, 15.0])
        self.assertEqual(out["seeds"], [1, 2])
        self.assertEqual(out["n_days"], 3)

    def test_none_values_are_skipped_not_counted_as_zero(self):
        a = {"cash": [10, None], "travel_per_task": [1.0, None]}
        b = {"cash": [20, 40], "travel_per_task": [2.0, 3.0]}
        out = fold_trace_to_summary([a, b], fields=["cash", "travel_per_task"])
        self.assertEqual(out["cash"], [15.0, 40.0])
        self.assertEqual(out["travel_per_task"], [1.5, 3.0])

    def test_n_days_is_the_shortest_trace(self):
        a = {"cash": [1, 2, 3, 4]}
        b = {"cash": [10, 20]}
        self.assertEqual(fold_trace_to_summary([a, b], fields=["cash"])["n_days"], 2)

    def test_no_traces_gives_empty_columns_for_every_field(self):
        out = fold_trace_to_summary([], seeds=[7])
        self.assertEqual(out["n_days"], 0)
        self.assertEqual(out["seeds"], [7])
        for f in SUMMARY_FIELDS:
            self.assertEqual(out[f], [], f)


class TestDictFields(unittest.TestCase):
    """AGE-359 sales_by_product: {item: qty} per day, averaged across seeds per key."""

    def test_dict_field_averages_per_key(self):
        a = {"cash": [0], "sales_by_product": [{"MELON": 4}]}
        b = {"cash": [0], "sales_by_product": [{"MELON": 6}]}
        out = fold_trace_to_summary([a, b], fields=["sales_by_product"])
        self.assertEqual(out["sales_by_product"], [{"MELON": 5.0}])

    def test_key_absent_on_one_seed_counts_as_zero_there(self):
        """MILK sold on one seed of two averages to half, not to its full value."""
        a = {"cash": [0], "sales_by_product": [{"MELON": 4}]}
        b = {"cash": [0], "sales_by_product": [{"MELON": 6, "MILK": 3}]}
        out = fold_trace_to_summary([a, b], fields=["sales_by_product"])
        self.assertEqual(out["sales_by_product"], [{"MELON": 5.0, "MILK": 1.5}])

    def test_empty_dict_days_are_kept_as_empty(self):
        a = {"cash": [0, 0], "sales_by_product": [{}, {"WHEAT": 2}]}
        b = {"cash": [0, 0], "sales_by_product": [{}, {}]}
        out = fold_trace_to_summary([a, b], fields=["sales_by_product"])
        self.assertEqual(out["sales_by_product"][0], {})
        self.assertEqual(out["sales_by_product"][1], {"WHEAT": 1.0})

    def test_single_trace_passes_dict_through_unchanged(self):
        a = {"cash": [0], "sales_by_product": [{"WOOL": 7}]}
        out = fold_trace_to_summary([a], fields=["sales_by_product"])
        self.assertEqual(out["sales_by_product"], [{"WOOL": 7.0}])

    def test_dict_and_numeric_fields_fold_in_the_same_call(self):
        a = {"cash": [10], "sales_by_product": [{"MELON": 4}]}
        b = {"cash": [20], "sales_by_product": [{"MELON": 6}]}
        out = fold_trace_to_summary([a, b], fields=["cash", "sales_by_product"])
        self.assertEqual(out["cash"], [15.0])
        self.assertEqual(out["sales_by_product"], [{"MELON": 5.0}])


class TestFieldContract(unittest.TestCase):
    def test_every_summary_field_folds(self):
        """The regression guard. Every name in SUMMARY_FIELDS must fold without raising.

        Add a field of a new type to SUMMARY_FIELDS and this fails here, loudly, instead of
        disabling trajectory/classify for every candidate with one log line per candidate.
        """
        n_days = 3
        samples = {"sales_by_product": [{"MELON": 2}] * n_days}
        trace = {f: samples.get(f, [1] * n_days) for f in SUMMARY_FIELDS}
        try:
            out = fold_trace_to_summary([trace, trace], seeds=[1, 2])
        except Exception as e:  # noqa: BLE001
            self.fail(f"fold_trace_to_summary raised {e!r}; a SUMMARY_FIELDS type is unhandled")
        for f in SUMMARY_FIELDS:
            self.assertIn(f, out, f)
            self.assertEqual(len(out[f]), n_days, f)

    def test_result_is_json_serializable(self):
        """cascade stores this via db.update(trajectory_summary=json.dumps(summary))."""
        n_days = 2
        samples = {"sales_by_product": [{"MELON": 2, "MILK": 1}] * n_days}
        trace = {f: samples.get(f, [1] * n_days) for f in SUMMARY_FIELDS}
        out = fold_trace_to_summary([trace, trace], seeds=[1, 2])
        self.assertEqual(json.loads(json.dumps(out)), out)

    def test_sales_by_product_is_still_in_summary_fields(self):
        """If this is ever removed, the action table loses its SELL source. Fail on purpose."""
        self.assertIn("sales_by_product", SUMMARY_FIELDS)


if __name__ == "__main__":
    unittest.main()
