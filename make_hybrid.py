#!/usr/bin/env python3
"""Build a tape-prefix hybrid: replay a recorded seat's actions for the first SWITCH_DAY days,
then hand over to the K.py policy. Adds two robustness features H10 lacked:

  * divergence guard: per-step signatures (money, hands, animals owned, shed wheat) from the
    source replay are embedded; if the live state drifts past tolerance, the policy takes over
    immediately instead of executing actions meant for a state that no longer exists;
  * optional cycle-free opening: replaces the tape's turn-0/1 wheat round-trip (a $133 no-op
    that is fragile in lockstep with an opponent doing the same) with a direct purchase.

  python3 make_hybrid.py Replays/.../episode-104892947-replay.json 1 --switch-day 10 \
      --knobs '{"opening":"frontier","early_hire_days":5,"feed_spare_poor":0,"open_melons":8}' \
      --no-cycle -o candidates/H11.py
"""
import argparse
import base64
import json
import re
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def build(replay, seat, switch_day, knobs, no_cycle, out, money_tol=400, count_tol=1):
    d = json.load(open(replay))
    steps = d["steps"]
    actions, sigs = [], []
    for k in range(1, len(steps)):
        a = steps[k][seat].get("action") or {}
        actions.append({"farmer": a.get("farmer", ["PASS"]), "hands": a.get("hands", []), "market": a.get("market", [])})
    for k in range(0, len(steps) - 1):
        o = steps[k][seat]["observation"]
        farm = o["farms"][seat]
        priv = o.get("private", {}) or {}
        shed = priv.get("shed", {}) or {}
        inv = priv.get("inventories", []) or []
        placed = sum(1 for row in farm["tiles"] for t in row if isinstance(t, dict) and "animal" in t)
        owned = placed + sum(shed.get(x, 0) for x in ("COW", "SHEEP", "GOOSE")) + \
            sum(i.get(x, 0) for i in inv for x in ("COW", "SHEEP", "GOOSE"))
        sigs.append([round(farm["money"]), len(farm["hands"]), owned, shed.get("WHEAT", 0)])
    if no_cycle:
        # turn 0: buy 53 wheat -> buy 5 wheat feed; turn 1: drop the SELL 48, keep the rest
        m0 = actions[0]["market"]
        if m0 and m0[0][0] == "BUY_PRODUCT" and m0[0][1] == "WHEAT" and int(m0[0][2]) >= 25:
            actions[0]["market"] = [["BUY_PRODUCT", "WHEAT", 5]]
            actions[1]["market"] = [o for o in actions[1]["market"] if not (o[0] == "SELL" and o[1] == "WHEAT")]
            # later tape turns sell/buy 1-2 wheat intraday; harmless (fail silently if absent)
    blob_a = base64.b85encode(zlib.compress(json.dumps(actions, separators=(",", ":")).encode(), 9)).decode()
    blob_s = base64.b85encode(zlib.compress(json.dumps(sigs, separators=(",", ":")).encode(), 9)).decode()

    k_src = (ROOT / "candidates" / "K.py").read_text()
    m = re.search(r"^KNOBS = \{.*?\}\n", k_src, re.S | re.M)
    base = eval(m.group(0)[len("KNOBS = "):])
    base.update(knobs or {})
    body = k_src[:m.start()] + "KNOBS = " + json.dumps(base) + "\n" + k_src[m.end():]
    prefix = f'''import base64 as _b64, zlib as _zlib, json as _json
_TAPE = _json.loads(_zlib.decompress(_b64.b85decode({blob_a!r})).decode("utf-8"))
_SIG = _json.loads(_zlib.decompress(_b64.b85decode({blob_s!r})).decode("utf-8"))
SWITCH_DAY = {switch_day}
MONEY_TOL = {money_tol}
COUNT_TOL = {count_tol}
_H = {{"switched": False, "why": None}}


def _live_sig(obs):
    p = obs["player"]
    farm = obs["farms"][p]
    priv = obs.get("private", {{}}) or {{}}
    shed = priv.get("shed", {{}}) or {{}}
    inv = priv.get("inventories", []) or []
    placed = sum(1 for row in farm["tiles"] for t in row if isinstance(t, dict) and "animal" in t)
    owned = placed + sum(shed.get(x, 0) for x in ("COW", "SHEEP", "GOOSE")) + sum(i.get(x, 0) for i in inv for x in ("COW", "SHEEP", "GOOSE"))
    return [round(farm["money"]), len(farm["hands"]), owned, shed.get("WHEAT", 0)]


def _diverged(obs, step):
    if step >= len(_SIG) or step < 3:
        return None
    live, rec = _live_sig(obs), _SIG[step]
    if abs(live[2] - rec[2]) > COUNT_TOL:
        return f"animals {{live[2]}} vs {{rec[2]}} at step {{step}}"
    if abs(live[1] - rec[1]) > COUNT_TOL + 1:
        return f"hands {{live[1]}} vs {{rec[1]}} at step {{step}}"
    if live[0] < rec[0] - max(MONEY_TOL, 0.5 * max(rec[0], 1)):
        return f"money {{live[0]}} vs {{rec[0]}} at step {{step}}"
    return None


def agent(obs, configuration=None):
    step = obs.get("step") if isinstance(obs, dict) else getattr(obs, "step", None)
    if step is None:
        step = obs["day"] * 24 + obs["hour"]
    if not _H["switched"] and step < SWITCH_DAY * 24 and step < len(_TAPE):
        why = _diverged(obs, step)
        if why is None:
            return _TAPE[step]
        _H["switched"] = True
        _H["why"] = why
    try:'''
    body = body.replace("def agent(obs, configuration=None):\n    try:", prefix, 1)
    assert "SWITCH_DAY" in body
    Path(out).write_text(body)
    return len(actions)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("replay")
    ap.add_argument("seat", type=int)
    ap.add_argument("--switch-day", type=int, default=10)
    ap.add_argument("--knobs", default='{"opening":"frontier","early_hire_days":5,"feed_spare_poor":0,"open_melons":8}')
    ap.add_argument("--no-cycle", action="store_true")
    ap.add_argument("--money-tol", type=int, default=400)
    ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    n = build(a.replay, a.seat, a.switch_day, json.loads(a.knobs), a.no_cycle, a.out, a.money_tol)
    print(f"wrote {a.out} ({n} tape steps, switch day {a.switch_day}, no_cycle={a.no_cycle})")


if __name__ == "__main__":
    main()
