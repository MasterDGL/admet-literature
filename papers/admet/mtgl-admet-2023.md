# MTGL-ADMET

[English](../../en/papers/admet/mtgl-admet-2023.md) | **简体中文**

**ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。

分类：核心论文。主题：多任务、辅助任务、负迁移。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | iScience 26(11), 108285；2023 年 11 月卷期。另有 RECOMB 2023 会议前序论文。 |
| 日期口径 | 期刊卷期月份；未在此补造具体日 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 把所有 ADMET 任务放进同一个多任务模型可能产生负迁移；不同主任务需要不同的辅助任务。 |
| 数据集 | 从 8 篇文献汇集 24 个端点：18 分类、6 回归，共 43,291 个化合物；含吸收、分布、代谢、排泄、毒性和 2 个理化性质端点。 |
| 方法 | 以状态理论和最大流选择辅助任务，结合共享原子表示、任务特异注意力和以主任务为中心的门控模块。 |
| 结论 | 在论文所比较的多任务模型及消融实验中，自适应选任务和门控模块改善预测表现，支持“按主任务选择辅助任务”的设计。 |

DOI：`10.1016/j.isci.2023.108285`

## 实验设置与结果分析

Table 1 使用随机 8:1:1 划分、10 个随机种子；分类指标为 AUROC，回归指标为 R²。

对照与消融围绕辅助任务选择和门控模块展开。论文的 24 端点数据与 TDC 22 任务在数据构成和划分上有所不同。

## 代码与参考资料

[代码与项目](https://github.com/dubingxue/MTGL-ADMET)

作者代码/项目入口已公开。

资料核对：**2026-09-19**。书目、正文关键部分及相关官方资源。

- [论文全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10654589/)
- [全文备用入口](https://europepmc.org/articles/PMC10654589)
- [作者代码](https://github.com/dubingxue/MTGL-ADMET)
