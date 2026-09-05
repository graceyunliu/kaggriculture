# Coupled allocation and hiring results (P7)

## Verdict

No candidate was promoted. The coupled P7 model regressed decisively in the full-game sanity stage and continued to regress in both permitted debugging rounds. The working candidate remains P6 (`candidates/P.py`, frozen identically as `candidates/P6_baseline.py`). P7 is retained only as `candidates/P7.py` for diagnosis.

This is not a marginal result: the initial model lost $3,327/game to E1 (t = -3.06), and the two repairs lost $17,775/game (t = -3.57) and $21,454/game (t = -5.65). Per the two-round stop rule, the remaining factorial cells and all held-out tests were gated off rather than searched after observing a decisive regression.

## Intended factorial

The preregistered small grid coupled three state-based axes. None keys on opponent identity or opponent actions.

| axis | low | high |
|---|---|---|
| hiring aggressiveness | committed daily load / 14 hand-hours | committed daily load / 12 hand-hours, with 15% deadline reserve |
| admission | current banded seed/animal admission | refuse commitments above the 13-hand service ceiling and require projected staffing affordability |
| market liquidation | P6 sale schedule | earlier deposits/liquidation when carried output and remaining days make holding unproductive |

The eight-cell grid was to be screened on the H32 and E1 day ledgers, then evaluated by full games in order: smoke (seeds 1-4, both seats, C1), dev (1-10, both seats, E1 and C1), and held-out (11-30, both seats, E1, C1, H10, tape_kiro, and tape_antigone). The search stopped before this grid could be completed because the common coupled hiring/admission mechanism failed the mandatory full-game sanity gate and both allowed repair rounds. Unrun cells are reported below rather than silently omitted.

| hiring | admission | liquidation | bench pre-filter | smoke | dev | held-out |
|---|---|---|---|---|---|---|---|
| low | current | P6 | P6 control: pass | not rerun; established control | E1 +$2,551/game, t=1.51, 8-2 | established P6 results; not selection data here |
| low | current | earlier | not run | gated | gated | gated |
| low | capped/affordable | P6 | not run | gated | gated | gated |
| low | capped/affordable | earlier | not run | gated | gated | gated |
| high | current | P6 | not run separately | gated | gated | gated |
| high | current | earlier | not run | gated | gated | gated |
| high | capped/affordable | P6 | H32: travel 1.008, cov_all 0.963, cov_hard 0.999; E1 ledger: cov_hard 1.002, cov_all 1.000 | full-game sanity used instead of C1 smoke: -$3,327/game vs E1, t=-3.06, 2-8 | failed gate | gated |
| high | capped/affordable | earlier | not run | gated | gated | gated |

The deviation from the requested C1-first cascade is explicit: inherited work had already run the stricter ten-seed E1 sanity test before this report was created. Once that test and two subsequent repairs were decisively negative, running easier smoke cells or held-out opponents could no longer justify promotion and would violate the stop discipline.

## Model and debugging rounds

P7 estimated next-day labor from the planner's own committed state: planted and planned crop tiles, mean crop distance, total animals, setup work, urgent/weeds backlog, day, cash, and Fibonacci hire cost. The same estimate constrained animal, seed, and land admission, so labor demand and commitments were coupled rather than fitted to H32's hand trajectory.

| full-game stage (both seats) | seeds | margin vs E1 | t | W-L | result |
|---|---:|---:|---:|---:|---|
| P6 control | 1-10 | +$2,551 | 1.51 | 8-2 | reproduced baseline |
| P7 initial | 1-10 | -$3,327 | -3.06 | 2-8 | sanity failure |
| repair 1: increase animal/setup load | 1-10 | -$17,775 | -3.57 | 0-10 | worse |
| repair 2: require immediate post-purchase staffing affordability | 1-10 | -$21,454 | -5.65 | 0-10 | worse; stop |

No combination reached dev or held-out, so there is no winner diagnosis to manufacture and no held-out t-statistic to report.

## Causal diagnosis

The seed-1 before/after trace localized the failure upstream. P6 stabilized at roughly 8 animals and 60-66 crop tiles. Initial P7 instead reached 18 animals and only about 37 crop tiles. The added animals consumed setup cash and recurring feed/care capacity; the shared capacity constraint then suppressed seeds and land exactly when crop production should have expanded.

The repairs made that interaction worse. Raising animal/setup load did not rebalance the portfolio; it reduced productive commitments. Requiring every purchase to fund its projected hires immediately treated lumpy setup spending and steady-state service capacity as if they occurred on the same cash horizon. That delayed commitments at the wrong points in the cash cycle and produced the final $21.5k/game regression.

The bench did not predict this failure because it replayed expert states with expert hires. It confirmed that P6/P7 could execute those supplied days (hard coverage about 1.0, travel 1.008), but it could not observe the endogenous 18-animal/37-crop state reached in full games. This is precisely why the full-game gate controls promotion.

## Remaining gap

Because P7 was rejected, the gap remains P6's measured gap: approximately -$9,374/game to H10 and -$22,908 to -$27,000/game to the reported frontier tapes on held-out seeds 11-30. No claim is made that coupled allocation/hiring closed any of it.
