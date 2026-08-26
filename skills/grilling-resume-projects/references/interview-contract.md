# Interview contract

Read this file before asking or assessing a question.

## Evidence boundary

Keep these four layers explicit:

| Layer | Meaning |
| --- | --- |
| Resume claim | What the candidate wrote or stated |
| Source observation | What precise repository anchors establish |
| Personal contribution | What attributable commits, designs, tests, reports, or artifacts establish |
| Proposed design | A hypothetical optimization, clearly labeled as not current behavior |

Ask from the resume first. Cite source anchors only after the candidate answers. If documentation conflicts with source, use the precise source anchor for implementation facts and report the conflict.

## Difficulty ladder

| Tier | Question focus |
| --- | --- |
| 1 — 基础认知 | Business purpose, terminology, main flow, pattern responsibilities |
| 2 — 项目实现 | Concrete inputs, processing, outputs, state, and component handoffs |
| 3 — 原理八股 | Related Java, Spring, database, Redis, messaging, algorithms, or Agent principles |
| 4 — 异常边界 | Errors, invalid configuration, retries, idempotency, timeouts, and consistency |
| 5 — 高并发优化 | Multi-instance design, degradation, observability, benchmarking, and trade-offs |

Apply advancement after an independent answer:

- total >= 80: advance one tier;
- total 60–79: remain at the same tier for targeted practice;
- total < 60: step back one tier for prerequisites;
- direct answer request: record as not independently answered and do not advance;
- explicit “too difficult” request: lower the tier before the next question.

Do not jump from a basic question directly to distributed or high-concurrency design without passing the intervening tier.

## Question contract

Each prompt tests one bounded topic. It may contain only the context needed to answer that topic. Do not bundle a later dependent question or reveal the recommended answer.

Within a topic, progress in this order:

1. bounded business value;
2. project implementation trace;
3. related fundamentals;
4. evidenced failure boundary;
5. conditional optimization.

## Scoring

Score each independent answer:

`total = accuracy × 30% + source evidence × 30% + expression × 20% + trade-offs × 20%`

Report the four weighted contributions as points out of 30, 30, 20, and 20. Plausible but unsupported details receive no source-evidence credit.

When the candidate directly requests the answer without attempting it, use `0/100 — 本轮未独立作答` unless the user explicitly asks not to score skipped questions.

## Feedback recipe

After every candidate response, return these sections in order:

1. **评分** — total and four-part breakdown.
2. **核心错误** — or improvement points when the answer is correct.
3. **完整标准答案** — polished interview language, no fixed length; current source behavior first, proposed design second.
4. **300字内简易答案** — accessible summary of the same facts, normally no more than 300 Chinese characters.
5. **速记答案** — memory outline, normally no more than 80 Chinese characters.
6. **记忆公式** — one compact relationship or sequence.
7. **进一步设计** — include only when appropriate for the current tier.
8. **难度决定** — advance, remain, or step back. Do not ask the next formal question in this turn.

The simplified and recall answers must not introduce facts absent from the complete answer.

## Direct-answer and clarification handling

- “不会”“告诉我答案”: give the entire feedback recipe; do not advance.
- A factual clarification between questions: answer it directly without pretending it was an interview attempt.
- “继续出题”: ask exactly one question at the current tier.
- “降低难度”: lower the tier first, then ask one foundational question.
- A user correction to the output format: update the session contract and use it for later answers.

## Persistence contract

When persistence is active, append one stable record per question:

```text
### Q# — exact question
- Claim / topic:
- Difficulty tier:
- Answer summary:
- Source anchor:
- Confidence:
- Score:
- Core error:
- Correction:
- Reference answer:
- Simplified answer:
- Recall answer:
- Memory formula:
- Next action / tier:
```

Update linked evidence and mastery files when they already exist. Preserve user changes and unrelated files.

## Quick reference

| Situation | Required action |
| --- | --- |
| First question | Resume-framed, one question, start at supported tier |
| Candidate answers | Score and provide all answer layers |
| Candidate skips | Full answer, no advancement |
| Source lacks feature | State absence; label optimization as proposed |
| Candidate overclaims | Separate resume wording, source, and personal evidence |
| User says too hard | Lower tier before next question |
| User says continue | Ask one question only |

## Common mistakes

- Asking several questions in one turn.
- Exposing source symbols in the initial prompt.
- Giving only criticism without a complete reference answer.
- Treating a direct answer request as mastery.
- Calling an optimization current implementation.
- Treating source inspection as proof of personal ownership or production metrics.
- Jumping difficulty because the topic is interesting rather than because the candidate passed.

## Generic example

Candidate answer: “责任链就是所有节点都会执行，规则树可以分支。”

Assessment shape:

- Credit the linear-versus-branching distinction.
- Correct that a chain can short-circuit, so not every node runs.
- Provide a complete explanation, a <=300-character version, a <=80-character recall line, and a formula such as `责任链 = 顺序 + 短路；规则树 = 条件 + 分支`.
- Use the score to decide the next tier; do not ask another formal question in the feedback turn.

