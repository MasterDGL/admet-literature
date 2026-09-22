# AmesNet: A Task-Conditioned Deep Learning Model with Enhanced Sensitivity and Generalization in Ames Mutagenicity Prediction

**English** | [简体中文](../../../papers/admet/amesnet-2026.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Chemical Research in Toxicology · 2026-06-29* · Published · Core papers

**Overview:** Combines molecular structure, bacterial strain and metabolic-activation conditions to improve Ames mutagenicity detection in unfamiliar chemical space.

Topics: AMES, Assay conditions, Out-of-distribution prediction.

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

**Design.** The published Lui dataset has 40,129 training/validation and 4,208 test records after curation; a record is a compound–strain–S9 combination. Source OOD partitions are retained, removing identical non-stereochemical SMILES across partitions. Comparators include STL, ungrouped/grouped multi-task models and conditioned ChemProp, GROVER and RF variants.

| Test | AmesNet | Comparator | Source |
| --- | --- | --- | --- |
| Lui OOD sensitivity | 0.72 (95% CI 0.68–0.76) | Reimplemented DeepAmes 0.69 (0.64–0.73) | Published main results |
| Lui OOD balanced accuracy | 0.81 (0.78–0.83) | Reimplemented DeepAmes 0.76 (0.73–0.78) | Published main results |
| Foil balanced accuracy | 0.72 (0.71–0.73) | STL-GROVER 0.70 (0.69–0.71) | Supplementary Fig. S1 |
| Foil sensitivity | 0.64 (0.62–0.66) | STL-DeepAmes 0.97 (0.96–0.98) | Supplementary Fig. S1 |

Foil intervals use 1,000 stratified bootstrap samples. STL-DeepAmes has high sensitivity but balanced accuracy 0.51 on that set, illustrating the need to also evaluate false positives.

The published main test set has 4,208 records versus 4,528 in preprint v2. Results here use the published version. Foil lacks strain/S9 metadata and is treated as a separate setting.

## Code and references

[Code and project](https://github.com/Model-Medicines/TCL-Ames)

The author repository provides comparator training code, some checkpoints, AmesNet predictions and bootstrap analysis; it does not list a training-code or weights entry for the main AmesNet model

Sources reviewed: **2026-09-22**. Checked the published abstract, searchable main-result passages, published Supplementary Fig. S1 and the author repository tree; training details also draw on earlier version records

- [Published version](https://pubs.acs.org/crtoec/article/doi/10.1021/acs.chemrestox.6c00082/5170705/AmesNet-A-Task-Conditioned-Deep-Learning-Model)
- [Published abstract](https://pubmed.ncbi.nlm.nih.gov/42371678/)
- [Published supplement](https://doi.org/10.1021/acs.chemrestox.6c00082.s001)
- [Author code and predictions](https://github.com/Model-Medicines/TCL-Ames)
- [Published supplement, Fig. S1](https://acs.figshare.com/articles/journal_contribution/32825956)
