# 毒性预测

[English](../en/topics/toxicity.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)

以 hERG 心脏安全性、AMES 致突变性和 Tox21 毒性筛查为主线，比较实验标签、类别不均衡和专门模型。

## 建议阅读顺序

1. [AI 药物毒性预测综述](../papers/admet/ai-toxicity-review-2023.md)：先建立毒性任务、数据来源和方法的整体认识。
2. [Tox21 10K 化合物库](../papers/admet/tox21-library-2020.md)：回到实验数据来源，理解筛查设计与质量控制。
3. [CardioTox net](../papers/admet/cardiotox-net-2021.md)：用 hERG 案例学习如何比较集成模型与外部测试。
4. [AMES 多任务 DNN](../papers/admet/ames-multitask-2022.md)：理解菌株级多任务标签与总体 AMES 判断的关系。
5. [AmesNet](../papers/admet/amesnet-2026.md)：继续看实验条件和分布变化如何进入致突变性建模。

## 阅读时比较什么

- 标签对应具体实验、机制端点还是临床毒性？不同标签之间能否直接比较？
- 类别比例、菌株和实验条件如何影响模型及评价指标？
- 是否测试新来源或新骨架分子，是否报告预测不确定性？

## 相关论文：由新到旧

| 时间 | 论文 | 期刊/会议 | 状态 | 内容概述 |
| --- | --- | --- | --- | --- |
| 2026-06-29 | [AmesNet: A Task-Conditioned Deep Learning Model with Enhanced Sensitivity and Generalization in Ames Mutagenicity Prediction](../papers/admet/amesnet-2026.md) | Chemical Research in Toxicology | 已发表 | 将分子结构、菌株与代谢活化条件一起输入模型，提高陌生化学结构的 Ames 致突变性识别能力。 |
| 2026-05-25 | [Mapping the avoid-ome: a systematic open-science approach to predictive ADMET](../papers/admet/openadmet-avoidome-2026.md) | Nature Communications | 已发表 | 提出结合开放实验数据、蛋白质结构、主动学习和盲测挑战，从机制上改进 ADMET 预测的研究路线。 |
| 2025-07-24 | [HERGAI: an artificial intelligence tool for structure-based prediction of hERG inhibitors](../papers/admet/hergai-2025.md) | Journal of Cheminformatics | 已发表 | 结合分子对接与集成模型，从大量候选分子中识别可能阻断 hERG 心脏离子通道的化合物。 |
| 2023-04-26 | [Artificial Intelligence in Drug Toxicity Prediction: Recent Advances, Challenges, and Future Perspectives](../papers/admet/ai-toxicity-review-2023.md) | Journal of Chemical Information and Modeling | 已发表 | 按毒性任务梳理机器学习和深度学习研究，并汇总可用于建模的公开数据与预测工具。 |
| 2023 | [Domain-aware representation of small molecules for explainable property prediction models](../papers/admet/domain-aware-pbrics-2023.md) | ICLR 2023 MLDD Workshop | Workshop | 按化学官能团对分子进行片段化，让图模型在预测 ADMET 性质时指出哪些片段影响结果。 |
| 2022-09-06 | [Multitask Deep Neural Networks for Ames Mutagenicity Prediction](../papers/admet/ames-multitask-2022.md) | Journal of Chemical Information and Modeling | 已发表 | 保留五种菌株各自的 Ames 结果进行多任务学习，而非只学习一个总体致突变标签。 |
| 2021-11-27 | [Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network](../papers/admet/ssl-gcn-2021.md) | Journal of Cheminformatics | 已发表 | 让图神经网络同时学习有毒性标签和无标签的分子，利用半监督学习改善 Tox21 毒性预测。 |
| 2021-08-16 | [CardioTox net: a robust predictor for hERG channel blockade based on deep learning meta-feature ensembles](../papers/admet/cardiotox-net-2021.md) | Journal of Cheminformatics | 已发表 | 融合不同分子表示的神经网络预测，改善 hERG 阻断剂识别，并在三个外部测试集上检验效果。 |
| 2021-05-27 | [Deep Learning-Based Conformal Prediction of Toxicity](../papers/admet/tox21-conformal-2021.md) | Journal of Chemical Information and Modeling | 已发表 | 给毒性模型加入共形预测，让用户按置信水平得到单一类别或多个候选类别，并评估漏检与不确定性。 |
| 2021 | [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](../papers/admet/tdc-2021.md) | NeurIPS Datasets and Benchmarks | 已发表 | 把药物发现中的多类数据和任务整理成统一接口与基准，让不同预测方法能够按共同规则比较。 |
| 2020-11-03 | [The Tox21 10K Compound Library: Collaborative Chemistry Advancing Toxicology](../papers/admet/tox21-library-2020.md) | Chemical Research in Toxicology | 已发表 | 解释 Tox21 化合物库如何整合多机构样品、开展高通量实验并形成可追溯的毒性数据。 |
