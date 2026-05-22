# Skills Directory

This repository uses a vendor-neutral `skills/` directory for reusable AI skill definitions.

## Purpose

- `skills/` is the primary home for capability definitions when using VS Code with different models such as Claude, Claude Code, or other LLM tools.
- `.github/skills/` is preserved for GitHub Copilot Chat compatibility, but it is secondary.

## Productside phase alignment

Skills are organized by Productside lifecycle phase:

- `skills/context/` — market research, competitive intelligence, document extraction, and product context discovery
- `skills/discover/` — customer interviews, hypothesis management, opportunity assessment
- `skills/define/` — problem framing, roadmap planning, pricing strategy, and solution definition
- `skills/create/` — prototype planning, experiment design, build-to-learn planning
- `skills/deliver/` — GTM planning, metrics frameworks, launch readiness
- `skills/iterate/` — learning reviews, retrospective analysis, strategy refresh

## How to use

- Use `skills/` for reusable capabilities that can be invoked by model integrations or assistant workflows.
- Use `prompts/` for individual slash commands and prompt templates.
- Use `agents/` for multi-step role-based workflows.

## Example

```
skills/
  context/
    market-research/SKILL.md
    document-extraction/SKILL.md
  discover/
    customer-interviews/SKILL.md
    hypothesis-tracking/SKILL.md
  define/
    problem-framing/SKILL.md
    roadmap-planning/SKILL.md
  create/
    prototype-planning/SKILL.md
  deliver/
    metrics-framework/SKILL.md
  iterate/
    learning-review/SKILL.md
```
