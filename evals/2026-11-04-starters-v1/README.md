# First starter skill evaluation

Six fictional cases, twelve fresh agent sessions, two starter skills. Each case ran once with the published skill and once without it. Tested skill source: [`c84292a`](https://github.com/jasminelsjames/leading-deeper-ai-skills/tree/c84292ad2f7c2d1411833ca0c26ed464b5af35e4/skills).

## What happened

The skill condition met **30 of 30 predefined checks**. The no-skill baseline met **28 of 30**. Both missed baseline checks concerned one case: it correctly declined to automate consequential one-off work, but offered no concrete recurring-work next step. Those two checks overlap. This small difference does not establish a general quality improvement.

Both conditions met every check in the other five cases. The skill answers were longer in every case: approximately 3,052 words in total versus 1,934 for the baseline, using the method below. Additional review found a factual counting error in a skill answer: it described six supplied excerpts as seven. That error was outside the original rubric. A full check score therefore does not mean an answer is error-free.

The useful next iteration is shorter default answers, distinct rather than overlapping criteria, and more tests with human review. We have not changed the skills to improve these reported results.

## Inspect the actual work

- **leader conflicting commitment**: [task](cases/01-leader-conflicting-commitment/task.txt), [checks](cases/01-leader-conflicting-commitment/criteria.json), [with skill](cases/01-leader-conflicting-commitment/with_skill/answer.md), [baseline](cases/01-leader-conflicting-commitment/without_skill/answer.md), [skill grading](cases/01-leader-conflicting-commitment/with_skill/grading.json), [baseline grading](cases/01-leader-conflicting-commitment/without_skill/grading.json).
- **ic stale ci and duplicates**: [task](cases/02-ic-stale-ci-and-duplicates/task.txt), [checks](cases/02-ic-stale-ci-and-duplicates/criteria.json), [with skill](cases/02-ic-stale-ci-and-duplicates/with_skill/answer.md), [baseline](cases/02-ic-stale-ci-and-duplicates/without_skill/answer.md), [skill grading](cases/02-ic-stale-ci-and-duplicates/with_skill/grading.json), [baseline grading](cases/02-ic-stale-ci-and-duplicates/without_skill/grading.json).
- **catchup partial source continuity**: [task](cases/03-catchup-partial-source-continuity/task.txt), [checks](cases/03-catchup-partial-source-continuity/criteria.json), [with skill](cases/03-catchup-partial-source-continuity/with_skill/answer.md), [baseline](cases/03-catchup-partial-source-continuity/without_skill/answer.md), [skill grading](cases/03-catchup-partial-source-continuity/with_skill/grading.json), [baseline grading](cases/03-catchup-partial-source-continuity/without_skill/grading.json).
- **leader prep versus relationships**: [task](cases/04-leader-prep-versus-relationships/task.txt), [checks](cases/04-leader-prep-versus-relationships/criteria.json), [with skill](cases/04-leader-prep-versus-relationships/with_skill/answer.md), [baseline](cases/04-leader-prep-versus-relationships/without_skill/answer.md), [skill grading](cases/04-leader-prep-versus-relationships/with_skill/grading.json), [baseline grading](cases/04-leader-prep-versus-relationships/without_skill/grading.json).
- **important oneoffs no repetition**: [task](cases/05-important-oneoffs-no-repetition/task.txt), [checks](cases/05-important-oneoffs-no-repetition/criteria.json), [with skill](cases/05-important-oneoffs-no-repetition/with_skill/answer.md), [baseline](cases/05-important-oneoffs-no-repetition/without_skill/answer.md), [skill grading](cases/05-important-oneoffs-no-repetition/with_skill/grading.json), [baseline grading](cases/05-important-oneoffs-no-repetition/without_skill/grading.json).
- **shared support growth and ownership**: [task](cases/06-shared-support-growth-and-ownership/task.txt), [checks](cases/06-shared-support-growth-and-ownership/criteria.json), [with skill](cases/06-shared-support-growth-and-ownership/with_skill/answer.md), [baseline](cases/06-shared-support-growth-and-ownership/without_skill/answer.md), [skill grading](cases/06-shared-support-growth-and-ownership/with_skill/grading.json), [baseline grading](cases/06-shared-support-growth-and-ownership/without_skill/grading.json).

[Results JSON](results.json) contains per-case counts, output lengths, findings and limitations. [Protocol](protocol.json), [test prompts](evals.json), [criteria registration](criteria-registration.json) and the [blinding map](blind-condition-map.json) make the procedure inspectable.

## Method and reproduction

1. Use the two skills from the exact commit above. Three cases use Daily Debrief; three use Find Low Leverage Workflows (shown on the website as Choose Where Attention Belongs).
2. For each task, start two fresh sessions with the same model configuration and no inherited conversation. Give both the task file and restrict them to the supplied fictional data, no web, external actions or other skills. In the skill condition, also load the matching `SKILL.md`. Request a final Markdown answer only; do not show either executor the expected answer or grading criteria.
3. Run one trial per condition. Save the original outputs unchanged. Cases and the protocol were registered before execution; grading criteria were frozen before output inspection, while some executions were in progress. One wording typo was clarified before grading.
4. Mask the conditions with A/B labels that vary between cases, and give graders only each task, the criteria and both labeled outputs. Here two fresh Codex graders reviewed three cases each. They were not shown the skills or condition mapping. The coordinating AI then inspected all twelve answers and grading. No human scoring has been performed.
5. Recompute recorded totals with `python3 recompute_results.py`. This checks arithmetic and exact output lengths against the saved grading; it does not validate the graders' judgments. Human readers can disagree with the grades and propose corrections.

Execution and grading used Codex subagents inheriting the same session configuration. The collaboration interface did not expose an exact backend model identifier. No model override was used. This limitation prevents exact model-version reproduction and is recorded rather than guessed.

Word counts are regex word-like sequences in raw Markdown, including source IDs and structured records. They indicate answer length, not readability, runtime or model tokens. Numbers mentioned informally in the original graders’ prose are unverified estimates and can differ; `results.json` and `recompute_results.py` provide the reproducible counts. The no-skill prompt was the identical user task with no skill instructions. These are explicit-invocation tests; automatic skill selection was not tested.

## Limits

- One run per condition across six hand-authored synthetic cases. No significance or uncertainty claim.
- Only two of the six skills tested. The other four do not yet have behavioral results.
- Same inherited model configuration for execution and grading; model judges can share biases.
- No installation, connector, scheduling, cross-model, latency, cost, real-world outcome or time-saving tests.
- The two missed checks overlap, and an unscored counting error was found after grading. More distinct criteria and broader factual review are needed.

These are preliminary, AI-graded task checks, not a certification or productivity benchmark. [Report a result or correction](https://github.com/jasminelsjames/leading-deeper-ai-skills/issues/new).
