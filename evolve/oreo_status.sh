#!/usr/bin/env bash
# One-shot live status snapshot for Oreo (or anyone) to relay as-is.
# No arguments, no interpretation needed -- just run and report the output.
set -uo pipefail
cd "$(dirname "$0")/.."

echo "=== Kaggriculture evolve loop status ($(date '+%F %T')) ==="
echo

echo "--- digest ---"
python3 evolve/digest.py 2>&1
echo

echo "--- is the loop actually running right now? ---"
if pgrep -f "evolve/loop.py" > /dev/null 2>&1; then
  echo "loop.py: RUNNING"
else
  echo "loop.py: NOT running (check launchd: launchctl list | grep kaggriculture)"
fi
echo

echo "--- last 5 supervisor log lines ---"
tail -5 evolve/logs/supervisor.log 2>/dev/null || echo "(no supervisor.log yet)"
echo

if [ -f evolve/PROMOTION_PENDING.txt ]; then
  echo "--- *** PROMOTION PENDING, needs human review *** ---"
  cat evolve/PROMOTION_PENDING.txt
  echo
fi

if [ -f evolve/logs/propose_failures.count ]; then
  fc=$(cat evolve/logs/propose_failures.count 2>/dev/null || echo 0)
  [ "$fc" != "0" ] && echo "--- propose.py consecutive failures: $fc ---" && echo
fi

echo "--- leaderboard replay disk usage ---"
du -sh Replays/Auto/leaderboard-* 2>/dev/null || echo "(no leaderboard replays yet)"
