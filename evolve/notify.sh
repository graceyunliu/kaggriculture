#!/usr/bin/env bash
# Push a message via ntfy.sh (phone app / browser / optional email forward). No account needed.
#   evolve/notify.sh digest            # send the full morning digest
#   evolve/notify.sh alerts            # send only new "beats C1" alerts (no-op if none)
#   evolve/notify.sh text "title" "message"
# Config: evolve/notify.conf (gitignored), one or both backends:
#   HERMES_TARGET=qqbot  HERMES_PROFILE=oreo     -> `hermes send` through Grace's Oreo QQ bot (needs ~/.hermes on this machine)
#   NTFY_TOPIC=...  [NTFY_URL=https://ntfy.sh]  -> ntfy push (phone app)
set -uo pipefail
cd "$(dirname "$0")/.."
CONF=evolve/notify.conf
[ -f "$CONF" ] || { echo "no $CONF (need NTFY_TOPIC=...)"; exit 2; }
# shellcheck disable=SC1090
. "$CONF"
NTFY_URL="${NTFY_URL:-https://ntfy.sh}"
[ -n "${NTFY_TOPIC:-}${HERMES_TARGET:-}" ] || { echo "set NTFY_TOPIC and/or HERMES_TARGET in $CONF"; exit 2; }
HERMES_PY="${HERMES_PY:-$HOME/.hermes/hermes-agent/venv/bin/python}"

send() {  # title, body, priority, tags
  local title="$1" body="$2" prio="${3:-default}" tags="${4:-}" ok=1
  if [ -n "${HERMES_TARGET:-}" ] && [ -x "$HERMES_PY" ]; then
    HERMES_HOME="$HOME/.hermes" "$HERMES_PY" -m hermes_cli.main --profile "${HERMES_PROFILE:-oreo}" send --to "$HERMES_TARGET" \
      --subject "[$title]" --file - <<< "$body" >> evolve/logs/notify.log 2>&1 && ok=0
    echo "[$(date '+%F %T')] hermes $HERMES_TARGET '$title' -> rc=$ok" >> evolve/logs/notify.log
  fi
  if [ -n "${NTFY_TOPIC:-}" ]; then
    local args=(-s -o /dev/null -w "%{http_code}" -H "Title: $title" -H "Priority: $prio" -H "Markdown: yes")
    [ -n "$tags" ] && args+=(-H "Tags: $tags")
    code=$(curl "${args[@]}" --data-binary "$body" "$NTFY_URL/$NTFY_TOPIC")
    echo "[$(date '+%F %T')] ntfy '$title' -> $code" >> evolve/logs/notify.log
    [ "$code" = "200" ] && ok=0
  fi
  return $ok
}

mkdir -p evolve/logs
case "${1:-digest}" in
  digest)
    body=$(python3 evolve/digest.py 2>&1)
    head1=$(echo "$body" | sed -n 2p)
    if echo "$body" | grep -q "^BEATS C1"; then prio=high; tags=tada; else prio=default; tags=seedling; fi
    send "Kaggriculture evolve digest" "$body" "$prio" "$tags" ;;
  alerts)
    body=$(python3 evolve/digest.py --alerts 2>&1)
    [ -z "$body" ] && exit 0
    send "Kaggriculture: candidate beats C1" "$body" high "tada" ;;
  text)
    send "${2:-Kaggriculture}" "${3:-}" default "" ;;
  *) echo "usage: notify.sh digest|alerts|text title msg"; exit 2 ;;
esac
