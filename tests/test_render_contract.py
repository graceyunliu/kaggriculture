"""render() must never silently drop a proposed parameter (AGE-336).

A candidate is only a genuine change relative to its parent if the values the proposer
asked for actually land in the rendered file. render() has two ways to no-op silently:

  * a KNOB_SPACE name the proposer asked for that the frozen chassis's KNOBS does not carry
  * a CONST_SPACE name whose `NAME = value` regex substitution finds nothing (n == 0)

Either one produces a byte-for-byte clone of the parent that still compiles and still plays
a game, so propose.validate() reports ok=True on a candidate that changed nothing. These
tests pin render() to raising instead.
"""
from __future__ import annotations

import re
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

import space  # noqa: E402


@contextmanager
def _out_dir():
    with tempfile.TemporaryDirectory() as td:
        yield Path(td)


@contextmanager
def _chassis_text(text):
    """Point space at a throwaway chassis snapshot, so _read_base() reads our text
    through the real code path instead of us mocking _read_base out."""
    with tempfile.TemporaryDirectory() as td:
        snap = Path(td) / "K_test.py"
        snap.write_text(text)
        with mock.patch.object(space, "K_SRC", snap):
            yield


class RenderKnobContractTests(unittest.TestCase):
    """render() must surface a knob it cannot realize against the live frozen chassis."""

    @contextmanager
    def absent_knob(self):
        """Name of a KNOB_SPACE knob the live frozen chassis does not carry.

        The chassis is genuinely out of sync today -- the spec_* knobs are advertised in
        KNOB_SPACE (and so in SPACE, and so accepted by propose.validate()) but are absent
        from chassis.py's KNOBS -- so we use a real one and reproduce the exact production
        failure against the real frozen source of truth. If the chassis is ever rebuilt so
        every knob is live, we synthesise the same drift by adding a name to KNOB_SPACE;
        that is the condition render() has to detect either way.
        """
        _, knobs, _ = space._read_base()
        drifted = [n for n in space.KNOB_SPACE if n not in knobs]
        if drifted:
            yield drifted[0]
            return
        name = "age336_unrealizable_knob"
        spec = ("int", 0, 9, 1)
        with mock.patch.dict(space.KNOB_SPACE, {name: spec}), \
             mock.patch.dict(space.SPACE, {name: spec}):
            yield name

    def test_knob_absent_from_frozen_chassis_is_surfaced(self):
        with self.absent_knob() as knob, _out_dir() as out:
            params = space.base_params()
            self.assertNotIn(knob, params, "knob must be absent from the chassis for this test")
            params[knob] = "age336-proposed-value"
            with self.assertRaises(ValueError) as ctx:
                space.render(params, out_dir=out)
            msg = str(ctx.exception)
            self.assertIn(knob, msg)
            self.assertIn("age336-proposed-value", msg)
            self.assertIn("melon_floor", msg, "error should name the live KNOBS so drift is diagnosable")
            self.assertFalse(list(out.iterdir()), "no candidate file may be written for an unrealizable param")

    def test_silent_drop_would_have_produced_a_noop_clone(self):
        """The thing the raise replaces: without it the rendered file is byte-identical to
        the parent's, i.e. the candidate is a no-op cousin wearing a fresh key."""
        with self.absent_knob() as knob, _out_dir() as out:
            base = space.base_params()
            parent = space.render(base, out_dir=out)
            proposed = dict(base, **{knob: "age336-proposed-value"})
            with self.assertRaises(ValueError):
                space.render(proposed, out_dir=out)
            self.assertEqual([p.name for p in out.iterdir()], [parent.name])


class RenderConstContractTests(unittest.TestCase):
    """render() must surface a CONST_SPACE substitution that matched nothing (n == 0).

    Every CONST_SPACE name is currently a plain column-0 assignment in the chassis, so the
    regex cannot miss as the chassis stands. We reproduce the two ways it drifts into
    missing by rendering against a mutated chassis snapshot -- the constant deleted, and
    the constant indented out of the `^NAME =` the regex anchors on.
    """

    CONST = "MAX_HANDS"

    def mutated_chassis(self, how):
        text = space.K_SRC.read_text()
        pattern = rf"^{self.CONST}\s*=\s*[^#\n]+"
        self.assertRegex(text, re.compile(pattern, re.M), "precondition: constant is currently renderable")
        if how == "deleted":
            return re.sub(pattern + r"\n", "", text, count=1, flags=re.M)
        return re.sub(pattern, lambda m: "if True:\n    " + m.group(0), text, count=1, flags=re.M)

    def test_const_substitution_noop_is_surfaced(self):
        for how in ("deleted", "indented"):
            with self.subTest(how=how), _chassis_text(self.mutated_chassis(how)), _out_dir() as out:
                params = space.base_params()
                params[self.CONST] = 11
                with self.assertRaises(ValueError) as ctx:
                    space.render(params, out_dir=out)
                msg = str(ctx.exception)
                self.assertIn(self.CONST, msg)
                self.assertIn("11", msg)
                self.assertFalse(list(out.iterdir()), "no candidate file may be written for an unrealizable param")


class RenderPositiveControlTests(unittest.TestCase):
    """A proposal render() *can* realize still lands in the file, unchanged by the fix."""

    def rendered_knobs(self, path):
        m = re.search(r"^KNOBS = (\{.*?\})\n", path.read_text(), re.S | re.M)
        self.assertIsNotNone(m, "rendered file must carry a KNOBS block")
        return eval(m.group(1))  # noqa: S307 - a file we just wrote

    def test_valid_knob_and_const_are_realized(self):
        _, knobs, consts = space._read_base()
        with _out_dir() as out:
            params = space.base_params()
            params["harvest_min"] = 3 if knobs["harvest_min"] != 3 else 2
            params["MAX_HANDS"] = consts["MAX_HANDS"] + 1
            path = space.render(params, out_dir=out)
            self.assertEqual(self.rendered_knobs(path)["harvest_min"], params["harvest_min"])
            self.assertRegex(path.read_text(), rf"(?m)^MAX_HANDS = {params['MAX_HANDS']}$")
            compile(path.read_text(), str(path), "exec")


class ValidateNoOpHoleTests(unittest.TestCase):
    """propose.validate() must not report ok=True for a candidate whose proposed change
    render() cannot realize. It filters proposals by `k in space.SPACE`, which lets a
    drifted knob through to render(); the raise is what stops it reaching a test game."""

    def test_validate_rejects_a_candidate_render_cannot_realize(self):
        import propose

        _, knobs, _ = space._read_base()
        drifted = [n for n in space.KNOB_SPACE if n not in knobs]
        if not drifted:
            self.skipTest("chassis carries every KNOB_SPACE knob; no drifted knob to propose")
        knob = drifted[0]
        cand = {"base": "c1", "params": {knob: space.KNOB_SPACE[knob][1][-1]}}
        with mock.patch.object(propose.space, "render", side_effect=space.render) as rendered:
            ok, why = propose.validate(cand, "")
        self.assertTrue(rendered.called, "validate must have attempted a render")
        self.assertFalse(ok, f"validate reported ok on an unrealizable candidate: {why}")
        self.assertIn(knob, why)


if __name__ == "__main__":
    unittest.main()
