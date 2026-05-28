---
name: market-research
description: "Conduct structured market research using web sources and workspace data. Use when investigating market size, trends, customer segments, or industry dynamics for product planning."
argument-hint: "Research question or market to investigate"
---

# Market Research

Conduct structured, evidence-based market research with clear source attribution and confidence ratings.

## When to Use
- Sizing a market (TAM/SAM/SOM)
- Investigating industry trends
- Understanding customer segments
- Evaluating market dynamics and entry barriers
- Comparing competitors where technology investment level influences execution advantage

## Procedure

### Step 1: Define the Research Question
Clarify with the user:
- What specifically do you want to learn?
- What decisions will this research inform?
- What do you already know?

### Step 2: Search Existing Workspace Data
- Check `products/*/product-context.md` for existing market context
- Check `competitive-analysis/` for competitive data and market signals
- Check `sample-product-data/` for raw research already gathered

### Step 3: Conduct Web Research
Use web sources for:
- analyst reports, market studies, and industry news
- customer segment descriptions and buying behavior
- competitor positioning and market share signals

### Step 4: Synthesize Findings
For each data point:
- cite the source with date
- rate confidence (High/Medium/Low)
- label Evidence vs Inference

When doing competitive analysis, add a technology investment assessment:
- capture investment signals such as funding, R&D spend, acquisition activity, hiring scale, infrastructure investment, and program-level spend
- distinguish audited/disclosed figures from estimates
- note comparability limitations (for example, company-level data vs product-level data)
- assign investment level with confidence

### Step 5: Identify Gaps
- What is missing?
- What requires primary research?
- What assumptions need validation?

## Output Format

# Market Research: [Topic]

**Research question**: [What we're trying to learn]
**Date**: [Research date]
**Confidence**: Overall High / Medium / Low

## Market Overview

## Market Size

## Key Trends

## Customer Segments

## Technology Investment Assessment (competitive analysis)
| Company | Investment signal | Scope (Company or Product) | Evidence type | Investment level | Confidence | Comparability caveat |
|---------|-------------------|----------------------------|---------------|------------------|------------|----------------------|
| ... | ... | ... | Audited / Disclosed / Estimated | ... | ... | ... |

## Research Gaps

## Sources
