# ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support

[English](../../en/papers/admet/admetlab-3-2024.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Nucleic Acids Research · 2024-04-04* · 已发表 · 专题补读

**内容概述：** 提供覆盖多类 ADMET 及理化性质的在线预测平台，并加入不确定性评估、API 和决策支持功能。

主题：综合ADMET、平台、不确定性。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nucleic Acids Research 52(W1), W422–W431；2024-04-04 在线发表，2024 年 7 月卷期。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 平台覆盖不足、调用不方便，且仅给出点预测难以支持化合物决策。 |
| 数据集 | 整理超过 40 万条建模数据，覆盖 77 个预测端点（59 分类、18 回归）；平台的 119 项输出还包含 34 个直接计算端点和 8 项规则。逐端点规模见 Supplementary Table S1。 |
| 方法 | 多任务有向消息传递模型与描述符建模，结合预测不确定性、API 和决策支持功能。 |
| 结论 | 在相同数据和划分下，DMPNN 系列在 59 个分类任务中的 47 个优于 MGA；平台将 77 个预测模型与计算属性、规则、预测不确定性和 API 集成。 |

DOI：`10.1093/nar/gkae236`

## 实验设置与结果分析

**实验设计。** 各端点随机 8:1:1 划分，重复 5 次；Adam 训练、贝叶斯搜索调参。比较 DMPNN、加入描述符的 DMPNN-Des，以及在相同数据和划分上训练的 MGA。分类指标为 AUC、ACC、MCC，回归为 R²、RMSE、MAE。

**结果与定位。** 正文报告 DMPNN 系列在 47/59 个分类端点上优于 MGA（Fig. 3）；18 个回归端点的表现分别列在 Supplementary Table S5，分类逐项成绩见 S4。原有回归端点中的 LC50FM R² 为 0.68，新加入的半衰期回归 R² 接近 0.7。S6–S7 给出不确定性分组与阈值。

**使用方式。** 提供网页和 API；API 可选择 DMPNN 或 DMPNN-Des，并返回预测值及置信度分组。模型验证采用随机划分，与 TDC 骨架基准分别解读。

119 是平台总输出数，77 是学习得到的预测端点数。平台覆盖与推理速度可以用于工具选型，模型准确率则按具体端点和划分评价。

## 代码与参考资料

提供在线平台与 API 文档；论文未提供完整训练代码和模型权重的公开仓库入口。

资料核对：**2026-09-22**。已核对全文模型构建、Fig. 3、端点计数及 Supplementary Tables S1–S7 的引用位置。

- [出版社论文](https://doi.org/10.1093/nar/gkae236)
- [开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223840/)
- [在线平台与 API](https://admetlab3.scbdd.com/)
