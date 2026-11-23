---
type: dashboard
tags: [home]
---

# AI and the Labour Market: United States

**Question (draft, US only):** Did the arrival of generative AI (ChatGPT, Nov 2022) reduce employment and raise output per worker in AI-exposed US occupations and industries between 2019 and 2026, and which workers carried the effect?

> [!warning] Israel dropped from scope (Nov 2026) on Dr. Hadass's advice. Israel notes are kept but marked out of scope. Next meeting: [[2026-11-11 Meeting prep - Dr. Hadass]].

**Team:** Alfie Rees & Lorenzo Del Monte · Applied Economics (Dr. Yael Hadass) · Reichman 2026-27

## Where things stand
- Phase: **Methodology presented; narrowing to US, then data**
- Next deadline: see [[Deadlines]]
- Latest decisions: [[Decisions Log]]
- Visual overview: [[Roadmap]] · [[Progress Tree]]

## Map of the vault
| Folder | What lives there |
|---|---|
| 01 Admin | [[Deadlines]], assignments, meeting notes, [[Decisions Log]] |
| 02 Question & Scope | [[Research Question]], [[Scope]], [[Open Questions]] |
| 03 Literature | One note per paper: core three, alternates, related work, exposure measures |
| 04 Sectors & Occupations | One note per sector group, exposed vs low exposure (controls) |
| 05 Data | One note per data source, [[Crosswalks]], [[Data Access Log]] |
| 06 Methodology | [[Design A - Occupation Event Study]], [[Design B - Industry Productivity]], [[Heterogeneity - Age Sex Seniority]], [[Measurement Choices (US)]], [[Identification Threats]], [[Inference with Few Clusters]] (Israel, parked) |
| 07 Analysis & Findings | [[Findings Log]] and one note per result |
| 08 Writing | [[Paper Outline]], drafts |
| 09 Visuals | [[Roadmap]], [[Progress Tree]] |
| Templates | Paper, sector, meeting, finding, decision |

## Sector status (needs the Dataview community plugin)
```dataview
TABLE exposure AS "Exposure", status AS "Status", us_data AS "US data"
FROM "04 Sectors & Occupations"
SORT exposure DESC, file.name ASC
```

## Papers (needs Dataview)
```dataview
TABLE journal AS "Journal", repec_rank AS "RePEc", role AS "Role", status AS "Status"
FROM "03 Literature"
WHERE type = "paper"
SORT role ASC
```

## Open tasks across the vault (needs Dataview)
```dataview
TASK
WHERE !completed
GROUP BY file.link
```
