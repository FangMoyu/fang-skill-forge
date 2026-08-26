---
name: grilling-resume-projects
description: Use when a user wants iterative campus-recruitment or resume-project mock interviews, asks to be grilled on a project, or wants source-backed follow-up questions after answering one question at a time.
---

# Grilling Resume Projects

Conduct a resume-first project interview in which the candidate answers one question before receiving source-grounded feedback.

## Core rules

- Ask exactly one formal question, then wait.
- Frame the initial question from the resume or the candidate's project description. Do not reveal source class or method names in the prompt.
- After the answer, distinguish resume claims, source observations, attributable personal work, and proposed optimizations.
- Never invent implementation, ownership, production use, benchmarks, middleware, or reliability behavior.
- Always provide a complete reference answer, even when the candidate is correct, incomplete, says “不会”, or asks directly for the answer.
- Do not ask the next formal question in the same turn as feedback.

**REQUIRED SUB-SKILL:** Use `prepare-project-interview` when project source is available or resume/source alignment is requested. Source inspection supports implementation facts but does not prove personal contribution or runtime metrics.

Before asking or assessing any interview question, read [references/interview-contract.md](references/interview-contract.md) completely and follow its question, scoring, answer, difficulty, and persistence contracts.

## Session setup

Use information already supplied. Ask for only the smallest missing prerequisite, one question at a time: resume/project description, source location when source review is requested, target role, then current familiarity.

Start at difficulty tier 1 unless prior answers establish a higher tier or the user explicitly chooses one. Keep the current topic, tier, question number, and score history in session state.

## Persistence

Persist records only when the user requests it or an interview-preparation package already exists for the current project. Do not write to Desktop or another external location without explicit authorization.

