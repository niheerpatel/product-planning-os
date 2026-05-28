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
- Comparing competitors where level of technology investment affects execution speed or defensibility

## Procedure

### Step 1: Define the Research Question
Clarify with the user:
- What specifically do you want to learn?
- What decisions will this research inform?
- What do you already know (to avoid redundant research)?

### Step 2: Search Existing Workspace Data
- Check `products/*/product-context.md` for existing market context
- Check `competitive-analysis/` for competitive data that provides market signals
- Check `sample-product-data/` for any raw research already gathered

### Step 3: Conduct Web Research
Use web search to gather data from:
- Industry analyst reports (Gartner, McKinsey, Forrester, IDC)
- Market data providers (Statista, Grand View Research)
- Trade publications and industry news
- Company filings and press releases
- Academic and government sources

### Step 4: Synthesize Findings
Organize research into the standard output format below. For every data point:
- Cite the source with date
- Rate confidence (High/Medium/Low)
- Label as Evidence or Inference

When competitors are part of the analysis, include a technology investment assessment:
- Identify company-level and product-level investment signals (funding rounds, R&D spend, acquisition cadence, hiring scale, infrastructure buildout, program-level budget where available)
- Separate audited/disclosed values from estimates
- Add a comparability caveat if one firm has company-level data and another only has program-level data
- Assign an investment level rating (e.g., Low / Moderate / High / Very High) with confidence

### Step 5: Identify Gaps
What couldn't you find? What requires primary research? What assumptions need validation?

## Output Format

# Market Research: [Topic]

**Research question**: [What we're trying to learn]
**Date**: [Research date]
**Confidence**: Overall High / Medium / Low

## Market Overview
[2-3 paragraph summary of key findings]

## Market Size
| Metric | Value | Source | Date | Confidence |
|--------|-------|--------|------|-----------|
| TAM | ... | ... | ... | ... |
| SAM | ... | ... | ... | ... |
| SOM | ... | ... | ... | ... |
| Growth rate | ... | ... | ... | ... |

## Key Trends
| Trend | Evidence | Implication for us | Source |
|-------|---------|-------------------|--------|
| ... | ... | ... | ... |

## Customer Segments
| Segment | Size | Pain points | Willingness to pay | Our fit |
|---------|------|------------|--------------------|---------| 
| ... | ... | ... | ... | ... |

## Technology Investment Assessment (for competitive analyses)
| Company | Investment signal | Scope (Company or Product) | Evidence type | Investment level | Confidence | Comparability caveat |
|---------|-------------------|----------------------------|---------------|------------------|------------|----------------------|
| ... | ... | ... | Audited / Disclosed / Estimated | ... | ... | ... |

## Research Gaps
- [What we still don't know and how to find out]

## Sources
- [Full source list with URLs and access dates]
