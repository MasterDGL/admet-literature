# MoleculeACE

**English** | [简体中文](../../../papers/foundations/moleculeace-2022.md)

**Exposing the Limitations of Molecular Machine Learning with Activity Cliffs**

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

**Overview:** Evaluates structurally similar molecules with large activity differences to expose model weaknesses hidden by average prediction errors.

Category: Data and benchmarks. Topics: Activity cliffs, Bioactivity, Evaluation.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Chemical Information and Modeling 62(23), 5938–5951; 2022-12-01; with a 2023 correction. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Overall error does not adequately capture activity-cliff performance, which matters for lead optimization. |
| Datasets | Curated bioactivity datasets for 30 macromolecular targets, comparing 24 machine-learning strategies. The authors provide data and evaluation workflows. |
| Method | Defines structurally similar pairs with large activity differences and reports overall RMSE alongside cliff-molecule RMSEcliff, comparing descriptor models with graph/sequence neural networks. |
| Findings | Several descriptor-based methods outperform more complex deep models in the tested activity-cliff settings. Performance varies by target, supporting separate cliff metrics. |

DOI: `10.1021/acs.jcim.2c01073`

## Experimental setup and analysis

Analyzes overall RMSE and RMSEcliff with fixed data/code versions and cliff definitions. A 2023 correction revises the early-stopping description.

The focus is bioactivity differences among similar structures. Original-paper and later implementation results are recorded separately to track changes in data and code.

## Code and references

[Code and project](https://github.com/molML/MoleculeACE)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Bibliographic metadata, relevant methods and results, and the listed official resources.

- [Published paper](https://doi.org/10.1021/acs.jcim.2c01073)
- [Published correction](https://doi.org/10.1021/acs.jcim.3c00423)
- [Author benchmark](https://github.com/molML/MoleculeACE)
