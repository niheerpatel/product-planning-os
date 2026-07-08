---
description: "Write one or more Jira capabilities using a fixed template: Capability Name, User Story, Objective, Acceptance Criteria, Definition of Done."
agent: "agent"
argument-hint: "Capability scope, persona, platforms, and intended outcomes"
tools: [read, search]
---

# Capability Builder

Generate Jira-ready capabilities that are clear, measurable, and release-oriented.

## Instructions
1. Use plain language understandable to non-LINC engineers.
2. Use this exact user story grammar:
As a <job title>, I want <action / capability> so that I can <business outcome>
3. For each capability, include all template fields.
4. Write measurable acceptance criteria (include thresholds or pass/fail conditions).
5. Write a concrete definition of done covering implementation, integration, docs, and release readiness.
6. Mark supporting claims with [EVIDENCE], [ASSUMPTION], or [INFERENCE] when presenting rationale.
7. If both MPU and MCU are in scope, include a scope label:
- Scope Lane: MPU Committed
- Scope Lane: MCU Stretch (Q3 target)

## Output Format

Capability Name: <Concise, descriptive, and understandable to a non-LINC engineer>

User Story: As a <job title>, I want <action / capability> so that I can <business outcome>

Objective: <What outcomes the capability enables once complete>

Acceptance Criteria:
1. <Measurable condition or KPI>
2. <Measurable condition or KPI>
3. <Measurable condition or KPI>

Definition of Done:
1. <Condition that proves implementation is complete>
2. <Condition that proves integration is complete>
3. <Condition that proves documentation and user guidance are complete>
4. <Condition that proves release readiness>

## Optional Add-On Sections
- Dependencies:
1. <Dependency>
- Risks:
1. <Risk and mitigation>
- Non-Goals:
1. <Explicit exclusion>
