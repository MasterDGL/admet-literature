# MTGL-ADMET

**English** | [简体中文](../../../papers/admet/mtgl-admet-2023.md)

**ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Selects useful auxiliary tasks for each ADMET endpoint to reduce interference during multitask training.

Category: Core papers. Topics: Multitask learning, Auxiliary tasks, Negative transfer.

| Field | Details |
| --- | --- |
| Publication and date | iScience 26(11), 108285; November 2023 issue. Preceded by a RECOMB 2023 conference paper. |
| Date basis | Journal issue month |
| Publication status | Journal article |
| Research problem | Training all ADMET tasks together can cause negative transfer; each primary task may need a different auxiliary-task set. |
| Datasets | 24 endpoints collected from 8 publications: 18 classification and 6 regression tasks, covering 43,291 compounds and including ADMET plus 2 physicochemical endpoints. |
| Method | Uses state theory and maximum flow for auxiliary-task selection, together with shared atom representations, task-specific attention and a primary-task-centered gating module. |
| Findings | Comparisons and ablations show that adaptive task selection and gating improve prediction, supporting auxiliary-task selection tailored to the primary task. |

DOI: `10.1016/j.isci.2023.108285`

## Experimental setup and analysis

Table 1 uses a random 8:1:1 split and 10 random seeds, with AUROC for classification and R² for regression.

Comparisons focus on auxiliary-task selection and gating. The 24-endpoint collection differs from TDC's 22 tasks in data composition and splitting.

## Code and references

[Code and project](https://github.com/dubingxue/MTGL-ADMET)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10654589/)
- [Alternative full text](https://europepmc.org/articles/PMC10654589)
- [Author code](https://github.com/dubingxue/MTGL-ADMET)
