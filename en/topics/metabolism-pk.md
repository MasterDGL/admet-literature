# Metabolism and pharmacokinetics

**English** | [简体中文](../../topics/metabolism-pk.md)

[Home](../../README.md) · [All reading routes](../docs/reading-routes.md) · [Knowledge map](../docs/knowledge-map.md)

Connect CYP activity and microsomal stability with human clearance, half-life and volume of distribution to understand how in vitro endpoints inform in vivo PK prediction.

## Suggested reading order

1. [TDC](../papers/admet/tdc-2021.md): Start with definitions of CYP, microsomal/hepatocyte clearance and half-life tasks.
2. [PharmaBench](../papers/admet/pharmabench-2024.md): Examine how assay conditions and data cleaning affect labels and model comparisons.
3. [HimNet](../papers/admet/himnet-2026.md): Study a dedicated stability model and the contribution of hierarchical molecular representations.
4. [PKSmart](../papers/admet/pksmart-2025.md): Explore cross-species modeling for human PK and examine external validation.

## Questions to compare

- Is the target CYP inhibition/substrate status, in vitro stability, or an in vivo PK parameter? Which species and units are used?
- Are cross-species inputs measured or predicted, and will those inputs be available at test time?
- What generalization question does each random, scaffold or external evaluation address?

## Papers, newest first

| Date | Paper | Venue | Status | Overview |
| --- | --- | --- | --- | --- |
| 2026-02-14 | [A hierarchical interaction message net for accurate molecular property prediction](../papers/admet/himnet-2026.md) | Communications Chemistry | Published | Exchanges information across atoms, substructures and whole molecules in a hierarchical graph network for property and selected ADMET predictions. |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | Published | Predicts animal pharmacokinetic parameters, then combines them with molecular features to estimate human intravenous clearance, distribution volume and half-life. |
| 2024-09-10 | [PharmaBench: Enhancing ADMET benchmarks with large language models](../papers/admet/pharmabench-2024.md) | Scientific Data | Published | Uses language models to extract assay conditions, then cleans and harmonizes ADMET records to build better-specified benchmarks. |
| 2024-06-24 | [ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries](../papers/admet/admet-ai-2024.md) | Bioinformatics | Published | Packages graph neural networks into web and local tools that predict multiple ADMET properties for large compound libraries. |
| 2024-04-22 | [admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties](../papers/admet/admetsar-3-2024.md) | Nucleic Acids Research | Published | Integrates ADMET data search, property prediction and structural optimization suggestions to help identify suitable candidates. |
| 2024-04-04 | [ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support](../papers/admet/admetlab-3-2024.md) | Nucleic Acids Research | Published | Provides online ADMET and physicochemical predictions with uncertainty estimates, an API and decision-support tools. |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | Published | Selects useful auxiliary tasks for each ADMET endpoint to reduce interference during multitask training. |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | Published | Organizes drug-discovery datasets and tasks into shared interfaces and benchmarks for consistent model comparison. |
