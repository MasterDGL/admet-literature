# 吸收与分布

[English](../en/topics/absorption-distribution.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)

围绕肠道通透性、血脑屏障和 P-gp 转运，理解分子能否被吸收、到达作用部位以及受到哪些转运机制影响。

## 建议阅读顺序

1. [TDC](../papers/admet/tdc-2021.md)：先区分 Caco-2、BBB、P-gp 和血浆蛋白结合等端点及其评价指标。
2. [CaliciBoost](../papers/admet/caliciboost-2025.md)：看 Caco-2 专门模型如何处理数据整理、特征与模型选择。
3. [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md)：追踪 BBB 预测从分子语言模型到体外验证的过程。
4. [MC-PGP](../papers/admet/mc-pgp-2025.md)：比较 P-gp 抑制剂与底物两项任务，以及随机、骨架和外部测试结果。

## 阅读时比较什么

- 标签描述通透率、屏障通过性，还是转运体底物或抑制剂？
- 换用新骨架或外部来源分子后，性能变化多大？
- 模型预测是否有体外实验支持，实验模型与最终应用场景如何衔接？

## 相关论文：由新到旧

| 时间 | 论文 | 期刊/会议 | 状态 | 内容概述 |
| --- | --- | --- | --- | --- |
| 2025-12-22 | [CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction](../papers/admet/caliciboost-2025.md) | Journal of Cheminformatics | 已发表 | 比较分子指纹和理化描述符，结合自动机器学习预测分子通过肠道细胞模型（Caco-2）的能力。 |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | 已发表 | 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。 |
| 2025-04-16 | [A multimodal contrastive learning framework for predicting P-glycoprotein substrates and inhibitors](../papers/admet/mc-pgp-2025.md) | Journal of Pharmaceutical Analysis | 已发表 | 融合 SMILES、指纹和分子图，分别判断分子是否抑制 P-gp、是否会被 P-gp 转运。 |
| 2024-07-09 | [Predicting blood–brain barrier permeability of molecules with a large language model and machine learning](../papers/admet/bbb-megamolbart-2024.md) | Scientific Reports | 已发表 | 用分子语言模型和 XGBoost 预测血脑屏障通透性，并用人源三维 BBB 球体检验部分候选。 |
| 2024-06-24 | [ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries](../papers/admet/admet-ai-2024.md) | Bioinformatics | 已发表 | 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。 |
| 2024-04-22 | [admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties](../papers/admet/admetsar-3-2024.md) | Nucleic Acids Research | 已发表 | 把 ADMET 数据查询、性质预测和结构优化建议整合到一个平台，帮助寻找更合适的候选分子。 |
| 2024-04-04 | [ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support](../papers/admet/admetlab-3-2024.md) | Nucleic Acids Research | 已发表 | 提供覆盖多类 ADMET 及理化性质的在线预测平台，并加入不确定性评估、API 和决策支持功能。 |
| 2023-10-24 | [ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection](../papers/admet/mtgl-admet-2023.md) | iScience | 已发表 | 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。 |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | 已发表 | 把药物发现中的多类数据和任务整理成统一接口与基准，让不同预测方法能够按共同规则比较。 |
