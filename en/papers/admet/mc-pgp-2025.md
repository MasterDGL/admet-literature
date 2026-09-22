# MC-PGP

**English** | [简体中文](../../../papers/admet/mc-pgp-2025.md)

**A multimodal contrastive learning framework for predicting P-glycoprotein substrates and inhibitors**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**In one sentence:** Fuses SMILES, fingerprints and molecular graphs to separately predict P-gp inhibition and transport-substrate status.

Category: Core papers. Topics: P-gp, Multimodal learning, External validation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Pharmaceutical Analysis 15(8), 101313; August 2025 issue (PubMed article date: 2025-04-16). |
| Date basis | Journal issue month; PubMed article date listed separately |
| Publication status | Journal article |
| Research problem | Single representations miss P-gp-related structural information. Inhibitors and substrates require distinct tasks and evaluation on compounds from new sources. |
| Datasets | Public databases/literature: 5,943 molecules for inhibition (4,558 positives, 1,385 negatives) and 4,018 for substrate prediction (2,455 positives, 1,563 negatives). Independent external sets contain 140 and 185 molecules, respectively. |
| Method | Attention fuses SMILES sequences, fingerprints and graphs. Graph contrastive learning aligns local and global structure, with analysis of relevant functional groups. |
| Findings | External inhibitor AUROC is 0.906 ± 0.015. The authors report relative AUROC improvements of 9.82%/10.62% over the next-best method on the inhibitor/substrate external sets. |

DOI: `10.1016/j.jpha.2025.101313`

## Experimental setup and analysis

Internal comparisons use random and scaffold splits; Tables 4–5 report external results. The 9.82%/10.62% values are relative AUROC improvements over the next-best method.

Inhibition and substrate status are evaluated separately, each with positive and negative examples. The corresponding TDC Pgp_Broccatelli task concerns inhibitor classification.

## Code and references

Public availability of the complete training implementation remains to be verified.

Sources reviewed: **2026-09-22**. Bibliographic metadata, relevant methods and results, and the listed official resources.

- [Open full text and result tables](https://pmc.ncbi.nlm.nih.gov/articles/PMC12409376/)
- [Journal page](https://jpa.xjtu.edu.cn/en/article/doi/10.1016/j.jpha.2025.101313)
- [TDC P-gp task definition](https://tdcommons.ai/single_pred_tasks/adme/)
