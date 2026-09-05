#!/usr/bin/env bash
# Persist generator failure state and send one alert when the threshold is crossed.
set -uo pipefail
cd "$(dirname "$0")/.."
STATE="${PROPOSE_FAILURE_STATE:-evolve/logs/propose_failures.count}"
THRESHOLD="${PROPOSE_FAILURE_THRESHOLD:-3}"
NOTIFY_SCRIPT="${PROPOSE_NOTIFY_SCRIPT:-evolve/notify.sh}"
mkdir -p "$(dirname "$STATE")"

case "${1:-}" in
  success)
    printf '0 0\n' > "$STATE"
    ;;
  failure)
    count=0 alerted=0
    if [ -f "$STATE" ]; then read -r count alerted < "$STATE" || true; fi
    count=$((count + 1))
    if [ "$count" -ge "$THRESHOLD" ] && [ "$alerted" -eq 0 ]; then
      last_error="${2:-$(tail -n 1 evolve/logs/propose.log 2>/dev/null || echo unavailable)}"
      bash "$NOTIFY_SCRIPT" text "Kaggriculture: generator unhealthy" \
        "propose.py has failed $count consecutive times, last error: $last_error"
      notify_rc=$?
      [ "$notify_rc" -eq 0 ] && alerted=1
    fi
    printf '%s %s\n' "$count" "$alerted" > "$STATE"
    echo "propose consecutive failures=$count alerted=$alerted"
    ;;
  *)
    echo "usage: propose_health.sh success|failure [last-error]" >&2
    exit 2
    ;;
esac
