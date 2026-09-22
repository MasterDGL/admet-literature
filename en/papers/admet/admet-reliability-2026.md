# ADMET reliability benchmark

**English** | [简体中文](../../../papers/admet/admet-reliability-2026.md)

**Revisiting ADMET prediction reliability under real-world challenges in the foundation model era**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Compares model families under limited data, unfamiliar molecular structures and class imbalance to assess ADMET prediction in practical research settings.

Category: Core papers. Topics: Generalization, Small data, Evaluation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 18, 95; 2026-05-18 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Average benchmark scores miss reliability issues involving small datasets, out-of-distribution prediction, class imbalance, beyond-rule-of-five molecules and activity cliffs. |
| Datasets | 14 property/ADMET datasets covering hERG, BBBP, Caco-2, half-life, VDss, CYP and peptide properties, plus 30 bioactivity tasks from MoleculeACE. |
| Method | Compares KPGT, Uni-Mol, TabPFNv2, classical machine learning and AutoML in a common framework, using random, scaffold and Perimeter splits, resampling and ensembles. |
| Findings | TabPFNv2 often performs well in the evaluated small-data/OOD settings. Undersampling ensembles help with imbalance, while KPGT performs strongly on cyclic-peptide permeability with more training data. Activity cliffs remain difficult across models. |

DOI: `10.1186/s13321-026-01217-2`

## Experimental setup and analysis

Uses random, scaffold and Perimeter splits, organizing experiments around small datasets, class imbalance and out-of-distribution prediction.

Table 1 and scenario-specific results show how model strengths change with data conditions. KPGT achieves R² = 0.627 on CycPept-PAMPA cyclic-peptide permeability.

## Code and references

[Code and project](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-026-01217-2)
- [Author code](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)
