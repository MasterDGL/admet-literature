# Multitask Deep Neural Networks for Ames Mutagenicity Prediction

**English** | [简体中文](../../../papers/admet/ames-multitask-2022.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Chemical Information and Modeling · 2022-09-06* · Published · Further reading

**Overview:** Learns Ames outcomes for five bacterial strains jointly, retaining strain-specific information alongside the overall mutagenicity label.

Topics: AMES, Strain-level labels, Multitask learning.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Chemical Information and Modeling 62(24), 6342–6351; online 2022-09-06. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Collapsing results across strains into one label discards strain-level information useful for mutagenicity prediction. |
| Datasets | Authors' Mendeley v2 data: 5,536 ISSSTY-curated molecules with 1,360 Mordred descriptors, labels for TA98, TA100, TA102, TA1535 and TA1537 plus Overall, including undetermined labels. Train/Internal/External partitions are provided. |
| Method | A shared network jointly predicts TA98, TA100, TA102, TA1535 and TA1537, then combines outputs by a consensus rule. Comparators predict the overall label directly or combine separately trained strain models; missing labels are handled explicitly. |
| Findings | The published abstract reports improvements over overall-label single-task models and ensembles of strain-specific models, supporting the use of strain-level information. |

DOI: `10.1021/acs.jcim.2c00532`

## Experimental setup and analysis

**Design.** Author data provide Train/Internal/External partitions, and training code uses fivefold validation. Published supplements include cross-validation predictions and external-prediction workbooks for MTL, Overall and separate-strain models. For example, external-validation-MTL.xls contains five Fold sheets with 1,114 compound rows each.

**Configuration.** Supplementary Table S2 distinguishes ordinary and weighted losses: MTL has five outputs and the overall-label model one, both using learning rate 0.0001. S3 lists separate-strain configurations. S4 specifies the strain variants and ±S9 conditions aggregated into each label.

**Results provenance.** The published abstract reports improvements over overall-label and separate-strain consensus models; the published supplements provide configurations and prediction files. Supplementary Table S1 summarizes other tools in the international Ames/QSAR challenge as background context.

Experimental variants are aggregated into five strain labels, unlike AmesNet’s explicit strain/S9 conditioning. The supplement identifies three possible salt-form duplicate pairs whose partition assignments deserve inspection during reproduction.

## Code and references

[Code and project](https://github.com/VirSabando/MTL_DNN_Ames)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked published abstract, Supplementary Tables S1–S4, prediction-file structure, and author data.py/compute_metrics.py; final main-text result tables still require full-text verification

- [Published-version abstract](https://pubmed.ncbi.nlm.nih.gov/36066065/)
- [Author data v2](https://data.mendeley.com/datasets/ktc6gbfsbh/2)
- [Author code](https://github.com/VirSabando/MTL_DNN_Ames)
- [Published supplement, Tables S1–S4](https://acs.figshare.com/articles/journal_contribution/20976947)
- [Published prediction files](https://acs.figshare.com/articles/journal_contribution/20976950)
