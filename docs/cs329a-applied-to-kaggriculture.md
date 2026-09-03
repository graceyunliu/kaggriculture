# CS329A (Self-Improving AI Agents) applied to Kaggriculture

A structural reading of Stanford's CS329A syllabus against this project's history: what the course's frameworks say about how we've been working, where the theory says the losses are coming from, and what a course-shaped program would look like. Grounded in the repo (`main_v10.6_radius3.py`, `seeded_h2h.py`, the v10 rethink report, the V3.x forensics, the unbuilt self-improving-agent spec) and the course reading list.

*Revision 2 (Sep 2): incorporates ChatGPT's review. Corrections adopted: market coupling (not single-player in payoff), ladder rating ≠ local cash, movement share ≠ waste, daily cash ≠ process signal, V3.11 is the frontier, discovery-before-explanation with declared blocks. Pushbacks retained: factorial bundles instead of hand-picked regimes; evaluator throughput budget; local margin vs. the dominant clone remains the authoritative proxy.*

---

## 1. The one fact that reframes everything

Every top ladder opponent we face is a **fixed replay tape** (`opp_scenario_v14`, `opp_frontier_v12`, etc. — 93% of the ladder is one cloned fingerprint). Their *decisions* do not react to us. The engine is in `vendor/`, importable, deterministic given (seed, seat, both agents) — the only stochasticity is weed spawn, and we control the seed.

That means Kaggriculture is a **720-step, fully-simulable optimization problem with an exact, cheap verifier**: run the engine, read the result. There is no generation–verification gap of the kind the course spends two lectures on (Cobbe, Lightman, "weak verifiers"). We have the strongest possible verifier and have been using it only to adjudicate a handful of human-authored hypotheses at a time.

Two qualifications (from ChatGPT's review, both correct). First, it is not *single-player in payoff*: market inventories and prices are shared, so our sales move the prices the opponent's tape sells into, its terminal cash is not fixed, and seat matters. The objective is therefore **margin against the real tapes in a shared market, both seats** — not absolute cash, and not self-play against a parent. The verifier is still exact; the objective is relational. Second, local terminal cash is an exact verifier for a *match* but only a proxy for *ladder rating* (the V2.7 analysis showed rating can't be reconstructed from local cash/W-L). Since 93% of the ladder is one fingerprint, margin vs. that clone is about as good a proxy as exists, but held-out and ladder budget should go only to robust frontier winners.

Nearly every course lecture is about what to do when you have a verifier that's better than your generator. The answer, in every lecture, is the same: **generate far more candidates and let the verifier choose.** We have not done that. That is the central diagnosis.

---

## 2. Lecture-by-lecture mapping

### Lecture 2 — Test-time compute scaling (Large Language Monkeys; Snell et al.; Archon)

The core empirical law: with a verifier available, coverage (probability *at least one* sample is correct) grows roughly log-linearly with the number of samples, and this beats improving the generator for a fixed budget.

Our history is a sample-starved version of this. Across all rounds we generated ~60 candidates at roughly 3–5 per human session, and ~3 were wins (v8.3, v10.5, v10.6). A ~5% hit rate with a perfect verifier is not a failure of ideas; it's a signal that the generator (a human, or an LLM directed by a human) is fine and the *sample count* is two orders of magnitude too low. Monkeys-style scaling says 1,000 candidates at 5% would yield ~50 wins, some of them compounding.

Archon's contribution is that inference-time techniques (sample → filter → rank → fuse) should themselves be *searched over*, not hand-designed. Our pipeline is hand-designed and fixed: one hypothesis, 20 games, verdict.

**What this implies:** the bottleneck to attack first is *evaluations per hour*, not hypothesis quality. Everything downstream depends on it.

### Lecture 3 — Robust verification (outcome vs. process reward models)

Lightman's "Let's Verify Step by Step" result: a process-reward signal (score each step) beats an outcome-reward signal (score only the final answer) for credit assignment on long-horizon problems.

Every one of our ~60 verdicts was outcome-only: mean final-money margin over 10 seeds. That tells us *whether* a change lost, never *where in the 30 days* it lost or *which hand* lost it. The one time the project used a process-level metric — labor per obligation (6.6 vs 11.3 unit-turns per animal-day, V3.8 forensics) — it produced the single most informative finding in the whole history, and led directly to the +$50k V3.9 rebuild.

We also have a free process reward we've never fully exploited: the opponent's tape gives a per-day trajectory for the same seed. But *daily cash alone is misleading* — low cash on day 8 is either productive investment or economic failure. The per-day quantity to diff is **net worth**: cash + capital committed to land/animals/workers/seeds/feed + output awaiting deposit + output awaiting sale + the production pipeline, alongside missed deadlines and deaths. Per-hand utilization and obligation latency localize the gap in space.

**What this implies:** instrument the evaluator to emit a per-day, per-hand trace, and diff every candidate against both the champion and the opponent tape *at day granularity*. A rejection should read "lost from days 7–11 because worker capacity lagged animal obligations; deposit latency then delayed rehiring," not "lost by $8,401."

### Lecture 4 — Learning from feedback with tools/code (ReAct; RLEF; Constitutional AI)

RLEF's thesis: a code agent should be trained on *execution feedback* over many iterations, not judged once. Constitutional AI's thesis: a written set of principles can replace the human in the critique loop.

We already have the constitution: `AGENT_LEARNINGS`-style rules, engine-verified invariants (no starvation, hand reset, budget never negative), and a long list of things known not to work (goose, tomato scale-up, radius > 4, capital-timing changes, ...). What we lack is the *loop that uses it without a human in the middle*. The `kaggriculture-self-improving-agent-spec.md` describes exactly this loop and was never built. The `kag-v2-candidate-generator-WIP.zip` is a second attempt, also unfinished.

**What this implies:** the spec was right; it was deprioritized in favor of more hand-authored hypotheses, which is the opposite of what the course teaches.

### Lecture 5 — Multi-step reasoning and planning (LATS; ADaPT; adaptive branching tree search)

This is where the engineering gap is largest and most concrete.

`assign_tasks()` is a **greedy one-step matcher**: each turn, rebuild the task pool from perception, do nearest-pair matching per tier, emit one step per unit. Its own docstring says: "no cross-turn memory — task lists are still rebuilt from perception every turn." Four independent confirmations show it's the load-bearing piece of the codebase, and that any fragmentation of it loses.

LATS's thesis: when you have an environment you can roll out, use tree search at decision time rather than a reactive policy. ADaPT's thesis: decompose adaptively — plan at the level where planning is cheap (the day), execute reactively at the level where it's not (the hour).

The structural gap: this is a **multi-vehicle routing problem with time windows** (10 hands, respawn at the shed each morning, revisit obligations with deadlines, travel cost dominating). Greedy nearest-neighbor is known to be far from optimal on that class. The v10.5 siting win (+$9–13k) was the one hypothesis that touched routing, and it was the largest win in the v10 lineage — while never changing the greedy dispatcher itself.

A correction to the first draft of this document: **raw movement share (58–60%) is not evidence of waste.** v10.6 beat v9.3 while making 1,662 *more* moves; the winning tapes also move more than V3.11. Productive agents move more because they employ more hands and complete more work. The metric that actually indicts execution is **travel per completed obligation** — which is what the V3.8 forensics measured (6.6 vs 11.3 unit-turns per animal-day, winners vs. V3.4) and why that was the one finding that led to a +$50k rebuild. The right process metrics are travel per obligation, obligation latency (creation → completion), empty travel, reversal/re-crossing frequency, and value per worker-turn.

**What this implies:** routing is a *candidate* for the dominant remaining cause, not a proven one. The course-shaped way to find out is cheap and ordered: (1) measure obligation latency and avoidable travel on V3.11 vs. the tapes; (2) build a *shadow* planner that proposes daily assignments without controlling actions; (3) compute an oracle/optimistic upper bound on what perfect scheduling of the same obligations would recover; (4) only if that bound is material, search schedules offline using copied engine states; (5) distill the winning schedule patterns into a policy fast enough for the per-turn action limit. Tree search never goes inside the submitted agent.

### Lecture 6 — Train-time scaling / RL (STaR; DeepSeekMath GRPO; DAPO)

STaR's mechanism: run the model, keep the trajectories that succeed, train on them, repeat. It is the simplest self-improvement loop and it works because the verifier filters.

We did a manual STaR step exactly once: the V3.9 from-scratch rebuild kept the mechanisms that worked (demand-coupled sizing), dropped what didn't, and gained +$50k. We never iterated it.

A cheaper, lower-risk instance: v10.6 has ~30 tunable constants (`NEAR_SHED_RADIUS`, fleet caps, seed targets, sell floors, hire thresholds). The radius sweep (4→3, +$7.3k) was a one-dimensional coordinate descent done by hand. Evolution strategies / CMA-ES over the whole constant vector, with 10-seed both-seats as fitness, is standard, requires no LLM, and would have found the radius result plus every interaction the hand sweep missed.

**What this implies:** parameter search is the fastest proof that the automated loop works before trusting it with code edits.

### Lecture 7 — Open-ended evolution (ADAS; AI Scientist; AlphaEvolve)

This is the lecture that matches our problem shape exactly. AlphaEvolve: an LLM proposes diffs to marked regions of a program, an automated evaluator scores each variant, and a *population database* (not a single champion) drives what gets mutated next. It found improvements to matrix-multiplication algorithms and data-center schedulers that decades of expert hill-climbing missed — the same "we're at a local optimum" story our report tells three times.

Two structural differences from what we've done:

*Population vs. single champion.* Rounds 3–11 all mutated v10.6. The report says "local optimum" repeatedly and then keeps climbing the same hill. Meanwhile, V3.9 (built from scratch) beat V3.4 by +$50k — direct evidence that different basins exist and that our lineage was sitting in a shallow one. AlphaEvolve's island model keeps several lineages alive precisely so the search can cross basins.

*Throughput.* AlphaEvolve runs thousands of evaluations; we ran ~60 over a month. Same loop, three orders of magnitude apart.

**What this implies:** the candidate generator isn't the hard part; the evaluator-as-a-service and the population store are. Build those, then plug in the LLM.

### Lecture 8 — Self-improvement with search (AlphaCode; AlphaCode 2)

AlphaCode's pipeline: sample millions of programs, filter by cheap tests, cluster by behavior, submit representatives. The insight for us is the **cascade**: a 2-seed screen kills most candidates in seconds; only survivors get 10 seeds; only finalists get the full opponent pool. The Hamburger notebook's two-stage gate (already in the spec) is this idea. We've been running every hypothesis at full cost.

Clustering by behavior also matters: several of our "rejections" were exact no-ops (v10.21 goose, v10.2 shop-relief, two of the ChatGPT agents were byte-identical to their parent). A behavioral fingerprint (per-day money trace) detects a no-op in one game instead of twenty.

### Lecture 13 — Agentic frameworks for software engineering (CodeMonkeys; KernelBench; LLM optimizers with agent–system interfaces)

The "agent–system interface" paper's point: LLM optimizers work when the program exposes a *narrow, well-described mutation surface* (marked blocks, a clear performance signal, a fast harness). A 2,085-line monolith with global mutable state (`animal_plans`, `reserved_sites`, `timing_engine`) is a hostile mutation surface — one reason the externally-supplied v11 candidates and the ChatGPT agents came back broken or no-op. The WIP candidate-generator's modular layout (`planning/`, `economics/`, `state/`) was the right instinct.

### Lecture 14 — Memory (MemGPT; Cartridges)

Two levels. *In-game*: the agent has no memory — task lists rebuild from perception each turn. A planner needs state that persists across hours (today's route, committed obligations). *Across experiments*: the learnings store exists as prose in memory files and reports; it isn't machine-readable, so an automated generator can't consult it and will re-propose goose.

### Lecture 17 — Agentic evaluation and long-horizon tasks (METR)

METR's finding: long-horizon task success is dominated by compounding small errors, not by any single decision. Our 720-turn horizon fits. This is another argument that the gap lives in per-turn execution efficiency (compounding) rather than in the handful of capital-allocation decisions (a dozen discrete choices) that 50 of our 60 hypotheses targeted.

What we got right on evaluation, and should keep: the both-seats discovery (a real ~$2.7k seat bias that would have corrupted every verdict), the insistence on the real-opponent pool rather than self-play, the engine-source grounding, and the invariants.

---

## 3. Theories about what we've been doing wrong

Ranked by how much of the $40–70k gap each plausibly explains.

**Theory 1 — We've been optimizing the wrong layer.** Roughly 50 of 60 hypotheses changed *what to buy and when* (land timing, herd size, crop mix, hiring, sell rhythm). The forensics say the winners' edge is *labor per obligation* — half ours — and the clone-replica experiment (Round 10) proved it directly: porting the opponent's entire allocation playbook onto our dispatcher *lost* by $68k. The allocation layer is low-dimensional and exhausted; the execution layer (routing 10 hands over 720 turns) is high-dimensional and touched once (v10.5), which produced the biggest win. The course's planning lecture is about exactly this layer.

**Theory 2 — Sample-starved search with a perfect verifier.** ~60 evaluations in a month, human-gated. Every course lecture says the right response to a strong verifier is volume. We had the spec for the loop and didn't build it.

**Theory 3 — Greedy, memoryless control in a simulable world.** The dispatcher plans one step ahead in a domain where a day of lookahead is cheap and exact. Nothing tested has been a *planner*; everything has been a *heuristic reorder*. Evidence for this being the dominant cause is suggestive (labor-per-obligation gap), not proven — the oracle-bound experiment in §2/Lecture 5 is how to settle it.

**Theory 4 — Single-lineage hill-climbing into a local optimum, and candidates measured against obsolete parents.** Every round since v10.5 mutated the same champion. The report says "local optimum" and keeps climbing. V3.9's from-scratch +$50k shows other basins exist. And the V3.12 case — 27–5 vs. its V3.4 parent, 0–32 vs. the actual V3.11 champion — shows that beating a parent proves nothing about the frontier. Note also that the frontier is **V3.11**, not v10.6: V3.10 beat the opp_v14 clone by +$22.7k where v10.6 loses to it by $40–70k. The v10 lineage is an archive island.

**Theory 4b — Wrong granularity, in both directions.** Isolated one-mechanism tests rejected pieces of coupled lifecycles (the v14 DROP work: DROP, trip admission, arbitration, inventory projection, and selling are one system; fragments lose because the surrounding architecture is missing). But hand-authored coherent bundles also lose decisively (v11a–d 0/40, clone-replica −$68k, tile agents 0/30). Bundle hit rate ≈ 3/10 (V3.9, V3.10, V3.11 won); atom hit rate ≈ 3/50. Bundles are better per draw, but neither is good enough for a human to pick which five to try. The resolution is *declared blocks + a fast evaluator + automatic ablation of winners* — discovery first, explanation after.

**Theory 5 — Outcome-only reward, no credit assignment.** Verdicts, not diagnoses. The one process-level metric we computed was the most valuable thing we learned.

**Theory 6 — We cloned the opponent's decisions instead of learning from its trajectories.** Round 10 copied *what* the opponent bought. STaR/SWiRL-style learning would use the 440 replay tapes as expert trajectories and extract *how* it executes: per-hand paths, revisit cadence, batching (alternate-day watering, 7-unit wheat pickups, fertilize-from-carry — the V3.8 forensics found these by hand; a script could find all of them).

**Theory 7 — Evaluation too slow to iterate.** 20 games per verdict, serial, human-triggered. No cascade, no parallelism, no behavioral-fingerprint early exit. This is the reason Theory 2 exists.

---

## 4. Evaluation of the current candidate-finding process

How it has actually worked: someone (Grace, Claude, ChatGPT, Perplexity, DeepSeek) proposes a hypothesis with a narrative rationale, almost always about capital allocation. It is implemented as a full copy of the champion with an edit, sometimes several bundled. It runs through `seeded_h2h.py --both-seats`, 10 seeds, 20 games, serially, against the champion and sometimes one tape. Verdict is a mean margin and a t-stat. Win → new champion; loss → a paragraph in a report; the candidate is discarded whole. Each round is gated on a human reading the last result before writing the next.

What is wrong with it, by the course's standards: the generator is one mind's model of the game, so draws are correlated (33 straight rejections in rounds 7–11 were mostly one hypothesis in different clothes); externally-authored whole agents had no mutation surface and came back as crashes or byte-identical no-ops; bundles without declared blocks destroy credit assignment and atoms without a fast evaluator miss interactions; every candidate pays full price (five known no-ops cost ~100 games to confirm nothing changed); the verdict is a scalar; there is no archive, so recombination (v10.5 siting × V3.9 sizing → V3.10, +$8k) happens only when a human does it by hand; and candidates have been measured against parents rather than the frontier.

What is right and must be kept: both-seats, engine-source grounding, the real-tape opponent pool, the invariants, the promotion threshold. The verifier is sound; everything wrong is upstream of it.

---

## 5. The merged program

Synthesized from the first draft of this document and ChatGPT's review. Ordered by dependency; each stage is useful alone.

**Stage 0 — Evaluator as a service, with a throughput budget.** Cached (code hash × seed × seat × opponent), parallel, versioned (engine and package hashes in every result), and *cascaded*:

1. Static: compiles, self-contained, no protected-source edits, semantic-diff/provenance check, no exact-copy or wrapper substitution.
2. Fingerprint: one game, seed 1, per-day trace vs. champion — identical trace = no-op or duplicate, discard in seconds.
3. Smoke: 2–4 seeds both seats; crash, illegal action, catastrophic regression.
4. Development suite: dev seeds, both seats, current champion + selected tapes, process traces; sequential halving rather than "one seed decides."
5. Full validation: all prescribed seeds, multiple opponent regimes, determinism rerun.
6. Held-out: finalists only, never tuned against.

**The frontier opponent is V3.11**, mandatory at stage 4 and up. Beating a parent promotes nothing. The evaluator's own throughput is its first reported metric: target median candidate ≤ 4 games, promotion candidate ≤ 40, hundreds of verdicts per night. If the matrix as specified pushes verdicts past that, cut stages, not throughput — an evaluator too expensive to run hundreds of times a night re-creates the starvation this whole program exists to fix.

**Stage 1 — Process traces.** Every game emits a trajectory vector: net worth by day (cash + committed capital + inventory awaiting deposit/sale + pipeline), worker count and worker-turn utilization, productive actions by domain, travel per completed obligation, obligation latency, empty travel, missed watering/feed/care deadlines, animal deaths, deposit latency, sale latency, market-slot utilization, shed pressure. Every verdict includes first divergence day and metric vs. champion and vs. tape.

**Stage 2 — Machine-readable experiment memory.** Per experiment: changed blocks, parent hash, behavioral fingerprint, contexts tested, results, first divergence, process-level cause, known interactions, and whether the rejection is *architecture-local* or *universal* ("new return trips ahead of V3.4 maintenance" is rejected; "DROP is useless" is not; "fertilizer-first arbitration in v10.6" is rejected; "deadline-aware scheduling everywhere" is not). Generators must query this before proposing.

**Stage 3 — Typed mutation blocks.** Expose the agent as declared regions: opening regime, capital proposal generation, worker-floor policy, animal acquisition cadence, crop/task admission, task arbitration, deposit lifecycle, market liquidation, land expansion, spatial assignment, plus the constant vector. A candidate may change any number of blocks but must declare which. This is what makes external generators reliable and crossover possible.

**Stage 4 — Generator portfolio.** Decorrelated sources, all feeding the same queue:

- *Constant perturbation* (CMA-ES / Gaussian ES over the vector). No LLM. Runs first; proves the pipeline end to end.
- *Factorial bundles over a human-declared axis set.* Not five hand-picked regimes — the full design. First run: {worker floor} × {produced-wheat feed} × {staged herd cadence} × {deposit-latency control} × {mixed-inventory liquidation} on V3.11 → 32 candidates, a few hundred games under the cascade.
- *LLM block mutation* conditioned on engine source for the block, the structured memory, and the champion-vs-tape trace diff (AlphaEvolve's shape).
- *Crossover* between archive members, block-wise.
- *Replay imitation*: parse the 440 tapes into per-hand action streams, extract routing/batching/cadence statistics, convert into admission and arbitration constraints.
- *Human hypotheses*, welcome, same queue, no priority.

**Stage 5 — Population with islands.** Archive the top ~20 by paired win rate, opponent-relative margin, seat/seed robustness, process efficiency, and behavioral novelty — bucketed so a slightly weaker but behaviorally distinct candidate survives as a parent. Islands: V3.11-derived, V3.4/v10.6 integrated, replay-imitation, scheduling/planning, novel architecture. Promotion to ladder still requires the full stage 5–6 gate; the archive is for generation, not submission.

**Stage 6 — Automatic ablation of winners.** Discovery first, explanation after. When a bundle wins robustly, the evaluator runs the factorial ablation (remove produced wheat; remove worker floor; revert DROP admission; revert deposit-aware selling; revert cadence) and records which components are necessary, interacting, or incidental. This is the *only* place one-mechanism tests belong.

**Stage 7 — Planning, gated by an oracle bound.** Measure obligation latency and avoidable travel on V3.11 (Stage 1 gives this for free). Build a shadow planner that proposes daily assignments without acting. Compute an optimistic upper bound on what perfect scheduling of the same obligations recovers. If material, search schedules offline on copied engine states and distill the patterns into a policy within the per-turn time limit. Never tree search inside the submitted agent.

**Human role, restated.** Define block boundaries and factorial axes. Read divergence traces and write memory rules. Decide which lever to open next. Not: author the 61st single-variable hypothesis and wait for its verdict.

**What the first two runs predict.** If constants-only ES on V3.11 finds a few thousand per game overnight, sample starvation is confirmed at the parameter layer. If the labor/feed/cadence/liquidation factorial finds a robust bundle, the coupled-lifecycle theory is confirmed and ablation tells us why. If both come back flat after a few hundred candidates, that is clean evidence the remaining gap is structural — and the oracle-bound experiment decides whether it's routing. Any of those outcomes is more informative than the next five hand-written hypotheses.

---

## 6. Where the course doesn't apply

The course's verifier lectures (learned PRMs, weak-verifier ensembles) are solutions to a problem we don't have — our verifier is exact. A learned value function is useful here only as a *fast proxy* inside the in-game planner, never as the final judge. Likewise, the memory-serving lectures (CacheBlend, KV-cache tricks) are about LLM inference cost and have no analogue. The RL-at-scale lectures (DAPO, GRPO) are about training LLMs; the relevant transferable idea is only the loop shape, not the algorithms.

---

## 7. Reading order

Lecture 7 (AlphaEvolve blog + ADAS) first — it's the closest match to the problem and the shortest path to a working loop. Then Lecture 5 (LATS, ADaPT) for the planner. Then Lecture 2 (Monkeys, Snell) for the scaling argument and Lecture 3 (Lightman) for process reward. Lectures are on the YouTube playlist; papers are linked from the course schedule.

Course site: https://cs329a.stanford.edu/ · Playlist: https://www.youtube.com/playlist?list=PLangBM27OtEA
