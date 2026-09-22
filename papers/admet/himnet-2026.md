# A hierarchical interaction message net for accurate molecular property prediction

[English](../../en/papers/admet/himnet-2026.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Communications Chemistry · 2026-02-14* · 已发表 · 专题补读

**内容概述：** 让原子、子结构和整个分子之间交换信息，用层级图神经网络预测分子性质及部分 ADMET 指标。

主题：层级GNN、代谢稳定性。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Communications Chemistry 9, 150；2026-02-14 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 原子、子结构与分子整体信息之间的交互不充分，单一层级的表示可能遗漏性质相关信息。 |
| 数据集 | 11 个数据集：8 个 MoleculeNet 子集及 Malaria、LMC、MetStab；其中 BBBP、Tox21、SIDER、ClinTox、代谢稳定性等与 ADMET 直接相关，其他任务属于更广泛性质/活性评价。 |
| 方法 | 层级消息传递与注意力，结合有向消息路径、跨层信息交互及多种指纹的一致性信息。 |
| 结论 | 在本文实验中，BBBP AUROC 为 0.954±0.020，ESOL RMSE 为 0.710±0.016；代谢稳定性 AUROC 为 0.896±0.008。层级消息传递及融合模块的消融表明，各组件对不同任务的贡献不同。 |

DOI：`10.1038/s42004-026-01922-x`

## 实验设置与结果分析

**实验设计。** 11 个数据集采用骨架 8:1:1 划分。正文说明生成 3 个独立划分，每个划分进行 10 次不同初始化训练；消融表另说明跨 3 次运行汇总。Adam 训练 100 个 epoch，batch size 64，学习率 0.0001，隐藏维度 512（Table 5）。分类用 AUROC，回归用 RMSE。

| 任务 | HimNet | 对照 | 原文位置 |
| --- | --- | --- | --- |
| BBBP，AUROC ↑ | 0.954±0.020 | FH-GNN 0.949±0.016 | Table 1 |
| ESOL，RMSE ↓ | 0.710±0.016 | FH-GNN 0.904±0.070 | Table 1 |
| MetStab，AUROC ↑ | 0.896±0.008 | FH-GNN 0.876±0.014 | Table 2 |
| LMC 多物种清除率，平均 RMSE ↓ | 111.0±9.8 | HiMol 117.085±10.1 | Table 2 |

Table 1 的 FH-GNN 由作者重新运行，其他基线取自原论文。表中的高低分同时受原始基线实验设置影响。

论文不同段落对重复实验的汇总写法不同，复现时需对照具体表和发布代码。LMC 为人、大鼠、小鼠的多任务清除率数据，其 RMSE 使用该数据集的量纲。

## 代码与参考资料

[代码与项目](https://github.com/Hugh415/HimNet)

作者代码及数据公开；MIT 许可，另提供 Zenodo 归档。

资料核对：**2026-09-22**。已核对正文实验设计、Tables 1–2、5–6 和代码/数据可用性声明。

- [出版社全文](https://www.nature.com/articles/s42004-026-01922-x)
- [作者代码与数据](https://github.com/Hugh415/HimNet)
- [代码归档](https://doi.org/10.5281/zenodo.18030100)
- [模型比较 Table 1](https://www.nature.com/articles/s42004-026-01922-x/tables/1)
