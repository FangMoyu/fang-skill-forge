# Backend and Agent topic map

Use this reference after a lightweight inventory and before choosing deep-dive
chains. It turns repository evidence into a ranked, interview-focused study
list. It does not assert that a repository has a Java stack, an Agent, or any
operational capability.

## Contents

- [Evidence-first selection](#evidence-first-selection)
- [Rank 5--8 topics](#rank-5--8-topics)
- [Topic coverage map](#topic-coverage-map)
- [Source implementation record](#source-implementation-record)
- [Java mapping record](#java-mapping-record)
- [Missing capabilities and truthfulness](#missing-capabilities-and-truthfulness)

## Evidence-first selection

Build a candidate row for every topic below from repository evidence: an entry
point, route or message boundary, configuration, data model, deployment
artifact, test, or directly related source symbol. Record the confidence as
`verified`, `reasonable inference`, or `pending confirmation`. Do not infer
runtime behavior from a dependency name, README claim, or a familiar
architecture.

Apply this selection gate before scoring or ranking:

- A **source-anchored implementation topic** has source-evidence score 2--4,
  a concrete `path : symbol` or equivalent implementation artifact, and a
  bounded observed concern. Only these topics enter the priority ranking.
- A no-anchor or weak-clue candidate (source-evidence score 0--1) is `pending
  confirmation`. Keep it in the backlog; it can never enter the ranked 5--8,
  regardless of its role relevance or hypothetical priority.
- A targeted search that finds no implementation is not a weak clue. Record
  the exact `Absent capability` marker and inspected scope. It is eligible
  only for the explicit five-topic fallback below, not for priority ranking.

Score only source-anchored implementation topics:

| Criterion | Range | What earns the score |
| --- | ---: | --- |
| Source evidence | 0--4 | 0 no anchor; 1 weak clue; 2 one concrete implementation anchor; 3 traceable flow; 4 entry-to-outcome flow with inputs, state, and boundary. |
| Target-role relevance | 0--4 | Importance for the stated backend and/or Agent role. |
| Flow centrality | 0--2 | How directly the topic connects a primary request, user-visible outcome, or important state transition. |
| Interview distinctiveness | 0--2 | Whether the observed design gives a concrete, defensible discussion rather than generic theory. |
| Study cost | 0--2 | 0 means bounded within the schedule; 2 means the evidence is too diffuse to defend soon. |

`Priority = source evidence + target-role relevance + flow centrality + interview distinctiveness - study cost`.
Use the score to order study time, not to claim quality or production impact.

## Rank 5--8 topics

1. Classify all eight topic groups with the selection gate. Put score-0/1
   `pending confirmation` candidates in the backlog before ranking.
2. Rank only source-anchored implementation topics by priority. Prefer distinct
   coverage of a core request flow and different boundaries (security, state,
   streaming, tool, or operations) over overlapping variants of one detail.
3. Start with the five highest-ranked distinct implementation topics. If fewer
   than five exist, retain every available implementation topic and fill only
   the remaining places through five with bounded, targeted-search topics that
   say `Absent capability` and identify the inspected scope. Never use a weak
   clue or no-anchor candidate as a filler.
4. Add a sixth, seventh, or eighth topic only in descending priority when it
   contributes distinct coverage and the three-day schedule has capacity after
   the first five. Stop at the first capacity or coverage limit, and never add
   a ninth topic. The absolute cap is 8 topics. `Absent capability` fallback
   topics fill up to five only.
5. For tied implementation scores, choose the clearer source anchor, then the
   closer target-role fit, then the lower study cost. Preserve all unselected
   implementation topics and every `pending confirmation` candidate as backlog.
6. Re-rank when new evidence appears. An absence marker can be replaced only
   by a concrete source anchor, not by a desired Java design.

Use this output shape:

```text
Rank N — [topic group] — Priority: [number] — [confidence]
Evidence: [path : symbol/configuration/test/deployment artifact]
Source implementation: [bounded observed flow, or Absent capability]
Study question: [one source-traceable question]
```

## Topic coverage map

| Topic group | Must inspect in the source implementation | Java mapping only after source explanation |
| --- | --- | --- |
| 1. HTTP boundary and identity | HTTP/RPC routes, request validation, error boundary, JWT/session parsing, security context, protected endpoints. | Spring MVC/WebFlux controllers, filters, validation, Spring Security resource-server/JWT context. |
| 2. Streaming and concurrency | SSE or other streaming protocol, event framing, cancellation, backpressure, async tasks, shared-state ownership. | WebFlux `Flux`/SSE, Reactor scheduling and cancellation; use Spring MVC only when the source is request/response. |
| 3. State, persistence, and integrity | Data models, repositories, migrations, persistence calls, transaction boundaries, connection-pool configuration, cache or queue integration. | JPA/MyBatis, `@Transactional`, datasource pooling, cache/queue clients only if the source has an equivalent concern. |
| 4. Configuration, observability, and deployment | Configuration loading, environment assumptions, logging, tracing/metrics hooks, health/readiness, container/build/deployment artifacts. | Spring configuration/profiles, Actuator, structured logging, container/Kubernetes deployment concepts. |
| 5. Agent loop and context | ReAct or other decision loop, model invocation, stop conditions, context assembly, memory/compression, prompt/state transitions. | A Java orchestration service/state machine; Spring AI or another library is a comparison, never a source fact. |
| 6. Tool execution and streaming | Tool registry, selection, argument validation, execution boundary, permissions, tool-result propagation, streamed model/tool events. | Typed tool interfaces, bean registry, validation, controlled async execution, SSE/WebFlux event translation. |
| 7. Reliability and evaluation | Timeouts, retry policy, idempotency keys, fallback, termination, evaluation harnesses, fixtures, test evidence. | Resilience4j/Spring retry, idempotency storage, circuit breaking, evaluation/test harnesses only as alternatives. |
| 8. Safety and policy boundary | Authentication/authorization checks, tool allowlists, input/output controls, data handling, audit trail, human approval. | Spring Security authorization, validation, policy enforcement, audit logging, and approval workflows. |

Every group is a coverage obligation, not proof that the capability exists.

## Source implementation record

For each selected topic, explain this section before discussing Java:

1. **Source anchor:** file, symbol, configuration, test, or deployment artifact.
2. **Observed flow:** input, control/data flow, output, and state transition.
3. **Boundary:** synchronous, asynchronous, streaming, external, security, or
   persistence boundary actually evidenced.
4. **Failure or limit:** observed handling, or `pending confirmation` when it
   is not evidenced.
5. **Confidence and scope:** what the evidence establishes and does not
   establish.

Do not call a static source inspection a production run. Do not turn a test
file, dependency, unused configuration key, or comment into proof of runtime
behavior.

## Java mapping record

Create a distinct section headed **Java mapping** only after the source record
is complete. State the mapping as a conceptual comparison:

```text
Java mapping: In a Java/Spring implementation, [observed source concern]
could be represented by [Java mechanism]. This is a comparison, not a fact
about the source repository.
```

Keep the mapping aligned with the observed boundary. For example, map an
observed reactive stream to WebFlux only after naming the source stream and its
cancellation/backpressure evidence; do not map an ordinary request/response
handler to WebFlux by default. State an alternative and trade-off when known.

## Missing capabilities and truthfulness

When a targeted search of the relevant source scope finds no implementation,
write the exact marker **`Absent capability`** followed by the scope searched:

```text
Source implementation: Absent capability — no transaction boundary found in
[inspected persistence/service scope].
```

An absence marker supports only a bounded statement about the inspected scope;
it does not prove repository-wide nonexistence unless the inventory supports
that conclusion. It may lead to a Java comparison or an interview discussion
of what would be needed, but never to a claim that the repository implements it.

Never fabricate Agent, cache, queue, transaction, retry, metric, or test
behavior. If evidence is missing, preserve the gap, lower confidence, and ask
for the next smallest source anchor or personal verification rather than
inventing a happy path, failure policy, benchmark, or production result.

