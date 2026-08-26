# Output templates

Create these files in the chosen interview-preparation directory. Use the exact filenames and headings below. A Claim uses a stable `C#` ID and Evidence uses a stable `E#` ID; keep those links unchanged through `08-mastery-report.md`. Do not expose IDs, lifecycle states, learning tasks, or evidence notes in `09-resume-final.md`.

## Contents

- [00-study-brief.md](#00-study-briefmd)
- [01-resume-draft.md](#01-resume-draftmd)
- [02-claim-contracts.md](#02-claim-contractsmd)
- [03-project-map.md](#03-project-mapmd)
- [04-evidence-cards.md](#04-evidence-cardsmd)
- [05-java-agent-mapping.md](#05-java-agent-mappingmd)
- [06-question-tree.md](#06-question-treemd)
- [07-project-pitch.md](#07-project-pitchmd)
- [08-mastery-report.md](#08-mastery-reportmd)
- [09-resume-final.md](#09-resume-finalmd)

## `00-study-brief.md`

```text
# Study brief
## Project and relationship
- Project: [name/path]
- Relationship: [verified relationship framing and evidence; otherwise `open-source study`]
- Source implementation: [language/framework or unknown]
## Target and boundary
- Target role: [role]
- Time budget: [schedule]
- Goals: [what will be learned and defended]
- Non-goals / skip: [what will not be studied]
## Truthfulness rules
- Upstream capability, source observation, and personal work remain separate.
- No unsupported ownership, runtime, production, or metric claims.
## Acceptance
- [project explanation, source anchors, evidence plan, interview threshold]
## ID policy
- Claim IDs: C1 onward, never reused or renumbered.
- Evidence IDs: E1 onward, never reused or renumbered.
```

## `01-resume-draft.md`

```text
# Resume draft
## Project context
- Project / relationship: [name] — [verified relationship framing; otherwise `open-source study`]
- One-line description: [bounded upstream context]
- Technology context: [observed stack]
## Claim ledger
### C# — [bounded draft statement]
- Upstream capability: [source fact]
- Source observation: [what the user can explain]
- Personal work: [evidenced action or “No personal work claimed.”]
- State: [Draft | Understood | Verified | Ready | Blocked | Dropped]
- Evidence: [E# ... | none]
- Next action: [smallest attributable action]
```

## `02-claim-contracts.md`

```text
# Claim contracts
## C# — [same statement as the draft]
- Why it matters: [role/interview value]
- Source anchor: [file : symbol / configuration]
- Source implementation: [faithful flow]
- Inputs, outputs, and state: [bounded flow]
- Edge case: [failure/boundary and handling]
- Alternative / trade-off: [comparison]
- Java mapping: [explicit conceptual comparison]
- Evidence: [E# ...]
- Follow-up 1: [question]
- Follow-up 2: [question]
- Follow-up 3: [question]
- State and gap: [state; missing Ready-gate items]
```

## `03-project-map.md`

```text
# Project map
## Core chain: [name]
- Related Claims: [C# ...]
- Source implementation scope: [entry point through outcome]
- Nodes: [file : symbol; input -> output/state]
- Boundaries: [sync/async/streaming, persistence, external dependency]
- Failure and recovery: [observed or pending]
- Evidence: [E# ...]
```

## `04-evidence-cards.md`

```text
# Evidence cards
## E# — [short evidence name]
- Type: [source anchor | run | reproduction | experiment | diagram | code artifact | interview]
- Related Claims: [C# ...]
- Source anchor or artifact location: [path, command record, diagram, commit, or note]
- Observation / result: [what happened or what source establishes]
- Scope and limitation: [what this does not establish]
- Confidence: [verified | reasonable inference | pending confirmation]
- Recorded on: [date]
```

## `05-java-agent-mapping.md`

```text
# Java and Agent mapping
## C# — [claim]
- Source implementation: [actual technology and behavior]
- Java mapping: [Spring / Java conceptual equivalent]
- Agent mapping: [agent concept when relevant, otherwise not applicable]
- Boundary: [why this is a comparison, not a source fact]
- Trade-off: [difference or limitation]
- Evidence: [E# ...]
```

## `06-question-tree.md`

```text
# Question tree
## C# — [claim]
- Project: [what problem / capability]
- Principle: [why this design]
- Source: [where and how the source implementation works]
- Exception: [failure, edge case, or boundary]
- Optimization: [trade-off or improvement condition]
- Evidence: [E# ...]
- Answer status: [state and weakest answer]
### Q# — [exact question]
- Claim / topic: [C# or bounded topic]
- Level: [1 | 2 | 3 | 4 | 5]
- Answer summary: [what the user answered]
- Source anchor: [path : symbol, or none]
- Confidence: [verified | reasonable inference | pending confirmation]
- Correction: [specific correction or none]
- Next action: [smallest evidence-backed action]
- Java mapping: [explicit comparison or not applicable]
```

## `07-project-pitch.md`

```text
# Project pitch
## 30 seconds
- Claims: [C# ...]
- Evidence: [E# ...]
- Script: [verified relationship framing, or open-source-study default, and only supported personal work]
## 3 minutes
- Claims: [C# ...]
- Evidence: [E# ...]
- Script: [architecture, source implementation, personal verification, trade-offs]
## 10 minutes
- Claims: [C# ...]
- Evidence: [E# ...]
- Script: [deeper chains, edge cases, Java mapping, follow-ups]
```

## `08-mastery-report.md`

```text
# Mastery report
## C# — [claim]
- State: [Draft | Understood | Verified | Ready | Blocked | Dropped]
- Evidence: [E# ...]
- Question records: [Q# ... used for this score]
- Ready gates: [source anchor; personal artifact; edge case; Java mapping; trade-off; three follow-ups; interview evidence check: total >= 80% and source-evidence >= 70%]
- Interview scores: [accuracy %; source-evidence %; expression %; trade-off %; total %]
- Decision: [Ready only if all gates, total >= 80%, and source-evidence >= 70%]
- Gaps and next action: [specific remediation]
## Finalization check
- Ready Claims: [C# ... | none]
- Withheld Claims: [C# ... and reason]
```

## `09-resume-final.md`

```text
# Resume-ready project content
## Project
- [name] — [verified relationship framing; otherwise `open-source study`]
- [one-line bounded description]
## Copy-ready bullets
- [supported bullet derived only from a Ready Claim]
```

Include a bullet only when its source Claim is `Ready` in `08-mastery-report.md`. The final file must contain no `C#` or `E#` IDs, lifecycle states, evidence notes, learning tasks, source-path notes, or score records. If no Claim is `Ready`, replace the bullet section with exactly:

```text
## Copy-ready bullets
No copy-ready bullets are available: no Claim has passed the Ready gate.
```

