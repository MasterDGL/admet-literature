# TDC model audit

**English** | [简体中文](../../../papers/admet/tdc-audit-2026.md)

**Critical Assessment of ML models for ADMET Prediction in TDC leaderboards**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Checks whether leading TDC models run, contain data leakage and reproduce their reported ADMET results.

Category: Preprints. Topics: Reproducibility, Data leakage, Model audit.

| Field | Details |
| --- | --- |
| Publication and date | bioRxiv preprint, 2026; Crossref publication date 2026-02-28; the DOI contains 02-26. |
| Date basis | Crossref preprint publication date; DOI date recorded separately |
| Publication status | 🟠 **Preprint** |
| Research problem | Leaderboard results may depend on pretraining leakage, validation/test overlap or environment problems that affect reproducibility. |
| Datasets | 10 leading methods selected from the 22-task TDC ADMET benchmark, using the audit's leaderboard snapshot and code versions. |
| Method | Sequentially checks environment availability, pretraining leakage, validation/test overlap and result reproduction. |
| Findings | The authors report that only MapLight, MapLight+GNN and CaliciBoost pass all checks. CaliciBoost addresses Caco-2 specifically, rather than all 22 tasks. |

DOI: `10.64898/2026.02.26.708193`

## Experimental setup and analysis

Audits 10 leading methods for execution, leakage, validation/test overlap and reproduction, recording the relevant leaderboard snapshot and code versions.

The audit separates environment failures from experimental-design issues and can inform reproduction workflows. These notes summarize the preprint's findings.

## Code and references

[Code and project](https://github.com/receptor-ai/tdc-admet-bench)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, abstract and accessible project documentation.

- [Preprint](https://www.biorxiv.org/content/10.64898/2026.02.26.708193v1)
- [Audit code and documentation](https://github.com/receptor-ai/tdc-admet-bench)
