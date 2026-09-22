# AmesNet

**English** | [简体中文](../../../papers/admet/amesnet-2026.md)

**AmesNet: A Task-Conditioned Deep Learning Model with Enhanced Sensitivity and Generalization in Ames Mutagenicity Prediction**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**In one sentence:** Combines molecular structure, bacterial strain and metabolic-activation conditions to improve Ames mutagenicity detection in unfamiliar chemical space.

Category: Core papers. Topics: AMES, Assay conditions, Out-of-distribution prediction.

| Field | Details |
| --- | --- |
| Publication and date | Chemical Research in Toxicology; online 2026-06-29. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Models miss mutagenic compounds outside the training domain, while increasing sensitivity alone can produce many false positives. |
| Datasets | Strain/S9-conditioned data compiled by Lui et al. After the published version's cleaning, training/validation contains 40,129 records and testing 4,208. Each record is a compound–strain–S9 combination. Foil data lacking strain/S9 information are evaluated separately. |
| Method | A molecular encoder and strain/±S9 condition channel form two branches. Compares single-task, ordinary/grouped multitask models and condition-augmented encoders including ChemProp and GROVER. |
| Findings | The published main OOD evaluation reports sensitivity 0.72 (95% CI 0.68–0.76) and balanced accuracy 0.81 (0.78–0.83). The supplementary Foil evaluation gives balanced accuracy 0.72. |

DOI: `10.1021/acs.chemrestox.6c00082`

## Experimental setup and analysis

Uses the source study's OOD partitions and removes identical non-stereochemical SMILES across partitions. Main-task and Foil metrics are separate; international Ames/QSAR challenge results provide background comparisons.

The published test set contains 4,208 records with sensitivity 0.72; preprint v2 uses 4,528 and reports 0.73. The revision changes data cleaning; these notes use the published results.

## Code and references

[Code and project](https://github.com/Model-Medicines/TCL-Ames)

TCL comparison models, predictions and statistical code are public, with some large files on Hugging Face. Availability of the complete AmesNet implementation and weights is unconfirmed.

Sources reviewed: **2026-09-22**. Published metadata/abstract, searchable publisher methods, supplementary material, preprint v2 methods and author repository; continuous access to the ACS full text was restricted.

- [Published version](https://pubs.acs.org/crtoec/article/doi/10.1021/acs.chemrestox.6c00082/5170705/AmesNet-A-Task-Conditioned-Deep-Learning-Model)
- [Published abstract](https://pubmed.ncbi.nlm.nih.gov/42371678/)
- [Published supplement](https://doi.org/10.1021/acs.chemrestox.6c00082.s001)
- [Author code and predictions](https://github.com/Model-Medicines/TCL-Ames)
