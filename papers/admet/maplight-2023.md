# MapLight

**ADMET property prediction through combinations of molecular fingerprints**

[返回 ADMET 总表](../../topics/admet.md) · [返回首页](../../README.md)

分类：预印本。主题：指纹、CatBoost、基线。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | arXiv 预印本，2023-09-29 首次提交；本次引用该版本，不填未经核实的正式期刊。 |
| 日期口径 | arXiv 首次提交日期；修订日期见发表信息 |
| 发表状态 | 预印本 |
| 主要痛点 | 简单、计算成本较低的特征模型是否仍能与深度模型竞争？ |
| 数据集 | TDC ADMET 22 任务。 |
| 方法 | 组合 ECFP、Avalon、ErG 和分子描述符，使用 CatBoost；另有增加 GNN 表示的变体。 |
| 结论 | 组合指纹模型在多个 ADMET 端点表现强，是值得保留的基线；后续第三方审计报告也将 MapLight 两个版本列为通过其审计流程的方法。 |

## 评测与结论适用范围

TDC ADMET 22 任务。变体和端点分别记录；第三方审计支持属于另一篇预印本报告。

不应因模型简单而忽略；但第三方审计是另一篇预印本的结论，且榜单优势必须落实到具体端点。

## 代码与证据

[代码或项目入口](https://github.com/maplightrx/MapLight-TDC)

代码状态：存在作者代码/项目入口；未独立验证安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-19**。核对范围：书目、正文关键部分及相关官方资源。

- [预印本](https://arxiv.org/abs/2310.00174)
- [作者代码](https://github.com/maplightrx/MapLight-TDC)
