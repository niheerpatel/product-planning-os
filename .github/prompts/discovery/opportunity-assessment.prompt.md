---
description: "Assess a product opportunity using structured scoring. Evaluates market size, customer pain, feasibility, and strategic fit."
agent: "agent"
argument-hint: "Describe the opportunity to assess"
tools: [read, search, web]
---

# Opportunity Assessment

Evaluate a product opportunity using structured criteria. This helps decide whether an opportunity is worth pursuing and how to prioritize it against alternatives.

## Scoring Criteria

| Dimension | Weight | 1 (Low) | 3 (Medium) | 5 (High) |
|-----------|--------|---------|------------|----------|
| **Customer pain** | 30% | Nice-to-have | Painful workaround exists | Hair-on-fire, no good solution |
| **Market size** | 20% | Niche (<$10M TAM) | Mid-market ($10-100M) | Large (>$100M TAM) |
| **Strategic fit** | 20% | Tangential to strategy | Supports guiding policy | Core to guiding policy |
| **Feasibility** | 15% | Requires new capabilities | Stretches current capabilities | Within current capabilities |
| **Competitive advantage** | 15% | Many competitors, no moat | Some differentiation | Unique position or defensibility |

## Process
1. Gather context on the opportunity (ask user or search workspace)
2. Score each dimension with evidence-backed reasoning
3. Calculate weighted score
4. Provide recommendation

## Output Format

## Opportunity: [Name]

**One-line summary**: [What is this opportunity?]

| Dimension | Score (1-5) | Rationale | Evidence type |
|-----------|-------------|-----------|---------------|
| Customer pain | ... | ... | Evidence / Assumption |
| Market size | ... | ... | Evidence / Assumption |
| Strategic fit | ... | ... | Evidence / Assumption |
| Feasibility | ... | ... | Evidence / Assumption |
| Competitive advantage | ... | ... | Evidence / Assumption |

**Weighted score**: X.X / 5.0

**Recommendation**: Pursue / Investigate further / Pass

**Key unknowns**: [What would change the score most if validated?]

**Cheapest next test**: [Smallest investment to reduce uncertainty]
