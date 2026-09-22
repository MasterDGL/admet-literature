# HimNet

[English](../../en/papers/admet/himnet-2026.md) | **简体中文**

**A hierarchical interaction message net for accurate molecular property prediction**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 让原子、子结构和整个分子之间交换信息，用层级图神经网络预测分子性质及部分 ADMET 指标。

分类：专题补读。主题：层级GNN、代谢稳定性。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Communications Chemistry 9, 150；2026-02-14 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 原子、子结构与分子整体信息之间的交互不充分，单一层级的表示可能遗漏性质相关信息。 |
| 数据集 | 11 个数据集：8 个 MoleculeNet 子集及 Malaria、LMC、MetStab；其中 BBBP、Tox21、SIDER、ClinTox、代谢稳定性等与 ADMET 直接相关，其他任务属于更广泛性质/活性评价。 |
| 方法 | 层级消息传递与注意力，结合有向消息路径、跨层信息交互及多种指纹的一致性信息。 |
| 结论 | 原文 Tables 1–2 报告多个任务上的最佳或接近最佳成绩，支持层级融合的价值。 |

DOI：`10.1038/s42004-026-01922-x`

## 实验设置与结果分析

Tables 1–2 汇总 11 个性质/活性数据集的结果；当前笔记记录主要比较，逐任务划分及超参数仍待补齐。

适合结合层级特征融合与代谢稳定性任务阅读，重点分析不同层级表示带来的性能变化。

## 代码与参考资料

代码链接待补充。

资料核对：**2026-09-19**。书目、正文关键部分及相关官方资源。

- [出版社全文](https://www.nature.com/articles/s42004-026-01922-x)
