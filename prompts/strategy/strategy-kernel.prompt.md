---
description: "Build a complete strategy kernel in one pass — diagnosis, guiding policy, and coherent actions. The most comprehensive strategy formulation prompt."
agent: "agent"
argument-hint: "Product, situation, or challenge to strategize about"
tools: [read, search, web]
---

# Full Strategy Kernel

Build a complete Good Strategy kernel (Rumelt) in a single structured pass. This prompt walks through all three elements: diagnosis, guiding policy, and coherent actions.

## Process

### Step 1: Gather Context
- Review any product context files in the workspace (`products/*/product-context.md`, `products/*/strategy-kernel.md`)
- Review competitive analysis if available (`competitive-analysis/` repo)
- Ask the user for any additional context needed

### Step 2: Diagnosis
- What is the core challenge? What's really going on?
- Simplify to the 2-3 most critical factors
- Name the real obstacle — don't avoid uncomfortable truths

### Step 3: Guiding Policy
- What approach addresses this challenge?
- This must be a METHOD, not a goal
- What does this policy rule out?

### Step 4: Coherent Actions
- What specific, coordinated steps carry out the policy?
- How do they reinforce each other?
- Are they feasible with current resources?

### Step 5: Bad Strategy Check
- Scan the output for the four hallmarks of bad strategy (fluff, avoiding the challenge, goals-as-strategy, dog's dinner objectives)
- Fix any issues before presenting

## Output Format

# Strategy Kernel: [Product/Situation Name]

## Diagnosis
**The core challenge**: [2-3 sentences]

**Key factors**:
- [Factor with evidence]
- [Factor with evidence]
- [Factor with evidence]

## Guiding Policy
**Our approach**: [Clear, specific approach that rules out alternatives]

**What this rules out**: [Explicitly named alternatives we're NOT pursuing]

## Coherent Actions

| # | Action | Why | Owner | Timeline |
|---|--------|-----|-------|----------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

**Coordination logic**: [How actions reinforce each other]

## Assumptions & Risks
| Assumption | Evidence level | How to validate |
|------------|---------------|----------------|
| ... | ... | ... |

## Next Steps
- [ ] [Specific, assignable, time-bound action]
- [ ] [Specific, assignable, time-bound action]
