# 代谢与药代动力学

[English](../en/topics/metabolism-pk.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)

从 CYP 与微粒体代谢稳定性出发，连接人体清除率、半衰期和分布容积，理解体外端点如何服务于体内 PK 预测。

## 建议阅读顺序

1. [TDC](../papers/admet/tdc-2021.md)：先认识 CYP、微粒体/肝细胞清除率与半衰期的数据定义。
2. [MetaboGNN](../papers/admet/metabognn-2025.md)：从微粒体剩余比例入手，理解人–小鼠差异如何作为辅助任务。
3. [CYP2C9 prediction and validation](../papers/admet/cyp2c9-ml-validation-2022.md)：看 CYP 抑制预测如何结合蛋白结构信息，并进入新实验验证。
4. [PKSmart](../papers/admet/pksmart-2025.md)：进一步看跨物种建模如何预测人体 PK，并检查外部验证。
5. [MMPK](../papers/admet/mmpk-2025.md)：进入口服给药场景，区分剂量组合、表观参数与外部验证结果。
6. [Human clearance with reduced bias](../papers/admet/human-clearance-bias-2024.md)：最后检验结构近邻排除后的人体清除率误差，理解更严格的泛化评测。

## 阅读时比较什么

- 研究预测的是 CYP 抑制/底物、体外稳定性，还是体内 PK 参数？物种和单位是什么？
- 跨物种信息来自实测值还是模型预测值，测试阶段能否获得这些输入？
- 随机划分、骨架划分和外部验证分别检验了什么泛化能力？

## 相关论文：由新到旧

| 时间 | 论文 | 期刊/会议 | 状态 | 内容概述 |
| --- | --- | --- | --- | --- |
| 2026-02-14 | [A hierarchical interaction message net for accurate molecular property prediction](../papers/admet/himnet-2026.md) | Communications Chemistry | 已发表 | 让原子、子结构和整个分子之间交换信息，用层级图神经网络预测分子性质及部分 ADMET 指标。 |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | 已发表 | 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。 |
| 2025-09-03 | [MetaboGNN: predicting liver metabolic stability with graph neural networks and cross-species data](../papers/admet/metabognn-2025.md) | Journal of Cheminformatics | 已发表 | 结合图对比预训练与人–小鼠代谢差异，预测化合物在肝微粒体中孵育 30 分钟后的剩余比例。 |
| 2025-07-31 | [MMPK: A Multimodal Deep Learning Framework to Predict Human Oral Pharmacokinetic Parameters](../papers/admet/mmpk-2025.md) | Journal of Medicinal Chemistry | 已发表 | 融合分子图、子结构图、SMILES 与剂量信息，预测人体口服给药后的八项药代参数。 |
| 2024-09-10 | [PharmaBench: Enhancing ADMET benchmarks with large language models](../papers/admet/pharmabench-2024.md) | Scientific Data | 已发表 | 用大语言模型辅助提取实验条件，再清洗和统一 ADMET 记录，构建条件更明确的评测数据集。 |
| 2024-06-24 | [ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries](../papers/admet/admet-ai-2024.md) | Bioinformatics | 已发表 | 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。 |
| 2024-04-22 | [admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties](../papers/admet/admetsar-3-2024.md) | Nucleic Acids Research | 已发表 | 把 ADMET 数据查询、性质预测和结构优化建议整合到一个平台，帮助寻找更合适的候选分子。 |
| 2024-04-04 | [ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support](../papers/admet/admetlab-3-2024.md) | Nucleic Acids Research | 已发表 | 提供覆盖多类 ADMET 及理化性质的在线预测平台，并加入不确定性评估、API 和决策支持功能。 |
| 2024-01-29 | [Prediction of Human Clearance Using In Silico Models with Reduced Bias](../papers/admet/human-clearance-bias-2024.md) | Molecular Pharmaceutics | 已发表 | 排除测试分子的同类和高相似训练化合物，检验人体清除率模型对新化学结构的预测能力。 |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | 已发表 | 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。 |
| 2022-01-26 | [Machine learning-driven identification of drugs inhibiting cytochrome P450 2C9](../papers/admet/cyp2c9-ml-validation-2022.md) | PLOS Computational Biology | 已发表 | 结合分子描述符和 CYP2C9 多构象对接筛选抑制剂，并通过新实验检验候选药物。 |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | 已发表 | 把药物发现中的多类数据和任务整理成统一接口与基准，让不同预测方法能够按共同规则比较。 |
