# Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation

**English** | [简体中文](../../../papers/admet/molmcl-2025.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Nature Communications · 2025-01-06* · Published · Further reading

**Overview:** Learns molecular, scaffold and local-context representations, then combines them by task for property and bioactivity prediction.

Topics: Multichannel pretraining, Activity cliffs.

| Field | Details |
| --- | --- |
| Publication and date | Nature Communications 16, 413; 2025-01-06. The DOI contains 2024; publication was in 2025. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Tasks depend on different structural levels, making fixed graph representations and readouts difficult to adapt across tasks. |
| Datasets | ZINC15 for pretraining; 7 MoleculeNet datasets and 30 MoleculeACE bioactivity tasks for downstream evaluation. |
| Method | Multichannel learning over molecular, scaffold and contextual information, using molecular perturbations, contrastive learning and prompt-guided readout. |
| Findings | Multichannel learning and task adaptation improve representations on the evaluated molecular tasks, with activity-cliff experiments demonstrating the design's value. |

DOI: `10.1038/s41467-024-55082-4`

## Experimental setup and analysis

Downstream experiments cover 7 MoleculeNet subsets and 30 MoleculeACE bioactivity tasks.

Activity-cliff experiments help examine representation sensitivity to local structural changes. This MolMCL and MoleMCL in Bioinformatics are separate studies.

## Code and references

[Code and project](https://github.com/yuewan2/MolMCL)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://www.nature.com/articles/s41467-024-55082-4)
- [Author code](https://github.com/yuewan2/MolMCL)
