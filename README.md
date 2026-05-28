# Product Planning OS

An AI-powered product management operating system for structured strategy, discovery, and competitive work. Built on four frameworks: **Rumelt's Good Strategy** kernel, the **Productside** product lifecycle, the **McKinsey Three Horizons** portfolio model, and the **S-Curve** technology adoption model. Designed as the shared hub in a multi-root VS Code workspace.

## Quick Start

1. Open this repo alongside your product repos in a VS Code multi-root workspace
2. Type `/` in Copilot Chat to see all available prompts and skills
3. Select an `@Agent` in the chat picker for guided multi-step workflows

## Available Tools

### Slash Commands (Prompts)

| Command | Purpose |
|---------|---------|
| **Strategy** | |
| `/diagnose` | Strategic diagnosis — identify the core challenge |
| `/guiding-policy` | Formulate the guiding policy |
| `/coherent-actions` | Define coordinated action set |
| `/strategy-kernel` | Full strategy kernel in one pass |
| `/strategy-review` | Detect bad strategy hallmarks |
| **Discovery** | |
| `/customer-profile` | Build an evidence-based profile for a target account or segment |
| `/customer-interview-guide` | Generate interview scripts |
| `/hypothesis-tracker` | Track and evaluate hypotheses |
| `/opportunity-assessment` | Score opportunities |
| **Competitive** | |
| `/competitor-profile` | Deep-dive a single competitor |
| `/competitive-landscape` | Map the competitive terrain |
| `/feature-comparison` | Feature comparison matrix |
| **Planning** | |
| `/roadmap` | Outcome-driven roadmap builder |
| `/prioritize` | RICE / impact-effort scoring |
| `/stakeholder-map` | Influence/interest stakeholder grid |
| **Delivery** | |
| `/gtm-plan` | Go-to-market plan |
| `/metrics-framework` | Leading/lagging KPI framework |
| `/launch-checklist` | Pre-launch readiness checklist |
| **Pricing** | |
| `/pricing-strategy` | Pricing strategy with licensing journey and persona value map |
| `/competitive-pricing` | Competitive pricing benchmark and TCO analysis |
| **Research** | |
| `/extract-document` | Extract text+images from PPT/XLS/PDF |
| `/extract-insights` | Pull insights from research content |
| `/organize-research` | Synthesize multiple research sources |
| `/market-research` | Structured market research |

### Agents

| Agent | Purpose |
|-------|---------|
| `@Strategist` | Multi-step strategy formulation (diagnosis → policy → actions) |
| `@Researcher` | Competitive and market research with evidence standards |
| `@Discovery` | Product discovery workflow (hypotheses → interviews → insights) |
| `@Planner` | Roadmap and prioritization connected to strategy |
| `@Reviewer` | Quality reviewer — catches bad strategy, weak evidence, logical gaps |

### User-Level Tools (available in any workspace)

| Command | Purpose |
|---------|---------|
| `/format-for-humans` | Reformat any content for readability |
| `/writing-style` | Apply professional PM writing style |
| `/copyright-notice` | Insert copyright notice |

## Skills Directory

This repo uses a vendor-neutral `skills/` directory for reusable AI capabilities.

- `skills/` is the primary home for skill definitions when using VS Code with non-GitHub models.
- `.github/skills/` is still available for GitHub Copilot Chat compatibility.
- Skills are organized by Productside phase:
  - `skills/context/`
  - `skills/discover/`
  - `skills/define/`
  - `skills/create/`
  - `skills/deliver/`
  - `skills/iterate/`

Use `skills/` for reusable model capabilities, `prompts/` for slash-command templates, and `agents/` for multi-step workflows.

## Workspace Architecture

```
User Level (global)         → Writing, formatting, legal standards
  └── product-planning-os   → PM frameworks, agents, skills, prompts
        ├── skills/               → Vendor-neutral AI skill definitions
        ├── prompts/              → Slash commands and prompt templates
        ├── agents/               → Workflow roles and guided sequences
        ├── competitive-analysis  → Product competitive intelligence
        └── sample-product-data   → Raw and processed research data
```

## Adding a New Product

1. Copy `products/_template/` to `products/<product-name>/`
2. Copy `competitive-analysis/_template/` to `competitive-analysis/<product-name>/`
3. Copy `sample-product-data/_template/` to `sample-product-data/<product-name>/`
4. Start with `product-context.md` — fill in market, customers, constraints
5. Use `@Strategist` to formulate the strategy kernel

## Frameworks

- [Good Strategy / Bad Strategy](frameworks/good-strategy-bad-strategy/README.md) — Rumelt's kernel
- [Productside Lifecycle](frameworks/productside/README.md) — Context → Discover → Define → Create → Deliver → Iterate
- [McKinsey Three Horizons](frameworks/mckinsey-3-horizons/README.md) — Baghai/Coley/White portfolio model for simultaneous growth management
- [S-Curve (Technology Adoption)](frameworks/s-curve/README.md) — Rogers/Foster diffusion and innovation curve, with curve-jumping strategy