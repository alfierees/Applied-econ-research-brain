---
type: scope
status: under-review
tags: [question]
updated: 2026-11-11
---

# Research Question

> [!warning] Scope change (Nov 2026): US only
> At the methodology presentation Dr. Hadass said doing the US and Israel together is a lot of work and recommended the US only. We were already leaning that way. The wording below is a draft to confirm at the meeting: [[2026-11-11 Meeting prep - Dr. Hadass]].

## Working question (draft, US only)
> Did the arrival of generative AI (ChatGPT, Nov 2022) effect employment and output per worker in AI-exposed US occupations and industries between 2019 and 2026, and which workers carried the effect?

### Versions to choose between
| Version | Wording | Pros | Cons |
|---|---|---|---|
| A. Employment only | Did ChatGPT reduce employment in AI-exposed US occupations, and for whom? | One clean coefficient (β); CPS alone is enough; fits paper length | Drops the productivity half |
| B. Employment + productivity | A, plus: did output per worker rise in exposed industries? | Answers "substitute or complement"; stronger policy story | Second dataset (BEA/BLS), only ~70 industries, productivity J-curve |
| C. Who is affected | Which workers in exposed occupations (young, women, junior) lost out after ChatGPT? | Sharpest novelty (see below) | Thin CPS cells, needs pooling |

**Our lean:** B with C as the headline section, i.e. β plus splits as the core, θ as a shorter extension. Drop θ if Dr. Hadass thinks it is too much.

## Where it sits in the US debate (new novelty)
The old novelty (first Israeli DiD, Israeli age split) goes with Israel. The US literature currently disagrees:
- **Canaries** (Brynjolfsson, Chandar & Chen, WP): ADP payroll data, finds employment falls for 22-25 year-olds in the most exposed jobs.
- **Yale Budget Lab** (Gimbel, Kinder, Kendall & Lee, Oct 2025, updated to the March 2026 CPS): public CPS data, finds the occupational mix is not changing faster than in past tech waves and exposed occupations have not lost employment share; only a small uptick in dissimilarity between younger and older graduates.
- **Gap:** neither runs a formal occupation × quarter event study on public CPS data with several exposure measures, splits by age, sex and seniority, and a window to 2026. Our paper can test which result holds. To confirm with Dr. Hadass.

## Policy hook
Old hook was Israeli high-tech job seekers (7,200 to 16,300). Needs a US replacement.
- [ ] Find a US policy hook (e.g. recent-graduate unemployment, entry-level hiring) #writing

## Coefficients
- **β**: % change in employment in exposed occupations relative to unexposed ones, after vs before ChatGPT. See [[Design A - Occupation Event Study]].
- **θ**: % change in output per worker in more exposed industries, after vs before. See [[Design B - Industry Productivity]].
- **β₃**: extra effect for a group (young, female, junior) within the same occupation and quarter. See [[Heterogeneity - Age Sex Seniority]].

## History
| Date | Question |
|---|---|
| Oct 2026 | Israel vs US comparison of AI and jobs |
| 1 Nov 2026 | Has generative AI adoption reduced employment and raised productivity in AI-exposed occupations and industries in Israel and the United States? |
| 9 Nov 2026 | Same, with US as main study and Israel secondary |
| 11 Nov 2026 | US only (draft above, pending Dr. Hadass) |
