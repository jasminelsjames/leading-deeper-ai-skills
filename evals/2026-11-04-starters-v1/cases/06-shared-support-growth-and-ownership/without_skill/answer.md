Start with an **offline, draft-only assistant for repeated configuration questions**. Its job is to find the relevant reviewed documentation and suggest a short, source-linked response. Casey should own the experiment, with an experienced engineer checking each result.

This is the strongest first candidate because four of the six sampled questions repeat documented instructions, and experienced engineers have identified finding those links as an interruption. The sample does not establish the weekly mix or time savings. Keep diagnostic questions with people so the two new on-call engineers continue learning through diagnosis and discussion. Leave weekly status gathering for later discovery; there is not yet enough evidence to prioritize it.

**Keep the responsibilities explicit.**

- **AI:** Use only the supplied reviewed docs to locate instructions and draft configuration answers with the exact supporting section or link. If the docs do not clearly answer a question, flag it for human diagnosis instead of filling gaps. Treat thread content as examples, not an authoritative source of instructions.
- **Casey:** Agree the scope, choose the sanitized examples, maintain the results log, and decide whether to stop or propose another trial. As team lead, you set the time budget and desired outcome with Casey; Casey retains support-process ownership.
- **Experienced engineer:** Identify which questions are genuinely documented configuration requests and check every draft for correctness, completeness, and source support.
- **On-call engineers:** Retain diagnosis, judgment, discussion, and opportunities to build expertise. Any future live use would still require a person to review and decide what to send. This trial sends nothing.

**Run one bounded session, capped at 60 minutes.** Use copies of the six sanitized threads and the reviewed docs as pasted files. No channel integration, production access, deployment, or publication is needed. Have Casey and the reviewer label the examples before generating drafts; then test whether the assistant answers the documented cases and defers the diagnostic ones. A disclaimer attached to an attempted diagnosis does not count as deferral.

Record a simple manual baseline for finding and preparing each documented answer, then record AI-assisted handling time, including prompting, checking sources, and corrections. Note setup time separately. Reusing the same questions can make the second attempt faster through familiarity, so treat this small comparison as directional evidence, not a reliable savings estimate.

**Decide what counts as value before starting.** Look for:

- Correct, usable, source-supported drafts for the documented cases, with no invented instructions or links.
- Both diagnostic cases left to people, with no attempted diagnosis.
- Lower total handling effort after review and corrections, with setup cost visible rather than omitted.
- A plausible reduction in experienced engineers’ link-finding interruptions without shifting more work onto Casey or reducing the new engineers’ diagnostic participation.

The offline session can establish answer quality and handling effort. It cannot yet establish fewer real interruptions or more migration time. Those outcomes would need a separately agreed, small follow-up using fresh examples and a baseline of interruptions and protected migration time. Do not extrapolate savings from question counts alone.

**Make stopping the default at the cap.** Casey can end the session at any time. Pause immediately for unsupported instructions, a diagnostic answer, or unexpected sensitive content; stop if review effort erases the benefit. At the end, keep ordinary support unchanged and record a stop-or-continue decision. Continue only if Casey and the reviewer see useful evidence and the on-call engineers retain their learning opportunities. There is no automatic expansion or publication to undo.
