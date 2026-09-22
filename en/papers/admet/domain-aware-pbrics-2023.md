# Domain-aware / pBRICS

**English** | [简体中文](../../../papers/admet/domain-aware-pbrics-2023.md)

**Domain-aware representation of small molecules for explainable property prediction models**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**In one sentence:** Builds chemically meaningful molecular fragments so graph models can predict ADMET properties and identify fragments contributing to each prediction.

Category: Further reading. Topics: Fragment representations, Interpretability, Multitask learning.

| Field | Details |
| --- | --- |
| Publication and date | ICLR 2023 Machine Learning for Drug Discovery (MLDD) Workshop; 2023 |
| Date basis | Year stated in the official workshop acceptance listing |
| Publication status | Workshop paper |
| Research problem | Atom-level importance is difficult to translate into functional groups and medicinal-chemistry changes, while generic fragmentation can break chemically meaningful substructures. |
| Datasets | 23 classification endpoints curated from ADMETlab 2.0 data, covering Ames mutagenicity, carcinogenicity, CYPs, eye and respiratory toxicity, BBBP and Tox21. ChEMBL molecules support fragmentation analysis; interpretation cases include 102 BBBP matched molecular pairs comprising 110 unique molecules. |
| Method | pBRICS post-processes BRICS fragments using functional-group rules to organize scaffolds and substituents. MACCS and ECFP2 fragment fingerprints feed single-task and multitask GCN/RGCN models; Grad-CAM and matched molecular pairs examine fragment contributions. |
| Findings | In Table 2, multitask fragment RGCN achieves mean AUROC of 84.47% across 23 endpoints, versus 83.35% for the comparator trained with ADMETlab 2.0 code, a gain of 1.12 percentage points. Fragment analyses connect functional-group changes with BBBP and Ames predictions. |

## Experimental setup and analysis

The train/validation/test ratio is 80%/10%/10%; the text does not specify random versus scaffold splitting. Table 2 compares MT-FraGCN, MT-FraRGCN, ST-FraGCN and the ADMETlab 2.0 comparator. Sections 3.3–3.4 examine BBBP and Ames matched molecular pairs.

Matched-pair analysis shows that scaffold correlations can dominate predictions: plausible local fragment attribution can coexist with an incorrect class prediction. The same team’s related pBRICS journal study (10.1021/acs.jcim.3c00689) covers 40 properties; the 23-task, 84.47% result here belongs to the workshop paper.

## Code and references

The paper and workshop listing do not provide an accompanying code link.

Sources reviewed: **2026-09-22**. Reviewed the official acceptance listing and its linked 13-page PDF, including fragment representations, splitting, Table 2 and matched-pair analyses; also checked the related journal study’s metadata and task count.

- [Official workshop accepted papers](https://sites.google.com/view/mldd-2023/accepted-papers_1)
- [Full text linked by the workshop](https://drive.google.com/file/d/102YpAC8_5EapFnaoJE1CCwjFgOP_I45U/view)
- [OpenReview paper page](https://openreview.net/forum?id=C9WW17wQF7p)
- [Related pBRICS journal study](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.3c00689)
