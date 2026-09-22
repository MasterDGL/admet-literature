# Absorption and distribution

**English** | [简体中文](../../topics/absorption-distribution.md)

[Home](../../README.md) · [All reading routes](../docs/reading-routes.md) · [Knowledge map](../docs/knowledge-map.md)

Explore intestinal permeability, the blood–brain barrier and P-gp transport to understand absorption, tissue access and transporter effects.

## Suggested reading order

1. [TDC](../papers/admet/tdc-2021.md): Distinguish Caco-2, BBB, P-gp and plasma protein binding endpoints and their metrics.
2. [CaliciBoost](../papers/admet/caliciboost-2025.md): Study data preparation, features and model selection for a dedicated Caco-2 predictor.
3. [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md): Follow BBB prediction from a molecular language model to in vitro validation.
4. [MC-PGP](../papers/admet/mc-pgp-2025.md): Compare P-gp inhibition and substrate prediction across random, scaffold and external tests.

## Questions to compare

- Does the label measure permeability, barrier penetration, or transporter substrate/inhibitor status?
- How does performance change on new scaffolds or external data?
- Which predictions have in vitro support, and how does the assay relate to the intended application?

## Papers, newest first

| Date | Paper | Venue | Status | Overview |
| --- | --- | --- | --- | --- |
| 2025-12-22 | [CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction](../papers/admet/caliciboost-2025.md) | Journal of Cheminformatics | Published | Combines molecular fingerprints, physicochemical descriptors and automated machine learning to predict permeability through the Caco-2 intestinal cell model. |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | Published | Predicts animal pharmacokinetic parameters, then combines them with molecular features to estimate human intravenous clearance, distribution volume and half-life. |
| 2025-07-31 | [MMPK: A Multimodal Deep Learning Framework to Predict Human Oral Pharmacokinetic Parameters](../papers/admet/mmpk-2025.md) | Journal of Medicinal Chemistry | Published | Combines molecular graphs, substructure graphs, SMILES and dose to predict eight human oral pharmacokinetic parameters. |
| 2025-04-16 | [A multimodal contrastive learning framework for predicting P-glycoprotein substrates and inhibitors](../papers/admet/mc-pgp-2025.md) | Journal of Pharmaceutical Analysis | Published | Fuses SMILES, fingerprints and molecular graphs to separately predict P-gp inhibition and transport-substrate status. |
| 2024-07-09 | [Predicting blood–brain barrier permeability of molecules with a large language model and machine learning](../papers/admet/bbb-megamolbart-2024.md) | Scientific Reports | Published | Predicts blood–brain barrier permeability with a molecular language model and XGBoost, then tests selected compounds in human-derived 3D BBB spheroids. |
| 2024-06-24 | [ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries](../papers/admet/admet-ai-2024.md) | Bioinformatics | Published | Packages graph neural networks into web and local tools that predict multiple ADMET properties for large compound libraries. |
| 2024-04-22 | [admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties](../papers/admet/admetsar-3-2024.md) | Nucleic Acids Research | Published | Integrates ADMET data search, property prediction and structural optimization suggestions to help identify suitable candidates. |
| 2024-04-04 | [ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support](../papers/admet/admetlab-3-2024.md) | Nucleic Acids Research | Published | Provides online ADMET and physicochemical predictions with uncertainty estimates, an API and decision-support tools. |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | Published | Selects useful auxiliary tasks for each ADMET endpoint to reduce interference during multitask training. |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | Published | Organizes drug-discovery datasets and tasks into shared interfaces and benchmarks for consistent model comparison. |
