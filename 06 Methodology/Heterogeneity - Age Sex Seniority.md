---
type: method
status: in-progress
tags: [method]
updated: 2026-11-11
---

# Heterogeneity: age, sex, seniority (US)

**Triple difference:** Y_ogt = β₃ (Exposure_o × Post_t × Group_g) + γ_og + λ_ot + μ_gt + ε

- o = occupation, g = worker group (e.g. young), t = quarter.
- λ_ot (occupation × quarter FE) absorbs anything hitting a whole occupation (rate rises, tech slowdown).
- β₃ compares, say, young vs older workers in the same occupation and quarter.

## The dilemmas
| Split | Options | CPS data | Our lean | Ask Dr. Hadass? |
|---|---|---|---|---|
| **Age** | (a) 22-25 vs 26+ (matches Canaries); (b) under-30 vs 30+; (c) bands 22-29, 30-44, 45+ | Age every month | (b) headline for cell size, (a) as robustness to compare with Canaries | Yes |
| **Sex** | Female dummy | Every month | Keep: top-exposure group is ~16 pp more female, so β partly reflects composition | Light check |
| **Seniority** | (a) age as proxy; (b) CPS Job Tenure Supplement (Jan 2022, 2024, 2026); (c) supervisor / manager occupations vs rest | No tenure in monthly CPS | (a) main, (b) as a simple pre/post side check (one pre, two post points) | Yes |
| **Education** | BA+ vs no BA | Every month | Add: Canaries and Yale both focus on young graduates | Yes, is it one split too many? |

## Practical constraints
- **Thin cells:** ~500 occupations × several groups × 30 quarters. Young workers in a given occupation-quarter can be a few dozen CPS respondents. Options: pool to half-years, aggregate to ~100 occupation groups for the splits, or use exposure-quintile × group × quarter cells.
- **Too many splits:** every extra split is another table. Probably age headline plus sex, others in robustness.
- **Interactions:** young women etc. only if cells allow.

## Dropped with Israel
- Israeli age bands (~25-29 vs 35+, army service) no longer needed.
