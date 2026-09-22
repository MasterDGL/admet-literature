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
| Datasets | Human intravenous PK data for 1,283 distinct compounds, covering VDss, clearance, half-life, unbound fraction and mean residence time; preclinical animal data for another collection of 371 compounds. Label availability varies by endpoint. |
| Method | First predicts rat, dog and monkey PK parameters from molecular features, then combines these predictions with molecular features in human random-forest models. Uses repeated nested cross-validation and external validation. |
| Findings | Reported external R² values are 0.39 for VDss and 0.46 for clearance, indicating that cross-species predictions can improve selected human PK endpoints. |

DOI: `10.1186/s13321-025-01066-5`

## Experimental setup and analysis

Repeated nested cross-validation and external validation; external R² is 0.39 for VDss and 0.46 for clearance.

The study concerns human intravenous PK. Two-stage model comparisons assess the contribution of animal PK information, while external R² values also show the remaining prediction error.

## Code and references

[Code and project](https://github.com/srijitseal/PKSmart)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-025-01066-5)
- [Author code](https://github.com/srijitseal/PKSmart)
