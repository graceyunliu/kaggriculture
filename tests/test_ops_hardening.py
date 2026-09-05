from __future__ import annotations

import sqlite3
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class OpsHardeningTests(unittest.TestCase):
 def test_frontier_alert_is_idempotent(self):
    with tempfile.TemporaryDirectory() as td:
     tmp_path = Path(td)
     db = tmp_path / "test.db"
     conn = sqlite3.connect(db)
     conn.executescript(
        """
        CREATE TABLE runs(run_id TEXT PRIMARY KEY, frontier TEXT);
        CREATE TABLE candidates(
          key TEXT, run_id TEXT, path TEXT, stage INTEGER, status TEXT,
          held_margin REAL, held_t REAL
        );
        INSERT INTO runs VALUES ('r1', 'candidates/H32.py');
        INSERT INTO candidates VALUES
          ('fake', 'r1', 'evolve/gen/cand_fake.py', 3, 'held_pass', 12345, 3.25);
        """
    )
     conn.commit()
     conn.close()
     flag = tmp_path / "pending.txt"
     notify = tmp_path / "notify.sh"
     calls = tmp_path / "calls.txt"
     alert_state = tmp_path / "alerted.txt"
     notify.write_text(f"#!/bin/sh\necho \"$*\" >> {calls}\n")

     cmd = [
        "python3", "evolve/check_frontier.py", "--db", str(db),
        "--frontier", "candidates/H32.py", "--flag", str(flag),
        "--alert-state", str(alert_state),
        "--notify-script", str(notify),
    ]
     first = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)
     second = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)
     self.assertIn("beats current frontier", first.stdout)
     self.assertIn("already sent", second.stdout)
     self.assertEqual(len(calls.read_text().splitlines()), 1)
     self.assertIn("$12,345/game (t=3.25)", flag.read_text())
     conn = sqlite3.connect(db)
     conn.execute("DELETE FROM candidates")
     conn.commit()
     conn.close()
     flag.unlink()
     normal = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)
     self.assertIn("no decisive held-out winner", normal.stdout)
     self.assertFalse(flag.exists())


 def test_propose_health_alerts_once_and_resets(self):
    with tempfile.TemporaryDirectory() as td:
     tmp_path = Path(td)
     state = tmp_path / "count"
     notify = tmp_path / "notify.sh"
     calls = tmp_path / "calls.txt"
     notify.write_text(f"#!/bin/sh\necho \"$*\" >> {calls}\n")
     env = {
        "PROPOSE_FAILURE_STATE": str(state),
        "PROPOSE_NOTIFY_SCRIPT": str(notify),
        "PROPOSE_FAILURE_THRESHOLD": "3",
    }
     import os
     run_env = os.environ | env
     for _ in range(4):
        subprocess.run(
            ["bash", "evolve/propose_health.sh", "failure", "synthetic claude exit 1"],
            cwd=ROOT, env=run_env, check=True, capture_output=True,
        )
     self.assertEqual(len(calls.read_text().splitlines()), 1)
     self.assertEqual(state.read_text(), "4 1\n")
     subprocess.run(["bash", "evolve/propose_health.sh", "success"], cwd=ROOT, env=run_env, check=True)
     self.assertEqual(state.read_text(), "0 0\n")


if __name__ == "__main__":
    unittest.main()
