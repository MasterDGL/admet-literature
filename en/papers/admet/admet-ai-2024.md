# ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries

**English** | [简体中文](../../../papers/admet/admet-ai-2024.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Bioinformatics · 2024-06-24* · Published · Core papers

**Overview:** Packages graph neural networks into web and local tools that predict multiple ADMET properties for large compound libraries.

Topics: ADMET, Platform, High throughput.

| Field | Details |
| --- | --- |
| Publication and date | Bioinformatics 40(7), btae416; online 2024-06-24; July 2024 issue. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Large-scale screening requires accurate multi-endpoint predictions, high throughput and local deployment. |
| Datasets | 41 TDC prediction tasks: 31 classification and 10 regression tasks. Performance rankings use the 22-task ADMET Benchmark Group subset. |
| Method | The paper uses Chemprop D-MPNN with 200 RDKit descriptors, separate multitask classification and regression models, and model ensembles. |
| Findings | Single-task models exceed AUROC 0.85 on 20/31 classification tasks and R² 0.6 on 5/10 regression tasks. Multi-task models perform similarly with faster inference. The 32-core CPU plus GPU timing is 3.1 hours for one million input records. |

DOI: `10.1093/bioinformatics/btae416`

## Experimental setup and analysis

**Design.** Uses 41 tasks from TDC v0.4.1, including the 22-task ADMET Benchmark Group. Models are trained across five train/validation/test splits; deployment averages five models. Single-task training is compared with separate classification and regression multi-task models.

| Experiment | Result | Location |
| --- | --- | --- |
| Single-task classification, 31 tasks | 20 tasks exceed AUROC 0.85 | Supplementary Fig. S2 |
| Single-task regression, 10 tasks | 5 tasks exceed R² 0.6 | Supplementary Fig. S2 |
| Local 32-core CPU + GPU | 3.1 hours for one million records | Fig. 1C |
| Local 8-core CPU, no GPU | About 5 hours for one million records | Fig. 1C |

**Timing data.** The million-record input repeats 1,000 DrugBank molecules 1,000 times; times are medians of three trials. This measures throughput, not predictive accuracy on one million distinct molecules. Endpoint scores are in Supplementary Table S1.

Paper evaluations, deployed multi-task ensembles and current software releases are distinguished. Version 2 changes Chemprop and feature configuration; use the matching release for paper reproduction.

## Code and references

[Code and project](https://github.com/swansonk14/admet_ai)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Checked training versus deployment, Fig. 1 timing design and supplementary result references

- [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11226862/)
- [Author code and version notes](https://github.com/swansonk14/admet_ai)
