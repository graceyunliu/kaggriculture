"""Complexity gate (AGE-335).

`propose.complexity_check` is a checklist, not a filter: it reads a proposal's own JSON, says which
of the five questions in RULES.md have no answer, and returns. Three things have to hold for it to
be worth having:

  * it never blocks and never costs anything -- no game, no render, no database, no LLM;
  * its lookup tables agree with the things they claim to mirror (evolve/blocks.py's block list,
    classify.py's failure classes, the scenario registry, and which knob the chassis reads where),
    because a table that has silently drifted gives confident wrong answers;
  * each flag fires on the case it names and stays quiet on the case it does not.
"""
from __future__ import annotations

import json
import re
import sys
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

import blocks as blocks_mod  # noqa: E402
import classify  # noqa: E402
import propose  # noqa: E402
import scenarios  # noqa: E402
import space  # noqa: E402


def flags(items):
    return [i["flag"] for i in items if i["severity"] == "flag"]


def infos(items):
    return [i["flag"] for i in items if i["severity"] == "info"]


GOOD = {
    "note": "batch non-urgent watering into one late sweep, so hands stop crossing the board per tile",
    "capability": "the agent can defer a tile's water to a later fuller sweep",
    "failure_class": "EXECUTION_FAILURE",
    "scenario": "execution_overload",
    "blocks": {"sweep": "def _build_sweep():\n    pass\n"},
}


class TableIntegrityTests(unittest.TestCase):
    """Every table in the gate mirrors something else in the repo. Fail loudly when they diverge."""

    def test_failure_class_table_covers_every_block_with_real_classes(self):
        self.assertEqual(set(propose.BLOCK_FAILURE_CLASSES), set(blocks_mod.BLOCKS))
        for block, classes in propose.BLOCK_FAILURE_CLASSES.items():
            with self.subTest(block):
                self.assertTrue(classes, "a block with no failure class can never answer Q2")
                for c in classes:
                    self.assertIn(c, classify.CLASSES)

    def test_scenario_table_covers_every_block_with_real_scenarios(self):
        self.assertEqual(set(propose.BLOCK_SCENARIOS), set(blocks_mod.BLOCKS))
        known = set(scenarios.names())
        for block, names in propose.BLOCK_SCENARIOS.items():
            with self.subTest(block):
                self.assertTrue(names)
                self.assertTrue(set(names) <= known, f"{set(names) - known} are not scenarios")

    def test_scenario_names_mirror_the_registry(self):
        # propose.py deliberately does not import the scenario package (it pulls in the tracer and
        # the engine); this test is what keeps the copy honest.
        self.assertEqual(list(propose.SCENARIO_NAMES), scenarios.names())
        self.assertTrue(set(propose.DISCRIMINATING_SCENARIOS) <= set(propose.SCENARIO_NAMES))

    def test_param_block_table_matches_the_frozen_chassis(self):
        """PARAM_BLOCK says which block reads which knob. Re-derive it and compare: if the chassis is
        rebuilt and a knob moves between blocks, the gate's Q2 answer for that knob moves with it."""
        blk = blocks_mod.extract(blocks_mod.CHASSIS.read_text())
        derived = {}
        for name in space.SPACE:
            hits = [b for b, src in blk.items() if re.search(r"\b" + re.escape(name) + r"\b", src)]
            if len(hits) == 1:
                derived[name] = hits[0]
            elif len(hits) > 1:
                # a knob read by more than one block: the table has to say which one owns it
                self.assertIn(name, propose.PARAM_BLOCK, f"{name} is read by {hits}")
                self.assertIn(propose.PARAM_BLOCK[name], hits)
        for name, block in derived.items():
            with self.subTest(name):
                self.assertEqual(propose.PARAM_BLOCK.get(name), block)
        for name in propose.PARAM_BLOCK:
            self.assertIn(name, space.SPACE)


class CostAndSafetyTests(unittest.TestCase):
    """The gate is a lookup. It must not run a game, render a file, or raise."""

    def test_never_renders_and_never_plays(self):
        real_render = space.render

        def explode(*a, **k):
            raise AssertionError("complexity_check must not render an agent")

        space.render = explode
        try:
            propose.complexity_check(GOOD)
            propose.complexity_check({"params": {"open_wheat": 9}})
        finally:
            space.render = real_render

    def test_junk_input_is_flagged_not_raised(self):
        for junk in (None, [], "candidate", 7, {"blocks": "not a dict"}):
            with self.subTest(repr(junk)):
                try:
                    items = propose.complexity_check(junk)
                except Exception as e:  # noqa: BLE001
                    self.fail(f"complexity_check raised on {junk!r}: {e!r}")
                self.assertIsInstance(items, list)

    def test_is_cheap_enough_to_run_on_every_proposal(self):
        propose.complexity_check(GOOD)          # warm the two cached chassis scans
        t0 = time.time()
        for _ in range(200):
            propose.complexity_check(GOOD)
        self.assertLess(time.time() - t0, 2.0, "the gate must not slow the proposal round")


class QuestionTests(unittest.TestCase):

    def test_a_fully_answered_proposal_is_clean(self):
        items = propose.complexity_check(GOOD)
        self.assertEqual(flags(items), [])
        self.assertEqual(propose.gate_summary(items), "gate: clean")
        self.assertIn("capability_recorded", infos(items))
        self.assertIn("mechanism_recorded", infos(items))

    def test_q1_missing_capability_and_note(self):
        items = propose.complexity_check({"blocks": {"sweep": "x"}})
        self.assertIn("no_capability_statement", flags(items))

    def test_q1_falls_back_to_the_note(self):
        cand = dict(GOOD)
        cand.pop("capability")
        self.assertIn("capability_from_note", infos(propose.complexity_check(cand)))

    def test_q2_missing_failure_class_names_the_plausible_ones(self):
        cand = dict(GOOD)
        cand.pop("failure_class")
        items = propose.complexity_check(cand)
        self.assertIn("no_failure_evidence", flags(items))
        detail = next(i["detail"] for i in items if i["flag"] == "no_failure_evidence")
        self.assertIn("EXECUTION_FAILURE", detail)

    def test_q2_unknown_and_mismatched_failure_classes(self):
        self.assertIn("unknown_failure_class",
                      flags(propose.complexity_check({**GOOD, "failure_class": "VIBES_FAILURE"})))
        self.assertIn("failure_class_mismatch",
                      flags(propose.complexity_check({**GOOD, "failure_class": "LAND_FAILURE"})))

    def test_q2_a_param_no_block_reads_has_no_failure_evidence(self):
        # harvest_min is read outside every typed block, so no classify.py rule attaches to it
        self.assertNotIn("harvest_min", propose.PARAM_BLOCK)
        items = propose.complexity_check({"note": "raise the harvest threshold because ...",
                                          "params": {"harvest_min": 3}})
        self.assertIn("no_failure_evidence", flags(items))
        self.assertIn("harvest_min", [i["target"] for i in items if i["flag"] == "no_failure_evidence"])

    def test_q3_missing_scenario_suggests_the_reachable_ones(self):
        cand = dict(GOOD)
        cand.pop("scenario")
        items = propose.complexity_check(cand)
        self.assertIn("no_independent_test", flags(items))
        self.assertIn("execution_overload",
                      next(i["detail"] for i in items if i["flag"] == "no_independent_test"))

    def test_q3_unknown_mismatched_and_non_discriminating_scenarios(self):
        self.assertIn("unknown_scenario",
                      flags(propose.complexity_check({**GOOD, "scenario": "crop_apocalypse"})))
        self.assertIn("scenario_mismatch",
                      flags(propose.complexity_check({**GOOD, "scenario": "late_expansion"})))
        # idle_labor IS reachable from dispatch, but it passes 30/30 of the real population
        items = propose.complexity_check({**GOOD, "scenario": "idle_labor",
                                          "blocks": {"dispatch": "def _unit_action():\n    pass\n"}})
        self.assertIn("test_does_not_discriminate", flags(items))

    def test_q4_an_outcome_is_not_a_mechanism(self):
        self.assertIn("mechanism_not_explained",
                      flags(propose.complexity_check({**GOOD, "note": "scores better"})))
        self.assertNotIn("mechanism_not_explained", flags(propose.complexity_check(GOOD)))

    def test_q5_reports_whether_the_loop_will_ablate(self):
        one = propose.complexity_check(GOOD)
        self.assertIn("ablation_is_the_dev_margin", infos(one))
        two = propose.complexity_check({**GOOD, "params": {"open_wheat": 9}})
        self.assertIn("ablation_planned", infos(two))
        base = space.c1_params()
        moved = {k: space.clamp(k, v + 1) for k, v in list(base.items())[:12]
                 if isinstance(v, int) and not isinstance(v, bool)}
        moved = {k: v for k, v in moved.items() if v != base[k]}
        self.assertGreater(len(moved), 8, "need >8 real changes to exercise the skip")
        self.assertIn("ablation_will_be_skipped",
                      flags(propose.complexity_check({**GOOD, "params": moved})))


class StructuralTests(unittest.TestCase):

    def test_unknown_block_and_unknown_param(self):
        items = propose.complexity_check({**GOOD, "blocks": {"telepathy": "x"},
                                          "params": {"nonsense": 1}})
        self.assertIn("unknown_block", flags(items))
        self.assertIn("unknown_param", flags(items))

    def test_inert_param_is_caught_before_render_raises(self):
        """A SPACE name the frozen chassis does not carry: space.render() raises on it (AGE-336), so
        the proposal is dead on arrival and the gate should say so without spending the game."""
        inert = sorted(set(space.SPACE) - set(space.c1_params()))
        self.assertTrue(inert, "no inert params -- update this test if the chassis was rebuilt")
        items = propose.complexity_check({"note": "try it because ...", "params": {inert[0]: 1}})
        self.assertIn("inert_param", flags(items))

    def test_unread_param_is_a_silent_no_op(self):
        """Declared in KNOBS, read by nothing: render() accepts it, the candidate gets its own key,
        and it behaves exactly like its parent."""
        unread = sorted(propose._unread_param_names() & set(space.c1_params()))
        self.assertTrue(unread, "no live-but-unread params -- update this test if KNOBS changed")
        items = propose.complexity_check({"note": "vary it because ...", "params": {unread[0]: 0.4}})
        self.assertIn("unread_param", flags(items))

    def test_a_param_set_to_the_value_it_already_has_is_a_no_op(self):
        base = space.c1_params()
        k = "open_wheat"
        items = propose.complexity_check({"note": "same value because ...", "params": {k: base[k]}})
        self.assertIn("no_op_param", flags(items))
        self.assertIn("no_change", flags(items))

    def test_a_factorial_grid_is_checked_through_its_axes(self):
        items = propose.complexity_check({"kind": "factorial", "note": "grid",
                                          "axes": {"open_wheat": [7, 9]},
                                          "block_options": {"sweep": [None, "src"]}})
        self.assertNotIn("no_change", flags(items))
        self.assertIn("ablation_planned", infos(items))


class QueueTests(unittest.TestCase):
    """The gate has to survive the files that are actually in the queue today."""

    def test_every_queue_item_gets_a_verdict(self):
        for path in sorted((ROOT / "evolve" / "queue").glob("*.json")):
            with self.subTest(path.name):
                items = propose.complexity_check(json.loads(path.read_text()))
                self.assertIsInstance(items, list)
                self.assertTrue(any(i["question"] == 4 for i in items))


if __name__ == "__main__":
    unittest.main()
