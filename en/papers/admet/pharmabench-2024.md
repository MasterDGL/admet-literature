# PharmaBench

**English** | [简体中文](../../../papers/admet/pharmabench-2024.md)

**PharmaBench: Enhancing ADMET benchmarks with large language models**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**In one sentence:** Uses language models to extract assay conditions, then cleans and harmonizes ADMET records to build better-specified benchmarks.

Category: Data and benchmarks. Topics: Data curation, Assay conditions.

| Field | Details |
| --- | --- |
| Publication and date | Scientific Data 11, 985; 2024-09-10 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Inconsistent assay conditions and endpoint definitions reduce benchmark quality when labels are simply pooled. |
| Datasets | 156,618 raw records from 14,401 bioassays, curated into 52,482 records across 11 ADMET datasets. |
| Method | Language-model-assisted assay-information extraction, followed by curation of structures, units, duplicates and assay conditions, with modeling splits provided. |
| Findings | Harmonizes assay conditions and data processing to provide ADMET modeling datasets with clearer experimental context. |

DOI: `10.1038/s41597-024-03793-0`

## Experimental setup and analysis

Benchmark construction focuses on assay conditions, units, structure cleaning and data splitting.

The workflow can guide data cleaning and label harmonization. Merging with other public data requires duplicate checks by source and molecular structure.

## Code and references

[Code and project](https://github.com/mindrank-ai/PharmaBench)

The authors provide a public code/project page.

Sources reviewed: **2026-09-19**. Bibliographic metadata, key sections of the paper and related official resources.

- [Publisher full text](https://www.nature.com/articles/s41597-024-03793-0)
- [Author resources](https://github.com/mindrank-ai/PharmaBench)
