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

**Design.** Blockers are defined by IC50≤20 μM. Bemis–Murcko scaffolds are allocated approximately 3:1 to training and testing. Table 1 lists 224,945 training molecules (1,453 positives) and 74,982 test molecules (484 positives). Fivefold training-set validation selects hyperparameters and thresholds; oversampling is confined to training folds, with seed 42.

**Results.** The final stacked DNN, HERGAI, achieves test recall 0.864 and recalls 94.29% of blockers with IC50≤1 μM. Comparisons include individual RF/XGBoost/DNN models, docking scores, and CardioTox net and AttenhERG evaluated on the same test set. Specificity, balanced accuracy, ROC-AUC and top-0.1%/1% enrichment are also reported (Results and Discussion, Table 2, Conclusions).

The test set is a scaffold holdout from the same curated sources. Test screening performance also informed docking-pose scoring selection, motivating a separate external evaluation of the complete pipeline. Recall should be read alongside specificity and enrichment.

## Code and references

[Code and project](https://github.com/vktrannguyen/HERGAI)

Author code and data are accessible; the repository was archived on 2026-01-01.

Sources reviewed: **2026-09-22**. Checked Table 1 sample counts, training-fold oversampling, threshold selection and test results

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-025-01063-8)
- [Author code](https://github.com/vktrannguyen/HERGAI)
