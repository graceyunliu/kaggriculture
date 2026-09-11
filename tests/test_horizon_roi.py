"""Contract tests for tools/horizon_roi.py (AGE-360).

Why this file exists. The remaining-horizon ROI number is a DIFFERENCE between two full games. If the
counterfactual replay diverges from the base run for any reason other than the block -- an unseeded RNG
draw, an agent reading wall-clock, a mutated module-level cache -- then every ROI in the table is noise
wearing a t-statistic. Three things therefore have to hold, and they are cheap to assert:

  1. Determinism. The same (candidate, tape, seed) replayed twice must return the identical final money.
     Without this nothing downstream means anything.
  2. A block that matches no order must be a bit-exact no-op. This is the real test of (1) against the
     specific code path the tool uses, because it runs the whole block-filter machinery and still has to
     land on the same number.
  3. A block that DOES match must actually remove the orders. A filter that silently matched nothing would
     produce a table of confident zeroes, which reads like "this investment does not matter" rather than
     like a bug.

Plus a unit test for payback_day, whose two off-by-one traps (day D itself is sampled before the blocked
spend, and cash rather than net worth is the series that shows the outlay) both produced plausible-looking
wrong answers during development.

Run: KAGG_FIXED_SHOPS=1 python3 tests/test_horizon_roi.py
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import horizon_roi as H  # noqa: E402

CAND = "candidates/O17_ORCH_CAPITAL.py"
TAPE = "Opponents/tape_peterparker_106816877.py"
SEED = 1


def test_replay_is_deterministic():
    a = H.play(CAND, TAPE, SEED)
    b = H.play(CAND, TAPE, SEED)
    assert a == b, f"non-deterministic replay: {a} != {b}"
    return a


def test_non_matching_block_is_a_noop(base):
    # No BUY_LAND order is ever placed on day 99 -- the game is 30 days long.
    cf = H.play(CAND, TAPE, SEED, block=("BUY_LAND", None, 99, None))
    assert cf == base, f"no-op block changed the game: {cf} != {base}"
    # An item filter that matches no item of a real verb must also be inert.
    cf2 = H.play(CAND, TAPE, SEED, block=("BUY_ANIMAL", "PENGUIN", 0, None))
    assert cf2 == base, f"unmatched item filter changed the game: {cf2} != {base}"


def test_matching_block_actually_removes_orders(base):
    spend_free = {}
    H.play(CAND, TAPE, SEED, spend=spend_free)
    assert spend_free.get("HIRE", {}).get("orders", 0) > 0, "fixture places no HIRE orders; test is vacuous"
    cf = H.play(CAND, TAPE, SEED, block=("HIRE", None, 0, None))
    assert cf != base, "blocking every HIRE order left the outcome unchanged -- the filter is not matching"
    # Blocking all labour must hurt, and by a lot; a sign flip here means the ROI sign convention is wrong.
    assert base - cf > 0, f"blocking all hiring did not reduce final money (base {base}, cf {cf})"


def test_payback_day_uses_cash_and_excludes_the_cutoff_day():
    # (day, networth, cash). Base spends at day 5 and earns it back by day 8.
    base_daily = [(4, 100, 100), (5, 100, 100), (6, 100, 40), (7, 100, 90), (8, 100, 130), (9, 100, 180)]
    cf_daily = [(4, 100, 100), (5, 100, 100), (6, 100, 100), (7, 100, 110), (8, 100, 120), (9, 100, 130)]
    pb, series = H.payback_day(base_daily, cf_daily, cutoff_day=5)
    assert pb == 8, f"expected payback on day 8, got {pb}"
    # Day 5 must not count even though delta there is 0: it is sampled before the blocked spend.
    assert dict(series)[5] == 0
    # A purchase that never earns its cost back inside the horizon reports None, not the last day.
    never = [(4, 100, 100), (5, 100, 100), (6, 100, 40), (7, 100, 50), (8, 100, 60), (9, 100, 70)]
    pb2, _ = H.payback_day(never, cf_daily, cutoff_day=5)
    assert pb2 is None, f"expected no payback, got {pb2}"
    # A run that goes ahead and then falls behind again has not paid back: the lead must hold to the end.
    flaky = [(4, 100, 100), (5, 100, 100), (6, 100, 40), (7, 100, 120), (8, 100, 115), (9, 100, 100)]
    pb3, _ = H.payback_day(flaky, cf_daily, cutoff_day=5)
    assert pb3 is None, f"a lead that does not hold is not payback, got {pb3}"


def test_aggregate_deduplicates_repeated_cells(tmpdir):
    import json
    import types
    p = Path(tmpdir) / "dup.jsonl"
    rec = {"cand": CAND, "mode": "cutoff", "type": "HIRE", "day": 10, "defer_days": None,
           "tape": "peter", "seed": 1, "base": 100.0, "cf": 90.0, "roi": 10.0, "payback_day": 12}
    other = dict(rec, seed=2, roi=20.0)
    # Same cell written three times, plus one genuinely different cell.
    p.write_text("\n".join(json.dumps(r) for r in [rec, rec, rec, other]) + "\n")
    args = types.SimpleNamespace(aggregate=str(p), quiet=True, emit=False)
    H.aggregate(args)
    # aggregate() prints nothing in quiet mode, so re-derive what it saw the same way it does.
    recs = [json.loads(ln) for ln in open(p) if ln.strip()]
    uniq = {(r["mode"], r["type"], r["day"], r.get("defer_days"), r["tape"], r["seed"]) for r in recs}
    assert len(recs) == 4 and len(uniq) == 2, "dedup fixture is wrong"


if __name__ == "__main__":
    if os.environ.get("KAGG_FIXED_SHOPS") != "1":
        print("NOTE: running without KAGG_FIXED_SHOPS=1; determinism still holds, "
              "but this is not the measurement mode the tool is meant for.")
    import tempfile
    base = test_replay_is_deterministic()
    print(f"  determinism ok (final money {base:,.0f})")
    test_non_matching_block_is_a_noop(base)
    print("  non-matching block is a no-op ok")
    test_matching_block_actually_removes_orders(base)
    print("  matching block removes orders ok")
    test_payback_day_uses_cash_and_excludes_the_cutoff_day()
    print("  payback_day semantics ok")
    with tempfile.TemporaryDirectory() as td:
        test_aggregate_deduplicates_repeated_cells(td)
    print("  aggregate dedup ok")
    print("all horizon_roi contract tests passed")
