# CardioTox net: a robust predictor for hERG channel blockade based on deep learning meta-feature ensembles

**English** | [简体中文](../../../papers/admet/cardiotox-net-2021.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2021-08-16* · Published · Further reading

**Overview:** Combines neural-network predictions from different molecular representations to identify hERG blockers and tests them on three external datasets.

Topics: hERG, Ensembles, External validation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 13, 60; 2021-08-16 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Single representations can omit relevant information, while simple model combinations struggle to balance sensitivity, specificity and predictive accuracy. |
| Datasets | 12,620 training molecules from BindingDB, ChEMBL and literature: 6,643 blockers and 5,977 non-blockers. Three external sets contain 44, 41 and 839 molecules, using an IC50 threshold of 10 μM. |
| Method | Five base neural networks process different chemical features; a separate neural network combines their predictions. A 70/10/10/10 allocation supports base-model training/validation and meta-model training/validation. |
| Findings | External MCC values are 0.599/0.452/0.220 and accuracies 0.810/0.755/0.746. Several metrics improve over selected earlier methods, but PPV on the third, imbalanced set is only 0.113. |

DOI: `10.1186/s13321-021-00541-z`

## Experimental setup and analysis

The Data preparation section describes the training and three external datasets and analyzes their chemical similarity.

Two external sets are small; the third has a low positive fraction. Its PPV of 0.113 highlights false positives under imbalance and should be read alongside recall.

## Code and references

[Code and project](https://github.com/Abdulk084/CardioTox)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Bibliographic metadata, relevant methods and results, and the listed official resources.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-021-00541-z)
- [Author code](https://github.com/Abdulk084/CardioTox)
