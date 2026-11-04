---
name: find-low-leverage-workflows
description: Identify repeated work that a leader or team could improve with AI, using ownership, leverage, available context and checkable results. Use when choosing a workflow to automate, reviewing a working week, or planning an AI experiment that preserves judgment and growth.
---

# Find low-leverage workflows

Help the user choose a real piece of repeated work to improve, then describe a small AI-assisted or automated experiment and what the user wants to make room for. Apply Jasmine James's AI Leverage Framework from **Leading Deeper with AI**.

## Start with the actual work

Use the user's examples or an authorized sample of their recent work. Ask only for missing information that materially changes the choice: who owns the outcome, which steps repeat, and where the friction or learning lies. Do not infer a person's work from their title or demand connected tools when the supplied examples are enough.

Separate a workflow into steps before classifying it. Drafting a stakeholder update and talking with stakeholders to resolve a disagreement require different attention, even when both belong to the same workflow.

Map the steps across two dimensions:

| | Work the leader owns | Work the team owns |
| --- | --- | --- |
| **Low leverage** | Repeated preparation, gathering, summarizing or drafting that adds little value when repeated manually. Look for a useful first automation. | Recurring support or coordination steps where a shared workflow could reduce repeated effort. Keep a clear owner. |
| **High leverage** | Decisions, relationships, prioritization and coaching where the leader's attention can change the outcome. | Meaningful delivery ownership, coordination and practice that develop the team's capability. |

Leverage depends on the person and situation. What is routine for an experienced engineer may be valuable practice for someone new. Check with the user before treating that learning as waste. AI can assist preparation in a high-leverage activity without owning the decision or relationship.

## Choose a candidate to try

For a repeated step, look for **usable context and a checkable result**. Recommend assistance or automation appropriate to what is available; do not equate a repeated task with permission to automate its whole workflow.

Assess:

- **Burden:** recurrence, interruptions, effort and rework. Use supplied measurements; label estimates and unknowns.
- **AI contribution:** what the agent would read, what work it could carry through, and the output someone could inspect.
- **Human responsibility:** the outcome owner, consequential decisions and review, and useful learning to preserve.
- **Practical fit:** available sources and tools, how quality could be checked, and how easy a small trial would be to stop or reverse.

Compare plausible candidates using the evidence, rather than inventing a numerical score. Recommend the strongest first choice; show alternatives when they materially affect that choice or the user asks for them. A one-off important decision is not low leverage simply because it is difficult or time-consuming. If there is no sensible candidate in the sample, explain what context would make a choice possible.

## Use a practice pool, then apply the learning

For the strongest candidate, propose a small trial using an authorized historical example, a copy, or synthetic data when useful. This is a place to test capabilities and develop judgment, not a requirement to build a separate app.

Specify the input, the AI's task, the expected output, and the check that determines whether it helped. Test the important failure cases for that workflow. If AI assesses quality, give it explicit criteria and have a person check a sample; an AI judgment is evidence to examine, not proof of correctness.

Describe how a successful trial could move into the real workflow. Keep consequential publication or approval with the appropriate owner. Identifying an opportunity does not itself authorize deployment, recurring jobs, messages or changes to shared systems.

## Match tools to the context

No particular MCP is mandatory. Use available, authorized tools with the operations needed for the selected sources:

| Context | Likely connector or MCP | Needed capability |
| --- | --- | --- |
| Support and team conversations | Slack or Microsoft Teams | Search and read selected messages and threads |
| Issues and planned work | GitHub, GitLab, Linear or Jira | Read issues, comments and status |
| Code, changes and instructions | GitHub, GitLab or local repository tools | Read relevant files, changes and history |
| Documentation and runbooks | Google Drive, SharePoint, Confluence, Notion or local files | Search and read selected documents |

State which connections are useful for the proposed experiment and which are unnecessary. If access is unavailable, work from user-provided examples or exports and describe the limitation. Do not claim to have inspected private systems or request broader access than the task needs. Choose models based on the available context, tools, quality checks, cost and latency rather than a universal model ranking.

## Return a usable decision

Lead with **one recommended step to improve and why**, grounded in the user's examples. Name what stays with people: consequential judgment, delivery ownership and useful learning. If no candidate is supported, say so and request the smallest useful recurring-work example; do not force a ranking or experiment.

When a trial is requested, give a concrete next step: **specific input → AI task → reviewable output → human check**. Identify the owner, required tools already available, important failure case and practical point to stop or adjust. Distinguish AI work from manual gathering or decisions. Keep this focused on the first trial rather than a deployment plan.

Connect the trial to what the user wants to make room for. State the baseline and follow-up needed to judge effort or interruptions, quality and rework. Preserve unknowns; do not promise saved hours or assume returned capacity must become extra delivery work.

Use a full work map, ranked alternatives or detailed measurement plan when requested or needed to resolve a real tradeoff. Otherwise omit them. Avoid repeating the same rationale in a map, ranking and closing summary.

For identification only, finish with the recommendation and essential missing evidence. If building is authorized, continue within that scope, preserving ownership and learning decisions.

Source and companion prompts: https://jasminejames.dev/leading-deeper/
