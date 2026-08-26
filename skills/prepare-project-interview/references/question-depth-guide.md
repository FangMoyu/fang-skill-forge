# Question depth guide

Use this guide to conduct source-grounded interview practice for a selected
topic or Claim. It tests explanation, not recall of generic Java or Agent
terminology. Keep upstream capability, source observation, and personal work
separate throughout the conversation.

## Contents

- [Interview protocol](#interview-protocol)
- [Five question levels](#five-question-levels)
- [Evidence-gap stop rule](#evidence-gap-stop-rule)
- [Scoring](#scoring)
- [Ready decision](#ready-decision)
- [Answer record](#answer-record)

## Interview protocol

Ask exactly one question at a time. Wait for the answer, assess it against the
current evidence record, give a concise correction or next action, and only
then decide whether to continue. Do not reveal a later-level answer in the
question, combine multiple prompts, or convert a missing source answer into a
hypothetical implementation exercise.

Start at the lowest unanswered level. Advance only when the answer is accurate
for its stated scope and is supported by the evidence available for that level.
Use the source implementation first; discuss a **Java mapping** only after the
source answer is clear and label it as a comparison.

## Five question levels

| Level | Purpose | One-question prompt shape | Evidence needed to advance |
| --- | --- | --- | --- |
| 1. Project value | Explain the bounded user or system value without taking ownership of upstream work. | “What bounded problem does this observed capability address?” | A bounded project statement and correct open-source/personal-work framing. |
| 2. Technical principle | Explain why the observed pattern is suitable and name a credible alternative. | “Why is [observed pattern or boundary] used here?” | A source-aligned principle and one non-invented trade-off. |
| 3. Source implementation | Locate and trace the actual implementation. | “Where is the source implementation for [selected behavior]?” | Precise anchor plus input, flow, output/state, and boundary. |
| 4. Failure or boundary | Explain an evidenced non-happy path, limit, or absence. | “What happens at the evidenced [failure or boundary]?” | Source-backed handling or the exact `Absent capability` marker with inspected scope. |
| 5. Optimization or alternative | Compare a conditional improvement without rewriting source facts. | “What alternative would you evaluate for [observed constraint]?” | A clearly hypothetical alternative tied to the observed constraint and evidence. |

After assessing an answer, ask further detail as a later, separate question at
the same level; never bundle it into the initial prompt or advance a level to
obtain it. Use these atomic follow-ups only when the preceding answer supports
the same-level question:

- Level 1: “What is the relevant project scope for that capability?”
- Level 2: “What trade-off does that observed choice make?”
- Level 3, later turn: “How does [input] move from [source anchor]?”
- Level 3, another later turn: “What output or state results from that flow?”
- Level 4: “Where is that behavior established?”
- Level 5: “Which trade-off would decide whether to adopt that alternative?”

At every level, ask about a single selected topic, not the entire repository.
For an Agent topic, do not assume a ReAct loop, context store, tool execution,
streaming, retry, evaluation, or safety control exists. For backend topics, do
not assume cache, queue, transaction, metric, or test behavior exists.

## Evidence-gap stop rule

Stop escalation immediately when the answer cannot cite the evidence required
for the current level. Record the first gap; do not ask a deeper question that
would require the missing fact.

| Gap | Stop and record | Smallest next action |
| --- | --- | --- |
| No source anchor | `pending confirmation`; source location unknown. | Find the route, entrypoint, symbol, configuration, or artifact that bounds the topic. |
| Anchor but no traceable flow | `reasonable inference`; flow not yet verified. | Trace one input through one output/state transition. |
| No evidenced failure behavior | `pending confirmation`; failure handling unknown. | Inspect the immediate error/cancellation/timeout boundary, or state `Absent capability` for the inspected scope. |
| Capability not found | `Absent capability` with the inspected scope. | Do not escalate; choose another evidenced topic or study the necessary design as a Java comparison. |
| No personal artifact | Keep the Claim below `Verified`/`Ready` as required by the claim rubric. | Record a bounded run, reproduction, experiment, diagram, or code artifact. |

Never bridge a gap by fabricating Agent, cache, queue, transaction, retry,
metric, or test behavior. A Java/Spring answer can be useful after an absence
is documented, but it cannot upgrade the source evidence or create a Ready
claim.

## Scoring

Score the completed answer set after the interview, using the fixed weights
below. Give each category a 0--100 assessment from recorded answers; the total
is the weighted sum. Do not award points for plausible but unanchored details.

| Category | Weight | Assess |
| --- | ---: | --- |
| Accuracy | 30% | Correct, bounded explanation that distinguishes facts, inferences, and unknowns. |
| Source evidence | 30% | Precise anchors and a defensible input-to-output/state trace. |
| Expression | 20% | Clear, ordered, direct explanation that answers the question asked. |
| Trade-offs | 20% | Relevant alternatives, limits, and reasons for the observed or proposed choice. |

`Total = accuracy × 30% + source evidence × 30% + expression × 20% + trade-offs × 20%`.

Use this record shape:

```text
Topic / Claim: [identifier]
Level reached: [1--5 or evidence-gap stop]
Accuracy: [0--100]
Source evidence: [0--100]
Expression: [0--100]
Trade-offs: [0--100]
Total: [weighted result]
Evidence gap / next action: [specific item or none]
```

## Ready decision

A Claim is `Ready` only when every Ready gate in the claim rubric is recorded,
the **total is >= 80%**, and **source evidence is >= 70%**. These are fixed
thresholds: a high expression or trade-off score cannot compensate for weak
source evidence, and a passing score cannot replace a missing personal artifact
or other Ready gate.

If either threshold fails, retain the current truthful state and schedule the
smallest evidence-backed remediation. If escalation stopped at an evidence gap,
do not calculate a persuasive substitute score or mark the Claim `Ready`.

## Answer record

For each asked question, create one repeatable `Q#` record in
`06-question-tree.md` with the topic/Claim, level, exact question, answer
summary, source anchor, confidence, correction, and next action. Keep the Java
mapping in its own field and label it as comparison. Reference the `Q#` records
used for each score in `08-mastery-report.md`. This record lets the next
practice round begin at the first unsupported level rather than repeating
generic questions.

