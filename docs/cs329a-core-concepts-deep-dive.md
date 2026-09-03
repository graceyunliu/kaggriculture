# CS329A core concepts — a deep dive, with the Kaggriculture analog for each

Companion to `cs329a-applied-to-kaggriculture.md`. That document maps the syllabus onto our history and proposes a program. This one goes underneath: for each core concept, what the mechanism actually is, what the evidence in the assigned papers shows, how it translates to a deterministic farm simulator, and the trap that makes the translation fail if you're careless.

Cross-cutting vocabulary first, because every lecture uses it.

---

## 0. Four ideas that run through the whole course

**Coverage vs. precision.** Coverage is the probability that *at least one* of k samples is correct (pass@k). Precision is the probability that the sample you *select* is correct. Generating many candidates raises coverage; a verifier converts coverage into precision. Without a verifier, extra samples are useless past a point — majority voting saturates. With one, coverage is the ceiling and the verifier determines how close you get to it.

**The generation–verification gap.** How much easier it is to check an answer than to produce it. Large gap → sample-and-verify dominates. Zero gap → nothing beats a better generator. The course is a study of domains with a large gap: math (check the number), code (run the tests), games (play it out). Kaggriculture's gap is as large as it gets *at the level of a whole agent* (run 20 games) and small *at the level of a single in-game action* (you can't roll out 720 turns per decision inside a one-second limit). Keep those two levels separate; most of our confusion has come from blurring them.

**Credit assignment.** When a long sequence of decisions produces one outcome, which decisions caused it? Outcome reward gives one bit for 720 turns. Process reward gives a signal per step. Every lecture on verification, planning, and RL is partly about buying better credit assignment.

**Exploration vs. exploitation.** Refine the best thing you have (deeper) or try something new (wider). Hill-climbing is pure exploitation; it converges to whatever local optimum the starting point sits in. Every population, island, novelty, and adaptive-branching idea in the course is a mechanism for controlling this trade-off explicitly instead of defaulting to exploitation.

---

## 1. Test-time compute scaling

### Mechanism

Hold the model fixed. Spend more compute *at inference* — more samples, longer search, iterative revision — and measure how quality scales with that compute. The surprising empirical fact is that it scales predictably, and often better per dollar than making the model bigger.

### Evidence

*Large Language Monkeys* (Brown et al. 2024). Sample a fixed model k times and measure coverage. Across five orders of magnitude in k, coverage rises roughly log-linearly, and the relationship is stable enough to fit and extrapolate. Concrete: a code model that solved ~16% of SWE-bench Lite with one attempt solved ~56% with 250 attempts. The catch, which the paper is careful about: those gains are *coverage*. Where a real verifier exists (unit tests), you keep the whole curve. Where it doesn't (majority vote on math), the achievable precision flattens after a few dozen samples while coverage keeps climbing. The gap between the two curves is the value of a verifier, measured directly.

*Scaling test-time compute optimally* (Snell et al. 2024). Two ways to spend inference compute: parallel search against a scorer (best-of-N, beam search, lookahead), and sequential revision (the model edits its own previous attempt). Which is better depends on problem difficulty: for easy problems, sequential revision wins — the first attempt is roughly right and needs polishing; for hard problems, wide parallel search wins — you need to land in a different region entirely. Allocating compute per-difficulty ("compute-optimal") is ~4× more efficient than naive best-of-N, and on easy/medium problems a small model with a compute-optimal test-time budget beats a model 14× larger.

*How do monkeys get their power laws?* (Schaeffer et al. 2025). Why log-linear? Because per-problem success probability is heavy-tailed: most problems are either easy (p near 1) or impossible (p near 0), and the aggregate curve is dominated by the minority of problems with small-but-nonzero p. Sampling only helps on those. It never helps where p = 0.

*Archon* (Saad-Falcon et al. 2024). The inference-time pipeline itself — how many samples, which ensembling, fusion, ranking, and verification layers, in what order — is a design space that can be searched automatically like hyperparameters. Hand-designed pipelines are reliably beaten by searched ones.

### Kaggriculture analog

A "sample" is a candidate agent. The verifier is 20 games. Our history is the k = 60 point on a coverage curve we never extended.

Snell's difficulty split maps cleanly onto our two layers. Tuning constants on a fixed architecture is an *easy* problem — the current point is roughly right, so sequential revision (evolution strategies, hill-climb on the vector) is compute-optimal. Finding a new architecture is a *hard* problem — the answer is in a different basin, so wide parallel search (a population, many islands, factorial bundles) is compute-optimal. We've been applying sequential revision (mutate the champion) to the hard problem.

Schaeffer's heavy tail explains the rejection record better than "we ran out of ideas." Some mutation directions have p = 0 (goose: closed three ways; more crop coverage: closed four ways). Sampling more of those is waste, which is why the structured memory matters — it's how the generator learns which directions have p = 0. Other directions have small-but-nonzero p, and *those* are where volume pays.

Archon's point is that our evaluation pipeline (one hypothesis → 20 games → verdict) is itself an unsearched design. Cascade depth, seeds per stage, which opponents at which stage, how to combine margin and robustness into a selection score — these should be tuned against the evaluator's own throughput and false-reject rate, not fixed by convention.

### The trap

Volume is worthless where p = 0, and hand-generated candidates cluster in a few directions. If the generator keeps drawing from the same region, k = 1,000 is not 1,000 independent samples. Decorrelate the generator before scaling it.

---

## 2. Verification: outcome reward, process reward, and where the labels come from

### Mechanism

A verifier scores candidates so you can select from many. An **outcome reward model** (ORM) scores the final answer. A **process reward model** (PRM) scores each intermediate step. Credit assignment is the whole difference: with an ORM a 20-step solution wrong at step 7 is just "wrong"; with a PRM steps 1–6 get credit and step 7 gets blame, so the selector can prefer solutions that are correct *for the right reasons* and the search can prune at step 7 instead of step 20.

### Evidence

*Training verifiers* (Cobbe et al. 2021). On grade-school math, train a verifier to score sampled solutions, then pick best-of-100. The verifier approach scales better with data than fine-tuning the generator, and a 6B model with a verifier matches a 175B model without one. First clean demonstration that verifier + samples beats a bigger generator.

*Let's Verify Step by Step* (Lightman et al. 2023). On competition math, an ORM and a PRM trained with the same base model. PRM-selected best-of-N reaches 78% on a MATH subset vs. ~72% for the ORM and ~70% for majority vote, and the PRM's advantage *grows* with N — at 1,860 samples the ORM has plateaued and the PRM hasn't. Step-level supervision is both more accurate and more sample-efficient at test time. Cost: 800,000 human step labels.

*Math-Shepherd* (Wang et al. 2023). Remove the humans. Label a step by rolling out from it: from this partial solution, sample completions; the step's score is the fraction that reach the correct final answer. This is a Monte Carlo value estimate of an intermediate state, and it recovers most of the PRM's benefit with zero human labels.

*Shrinking the generation–verification gap with weak verifiers* (2025). When no ground truth exists, combine many weak, noisy verifiers (LM judges, reward models) with weak-supervision methods to estimate each one's reliability and weight them. Approaches a strong verifier's selection accuracy at a fraction of the cost.

### Kaggriculture analog

The hierarchy of verifiers, from strongest to weakest, and what each one is *for* here:

*Exact* — the engine, 10 seeds, both seats, vs. V3.11 and the tapes. This is our final judge. It is better than anything in the course's papers and needs no learning. Weak-verifier ensembles are solving a problem we don't have at this level.

*Rollout-based (Math-Shepherd)* — the value of a game state on day d is what a fixed policy earns by playing it out to day 30. This is computable exactly, per state, offline. It gives us the process reward we've never had: run the champion and a candidate on the same seed, and at each day where their states differ, roll both forward with the same policy. The day where the value curves diverge is the day the candidate's decision mattered. This is credit assignment at day granularity, from rollouts, with no labels. It is also the thing we'd need to guide any in-game lookahead, because a full 720-turn rollout per action is too slow — a value estimate at the day boundary is not.

*Learned proxy* — a small model trained on (state features → rollout value) so the in-game planner can score candidate day-plans in milliseconds. Useful only inside the agent; never as the final judge.

*Weak signals* — the process metrics (travel per obligation, latency, deposit lag). Individually noisy, collectively diagnostic. Their job is not selection but *explanation* — telling the generator where the loss happened.

### The trap

Optimizing a proxy. If the selector ever uses a process metric as the objective rather than the engine's outcome, the search will find agents that minimize travel-per-obligation by not taking on obligations. Process signals go to the generator (as diagnosis) and the archive (as behavioral descriptors), never to promotion.

---

## 3. Learning from feedback with tools and code

### Mechanism

Close the loop between an agent's output and the world's response, and make the agent *condition on* that response. The ladder: single-shot (generate, done) → ReAct (generate, act, observe, generate again) → RLEF (train the policy so that it gets *better at using* the observations across turns) → Constitutional AI (replace the human critic with a written set of principles applied by a model).

### Evidence

*ReAct* (Yao et al. 2022). Interleave reasoning traces with actions and observations. On knowledge tasks it cuts hallucination because claims get grounded in retrieved facts; on interactive tasks it beats both pure-reasoning and pure-acting baselines. The key property is that reasoning is *conditioned on observations*, not done up front.

*RLEF* (Gehring et al. 2024). Code generation where the model sees test results and gets more attempts, trained with RL so the reward depends on the final attempt. On competition programming it cuts the number of samples needed for a given solve rate by roughly an order of magnitude — the model learns to actually *read* the execution feedback and fix the specific failure, instead of resampling from scratch.

*Constitutional AI* (Bai et al. 2022). A list of written principles; the model critiques its own output against them and revises; the revised outputs train the next model; preference labels for RL come from a model applying the principles rather than from humans. The result matches human-feedback training on harmlessness with far fewer human labels.

### Kaggriculture analog

We have run ReAct with a human as the model: propose, run, read the number, propose again. The RLEF lesson is that the *next proposal should be conditioned on the diagnosis of the last one*, specifically — not on a scalar. "Lost by $8,401" gives the generator nothing to condition on. "Lost from day 7 to 11 because worker capacity lagged animal obligations, then deposit latency delayed rehiring" is an execution trace the generator can act on. RLEF's order-of-magnitude sample efficiency came from exactly this — reading the failure, not resampling.

Constitutional AI is the structured memory. Our "constitution" already exists as prose: engine-verified invariants, closed directions, architecture-local vs. universal rejections. Making it machine-readable and putting it in the generator's context is the difference between a critic that remembers and one that re-proposes goose.

### The trap

Feedback that isn't specific enough to condition on. If the trace can't localize the failure to a day range and a mechanism, the generator is back to sampling blind, and the loop degenerates to Monkeys-style volume without the decorrelation.

---

## 4. Multi-step reasoning, planning, and search

### Mechanism

A reactive policy maps state → action. A planner considers sequences of actions, evaluates where they lead, and picks the first action of the best sequence. When a simulator exists, "evaluates where they lead" can be exact rollouts; when it doesn't, it's a learned value estimate. Tree search organizes this: expand promising branches, estimate their value, back the estimates up, and allocate more expansion to branches that look good (MCTS's exploration–exploitation rule).

### Evidence

*LATS* (Zhou et al. 2023). MCTS where the LM proposes actions, the environment returns observations, the LM (or the environment) scores states, values are backed up the tree, and failed trajectories generate reflections that are stored and fed to later expansions. Beats ReAct and reflection-only baselines on QA, web shopping, and code. The two ingredients that matter: *real environment feedback in the tree* (not imagined outcomes), and *memory of failures* across branches.

*ADaPT* (Prasad et al. 2024). Don't decompose up front. Try to execute the task; if execution fails, decompose it into subtasks and recurse. Planning depth adapts to task difficulty and executor capability, so easy tasks don't pay a planning tax and hard tasks get as much decomposition as they need.

*SWiRL* (2025). Generate multi-step tool-use trajectories synthetically, filter them by a process judge, then train step-wise with RL. Improvements transfer across tasks — the model learns *how to plan and use tools*, not just the specific task.

*SPRINT* (2025). Interleave planning with parallel execution of independent sub-steps. The planner identifies which steps don't depend on each other and dispatches them together.

*Wider or deeper?* (Adaptive branching MCTS, 2025). At each node, choose between generating a new sibling (explore wider) and refining an existing child (go deeper), using a Bayesian estimate of which is more likely to improve the best-so-far. Beats fixed-width and fixed-depth search on the same budget.

### Kaggriculture analog

Two different applications, and they should not be confused.

*In-game planning.* `assign_tasks()` is reactive: state → one step per hand, no memory, no lookahead. The domain is a multi-vehicle routing problem with time windows and a daily respawn — a class where greedy nearest-neighbor is known to leave a lot on the table. ADaPT gives the right shape: plan at the day boundary (cheap, once per 24 turns, obligations known), execute reactively within the day, and re-plan only when execution diverges from the plan. LATS gives the evaluation: candidate day-plans are scored by rollout, exactly, on a copied engine state. SPRINT gives the dispatch: independent obligations run in parallel across hands. The ADaPT principle also says *measure first* — if an oracle scheduler on the same obligations recovers little, don't pay the planning tax. That's the oracle-bound experiment.

*Search over agents.* The wider-or-deeper question is the population's question too. Mutating the champion again is "deeper"; opening a new island is "wider." Adaptive branching says: estimate, from the recent hit rate on each, which is more likely to improve the frontier, and allocate accordingly. Our history was fixed-depth: always deeper, on one node.

LATS's failure memory is the structured experiment log, again — the same object shows up in three lectures, which is a sign it's load-bearing.

### The trap

Putting search inside the submitted agent before proving it pays. In-game rollouts cost real time under a per-turn limit, and a planner that times out is worse than a greedy one. The course's own pattern — expensive search at train time, distilled cheap policy at test time (§5) — is the safe route.

---

## 5. Train-time scaling: bootstrapping and RL

### Mechanism

Instead of spending compute at inference, spend it once to improve the policy. The simplest form: run the current policy, keep what worked, train on it, repeat (STaR). The general form: RL, where the reward comes from a verifier and the policy is updated toward higher-reward outputs. The course's focus is the *practical* machinery that makes this work at scale — baselines, sampling rules, stability.

### Evidence

*STaR* (Zelikman et al. 2022). Sample rationales; keep those that reach the correct answer; fine-tune on them; repeat. Plus "rationalization": for problems the model got wrong, show it the answer and have it generate a rationale that reaches it, so the training set includes hard cases and the loop doesn't saturate on easy ones. A few iterations match a model 30× larger on reasoning tasks.

*DeepSeekMath / GRPO* (2024). Group Relative Policy Optimization: for each prompt sample a *group* of outputs, compute each one's advantage as its reward minus the group mean, divided by the group's standard deviation. No separate value network. The baseline is "how did the other samples do *on this same prompt*" — which removes prompt-difficulty variance from the signal.

*DAPO* (2025). Four fixes that made large-scale RL work reliably: decoupled clipping to prevent entropy collapse (the policy narrowing onto a few outputs); *dynamic sampling* — drop prompts where every sample in the group succeeds or every sample fails, because they contribute zero gradient; token-level rather than sequence-level loss; and reward shaping for over-long outputs.

### Kaggriculture analog

STaR is the from-scratch rebuild loop, done once by hand (V3.9). The rationalization step has an analog: when a candidate loses, don't just discard it — trace *what would have had to be true* for it to win (which obligation it should have served, which purchase it should have delayed), and feed that as a constraint to the next generation. That's how the loop learns from failures instead of only from successes.

GRPO is our evaluation design, already. Paired seeds, both seats, margin vs. the same opponent on the same seed — that *is* a group-relative baseline, and it's why our verdicts are as clean as they are. The transfer is to keep it: never compare across seeds or seats, always within.

DAPO's dynamic sampling is a direct improvement to the cascade: seeds where every candidate ties the champion carry no information. Track per-seed discrimination over time and allocate evaluation budget to seeds that separate candidates. DAPO's entropy-collapse warning is the population-collapse warning: without a novelty term in selection, the archive converges to variants of one lineage and the search stops being wide.

### The trap

Selection on a noisy verifier at scale finds the verifier's blind spots. Ours is exact, but *seed-limited*: a policy tuned on 10 seeds can fit those 10. Train/dev/held-out seed splits are the STaR-era answer to this and they cost nothing.

---

## 6. Open-ended evolution: search over programs

### Mechanism

Treat the agent's *code* as the thing being optimized. An LLM proposes edits; an evaluator scores the result; a database keeps a population; the next proposal is conditioned on high-scoring ancestors. Diversity is maintained explicitly (islands, behavioral niches) so the population doesn't collapse. Because the evaluator is automated, this runs unattended at scale.

### Evidence

*Automated Design of Agentic Systems* (Hu et al. 2024). A meta-agent writes new agent architectures as code, tests them, and keeps an archive; the archive is in the prompt for the next proposal. Discovered agents beat hand-designed ones and transfer across domains. The insight: the search space "programs" is expressive enough to contain any hand-designed agent, so a search over it can only do at least as well.

*The AI Scientist* (Lu et al. 2024). Full pipeline: idea → experiment code → run → analyze → write paper → automated review. The lessons that matter for us are the failure modes: it needs a sandbox (it once edited its own timeout), an evaluator that can't be gamed, and a review step that catches plausible-looking nonsense.

*AlphaEvolve* (DeepMind 2025). The reference design. Marked regions in a codebase are the mutation surface; an evaluator function returns scores; a two-model ensemble (a fast model for breadth, a stronger one for depth) proposes diffs; a database combining MAP-Elites (niches by behavioral descriptors) with an island model (independent sub-populations, occasional migration) keeps diversity; an *evaluation cascade* kills bad candidates cheaply. Results include a 4×4 complex matrix-multiplication algorithm using 48 scalar multiplications — the first improvement on Strassen's 1969 result in that setting — a Borg scheduling heuristic that recovered ~0.7% of Google's fleet compute, and improvements on ~20% of fifty open math problems. In every case, decades of expert hill-climbing had stalled.

### Kaggriculture analog

This is our loop, at 100–1,000× our throughput. The correspondence is exact: marked regions = typed mutation blocks; evaluator = cascaded engine harness; database = archive with islands; the prompt's ancestor context = structured experiment memory.

The AlphaEvolve results are the strongest available evidence for the "local optimum" hypothesis in our reports. Strassen stood for 56 years not because nobody smart looked, but because hand-search from the known best point doesn't cross basins. Our V3.x-vs-v10.x split is a small instance: two basins, found by two from-scratch efforts, never crossed until a human did it manually.

MAP-Elites deserves emphasis because it's the piece we've never had. Instead of one score, each candidate has a *behavior descriptor* — say (fleet size at day 15, land count, travel per obligation). The archive keeps the best candidate *per descriptor cell*. A candidate that's $10k worse but plays a completely different economy survives in its own cell and stays available as a parent. Without this, selection pressure alone collapses the population to one lineage within a few generations — DAPO's entropy collapse in evolutionary form.

### The trap

Mutation surface too wide (arbitrary edits to a 2,000-line file → crashes and no-ops, which is what the externally-authored agents produced) or too narrow (constants only → can't cross basins). Typed blocks with declared changes is the middle. And the AI Scientist's sandbox lesson applies: the evaluator must be un-gameable — provenance checks, no engine edits, no wrapper substitution.

---

## 7. Search at scale: filter, cluster, rank

### Mechanism

When you can generate far more candidates than you can afford to fully evaluate, build a funnel: cheap filters remove most, behavioral clustering removes duplicates, and expensive evaluation is spent only on cluster representatives.

### Evidence

*AlphaCode* (Li et al. 2022). Millions of program samples per problem. Filter by the example tests in the problem statement — removes ~99%. Cluster the survivors by their outputs on generated inputs, so programs that behave identically are treated as one. Submit representatives from the largest clusters. Result: median-competitor level on Codeforces. *AlphaCode 2* (2023): same funnel on a stronger base, ~a million samples, plus a learned scoring model for the final ranking; 85th percentile.

*Search-o1* (2025). A reasoning model that decides *when* to retrieve during a long chain of reasoning and how to compress what it retrieves, rather than retrieving everything up front.

### Kaggriculture analog

The evaluation cascade is AlphaCode's funnel. Static checks and the one-game fingerprint are the example-test filter. Behavioral clustering is the fingerprint compared across candidates: two candidates with identical per-day traces on seed 1 are the same candidate — evaluate one. This would have caught the five known no-ops at a cost of one game each instead of twenty, and it catches the byte-identical-with-different-header case for free.

The scoring model in AlphaCode 2 is the learned proxy from §2: cheap ranking before expensive evaluation, never instead of it.

### The trap

Filters that are too aggressive discard the small-p candidates that Schaeffer's heavy tail says are the whole point. Calibrate the early stages by their false-reject rate against a sample that was evaluated fully.

---

## 8. Evaluation for long-horizon agents

### Mechanism

An evaluation is a claim about generalization: this agent will do well on games it hasn't seen. The threats are contamination (tuning on the test), non-stationarity (the ladder changes), and horizon (small per-step errors compound over long tasks, so short-task performance doesn't predict long-task performance).

### Evidence

*Measuring AI ability to complete long tasks* (METR 2025). Task success falls off sharply with task length; the length at which an agent succeeds half the time is the useful summary, and it has been doubling roughly every seven months. Long tasks fail from accumulated small errors more than from any single hard step.

*GDPVal* and *DeepScholar-Bench* (2025). Real-world, economically-valued tasks and *live* benchmarks that refresh so they can't be contaminated.

### Kaggriculture analog

Our horizon is 720 turns; METR says the loss accumulates. That is consistent with the gap living in per-turn execution efficiency rather than in a dozen capital decisions — but it's a prior, not proof, which is why the oracle bound comes before the planner.

Contamination is seed-fitting; held-out seeds are our live benchmark. Non-stationarity is the ladder: 93% one fingerprint today, but a real ladder shift (a new dominant clone) would invalidate the tape pool. The `sync_replays.py` pipeline and the fingerprint census are the monitoring for that.

The evaluation finding we already got right — the ~$2.7k seat bias that would have corrupted every verdict — is exactly the kind of thing this lecture is about. It was found by running an agent against itself and noticing it didn't tie. Keep doing that: an agent vs. itself must score zero under any evaluator change.

### The trap

Reading ladder W/L as a verifier. It's a small, noisy, non-stationary sample against a shifting opponent mix. It is where robust winners get *confirmed*, not where candidates get *selected*.

---

## 9. Memory

Briefly, since it's the least novel piece for us. *MemGPT* treats the LM's context as a tier in a memory hierarchy the agent manages itself; *Cartridges* distills a long context into a small trained module. The analogs are the two memories this project keeps failing to build: in-game state that persists across turns (a plan, committed obligations — `assign_tasks` has none), and the cross-experiment memory that the generator consults. Both are load-bearing in three other lectures.

---

## 10. How the concepts fit together

Read as one system rather than nine lectures:

A **generator** proposes candidates. Its quality matters less than its *decorrelation* (§1, §6) and whether it's *conditioned on diagnoses* of prior failures (§3) and a *memory* of closed directions (§3, §9).

A **verifier** selects. Ours is exact at the agent level (§2), so the coverage curve is the ceiling and volume is the lever (§1). At the in-game action level it's not exact, so rollout values and learned proxies fill in (§2, §4) — but only ever for generation and in-game guidance, never for promotion.

A **funnel** makes volume affordable: cheap filters, behavioral dedup, expensive evaluation on survivors (§7), with budget steered to seeds that discriminate (§5).

A **population** keeps the search wide: islands and behavioral niches so basins get crossed instead of climbed (§6), with an explicit wider-vs-deeper allocation (§4).

**Process reward** turns rejections into diagnoses (§2), which is what makes the generator's conditioning (§3) and the memory (§9) worth anything.

**Planning** is a separate lever on the agent itself, not on the search: plan at the day, execute at the hour, evaluate plans by rollout, and distill (§4, §5) — after an oracle bound says it's worth it.

And **evaluation discipline** (§8) — paired seeds, both seats, frontier opponent, held-out set, self-play must tie — is what keeps all of the above from optimizing an artifact.

Everything we did well in the past month lives in the last paragraph. Everything we did poorly is the absence of the first five.
