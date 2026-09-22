# ADMET property prediction through combinations of molecular fingerprints

[English](../../en/papers/admet/maplight-2023.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*arXiv · 2023-09-29* · 🟠 **预印本** · 预印本

**内容概述：** 组合多种分子指纹和描述符，用 CatBoost 建立 ADMET 预测模型，检验传统特征方法的竞争力。

主题：指纹、CatBoost、基线。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | arXiv 预印本，2023-09-29 首次提交；本文整理该版本。 |
| 日期口径 | arXiv 首次提交日期；修订日期见发表信息 |
| 发表状态 | 🟠 **预印本** |
| 主要痛点 | 简单、计算成本较低的特征模型是否仍能与深度模型竞争？ |
| 数据集 | TDC ADMET 22 任务。 |
| 方法 | 组合 ECFP、Avalon、ErG 和分子描述符，使用 CatBoost；另有增加 GNN 表示的变体。 |
| 结论 | 组合指纹模型在多个 ADMET 端点取得较好结果，为端点建模提供基线；后续第三方审计报告将 MapLight 两个版本列为通过其审计流程的方法。 |

## 实验设置与结果分析

使用 TDC ADMET 22 任务评价不同模型变体；另有第三方预印本对两个版本开展复现审计。

组合指纹模型为端点建模提供了实用基线；第三方审计结果可结合其代码版本与检查项目阅读。

## 代码与参考资料

[代码与项目](https://github.com/maplightrx/MapLight-TDC)

作者代码/项目入口已公开。

资料核对：**2026-09-19**。书目、正文关键部分及相关官方资源。

- [预印本](https://arxiv.org/abs/2310.00174)
- [作者代码](https://github.com/maplightrx/MapLight-TDC)
