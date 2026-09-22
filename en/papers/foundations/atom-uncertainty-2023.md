# Explainable uncertainty quantifications for deep learning-based molecular property prediction

**English** | [简体中文](../../../papers/foundations/atom-uncertainty-2023.md)

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2023-02-03* · Published · Foundational methods

**Overview:** Attributes uncertainty to atoms to locate unfamiliar structures and potential noise, then calibrates ensemble confidence estimates.

Topics: Uncertainty, Calibration, Explainability, D-MPNN.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 15, 13; 2023-02-03 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Molecular uncertainty does not locate problematic structures; averaging network variances can overestimate ensemble uncertainty. |
| Datasets | QM9 enthalpy (133,885), Zinc15 calculated logP (250,000), Lipophilicity experimental logD7.4 (4,187), and Delaney/ESOL solubility (1,128), using the processed versions in Table 1. |
| Method | A D-MPNN predicts atomic contributions and variances, aggregates them with covariance terms, and separates aleatoric and epistemic uncertainty through ensembles. Post-hoc calibration updates only variance layers. |
| Findings | Atomic uncertainty highlights unfamiliar structures. Calibration improves several tasks: ESOL aleatoric ECE falls from 0.2118 to 0.0622. Gains vary across datasets. |

DOI: `10.1186/s13321-023-00682-3`

## Experimental setup and analysis

**Design.** Random 8:1:1 splits compare AtomUnc with molecule-based MolUnc. MAE/RMSE measure prediction error; ECE/ENCE measure calibration error. All decrease with improvement.

| AtomUnc task | ECE before → after calibration | ENCE before → after calibration |
| --- | --- | --- |
| ESOL | 0.2118 → 0.0622 | 0.6414 → 0.5578 |
| Lipophilicity | 0.0413 → 0.0396 | 0.3683 → 0.3704 |

Table 2 reports these aleatoric uncertainties. Table 3 RMSE: AtomUnc/MolUnc = 0.5952/0.8418 for Lipophilicity and 0.6715/0.7520 for ESOL. Variance-only calibration leaves mean predictions unchanged.

This study supports confidence analysis for property regression. Zinc15 logP labels are calculated. Results use random splits; Lipophilicity ENCE increases slightly after calibration, showing endpoint-dependent gains.

## Code and references

[Code and project](https://github.com/chuiyang/atom-based_uncertainty_model)

Author scripts cover training, prediction, atomic visualization and calibration; the implementation supports regression.

Sources reviewed: **2026-09-22**. Checked Crossref, PubMed 36737786, Methods, Tables 1–3 and the author repository

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-023-00682-3)
- [Table 1: datasets](https://link.springer.com/article/10.1186/s13321-023-00682-3/tables/1)
- [Table 2: calibration](https://link.springer.com/article/10.1186/s13321-023-00682-3/tables/2)
- [Table 3: prediction errors](https://link.springer.com/article/10.1186/s13321-023-00682-3/tables/3)
- [Author code](https://github.com/chuiyang/atom-based_uncertainty_model)
