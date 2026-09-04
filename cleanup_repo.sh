#!/usr/bin/env bash
# One-shot repo tidy (Sep 4 2026). Run from the repo root on the Mac, review `git status`, then commit + push.
#   bash cleanup_repo.sh && git status --short | head -50
# Nothing the Air pipeline uses is moved: mini_engine.py, harness.py, sync_replays.py, pull_ladder.py,
# replay_verify.py, make_tape_agent.py, seeded_h2h.py, evolve/, vendor/, Opponents/, candidates/{C1,C2,E*,H10,H11,H12,H30,K,P,V3_11,V3_12,V3_29}.py
set -euo pipefail
cd "$(dirname "$0")"
rm -f .git/index.lock
mv_() {
    local dst="$1"
    shift
    mkdir -p "$dst"
    for f in "$@"; do
        [ -e "$f" ] || continue
        if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
            git mv -k "$f" "$dst/"
        else
            mv "$f" "$dst/"
        fi
    done
}

# 1. junk: sandbox artefacts, generated candidates, zips whose contents are already checked in, stray logs
git rm -rq --cached "Loading environment werewolf failed"* 2>/dev/null || true
rm -rf "Loading environment werewolf failed"* ChatGPT--Kaggriculture
git rm -rq --cached ChatGPT--Kaggriculture 2>/dev/null || true
git rm -rq candidates/gen candidates/gen_h 2>/dev/null || true
git rm -rq --cached candidates/__pycache__ 2>/dev/null || true
git rm -q kaggriculture.zip kag-v2-candidate-generator-WIP.zip "Chatgpt Agents/kaggriculture_blended_efficiency_agents.zip" "Chatgpt Agents/kaggriculture_efficiency_agents.zip" 2>/dev/null || true
rm -f ./de*.log ./err*.log

# 2. superseded agents (v6–v11 lineage, external agent batches)
mv_ archive/agents main_v8.3.py main_v9.1_buyfeed_herd.py main_v9.2_parallel_build.py main_v9.3_fertilize.py main_v9.10_hire_calibrated.py \
    main_v10.5_siting.py main_v10.6_radius3.py main_v10.6a_radius3.py main_v_clonereplica1.py labor_02_eight_hand_cap.py
git mv -k "Archived versions" archive/agents/v6-v10 2>/dev/null || true
git mv -k "Chatgpt Agents" archive/agents/chatgpt 2>/dev/null || true
git mv -k "Perplexity Agents" archive/agents/perplexity 2>/dev/null || true
git mv -k "User Notebooks" archive/notebooks 2>/dev/null || true

# 3. candidate variants that were tested and rejected (kept for provenance, out of the working list)
mv_ archive/candidates candidates/H5.py candidates/H8.py candidates/H10b.py candidates/H10w05.py candidates/H10w05n.py candidates/H10w05s.py \
    candidates/H10w07.py candidates/H10w10.py candidates/H10w10h0.py candidates/H10w10s.py candidates/H11_s12.py candidates/H11_s15.py \
    candidates/H11_s20.py candidates/H11_s30.py candidates/H11g.py candidates/H11gc.py candidates/H11gc_m800.py candidates/H11gc_nomoney.py \
    candidates/H12_s15.py candidates/H12_s20.py candidates/H30_atakan.py candidates/H30_icelemon.py candidates/H30_yuan.py
mv_ archive/candidates/rounds candidates/round*.json candidates/variants_round*.json

# 4. one-off analysis scripts and their outputs
mv_ archive/scripts analyze2.py analyze_replays.py v811_h2h.py fleet_census.py fert_diag.py fert_trace.py census_movement.py decompose.py \
    smoke_gate.py smoke_test.py search.py search_hybrid.py make_hybrid.py
mv_ archive/experiments experiments artifacts replay_evidence
mv_ archive/notes hr_trace.txt hr_trace2.txt v813_30seed_results.txt ep_to_ver.json kaggriculture_strategy_item_counts.xlsx \
    kaggriculture-agent-design.md kaggriculture-self-improving-agent-spec.md kaggriculture-strategy-summary.md \
    kaggriculture-v10-fresh-rethink-report.md kaggriculture-v9-adaptive-directional-test.md kaggriculture-v9.1-buyfeed-herd.md \
    kaggriculture_20_strategies.md kaggriculture_opponent_strategy_identifiers.md KAGGRICULTURE_CLOUD_SETUP.md

# 5. daily reports live under docs
git mv -k Reports docs/reports 2>/dev/null || true

# 6. keep generated things out from now on
cat >> .gitignore <<'EOF'

# generated candidates / scratch logs
candidates/gen/
candidates/gen_h/
candidates/__pycache__/
*.log
EOF

echo "done — review with: git status --short | less   then: git commit -m 'Tidy repo: archive superseded agents, candidates, scripts' && git push"
