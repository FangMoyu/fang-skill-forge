---
name: project-resume-visual-interview-kit
description: Create a source-grounded project resume, plain-language business-flow diagrams, and campus-interview grilling materials from one or more project repositories.
---

# Project Resume, Business Diagram, and Interview Kit

Use this skill when a user wants to turn a project resume description and its source code into a reusable interview-ready package. It is designed for Java backend and Agent projects, but first describe the repository's actual language and behavior. A companion repository may be used for comparison; do not silently merge its capabilities into the primary project.

## Outcome

Produce a coherent package that a candidate can read before an interview:

- a 30–90 second project introduction and a bounded copy-ready resume draft;
- 5–6 highest-value resume claims, selected for distinct interview coverage;
- one or more user-facing business flow or use-case diagrams, starting at a user click or other real entry action;
- a plain-language explanation of each diagram and each resume claim;
- a source-grounded grilling handbook with questions, common traps, complete reference answers, short answers, recall lines, formulas, source anchors, and verification actions;
- a truthfulness and verification checklist.

Do not create a claim merely because the project dependency, README, design document, or a related project suggests it. Distinguish four layers throughout: resume claim, source observation, personal contribution, and proposed future design.

## Required source-first workflow

1. Identify the primary repository, any comparison repository, the target role, time budget, and the requested output location. Ask only for information that cannot be safely inferred; otherwise state the conservative assumption.
2. Perform a lightweight inventory with `rg --files` and inspect the README, build manifest, entry points/routes, persistence/migrations, relevant services or agents, tests, deployment files, and recent source evidence. Do not replace this with an unbounded file tour.
3. Select 5–6 claims. Prefer one central user flow and distinct boundaries such as state, retrieval, persistence, reliability, streaming, security, or evaluation. Merge duplicate claims instead of filling space with generic technology names.
4. Trace every selected claim from a real input through orchestration, decision or Agent boundary, persistence/external dependency, output, and failure behavior. Record exact source anchors and confidence.
5. Draft the resume before expanding the explanation. Keep unsupported ownership, metrics, production use, and runtime behavior out of the draft. A source-only fact is not proof of personal work.
6. Create diagrams only for the selected business flows. When the user asks for Excalidraw, use the `excalidraw-diagram-generator` skill and follow its JSON/schema requirements. Keep diagram labels in ordinary business language: for example, “按明确标签找菜”, “检查是否属于你的菜单”, or “提示补充信息”. Do not put class, controller, mapper, service, package, or method names inside diagram nodes.
7. Build the grilling handbook from the resume claims, in this order for each topic: project value, implementation trace, relevant fundamentals, evidenced failure/boundary, and conditional optimization. Ask one formal question at a time during live practice; a bulk handbook is a study artifact, not evidence of answered questions.
8. Validate every local link, diagram JSON ID/binding, text font requirement, image path, question sequence, and document section. Run only checks appropriate to the requested artifact. Never manufacture a smoke test, benchmark, accuracy rate, or evaluation report.

## Claim selection and wording

Use 5–6 claims only when each contributes distinct interview value. A strong claim names the business concern, mechanism, boundary, and result shape without promising an outcome that was not measured.

Prefer:

> “将正式菜单与可重建的语义查找资料分开，提交后异步更新；查找结果回到真实菜单核对。”

Avoid:

> “保证跨库最终一致、任意故障不中断、准确率提升 30%。”

For every claim, state whether it is code-backed, tested, runtime-verified, personally reproduced, or only proposed. If a known defect affects the selected path, surface it in the explanation and narrow the claim rather than hiding it.

## Diagram guidance

Use a small number of readable diagrams instead of one crowded architecture map. A useful set often includes:

- “点击发送后会发生什么”：user action, menu scope, task routing, clarification/recommendation, response;
- “推荐为什么是这几道菜”：explicit-condition search, meaning-based search, fact/ownership check, filtering, ranking, response;
- “保存菜单后发生什么”：save the real menu first, background search-material update, success/failure boundary;
- “智能服务出错怎么办”：call failure, alternate candidate, output validation, rules/templates;
- “下一句话怎样接上”：conversation coordination, structured state, recent context, summary, cursor;
- “反馈怎样帮助改进”：feedback, trace, annotation, batch evaluation, manual improvement.

Use colors consistently for user action, system processing, decisions, warnings, background jobs, and proposed future work. Mark proposed or unverified paths clearly. A diagram describes the business flow; it does not prove the flow has passed runtime acceptance.

## Grilling handbook format

For each question include: exact prompt, topic and difficulty, what it tests, common traps, a complete current-source-first answer, a short answer of at most 300 Chinese characters, a recall line of at most 80 Chinese characters, one compact memory formula, source anchors, and the smallest verification action. Label Java/Spring alternatives as comparisons and future designs as proposals.

For live grilling, use the companion `grilling-resume-projects` skill: ask exactly one formal question, wait, score accuracy/source evidence/expression/trade-offs, provide the complete feedback recipe, and only then choose whether to advance. A request to see the answer is not an independent pass.

## Verification and delivery

Keep raw project code untouched unless the user separately asks for implementation. Use a new output directory when the user requests a package. Copy diagrams and images without changing their content, and include an index or offline reader when it materially improves use.

Before declaring success, report what was validated and what was not. For a diagram package, validate JSON, unique IDs, arrow bindings, text font settings, image rendering, and navigation. For interview materials, validate question numbering, answer sections, source links, and that unperformed practice has no fabricated score. If the user requests desktop or another external location, obtain any required filesystem authorization immediately before copying and verify the copied files afterward.

## Related skills

- Read `prepare-project-interview` when source-level claim alignment and evidence contracts are needed.
- Read `grilling-resume-projects` for live one-question-at-a-time practice.
- Read `excalidraw-diagram-generator` when generating or validating Excalidraw diagrams.
- Read [references/package-template.md](references/package-template.md) when producing the full multi-document package.
- Read [references/claim-and-question-template.md](references/claim-and-question-template.md) when the user asks for exhaustive claim explanations or a grilling handbook.

