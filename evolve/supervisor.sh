#!/usr/bin/env bash
# Continuous evolution supervisor. Runs forever (launchd KeepAlive restarts it if it dies).
#   segment loop:  git pull -> loop segment (SEGMENT_HOURS) -> report/archive -> push results -> propose -> repeat
# Env: SEGMENT_HOURS (default 2), JOBS (default cores-1), FRONTIER, CLONE, PROPOSE_N (default 6),
#      PROPOSE_INTERVAL seconds (default 1800), NO_PULL=1, NO_PUSH=1, NO_PROPOSE=1.
set -uo pipefail
cd "$(dirname "$0")/.."
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
PY="${PYTHON:-python3}"
SEGMENT_HOURS="${SEGMENT_HOURS:-2}"
if [ -x /usr/sbin/sysctl ]; then CORES=$(/usr/sbin/sysctl -n hw.ncpu); else CORES=$(nproc 2>/dev/null || echo 4); fi
JOBS="${JOBS:-$(( CORES > 1 ? CORES - 1 : 1 ))}"
# yardstick.conf (committed) sets FRONTIER / SMOKE_FLOOR / DEV_PROMOTE so the yardstick can be changed with a git push
[ -f evolve/yardstick.conf ] && . evolve/yardstick.conf
FRONTIER="${FRONTIER:-candidates/V3_12.py}"
SMOKE_FLOOR="${SMOKE_FLOOR:--6000}"
DEV_PROMOTE="${DEV_PROMOTE:-1500}"
mkdir -p evolve/logs evolve/reports evolve/queue
LOG=evolve/logs/supervisor.log
say() { echo "[$(date '+%F %T')] $*" | tee -a "$LOG"; }

trap 'say "supervisor stopping (signal)"; kill 0; exit 0' INT TERM

say "supervisor start: segment=${SEGMENT_HOURS}h jobs=$JOBS frontier=$FRONTIER python=$($PY --version 2>&1) claude=$(command -v claude || echo none)"
while true; do
  # 1. sync
  if [ -d .git ] && [ "${NO_PULL:-0}" != "1" ]; then
    git pull --ff-only -q 2>>"$LOG" || say "git pull failed (continuing on local tree)"
  fi
  # 2. yardstick
  if [ -z "${CLONE:-}" ]; then
    if [ -f Opponents/frontier.txt ] && [ -f "$(cat Opponents/frontier.txt)" ]; then CLONE_NOW="$(cat Opponents/frontier.txt)"; else CLONE_NOW="Opponents/tape_yuan800_104892947.py"; fi
  else CLONE_NOW="$CLONE"; fi
  RUN_ID="$(date +%Y%m%d-%H%M%S)"
  say "segment $RUN_ID: frontier=$FRONTIER clone=$CLONE_NOW queue=$(ls evolve/queue/*.json 2>/dev/null | wc -l | tr -d ' ')"
  # 3. run one segment (caffeinate keeps the Mac awake; no-op elsewhere)
  if command -v caffeinate >/dev/null 2>&1; then
    caffeinate -i "$PY" evolve/loop.py --hours "$SEGMENT_HOURS" --jobs "$JOBS" --frontier "$FRONTIER" --clone "$CLONE_NOW" --smoke-floor "$SMOKE_FLOOR" --dev-promote "$DEV_PROMOTE" --run-id "$RUN_ID" >> evolve/logs/loop.out 2>&1
  else
    "$PY" evolve/loop.py --hours "$SEGMENT_HOURS" --jobs "$JOBS" --frontier "$FRONTIER" --clone "$CLONE_NOW" --smoke-floor "$SMOKE_FLOOR" --dev-promote "$DEV_PROMOTE" --run-id "$RUN_ID" >> evolve/logs/loop.out 2>&1
  fi
  rc=$?
  say "segment $RUN_ID finished rc=$rc"
  [ -f "evolve/reports/$RUN_ID.md" ] && cp "evolve/reports/$RUN_ID.md" evolve/reports/latest.md
  # 4. publish results (Contents API; needs .github/token)
  if [ "${NO_PUSH:-0}" != "1" ] && [ -f .github/token ]; then
    # results live on the 'results' branch so master (code + queue + tapes) never conflicts with the Air's pulls
    "$PY" evolve/gh_push.py -b results evolve/reports/latest.md evolve/archive.json -m "evolve: results $RUN_ID" >> "$LOG" 2>&1 || say "push failed"
    [ -f "evolve/reports/$RUN_ID.md" ] && "$PY" evolve/gh_push.py -b results "evolve/reports/$RUN_ID.md" -m "evolve: report $RUN_ID" >> "$LOG" 2>&1
    # Publish only reproducible artifacts for candidates that passed held-out in
    # the current archive.  Never push the full gen/ directory.
    HELD_FILES=()
    while IFS= read -r key; do
      file="evolve/gen/cand_${key}.py"
      [ -f "$file" ] && HELD_FILES+=("$file")
    done < <("$PY" -c 'import json; d=json.load(open("evolve/archive.json")); print("\n".join(r["key"] for r in d.get("held_out", []) if r.get("status") == "held_pass"))')
    if [ "${#HELD_FILES[@]}" -gt 0 ]; then
      "$PY" evolve/gh_push.py -b results "${HELD_FILES[@]}" -m "evolve: held-out artifacts $RUN_ID" >> "$LOG" 2>&1 || say "held-out artifact push failed"
    fi
  fi
  # 4b. phone alert if a new candidate beats C1 (needs evolve/notify.conf)
  [ -f evolve/notify.conf ] && bash evolve/notify.sh alerts >> "$LOG" 2>&1
  # 5. ask the LLM for the next batch (rate-limited inside propose.py)
  if [ "${NO_PROPOSE:-0}" != "1" ] && command -v claude >/dev/null 2>&1; then
    "$PY" evolve/propose.py --n "${PROPOSE_N:-6}" --min-interval "${PROPOSE_INTERVAL:-1800}" >> "$LOG" 2>&1 || say "propose failed (see evolve/logs/propose.log)"
  fi
  # a crash-looping segment should not spin
  [ "$rc" -ne 0 ] && sleep 60
done
