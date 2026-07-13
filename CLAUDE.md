# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

An AI-powered product management operating system. It is designed to be opened alongside product repos in a VS Code multi-root workspace, providing shared PM frameworks, prompt templates, agent definitions, and extraction scripts.

## Commands

### Python Script Utilities

Install dependencies first:
```
pip install -r scripts/requirements.txt
```

Extract documents to markdown:
```
python scripts/extract_pdf.py input.pdf out/
python scripts/extract_pptx.py input.pptx out/
python scripts/extract_xlsx.py input.xlsx out/
```

Convert markdown to styled PDF:
```
python scripts/md_to_pdf.py file.md file.pdf
```

Note: PPTX/Excel chart rendering requires Windows with Office installed. All scripts require Python 3.8+.

## Architecture

### Four Layers

**1. Frameworks** (`frameworks/`) — Source-of-truth reference documents for the four mental models that govern all work:
- `good-strategy-bad-strategy/` — Rumelt's strategy kernel (diagnosis → guiding policy → coherent actions)
- `productside/` — The six-phase product lifecycle (Context → Discover → Define → Create → Deliver → Iterate)
- `mckinsey-3-horizons/` — Portfolio model for simultaneous growth management
- `s-curve/` — Rogers/Foster technology adoption and curve-jumping strategy

**2. Skills** (`skills/`) — Vendor-neutral reusable AI capability definitions, organized by Productside phase: `context/`, `discover/`, `define/`, `create/`, `deliver/`, `iterate/`. `.github/skills/` mirrors these for GitHub Copilot Chat compatibility.

**3. Prompts** (`prompts/`) — Slash command templates for direct invocation. Organized by domain: `strategy/`, `competitive/`, `discovery/`, `planning/`, `delivery/`, `pricing/`, `extraction/`.

**4. Agents** (`agents/`) — Multi-step workflow definitions that chain skills and prompts into guided sequences. The five agents are: `Strategist`, `Researcher`, `Discovery`, `Planner`, `Reviewer`.

### Product Data

`products/` holds per-product working documents. Each product folder uses the `_template/` structure:
- `product-context.md` — market, customers, constraints (fill this first)
- `strategy-kernel.md` — current diagnosis, guiding policy, coherent actions
- `roadmap.md`, `discovery-log.md`, `competitive-landscape.md`, `pricing-licensing.md`

Product-specific data is gitignored (`products/*/`); only `_template/` is committed.

### VS Code MCP Servers

Two MCP servers are configured in `.vscode/mcp.json`:
- `pdf-reader` — text extraction, page screenshots, search in PDFs
- `excel-reader` — read and query Excel spreadsheet data

## Strategic Framework Rules

Always structure strategy work around the Rumelt kernel:
- **Diagnosis** — What is the actual challenge? (assessment, not a wish)
- **Guiding Policy** — What approach rules out alternatives? (a method, not a goal)
- **Coherent Actions** — What coordinated steps carry out the policy? (must reinforce each other)

Flag bad strategy when you see: fluff/buzzwords, avoidance of the real problem, goals stated as strategy ("grow 20%"), or unfocused to-do lists.

## Evidence Standard

Distinguish **evidence** (data, research, quotes) from **assumptions** (beliefs, hypotheses). When summarizing research, note: source, date, methodology, and confidence level. Prefer quantitative evidence; include direct quotes for qualitative.

## Output Conventions

- Lead with the insight or recommendation, then supporting evidence
- Use headers, bold key terms, bullets, and tables for comparisons
- End strategic documents with specific, assignable, time-bound "Next Steps"
- When presenting options, use a comparison table with evaluation criteria
