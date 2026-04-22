---
description: "Extract key insights from raw research documents. Pulls out quotes, findings, data points, and organizes them by theme."
agent: "agent"
argument-hint: "Paste content or reference a file to extract insights from"
tools: [read, search, edit]
---

# Extract Insights

Pull structured insights from raw research content (interview notes, survey results, articles, reports). This transforms unstructured text into organized, referenceable findings.

## Process
1. Read the provided content
2. Identify and extract: key findings, direct quotes, data points, surprises
3. Categorize by theme
4. Label each as evidence or inference
5. Rate significance

## Output Format

# Insights: [Source Description]

**Source**: [Document name, author, date]
**Extracted by**: AI-assisted extraction — verify all quotes against source

## Key Findings
| # | Finding | Type | Significance | Theme |
|---|---------|------|-------------|-------|
| 1 | ... | Evidence / Inference | High/Med/Low | ... |

## Direct Quotes
| Quote | Speaker/Source | Context | Theme |
|-------|--------------|---------|-------|
| "..." | ... | ... | ... |

## Data Points
| Metric | Value | Source | Date | Confidence |
|--------|-------|--------|------|-----------|
| ... | ... | ... | ... | High/Med/Low |

## Surprises & Contradictions
- [Anything unexpected or that contradicts prior assumptions]

## Implications
- [What should we do differently based on these findings?]

## Questions Raised
- [What new questions does this evidence prompt?]
