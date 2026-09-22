# ADMET-AI

[English](../../en/papers/admet/admet-ai-2024.md) | **简体中文**

**ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**一句话概括：** 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。

分类：核心论文。主题：综合ADMET、平台、高通量。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Bioinformatics 40(7), btae416；2024-06-24 在线发表，2024 年 7 月卷期。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 大规模筛选需要兼顾多端点预测效果、吞吐量和本地部署能力。 |
| 数据集 | TDC 的 41 个预测任务：31 分类、10 回归；性能排名比较使用其中的 22 任务 ADMET Benchmark Group。 |
| 方法 | 论文版采用 Chemprop D-MPNN 与 200 个 RDKit 描述符；分别训练分类、回归多任务模型，并使用模型集成。 |
| 结论 | 作者在发表时报告 TDC ADMET 平均排名领先，并显示较高批量处理效率；提供网页与本地工具。 |

DOI：`10.1093/bioinformatics/btae416`

## 实验设置与结果分析

模型训练覆盖 41 个任务，性能排名使用其中 22 个 ADMET 基准任务；Fig. 1B–C 给出性能与运行效率比较。

推理效率取决于硬件和处理批量。当前 v2 已调整 Chemprop 版本及特征配置，复现论文应使用对应版本。

## 代码与参考资料

[代码与项目](https://github.com/swansonk14/admet_ai)

作者代码/项目入口已公开。

资料核对：**2026-09-19**。书目、正文关键部分及相关官方资源。

- [论文全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11226862/)
- [作者代码及版本说明](https://github.com/swansonk14/admet_ai)
