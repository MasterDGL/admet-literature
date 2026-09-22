# HERGAI: an artificial intelligence tool for structure-based prediction of hERG inhibitors

**English** | [简体中文](../../../papers/admet/hergai-2025.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2025-07-24* · Published · Core papers

**Overview:** Combines docking and ensemble models to identify compounds likely to block the cardiac hERG ion channel in large candidate collections.

Topics: hERG, Docking, Class imbalance.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 17, 110; 2025-07-24 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Small or positive-enriched test sets poorly represent screening collections containing many negatives and few hERG blockers. |
| Datasets | 299,927 curated PubChem/ChEMBL molecules: 1,937 positives and 297,990 negatives. Uses an IC50 threshold of 20 μM and an approximately 3:1 train/test allocation grouped by Bemis–Murcko scaffold. |
| Method | Selects poses after Smina docking and extracts protein–ligand PLEC fingerprints. RF, XGBoost and DNN base models feed a DNN stacking model; oversampling occurs within training folds. |
| Findings | Reports test recall of approximately 86% for blockers with IC50 ≤ 20 μM and 94% for those with IC50 ≤ 1 μM. Screening enrichment exceeds the generic docking scores compared in the paper. |

DOI: `10.1186/s13321-025-01063-8`

## Experimental setup and analysis

Five-fold training-set cross-validation for tuning; reports recall, specificity, balanced accuracy and enrichment. The 86%/94% values are positive recall at two activity thresholds.

Test-set screening performance informed the choice of pose-scoring scheme. High recall comes with false positives, so specificity and enrichment matter; the workflow also requires docking and structural fingerprint calculation.

## Code and references

[Code and project](https://github.com/vktrannguyen/HERGAI)

Author code and data are accessible; the repository was archived on 2026-01-01.

Sources reviewed: **2026-09-22**. Bibliographic metadata, relevant methods and results, and the listed official resources.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-025-01063-8)
- [Author code](https://github.com/vktrannguyen/HERGAI)
