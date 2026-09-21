# CaliciBoost

**CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction**

[返回 ADMET 总表](../../topics/admet.md) · [返回首页](../../README.md)

分类：核心论文。主题：吸收、Caco-2、AutoML。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 17, 184；2025-12-22；此前有 2025 年预印本。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | Caco-2 渗透性数据少、实验条件不一致，不清楚哪些分子特征与建模策略最有效。 |
| 数据集 | TDC Caco2_Wang，906 个分子；另整理 OCHEM 数据，由 9,402 条原始记录经筛选清洗形成 5,481 条建模数据。两个来源的实验设置应分别阅读。 |
| 方法 | 系统比较分子指纹、RDKit/PaDEL/Mordred 描述符、CDDD 等表示；结合 AutoGluon、特征筛选、解释分析与超参数优化。 |
| 结论 | 精心选择的特征与集成学习在该端点上具有很强竞争力。核验日 TDC Caco-2 官方榜单列 CaliciBoost 的 MAE 为 0.256 ± 0.006、排名第一。 |

DOI：`10.1186/s13321-025-01137-7`

## 评测与结论适用范围

TDC Caco2_Wang 与另外整理的 OCHEM 数据分别评价。0.256 ± 0.006 是 2026-09-19 的 TDC 榜单 MAE 记录。

上述 MAE 来自 2026-09-19 的公开榜单记录；不是本次复现结果，也不是其 OCHEM 实验成绩。论文只直接支持 Caco-2 结论；OCHEM 部分缺失测定方向的处理仍可能带入噪声。

## 代码与证据

[代码或项目入口](https://github.com/Calici/CaliciBoost)

代码状态：存在作者代码/项目入口；未独立验证安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-19**。核对范围：书目、正文关键部分及相关官方资源。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-025-01137-7)
- [作者代码](https://github.com/Calici/CaliciBoost)
- [TDC Caco-2 榜单](https://tdcommons.ai/benchmark/admet_group/01caco2/)
