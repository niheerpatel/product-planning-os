---
name: jira-capability-spec
description: "Write Jira-ready capabilities with fields: Capability Name, User Story, Objective, Acceptance Criteria, and Definition of Done."
argument-hint: "Capability context, target users, and desired business outcomes"
---

# Jira Capability Spec

Convert strategy and roadmap intent into a delivery-ready capability spec for Jira.

## When to Use
- After strategy kernel and roadmap direction exist
- When preparing capability-level planning before story breakdown
- When you need consistent, measurable capability definitions across teams

## Required Input
1. Product or initiative context
2. Target persona and user journey
3. Scope boundaries and non-goals
4. Any known constraints (timeline, platforms, dependencies)

## Guardrails
1. Use this exact user story format:
As a <job title>, I want <action / capability> so that I can <business outcome>
2. Keep capability names understandable to non-LINC engineers.
3. Acceptance criteria must be measurable and testable.
4. Definition of done must include implementation, integration, and release readiness.
5. Label supporting statements as [EVIDENCE], [ASSUMPTION], or [INFERENCE] where relevant.
6. For dual-track efforts, tag scope clearly as MPU Committed or MCU Stretch.

## Procedure
1. Confirm the core challenge and desired outcome.
2. Draft one capability statement with explicit scope and exclusions.
3. Write user story and objective in plain language.
4. Define acceptance criteria with success thresholds.
5. Define done criteria with verification gates.
6. Check for bad-strategy patterns (goals without method, vague language, uncoordinated work).

## Output Template

Capability Name: <Concise, descriptive, understandable to non-LINC engineer>

User Story: As a <job title>, I want <action / capability> so that I can <business outcome>

Objective: <What outcomes the capability enables once complete>

Acceptance Criteria:
1. <Measurable condition or KPI>
2. <Measurable condition or KPI>
3. <Measurable condition or KPI>

Definition of Done:
1. <Implementation complete and reviewed>
2. <Integrated with dependent systems and validated>
3. <Documentation and evaluator guidance updated>
4. <Release readiness checks passed>

## Quality Check
1. Is the capability specific enough to execute but broad enough to contain multiple stories?
2. Are metrics explicit enough to confirm success objectively?
3. Does done criteria prevent ambiguous "almost complete" status?
4. Are assumptions clearly marked for follow-up validation?
