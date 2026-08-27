# Claim and question template

Use this reference for the detailed resume explanation and the grilling handbook. It is intentionally source-first: a plausible Java or Agent design cannot substitute for missing repository evidence.

## Claim record

For each selected claim record:

```text
Claim: [bounded resume sentence]
Business value: [user/system problem]
Upstream capability: [what the project provides]
Source observation: [precise file/symbol/configuration/test and input→output/state flow]
Personal work: [specific artifact, or “No personal work claimed.”]
Failure/boundary: [observed handling, or “not evidenced”]
Alternative/trade-off: [credible alternative and why it differs]
Java/Agent mapping: [comparison, clearly not a source fact]
Evidence and confidence: [source/run/experiment; verified, reasonable inference, or pending]
Smallest next action: [one bounded verification]
```

Select claims for distinct coverage. A useful six-claim set for an Agent product might cover orchestration and constrained intent, retrieval/ranking, persistence or indexing, reliability/fallback, state/memory, and Trace/evaluation. Replace or remove topics when the source lacks them.

## Wording rules

Use “design” for a justified choice, “implemented” only with a matching code artifact, “supports” with explicit conditions, and “verified” only with a recorded run or test scope. Replace “always”, “complete”, “production-ready”, “guarantees”, and numerical improvement language unless the evidence truly covers those statements.

When source and design documentation differ, privilege the source anchor and record the conflict. When source has a capability but no personal artifact, keep the statement as a neutral source observation or bounded draft.

## Question ladder

Generate one atomic topic at each level before moving to the next:

1. **Project value:** What bounded user or system problem does this capability address?
2. **Implementation trace:** What input, state, component boundary, output, and persistence/external dependency are involved?
3. **Fundamentals:** Why is the observed algorithm, Java/Spring, database, Redis, Agent, or streaming choice suitable?
4. **Failure boundary:** What happens for timeout, invalid output, missing data, concurrency, authorization, or consistency failure actually evidenced in the source?
5. **Conditional optimization:** What alternative would you evaluate, under what trigger, and what trade-off would it introduce?

Do not put two independent questions into one prompt. In live practice ask exactly one formal question, wait for the answer, then provide feedback. In a bulk handbook, mark every unanswered question as unpracticed and do not assign a score.

## Per-question format

```markdown
## QN｜[plain-language topic]

**Claim / topic:** [claim]
**Difficulty:** [1–5]
**Practice status:** [independent answer / reference requested / unpracticed]

### Question
[one atomic prompt]

### What it tests and common traps
[bounded explanation]

### Complete reference answer
[current source behavior first; proposed design labeled]

### Short answer (≤300 Chinese characters)
[same facts, no new claims]

### Recall line (≤80 Chinese characters)
[same facts, no new claims]

### Memory formula
[one compact relationship]

### Source anchors
[links]

### Smallest verification action
[bounded run/reproduction/diagram/code artifact]
```

The complete answer must explain the current source, not just generic theory. Add one alternative or trade-off when the question reaches level 2 or higher. Say `Absent capability` with the inspected scope when a requested feature is not present; never fill the gap with an imagined implementation.

## Feedback for live grilling

Use fixed categories: accuracy 30%, source evidence 30%, expression 20%, trade-offs 20%. Give a complete reference answer even when the candidate says “不会” or asks for the answer. A direct answer request is not an independent pass. Do not ask the next formal question in the same feedback turn.

## Privacy and evidence

Sanitize API keys, passwords, authorization headers, private user data, and long raw prompts before including them in a Trace example or study package. A test passing proves only its covered behavior. A source inspection proves neither personal ownership nor production reliability.

