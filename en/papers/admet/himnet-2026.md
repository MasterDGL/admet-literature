# HimNet

**English** | [简体中文](../../../papers/admet/himnet-2026.md)

**A hierarchical interaction message net for accurate molecular property prediction**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**In one sentence:** Exchanges information across atoms, substructures and whole molecules in a hierarchical graph network for property and selected ADMET predictions.

Category: Further reading. Topics: Hierarchical GNN, Metabolic stability.

| Field | Details |
| --- | --- |
| Publication and date | Communications Chemistry 9, 150; 2026-02-14 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Limited interaction across atom, substructure and molecular levels can leave property-relevant information out of single-level representations. |
| Datasets | 11 datasets: 8 MoleculeNet subsets plus Malaria, LMC and MetStab. BBBP, Tox21, SIDER, ClinTox and metabolic-stability tasks directly concern ADMET; others assess broader properties or bioactivity. |
| Method | Hierarchical message passing and attention combine directed message paths, cross-level interactions and consistency information from multiple fingerprints. |
| Findings | Tables 1–2 report best or near-best results on several tasks among the compared methods, supporting hierarchical feature fusion. |

DOI: `10.1038/s42004-026-01922-x`

## Experimental setup and analysis

Tables 1–2 summarize 11 property/activity datasets. These notes cover the main comparisons; task-specific splits and hyperparameters remain to be added.

Useful for studying hierarchical feature fusion alongside metabolic-stability tasks, especially how representations at different levels affect performance.

## Code and references

Code link to be added.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://www.nature.com/articles/s42004-026-01922-x)
