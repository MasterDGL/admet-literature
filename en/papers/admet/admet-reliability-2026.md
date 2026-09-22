# Revisiting ADMET prediction reliability under real-world challenges in the foundation model era

**English** | [简体中文](../../../papers/admet/admet-reliability-2026.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2026-05-18* · Published · Core papers

**Overview:** Compares model families under limited data, unfamiliar molecular structures and class imbalance to assess ADMET prediction in practical research settings.

Topics: Generalization, Small data, Evaluation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 18, 95; 2026-05-18 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Average benchmark scores miss reliability issues involving small datasets, out-of-distribution prediction, class imbalance, beyond-rule-of-five molecules and activity cliffs. |
| Datasets | Fourteen curated property datasets plus 30 MoleculeACE bioactivity tasks. Examples after curation: BBBP 3,873; hERG 9,673; Caco-2 842; half-life 1,314; VDss 1,092; CycPept-PAMPA 6,637 samples (Table 1). Counts refer to this study’s processed versions. |
| Method | Compares KPGT, Uni-Mol, TabPFNv2, classical machine learning and AutoML in a common framework, using random, scaffold and Perimeter splits, resampling and ensembles. |
| Findings | TabPFNv2 often performs well in the evaluated small-data/OOD settings. Undersampling ensembles help with imbalance, while KPGT performs strongly on cyclic-peptide permeability with more training data. Activity cliffs remain difficult across models. |

DOI: `10.1186/s13321-026-01217-2`

## Experimental setup and analysis

**Design.** Random, scaffold and Perimeter splits; five split seeds and five training runs per split yield 25 results per splitting strategy. AutoGluon yields five results per strategy. Comparators include KPGT, Uni-Mol, GEM, graph networks, classical ML, TabPFNv2 and AutoGluon. Classification analysis combines AUROC, recall, F1 and false-positive rate; regression includes R².

| Setting | Result | Location |
| --- | --- | --- |
| Imbalanced Tox21 NR ER | Undersampling ensembles raise KPGT recall from 0.22 to 0.60; false-positive rate 0.27 | Fig. 4 |
| Cyclic-peptide permeability, 6,637 samples | R²: KPGT 0.627; GNNAK 0.605 | Fig. 5 |
| Activity-cliff molecules | R²: KPGT 0.46; XGBoost + MorganCount 0.51 | Fig. 6b |
| Activity-cliff pair detection | Recall: MOLMCL 0.130; KPGT 0.128 | Fig. 6c |

Model selection depends on sample size, distribution shift and task. The activity-cliff experiments use bioactivity datasets to probe representation quality; these scores are separate from the ADMET endpoint evaluations.

## Code and references

[Code and project](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked Methods, Table 1 and the experimental designs and results in Figs. 4–6

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-026-01217-2)
- [Author code](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)
