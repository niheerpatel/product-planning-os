---
name: rfq-intelligence
description: "Analyze a multi-document RFQ package to extract instructions, scope, decision criteria, and cross-functional implications for PM, engineering, sales, and leadership."
argument-hint: "Path to RFQ folder (or extracted markdown folder)"
---

# RFQ Intelligence

Build an evidence-based understanding of what the customer is asking for, how they will evaluate responses, and what must be submitted.

## When to Use
- Preparing a first-pass RFQ readout for leadership and bid/no-bid decisions
- Aligning product, architecture, purchasing, and sales on RFQ scope and constraints
- Converting large RFQ packages (PDF, XLSX, PPTX, ZIP references) into actionable requirements
- Identifying ambiguities, conflicts, and missing information before drafting a response

## Procedure

### Step 1: Build Source Inventory and Precedence
List all RFQ artifacts and classify each as primary RFQ, requirements, compliance template, commercial terms, SOW, or references.
Set version precedence rules (latest wins unless RFQ explicitly states otherwise).

### Step 2: Extract Documents to Markdown
Use repository extraction scripts to parse binary files into markdown and images.
If a file is protected/encrypted, label it as blocked and record what can still be observed (file type, wrapper, metadata, protection notice).

### Step 3: Parse Explicit RFQ Instructions
From primary RFQ and related artifacts, capture:
- submission deadline and timezone
- submission format and channel
- mandatory attachments/forms
- Q&A process and contact path
- evaluation process and gating criteria
- legal/commercial constraints and assumptions

### Step 4: Build Requirement Taxonomy
Create a unified requirement set across platform, SDK, domain-specific modules, and references.
Tag each requirement as Mandatory, Conditional, Optional, or Informational.

### Step 5: Apply Three Role Lenses
For each major requirement cluster, summarize impact by role:
- Program manager: schedule, milestones, dependencies, governance
- Automotive purchaser: commercial model, terms, supplier obligations, compliance evidence
- Automotive system architect: interfaces, performance/safety/security constraints, integration risks

### Step 6: Label Evidence Quality
For every key claim, label as Evidence, Inference, or [ASSUMPTION], and include source, date/version, methodology, and confidence.

### Step 7: Produce Decision-Ready Outputs
Generate an instruction brief, requirement matrix, risk register, and executive summary.
Clearly separate what is known versus blocked due to protection/access constraints.

## Output
- RFQ instruction brief (deadline, format, must-submit list, process)
- Requirement traceability matrix with source references
- Cross-functional impact view (PM, purchasing, architecture)
- Ambiguity and blocker log with owner and next action
- Executive one-page summary for leadership decision review
