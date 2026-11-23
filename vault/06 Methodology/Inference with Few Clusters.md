---
type: method
tags: [method, israel]
---

# Inference with few clusters (Israel ~36 vs US ~500)

> [!note] Parked (Nov 2026): Israel is out of scope. Kept as the reason we dropped it. With ~500 US occupations, standard clustered SEs are fine.

## Problem 1: mixing
ISCO group 26 holds writers and translators (very exposed) with clergy, social workers and actors (near zero). Illustration: 30% writers at score 0.6, rest at 0.05, gives a group score of ~0.22. A 10% fall in writer jobs shows up as only a 3% fall for the group. Attenuation pulls β towards zero.

## Problem 2: inference
Clustered SEs are too small with ~36 clusters; a top-quartile split leaves only 9 treated clusters. Use wild cluster bootstrap; expect wide intervals.

## Problem 3: thin cells at fine detail
More categories mean fewer survey respondents per cell, especially after age × sex splits.

## Plan
US = main estimate. Israel at 3-digit (~130 groups) or 4-digit via CBS microdata. Age triple difference helps Israel most.
