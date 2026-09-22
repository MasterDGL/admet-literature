# ADMET-AI

**English** | [简体中文](../../../papers/admet/admet-ai-2024.md)

**ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Packages graph neural networks into web and local tools that predict multiple ADMET properties for large compound libraries.

Category: Core papers. Topics: ADMET, Platform, High throughput.

| Field | Details |
| --- | --- |
| Publication and date | Bioinformatics 40(7), btae416; online 2024-06-24; July 2024 issue. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Large-scale screening requires accurate multi-endpoint predictions, high throughput and local deployment. |
| Datasets | 41 TDC prediction tasks: 31 classification and 10 regression tasks. Performance rankings use the 22-task ADMET Benchmark Group subset. |
| Method | The paper uses Chemprop D-MPNN with 200 RDKit descriptors, separate multitask classification and regression models, and model ensembles. |
| Findings | At publication, the authors reported a leading average TDC ADMET rank and high batch-processing efficiency, with both web and local tools available. |

DOI: `10.1093/bioinformatics/btae416`

## Experimental setup and analysis

Training covers 41 tasks; performance rankings use 22 ADMET benchmark tasks. Figure 1B–C compares predictive performance and runtime.

Inference speed depends on hardware and batch size. Version 2 changes the Chemprop version and feature configuration, so paper reproduction requires the corresponding software version.

## Code and references

[Code and project](https://github.com/swansonk14/admet_ai)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11226862/)
- [Author code and version notes](https://github.com/swansonk14/admet_ai)
