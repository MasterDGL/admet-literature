# CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction

[English](../../en/papers/admet/caliciboost-2025.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Cheminformatics · 2025-12-22* · 已发表 · 核心论文

**内容概述：** 比较分子指纹和理化描述符，结合自动机器学习预测分子通过肠道细胞模型（Caco-2）的能力。

主题：吸收、Caco-2、AutoML。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 17, 184；2025-12-22；此前有 2025 年预印本。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | Caco-2 渗透性数据少、实验条件不一致，不清楚哪些分子特征与建模策略最有效。 |
| 数据集 | TDC Caco2_Wang，906 个分子；另整理 OCHEM 数据，由 9,402 条原始记录经筛选清洗形成 5,481 条建模数据。两套数据分别建模评价。 |
| 方法 | 比较 8 类分子表示，用 AutoGluon 筛选模型，再进行特征筛选和超参数优化；最终提交的 CaliciBoost 是使用精选 PaDEL 描述符的 XGBoost 回归器。 |
| 结论 | TDC 五次运行的 MAE 为 0.2560±0.006。论文单次特征比较中，PaDEL 筛选与优化后的 MAE 为 0.2525，优于全部 PaDEL 特征的 0.3058。 |

DOI：`10.1186/s13321-025-01137-7`

## 实验设置与结果分析

**实验设计。** TDC Caco2_Wang 共 906 个分子，采用官方骨架划分，保留 20% 测试集；最终榜单结果按 5 个种子报告。OCHEM 的 5,481 条数据另按结构聚类和渗透性分箱划分、独立建模。比较 Morgan、Avalon、ErG、MACCS、RDKit、PaDEL、Mordred 和 CDDD；主要指标为 MAE。

| 实验 | MAE ↓ | 说明 |
| --- | --- | --- |
| 全部 PaDEL 特征 | 0.3058 | 论文特征比较，Supplementary Table 1 |
| 筛选 PaDEL 特征并优化模型 | 0.2525 | 单次实验；RMSE 0.3216、R² 0.7805，Fig. 6 |
| CaliciBoost 官方基准 | 0.2560±0.006 | 5 个种子的均值±标准差，Figs. 10–11 |

**结果解读。** 0.2525 与 0.2560±0.006 对应不同统计口径。TDC 与 OCHEM 分别训练和测试，OCHEM 实验并非将 TDC 训练好的模型直接迁移到外部集。

特征筛选与模型优化共同产生了改进，不能将全部增益归于某一种描述符。OCHEM 部分记录缺少测定方向，实验条件的一致性仍影响标签质量。

## 代码与参考资料

[代码与项目](https://github.com/Calici/CaliciBoost)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。已核对数据处理、划分、模型选择及 Figs. 6、10–11 对应结果。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-025-01137-7)
- [作者代码](https://github.com/Calici/CaliciBoost)
- [TDC Caco-2 榜单](https://tdcommons.ai/benchmark/admet_group/01caco2/)
