# BBB MegaMolBART

**English** | [简体中文](../../../papers/admet/bbb-megamolbart-2024.md)

**Predicting blood–brain barrier permeability of molecules with a large language model and machine learning**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Predicts blood–brain barrier permeability with a molecular language model and XGBoost, then tests selected compounds in human-derived 3D BBB spheroids.

Category: Further reading. Topics: BBB, Molecular language models, In vitro validation.

| Field | Details |
| --- | --- |
| Publication and date | Scientific Reports 14, 15844; 2024-07-09 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | BBB labels are limited; the study tests whether pretrained molecular representations improve prediction and receive experimental support in vitro. |
| Datasets | B3DB: 7,807 molecules (4,956 BBB+, 2,851 BBB−); CMUH: 2,499 (105 BBB+, 2,394 BBB−). B3DB includes 1,058 logBB values. Spheroid experiments select 21 predicted permeable and 5 predicted impermeable candidates, with controls. |
| Method | MegaMolBART encodes SMILES for XGBoost classification/regression, compared with Morgan fingerprints. BBB spheroids contain human brain microvascular endothelial cells, pericytes and astrocytes; LC–MS/MS measures permeability. |
| Findings | Reports a final held-out AUROC of 0.88. Spheroid results agree with prediction directions for the selected candidates, supporting exploratory BBB screening. |

DOI: `10.1038/s41598-024-66897-y`

## Experimental setup and analysis

Compares B3DB-only training, CMUH external testing and mixed-data settings. The final classifier splits B3DB/CMUH 80/10/10, achieving held-out AUROC = 0.88.

Spheroid experiments select candidates with very high or low scores, supporting their in vitro permeability classification. Intermediate-score compounds and human permeability need further experiments.

## Code and references

The paper links B3DB and MegaMolBART components; a link to the complete training workflow remains to be added.

Sources reviewed: **2026-09-22**. Bibliographic metadata, relevant methods and results, and the listed official resources.

- [Publisher full text and supplements](https://www.nature.com/articles/s41598-024-66897-y)
- [B3DB data source](https://github.com/theochem/B3DB)
