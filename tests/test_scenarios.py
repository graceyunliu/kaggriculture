"""Adversarial diagnostic scenarios (AGE-333).

Four things have to hold for the suite to be worth anything:

  * all five scenarios run on a candidate and produce pass/fail plus an explanation naming the
    metric that decided it;
  * the runner is separate from the cascade -- no import edge in either direction, and no value it
    produces reaches ranking;
  * verdicts are stored and queryable;
  * the criteria actually discriminate. The population currently passes idle_labor and
    late_expansion unanimously, which is only evidence about the population if the FAIL path is
    known to work, so each scenario is also run against a control agent carrying exactly the
    pathology it is meant to catch (evolve/scenarios/controls.py).

The end-to-end tests play real games and are the slow ones; they use a single seed.
"""
from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

import scenarios  # noqa: E402
from scenarios import controls, metrics, report as report_mod, runner, spec, store  # noqa: E402

C1 = ROOT / "candidates" / "C1.py"
FAST_SEEDS = (1,)

# Engine configuration keys kaggriculture.json declares. A scenario that sets anything else is
# silently ignored by the engine, so its world would not be the world its docstring describes.
ENGINE_CONFIG_KEYS = set(json.loads(
    (ROOT / "vendor" / "kaggle_environments_engine_master" / "kaggriculture.json").read_text()
)["configuration"])


class ScenarioDefinitionTests(unittest.TestCase):
    """The definitions are the readable part of the suite; keep them well-formed."""

    def test_five_scenarios_with_unique_names(self):
        scen = scenarios.all_scenarios()
        self.assertEqual(len(scen), 5)
        self.assertEqual(len(scen), len({s.name for s in scen}))
        self.assertEqual(scenarios.names(),
                         ["unsupported_livestock", "idle_labor", "late_expansion", "land_pressure",
                          "execution_overload"])

    def test_every_scenario_is_documented_and_thresholded(self):
        for sc in scenarios.all_scenarios():
            with self.subTest(sc.name):
                self.assertTrue(sc.question.strip(), "a scenario must state its question")
                self.assertTrue(sc.description.strip())
                self.assertTrue(sc.fail_when, "a scenario with no fail criterion can never fail")
                self.assertTrue(sc.seeds, "3-5 seeds per scenario")
                self.assertLessEqual(len(sc.seeds), 5)

    def test_configs_only_use_keys_the_engine_declares(self):
        for sc in scenarios.all_scenarios():
            with self.subTest(sc.name):
                unknown = set(sc.config) - ENGINE_CONFIG_KEYS
                self.assertFalse(unknown, f"{sc.name} sets configuration the engine ignores: {unknown}")

    def test_criteria_reference_metrics_the_extractor_produces(self):
        """A criterion on a metric metrics.py never emits would silently never trip."""
        produced = set(metrics.scenario_metrics(_synthetic_trace()))
        for sc in scenarios.all_scenarios():
            for c in sc.criteria_metrics():
                with self.subTest(scenario=sc.name, metric=c):
                    self.assertIn(c, produced)

    def test_selection_is_composable(self):
        self.assertEqual([s.name for s in scenarios.select(["idle_labor"])], ["idle_labor"])
        self.assertEqual(len(scenarios.select(None)), 5)
        with self.assertRaises(KeyError):
            scenarios.get("no_such_scenario")

    def test_unknown_operator_is_rejected_at_definition_time(self):
        with self.assertRaises(ValueError):
            spec.Criterion("idle_share", "=~", 1, "nonsense")


class VerdictLogicTests(unittest.TestCase):
    """spec.Scenario.evaluate, without playing a game."""

    def make(self, **kw):
        base = dict(name="t", question="q", description="d", config={},
                    fail_when=(spec.Criterion("idle_share", ">=", 0.25, "too much PASS"),))
        base.update(kw)
        return spec.Scenario(**base)

    def test_fail_criterion_trips_and_names_the_metric(self):
        v = self.make().evaluate({"idle_share": 0.4})
        self.assertFalse(v["passed"])
        self.assertEqual(v["trigger"], "idle_share")
        self.assertIn("idle_share", v["explanation"])
        self.assertIn("0.4", v["explanation"])

    def test_no_fail_criterion_tripped_passes(self):
        v = self.make().evaluate({"idle_share": 0.1})
        self.assertTrue(v["passed"])

    def test_exemption_short_circuits_before_fail_criteria(self):
        sc = self.make(exempt_when=(spec.Criterion("max_hands", "<=", 4, "tiny crew"),))
        v = sc.evaluate({"max_hands": 2, "idle_share": 0.9})
        self.assertTrue(v["passed"])
        self.assertEqual(v["reason"], "exempt")
        self.assertIn("max_hands", v["explanation"])

    def test_missing_metric_never_trips_a_criterion(self):
        v = self.make().evaluate({})
        self.assertTrue(v["passed"], "an absent metric must not be read as evidence of failure")


class MetricTests(unittest.TestCase):
    """The derived metrics the criteria threshold."""

    def test_acquisition_windows(self):
        # land 1 -> 2 on day 24 and 2 -> 3 on day 26 costs LAND_PRICES[0] + LAND_PRICES[1]
        land = [1] * 24 + [2, 2, 3, 3, 3, 3]
        self.assertEqual(metrics._land_spend(land, metrics.LATE_GAME_START), 1000 + 2000)
        self.assertEqual(metrics._land_spend(land, 0, metrics.LATE_GAME_START), 0)
        # herd of 4 from day 20; +2 on day 25, one escape on day 27, +1 on day 28
        animals = [0] * 20 + [4, 4, 4, 4, 4, 6, 6, 5, 6, 6]
        self.assertEqual(metrics._rises(animals, metrics.LATE_GAME_START), 3)
        self.assertEqual(metrics._rises(animals, 0), 7, "the day-20 build-up is not a late purchase")

    def test_scenario_metrics_shape(self):
        m = metrics.scenario_metrics(_synthetic_trace())
        self.assertEqual(m["peak_animals"], 6)
        self.assertEqual(m["animal_revenue"], 30 * (10 + 20))
        self.assertEqual(m["crop_revenue"], 30 * 100)
        self.assertAlmostEqual(m["chore_completion"], 0.5)
        self.assertEqual(m["land_at_midgame"], 2)
        self.assertEqual(m["early_cash_trough"], 500)

    def test_empty_trace_is_not_a_verdict(self):
        self.assertEqual(metrics.scenario_metrics({"cash": []}), {})

    def test_aggregate_means_across_seeds(self):
        agg = metrics.aggregate([{"escapes": 0, "idle_share": 0.1}, {"escapes": 4, "idle_share": 0.3}])
        self.assertEqual(agg["escapes"], 2.0)
        self.assertAlmostEqual(agg["idle_share"], 0.2)


class SeparationFromCascadeTests(unittest.TestCase):
    """The suite is a diagnostic, not a stage. Keep the two code paths disconnected."""

    def test_cascade_does_not_reference_the_scenario_suite(self):
        text = (ROOT / "evolve" / "cascade.py").read_text()
        self.assertNotIn("scenario", text.lower())

    def test_suite_does_not_import_cascade(self):
        for py in sorted((ROOT / "evolve" / "scenarios").glob("*.py")):
            with self.subTest(py.name):
                self.assertNotIn("import cascade", py.read_text())

    def test_only_dev_stage_candidates_are_selected(self):
        with tempfile.TemporaryDirectory() as td:
            conn = sqlite3.connect(Path(td) / "t.db")
            conn.row_factory = sqlite3.Row
            conn.executescript(
                "CREATE TABLE runs(run_id TEXT PRIMARY KEY, frontier TEXT);"
                "CREATE TABLE candidates(key TEXT, run_id TEXT, path TEXT, stage INTEGER,"
                " status TEXT, dev_margin REAL, island TEXT);"
                "INSERT INTO runs VALUES('r1','candidates/H32.py');"
                "INSERT INTO runs VALUES('r2','candidates/V3_12.py');"
                "INSERT INTO candidates VALUES('dev','r1','a.py',2,'alive',900,'c1');"
                "INSERT INTO candidates VALUES('held','r1','b.py',3,'held_pass',5000,'c1');"
                "INSERT INTO candidates VALUES('smoke','r1','c.py',1,'dead_smoke',NULL,'c1');"
                "INSERT INTO candidates VALUES('other','r2','d.py',3,'held_pass',9000,'c1');")
            conn.commit()
            db = type("Fake", (), {"conn": conn})()
            keys = [r["key"] for r in runner.dev_candidates(db)]
            self.assertEqual(sorted(keys), ["dev", "held", "other"])
            self.assertNotIn("smoke", keys)
            scoped = [r["key"] for r in runner.dev_candidates(db, frontier="candidates/H32.py")]
            self.assertEqual(scoped, ["held", "dev"], "one yardstick only, best dev_margin first")


class StorageTests(unittest.TestCase):
    """Verdicts are stored and queryable, in a table the evolution loop does not depend on."""

    def report(self, agent="x.py", passed=(True, False)):
        return {"key": "k1", "agent": agent, "suite_version": "test", "opponent": "opp.py",
                "n_pass": sum(passed), "n_fail": len(passed) - sum(passed), "n_inconclusive": 0,
                "failed": [], "seconds": 1.0,
                "results": [{"scenario": f"s{i}", "passed": p, "trigger": "idle_share",
                             "explanation": "because", "metrics": {"idle_share": 0.3},
                             "criteria": [], "per_seed": [], "seeds": [1], "seconds": 0.5,
                             "errors": 0}
                            for i, p in enumerate(passed)]}

    def test_round_trip_and_population_view(self):
        with tempfile.TemporaryDirectory() as td:
            conn = sqlite3.connect(Path(td) / "t.db")
            conn.row_factory = sqlite3.Row
            store.save_report(conn, self.report("a.py"))
            store.save_report(conn, self.report("b.py", (False, False)))
            rows = store.results_for(conn, agent="a.py")
            self.assertEqual(len(rows), 2)
            self.assertEqual({r["scenario"] for r in rows}, {"s0", "s1"})
            self.assertEqual(rows[0]["key"], "k1")
            self.assertEqual(json.loads(rows[0]["metrics"])["idle_share"], 0.3)
            self.assertEqual(store.pass_rates(conn, "test"),
                             {"s0": {"pass": 1, "fail": 1, "inconclusive": 0},
                              "s1": {"pass": 0, "fail": 2, "inconclusive": 0}})

    def test_rerun_replaces_rather_than_duplicates(self):
        with tempfile.TemporaryDirectory() as td:
            conn = sqlite3.connect(Path(td) / "t.db")
            conn.row_factory = sqlite3.Row
            store.save_report(conn, self.report("a.py", (True, True)))
            store.save_report(conn, self.report("a.py", (False, False)))
            rows = store.results_for(conn, agent="a.py")
            self.assertEqual(len(rows), 2)
            self.assertEqual([r["passed"] for r in rows], [0, 0])

    def test_schema_is_not_part_of_the_evolution_db_schema(self):
        self.assertNotIn("scenario_results", (ROOT / "evolve" / "db.py").read_text())


class ReportTests(unittest.TestCase):
    def test_markdown_has_the_three_views(self):
        rep = {"key": None, "agent": "candidates/C1.py", "suite_version": "v1", "opponent": "opp.py",
               "n_pass": 1, "n_fail": 1, "n_inconclusive": 0, "failed": ["idle_labor"], "seconds": 1.0,
               "results": [
                   {"scenario": "idle_labor", "passed": False, "trigger": "idle_share",
                    "explanation": "FAIL: idle_share >= 0.25 (actual 0.68)",
                    "metrics": {"idle_share": 0.68, "max_hands": 12}, "criteria": [], "per_seed": [],
                    "seeds": [1], "seconds": 0.5, "errors": 0},
                   {"scenario": "land_pressure", "passed": True, "trigger": None,
                    "explanation": "PASS", "metrics": {"land_at_midgame": 3}, "criteria": [],
                    "per_seed": [], "seeds": [1], "seconds": 0.5, "errors": 0}]}
        md = report_mod.render([rep])
        self.assertIn("## Per-candidate", md)
        self.assertIn("## Per-scenario", md)
        self.assertIn("## Fail analysis", md)
        self.assertIn("**FAIL**", md)
        self.assertIn("idle_share", md)
        self.assertIn("C1", md)

    def test_empty_report_renders(self):
        self.assertIn("No scenario results", report_mod.render([]))


class CacheKeyTests(unittest.TestCase):
    """trace.traced()'s cache key omits the engine config, so two scenarios with different worlds
    would collide on it. The suite keys its own cache on the config; pin that."""

    def test_config_is_part_of_the_cache_key(self):
        a = runner._cache_key(C1, C1, 1, "master", {"startingMoney": 3000}, "v1")
        b = runner._cache_key(C1, C1, 1, "master", {"startingMoney": 60000}, "v1")
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, runner._cache_key(C1, C1, 2, "master", {"startingMoney": 3000}, "v1"))
        self.assertNotEqual(a, runner._cache_key(C1, C1, 1, "master", {"startingMoney": 3000}, "v2"))


class EndToEndTests(unittest.TestCase):
    """Plays real games."""

    def test_all_five_scenarios_produce_a_verdict_and_an_explanation(self):
        rep = scenarios.run_suite(C1, seeds=FAST_SEEDS)
        self.assertEqual(len(rep["results"]), 5)
        self.assertEqual([r["scenario"] for r in rep["results"]], scenarios.names())
        for r in rep["results"]:
            with self.subTest(r["scenario"]):
                self.assertIn(r["passed"], (True, False), "no verdict was reached")
                self.assertTrue(r["explanation"])
                self.assertIn(r["trigger"] or "", r["explanation"] + "")
                self.assertTrue(r["metrics"], "a verdict must carry the metrics behind it")
                self.assertEqual(r["errors"], 0, "C1 must not raise inside a scenario world")
        self.assertEqual(rep["n_pass"] + rep["n_fail"] + rep["n_inconclusive"], 5)

    def test_subset_runs_on_its_own(self):
        rep = scenarios.run_suite(C1, only=["land_pressure"], seeds=FAST_SEEDS)
        self.assertEqual([r["scenario"] for r in rep["results"]], ["land_pressure"])


class DiscriminationTests(unittest.TestCase):
    """Each scenario's FAIL path fires on an agent carrying exactly its pathology, and does not
    fire on the same agent without it. Controls are lab fixtures, never candidates."""

    CASES = [
        # scenario,               control that must FAIL,   control that must PASS
        ("unsupported_livestock", "hold_animal_products",   "no_livestock"),
        ("idle_labor",            "overhire",               None),
        ("late_expansion",        "defer_expansion",        None),
        ("land_pressure",         "hoard",                  None),
        ("execution_overload",    "neglect_feeding",        "starve_labor"),
    ]

    @classmethod
    def setUpClass(cls):
        cls._td = tempfile.TemporaryDirectory()
        cls.out = Path(cls._td.name)

    @classmethod
    def tearDownClass(cls):
        cls._td.cleanup()

    def verdict(self, agent, name):
        return scenarios.run_suite(agent, only=[name], seeds=FAST_SEEDS)["results"][0]

    def test_pathological_control_fails_the_scenario_it_targets(self):
        for name, bad, _good in self.CASES:
            with self.subTest(scenario=name, control=bad):
                r = self.verdict(controls.write_control(C1, bad, self.out), name)
                self.assertIs(r["passed"], False,
                              f"{name} did not catch the {bad} control: {r['explanation']}")
                self.assertIn(r["trigger"], [c.metric for c in scenarios.get(name).fail_when])

    def test_healthy_control_passes_the_same_scenario(self):
        for name, _bad, good in self.CASES:
            if good is None:
                continue
            with self.subTest(scenario=name, control=good):
                r = self.verdict(controls.write_control(C1, good, self.out), name)
                self.assertIs(r["passed"], True,
                              f"{name} failed the healthy {good} control: {r['explanation']}")

    def test_known_candidates_are_not_all_scored_alike(self):
        """The suite has to separate real candidates, not just synthetic controls: C1 and H10
        differ on unsupported_livestock, and C1 and H32 on land_pressure."""
        pairs = [("unsupported_livestock", "C1.py", "H10.py"), ("land_pressure", "C1.py", "H32.py")]
        for name, a, b in pairs:
            with self.subTest(scenario=name):
                va = self.verdict(ROOT / "candidates" / a, name)["passed"]
                vb = self.verdict(ROOT / "candidates" / b, name)["passed"]
                self.assertNotEqual(va, vb, f"{name} scores {a} and {b} identically")


def _synthetic_trace(days=30):
    """A hand-built trace with known answers, so the metric arithmetic is checked without a game."""
    return {
        "cash": [1000.0] * 3 + [500.0] * 10 + [2000.0] * (days - 13),
        "networth": [1000] * days,
        "animals": [0] * 5 + [6] * (days - 5),
        "plants": [10] * days,
        "land": [1, 1, 2] + [2] * (days - 3),
        "hands": [4] * days,
        "unit_turns": [100] * days,
        "idle_turns": [20] * days,
        "work_turns": [40] * days,
        "move_turns": [40] * days,
        "sales_rev": [130] * days,
        "buys_cost": [10] * days,
        "chores_enumerated": [10] * days,
        "chores_completed": [5] * days,
        "escapes": [0] * days,
        "missed_feed": [0] * days,
        "missed_water": [1] * days,
        "weeds_new": [0] * days,
        "shed_units": [3] * days,
        "sales_by_product": [{"MILK": 10, "WOOL": 20, "WHEAT": 100}] * days,
    }


if __name__ == "__main__":
    unittest.main()
