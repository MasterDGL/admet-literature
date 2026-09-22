# MC-PGP

[English](../../en/papers/admet/mc-pgp-2025.md) | **简体中文**

**A multimodal contrastive learning framework for predicting P-glycoprotein substrates and inhibitors**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 融合 SMILES、指纹和分子图，分别判断分子是否抑制 P-gp、是否会被 P-gp 转运。

分类：核心论文。主题：P-gp、多模态、外部验证。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Pharmaceutical Analysis 15(8), 101313；2025-08 卷期（PubMed article date：2025-04-16） |
| 日期口径 | 采用期刊卷期月份；另列 PubMed article date，二者不混用 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 单一表示难以覆盖 P-gp 相关结构信息；抑制剂与底物需要区分，并检验新来源化合物上的表现。 |
| 数据集 | 公开数据库/文献汇编：抑制剂数据集共 5,943 个分子（4,558 阳性、1,385 阴性），底物集共 4,018（2,455 阳性、1,563 阴性）；独立外部集分别为 140 和 185 个分子。 |
| 方法 | 注意力融合 SMILES 序列、分子指纹与分子图表示；图对比学习对齐局部与全局结构，并分析相关官能团。 |
| 结论 | 抑制剂外部集 AUROC 为 0.906±0.015；作者报告抑制剂/底物外部集 AUROC 相对次优方法提高 9.82%/10.62%。 |

DOI：`10.1016/j.jpha.2025.101313`

## 实验设置与结果分析

内部比较含随机与骨架划分；Tables 4–5 给出外部集成绩。9.82%/10.62% 为 AUROC 相对次优方法的提升比例。

两个任务分别评价抑制作用与转运底物属性，且各含阳性、阴性样本。与 TDC 对照时，对应的 Pgp_Broccatelli 任务是抑制剂分类。

## 代码与参考资料

完整训练实现的公开链接待核实。

资料核对：**2026-09-22**。书目、正文相关方法与结果及列出的官方资源。

- [开放全文与结果表](https://pmc.ncbi.nlm.nih.gov/articles/PMC12409376/)
- [期刊页面](https://jpa.xjtu.edu.cn/en/article/doi/10.1016/j.jpha.2025.101313)
- [TDC P-gp 定义](https://tdcommons.ai/single_pred_tasks/adme/)
