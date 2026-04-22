---
description: "Prioritize a list of opportunities, features, or initiatives using structured scoring. Supports RICE and impact/effort frameworks."
agent: "agent"
argument-hint: "List of items to prioritize, or 'help me identify items'"
tools: [read, search]
---

# Prioritization Framework

Score and rank a set of opportunities, features, or initiatives using a structured framework. Choose the framework that fits:

## Framework Options

### RICE (for feature/initiative prioritization)
- **Reach**: How many users/customers affected per quarter?
- **Impact**: How much does it move the needle per user? (3=massive, 2=high, 1=medium, 0.5=low, 0.25=minimal)
- **Confidence**: How sure are we about reach and impact? (100%=high, 80%=medium, 50%=low)
- **Effort**: Person-months to implement
- **Score**: (Reach × Impact × Confidence) / Effort

### Impact/Effort (for quick prioritization)
- Plot items on a 2×2 matrix: High Impact + Low Effort = Do First

## Process
1. List all items to prioritize
2. Score each item (ask user for input on unknowns)
3. Rank by score
4. Sense-check: does the ranking feel right? If not, examine which dimension is off

## Output Format

## Prioritization: [Context]

### Scored Items (RICE)

| # | Item | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---|------|-------|--------|------------|--------|-----------|------|
| 1 | ... | ... | ... | ... | ... | ... | ... |

### Recommended Priority Order
1. **[Item]** — [1-sentence why it's #1]
2. **[Item]** — [1-sentence rationale]
3. **[Item]** — [1-sentence rationale]

### Cut Line
Items below rank [X] should not be pursued this quarter. Rationale: [why]

### Key Trade-offs
- [Trade-off 1: what you gain and lose by this ranking]
- [Trade-off 2]
