# admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties

[English](../../en/papers/admet/admetsar-3-2024.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Nucleic Acids Research · 2024-04-22* · 已发表 · 专题补读

**内容概述：** 把 ADMET 数据查询、性质预测和结构优化建议整合到一个平台，帮助寻找更合适的候选分子。

主题：综合ADMET、平台、结构优化。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nucleic Acids Research 52(W1), W432–W438；2024-04-22 在线发表，2024 年 7 月卷期。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 用户不仅需要性质预测，还需要查询相似化合物及寻找改善 ADMET 的结构修改方向。 |
| 数据集 | 超过 37 万条实验记录，涉及 104,652 个不同化合物、119 个 ADMET 端点。 |
| 方法 | CLMGraph 先依据 1,000 万个小分子的 QED 构造分子对进行对比预训练，再进行 ADMET 多任务微调；另整合相似性检索、骨架跃迁和匹配分子对变换规则。 |
| 结论 | 90 个分类端点的平均 AUC 为 0.870，超过 82% 的回归端点 Pearson r>0.70；半衰期和平均滞留时间表现较弱。平台同时提供实验数据查询和结构优化功能。 |

DOI：`10.1093/nar/gkae298`

## 实验设置与结果分析

**实验设计。** 使用五折交叉验证和外部验证；CLMGraph 分类采用 BCE 损失，回归采用 MSE 损失。监督微调前，使用 1,000 万个分子的 QED 信息构造对比学习任务。

**结果。** 正文 Results presentation 报告 90 个分类端点平均 AUC 0.870；超过 82% 的回归端点 Pearson r>0.70。肾清除率分类、半衰期和平均滞留时间回归表现较弱。正文没有逐端点给出外部集规模及分数，因此这些平均值仅按文中总体结果记录，不标成外部验证均值。

**优化案例。** ADMETopt2 从匹配分子对提取 21 个 ADMET 端点的变换规则；案例将建议与既有文献的结构修改和实验结果对应（Supplementary Text S1、Table S1）。Table 1 的平台比较主要比较覆盖、功能和速度。

五折验证和外部验证的逐端点信息需与各模型报告对应。结构优化案例属于已有化合物的回顾性案例，不能代表全部生成建议已经过实验验证。

## 代码与参考资料

在线平台免费开放，ADMETopt2 变换规则在 figshare 提供下载；正文未链接完整预测模型的训练代码及权重仓库。

资料核对：**2026-09-22**。已核对全文 Model building、Results presentation、优化案例及数据可用性声明。

- [出版社论文](https://doi.org/10.1093/nar/gkae298)
- [平台](http://lmmd.ecust.edu.cn/admetsar3/)
- [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223829/)
- [ADMETopt2 变换规则](https://figshare.com/articles/dataset/ADMETopt2Transformation_Rules/25472317)
