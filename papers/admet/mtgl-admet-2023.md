# ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection

[English](../../en/papers/admet/mtgl-admet-2023.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*iScience · 2023-11* · 已发表 · 核心论文

**内容概述：** 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。

主题：多任务、辅助任务、负迁移。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | iScience 26(11), 108285；2023 年 11 月卷期。另有 RECOMB 2023 会议前序论文。 |
| 日期口径 | 期刊卷期月份；未在此补造具体日 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 把所有 ADMET 任务放进同一个多任务模型可能产生负迁移；不同主任务需要不同的辅助任务。 |
| 数据集 | 从 8 篇文献汇集 24 个端点：18 分类、6 回归，共 43,291 个化合物；含吸收、分布、代谢、排泄、毒性和 2 个理化性质端点。 |
| 方法 | 以状态理论和最大流选择辅助任务，结合共享原子表示、任务特异注意力和以主任务为中心的门控模块。 |
| 结论 | 在本文 24 个端点的统一实验中，20 个取得最高均值，其余 4 个排名第二；P-gp 底物 AUROC 0.801±0.031，优于 MGA 的 0.719±0.035，支持按主任务挑选辅助任务。 |

DOI：`10.1016/j.isci.2023.108285`

## 实验设置与结果分析

**实验设计。** 汇集 43,291 个化合物、24 个端点（18 分类、6 回归），随机 8:1:1 划分，10 个随机种子；验证集用于辅助任务选择。对照为 ST-GCN、ST-MGA、MT-GCN、MT-GCNAtt 和 MGA。

| 端点 | 指标 | MTGL-ADMET | MGA |
| --- | --- | --- | --- |
| P-gp 底物 | AUROC ↑ | 0.801±0.031 | 0.719±0.035 |
| BBB | AUROC ↑ | 0.973±0.005 | 0.956±0.010 |
| Caco-2 | R² ↑ | 0.523±0.025 | 0.385±0.031 |
| ESOL | R² ↑ | 0.931±0.038 | 0.866±0.020 |

来源：Table 1，均值±标准差。CYP2C9、CYP2D6 抑制剂和肝毒性任务上，MGA 的均值更高；呼吸毒性任务上 ST-MGA 更高。

该论文的半衰期和清除率是分类任务，Caco-2 使用 R²。任务定义和随机划分与 TDC 对应基准不同，比较时需保留这些设置。

## 代码与参考资料

[代码与项目](https://github.com/dubingxue/MTGL-ADMET)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。已核对 STAR Methods、24 端点数据说明及 Table 1。

- [论文全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10654589/)
- [全文备用入口](https://europepmc.org/articles/PMC10654589)
- [作者代码](https://github.com/dubingxue/MTGL-ADMET)
