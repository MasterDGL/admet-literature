# ADMET-AI

**ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries**

[返回 ADMET 总表](../../topics/admet.md) · [返回首页](../../README.md)

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

## 评测与结论适用范围

41 个训练任务与其中 22 任务的基准比较须区分。原文比较见 Fig. 1B–C；论文版与当前仓库版本不同。

重点看 Fig. 1B–C、训练及运行时间说明。速度与硬件、测试负载有关。当前仓库的 v2 实现已变更，包括 Chemprop 版本及特征配置；复现论文时必须固定论文对应版本，不能将当前软件直接视为原文模型。

## 代码与证据

[代码或项目入口](https://github.com/swansonk14/admet_ai)

代码状态：存在作者代码/项目入口；未独立验证安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-19**。核对范围：书目、正文关键部分及相关官方资源。

- [论文全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11226862/)
- [作者代码及版本说明](https://github.com/swansonk14/admet_ai)
