# Explainable uncertainty quantifications for deep learning-based molecular property prediction

[English](../../en/papers/foundations/atom-uncertainty-2023.md) | **简体中文**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.zh-CN.md)

*Journal of Cheminformatics · 2023-02-03* · 已发表 · 基础方法

**内容概述：** 把预测不确定性分解到分子中的原子，帮助定位陌生化学结构和潜在噪声，并校准集成模型的置信估计。

主题：不确定性、校准、可解释性、D-MPNN。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 15, 13；2023-02-03 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 分子级误差估计难以指出哪部分结构导致预测不可靠；直接平均多个网络的方差还会使集成模型的不确定性偏大。 |
| 数据集 | QM9 焓（133,885）、Zinc15 计算 logP（250,000）、Lipophilicity 实验 logD7.4（4,187）、Delaney/ESOL 水溶解度（1,128）。按本文清洗版本计数，见表 1。 |
| 方法 | 在 D-MPNN 上预测原子级性质贡献与方差，通过原子间协方差汇总分子分布；深度集成区分数据噪声与模型知识不足，训练后仅更新方差层进行校准。 |
| 结论 | 原子不确定性可以提示模型陌生的结构。校准降低多个任务的误差，例如 ESOL 的偶然不确定性 ECE 从 0.2118 降到 0.0622；改善程度随数据集而变。 |

DOI：`10.1186/s13321-023-00682-3`

## 实验设置与结果分析

**实验设计。** 四个数据集采用随机 8:1:1 划分；比较原子级 AtomUnc 与分子级 MolUnc。性质误差用 MAE/RMSE，校准质量用 ECE/ENCE，均越低越好。

| AtomUnc 任务 | 校准前 → 校准后 ECE | 校准前 → 校准后 ENCE |
| --- | --- | --- |
| ESOL | 0.2118 → 0.0622 | 0.6414 → 0.5578 |
| Lipophilicity | 0.0413 → 0.0396 | 0.3683 → 0.3704 |

数值为表 2 的偶然不确定性结果。表 3 中，Lipophilicity 的 RMSE：AtomUnc 0.5952，MolUnc 0.8418；ESOL：0.6715 与 0.7520。校准仅更新方差层，均值预测保持不变。

该工作补充性质回归的可信度分析。Zinc15 的 logP 标签由计算产生；随机划分结果用于本实验比较。Lipophilicity 的 ENCE 校准后略有上升，校准收益需逐端点评估。

## 代码与参考资料

[代码与项目](https://github.com/chuiyang/atom-based_uncertainty_model)

作者公开训练、预测、原子可视化和校准脚本；当前实现支持回归任务。

资料核对：**2026-09-22**。核对 Crossref、PubMed 36737786、正文方法、表 1–3 与作者代码说明。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-023-00682-3)
- [表 1：数据集](https://link.springer.com/article/10.1186/s13321-023-00682-3/tables/1)
- [表 2：校准实验](https://link.springer.com/article/10.1186/s13321-023-00682-3/tables/2)
- [表 3：预测误差](https://link.springer.com/article/10.1186/s13321-023-00682-3/tables/3)
- [作者代码](https://github.com/chuiyang/atom-based_uncertainty_model)
