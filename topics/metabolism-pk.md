# 代谢与药代动力学

[English](../en/topics/metabolism-pk.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)

从 CYP 与微粒体代谢稳定性出发，连接人体清除率、半衰期和分布容积，理解体外端点如何服务于体内 PK 预测。

## 建议阅读顺序

1. [TDC](../papers/admet/tdc-2021.md)：先认识 CYP、微粒体/肝细胞清除率与半衰期的数据定义。
2. [PharmaBench](../papers/admet/pharmabench-2024.md)：理解实验条件和数据清洗为何会影响标签与模型比较。
3. [HimNet](../papers/admet/himnet-2026.md)：阅读代谢稳定性专门模型，检查层级分子表示带来的贡献。
4. [PKSmart](../papers/admet/pksmart-2025.md)：进一步看跨物种建模如何预测人体 PK，并检查外部验证。

## 阅读时比较什么

- 研究预测的是 CYP 抑制/底物、体外稳定性，还是体内 PK 参数？物种和单位是什么？
- 跨物种信息来自实测值还是模型预测值，测试阶段能否获得这些输入？
- 随机划分、骨架划分和外部验证分别检验了什么泛化能力？

## 相关论文：由新到旧

| 时间 | 论文 | 期刊/会议 | 状态 | 内容概述 |
| --- | --- | --- | --- | --- |
| 2026-02-14 | [A hierarchical interaction message net for accurate molecular property prediction](../papers/admet/himnet-2026.md) | Communications Chemistry | 已发表 | 让原子、子结构和整个分子之间交换信息，用层级图神经网络预测分子性质及部分 ADMET 指标。 |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | 已发表 | 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。 |
| 2024-09-10 | [PharmaBench: Enhancing ADMET benchmarks with large language models](../papers/admet/pharmabench-2024.md) | Scientific Data | 已发表 | 用大语言模型辅助提取实验条件，再清洗和统一 ADMET 记录，构建条件更明确的评测数据集。 |
| 2024-06-24 | [ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries](../papers/admet/admet-ai-2024.md) | Bioinformatics | 已发表 | 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。 |
| 2024-04-22 | [admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties](../papers/admet/admetsar-3-2024.md) | Nucleic Acids Research | 已发表 | 把 ADMET 数据查询、性质预测和结构优化建议整合到一个平台，帮助寻找更合适的候选分子。 |
| 2024-04-04 | [ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support](../papers/admet/admetlab-3-2024.md) | Nucleic Acids Research | 已发表 | 提供覆盖多类 ADMET 及理化性质的在线预测平台，并加入不确定性评估、API 和决策支持功能。 |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | 已发表 | 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。 |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | 已发表 | 把药物发现中的多类数据和任务整理成统一接口与基准，让不同预测方法能够按共同规则比较。 |
