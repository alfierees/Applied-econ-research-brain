---
type: paper
authors: "Hui, Reshef, Zhou"
year: 2024
journal: "Organization Science 35(6): 1977-1989"
repec_rank: 48
role: core-method-source
status: read
tags: [paper]
---

# Hui, Reshef & Zhou (2024): The Short-Term Effects of Generative Artificial Intelligence on Employment: Evidence from an Online Labor Market

| | |
|---|---|
| **Question** | Did ChatGPT and image AI reduce work and pay for exposed freelancers? |
| **Data** | Upwork, ~80,000 freelancers, Jan 2022 to Apr 2023, freelancer-month |
| **Method** | DiD + event study: writing occupations vs less affected, before vs after Nov 2022; freelancer and month FE; SEs clustered by occupation |
| **Main finding** | About 2% fewer monthly jobs and 5.2% lower monthly earnings; top freelancers not protected |
| **How we use it** | **Methodology source paper.** We keep the model and change the country and the unit (occupation × quarter) |

## Their equation
Y_it = β (Post_t × T_i) + X_it γ + α_i + δ_t + ε_it
- Y: jobs, earnings (IHS) · T: writing occupation · Post: after Nov 2022 · X: feedback score, past jobs, past income · α, δ: freelancer, month FE
- Threats they discuss: parallel trends, spillovers to controls (β = lower bound), off-platform work, selection/exit, seasonality, demand vs supply
- Robustness: wild bootstrap, coarsened exact matching, seasonality controls, Poisson/NB

## Notes
-
