Start with an **offline assistant for finding reviewed configuration instructions and drafting a cited reply**. Casey owns the trial; an experienced engineer checks its answers. Keep diagnosis and discussion with people, including the two new on-call engineers. Nothing should be deployed or sent.

### Work map

| Step | Ownership | Where attention adds value |
| --- | --- | --- |
| Find the same configuration instructions and prepare a reply | Team-owned support; Casey owns the process | Repeated lookup interrupts experienced engineers. This is the strongest low-leverage candidate. |
| Decide whether documented instructions fit a question | Team-owned; on-call engineers, supported by an experienced reviewer | Requires judgment. New engineers should still practice recognizing configuration issues versus diagnostic work. |
| Diagnose unfamiliar problems and discuss solutions | Team-owned | High-leverage learning for new on-call engineers; retain investigation, discussion and decisions. |
| Gather weekly status | Ownership not specified | Potentially repetitive preparation, but its inputs, burden and owner are unknown. |
| Set priorities and protect learning time | You as team lead, working with Casey | High-leverage leadership: make room for the team-owned migration and engineer development. |

### Ranked opportunities

1. **Configuration lookup and reply preparation.** Four of six sampled questions repeat reviewed documentation, and experienced engineers report interruption from finding the same links. The documentation provides a checkable source. The channel receives about 12 questions weekly, but the small sample does not establish the ongoing configuration share, and time per question is unknown.
2. **Weekly status gathering.** A plausible later candidate. First establish its owner, inspect a small sample and measure gathering effort; there is not enough evidence to prioritize it over support lookup.

Do not automate diagnostic answers in this first trial. The two diagnostic examples are useful tests of whether the assistant recognizes its limits, while the work itself remains valuable practice.

### First experiment: six-thread practice pool

**Input → AI work → reviewable output:** Casey supplies the six sanitized historical threads and reviewed documentation as pasted files. Give the AI each initial question and necessary context, withholding the historical resolution for comparison. Ask it to find directly applicable configuration instructions and produce a short draft with an exact document title, section or link. Each output should state its assumptions and uncertainties. If the documentation does not clearly support an answer, it should flag the question for human diagnosis rather than invent instructions.

**Tools:** Pasted files and an AI chat are enough. No Slack MCP, production access or additional service connection is needed. The trial cannot establish performance on unseen channel traffic or access-controlled production details.

**People:** Casey defines the scope, records results and decides whether to stop. The experienced engineer verifies applicability, citations, completeness and safety against the reviewed docs and historical resolution. New engineers retain diagnostic investigation and discussion, and give feedback on whether the proposed assistance supports their learning. AI drafts; people own technical judgments, corrections, process changes and any future publication.

**Checks:** Review all six outputs. The four documented configuration cases should yield correct, usable citations and instructions. The two diagnostic cases should be left for people. Also test clearly labeled variants with missing configuration details, an unsupported request and a misleading keyword match. Expect a clarification or handoff when the source does not justify a reply. Treat any AI self-assessment as a claim for the reviewer to verify.

**Stop or adjust:** Cap the trial at these six examples plus the failure-case variants and one revision of the instructions. Stop immediately if sanitation is inadequate or the assistant recommends unsupported changes. Narrow or abandon it if it keeps answering diagnostic questions, invents citations, or takes as much human effort to review and correct as manual lookup. Stopping means ceasing use of the prompt and drafts; there is no integration or shared-system change to undo.

### Evidence of value

Before testing, measure manual lookup and reply-preparation time on comparable configuration examples. Then record AI waiting time, human review/correction time, citation accuracy, substantive errors and rework. Use matched examples or vary the order where practical; repeated exposure can make the second method look faster. Six threads provide directional evidence, not a reliable savings estimate.

A promising result is correct, source-supported configuration drafts with lower total human effort, reliable handoff of diagnostic cases, and positive feedback from Casey, experienced engineers and new on-call engineers. A successful offline trial could justify a separately agreed, time-limited manual-use pilot: Casey pastes selected questions, a person approves and posts any answer, and diagnostic work stays with the engineers. There is no authorization for auto-publication.

Only a later live pilot could show fewer interruptions. Compare interruption frequency and support effort before and during that pilot, alongside rework and engineer feedback. Look for more uninterrupted migration time **and continued diagnostic learning**, rather than promising saved hours or automatically filling every available minute with additional delivery work.
