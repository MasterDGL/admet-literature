# Pushing the Boundaries of Molecular Representation for Drug Discovery with the Graph Attention Mechanism

[English](../../en/papers/foundations/attentivefp-2019.md) | **简体中文**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.zh-CN.md)

*Journal of Medicinal Chemistry · 2019* · 已发表 · 基础方法

**内容概述：** 让图神经网络在汇总分子信息时学习关注哪些原子和邻域，用于性质预测与结构归因。

主题：分子图、注意力、分子表示。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Medicinal Chemistry 63(16), 8749–8760；2019 年在线，2020-08-27 卷期 |
| 日期口径 | 在线年份；精确在线日存在来源字段冲突，卷期日期另列 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 分子表示需要捕捉局部及较远结构联系，同时让模型关注的化学特征更容易检查。 |
| 数据集 | 正式 Supplementary Table 1/6 包括 BBBP 2,053、Tox21 8,014（12 任务）、ToxCast 8,615（617 任务）、SIDER 1,427（27 任务）、ClinTox 1,491（2 任务）、ESOL 1,128、FreeSolv 643、Lipophilicity 4,200 个分子，另有活性及 QM9 任务。 |
| 方法 | 在分子图消息聚合和图级读出中使用注意力，构建可学习的分子指纹，并通过注意力可视化分析结构信息。 |
| 结论 | 正式补充表报告 BBBP AUROC 0.920±0.015、Tox21 AUROC 0.858±0.014、ESOL RMSE 0.503±0.076。原子及分子读出注意力提供了可视化的结构归因方式。 |

DOI：`10.1021/acs.jmedchem.9b00959`

## 实验设置与结果分析

**实验设置。** 作者 BBBP、Tox21 和 ESOL 示例 notebook 先随机抽取 10% 测试数据，再从剩余数据抽取 1/9 作为验证集，形成约 8:1:1 的随机划分。正式 Supplementary Table 6 分别列训练、验证和测试成绩；以下摘录 Test 列。

| 数据集 | 分子数 | 指标 | Test |
| --- | --- | --- | --- |
| BBBP | 2,053 | AUROC ↑ | 0.920±0.015 |
| Tox21 | 8,014 | AUROC ↑ | 0.858±0.014 |
| SIDER | 1,427 | AUROC ↑ | 0.637±0.017 |
| ClinTox | 1,491 | AUROC ↑ | 0.940±0.018 |
| ESOL | 1,128 | RMSE ↓ | 0.503±0.076 |
| FreeSolv | 643 | RMSE ↓ | 0.736±0.037 |

这些是作者原始实验数据版本上的成绩。TDC 后续重新整理的数据和骨架划分实验另见方法对比页；两者不合并排名。

注意力可视化描述模型关注的结构，并不直接证明化学因果机制。ACS 页首/Crossref 和出版历史的在线日字段分别为 2019-08-13 与 2019-08-27，因此索引保留已确认的在线年份。

## 代码与参考资料

[代码与项目](https://github.com/OpenDrugAI/AttentiveFP)

作者代码与配套数据可访问；原 Code Ocean 环境需按复现说明重建。

资料核对：**2026-09-22**。已核对正式补充 Tables 1、6、作者 BBBP/Tox21/ESOL 划分代码及日期字段差异。

- [正式论文](https://doi.org/10.1021/acs.jmedchem.9b00959)
- [书目元数据](https://api.crossref.org/works/10.1021/acs.jmedchem.9b00959)
- [作者实现](https://github.com/OpenDrugAI/AttentiveFP)
- [作者配套数据目录](https://github.com/OpenDrugAI/AttentiveFP/tree/master/data)
- [正式补充材料 Tables 1、6](https://acs.figshare.com/articles/journal_contribution/9733613)
- [作者 BBBP 实验代码](https://github.com/OpenDrugAI/AttentiveFP/blob/master/code/2_Physiology_or_Toxicity_BBBP.ipynb)
