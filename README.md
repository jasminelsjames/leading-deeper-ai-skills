# Leading Deeper AI skills

Give your agent a process you can reuse for recurring work.

Start with **[Daily Debrief](skills/daily-debrief/SKILL.md)** for a sourced action list, or **[Choose Where Attention Belongs](skills/find-low-leverage-workflows/SKILL.md)** to pick one repeated task to improve.

These skills capture a process you can reuse: what your agent should read, what it should return and what you need to check. Supply fresh context each time instead of rebuilding the instructions. You keep the decisions.

## Use a skill

Give your agent the relevant `SKILL.md` and the context it asks for. Start with pasted excerpts; connectors are optional for a first trial. Your agent environment controls installation, tools and recurring runs.

For example, with this repository available to your agent:

```text
Read skills/daily-debrief/SKILL.md and prepare a private debrief.
Me: [name or handle]
Work focus: [leader, individual contributor or mixed]
Day and timezone: [one day, timezone]
Sources: [approved calendar entries, notes and message excerpts]
Previous brief: [optional]
Return Tonight, Tomorrow and Tracking with sources and uncertainty.
I choose the priorities. Do not send messages or change tasks.
```

## Pick the result you need

| Agent skill | What you get | Try it |
| --- | --- | --- |
| [Choose Where Attention Belongs](skills/find-low-leverage-workflows/SKILL.md) | One repeated task to improve, with a small AI experiment to try. | [Example](examples/find-low-leverage-workflows.json) |
| [Daily Debrief](skills/daily-debrief/SKILL.md) | A sourced action list for Tonight, Tomorrow and Tracking. | [Example](examples/daily-debrief.json) |
| [Review feedback and propose improvements](skills/review-feedback/SKILL.md) | A proposed fix, with the feedback and evidence behind it. | [Example](examples/review-feedback.json) |
| [Build reusable context](skills/build-reusable-context/SKILL.md) | A knowledge starting point with sources and unanswered questions. | [Example](examples/build-reusable-context.json) |
| [Delegate work you can review](skills/delegate-reviewable-work/SKILL.md) | A task brief or reviewable result, with clear checks and a stopping point. | [Example](examples/delegate-reviewable-work.json) |
| [Check whether the automation is helping](skills/assess-workflow-value/SKILL.md) | An effort comparison and a keep, revise or stop recommendation. | [Example](examples/assess-workflow-value.json) |

[Website guides](https://jasminejames.dev/leading-deeper) show the inputs, outputs and human checks. [catalog.json](catalog.json) provides the same skill names, requests, connector guidance and first-use contracts for agents. Examples are fictional, not company reports or measured benefits.

## What have we tested?

[Initial comparison](evals/2026-11-04-starters-v1/README.md) and [concision revision](evals/2026-11-04-starters-v2/README.md): actual outputs, checks and limits for the two starter skills. The revision retained the original checks in six known cases and shortened five answers. These are small AI-reviewed tests, not a productivity benchmark.

## Was the result useful?

[Share feedback](https://github.com/jasminelsjames/leading-deeper-ai-skills/issues/new): what you used, what you had to correct and what would make the next run better. Use fictional or sanitized examples.

Have an improvement? [Open a PR](CONTRIBUTING.md) with the problem, your change and an example showing its effect. Run `python3 scripts/validate_repository.py` before submitting. Maintainers review changes before the website imports an approved version.

[MIT license](LICENSE). These are Jasmine’s personal resources accompanying *Leading Deeper with AI*.
