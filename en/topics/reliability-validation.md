# Reliability and experimental validation

**English** | [简体中文](../../topics/reliability-validation.md)

[Home](../../README.md) · [All reading routes](../docs/reading-routes.md) · [Knowledge map](../docs/knowledge-map.md)

Use data splits, activity cliffs, uncertainty and experimental validation to assess where predictions work and whether failures can be detected.

## Suggested reading order

1. [MoleculeNet](../papers/foundations/moleculenet-2018.md): Start with how benchmarks, tasks and splits define an evaluation question.
2. [MoleculeACE](../papers/foundations/moleculeace-2022.md): Examine whether average scores hide large activity differences among similar molecules.
3. [Atom-based uncertainty](../papers/foundations/atom-uncertainty-2023.md): Connect atom-level uncertainty to molecular prediction errors and structural interpretation.
4. [ADMET reliability benchmark](../papers/admet/admet-reliability-2026.md): Examine model failures under small-data and generalization evaluations.
5. [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md): Follow an in vitro validation study and distinguish model scores from experimental observations.
6. [Human clearance with reduced bias](../papers/admet/human-clearance-bias-2024.md): Compare clearance errors with and without neighbor exclusion, including high-error subgroups.

## Questions to compare

- Does testing isolate new molecules, new scaffolds and new data sources?
- Beyond average scores, are activity cliffs, error distributions and uncertainty calibration examined?
- Which predictions were tested in new experiments, and what conclusions do those experiments support?

## Papers, newest first

| Date | Paper | Venue | Status | Overview |
| --- | --- | --- | --- | --- |
| 2026-05-25 | [Mapping the avoid-ome: a systematic open-science approach to predictive ADMET](../papers/admet/openadmet-avoidome-2026.md) | Nature Communications | Published | Proposes combining open experimental data, protein structures, active learning and blind challenges to improve mechanistic ADMET prediction. |
| 2026-05-18 | [Revisiting ADMET prediction reliability under real-world challenges in the foundation model era](../papers/admet/admet-reliability-2026.md) | Journal of Cheminformatics | Published | Compares model families under limited data, unfamiliar molecular structures and class imbalance to assess ADMET prediction in practical research settings. |
| 2026-02-28 | [Critical Assessment of ML models for ADMET Prediction in TDC leaderboards](../papers/admet/tdc-audit-2026.md) | bioRxiv | 🟠 **Preprint** | Checks whether leading TDC models run, contain data leakage and reproduce their reported ADMET results. |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | Published | Predicts animal pharmacokinetic parameters, then combines them with molecular features to estimate human intravenous clearance, distribution volume and half-life. |
| 2025-07-31 | [MMPK: A Multimodal Deep Learning Framework to Predict Human Oral Pharmacokinetic Parameters](../papers/admet/mmpk-2025.md) | Journal of Medicinal Chemistry | Published | Combines molecular graphs, substructure graphs, SMILES and dose to predict eight human oral pharmacokinetic parameters. |
| 2025-01-06 | [Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation](../papers/admet/molmcl-2025.md) | Nature Communications | Published | Learns molecular, scaffold and local-context representations, then combines them by task for property and bioactivity prediction. |
| 2024-09-10 | [PharmaBench: Enhancing ADMET benchmarks with large language models](../papers/admet/pharmabench-2024.md) | Scientific Data | Published | Uses language models to extract assay conditions, then cleans and harmonizes ADMET records to build better-specified benchmarks. |
| 2024-07-09 | [Predicting blood–brain barrier permeability of molecules with a large language model and machine learning](../papers/admet/bbb-megamolbart-2024.md) | Scientific Reports | Published | Predicts blood–brain barrier permeability with a molecular language model and XGBoost, then tests selected compounds in human-derived 3D BBB spheroids. |
| 2024-01-29 | [Prediction of Human Clearance Using In Silico Models with Reduced Bias](../papers/admet/human-clearance-bias-2024.md) | Molecular Pharmaceutics | Published | Removes structurally similar and same-class training compounds to evaluate human clearance prediction for new chemistry. |
| 2023-02-03 | [Explainable uncertainty quantifications for deep learning-based molecular property prediction](../papers/foundations/atom-uncertainty-2023.md) | Journal of Cheminformatics | Published | Attributes uncertainty to atoms to locate unfamiliar structures and potential noise, then calibrates ensemble confidence estimates. |
| 2022-12-01 | [Exposing the Limitations of Molecular Machine Learning with Activity Cliffs](../papers/foundations/moleculeace-2022.md) | Journal of Chemical Information and Modeling | Published | Evaluates structurally similar molecules with large activity differences to expose model weaknesses hidden by average prediction errors. |
| 2022-01-26 | [Machine learning-driven identification of drugs inhibiting cytochrome P450 2C9](../papers/admet/cyp2c9-ml-validation-2022.md) | PLOS Computational Biology | Published | Combines molecular descriptors and CYP2C9 ensemble docking to screen inhibitors, then tests selected drugs experimentally. |
| 2021-05-27 | [Deep Learning-Based Conformal Prediction of Toxicity](../papers/admet/tox21-conformal-2021.md) | Journal of Chemical Information and Modeling | Published | Adds conformal prediction to toxicity models, returning one or multiple candidate labels at a chosen confidence level and assessing uncertainty and missed toxic compounds. |
| 2017-10-31 | [MoleculeNet: a benchmark for molecular machine learning](../papers/foundations/moleculenet-2018.md) | Chemical Science | Published | Brings molecular datasets, splits, metrics and algorithms into a shared benchmark for property prediction. |
