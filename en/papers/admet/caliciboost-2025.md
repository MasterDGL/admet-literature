# CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction

**English** | [简体中文](../../../papers/admet/caliciboost-2025.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2025-12-22* · Published · Core papers

**Overview:** Combines molecular fingerprints, physicochemical descriptors and automated machine learning to predict permeability through the Caco-2 intestinal cell model.

Topics: Absorption, Caco-2, AutoML.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 17, 184; 2025-12-22; preceded by a 2025 preprint. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Caco-2 permeability data are limited and assay conditions vary, making it difficult to identify effective molecular features and modeling strategies. |
| Datasets | TDC Caco2_Wang contains 906 molecules. A separate OCHEM collection was reduced from 9,402 raw records to 5,481 modeling records through filtering and cleaning. The two datasets are modeled and evaluated separately. |
| Method | Compares fingerprints, RDKit/PaDEL/Mordred descriptors and CDDD representations, combining AutoGluon with feature selection, interpretation and hyperparameter optimization. |
| Findings | Feature selection and ensemble learning improve Caco-2 prediction. The official TDC Caco-2 leaderboard snapshot dated 2026-09-19 lists MAE = 0.256 ± 0.006 and ranks CaliciBoost first. |

DOI: `10.1186/s13321-025-01137-7`

## Experimental setup and analysis

Evaluates TDC Caco2_Wang and the curated OCHEM data separately. The 2026-09-19 TDC snapshot reports MAE = 0.256 ± 0.006.

Results illustrate the contribution of feature selection and ensembles. Some OCHEM records lack the assay direction, leaving label consistency as a data-quality issue.

## Code and references

[Code and project](https://github.com/Calici/CaliciBoost)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-025-01137-7)
- [Author code](https://github.com/Calici/CaliciBoost)
- [TDC Caco-2 leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/)
