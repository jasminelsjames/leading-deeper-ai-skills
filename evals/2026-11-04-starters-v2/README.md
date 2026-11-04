# Starter skill concision regression check

The first study showed longer skill answers. We revised what the two starter skills show by default: lead with the useful action, keep evidence visible, and include detailed maps or continuity records when requested or necessary.

## What changed

- **Daily Debrief:** default to actionable Tonight, Tomorrow and Tracking items with sources and meaningful changes. Do not print an entire ledger by default. Preserve full records and coverage boundaries when requested. Omit unnecessary excerpt counts.
- **Choose Where Attention Belongs:** default to one supported choice and a compact input → AI task → reviewable result → human check experiment. Show maps and alternatives when they help a real decision.

Tested revision: [`cfb7338`](https://github.com/jasminelsjames/leading-deeper-ai-skills/tree/cfb7338c138386b7fb06cdbf3fd646cf29aea893/skills). The other four skill instruction bodies are unchanged.

## Results

All six fresh revised-skill outputs met the 30 original task checks. Those checks include overlap from v1, so this is a regression result, not proof of a quality improvement. Saved original skill outputs also met all 30 checks when regraded.

Five of six revised answers were shorter: approximately 2,364 words in total versus 3,052 in the saved original answers. The case explicitly requesting a full continuity record grew from 580 to 664 words; a reviewer still found room to make that record easier to scan. No factual errors were flagged in the six revised answers by this limited AI review. Historical answers still include the excerpt-count error; the new review also noted an unsupported owner assignment for C-09 in the original first case.

There was no new no-skill baseline. This is a known-case regression check comparing six fresh revised runs with historical outputs. It does not establish saved review time, general reliability or a broad benefit over an agent without a skill.

## Inspect the outputs

- **leader conflicting commitment**: [task](cases/01-leader-conflicting-commitment/task.txt), [checks](cases/01-leader-conflicting-commitment/criteria.json), [revised](cases/01-leader-conflicting-commitment/revised/answer.md), [original historical answer](cases/01-leader-conflicting-commitment/original/answer.md), [revised grade](cases/01-leader-conflicting-commitment/revised/grading.json), [original regrade](cases/01-leader-conflicting-commitment/original/grading.json).
- **ic stale ci and duplicates**: [task](cases/02-ic-stale-ci-and-duplicates/task.txt), [checks](cases/02-ic-stale-ci-and-duplicates/criteria.json), [revised](cases/02-ic-stale-ci-and-duplicates/revised/answer.md), [original historical answer](cases/02-ic-stale-ci-and-duplicates/original/answer.md), [revised grade](cases/02-ic-stale-ci-and-duplicates/revised/grading.json), [original regrade](cases/02-ic-stale-ci-and-duplicates/original/grading.json).
- **catchup partial source continuity**: [task](cases/03-catchup-partial-source-continuity/task.txt), [checks](cases/03-catchup-partial-source-continuity/criteria.json), [revised](cases/03-catchup-partial-source-continuity/revised/answer.md), [original historical answer](cases/03-catchup-partial-source-continuity/original/answer.md), [revised grade](cases/03-catchup-partial-source-continuity/revised/grading.json), [original regrade](cases/03-catchup-partial-source-continuity/original/grading.json).
- **leader prep versus relationships**: [task](cases/04-leader-prep-versus-relationships/task.txt), [checks](cases/04-leader-prep-versus-relationships/criteria.json), [revised](cases/04-leader-prep-versus-relationships/revised/answer.md), [original historical answer](cases/04-leader-prep-versus-relationships/original/answer.md), [revised grade](cases/04-leader-prep-versus-relationships/revised/grading.json), [original regrade](cases/04-leader-prep-versus-relationships/original/grading.json).
- **important oneoffs no repetition**: [task](cases/05-important-oneoffs-no-repetition/task.txt), [checks](cases/05-important-oneoffs-no-repetition/criteria.json), [revised](cases/05-important-oneoffs-no-repetition/revised/answer.md), [original historical answer](cases/05-important-oneoffs-no-repetition/original/answer.md), [revised grade](cases/05-important-oneoffs-no-repetition/revised/grading.json), [original regrade](cases/05-important-oneoffs-no-repetition/original/grading.json).
- **shared support growth and ownership**: [task](cases/06-shared-support-growth-and-ownership/task.txt), [checks](cases/06-shared-support-growth-and-ownership/criteria.json), [revised](cases/06-shared-support-growth-and-ownership/revised/answer.md), [original historical answer](cases/06-shared-support-growth-and-ownership/original/answer.md), [revised grade](cases/06-shared-support-growth-and-ownership/revised/grading.json), [original regrade](cases/06-shared-support-growth-and-ownership/original/grading.json).

[Result data](results.json), [registered protocol](protocol.json) and [blind condition map](blind-condition-map.json) are included. [The original study](../2026-11-04-starters-v1/README.md) is unchanged.

## Method and limits

Use the original six tasks with fresh sessions and the exact revised skills. Do not show executors grading criteria or historical answers. We ran one revised-skill session per task, restricted to fictional task data and the skill file. Two fresh model graders received only tasks, criteria and A/B answers with conditions hidden. The coordinator reviewed all answers and grading. Session model configuration was inherited; the interface did not expose the exact backend identifier. No human has scored these outputs.

Counts use the same regex method as v1, including source IDs and structured records. Run `python3 recompute_results.py` to check arithmetic and lengths; it does not validate the graders' judgments. Single runs, familiar cases and model-based grading limit the result. No installation, live connector, scheduling, cross-model, cost, latency or workplace outcome test was performed.

The practical value of these skills is reusable instructions for repeated work. These tests show how current instructions behaved on these examples; usefulness in your setting still needs your review. [Share what you used and corrected](https://github.com/jasminelsjames/leading-deeper-ai-skills/issues/new).
