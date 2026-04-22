---
description: "Design a metrics framework linking leading indicators to lagging KPIs. For product launch instrumentation and ongoing measurement."
agent: "agent"
argument-hint: "Product or feature to build metrics for"
tools: [read, search]
---

# Metrics Framework

Design a measurement system that connects leading indicators (things you can influence now) to lagging KPIs (business outcomes you're trying to move).

## Principles
- **Leading indicators first**: These are your early warning system — they predict future outcomes
- **Every metric needs an owner**: If no one owns it, no one acts on it
- **Instrument before launch**: Measurement should be in place before you ship
- **Fewer is better**: 5 metrics you act on beat 50 you ignore

## Output Format

# Metrics Framework: [Product/Feature]

## Metric Hierarchy

```
Business KPI (lagging)
  └── Product metric (lagging)
        └── Leading indicator 1
        └── Leading indicator 2
              └── Input metric
```

## Metrics Table

| Metric | Type | Current baseline | Target | Leading/Lagging | Owner | Data source |
|--------|------|-----------------|--------|----------------|-------|------------|
| ... | ... | ... | ... | ... | ... | ... |

## Leading → Lagging Connections
| Leading indicator | Predicts... | Confidence | Lag time |
|------------------|------------|-----------|---------|
| ... | ... | High/Med/Low | ... |

## Instrumentation Checklist
- [ ] [Event/metric to instrument]
- [ ] [Dashboard to create]
- [ ] [Alert to set up]

## Review Cadence
| Frequency | Metrics reviewed | Forum | Action if off-track |
|-----------|-----------------|-------|-------------------|
| Daily | [Input metrics] | Stand-up | [Immediate action] |
| Weekly | [Leading indicators] | Team review | [Course correct] |
| Monthly | [Lagging KPIs] | Business review | [Strategy update] |
