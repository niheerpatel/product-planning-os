---
description: "Build an objective customer profile across company health, direction, operating challenges, and technical landscape."
agent: "agent"
argument-hint: "Company name or customer segment to profile"
tools: [read, search, web]
---

# Customer Profile

Create an evidence-based profile of a potential customer account or customer segment. The profile should help sales, product, and marketing understand company health, strategic direction, partner-fit challenges, and technical context.

## Principles
- **Evidence over narrative**: Every substantive claim should include source, date, methodology (if known), and confidence.
- **Label uncertainty**: If evidence is unavailable, tag the statement as `[ASSUMPTION]` and explain what would validate it.
- **Objective analyst stance**: Describe the company as it is, not as we want it to be.
- **Actionable implications**: Translate findings into concrete implications for sales, product, and marketing.

## Process
1. Confirm scope: named account profile or industry-segment profile.
2. Search workspace artifacts for prior context and customer evidence.
3. Run web research to fill gaps in financial, leadership, organizational, technical, and operational data.
4. Build the profile using the output template below.
5. For each section, explicitly label key points as Evidence, Inference, or `[ASSUMPTION]`.
6. End with partner-fit opportunities, risk signals, and open validation questions.

## Output Format

# Customer Profile: [Company or Segment]

**Profile mode**: Named account / Segment
**Last updated**: [Date]
**Overall confidence**: High / Medium / Low

## Executive Summary
- **Health snapshot**: [1-2 sentence view of business health]
- **Strategic direction**: [1-2 sentence view of where the company is headed]
- **Partner relevance**: [Why this profile matters for us now]

## Company Demographics
- **Headquarters**: [Location]
- **Operating regions**: [Geographies]
- **Company size**: [Employees / revenue band]
- **Culture signals**: [Public values, operating style, risk posture]
- **Industry position**: [Leader / challenger / specialist / follower]

## Financial Health
| Metric or signal | Finding | Evidence type | Source + date | Confidence |
|------------------|---------|---------------|---------------|------------|
| Revenue trend | ... | Evidence / Inference / [ASSUMPTION] | ... | ... |
| Profitability / margins | ... | ... | ... | ... |
| Cash / funding / debt | ... | ... | ... | ... |
| Investment capacity | ... | ... | ... | ... |

## Leadership and Organizational Profile
- **Leadership team and priorities**: [Evidence-backed summary]
- **Org model**: [Centralized / BU-led / matrix, where known]
- **Decision style**: [Top-down / consensus / procurement-led]
- **Evidence markers**: earnings calls, investor updates, leadership interviews, job postings

## Strategic Direction and Active Initiatives
| Initiative | What they appear to be solving | Stage | Evidence / [ASSUMPTION] | Confidence |
|-----------|--------------------------------|-------|--------------------------|------------|
| ... | ... | ... | ... | ... |

## Operational Problems and Partner-Fit Challenges
| Problem or constraint | Business impact | Current approach/workaround | Partner/vendor help needed | Evidence status |
|-----------------------|-----------------|-----------------------------|----------------------------|-----------------|
| ... | ... | ... | ... | Evidence / Inference / [ASSUMPTION] |

## Application Domain and Technical Landscape
- **Primary application domains**: [Use-cases/workloads]
- **Software architecture signals**: [Cloud/on-prem/hybrid, platform signals, integration patterns]
- **Hardware architecture signals**: [Compute platforms, embedded constraints, deployment targets]
- **Toolchain and ecosystem**: [Vendors, standards, frameworks]
- **Known technical constraints**: [Safety, regulatory, latency, reliability, cybersecurity, etc.]

## Production and Volume Signals
| Signal | Current state | Trajectory | Source + date | Confidence |
|--------|---------------|------------|---------------|------------|
| Annual production volume | ... | ... | ... | ... |
| Program scale / installed base | ... | ... | ... | ... |
| Capacity expansion or cuts | ... | ... | ... | ... |

## Buying Process and Commercial Fit
- **Economic buyer**: [Title/function]
- **Technical buyer/champions**: [Roles]
- **Procurement dynamics**: [Cycle, controls, preferred contract shape]
- **Budget posture**: [Cost pressure / growth investment / mixed]
- **Deal feasibility factors**: [What will make or break a deal]

## Implications for Us
- **Sales**: [Account strategy, stakeholder approach, qualification notes]
- **Product**: [Capability gaps, roadmap relevance, integration requirements]
- **Marketing**: [Positioning angle, proof points, objection handling]

## Evidence Ledger
| Claim ID | Claim | Label (Evidence / Inference / [ASSUMPTION]) | Source | Date | Methodology | Confidence |
|----------|-------|----------------------------------------------|--------|------|-------------|------------|
| C1 | ... | ... | ... | ... | ... | ... |

## Open Questions to Validate
1. [Critical unknown #1]
2. [Critical unknown #2]
3. [Critical unknown #3]

## Sources
- [Source 1](URL) - accessed [date]
- [Source 2](URL) - accessed [date]
