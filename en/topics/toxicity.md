# Toxicity prediction

**English** | [简体中文](../../topics/toxicity.md)

[Home](../../README.md) · [All reading routes](../docs/reading-routes.md) · [Knowledge map](../docs/knowledge-map.md)

Follow hERG cardiac safety, AMES mutagenicity and Tox21 screening to compare assay labels, class imbalance and endpoint-specific models.

## Suggested reading order

1. [AI for drug toxicity: review](../papers/admet/ai-toxicity-review-2023.md): Build an overview of toxicity tasks, data sources and methods.
2. [Tox21 10K compound library](../papers/admet/tox21-library-2020.md): Examine the experimental origin of screening data and its quality control.
3. [CardioTox net](../papers/admet/cardiotox-net-2021.md): Use hERG to examine ensemble models and external testing.
4. [AMES multitask DNN](../papers/admet/ames-multitask-2022.md): Understand strain-specific multitask labels and overall AMES prediction.
5. [AmesNet](../papers/admet/amesnet-2026.md): Examine how assay conditions and distribution shifts enter mutagenicity modeling.

## Questions to compare

- Does the label describe an assay, a mechanistic endpoint or clinical toxicity, and which labels are comparable?
- How do class balance, bacterial strains and assay conditions affect modeling and evaluation?
- Are new sources or scaffolds tested, and is predictive uncertainty reported?

## Papers, newest first

| Date | Paper | Venue | Status | Overview |
| --- | --- | --- | --- | --- |
| 2026-06-29 | [AmesNet: A Task-Conditioned Deep Learning Model with Enhanced Sensitivity and Generalization in Ames Mutagenicity Prediction](../papers/admet/amesnet-2026.md) | Chemical Research in Toxicology | Published | Combines molecular structure, bacterial strain and metabolic-activation conditions to improve Ames mutagenicity detection in unfamiliar chemical space. |
| 2026-05-25 | [Mapping the avoid-ome: a systematic open-science approach to predictive ADMET](../papers/admet/openadmet-avoidome-2026.md) | Nature Communications | Published | Proposes combining open experimental data, protein structures, active learning and blind challenges to improve mechanistic ADMET prediction. |
| 2025-07-24 | [HERGAI: an artificial intelligence tool for structure-based prediction of hERG inhibitors](../papers/admet/hergai-2025.md) | Journal of Cheminformatics | Published | Combines docking and ensemble models to identify compounds likely to block the cardiac hERG ion channel in large candidate collections. |
| 2023-04-26 | [Artificial Intelligence in Drug Toxicity Prediction: Recent Advances, Challenges, and Future Perspectives](../papers/admet/ai-toxicity-review-2023.md) | Journal of Chemical Information and Modeling | Published | Surveys machine-learning and deep-learning approaches by toxicity task and collects public datasets and prediction tools for model development. |
| 2023 | [Domain-aware representation of small molecules for explainable property prediction models](../papers/admet/domain-aware-pbrics-2023.md) | ICLR 2023 MLDD Workshop | Workshop | Builds chemically meaningful molecular fragments so graph models can predict ADMET properties and identify fragments contributing to each prediction. |
| 2022-09-06 | [Multitask Deep Neural Networks for Ames Mutagenicity Prediction](../papers/admet/ames-multitask-2022.md) | Journal of Chemical Information and Modeling | Published | Learns Ames outcomes for five bacterial strains jointly, retaining strain-specific information alongside the overall mutagenicity label. |
| 2021-11-27 | [Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network](../papers/admet/ssl-gcn-2021.md) | Journal of Cheminformatics | Published | Trains a graph neural network on labeled and unlabeled molecules to improve Tox21 toxicity prediction through semi-supervised learning. |
| 2021-08-16 | [CardioTox net: a robust predictor for hERG channel blockade based on deep learning meta-feature ensembles](../papers/admet/cardiotox-net-2021.md) | Journal of Cheminformatics | Published | Combines neural-network predictions from different molecular representations to identify hERG blockers and tests them on three external datasets. |
| 2021-05-27 | [Deep Learning-Based Conformal Prediction of Toxicity](../papers/admet/tox21-conformal-2021.md) | Journal of Chemical Information and Modeling | Published | Adds conformal prediction to toxicity models, returning one or multiple candidate labels at a chosen confidence level and assessing uncertainty and missed toxic compounds. |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | Published | Organizes drug-discovery datasets and tasks into shared interfaces and benchmarks for consistent model comparison. |
| 2020-11-03 | [The Tox21 10K Compound Library: Collaborative Chemistry Advancing Toxicology](../papers/admet/tox21-library-2020.md) | Chemical Research in Toxicology | Published | Explains how the Tox21 library combines agency collections, high-throughput experiments and traceable chemical annotations to produce toxicity data. |
