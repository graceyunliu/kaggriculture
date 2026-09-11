# Prompt: recover unregistered genes from agent history

Audit every Kaggriculture conversation/task you can access in your own history, plus the
repository's experiment reports, candidate diffs, replay-mining outputs, and `evolve/RULES.md`.
Compare every finding with `evolve/gene_registry.json`. Find useful mechanisms that are
missing from the registry, especially small positive effects that were inherited into a later
candidate, dismissed as too small for a ladder submission, buried inside a composite, or
reported only as a side-finding.

Do not equate "positive once" with "validated." For each finding, return:

1. exact base candidate and exact code/parameter change;
2. causal mechanism and proof that the behavior actually fired;
3. seed blocks, opponents/streams, seats, shop regime, sample size, own-money delta,
   opponent-money delta, margin delta, t-statistics, and win/loss counts where available;
4. whether the evidence is selection, held-out, fresh replication, or live ladder evidence;
5. whether it is already inherited by O26/O33, independent, matchup-specific, or inseparable
   from another change because of a measured interaction;
6. the precise source: chat/task title and ID if available, plus file paths and report headings;
7. one status from `validated_gene`, `validated_interaction_pair`, `validated_bundle`,
   `provisional_gene`, `composite_needs_ablation`, `matchup_specific`, `already_registered`,
   or `rejected_not_a_gene`.

Explicitly search for phrases such as "small positive," "not promoted," "for review,"
"side-finding," "held-out," "fresh," "own money," "all streams positive," "null alone,"
"interaction," and candidate-to-candidate deltas. Include negative and null findings when
they prevent an attractive false gene from being rediscovered.

Use the project's evidence rules: a margin-only gain is not a gene without own-money support;
small or trajectory-changing samples require replication; fixed-tape market attacks are not
assumed to transfer; and two changes with a demonstrated interaction stay coupled. Do not use
quarantined final-evaluation seeds, submit a ladder candidate, or modify the registry.

Output two artifacts in your response:

- a concise ledger sorted by confidence and expected value; and
- a proposed JSON patch containing only genuinely missing entries, with uncertainties stated
  rather than filled in from memory.

Finish by recommending the highest-value independent gene to cross with `FERT_DENIAL4` in a
preregistered Base / Fert / New / Fert+New factorial.
