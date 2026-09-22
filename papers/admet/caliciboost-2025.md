# CaliciBoost

[English](../../en/papers/admet/caliciboost-2025.md) | **简体中文**

**CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**一句话概括：** 比较分子指纹和理化描述符，结合自动机器学习预测分子通过肠道细胞模型（Caco-2）的能力。

分类：核心论文。主题：吸收、Caco-2、AutoML。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 17, 184；2025-12-22；此前有 2025 年预印本。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | Caco-2 渗透性数据少、实验条件不一致，不清楚哪些分子特征与建模策略最有效。 |
| 数据集 | TDC Caco2_Wang，906 个分子；另整理 OCHEM 数据，由 9,402 条原始记录经筛选清洗形成 5,481 条建模数据。两套数据分别建模评价。 |
| 方法 | 系统比较分子指纹、RDKit/PaDEL/Mordred 描述符、CDDD 等表示；结合 AutoGluon、特征筛选、解释分析与超参数优化。 |
| 结论 | 特征筛选与集成学习改善 Caco-2 渗透性预测。2026-09-19 的 TDC Caco-2 官方榜单记录其 MAE 为 0.256 ± 0.006，排名第一。 |

DOI：`10.1186/s13321-025-01137-7`

## 实验设置与结果分析

分别评价 TDC Caco2_Wang 和整理后的 OCHEM 数据。2026-09-19 的 TDC 榜单记录为 MAE 0.256±0.006。

结果体现特征选择与集成学习在 Caco-2 预测中的作用。OCHEM 部分记录缺少测定方向，标签一致性是进一步改进的数据问题。

## 代码与参考资料

[代码与项目](https://github.com/Calici/CaliciBoost)

作者代码/项目入口已公开。

资料核对：**2026-09-19**。书目、正文关键部分及相关官方资源。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-025-01137-7)
- [作者代码](https://github.com/Calici/CaliciBoost)
- [TDC Caco-2 榜单](https://tdcommons.ai/benchmark/admet_group/01caco2/)
