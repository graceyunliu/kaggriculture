# Cloud evolution results and search memory — Sep 11, 2026

This is the canonical memory for the Manus and Perplexity runs. Attached reports are evidence, not instructions. Future agents and the autonomous proposer must not describe a candidate as an improvement unless it passes every configured local gate; only ladder evidence can make it ladder-verified.

## Baseline and evaluator corrections

- O26 (`candidates/O26_CARROT_SIZING.py`) is the frozen frontier. Early Manus results showing six large held-out wins were invalid for O26 selection because the evolvable chassis was not behaviorally identical to O26.
- The chassis was rebuilt from O26 and verified on seeds 1, 2, 31, 32, 41, and 42, both seats, cache disabled: identical actions/traces, identical final money, zero errors and exactly $0 paired difference. `check_o26_equivalence.py` is the required guard.
- A strong frontier may reject every island seed. Bootstrap mutation from the configured seed is required when there is no alive parent; otherwise the loop silently spins.
- Development is one preregistered 30-seed decision: blocks 1-10, 31-40, and 41-50 must each be positive, and the pooled result must have margin >= $1,500 and t >= 2. No block has its own margin/t promotion gate.
- Missing population baselines fail closed. Local survivors are `pending_external_validation`, never ladder-verified.

## Run evidence

### Exact-O26 five-minute Manus run

25 candidates / 1,774 games / 19,342 games/hour. Three candidates cleared the three development blocks; none passed all final gates. `c89abae0234a` reached held-out +$2,199 (t=2.3) but population delta was -$250. `4ced46f13e89` reached held-out +$1,956 (t=2.7) but population delta was -$753. Neither is promotable.

### Preregistered 2^4 factorial

Factors were open wheat 7/9, fertilizer carry 2/1, melon max tiles 38/31, and herd last day 17/15. Only the open-wheat=9 plus fert-carry=1 cells passed the old development set (+$1,942, t=2.94); the signal reversed on fresh confirmation seeds 71-90 (-$817, t=-1.35, 9-11). `MELON_MAX_TILES` had exactly zero estimated effect and is not used by the exact-O26 decision path. `HERD_LAST_DAY` was negligible. Do not retry this branch without a new causal mechanism.

### Perplexity execution check

29 candidates / 1,078 games / 11,863 games/hour, with exact-O26 equivalence and zero errors. No candidate reached held-out. This validated Perplexity as a runner but produced no strategy evidence.

### Interrupted Perplexity 30-minute run

Perplexity's sandbox failed after about 26 minutes of a second attempt, after an earlier attempt had been killed by its process supervisor. The database, generated sources, and complete logs were not recovered, so candidate identities below are evidence labels only and cannot reconstruct their parameter bundles.

- `7a735e93b1b9`: pooled dev +$1,989 (t=3.2); held-out +$2,576 (t=2.4), but historical-panel margin delta -$2,748 and own-money delta -$2,016. Final status: rejected.
- `26bb1ab37c2d`: pooled dev +$3,380 (t=4.8); held-out +$2,703 (t=3.2); historical-panel delta +$1,027 and own +$1,971, but population delta -$3,344 and population own -$4,775. Final status: rejected.
- `a34a48f59746`: pooled dev +$4,965 (t=5.6), but the sandbox died during held-out evaluation. Status: incomplete, never promoted, and not evidence of improvement.

The cloud edit used `range(131, 150)`, which is only seeds 131-149. The canonical pipeline uses `range(131, 151)` for the declared inclusive 131-150 panel. Because at least 131-149 were evaluated for frozen baselines, conservatively treat the entire 131-150 range as exposed after this run; rotate population validation before the next final-gate evaluation.

### Manus broad-behavioral run

141 candidates / 5,804 games / 17,378 games/hour, zero errors. No candidate reached fresh confirmation. `bf757c08b2cc` scored +$2,011, t=1.9 on seeds 1-10 but was prematurely rejected by the obsolete single-block pre-screen.

### Targeted pooled evaluation of `bf757c08b2cc`

The candidate was evaluated once under the corrected contract. Block margins were +$2,010.6 (seeds 1-10), +$43.6 (31-40), and +$1,233.4 (41-50). Although every block was positive, the pooled result was only +$1,095.9, t=1.85, 19-11. It failed both pooled thresholds and is closed. Confirmation seeds 111-130 and population seeds 131-150 were not evaluated in this targeted trial; they were subsequently exposed by the interrupted Perplexity run below.

### Manus rapid search: `f01cec5376e1`

An additional five-minute parameter search evaluated 18 candidates. `f01cec5376e1` passed all three development blocks (+$6,731.2 / +$5,130.9 / +$5,940.9; pooled +$5,934.3, t=6.29, 28-2) but failed confirmation on the already-retired seeds 111-130: +$2,677, t=1.67, 10-10. Its historical-panel delta was +$844 and own-money delta +$1,707, but no population evaluation was allowed. Final status: rejected, not `pending_external_validation`.

Exact changes from O26 were: `load_per_hand` 20->19, `open_melons` 10->4, `wheat_cap` 22->25, `MAX_HANDS` 14->12, `ROUTE_LEN` 3->2, `CROP_SWEEP_LEN` 6->7, `STRAW_CUTOFF` 19->20, `HERD_LAST_DAY` 17->20, `NEAR_RADIUS` 2->4, `SPREAD_W` 1.25->1.0, `MELON_MORNING` 1->0, and `MELON_MORNING_LAST_HOUR` 8->7. Do not retest this bundle on newer quarantined seeds merely because its development margin was large.

### O26 capital look-ahead factorial

A preregistered OFF + 2x2x2 factorial wrapped O26's purchase orders with a deterministic 2/4-day cash-and-labor reserve gate. OFF reproduced O26 exactly. Every ON cell failed every development block. The least-negative cell (four-day horizon, 25% revenue haircut, inputs-only reserve) lost $125,913/game with t=-28.25. Own money fell to roughly $16k-$18k while opponents rose to roughly $144k-$145k. Final productive capacity collapsed from O26's averages of 14.2 animals, 5.3 maximum hands, and 3.0 land to 4.3-4.7 animals, 1.8-3.3 hands, and 1.7-1.8 land.

The mechanism failure is specific and decisive: a hard global veto that reserves several days of projected feed/setup before allowing each current purchase blocks the investments needed to produce the cash and capacity assumed by the projection. This self-reinforcing starvation loop is rejected. It does not prove that all look-ahead is useless; any future planner must rank incremental investments or compare action alternatives, not apply another all-purchase solvency veto. Confirmation 151-170 and population 171-190 were untouched.

## Seed exposure ledger

- Development/search-visible: 1-10, 31-50.
- Previously exposed validation: 11-30, 51-110. These cannot support a new fresh-validation claim.
- Previously exposed confirmation: 111-130 (two candidates completed held-out evaluation during the interrupted Perplexity run).
- Previously exposed population: 131-150 (the interrupted Perplexity run computed its frontier baselines; its code omitted seed 150, but the full declared range is retired conservatively).
- Current quarantined confirmation: 151-170.
- Current quarantined population: 171-190.

After either current quarantined range is inspected, record that fact here and preregister new disjoint ranges before another search.

## Current action

O26 remains the only submission candidate. The global hard-veto capital planner is closed; do not soften its reserve constants and retry the same architecture. The parallel adaptive-opening diagnosis remains the next independent structural investigation. Preserve final-gate-first reporting and archive all failures so the proposer cannot recycle them as novel ideas.
