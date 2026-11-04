---
name: assess-workflow-value
description: Assess whether an AI-assisted workflow reduces human effort at an acceptable quality and cost, using supplied measurements or scoped evidence. Use for a workflow experiment or review, not to infer savings from activity counts or change the workflow.
---

# Assess workflow value

Prepare an evidence-backed assessment of one workflow experiment. This is a new companion exercise, not evidence that the talk's examples achieved any particular saving. Separate human effort, monetary cost, quality and the use of any available attention. The owner decides whether to keep, revise or stop the experiment.

## Define a comparable case

Establish the workflow step, intended outcome, outcome owner, people involved, reporting period and what counts as a completed case. Compare cases with similar scope, complexity and quality requirements; make changes in volume, staffing or case mix visible. Record each number's source, date, unit, coverage and whether it was measured, recalled, estimated or assumed.

Use approved supplied data first. Optional timing logs, issue records or calendar exports can help check scope. Calendar duration, messages, assistance percentages, generated output and elapsed agent runtime do not measure active human effort. If evidence is missing, retain an unknown value and propose the smallest useful measurement; never turn unmeasured work into zero.

## Account for human effort

Use active person-minutes for both the manual baseline and the assisted approach. Include remaining preparation, review, corrections, interventions and relevant handoffs. Count each person's effort once. Do not add an all-inclusive review total to the corrections already included in it. Simultaneous work by two people is two people's effort, not elapsed calendar time.

Include unsuccessful attempts and rework within the agreed effort window. Do not compare only successful assisted runs with all manual cases. If failures or unfinished cases prevent a fair per-completed-case comparison, show them separately and limit the conclusion.

Keep recurring maintenance and one-time setup visible. Allocate maintenance across the cases it actually supports. Amortize setup only when its effort and an explicit supported or proposed case horizon are available; label a projected horizon as an estimate. Do not charge the same setup effort twice. A result excluding unknown setup is a recurring-effort result **before setup**, not an all-in saving.

For a simple comparable case, in minutes:

```text
baseline effort/case = baseline case effort + allocated baseline overhead
assisted effort/case = assisted human effort + allocated assisted overhead
net recurring reduction/case = baseline effort/case - assisted effort/case
all-in reduction/case = net recurring reduction/case - allocated setup
period reduction = per-case reduction × supported comparable case count
```

Preserve negative results. Use actual case-level totals or appropriate summaries when cases vary; do not imply a mean describes every case. Report a range when inputs are bounded estimates, propagate the bounds conservatively, and explain their provenance. These are estimates, not measured hours. Convert minutes to hours only after calculating the scoped total. Extrapolate using an explicit frequency and period supported by evidence, not an assumed adoption rate.

The optional [fictional worked example](https://jasminejames.dev/leading-deeper/assess-workflow-value-example.json) illustrates maintenance allocation and an intentionally unknown setup cost. Read it when an example would clarify the calculation.

## Assess value beyond effort

Keep four findings distinct:

* **Effort:** comparable human preparation, review, correction and overhead, with exclusions and uncertainty.
* **Cost:** known API, tool or hosting charges for the same scope. Do not convert effort to money without a supplied rate and stated assumptions. Do not combine subscriptions and marginal usage charges without explaining the allocation.
* **Quality:** agreed acceptance checks, errors, coverage, rework and useful feedback. A model's self-assessment or a completed task state does not independently establish quality.
* **Attention and development:** what the owner intended to make room for and what actually happened, with evidence if available. Reduced effort does not prove a customer outcome, growth or improved wellbeing.

Check judgment, relationships, ownership and useful practice before recommending automation. A routine step for one person may be valuable development for another. Protect the intended learning and reviewer capacity; a faster process that removes needed practice or shifts uncounted burden to someone else is not automatically better.

## Return a decision draft

Give a concise conclusion followed by the calculation or comparison, source provenance, quality and cost findings, and any observed use of attention. Distinguish supported observations, bounded estimates and unknowns. State material exclusions, case-mix limits and whether setup is included. Recommend **keep**, **revise** or **stop** against the owner's intended outcome and acceptance conditions; when evidence is insufficient, recommend a measurement or bounded revision rather than declaring success.

Name one small next measurement, its scope, owner and review point. A supplied table or a few comparable cases may be sufficient; no MCP is compulsory. Read external sources only within the agreed accounts, measures and period. Return the draft in the current response unless a destination is authorized. Do not modify workflows, assign people, publish results, contact colleagues or create tracking or scheduled automation as a side effect.
