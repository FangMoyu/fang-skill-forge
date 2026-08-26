# Resume claim rubric

Use this reference to keep the project relationship, source implementation facts, and the user's work separate. A Claim is a proposed resume statement. Evidence is a source anchor or personal artifact that supports a Claim. A source inspection alone does not establish personal work, runtime behavior, production use, or metrics.

## Identity and lifecycle

- Assign Claim IDs in creation order: `C1`, `C2`, `C3`, and so on. Never reuse or renumber an ID; mark obsolete work `Dropped` instead.
- Assign Evidence IDs in recording order: `E1`, `E2`, `E3`, and so on. An Evidence record may support multiple Claims.
- Keep both IDs unchanged in `01-resume-draft.md` through `08-mastery-report.md`. A claim must cite its Evidence IDs; evidence must cite its related Claim IDs.
- Record the project as an **open-source study** when the user has not supplied evidence of a different relationship. Preserve an evidenced author, contributor, maintainer, employee, or owner relationship in `00-study-brief.md`, `01-resume-draft.md`, `07-project-pitch.md`, and `09-resume-final.md`.
- Relationship evidence establishes only that relationship. It does not establish work on any feature, ownership of a module, runtime results, or metrics; keep each such personal-work claim separately evidenced and bounded.

| State | Meaning | Permitted next step |
| --- | --- | --- |
| `Draft` | A useful but unproven statement; it is not resume-ready. | Find a source anchor and narrow the claim. |
| `Understood` | The user can locate the source implementation and explain the relevant flow. | Record personal verification and an edge case. |
| `Verified` | Source facts and a personal artifact support the bounded statement. | Practice follow-ups and complete the Ready gate. |
| `Ready` | Every Ready gate below is recorded and the claim can appear in the final resume. | Copy only the supported, bounded statement. |
| `Blocked` | Evidence is unavailable because of a concrete constraint. | State the constraint and smallest unblocking action. |
| `Dropped` | The claim is inaccurate, too broad, or not worth further work. | Preserve the ID and omit it from final output. |

`Blocked` and `Dropped` never become `Ready` without new recorded evidence and a fresh gate check.

## Ready gate

Mark a Claim `Ready` only when all of these are explicit in its record:

1. **Source anchor:** a precise source implementation location and an explanation of the relevant input, output, and state flow.
2. **Personal artifact:** a recorded personal run, reproduction, experiment, diagram explained by the user, or code artifact. State what the artifact proves and does not prove.
3. **Edge case:** one failure, boundary, retry, fallback, or other non-happy-path explanation tied to the claim.
4. **Java mapping:** an explicit conceptual Java/Spring comparison, clearly separate from the source implementation.
5. **Alternative or trade-off:** at least one credible alternative and why the observed design differs.
6. **Three follow-ups:** the user can answer three recorded follow-up questions about why, source location, failure handling, Java mapping, or optimization without inventing facts.
7. **Interview evidence check:** record accuracy, source-evidence, expression, and trade-off scores; require both an overall score of at least 80% and a source-evidence score of at least 70%.

A failed score threshold leaves the claim `Verified` or lower. A missing gate means the claim is not `Ready`.

## Truthful claim shape

Write a draft entry in this positive shape:

```text
C#: [verified relationship framing, or open-source study] — [bounded source observation].
Personal work: [only the completed, evidenced action; otherwise “No personal work claimed.”]
Evidence: [E# ...] | State: [lifecycle state] | Next action: [smallest attributable action]
```

Keep three fields distinct:

- **Upstream capability:** what the source implementation provides.
- **Source observation:** what the user can point to and explain.
- **Personal work:** only the user’s completed, evidenced action.

Use `studied`, `researched`, `traced`, `organized`, `deployed`, `verified`, `reproduced`, `analyzed`, or `compared` only for work the user actually did. Use `implemented`, `extended`, `refactored`, `optimized`, or `designed` only when the user has a matching code, experiment, or comparison artifact. Do not describe a Java mapping as a source implementation fact.

Do not use unsupported ownership wording such as `led`, `owned`, `responsible for the core module`, `independently completed`, `built`, or `architected`. Do not invent or imply unsupported latency, throughput, cost, reliability, user, production, or percentage improvements. Do not claim authorship, contribution, reproduction, or personal practice that the evidence record does not establish.

