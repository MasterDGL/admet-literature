# Uni-QSAR

**English** | [简体中文](../../../papers/admet/uni-qsar-2023.md)

**Uni-QSAR: an Auto-ML Tool for Molecular Property Prediction**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**In one sentence:** Automatically combines fingerprints, descriptors and pretrained 1D, 2D and 3D molecular representations with tuning and stacked ensembles for ADMET prediction.

Category: Preprints. Topics: AutoML, Multimodal representations, Ensembles.

| Field | Details |
| --- | --- |
| Publication and date | arXiv:2304.12239, v1; 2023-04-24 |
| Date basis | arXiv version 1 submission date |
| Publication status | Preprint |
| Research problem | Different properties favor different molecular features, making manual representation, model and hyperparameter selection costly; skewed regression labels and class imbalance add further modeling challenges. |
| Datasets | The 22 TDC ADMET Benchmark Group tasks: nine regression and 13 classification tasks. A separate CNS penetration case uses 940 training compounds (315 positive and 625 negative) and 117 external test compounds. |
| Method | Combines fingerprints and descriptors with 1D representations such as K-BERT, 2D representations including GROVER, MolCLR and KPGT, and Uni-Mol 3D representations. Target transformations, imbalance-aware learning, Bayesian optimization and two-level stacking are orchestrated with dflow. |
| Findings | Tables 1–2 report Caco-2 MAE of 0.273 and BBBP AUROC of 0.925. Counting the printed TDC ranking rows gives 17 first-place results across 22 tasks. The CNS case reports AUROC of 0.980; ablations support the contributions of 3D representations, stacking and target transformations. |

## Experimental setup and analysis

TDC experiments follow the benchmark report cited in the paper and compare with Chemprop, DeepAutoQSAR and DeepPurpose; some baseline scores come from prior reports or leaderboards. Per-task splits and seeds are not detailed. Table 1 shows first place for 8/9 regression tasks and Table 2 for 9/13 classification tasks, as recorded in the paper.

The abstract claims SOTA on 21/22 tasks, whereas the TDC ranking rows in Tables 1–2 contain 17/22 first-place entries. These notes use the task metrics and rank counts in the tables; the paper does not reconcile the two counts.

## Code and references

[Code and project](https://github.com/deepmodeling/unimol_tools)

The related public component, Uni-Mol Tools, provides Uni-Mol representations and property prediction, rather than the complete multi-representation stacking pipeline described in the paper.

Sources reviewed: **2026-09-22**. Reviewed arXiv v1, Tables 1–2, the CNS case and ablations, and checked the Uni-Mol Tools README for its paper citation and documented features.

- [arXiv version record](https://arxiv.org/abs/2304.12239)
- [Version 1 full text and result tables](https://arxiv.org/html/2304.12239v1)
- [Related component: Uni-Mol Tools](https://github.com/deepmodeling/unimol_tools)
