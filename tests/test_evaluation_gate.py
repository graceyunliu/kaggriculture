"""Contracts for the replicated development gate added after the Sep 11 plateau diagnosis."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evolve"))

import cascade  # noqa: E402


def result(seed_margins):
    per_seed = {seed: {"a": margin, "b": 0.0, "errors": [0, 0]}
                for seed, margin in seed_margins.items()}
    margins = list(seed_margins.values())
    mean = sum(margins) / len(margins)
    return {"mean_margin_per_game": mean / 2, "t": 99.0,
            "wins": sum(x > 0 for x in margins), "losses": sum(x < 0 for x in margins),
            "agent_errors": [0, 0], "per_seed": per_seed}


class ReplicatedDevelopmentGateTests(unittest.TestCase):
    def test_rejects_one_negative_block_even_when_pooled_mean_is_large(self):
        blocks = [result({1: 20000, 2: 20000}), result({31: -1000, 32: -1000}),
                  result({41: 20000, 42: 20000})]
        passed, pooled = cascade.dev_blocks_pass(blocks, margin_floor=1500, t_floor=0)
        self.assertGreater(pooled["mean_margin_per_game"], 1500)
        self.assertFalse(passed)

    def test_accepts_consistent_disjoint_blocks(self):
        blocks = [result({1: 4000, 2: 6000}), result({31: 5000, 32: 7000}),
                  result({41: 4500, 42: 6500})]
        passed, pooled = cascade.dev_blocks_pass(blocks, margin_floor=1500, t_floor=2)
        self.assertTrue(passed)
        self.assertEqual(len(pooled["per_seed"]), 6)

    def test_overlapping_blocks_are_an_error(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            cascade.combine_results([result({1: 100}), result({1: 200})])

    def test_preregistered_seed_partitions_are_disjoint(self):
        groups = [cascade.DEV_SEEDS, *cascade.DEV_CONFIRM_BLOCKS,
                  cascade.HELD_SEEDS, cascade.POPULATION_SEEDS]
        flattened = [seed for group in groups for seed in group]
        self.assertEqual(len(flattened), len(set(flattened)))

    def test_first_block_t_is_not_a_standalone_gate(self):
        """A noisy first block may fail t>=2 while the preregistered pool passes."""
        first = result({1: 3000, 2: 5000})
        first["t"] = 1.9
        blocks = [first, result({31: 5000, 32: 7000}),
                  result({41: 4500, 42: 6500})]
        passed, pooled = cascade.dev_blocks_pass(blocks, margin_floor=1500, t_floor=2)
        self.assertLess(first["t"], 2)
        self.assertGreaterEqual(pooled["t"], 2)
        self.assertTrue(passed)


if __name__ == "__main__":
    unittest.main()
