# SSL-GCN

**English** | [简体中文](../../../papers/admet/ssl-gcn-2021.md)

**Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Trains a graph neural network on labeled and unlabeled molecules to improve Tox21 toxicity prediction through semi-supervised learning.

Category: Further reading. Topics: Toxicity, Semi-supervised learning, Tox21.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 13, 93; 2021-11-27 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Toxicity labels are limited, while many compounds have only structural information; supervised graph models cannot fully use these unlabeled molecules. |
| Datasets | Tox21: 7,831 molecules and 12 toxicity endpoints. Removing labels from ClinTox, SIDER, ToxCast and HIV and excluding structures overlapping with Tox21 yields 50,527 unlabeled molecules. |
| Method | A GCN encodes molecular graphs within a Mean Teacher framework. The student learns toxicity labels, teacher parameters follow an exponential moving average of student parameters, and prediction consistency under perturbations incorporates unlabeled data. |
| Findings | The paper reports a best mean ROC-AUC of 0.757, compared with about 0.71 for the conventional machine-learning models evaluated. Unlabeled data improve prediction, with the best mixing ratio varying by endpoint. |

DOI: `10.1186/s13321-021-00570-8`

## Experimental setup and analysis

Tox21 uses an 80%/10%/10% scaffold split and five repeated runs. Comparisons include supervised SL-GCN, ECFP4-based KNN, neural networks, random forests, SVM and XGBoost, and DeepChem models. Tested unlabeled-to-labeled ratios are 0.5, 1, 2, 3 and 4.

Label completeness and class balance vary across the 12 endpoints. Endpoint AUROC and mixing-ratio experiments show that adding more unlabeled molecules does not consistently improve every task.

## Code and references

[Code and project](https://github.com/chen709847237/SSL-GCN)

The author repository provides training and prediction scripts, with README links to data and model archives.

Sources reviewed: **2026-09-22**. Reviewed the publisher full text for data, scaffold splitting, Mean Teacher and results, and checked the author repository README.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-021-00570-8)
- [Author code](https://github.com/chen709847237/SSL-GCN)
