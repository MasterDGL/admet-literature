# 分子表示与学习方法

[English](../en/topics/representations-learning.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)

从指纹和描述符基线出发，比较图神经网络、预训练、多任务学习与模型集成如何支持 ADMET 预测。

## 建议阅读顺序

1. [MolMapNet](../papers/foundations/molmapnet-2021.md)：认识指纹和描述符的另一种组织方式，建立结构化特征基线。
2. [Chemprop / D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md)：理解有向键消息传递，并关注描述符基线与划分方式。
3. [AttentiveFP](../papers/foundations/attentivefp-2019.md)：看注意力如何参与原子邻域聚合和分子级读出。
4. [KPGT](../papers/admet/kpgt-2023.md)：看化学知识如何进入图预训练，并检查各任务的迁移效果。
5. [MTGL-ADMET](../papers/admet/mtgl-admet-2023.md)：理解辅助任务选择，以及多任务学习中的负迁移。

## 阅读时比较什么

- 性能提升来自表示、预训练数据、辅助任务，还是集成与调参？
- 与指纹/描述符基线比较时，数据划分、搜索预算和训练数据是否一致？
- 预训练目标和下游端点有什么联系，消融实验支持哪些设计？

## 相关论文：由新到旧

| 时间 | 论文 | 期刊/会议 | 状态 | 内容概述 |
| --- | --- | --- | --- | --- |
| 2026-09-09 | [ADMET-EvO: a self-evolving scientific agent for sustained research across heterogeneous tasks](../papers/admet/admet-evo-2026.md) | arXiv | 🟠 **预印本** | 让研究智能体针对不同 ADMET 任务探索特征和模型，并通过固定测试流程评价预测效果与研究效率。 |
| 2026-08-25 | [A multimodal representation learning platform for accurate molecular ADMET prediction](../papers/admet/trimole-hybrid-2026.md) | bioRxiv | 🟠 **预印本** | 融合分子序列、分子图、三维结构和化学先验，并按 ADMET 任务选择预测模型或集成方案。 |
| 2026-06-20 | [DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction](../papers/admet/dcpm-admet-2026.md) | Journal of Cheminformatics | 已发表 | 将两种预训练模型学到的分子表示与化学指纹结合，用于预测 97 项 ADMET 性质。 |
| 2025-01-06 | [Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation](../papers/admet/molmcl-2025.md) | Nature Communications | 已发表 | 从分子整体、骨架和局部环境等层面学习表示，再按任务组合这些信息，用于性质和生物活性预测。 |
| 2024-11-12 | [MolE: a foundation model for molecular graphs using disentangled attention](../papers/admet/mole-2024.md) | Nature Communications | 已发表 | 先在海量分子图上预训练，再利用生物学任务数据进一步训练，最后用于 ADMET 性质预测。 |
| 2023-11-21 | [A knowledge-guided pre-training framework for improving molecular representation learning](../papers/admet/kpgt-2023.md) | Nature Communications | 已发表 | 把分子指纹和理化描述符融入图预训练，让模型学到更适合预测 ADMET 等性质的分子表示。 |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | 已发表 | 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。 |
| 2023-09-29 | [ADMET property prediction through combinations of molecular fingerprints](../papers/admet/maplight-2023.md) | arXiv | 🟠 **预印本** | 组合多种分子指纹和描述符，用 CatBoost 建立 ADMET 预测模型，检验传统特征方法的竞争力。 |
| 2023-04-24 | [Uni-QSAR: an Auto-ML Tool for Molecular Property Prediction](../papers/admet/uni-qsar-2023.md) | arXiv | 🟠 **预印本** | 自动组合分子指纹、描述符和一维至三维预训练表示，通过调参与堆叠集成完成多种 ADMET 性质预测。 |
| 2023 | [Domain-aware representation of small molecules for explainable property prediction models](../papers/admet/domain-aware-pbrics-2023.md) | ICLR 2023 MLDD Workshop | Workshop | 按化学官能团对分子进行片段化，让图模型在预测 ADMET 性质时指出哪些片段影响结果。 |
| 2021-11-27 | [Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network](../papers/admet/ssl-gcn-2021.md) | Journal of Cheminformatics | 已发表 | 让图神经网络同时学习有毒性标签和无标签的分子，利用半监督学习改善 Tox21 毒性预测。 |
| 2021-03-01 | [Out-of-the-box deep learning prediction of pharmaceutical properties by broadly learned knowledge-based molecular representations](../papers/foundations/molmapnet-2021.md) | Nature Machine Intelligence | 已发表 | 把分子描述符和指纹排成二维特征图，再用卷积网络预测理化、药代和毒性相关性质。 |
| 2019-07-30 | [Analyzing Learned Molecular Representations for Property Prediction](../papers/foundations/chemprop-dmpnn-2019.md) | Journal of Chemical Information and Modeling | 已发表 | 通过沿有向化学键传递信息来学习分子表示，并在公开和工业数据上检验性质预测。 |
| 2019 | [Pushing the Boundaries of Molecular Representation for Drug Discovery with the Graph Attention Mechanism](../papers/foundations/attentivefp-2019.md) | Journal of Medicinal Chemistry | 已发表 | 让图神经网络在汇总分子信息时学习关注哪些原子和邻域，用于性质预测与结构归因。 |
| 2017-10-31 | [MoleculeNet: a benchmark for molecular machine learning](../papers/foundations/moleculenet-2018.md) | Chemical Science | 已发表 | 把分散的分子数据集、划分、指标与算法组织成基准，让性质预测方法有共同的比较起点。 |
