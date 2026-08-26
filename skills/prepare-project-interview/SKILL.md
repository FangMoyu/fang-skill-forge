---
name: prepare-project-interview
description: Use when preparing resume content and source-level interview follow-ups from an unfamiliar or open-source project under a limited study schedule, especially for Java backend or AI Agent roles.
---

# Resume-first project interview preparation

Treat an unfamiliar repository as an open-source study project unless the user supplies evidence of another relationship. The workflow is **resume first, then evidence-driven study**: a brief is administrative context, and the first substantive learning artifact is the resume draft.

Before writing, name the chosen `interview-prep/` directory and note that it normally should not be committed to the upstream repository. Use POSIX-style relative paths in records.

## Calibrate

Confirm only missing information, one question at a time, in this order: target role, time budget, relationship/ownership, current knowledge, and desired outcome. Do not repeat information the user already supplied.

- If the user requests no questions or time is too short, record each missing item as `pending confirmation`, state the conservative assumption, and continue. Never manufacture missing personal work, knowledge, runtime results, or metrics.
- Record the boundary in `00-study-brief.md`: what will be learned and defended, what will be skipped, and the truthful acceptance criteria.
- Default to an open-source study, a three-day schedule of 4–6 hours per day, and Java backend plus AI Agent comparisons only when the user has not set those values. Defaults are planning assumptions, not project facts.
- Keep upstream capability, source observation, and personal work separate. Reject wording that claims authorship, contribution, reproduction, ownership, leadership, implementation, or performance results without a matching personal artifact.

## Take a lightweight inventory

Spend 30–60 minutes obtaining structural evidence; do not begin a file-by-file repository tour. From this Skill directory, run the read-only scanner:

```text
python scripts/project_inventory.py <project-root>
```

Use its JSON only as an inventory, then inspect the relevant README/architecture/deployment documents, manifests, entrypoints, routes or controllers, migrations/models, tests, and recent commits. Capture only source anchors needed to bound likely claims and chains.

- If startup fails, retain the static inventory and record the failed command, error, and the smallest next action; do not infer runtime behavior.
- If secrets, API keys, or external services are missing, do not bypass them or invent a run. Mark runtime behavior, production behavior, and metrics `pending confirmation`.
- If documentation conflicts with source, privilege the precise source anchor for implementation facts; record the document claim and conflict as unresolved until checked.
- If evidence conflicts, preserve both Evidence records, lower confidence to `reasonable inference` or `pending confirmation`, and do not promote the affected Claim.

## Draft the resume first

Read [the claim rubric](references/resume-claim-rubric.md) and [the output templates](references/output-templates.md) before drafting. Create `01-resume-draft.md` as the first substantive output, immediately after the lightweight inventory; use the template's exact headings and stable `C#`/`E#` links.

Draft 3–4 bounded Claims in the rubric's positive shape. Each has separate fields for upstream capability, source observation, personal work, evidence, state, and the smallest next action. Until a real personal artifact exists, write **`No personal work claimed.`** and keep the Claim below `Verified` and `Ready`.

When personal work is `No personal work claimed.`, write the Claim statement as a neutral repository observation (for example, `The source exposes ...`), not as a completed learner action. Do not use `studied`, `researched`, `traced`, `organized`, `deployed`, `verified`, `reproduced`, `analyzed`, `compared`, or other completion verbs for the learner until the matching personal artifact is recorded.

For a configuration-driven Claim, trace the selected flow to its invocation site. Record a type or library default separately from any route, service, or caller override; never present a default as the applied setting without evidence that the selected flow uses it.

For a failure or boundary Claim, trace the exact selected call site and operator. Distinguish an error returned or propagated with `?` from a panic or `expect`, fallback/default behavior, logged or swallowed errors, and ignored results; do not collapse these into a generic failure claim.

Build a resume-first evidence plan for each Claim before wider study:

1. Choose one small attributable action (for example, a bounded run, reproduction, experiment, user-explained diagram, or code artifact).
2. Name the required artifact, command/result or explanation, and its Evidence ID.
3. Name one source anchor and one edge/failure question to investigate.

When a request pressures immediate bullets and asks what code to study, use this output order: submission status; 3–4 truthful `Draft` Claims; a claim-by-claim evidence plan naming each attributable action and artifact; then a short, source-anchor study order that directly supports those actions. This is the required resume-first shape.

Do not label draft source-study bullets `Ready`, `interview-ready`, copy-ready, or ready to submit. A conditional future warning is not current verification. If an unsupported claim cannot be narrowed to a truthful study observation, mark it `Dropped`; if a concrete constraint prevents evidence, mark it `Blocked` with its smallest unblocking action.

## Turn claims into a study plan

Create `02-claim-contracts.md` from the exact template. For each retained Claim, specify why it matters, a source anchor, input/output/state flow, an edge case, an alternative or trade-off, a clearly labeled Java mapping, three follow-ups, and the missing Ready gates.

Read [the backend and Agent topic map](references/backend-agent-topic-map.md) after the inventory. Explain the source implementation first; only then state a Java/Spring or Agent comparison. A comparison is never a repository fact.

- Select about three distinct core chains and rank 5–8 source-anchored topics using the guide's evidence gate. Weak clues stay backlog; if fewer than five implementation topics exist, use the exact scoped `Absent capability` fallback only to fill through five.
- Allocate the three-day plan: day 1 inventory, draft, contracts, and chains; day 2 source traces, evidence cards, and mappings; day 3 practice, remediation, pitch, and finalization. With less time, preserve one attributable action and the highest-evidence chains, reduce breadth, and withhold unfinished claims rather than compressing verification.
- Create `03-project-map.md` and `04-evidence-cards.md` using the routed template. Assign Evidence IDs in recording order and state both what each record establishes and what it does not establish.

## Build source evidence and mappings

For each selected chain, trace one bounded path from input through entry point, orchestration/service or Agent boundary, tools/external dependencies or persistence, and response/artifact. Record file, symbol, inputs, outputs, state changes, sync/async/streaming boundary, failure behavior, and confidence in `03-project-map.md` and `04-evidence-cards.md`.

Read [the backend and Agent topic map](references/backend-agent-topic-map.md) for source-evidence requirements, ranked topic selection, missing-capability handling, and the source-first Java comparison. Create `05-java-agent-mapping.md` with the template.

- For a non-Java repository, faithfully name the actual source language/framework and behavior. Put Java/Spring material in a separate **Java mapping** field headed as a conceptual comparison; never rewrite source facts as Spring Boot, WebFlux, JPA, or other Java implementation facts.
- Do not infer Agent loops, context stores, tools, streaming, retries, transactions, caches, queues, tests, metrics, or safety controls from a dependency, README, or familiarity. If a focused search finds none, use the exact `Absent capability` marker plus inspected scope.
- Personal verification may support a Claim only when its artifact is recorded with scope and limitation. Source inspection alone does not prove personal work, runtime behavior, production use, reliability, or performance.

## Drill, score, and finalize

Read [the question depth guide](references/question-depth-guide.md) before practice. Create `06-question-tree.md`, `07-project-pitch.md`, and `08-mastery-report.md` with [the output templates](references/output-templates.md).

Ask exactly one source-grounded question at a time, wait for the answer, assess it, record the correction/next action, and only then ask a later atomic question. Start at the lowest unsupported level and stop escalation at the first evidence gap; never substitute a plausible Java or Agent answer for missing source evidence.

Use the guide's fixed scores: accuracy 30%, source evidence 30%, expression 20%, and trade-offs 20%. A Claim is `Ready` only when every rubric gate is recorded: source anchor, personal artifact, edge case, Java mapping, alternative/trade-off, three follow-ups, and interview evidence check with total at least 80% and source evidence at least 70%.

Create `09-resume-final.md` only from `Ready` Claims and use the template's exact no-Ready withholding text when none pass. The final resume must retain the verified relationship framing (or `open-source study` only when no other relationship is evidenced) and must not include IDs, lifecycle states, learning tasks, evidence notes, source-path notes, score records, unsupported ownership, invented stack/runtime facts, or invented metrics.

