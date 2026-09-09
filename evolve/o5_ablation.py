#!/usr/bin/env python3
"""Sep 9: does closing the residual DROP->SELL 1-hour lag (same-turn top-up) help?
Paired same-seed margin: O5_SAMETURN_SELL vs O4 (current frontier), then cross-check
vs C1 and V3_15 to confirm it isn't a fluke of one opponent.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

C = "candidates/"
O4 = C + "O4_PRODUCTIVE_SERVICE.py"
O5 = C + "O5_SAMETURN_SELL.py"
O6 = C + "O6_MELON_RUSH.py"
O7 = C + "O7_WHEAT_LIFECYCLE_SELL.py"
O8 = C + "O8_MORE_ANIMAL_CLAIM.py"
O8P = C + "O8_PURE_ANIMAL_THROTTLE.py"
Clone = "Opponents/opp_scenario_v14.py"
C1 = C + "C1.py"
V15 = C + "V3_15.py"

def run(a, b, seeds, label):
    r, dt = cascade._eval(a, b, seeds, "master", jobs=5)
    print(f"[{label}] {a} vs {b}: mean_margin={r['mean_margin_per_game']:.1f}/game  t={r['t']:.2f}  wins={r['wins']}-{r['losses']}  errors={r['agent_errors']}")

if __name__ == "__main__":
    import sys
    if "o8pure" in sys.argv:
        run(O8P, O4, list(range(1, 11)), "DEV O8PurevsO4")
        run(O8P, O4, list(range(11, 31)), "HELD O8PurevsO4")
        run(O8P, C1, list(range(1, 11)), "DEV O8PurevsC1")
        run(O8P, V15, list(range(1, 11)), "DEV O8PurevsV3_15")
    elif "o8clone" in sys.argv:
        run(O8P, Clone, list(range(1, 11)), "DEV O8PurevsClone")
        run(O4, Clone, list(range(1, 11)), "DEV O4vsClone")
        run(O8P, Clone, list(range(11, 31)), "HELD O8PurevsClone")
    elif "o8held" in sys.argv:
        run(O8, O4, list(range(11, 31)), "HELD O8vsO4")
        run(O8, C1, list(range(1, 11)), "DEV O8vsC1")
        run(O8, V15, list(range(1, 11)), "DEV O8vsV3_15")
    elif "o6" in sys.argv:
        run(O6, O4, list(range(1, 11)), "DEV O6vsO4")
        run(O6, O4, list(range(11, 31)), "HELD O6vsO4")
        run(O6, O5, list(range(1, 11)), "DEV O6vsO5")
    elif "o8" in sys.argv:
        run(O8, O4, list(range(1, 11)), "DEV O8vsO4")
        run(O8, O7, list(range(1, 11)), "DEV O8vsO7")
    elif "o7" in sys.argv:
        run(O7, O4, list(range(1, 11)), "DEV O7vsO4")
        run(O7, O4, list(range(11, 31)), "HELD O7vsO4")
        run(O7, O5, list(range(1, 11)), "DEV O7vsO5")
        run(O7, C1, list(range(1, 11)), "DEV O7vsC1")
        run(O7, V15, list(range(1, 11)), "DEV O7vsV3_15")
    else:
        run(O5, O4, list(range(1, 11)), "DEV O5vsO4")
        run(O5, O4, list(range(11, 31)), "HELD O5vsO4")
        run(O5, C1, list(range(1, 11)), "DEV O5vsC1")
        run(O5, V15, list(range(1, 11)), "DEV O5vsV3_15")
