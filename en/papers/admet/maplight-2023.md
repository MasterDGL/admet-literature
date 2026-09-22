# ADMET property prediction through combinations of molecular fingerprints

**English** | [简体中文](../../../papers/admet/maplight-2023.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*arXiv · 2023-09-29* · 🟠 **Preprint** · Preprints

**Overview:** Combines molecular fingerprints and descriptors in CatBoost models to assess the strength of conventional features for ADMET prediction.

Topics: Fingerprints, CatBoost, Baselines.

| Field | Details |
| --- | --- |
| Publication and date | arXiv preprint, initially submitted 2023-09-29; these notes cover that version. |
| Date basis | Initial arXiv submission date; revisions listed in the citation |
| Publication status | 🟠 **Preprint** |
| Research problem | Can simple, computationally inexpensive feature-based models remain competitive with deep learning? |
| Datasets | 22 TDC ADMET tasks. |
| Method | Combines ECFP, Avalon, ErG and molecular descriptors in CatBoost, with an additional variant incorporating GNN representations. |
| Findings | Fingerprint combinations perform well on multiple ADMET endpoints and provide useful baselines. A subsequent third-party audit reports that two MapLight variants passed its checks. |

## Experimental setup and analysis

Evaluates model variants on 22 TDC ADMET tasks; a separate third-party preprint audits the reproducibility of two variants.

Fingerprint combinations offer practical endpoint-modeling baselines. Read third-party audit results alongside the code versions and checks used.

## Code and references

[Code and project](https://github.com/maplightrx/MapLight-TDC)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Preprint](https://arxiv.org/abs/2310.00174)
- [Author code](https://github.com/maplightrx/MapLight-TDC)
