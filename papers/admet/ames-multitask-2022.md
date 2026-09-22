# Multitask Deep Neural Networks for Ames Mutagenicity Prediction

[English](../../en/papers/admet/ames-multitask-2022.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Chemical Information and Modeling · 2022-09-06* · 已发表 · 专题补读

**内容概述：** 保留五种菌株各自的 Ames 结果进行多任务学习，而非只学习一个总体致突变标签。

主题：AMES、菌株级标签、多任务学习。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Chemical Information and Modeling 62(24), 6342–6351；2022-09-06 在线 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 将不同菌株的实验结果压成单一标签，会丢失可用于预测致突变性的菌株差异信息。 |
| 数据集 | 作者 Mendeley v2 数据：ISSSTY 整理的 5,536 个分子、1,360 个 Mordred 描述符；TA98、TA100、TA102、TA1535、TA1537 五种菌株标签及 Overall 标签，含未确定标签；提供 Train/Internal/External 分区。 |
| 方法 | 共享核心网络联合学习 TA98、TA100、TA102、TA1535、TA1537 五个输出，再通过共识规则形成总体预测；比较总体标签单任务模型和菌株单任务模型的共识结果，并处理缺失标签。 |
| 结论 | 正式摘要报告多任务模型优于总体标签单任务模型和菌株单任务集成，说明保留菌株级信息有助于致突变性预测。 |

DOI：`10.1021/acs.jcim.2c00532`

## 实验设置与结果分析

**实验设计。** 作者数据包含 Train/Internal/External 分区，训练代码采用五折验证。正式补充文件提供 MTL、Overall 和各菌株模型的交叉验证预测，以及三类模型的外部预测工作簿；例如 external-validation-MTL.xls 包含 5 个 Fold 工作表，每表 1,114 行化合物记录。

**参数与对照。** 正式 Supplementary Table S2 分列普通和加权损失设置：MTL 使用 5 个输出，总体标签单任务模型使用 1 个输出，学习率均为 0.0001；S3 给出各菌株独立模型的配置。S4 明确列出合并到各菌株标签中的 ±S9 及菌株变体。

**结果来源。** 正式摘要报告多任务模型优于总体标签单任务和菌株单任务共识；正式补充材料提供模型配置与预测文件。补充 Table S1 汇总国际 Ames/QSAR 挑战中其他工具的成绩，用于背景比较。

该研究把实验变体汇总为五个菌株标签；这与 AmesNet 显式输入菌株及 S9 条件的设计不同。补充材料还指出三对可能互为盐形式的重复化合物，复现时应检查它们的分区。

## 代码与参考资料

[代码与项目](https://github.com/VirSabando/MTL_DNN_Ames)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。已核对正式摘要、补充 Tables S1–S4、预测文件结构、作者 data.py 与 compute_metrics.py；正文最终结果表仍缺全文核对。

- [正式版摘要](https://pubmed.ncbi.nlm.nih.gov/36066065/)
- [作者数据 v2](https://data.mendeley.com/datasets/ktc6gbfsbh/2)
- [作者代码](https://github.com/VirSabando/MTL_DNN_Ames)
- [正式补充材料 Tables S1–S4](https://acs.figshare.com/articles/journal_contribution/20976947)
- [正式补充预测数据](https://acs.figshare.com/articles/journal_contribution/20976950)
