---
type: method
status: in-progress
tags: [method, us]
created: 2026-11-11
---

# Measurement choices (US)

Decisions still open for [[Design A - Occupation Event Study]]. Splits are in [[Heterogeneity - Age Sex Seniority]].

| Choice | Options | Our lean | Notes |
|---|---|---|---|
| **Main outcome** | ln employment; employment share of total; unemployment by last occupation; hours; wages (CPS ORG) | ln employment main, share as robustness | Wages stay an extension |
| **Unit** | Occupation × quarter (~500 occupations) vs ~100 broader groups | ~500 for β, broader groups for splits | Clusters by occupation, ~500 so standard clustering is fine |
| **Primary exposure** | Anthropic observed, Microsoft applicability, Felten AIOE; Eloundou | Felten as primary (tool-agnostic), vendors side by side | Each vendor measure tilts to its own users |
| **Treatment form** | Continuous score × post vs top quartile vs zero | Continuous main, quartile robustness | |
| **Window and COVID** | Start 2019 with COVID quarters dummied/dropped (2020Q2 to 2021Q2); start 2021; extend back to 2015 | Start 2019, drop 2020Q2 to 2021Q2, show full series in the event-study plot | Yale Budget Lab notes the occupational mix was already shifting in 2021 |
| **Occupation codes** | CPS switched to 2018 Census codes in 2020 | Use IPUMS harmonised codes (OCC2010) or a crosswalk | See [[Crosswalks]] |
| **Weights** | CPS person weights vs unweighted | Weighted | |
| **Productivity data (θ)** | BEA quarterly value added by industry vs BLS annual labour productivity | BEA quarterly, BLS as check | Only ~70 industries |
