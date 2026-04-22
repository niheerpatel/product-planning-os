---
description: "Track and manage product hypotheses through the discovery process. Create, update, and evaluate hypothesis cards."
agent: "agent"
argument-hint: "Hypothesis to track, or 'review' to assess existing ones"
tools: [read, search, edit]
---

# Hypothesis Tracker

Manage product hypotheses through the Productside discovery process. Every insight should be captured as a testable hypothesis before committing resources.

## Hypothesis Card Format

### Hypothesis: [Short name]
- **Statement**: We believe that [target user] has [problem/need] because [reason], and if we [intervention], we will see [measurable outcome].
- **Phase**: Investigation / Validation / Validated / Invalidated
- **Evidence for**:
  - [Source, date]: [Finding]
- **Evidence against**:
  - [Source, date]: [Finding]
- **Confidence**: High / Medium / Low
- **Next test**: [How to get more evidence]
- **Decision threshold**: [What evidence would make us act on this?]

## When Creating New Hypotheses
1. Frame as testable "we believe... because... if we... then..." statements
2. Identify what evidence would validate OR invalidate
3. Set a confidence level based on current evidence
4. Define the next cheapest test

## When Reviewing Existing Hypotheses
1. Read the current hypothesis log from the product's `discovery-log.md`
2. Assess each hypothesis against new evidence
3. Update confidence levels
4. Recommend which hypotheses to pursue, pivot, or kill
5. Flag hypotheses stuck in "investigation" too long without new evidence
