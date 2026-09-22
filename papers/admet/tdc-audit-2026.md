# TDC模型审计

[English](../../en/papers/admet/tdc-audit-2026.md) | **简体中文**

**Critical Assessment of ML models for ADMET Prediction in TDC leaderboards**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**一句话概括：** 检查 TDC 榜单领先模型能否运行、有无数据泄漏，以及报告的 ADMET 成绩能否复现。

分类：预印本。主题：可复现性、数据泄漏、审计。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | bioRxiv 预印本，2026 年；Crossref 发布日期为 2026-02-28，DOI 中含 02-26。此处不把 DOI 中日期直接当作发布日期。 |
| 日期口径 | Crossref 预印本发布日期；与 DOI 中日期区分 |
| 发表状态 | 预印本 |
| 主要痛点 | 排行榜领先成绩是否能复现，是否受到预训练泄漏、验证/测试重叠或环境问题影响？ |
| 数据集 | 从 TDC 22 任务的领先方法中选出 10 个方法进行审查；具体结论受其榜单快照与代码版本限制。 |
| 方法 | 分阶段检查环境可用性、预训练泄漏、验证/测试重叠和结果复现。 |
| 结论 | 作者报告仅 MapLight、MapLight+GNN 和 CaliciBoost 通过全部检查；其中 CaliciBoost 仅针对 Caco-2，并非覆盖全部 22 任务。 |

DOI：`10.64898/2026.02.26.708193`

## 实验设置与结果分析

对 10 个领先方法检查运行环境、数据泄漏、验证/测试重叠与结果复现；记录对应的榜单快照及代码版本。

审计将运行环境问题与实验设计问题分开讨论，适合据此制定复现检查流程。当前条目对应预印本中的审计结果。

## 代码与参考资料

[代码与项目](https://github.com/receptor-ai/tdc-admet-bench)

作者代码/项目入口已公开。

资料核对：**2026-09-19**。书目、摘要及可访问项目说明。

- [预印本](https://www.biorxiv.org/content/10.64898/2026.02.26.708193v1)
- [审计代码与说明](https://github.com/receptor-ai/tdc-admet-bench)
