"""
test_ladder_watcher.py -- tests for ladder_watcher.py

Uses MockLadderDataSource -- no live Kaggle access needed/attempted. Covers:
  - simple sequential checkpoint crossing (7 -> 13 -> 21 -> 21 idempotent)
  - a single big jump crossing two checkpoints at once (7 -> 25)
  - restart persistence (state survives a fresh load_state(), no refire)
  - transient API failure + retry-worthy error surfaced, not crashing
  - malformed/incomplete poll response handled without crashing
  - O42 hash verification is read-only and detects a mismatch
Run: python3 -m pytest test_ladder_watcher.py -q
     or: python3 test_ladder_watcher.py
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ladder_watcher as lw
import experiment_ledger as el


def _poll(games, wins, losses, draws, rating, extra_games=None):
    games_list = extra_games if extra_games is not None else [
        {"episode_id": f"ep{i}", "opponent_submission_id": f"opp{i}",
         "opponent_name": "unavailable", "my_reward": 1, "opponent_reward": 0,
         "money_margin": "unavailable", "result": "win", "rating_after": rating,
         "replay_available": "unavailable", "is_real_opponent": True}
        for i in range(games)
    ]
    return {
        "submission_id": "999999",
        "games_completed": games,
        "wins": wins, "losses": losses, "draws": draws,
        "rating": rating,
        "games": games_list,
        "raw": {"note": "mock"},
    }


CANDIDATES = [{"candidate_id": "adaptive-v0.3", "submission_id": "999999",
               "filename": "adaptive-v0.3-ladder-submission.zip",
               "parent_candidate": "adaptive-v0.2-ladder-candidate"}]


class LadderWatcherTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="ladder_watcher_test_")
        self.state_path = os.path.join(self.tmpdir, "state", "ladder_watcher_state.json")
        lw.RAW_EVIDENCE_DIR = os.path.join(self.tmpdir, "state", "raw_ladder_evidence")
        lw.DIAGNOSTICS_DIR = os.path.join(self.tmpdir, "state", "checkpoint_diagnostics")
        # Redirect the ledger to a scratch file so tests never touch the
        # real experiment_ledger.jsonl.
        self._orig_ledger_path = el.LEDGER_PATH
        el.LEDGER_PATH = os.path.join(self.tmpdir, "experiment_ledger.jsonl")

    def tearDown(self):
        el.LEDGER_PATH = self._orig_ledger_path
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    # ---- sequential checkpoint crossing + idempotency -------------------
    def test_sequential_checkpoints_and_idempotent_replay(self):
        script = {"999999": [_poll(7, 3, 4, 0, 850), _poll(13, 6, 7, 0, 860),
                              _poll(21, 10, 11, 0, 870), _poll(21, 10, 11, 0, 870)]}
        source = lw.MockLadderDataSource(CANDIDATES, script)

        r1 = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual(r1["checkpoints_fired"], [])  # 7 games: nothing yet

        r2 = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual([c["checkpoint"] for c in r2["checkpoints_fired"]], [10])

        r3 = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual([c["checkpoint"] for c in r3["checkpoints_fired"]], [20])

        r4 = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual(r4["checkpoints_fired"], [])  # same count again: idempotent, no refire

        state = lw.load_state(self.state_path)
        self.assertEqual(state["candidates"]["adaptive-v0.3"]["completed_checkpoints"], [10, 20])
        self.assertEqual(state["candidates"]["adaptive-v0.3"]["last_seen_game_count"], 21)

    # ---- big jump fires both checkpoints exactly once --------------------
    def test_big_jump_fires_both_checkpoints_once(self):
        script = {"999999": [_poll(7, 3, 4, 0, 850), _poll(25, 12, 13, 0, 880)]}
        source = lw.MockLadderDataSource(CANDIDATES, script)

        lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        r2 = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        fired = sorted(c["checkpoint"] for c in r2["checkpoints_fired"])
        self.assertEqual(fired, [10, 20])

        # exactly one ledger row (append) then one result_update per checkpoint;
        # confirm no duplicate checkpoint diagnostics were written.
        diag_files = os.listdir(lw.DIAGNOSTICS_DIR)
        self.assertEqual(len(diag_files), 2)

    # ---- restart persistence: no refire after reload ----------------------
    def test_restart_persistence_no_refire(self):
        script = {"999999": [_poll(13, 6, 7, 0, 860)]}
        source = lw.MockLadderDataSource(CANDIDATES, script)
        lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)

        # Simulate a fresh process: reload state from disk, poll again with
        # the SAME game count (submission hasn't produced new games yet).
        script2 = {"999999": [_poll(13, 6, 7, 0, 860)]}
        source2 = lw.MockLadderDataSource(CANDIDATES, script2)
        reloaded_state = lw.load_state(self.state_path)
        self.assertEqual(reloaded_state["candidates"]["adaptive-v0.3"]["completed_checkpoints"], [10])

        r2 = lw.poll_once(source2, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual(r2["checkpoints_fired"], [])  # must NOT refire checkpoint 10

    # ---- transient API failure: surfaced, not crashing --------------------
    def test_transient_failure_does_not_crash(self):
        script = {"999999": [_poll(7, 3, 4, 0, 850)]}
        fail_script = {"999999": [lw.LadderTransientError("simulated 503")]}
        source = lw.MockLadderDataSource(CANDIDATES, script, fail_script=fail_script)

        report = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertTrue(any(not e.get("fatal") for e in report["errors"]))
        self.assertEqual(report["polled"], [])  # no state advanced on failure

        # Should not have crashed, and a subsequent real poll should work fine.
        report2 = lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual(len(report2["polled"]), 1)

    def test_auth_failure_surfaced_clearly(self):
        candidates = CANDIDATES

        class AuthFailSource(lw.LadderDataSource):
            def discover_candidates(self):
                raise lw.LadderAuthError("token rejected")

            def poll_submission(self, submission_id):
                raise AssertionError("should not be reached")

        report = lw.poll_once(AuthFailSource(), checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertTrue(any(e.get("fatal") for e in report["errors"]))

    # ---- malformed/incomplete responses handled gracefully -----------------
    def test_malformed_response_does_not_crash(self):
        class MalformedSource(lw.LadderDataSource):
            def discover_candidates(self):
                return CANDIDATES

            def poll_submission(self, submission_id):
                return {"unexpected": "shape"}  # missing games_completed entirely

        report = lw.poll_once(MalformedSource(), checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual(report["polled"], [])
        self.assertTrue(len(report["errors"]) == 1)

        class NoneSource(lw.LadderDataSource):
            def discover_candidates(self):
                return CANDIDATES

            def poll_submission(self, submission_id):
                return None

        report2 = lw.poll_once(NoneSource(), checkpoints=(10, 20, 30), state_path=self.state_path)
        self.assertEqual(report2["polled"], [])

    # ---- checkpoint math is exact, order-independent of input order --------
    def test_newly_crossed_checkpoints_helper(self):
        self.assertEqual(lw.newly_crossed_checkpoints(7, 7, [], (10, 20, 30)), [])
        self.assertEqual(lw.newly_crossed_checkpoints(7, 13, [], (10, 20, 30)), [10])
        self.assertEqual(lw.newly_crossed_checkpoints(13, 21, [10], (10, 20, 30)), [20])
        self.assertEqual(lw.newly_crossed_checkpoints(7, 25, [], (10, 20, 30)), [10, 20])
        self.assertEqual(lw.newly_crossed_checkpoints(21, 21, [10, 20], (10, 20, 30)), [])

    # ---- O42 immutability check is read-only and detects tampering --------
    def test_o42_hash_check_detects_mismatch(self):
        good = lw.verify_o42_immutable()
        self.assertTrue(good.get("checked"))
        self.assertTrue(good.get("matches"), f"O42 hash mismatch detected: {good}")

        tmp_o42 = os.path.join(self.tmpdir, "fake_o42.py")
        with open(tmp_o42, "w") as f:
            f.write("# tampered\n")
        orig_path = lw.O42_PATH
        try:
            lw.O42_PATH = tmp_o42
            bad = lw.verify_o42_immutable()
            self.assertFalse(bad["matches"])
        finally:
            lw.O42_PATH = orig_path

    # ---- research-loop integration writes ledger + diagnostic -------------
    def test_checkpoint_triggers_ledger_and_diagnostic(self):
        script = {"999999": [_poll(13, 6, 7, 0, 860)]}
        source = lw.MockLadderDataSource(CANDIDATES, script)
        lw.poll_once(source, checkpoints=(10, 20, 30), state_path=self.state_path)

        rows = el.read_all()
        self.assertEqual(len(rows), 1)
        self.assertIn("CHECKPOINT: 10_GAMES", rows[0]["ladder_result"])
        self.assertIn("PARTIAL", rows[0]["observations"])

        diag_files = os.listdir(lw.DIAGNOSTICS_DIR)
        self.assertEqual(len(diag_files), 1)
        with open(os.path.join(lw.DIAGNOSTICS_DIR, diag_files[0])) as f:
            diag = json.load(f)
        self.assertEqual(diag["label"], "CHECKPOINT: 10_GAMES")
        self.assertFalse(diag["is_final_result"])
        self.assertEqual(diag["new_games_since_previous_checkpoint"], 10)


if __name__ == "__main__":
    unittest.main()
