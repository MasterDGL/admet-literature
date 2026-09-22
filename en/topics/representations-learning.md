# Molecular representations and learning methods

**English** | [简体中文](../../topics/representations-learning.md)

[Home](../../README.md) · [All reading routes](../docs/reading-routes.md) · [Knowledge map](../docs/knowledge-map.md)

Start with fingerprint and descriptor baselines, then compare graph networks, pretraining, multitask learning and ensembles for ADMET prediction.

## Suggested reading order

1. [MolMapNet](../papers/foundations/molmapnet-2021.md): Study how fingerprints and descriptors can be organized into structured feature maps.
2. [Chemprop / D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md): Understand directed bond message passing, descriptor baselines and data splits.
3. [AttentiveFP](../papers/foundations/attentivefp-2019.md): Examine attention in atomic neighborhood aggregation and molecular readout.
4. [KPGT](../papers/admet/kpgt-2023.md): Follow chemical knowledge into graph pretraining and assess transfer across tasks.
5. [MTGL-ADMET](../papers/admet/mtgl-admet-2023.md): Study auxiliary-task selection and negative transfer in multitask learning.

## Questions to compare

- Does the gain come from representation, pretraining data, auxiliary tasks, ensembling or tuning?
- Are splits, search budgets and training data matched when comparing against fingerprint/descriptor baselines?
- How does the pretraining objective relate to downstream endpoints, and which designs are supported by ablations?

## Papers, newest first

| Date | Paper | Venue | Status | Overview |
| --- | --- | --- | --- | --- |
| 2026-09-09 | [ADMET-EvO: a self-evolving scientific agent for sustained research across heterogeneous tasks](../papers/admet/admet-evo-2026.md) | arXiv | 🟠 **Preprint** | Uses a research agent to explore features and models for ADMET tasks, evaluating prediction and research efficiency through a fixed testing workflow. |
| 2026-08-25 | [A multimodal representation learning platform for accurate molecular ADMET prediction](../papers/admet/trimole-hybrid-2026.md) | bioRxiv | 🟠 **Preprint** | Fuses sequences, molecular graphs, 3D structures and chemical priors, selecting prediction models or ensembles for each ADMET task. |
| 2026-06-20 | [DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction](../papers/admet/dcpm-admet-2026.md) | Journal of Cheminformatics | Published | Combines representations from two pretrained models with chemical fingerprints to predict 97 ADMET properties. |
| 2025-01-06 | [Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation](../papers/admet/molmcl-2025.md) | Nature Communications | Published | Learns molecular, scaffold and local-context representations, then combines them by task for property and bioactivity prediction. |
| 2024-11-12 | [MolE: a foundation model for molecular graphs using disentangled attention](../papers/admet/mole-2024.md) | Nature Communications | Published | Pretrains on a large collection of molecular graphs, adds supervised biological-task training, and fine-tunes for ADMET prediction. |
| 2023-11-21 | [A knowledge-guided pre-training framework for improving molecular representation learning](../papers/admet/kpgt-2023.md) | Nature Communications | Published | Incorporates fingerprints and physicochemical descriptors into graph pretraining to learn representations for ADMET and other molecular properties. |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | Published | Selects useful auxiliary tasks for each ADMET endpoint to reduce interference during multitask training. |
| 2023-09-29 | [ADMET property prediction through combinations of molecular fingerprints](../papers/admet/maplight-2023.md) | arXiv | 🟠 **Preprint** | Combines molecular fingerprints and descriptors in CatBoost models to assess the strength of conventional features for ADMET prediction. |
| 2023-04-24 | [Uni-QSAR: an Auto-ML Tool for Molecular Property Prediction](../papers/admet/uni-qsar-2023.md) | arXiv | 🟠 **Preprint** | Automatically combines fingerprints, descriptors and pretrained 1D, 2D and 3D molecular representations with tuning and stacked ensembles for ADMET prediction. |
| 2023 | [Domain-aware representation of small molecules for explainable property prediction models](../papers/admet/domain-aware-pbrics-2023.md) | ICLR 2023 MLDD Workshop | Workshop | Builds chemically meaningful molecular fragments so graph models can predict ADMET properties and identify fragments contributing to each prediction. |
| 2021-11-27 | [Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network](../papers/admet/ssl-gcn-2021.md) | Journal of Cheminformatics | Published | Trains a graph neural network on labeled and unlabeled molecules to improve Tox21 toxicity prediction through semi-supervised learning. |
| 2021-03-01 | [Out-of-the-box deep learning prediction of pharmaceutical properties by broadly learned knowledge-based molecular representations](../papers/foundations/molmapnet-2021.md) | Nature Machine Intelligence | Published | Arranges descriptors and fingerprints into 2D feature maps and trains CNNs to predict physicochemical, pharmacokinetic and toxicity-related properties. |
| 2019-07-30 | [Analyzing Learned Molecular Representations for Property Prediction](../papers/foundations/chemprop-dmpnn-2019.md) | Journal of Chemical Information and Modeling | Published | Learns molecular representations by passing messages along directed chemical bonds and evaluates property prediction on public and industrial data. |
| 2019 | [Pushing the Boundaries of Molecular Representation for Drug Discovery with the Graph Attention Mechanism](../papers/foundations/attentivefp-2019.md) | Journal of Medicinal Chemistry | Published | Learns which atoms and neighborhoods to emphasize when aggregating molecular information for property prediction and structural attribution. |
| 2017-10-31 | [MoleculeNet: a benchmark for molecular machine learning](../papers/foundations/moleculenet-2018.md) | Chemical Science | Published | Brings molecular datasets, splits, metrics and algorithms into a shared benchmark for property prediction. |
