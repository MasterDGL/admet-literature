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
| Method | Compares eight molecular representations through AutoGluon, feature selection and hyperparameter optimization. The submitted CaliciBoost predictor is an XGBoost regressor using selected PaDEL descriptors. |
| Findings | Five-seed TDC MAE is 0.2560±0.006. In the paper’s individual feature comparison, selected PaDEL features plus optimization achieve MAE 0.2525 versus 0.3058 with all PaDEL features. |

DOI: `10.1186/s13321-025-01137-7`

## Experimental setup and analysis

**Design.** TDC Caco2_Wang contains 906 molecules; the official scaffold split reserves 20% for testing, with five seeds for the final benchmark. The 5,481 curated OCHEM records are split separately using structural clusters and permeability bins, then modeled independently. Eight representations are compared; MAE is the primary metric.

| Experiment | MAE ↓ | Context |
| --- | --- | --- |
| All PaDEL features | 0.3058 | Feature comparison, Supplementary Table 1 |
| Selected PaDEL features and optimization | 0.2525 | Individual experiment; RMSE 0.3216, R² 0.7805, Fig. 6 |
| CaliciBoost official benchmark | 0.2560±0.006 | Mean±SD over five seeds, Figs. 10–11 |

**Interpretation.** The two final MAE values describe different summaries. TDC and OCHEM models are trained and tested separately; OCHEM is not a direct external transfer test of the TDC-trained predictor.

Feature selection and optimization contribute jointly. Some OCHEM records lack assay direction, making assay consistency an additional data-quality issue.

## Code and references

[Code and project](https://github.com/Calici/CaliciBoost)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked data processing, splits, model selection and results associated with Figs. 6 and 10–11

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-025-01137-7)
- [Author code](https://github.com/Calici/CaliciBoost)
- [TDC Caco-2 leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/)
