#!/usr/bin/env python3
"""Per-item revenue/price/timing decomposition of A vs B over N seeds (A in seat 0).

  python3 decompose.py candidates/C1.py Opponents/tape_yuan800_104892947.py --seeds 1-10
"""
import argparse
import collections
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mini_engine as me  # noqa: E402

ITEMS = ["STRAWBERRY", "MELON", "MILK", "WOOL", "WHEAT", "FERTILIZER", "EGG", "CARROT", "TOMATO"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("a")
    p.add_argument("b")
    p.add_argument("--seeds", default="1-10")
    p.add_argument("--engine", default="master")
    args = p.parse_args()
    seeds = []
    for part in args.seeds.split(","):
        if "-" in part:
            x, y = part.split("-"); seeds += list(range(int(x), int(y) + 1))
        else:
            seeds.append(int(part))
    rs = [me.run_game(args.a, args.b, s, args.engine) for s in seeds]
    n = len(rs)
    agg = [collections.defaultdict(lambda: [0, 0]) for _ in range(2)]
    buy = [collections.defaultdict(lambda: [0, 0]) for _ in range(2)]
    sday = [collections.defaultdict(lambda: [0, 0]) for _ in range(2)]
    for r in rs:
        for i in range(2):
            for d, day in enumerate(r["trace"][i]["sales"]):
                for it, (q, rev) in day.items():
                    agg[i][it][0] += q / n; agg[i][it][1] += rev / n
                    sday[i][it][0] += d * q; sday[i][it][1] += q
            for day in r["trace"][i]["buys"]:
                for it, (q, c) in day.items():
                    buy[i][it][0] += q / n; buy[i][it][1] += c / n
    na, nb = Path(args.a).stem[:10], Path(args.b).stem[:10]
    print(f"{'item':11s} {na+' units':>12s} {'$':>7s} {'avg':>5s} {'day':>5s} | {nb+' units':>12s} {'$':>7s} {'avg':>5s} {'day':>5s} | gap")
    tot = 0
    for it in ITEMS:
        a, b = agg[0][it], agg[1][it]
        if a[0] == 0 and b[0] == 0:
            continue
        gap = a[1] - b[1]; tot += gap
        da = sday[0][it][0] / max(1, sday[0][it][1]); db = sday[1][it][0] / max(1, sday[1][it][1])
        print(f"{it:11s} {a[0]:12.0f} {a[1]:7.0f} {a[1]/max(a[0],1):5.0f} {da:5.1f} | {b[0]:12.0f} {b[1]:7.0f} {b[1]/max(b[0],1):5.0f} {db:5.1f} | {gap:+7.0f}")
    print("sales gap", round(tot))
    bg = 0
    for it in sorted(set(buy[0]) | set(buy[1])):
        a, b = buy[0][it], buy[1][it]; bg += a[1] - b[1]
        print(f"  buy {it:11s} {a[0]:5.0f}u ${a[1]:6.0f} | {b[0]:5.0f}u ${b[1]:6.0f} | {-(a[1]-b[1]):+7.0f}")
    print("buy-cost gap", round(-bg))
    mA = sum(r["money"][0] for r in rs) / n; mB = sum(r["money"][1] for r in rs) / n
    print(f"money {na} ${mA:,.0f}  {nb} ${mB:,.0f}  gap {mA-mB:+,.0f}")
    # trajectory medians
    import statistics as st
    for key in ("animals", "hands_eod", "land", "money"):
        ta = [st.median(r["trace"][0][key][d] for r in rs) for d in (0, 3, 5, 7, 10, 15, 20, 25, 29) if d < len(rs[0]["trace"][0][key])]
        tb = [st.median(r["trace"][1][key][d] for r in rs) for d in (0, 3, 5, 7, 10, 15, 20, 25, 29) if d < len(rs[0]["trace"][1][key])]
        print(f"{key:9s} A:", " ".join(f"{x:6.0f}" for x in ta)); print(f"{'':9s} B:", " ".join(f"{x:6.0f}" for x in tb))


if __name__ == "__main__":
    main()
