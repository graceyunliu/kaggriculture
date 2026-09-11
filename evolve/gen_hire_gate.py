#!/usr/bin/env python3
"""Generate HIRE marginal-cost-gate candidates from a base chassis (AGE-360 follow-up, Sep 11).

Mechanism. The engine clears `farm["hands"]` at the end of every day and the n-th hire of a day costs
`_fib(n)` -- 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233. So labour is re-bought daily on a CONVEX
price curve, and the last hire of a 13-hand day costs 233 while the 9th costs 34, a 7x difference.

The chassis's `_hire_plan` tops up toward a workload-derived `target` and stops only when it runs out of
cash. It never asks whether the NEXT hire is worth its own fibonacci price. Measured wage bill: ~$6,700/game,
9.5% of final money, concentrated in the tail -- days 18-28 pay 144-233 for the last hire of the day.

This gate refuses any hire whose marginal fibonacci price exceeds HIRE_MAX_MARGINAL. Because early days
place only 5-8 hires (marginal cost <= 8), the gate is inert early and binds only on the steep tail, which
is where tools/horizon_roi.py --mode marginal measured the last hire to be value-destroying:
-$361 to -$2,108 per game at t=-2.6 to -10.4, 0% of held-out cells positive.

M maps to an effective hands/day cap: 55 -> 10, 89 -> 11, 144 -> 12, 233 -> 13, 10**9 -> uncapped (control).

Usage: python3 evolve/gen_hire_gate.py [BASE] [M ...]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OLD = '''def _hire_plan(target, have, hires_today, cash):
    """Return number of HIRE orders affordable now toward `target` hands."""
    n = 0
    spent = 0
    while have + n < target:
        c = _fib(hires_today + n)
        if spent + c > cash:
            break
        spent += c
        n += 1
    return n, spent'''

NEW = '''HIRE_MAX_MARGINAL = {M}   # refuse any hire whose own fibonacci price exceeds this (AGE-360 marginal ROI)


def _hire_plan(target, have, hires_today, cash):
    """Return number of HIRE orders affordable now toward `target` hands.

    Hands are cleared nightly and the n-th hire of a day costs _fib(n), so labour is re-bought daily on a
    convex curve. Topping up to `target` while only checking affordability buys the steep tail of that
    curve -- the 13th hire of a day costs 233 against the 9th at 34. HIRE_MAX_MARGINAL gates on the price
    of the NEXT hire, so the rule is inert on cheap early hires and binds only where the marginal
    counterfactual says the last hire destroys value.
    """
    n = 0
    spent = 0
    while have + n < target:
        c = _fib(hires_today + n)
        if c > HIRE_MAX_MARGINAL:
            break
        if spent + c > cash:
            break
        spent += c
        n += 1
    return n, spent'''


def main():
    args = sys.argv[1:]
    base = args[0] if args and args[0].endswith(".py") else "candidates/O17_ORCH_CAPITAL.py"
    ms = [int(x) for x in (args[1:] if base == (args[0] if args else None) else args)] or [55, 89, 144, 233]
    src = open(os.path.join(ROOT, base)).read()
    if OLD not in src:
        sys.exit(f"{base}: _hire_plan does not match the expected form; the chassis has drifted, "
                 f"re-derive the patch rather than editing blind.")
    stem = os.path.basename(base).replace(".py", "")
    for m in ms:
        out = src.replace(OLD, NEW.replace("{M}", str(m)), 1)
        assert out != src
        name = f"H_GATE{m}_{stem}.py"
        path = os.path.join(ROOT, "candidates", name)
        open(path, "w").write(out)
        print(f"wrote candidates/{name}  (HIRE_MAX_MARGINAL={m}, effective cap "
              f"{sum(1 for i in range(30) if _fib(i) <= m)} hands/day)")


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    main()
