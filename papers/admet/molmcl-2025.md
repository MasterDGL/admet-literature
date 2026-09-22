# MolMCL

**Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.md)

**一句话概括：** 从分子整体、骨架和局部环境等层面学习表示，再按任务组合这些信息，用于性质和生物活性预测。

分类：专题补读。主题：多通道预训练、活性悬崖。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nature Communications 16, 413；2025-01-06。DOI 中的 2024 不是正式发表年份。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 不同任务依赖的分子结构层级不同，固定的图表示和读出方式难以适配所有任务。 |
| 数据集 | ZINC15 用于预训练；7 个 MoleculeNet 数据集及 MoleculeACE 的 30 个生物活性任务用于下游评价。 |
| 方法 | 分子、骨架和上下文相关的多通道学习，结合分子扰动、对比学习及提示引导的读出。 |
| 结论 | 多通道及任务适配改善所测分子任务的表示，活性悬崖实验显示该设计的价值；这些活性实验不是 30 项 ADMET 实验。 |

DOI：`10.1038/s41467-024-55082-4`

## 评测与结论适用范围

7 个 MoleculeNet 子集和 30 个 MoleculeACE 生物活性任务；不能合称 ADMET 基准。

研究表示学习与性质悬崖时补读；它与 Bioinformatics 的 MoleMCL 是不同论文，名字不能混写。

## 代码与证据

[代码或项目入口](https://github.com/yuewan2/MolMCL)

代码状态：存在作者代码/项目入口；未独立验证安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-19**。核对范围：书目、正文关键部分及相关官方资源。

- [出版社全文](https://www.nature.com/articles/s41467-024-55082-4)
- [作者代码](https://github.com/yuewan2/MolMCL)
