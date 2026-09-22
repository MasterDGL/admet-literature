# ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries

[English](../../en/papers/admet/admet-ai-2024.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Bioinformatics · 2024-06-24* · 已发表 · 核心论文

**内容概述：** 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。

主题：综合ADMET、平台、高通量。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Bioinformatics 40(7), btae416；2024-06-24 在线发表，2024 年 7 月卷期。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 大规模筛选需要兼顾多端点预测效果、吞吐量和本地部署能力。 |
| 数据集 | TDC 的 41 个预测任务：31 分类、10 回归；性能排名比较使用其中的 22 任务 ADMET Benchmark Group。 |
| 方法 | 论文版采用 Chemprop D-MPNN 与 200 个 RDKit 描述符；分别训练分类、回归多任务模型，并使用模型集成。 |
| 结论 | 论文中单任务模型在 20/31 个分类任务达到 AUROC>0.85，在 5/10 个回归任务达到 R²>0.6；多任务模型效果接近且推理更快。32 核 CPU 加 GPU 的百万条输入计时为 3.1 小时。 |

DOI：`10.1093/bioinformatics/btae416`

## 实验设置与结果分析

**实验设计。** 使用 TDC v0.4.1 的 41 个任务，其中 22 个属于 ADMET Benchmark Group。每个任务按 5 组训练/验证/测试划分训练并汇总测试成绩；部署时集成 5 个模型。比较单任务训练和按分类/回归分组的多任务训练。

| 实验 | 结果 | 原文位置 |
| --- | --- | --- |
| 单任务分类，31 个任务 | 20 个任务 AUROC>0.85 | Supplementary Fig. S2 |
| 单任务回归，10 个任务 | 5 个任务 R²>0.6 | Supplementary Fig. S2 |
| 本地 32 核 CPU + GPU | 百万条输入 3.1 小时 | Fig. 1C |
| 本地 8 核 CPU、无 GPU | 百万条输入约 5 小时 | Fig. 1C |

**计时数据。** 百万条输入由 1,000 个 DrugBank 分子重复 1,000 次组成，记录 3 次计时的中位数；这是吞吐量测试，不是百万个不同分子的预测准确率验证。全部逐任务成绩见 Supplementary Table S1。

论文评测、网页部署的多任务集成和当前软件版本分别记录。v2 调整了 Chemprop 与特征配置，复现论文应使用对应版本。

## 代码与参考资料

[代码与项目](https://github.com/swansonk14/admet_ai)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。已核对正文训练/部署区别、Fig. 1 计时设计与补充结果索引。

- [论文全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11226862/)
- [作者代码及版本说明](https://github.com/swansonk14/admet_ai)
