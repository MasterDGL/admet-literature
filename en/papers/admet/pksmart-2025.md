# PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules

**English** | [简体中文](../../../papers/admet/pksmart-2025.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2025-09-26* · Published · Core papers

**Overview:** Predicts animal pharmacokinetic parameters, then combines them with molecular features to estimate human intravenous clearance, distribution volume and half-life.

Topics: Human PK, Cross-species prediction, External validation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 17, 147; 2025-09-26 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Human PK data are scarce, limiting structure-only models. The study examines how preclinical species information can improve human parameter prediction. |
| Datasets | Human IV PK: 1,283 compounds, with 1,249/1,281/1,265/879/1,243 labels for VDss/CL/half-life/fraction unbound/MRT. Animal data cover 371 compounds. A separate external set has 315 compounds, with 51/302/38/34 labels for the four evaluable endpoints. |
| Method | First predicts rat, dog and monkey PK parameters from molecular features, then combines these predictions with molecular features in human random-forest models. Uses repeated nested cross-validation and external validation. |
| Findings | External R² is 0.39 for VDss and 0.46 for clearance, with 52.94% and 70.20% of predictions within twofold error. Half-life external R² is 0.06, demonstrating substantial endpoint differences. |

DOI: `10.1186/s13321-025-01066-5`

## Experimental setup and analysis

**Design.** Five outer folds repeated five times yield 25 test folds; fourfold inner grid search tunes hyperparameters. Standardized SMILES exclude training overlap from the external set. Ablations compare molecular features, predicted animal PK, and their combination. All PK labels except fraction unbound are log10-transformed.

| External endpoint | N | R² ↑ | RMSE ↓ | Within twofold error ↑ |
| --- | --- | --- | --- | --- |
| VDss | 51 | 0.39 | 0.56 | 52.94% |
| Clearance | 302 | 0.46 | 0.44 | 70.20% |
| Half-life | 38 | 0.06 | 0.68 | 31.58% |
| Fraction unbound | 34 | 0.26 | 0.22 | 26.47% |

Source: Table 2. RMSE uses log10 labels for the first three endpoints and the untransformed fraction for the fourth. Fold error uses the original scale. MRT has no external test set.

External sample sizes differ substantially across endpoints. Comparison with AstraZeneca mainly measures agreement between model predictions, a different question from prediction accuracy against measured external labels.

## Code and references

[Code and project](https://github.com/srijitseal/PKSmart)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked curation, nested validation, external sample counts and Table 2

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-025-01066-5)
- [Author code](https://github.com/srijitseal/PKSmart)
- [External validation, Table 2](https://link.springer.com/article/10.1186/s13321-025-01066-5/tables/2)
