# v9 Adaptive-Strategy Directional Test — 2026-08-06

## Question

Is an opponent-detection rules engine + counter-strategy worth building as the v9 long-term direction, versus continuing to optimize our own fixed strategy?

## Method: test the counter before building the detector

The replay corpus is 93.2% one clone, so detection is trivial (day-0 COW+SHEEP+pasture fingerprint, readable directly off `obs.farms[1-p]` — full opponent farm state is live-observable, no proxies needed). The part of the hypothesis actually at risk is whether *countering* a known opponent beats v8.3. So we tested counters under oracle conditions (perfect opponent knowledge, no classifier) — if these fail, the rules engine has nothing to drive.

Test protocol: challenger and champion (v8.3) each play the **same opponent, same seed, same seat**; the per-seed margin difference is seat-controlled by construction. 15 seeds. Opponent: `Opponents/opp_scenario_v14.py` (top-leaderboard-derived herd script). Engine: vendored kaggriculture, local sandbox.

## Counter 1: opponent-aware sell timing (`main_v9_oracle.py`, committed 2e177de)

v8.3 + a market-forecast module: for each product, project price 2 days out from (opponent supply/day estimated live off their tiles/animals/standing yields) minus (exact town-drain schedule from `obs.town.unlocked_shops`). Projected crash → front-run at a lowered floor and skip holding phases; projected scarcity → hold paced sells. ~120 lines, four changed lines in the sell loop; all force-dump/liquidation safety paths untouched.

- **Mirror vs v8.3: exact tie, both seats** (behaviorally identical; forecast fires but never changes a binding decision — v8.3-class games stay supply-constrained, prices inflate, floors never bind). No regression risk.
- **vs herd clone: +$128/game, t=+0.55 — statistical zero.**

## Counter 2 & 3: conditional fleet sizing

If opponent type were detectable, would switching to a different on-disk strategy pay against the herd clone?

| challenger vs v8.3, same opponent | paired diff/game | t |
|---|---|---|
| main_v9_oracle.py (sell timing) | +$128 | +0.55 |
| main_v8.11.py (capacity bundle, 7 cow+3 sheep) | **-$5,358** | **-2.43** |
| turn_08_small_cow_fleet.py (smaller fleet) | +$737 | +0.56 |

Scaling animals INTO pools the herd opponent floods is significantly worse; shrinking the fleet is a wash. No on-disk strategy variant does better than v8.3 against the herd clone conditional on knowing it's a herd clone.

## Structural findings

1. **v8.3 loses to all 5 local top-leader clones, every seed, by ~$52–75k/game** (mean -$62,202 vs scenario_v14). All five run 11–15-animal herds (checked empirically: kaito 13, replay_shield 14, soil 11, + scenario/frontier). None of them is the mass-field 1+1-animal clone from the identifier doc — the local Opponents folder has no replica of the 93% clone.
2. **The market coupling between farms is too weak for reactive play to move money.** I0=10,000 buffers with sqrt/log price shaping mean opponent supply mostly determines *their* income, not ours; sell-timing is a ~$100s lever while the structural gap is ~$60k. The game at our margin is nearly two solitaire economies sharing softly-coupled pools.
3. The live ladder (90W/76L overall) is much softer than these clones — the mass field is beatable with our current line; the top tier is unreachable by reactive adjustment.

## Directional answer

**Adaptive counter-play is a dead direction on this game's mechanics — do not invest in the rules engine as a win lever.** Detection is free but has nothing profitable to trigger: the market channel (timing) is worth ~nothing, and the strategy-switch channel makes things worse or nothing with the variants we own. The human-strategy-game intuition (observe → deduce → counter) doesn't transfer because the interaction bandwidth between farms is tiny by design.

**What today's data says to do instead:** the herd clones beat v8.3 by $60k *structurally*, and we have five of them locally as sparring partners. The proven approach — study what the stronger economy actually earns money from (herd scale? the ~1200-unit trading loop? labor allocation?) and replicate the mechanism — now has a much stronger target and a local test bench. That's mimicry, not adaptation, and it's where the $60k is.

The v9 forecast module is shelf-ready and regression-free (exact tie in mirror) — it can ride along in any future version at zero cost, it just doesn't win games by itself.

## Artifacts

- `main_v9_oracle.py` — committed (2e177de), NOT submitted to ladder (no reason to: identical to v8.3 in-family, null vs clones).
- Raw per-seed results: 60 games, `/tmp/v9s.tsv` (sandbox-transient); per-seed tables reproduced above and in session log.
- Test runner pattern: paired same-seed-same-seat vs a common opponent — cheaper and seat-controlled; reusable for future counter tests.
