#!/usr/bin/env bash
# Nightly evolution run. Usage: evolve/run_nightly.sh [hours] [frontier.py]
#   HOURS default 8; JOBS default = cores-1.
# Writes evolve/logs/<run>.log, evolve/reports/<run>.md and evolve/reports/latest.md.
set -euo pipefail
cd "$(dirname "$0")/.."

HOURS="${1:-${HOURS:-8}}"
FRONTIER="${2:-${FRONTIER:-candidates/V3_12.py}}"
if command -v sysctl >/dev/null 2>&1 && sysctl -n hw.ncpu >/dev/null 2>&1; then
  CORES=$(sysctl -n hw.ncpu)
else
  CORES=$(nproc)
fi
JOBS="${JOBS:-$(( CORES > 1 ? CORES - 1 : 1 ))}"
RUN_ID="$(date +%Y%m%d-%H%M)"
PY="${PYTHON:-python3}"

mkdir -p evolve/logs evolve/reports
echo "[$(date)] starting run $RUN_ID: hours=$HOURS jobs=$JOBS frontier=$FRONTIER python=$($PY --version 2>&1)" | tee -a evolve/logs/nightly.log

# caffeinate keeps a Mac awake for the duration (no-op elsewhere)
if command -v caffeinate >/dev/null 2>&1; then
  caffeinate -i "$PY" evolve/loop.py --hours "$HOURS" --jobs "$JOBS" --frontier "$FRONTIER" --run-id "$RUN_ID"
else
  "$PY" evolve/loop.py --hours "$HOURS" --jobs "$JOBS" --frontier "$FRONTIER" --run-id "$RUN_ID"
fi

cp "evolve/reports/$RUN_ID.md" evolve/reports/latest.md
echo "[$(date)] finished run $RUN_ID -> evolve/reports/$RUN_ID.md" | tee -a evolve/logs/nightly.log
