---
name: rfq-response-validation
description: "Validate an RFQ response package against a weighted rubric for technical compliance, commercial competitiveness, delivery feasibility, strategic fit, and evidence traceability."
argument-hint: "Path to extracted RFQ package plus draft response artifacts"
---

# RFQ Response Validation

Score and stress-test an RFQ response before submission using explicit pass/fail gates and weighted scoring.

## When to Use
- Pre-submission quality gate for an RFQ response package
- Red-team review of technical, commercial, and delivery claims
- Executive readiness review with objective scoring and remediation actions
- Comparing multiple draft responses or partner options using the same rubric

## Proposed Rubric (Default Weights)
| Dimension | Weight | Pass/Fail Gate |
|---|---:|---|
| Technical compliance completeness | 35% | All mandatory requirements addressed with explicit response status |
| Commercial competitiveness | 20% | Pricing model, assumptions, and commercial terms are internally consistent |
| Delivery feasibility and risk | 20% | Plan includes milestones, dependencies, staffing model, and risk mitigations |
| Strategic fit to customer intent | 15% | Response maps to customer outcomes and stated strategic priorities |
| Evidence strength and traceability | 10% | Major claims cite source evidence, ownership, and confidence |

## Procedure

### Step 1: Load Baseline RFQ Requirements
Use RFQ instruction brief and requirement matrix as the canonical baseline.
Reject validation if baseline is incomplete or untrusted.

### Step 2: Build Coverage Map
Map each requirement to one or more response sections.
Mark each row as Covered, Partially Covered, Not Covered, or Not Applicable (with justification).

### Step 3: Evaluate Pass/Fail Gates
Check hard gates first:
- mandatory requirements covered
- required forms/attachments present
- no contradictory commercial assumptions
If any hard gate fails, mark overall status as Red and list blockers.

### Step 4: Score Weighted Dimensions
Score each rubric dimension from 0 to 5:
- 0 = absent
- 1 = weak
- 2 = partial
- 3 = acceptable
- 4 = strong
- 5 = compelling
Convert to weighted score out of 100.

### Step 5: Generate Compliance Heatmap
Create a heatmap by requirement cluster and rubric dimension:
- Green: strong and evidenced
- Yellow: partial or weak evidence
- Red: missing, conflicting, or high risk

### Step 6: Assign Remediation Actions
For every Red/Yellow item, assign:
- owner
- corrective action
- due date
- expected score lift

### Step 7: Publish Validation Pack
Publish final status (Green/Yellow/Red), weighted scorecard, blocker list, and executive recommendation.

## Output
- Weighted RFQ response scorecard with pass/fail gate results
- Requirement-level compliance map and gap list
- Compliance heatmap for rapid triage
- Remediation plan with owners, due dates, and expected impact
- Submission-readiness recommendation for leadership
