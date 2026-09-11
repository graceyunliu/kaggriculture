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

### Manus broad-behavioral run

141 candidates / 5,804 games / 17,378 games/hour, zero errors. No candidate reached fresh confirmation. `bf757c08b2cc` scored +$2,011, t=1.9 on seeds 1-10 but was prematurely rejected by the obsolete single-block pre-screen. It is not a winner; it must receive blocks 31-40 and 41-50 under the corrected pooled contract before any conclusion. Do not use confirmation or population seeds to tune it.

## Seed exposure ledger

- Development/search-visible: 1-10, 31-50.
- Previously exposed validation: 11-30, 51-110. These cannot support a new fresh-validation claim.
- Current quarantined confirmation: 111-130.
- Current quarantined population: 131-150.

After either current quarantined range is inspected, record that fact here and preregister new disjoint ranges before another search.

## Current action

O26 remains the only submission candidate. First re-evaluate `bf757c08b2cc` on the remaining development blocks. Continue broad search only with controls proven renderable in the exact-O26 chassis. Preserve final-gate-first reporting and archive all failures so the proposer cannot recycle them as novel ideas.
