# Prediction of Human Clearance Using In Silico Models with Reduced Bias

**English** | [简体中文](../../../papers/admet/human-clearance-bias-2024.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Molecular Pharmaceutics · 2024-01-29* · Published · Further reading

**Overview:** Removes structurally similar and same-class training compounds to evaluate human clearance prediction for new chemistry.

Topics: Human clearance, Generalization, Conformal prediction, Random forest.

| Field | Details |
| --- | --- |
| Publication and date | Molecular Pharmaceutics 21(3), 1192–1203; online 2024-01-29, issue 2024-03-04. |
| Date basis | Publisher online publication date. |
| Publication status | Journal article |
| Research problem | Structural neighbors and therapeutic-class relationships affect generalization estimates for human clearance models. |
| Datasets | A collection of 1,340 compounds with human intravenous PK data; Test343 contains 343 compounds for quasi-prospective testing. Clearance is measured in mL/min/kg. |
| Method | Descriptor-based random forests are compared with ChemProp and PLS. R4 removes same structural–therapeutic-class compounds or neighbors with Tanimoto similarity >0.7 and trains a separate model for each test molecule. Conformal prediction supplies intervals. |
| Findings | On Test343, RF GMFE changes from 3.11 in R3 to 3.33 after neighbor exclusion in R4; the fraction within two-fold error falls from 44% to 41%. |

DOI: `10.1021/acs.molpharmaceut.3c00812`

## Experimental setup and analysis

**Design.** R3 uses one model trained on Lombardo 2014 data. R4 trains 343 models, each after test-molecule-specific exclusions.

| Model | GMFE ↓ | Within two-fold ↑ | Within three-fold ↑ |
| --- | --- | --- | --- |
| RF R3 | 3.11 | 44% | 60% |
| RF R4 | 3.33 | 41% | 57% |
| ChemProp CP4 | 3.27 | 39% | 57% |
| PLS4 | 4.80 | 36% | 53% |

Source: Table S9. CP4/PLS4 use corresponding per-molecule exclusions. Table S8 reports R4 GMFE 11.66 for 47 compounds with clearance >20.7 mL/min/kg, exposing a high-error subgroup.

Errors vary by clearance mechanism and range. Per-test-molecule retraining in R4 is a distinct protocol from evaluating one fixed model.

## Code and references

[Code and project](https://acs.figshare.com/articles/dataset/25104249)

Publisher attachments provide a KNIME workflow ZIP and data XLSX; files were inspected but the workflow was not executed.

Sources reviewed: **2026-09-22**. Checked the official abstract, Tables S3/S8/S9, data XLSX and KNIME archive; models were not reproduced.

- [Official abstract and publication dates](https://pubmed.ncbi.nlm.nih.gov/38285644/)
- [Official supplement: Tables S3, S8 and S9](https://acs.figshare.com/articles/journal_contribution/25104243)
- [Human clearance data XLSX](https://acs.figshare.com/articles/dataset/25104246)
- [Author KNIME workflow](https://acs.figshare.com/articles/dataset/25104249)
