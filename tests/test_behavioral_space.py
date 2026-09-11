"""The active evolution space must be realizable in the exact-O26 chassis."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evolve"))

import space  # noqa: E402


class BehavioralSpaceTests(unittest.TestCase):
    def test_active_behavioral_space_is_renderable(self):
        live = space.validate_behavioral_space()
        self.assertTrue(live)
        params = space.base_params()
        self.assertLessEqual(set(live), set(params))

    def test_dead_melon_tile_constant_is_not_actively_searched(self):
        self.assertNotIn("MELON_MAX_TILES", space.BEHAVIORAL_PARAMS)

    def test_rejected_factorial_branch_is_not_actively_searched(self):
        self.assertNotIn("fert_carry", space.BEHAVIORAL_PARAMS)


if __name__ == "__main__":
    unittest.main()
