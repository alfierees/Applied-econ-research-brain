---
type: method
status: in-progress
tags: [method]
---

# Design A: Occupation × quarter event study (main)

Borrowed from [[Hui, Reshef & Zhou (2024)]].

**DiD:** ln Emp_ot = β (Exposure_o × Post_t) + X_ot γ + α_o + δ_t + ε_ot

**Event study:** replace Post with quarter dummies; reference quarter 2022Q4.

| Term | Ours |
|---|---|
| o, t | Occupation, quarter (2019Q1-2026Q2) |
| Exposure | Continuous score (main); top quartile vs zero (robustness) |
| Post | 1 from 2023Q1 |
| X | Age, education, sex shares of the occupation |
| α, δ | Occupation and quarter FE |
| SEs | Clustered by occupation (~500 clusters) |
| Data | CPS via IPUMS, person weights, harmonised occupation codes |

**β in words:** % change in employment in exposed occupations relative to unexposed ones, after vs before ChatGPT.

Outcomes: log employment (main), under-30 share. Vacancies dropped with Israel. Open choices: [[Measurement Choices (US)]].
