# MoleculeNet

**English** | [简体中文](../../../papers/foundations/moleculenet-2018.md)

**MoleculeNet: a benchmark for molecular machine learning**

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

**Overview:** Brings molecular datasets, splits, metrics and algorithms into a shared benchmark for property prediction.

Category: Data and benchmarks. Topics: Datasets, Benchmarks, Evaluation.

| Field | Details |
| --- | --- |
| Publication and date | Chemical Science 9(2), 513–530 (2018 issue); online 2017-10-31. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Different choices of datasets, metrics and implementations make model improvements difficult to separate from evaluation effects. |
| Datasets | Public quantum-chemical, physicochemical, biophysical and physiological datasets, including ESOL, FreeSolv, Lipophilicity, BBBP, Tox21, ClinTox, SIDER, BACE, HIV and QM collections, with task-specific metrics and splits. |
| Method | DeepChem data loaders, molecular featurizers and learning algorithms support systematic comparisons of fixed descriptors and learned representations. |
| Findings | Learned representations work across multiple tasks, while small datasets and imbalance remain challenging. Physically informed features can matter more than algorithm choice in quantum/biophysical tasks. |

DOI: `10.1039/C7SC02664A`

## Experimental setup and analysis

Metrics and splits are task-specific; comparisons should record the subset, data version, cleaning steps and split.

Coverage includes ADMET, activity, physicochemical and quantum-chemical tasks. DeepChem loading workflows evolve. Publication metadata records the publisher's 2017-10-31 online date alongside the 2018 issue.

## Code and references

[Code and project](https://github.com/deepchem/deepchem)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Publisher metadata, abstract/benchmark description and official DeepChem resources; individual subsets have not been run.

- [Publisher article](https://pubs.rsc.org/en/content/articlelanding/2017/sc/c7sc02664a)
- [DeepChem](https://github.com/deepchem/deepchem)
