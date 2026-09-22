# A multimodal contrastive learning framework for predicting P-glycoprotein substrates and inhibitors

**English** | [简体中文](../../../papers/admet/mc-pgp-2025.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Pharmaceutical Analysis · 2025-08* · Published · Core papers

**Overview:** Fuses SMILES, fingerprints and molecular graphs to separately predict P-gp inhibition and transport-substrate status.

Topics: P-gp, Multimodal learning, External validation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Pharmaceutical Analysis 15(8), 101313; August 2025 issue (PubMed article date: 2025-04-16). |
| Date basis | Journal issue month; PubMed article date listed separately |
| Publication status | Journal article |
| Research problem | Single representations miss P-gp-related structural information. Inhibitors and substrates require distinct tasks and evaluation on compounds from new sources. |
| Datasets | Public databases/literature: 5,943 molecules for inhibition (4,558 positives, 1,385 negatives) and 4,018 for substrate prediction (2,455 positives, 1,563 negatives). Independent external sets contain 140 and 185 molecules, respectively. |
| Method | Attention fuses SMILES sequences, fingerprints and graphs. Graph contrastive learning aligns local and global structure, with analysis of relevant functional groups. |
| Findings | External AUROC is 0.906±0.015 for inhibitors and 0.906±0.022 for substrates; FP-GNN scores 0.825±0.015 and 0.819±0.027 on the same tests. Absolute gains are 0.081 and 0.087. |

DOI: `10.1016/j.jpha.2025.101313`

## Experimental setup and analysis

**Design.** Inhibitor and substrate collections contain 5,943 and 4,018 molecules. Both use random and scaffold 8:1:1 splits, 30 Bayesian optimization trials on validation data, and ten seeds. External sets contain 140 and 185 molecules, evaluated with models from the random-split experiments.

| Evaluation | MC-PGP AUROC ↑ | Comparator AUROC ↑ | Location |
| --- | --- | --- | --- |
| Inhibitors, random | 0.939±0.006 | CMMS-GCL 0.928±0.010 | Table 2 |
| Inhibitors, scaffold | 0.857±0.009 | FP-GNN 0.832±0.010 | Table 3 |
| Inhibitors, external | 0.906±0.015 | FP-GNN 0.825±0.015 | Table 4 |
| Substrates, external | 0.906±0.022 | FP-GNN 0.819±0.027 | Table 5 |

The reported 9.82%/10.62% improvements are relative; absolute AUROC gains are 0.081/0.087.

Inhibition and substrate transport are separate tasks. The inhibitor AUROC drop from random to scaffold splitting demonstrates the remaining challenge of generalizing to new scaffolds.

## Code and references

Public availability of the complete training implementation remains to be verified.

Sources reviewed: **2026-09-22**. Checked training protocol, external-set descriptions and Tables 2–5

- [Open full text and result tables](https://pmc.ncbi.nlm.nih.gov/articles/PMC12409376/)
- [Journal page](https://jpa.xjtu.edu.cn/en/article/doi/10.1016/j.jpha.2025.101313)
- [TDC P-gp task definition](https://tdcommons.ai/single_pred_tasks/adme/)
