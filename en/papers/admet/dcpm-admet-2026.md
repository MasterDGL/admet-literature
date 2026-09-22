# DCPM-ADMET

**English** | [简体中文](../../../papers/admet/dcpm-admet-2026.md)

**DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Combines representations from two pretrained models with chemical fingerprints to predict 97 ADMET properties.

Category: Core papers. Topics: ADMET, Pretraining, Representation fusion.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 18, 126; 2026-06-20 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | A single representation struggles to capture semantic, structural and physicochemical information together, while ADMET labels are sparse and endpoints heterogeneous. |
| Datasets | Pretraining uses approximately 111 million PubChem records. The ADMET collection contains 97 endpoints: 43 regression and 54 classification tasks, with 465,470 endpoint records. Also evaluates 10 MoleculeNet datasets. |
| Method | Fuses XLNet semantic representations, a GRU component incorporating SMILES-to-InChI and property learning, and ECFP fingerprints; combines single-task random forests, multitask neural networks and parameter optimization. |
| Findings | Reports improvements over the ECFP baseline on 67/97 endpoints and the best results among compared methods on 5 of 10 MoleculeNet tasks. |

DOI: `10.1186/s13321-026-01244-z`

## Experimental setup and analysis

Uses scaffold splits and model/feature comparisons; 67 of 97 endpoints outperform the paper's ECFP baseline.

Fusion ablations examine the contribution of each representation. The platform offers 133 outputs: 97 model predictions and 36 calculated properties.

## Code and references

[Code and project](https://github.com/zhangzhangleilei/DCPM-ADMET)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://link.springer.com/article/10.1186/s13321-026-01244-z)
- [Author code](https://github.com/zhangzhangleilei/DCPM-ADMET)
