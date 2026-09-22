# ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection

**English** | [简体中文](../../../papers/admet/mtgl-admet-2023.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*iScience · 2023-10-24* · Published · Core papers

**Overview:** Selects useful auxiliary tasks for each ADMET endpoint to reduce interference during multitask training.

Topics: Multitask learning, Auxiliary tasks, Negative transfer.

| Field | Details |
| --- | --- |
| Publication and date | iScience 26(11), 108285; published online 2023-10-24, November 2023 issue. A preceding conference version appeared at RECOMB 2023. |
| Date basis | Online publication date; issue month listed separately. |
| Publication status | Journal article |
| Research problem | Training all ADMET tasks together can cause negative transfer; each primary task may need a different auxiliary-task set. |
| Datasets | 24 endpoints collected from 8 publications: 18 classification and 6 regression tasks, covering 43,291 compounds and including ADMET plus 2 physicochemical endpoints. |
| Method | Uses state theory and maximum flow for auxiliary-task selection, together with shared atom representations, task-specific attention and a primary-task-centered gating module. |
| Findings | Under the paper’s common evaluation, MTGL-ADMET has the highest mean on 20/24 endpoints and ranks second on four. P-gp substrate AUROC is 0.801±0.031 versus MGA’s 0.719±0.035, supporting task-specific auxiliary selection. |

DOI: `10.1016/j.isci.2023.108285`

## Experimental setup and analysis

**Design.** The collection contains 43,291 compounds and 24 endpoints (18 classification, six regression). Random 8:1:1 splits use ten seeds; validation data select auxiliary tasks. Baselines are ST-GCN, ST-MGA, MT-GCN, MT-GCNAtt and MGA.

| Endpoint | Metric | MTGL-ADMET | MGA |
| --- | --- | --- | --- |
| P-gp substrate | AUROC ↑ | 0.801±0.031 | 0.719±0.035 |
| BBB | AUROC ↑ | 0.973±0.005 | 0.956±0.010 |
| Caco-2 | R² ↑ | 0.523±0.025 | 0.385±0.031 |
| ESOL | R² ↑ | 0.931±0.038 | 0.866±0.020 |

Source: Table 1, mean±SD. MGA has higher means for CYP2C9 inhibition, CYP2D6 inhibition and hepatotoxicity; ST-MGA leads respiratory toxicity.

Half-life and clearance are classification tasks here, and Caco-2 uses R². These task definitions and random splits differ from the corresponding TDC benchmarks.

## Code and references

[Code and project](https://github.com/dubingxue/MTGL-ADMET)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked STAR Methods, the 24-endpoint collection and Table 1

- [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10654589/)
- [Alternative full text](https://europepmc.org/articles/PMC10654589)
- [Author code](https://github.com/dubingxue/MTGL-ADMET)
