# 可靠性与实验验证

[English](../en/topics/reliability-validation.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [全部阅读路线](../docs/reading-routes.md) · [知识地图](../docs/knowledge-map.md)

沿数据划分、活性悬崖、不确定性和实验验证，检查预测在哪些分子上有效，以及失败时能否被识别。

## 建议阅读顺序

1. [MoleculeNet](../papers/foundations/moleculenet-2018.md)：先理解基准、任务和数据划分如何决定评价问题。
2. [MoleculeACE](../papers/foundations/moleculeace-2022.md)：检查平均成绩是否掩盖相似分子间的大幅活性变化。
3. [原子级不确定性](../papers/foundations/atom-uncertainty-2023.md)：理解原子级不确定性与分子预测误差、结构解释的联系。
4. [ADMET可靠性评测](../papers/admet/admet-reliability-2026.md)：对照小样本和泛化评测，检查常用模型在哪些条件下失效。
5. [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md)：最后追踪一次体外实验验证，区分模型分数与实验观察。

## 阅读时比较什么

- 测试是否真正隔离了新分子、新骨架和新数据来源？
- 平均指标之外，是否分析活性悬崖、误差分布和不确定性校准？
- 新实验检验了什么预测，结果支持到哪个层次？

## 相关论文：由新到旧

| 时间 | 论文 | 期刊/会议 | 状态 | 内容概述 |
| --- | --- | --- | --- | --- |
| 2026-05-25 | [Mapping the avoid-ome: a systematic open-science approach to predictive ADMET](../papers/admet/openadmet-avoidome-2026.md) | Nature Communications | 已发表 | 提出结合开放实验数据、蛋白质结构、主动学习和盲测挑战，从机制上改进 ADMET 预测的研究路线。 |
| 2026-05-18 | [Revisiting ADMET prediction reliability under real-world challenges in the foundation model era](../papers/admet/admet-reliability-2026.md) | Journal of Cheminformatics | 已发表 | 在小样本、陌生分子结构和类别不均衡等条件下比较多类模型，检验 ADMET 预测在实际研究中是否可靠。 |
| 2026-02-28 | [Critical Assessment of ML models for ADMET Prediction in TDC leaderboards](../papers/admet/tdc-audit-2026.md) | bioRxiv | 🟠 **预印本** | 检查 TDC 榜单领先模型能否运行、有无数据泄漏，以及报告的 ADMET 成绩能否复现。 |
| 2025-09-26 | [PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules](../papers/admet/pksmart-2025.md) | Journal of Cheminformatics | 已发表 | 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。 |
| 2025-01-06 | [Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation](../papers/admet/molmcl-2025.md) | Nature Communications | 已发表 | 从分子整体、骨架和局部环境等层面学习表示，再按任务组合这些信息，用于性质和生物活性预测。 |
| 2024-09-10 | [PharmaBench: Enhancing ADMET benchmarks with large language models](../papers/admet/pharmabench-2024.md) | Scientific Data | 已发表 | 用大语言模型辅助提取实验条件，再清洗和统一 ADMET 记录，构建条件更明确的评测数据集。 |
| 2024-07-09 | [Predicting blood–brain barrier permeability of molecules with a large language model and machine learning](../papers/admet/bbb-megamolbart-2024.md) | Scientific Reports | 已发表 | 用分子语言模型和 XGBoost 预测血脑屏障通透性，并用人源三维 BBB 球体检验部分候选。 |
| 2023-02-03 | [Explainable uncertainty quantifications for deep learning-based molecular property prediction](../papers/foundations/atom-uncertainty-2023.md) | Journal of Cheminformatics | 已发表 | 把预测不确定性分解到分子中的原子，帮助定位陌生化学结构和潜在噪声，并校准集成模型的置信估计。 |
| 2022-12-01 | [Exposing the Limitations of Molecular Machine Learning with Activity Cliffs](../papers/foundations/moleculeace-2022.md) | Journal of Chemical Information and Modeling | 已发表 | 专门检查结构很相似、活性却差很多的分子，揭示平均预测误差容易掩盖的模型弱点。 |
| 2021-05-27 | [Deep Learning-Based Conformal Prediction of Toxicity](../papers/admet/tox21-conformal-2021.md) | Journal of Chemical Information and Modeling | 已发表 | 给毒性模型加入共形预测，让用户按置信水平得到单一类别或多个候选类别，并评估漏检与不确定性。 |
| 2017-10-31 | [MoleculeNet: a benchmark for molecular machine learning](../papers/foundations/moleculenet-2018.md) | Chemical Science | 已发表 | 把分散的分子数据集、划分、指标与算法组织成基准，让性质预测方法有共同的比较起点。 |
