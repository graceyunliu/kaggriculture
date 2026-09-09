# Phase 8: Lead 1 causal test -- labor headcount vs score (opponent-vs-opponent correlation)

Mining: `mine_oppvsopp.py`/`mine_oppvsopp2.py` (repo-relative copies below)
sample 200 files from `Replays/Auto/leaderboard-*/`, verified zero contain
`graceyunliu`. Found `max_hands` vs `final_money`: r=0.187, t=3.79, n=400.

Causal test: `variant_labor_boost.py` -- single-line change to
`candidates/V3_15.py`'s `_load_model()`, forcing the hire target +3 above
whatever the policy's own workload-based target already computed
(`tgt = min(MAX_HANDS, tgt + 3)`), funded from the SAME cash trajectory
(not free hands) -- this is the design specifically requested to address
the cash-confound: if hands have independent causal value, spending more
of the same budget on them should help; if the correlation is just
"richer play affords both hands and money," forcing extra hands should be
neutral-to-negative (paying hire cost for a hand the policy didn't
actually need).

Result: no significant score effect in any of 4 tests (matched seeds 1-20
vs one opponent, fresh seeds 101-120 vs 3 opponents) -- t = 0.01, 1.01,
-0.99, 0.52. See `../../artifacts/replay_state_policy_audit/REPORT_PHASE8_LABOR_HEADCOUNT.md`.
