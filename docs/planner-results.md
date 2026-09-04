# Day-planner executor results (Sep 4)

Status: stopped after two debugging rounds on the same regression, as required by the implementation brief. The block implementation compiles and runs without agent errors, but it does not pass the sanity floor and must not be promoted.

## Implementation

The candidate uses E1's parameter values and unchanged banded `crop_admission` block. The four `planner_*` blocks jointly enumerate crop and animal chores, assign them with deterministic insertion-cost routing, reserve route pickups, replan at hour 1, execute stale-task checks, and append same-day water immediately after planting.

## Acceptance results

### Clean run

`P` vs `V3_12`, seeds 1-3, both seats: agent errors `[0, 0]`; no `GUARD` output.

After round 2: mean P $65,742 vs V3_12 $103,742; margin/game **-$37,999**, t=-25.59, W-L 0-3.

### Process trace

Seed 1 vs V3_12 after round 2:

- final money: P $79,736 vs V3_12 $118,367
- final net worth: $84,810
- travel/work action: **1.16** (routing target met)
- missed feed: 65
- missed water: 469
- escaped animals: 0
- new weeds: 38
- maximum hands: 13; maximum animals: 14
- move share 31.5%; idle share 41.3%

The trace does not meet the coverage targets (zero weeds and at least 95% hard chores completed), so held-out and coupled-scale promotion tests were not run.

### Sanity floor

`P` vs `E1`, seeds 1-10, both seats:

- mean P: $60,710
- mean E1: $105,105
- margin/game: **-$44,395**
- t=-11.45; W-L 0-10
- agent errors `[0, 0]`

Per-seed paired margins were -$100,568, -$36,225, -$82,786, -$79,127, -$75,348, -$102,260, -$89,604, -$101,100, -$88,931, and -$131,949.

## Debugging rounds

1. Initial planner retained position-based `chore_done` ids across days. That suppressed recurring feed and water chores permanently after their first completion. Seed 1 ended at $175 net worth with 4 escapes, 21 new weeds, and 92.4% idle turns. Fix: reset completion ids at each day boundary.
2. The restored planner under-hired and allowed later insertions to push earlier-deadline plant chores past their deadline. Fixes: size labor at approximately 10 planned actions per hand-day (still bounded by hard chores/8 and MAX_HANDS), and reject a trial route if any stop misses its own deadline. This restored the economy and achieved 1.16 travel/work, but the large service and money regression remained.

## Likely causes for a future redesign

- Planning from hour-1 state only is too static. Routes become empty while unassigned and newly-created chores remain; the specified idle-with-hard-work replan/steal path is not yet implemented.
- The insertion objective minimizes incremental route length but does not account for multi-action bundles at one animal tile strongly enough. Feed/care/collect/harvest can be split across routes, wasting pickup capacity and deadlines.
- Optional recurring-crop watering is deliberately omitted unless fertilized, so the generic trace's `missed_water` includes intentional skips; however 38 weeds proves urgent recovery is also failing.
- Pickup accounting is global at plan time but execution is per inventory. Existing carried wheat can be counted as available to a different route, leaving some feed stops invalid and silently popped.
- Static plant admission can schedule planting near hour 21 without reserving enough downstream capacity after world changes.

## Decomposition (round 1, P vs E1, seeds 1-3)

Round 1 was dominated by the cross-day completion-id bug: P sold 7 wheat ($284) and 4 fertilizer ($398), but no strawberry, melon, milk, wool, or other crops. E1 sold about $190,261 more goods. Mean money was P $161 vs E1 $158,261. This decomposition is diagnostic only; it predates round 2.

The requested P-vs-tape_yuan800 decomposition was not run because the candidate failed the earlier mandatory sanity floor. Running later ladder stages would contradict the acceptance-ladder stop rule.

## P2 reliability attempt

P2 added location bundling, per-worker inventory accounting, and bounded idle-triggered replanning. Its first run was clean but produced -$72,610/game vs V3_12 on seeds 1-3; the seed-1 trace had travel/work 1.20, 123 missed feeds, 2 escapes, and 7 weeds.

The second round made every daily feed hard and suppressed optional work while hard work was unassigned. Seeds 1-3 both seats vs V3_12 remained clean (errors `[0, 0]`) but returned **-$58,784/game**. Seed 1 ended with $69,125 cash and $73,044 net worth, travel/work **1.12**, 9 missed feeds, 0 escapes, 468 missed waters, and 22 new weeds. Maximum hands was 13 and maximum animals 14; idle share remained 43.6%.

P2 therefore improved travel and animal reliability but failed the mandatory crop-coverage gate after two rounds. Later ladder stages were not run. The high idle share alongside new weeds suggests urgent-water stops are being lost during validation/replanning rather than capacity being insufficient. A future P3 should first add an independent emergency-water queue with explicit enumerated/completed counters, then reintroduce general route optimization only after that invariant passes.

## P5 challenger (post-review correction)

After the P1/P2 failure, a narrower hybrid was built on the held-out-qualified Daba allocation: wheat-shortage feed rotation plus crop-sweep work sharing. Sweep sharing is disabled after day 2 for the publicly observable low-money/four-animal opening bucket where it regresses. The state key is explicitly reset at day 0/hour 0 so evaluator workers cannot leak classification between games.

P5 is positive versus E1 but does not clear the project's significance bar: +$778/game on seeds 1-10 (t=0.48) and +$1,220/game on held-out seeds 11-30 (t=1.45). It is decisive versus V3.12 on held-out seeds: +$9,848/game, t=8.64, W-L 20-0.

Paired differences in tape margin versus E1, using identical held-out seeds 11-30 and both seats:

| tape | delta/game vs E1 | paired t | delta W-L |
|---|---:|---:|---:|
| Yuan | +$6,353 | 1.51 | 12-8 |
| Shirabe | +$6,193 | 1.75 | 12-8 |
| Atakan | +$5,210 | 1.41 | 13-7 |

All point estimates clear +$5k, but none reaches `t >= 2`. P5 is therefore a promising challenger and queue candidate, **not a statistically confirmed replacement for E1**.

## P5 expanded held-out confirmation

The initial 20-seed tape estimates above were underpowered. A preregistered-style expansion to the untouched seeds 31-100 (reported jointly as seeds 11-100, 90 seeds total, both seats) produced:

- P5 vs E1: **+$1,255/game**, t=2.66, seed W-L 59-31, agent errors `[0, 0]`.
- Yuan tape paired delta vs E1: +$675/game, paired t=0.40, delta W-L 47-43.
- Shirabe tape paired delta vs E1: **+$3,177/game**, paired t=2.15, delta W-L 50-40.
- Atakan tape paired delta vs E1: **+$3,653/game**, paired t=2.22, delta W-L 55-35.

Thus P5 now clears the project's `t >= 2` bar directly against E1 and on two of three tape opponents. The larger sample disproves the earlier apparent Yuan-specific gain: that matchup is statistically neutral, not a confirmed improvement. P5 can be treated as a confirmed overall challenger/replacement for E1, but must not be described as universally better or as a successful implementation of the original monolithic travel-minimizing planner.

## Frontier correction

P5 is not a ladder promotion candidate. On held-out seeds 11-30, both seats, it scored -$13,300/game versus H10 (t=-6.5, 3-17) and -$12,375/game versus H11 (t=-6.2, 2-18). Its E1 improvement is real but E1 is a weak baseline; H10/H11/H30 are the relevant frontier gates.
