# AMES multitask DNN

**English** | [简体中文](../../../papers/admet/ames-multitask-2022.md)

**Multitask Deep Neural Networks for Ames Mutagenicity Prediction**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Learns Ames outcomes for five bacterial strains jointly, retaining strain-specific information alongside the overall mutagenicity label.

Category: Further reading. Topics: AMES, Strain-level labels, Multitask learning.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Chemical Information and Modeling 62(24), 6342–6351; online 2022-09-06. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Collapsing results across strains into one label discards strain-level information useful for mutagenicity prediction. |
| Datasets | Authors' Mendeley v2 data: 5,536 ISSSTY-curated molecules with 1,360 Mordred descriptors, labels for TA98, TA100, TA102, TA1535 and TA1537 plus Overall, including undetermined labels. Train/Internal/External partitions are provided. |
| Method | A shared-representation multitask DNN learns five strain outcomes and is compared with overall-label single-task models, strain-specific models and their ensembles. Compounds with partially undetermined labels are retained. |
| Findings | The published abstract reports improvements over overall-label single-task models and ensembles of strain-specific models, supporting the use of strain-level information. |

DOI: `10.1021/acs.jcim.2c00532`

## Experimental setup and analysis

The authors' data.py provides Train/Internal/External partitions and five-fold cross-validation, stratifying multitask folds by Overall labels. Individual scores await checking against the published tables.

Five strain labels provide information about different mutation sensitivities. The code README retains submission-stage wording; citations use the published JCIM version.

## Code and references

[Code and project](https://github.com/VirSabando/MTL_DNN_Ames)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Published metadata/abstract, authors' Mendeley v2 documentation, code README and data.py; published result tables have not been fully checked.

- [Published-version abstract](https://pubmed.ncbi.nlm.nih.gov/36066065/)
- [Author data v2](https://data.mendeley.com/datasets/ktc6gbfsbh/2)
- [Author code](https://github.com/VirSabando/MTL_DNN_Ames)
