# Machine learning-driven identification of drugs inhibiting cytochrome P450 2C9

**English** | [简体中文](../../../papers/admet/cyp2c9-ml-validation-2022.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*PLOS Computational Biology · 2022-01-26* · Published · Further reading

**Overview:** Combines molecular descriptors and CYP2C9 ensemble docking to screen inhibitors, then tests selected drugs experimentally.

Topics: CYP2C9, Structural information, Ensemble docking, Experimental validation.

| Field | Details |
| --- | --- |
| Publication and date | PLOS Computational Biology 18(1), e1009820; published 2022-01-26. |
| Date basis | Publisher online publication date. |
| Publication status | Journal article |
| Research problem | CYP2C9 inhibition depends on ligand properties and protein flexibility; computational hits need experimental testing. |
| Datasets | Filtered and clustered PubChem/ChEMBL data: 8,141 compounds, comprising 4,840 inhibitors and 3,301 non-inhibitors, with a stratified random 80/20 holdout. Another 4,480 drugs were screened and 18 selected for experiments. |
| Method | RF/SVM models combine 36 MOE descriptors with docking energies for seven protein conformations. Consensus, energy thresholds and diversity selection prioritize HepG2 and CYP2C9 supersome assays. |
| Findings | RF balanced accuracy is 84.33% and sensitivity 89.97% in Table 3. Testing 18 candidates identifies four stronger inhibitors, including vatalanib with IC50 0.067 μM. |

DOI: `10.1371/journal.pcbi.1009820`

## Experimental setup and analysis

**Design.** The paper’s “external” model test set is a stratified random holdout from the same collection; new-candidate experiments are a separate validation stage.

| Model (Table 3) | Balanced accuracy ↑ | Sensitivity ↑ | Specificity ↑ |
| --- | --- | --- | --- |
| RF, 36 MOE + 7 IE | 84.33% | 89.97% | 78.69% |
| SVM, 36 MOE + 7 IE | 83.35% | 89.87% | 76.83% |

The text defines Table 3’s Accuracy column as balanced accuracy. Table 5 supersome IC50 values: vatalanib 0.067, piriqualone 10.9, ticagrelor 11.8 and cloperidone 17.7 μM.

Enzyme inhibition and in vivo drug interactions are distinct outcomes. Assays establish inhibition under the tested conditions; modeling requires MOE descriptors and docking.

## Code and references

Data and experimental details are provided in the article and supplements; no standalone code repository is listed.

Sources reviewed: **2026-09-22**. Checked full-text data filtering, 80/20 splitting, features, Tables 3/5, candidate selection and assays.

- [Full text, methods and Tables 3 and 5](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009820)
- [Open full text and supporting information](https://pmc.ncbi.nlm.nih.gov/articles/PMC8820617/)
