#!/usr/bin/env bash
# One-time check on the machine that will run the loop (the MacBook Air).
# Needs only python3 (3.9+); no pip installs -- mini_engine runs the vendored engine directly.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"

echo "python: $($PY --version 2>&1)"
$PY - <<'EOF'
import sys
assert sys.version_info >= (3, 9), "need python3 >= 3.9 (brew install python@3.12)"
EOF

echo "== smoke: one game C1 vs V3_12 (master engine)"
$PY - <<'EOF'
import sys, time
sys.path.insert(0, ".")
import mini_engine as me
t = time.time()
r = me.run_game("candidates/C1.py", "candidates/V3_12.py", seed=1, engine="master")
dt = time.time() - t
assert r["errors"] == [0, 0], r["errors"]
print(f"ok: money={r['money']} errors={r['errors']} {dt:.2f}s/game")
EOF

echo "== throughput: 20 games, all cores"
$PY - <<'EOF'
import os, sys, time
sys.path.insert(0, ".")
import mini_engine as me
jobs = max(1, (os.cpu_count() or 2) - 1)
t = time.time()
r = me.evaluate("candidates/C1.py", "candidates/V3_12.py", list(range(101, 111)), engine="master",
                both_seats=True, jobs=jobs, use_cache=False)
dt = time.time() - t
print(f"jobs={jobs}: 20 games in {dt:.1f}s -> {20/dt*3600:,.0f} games/hour; C1 vs V3_12 margin {r['mean_margin_per_game']:+,.0f}")
EOF

echo "== evolution loop, 3-minute dry run"
$PY evolve/loop.py --minutes 3 --run-id setup-check
echo
echo "All good. Nightly: evolve/run_nightly.sh 8      (or install the launchd job, see evolve/README.md)"
