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
| 方法 | 用共享表示的多任务 DNN 学习五种菌株结果，与总体标签单任务模型、各菌株单任务及其集成比较；保留部分标签未确定的化合物信息。 |
| 结论 | 正式摘要报告多任务模型优于总体标签单任务模型和菌株单任务集成，说明保留菌株级信息有助于致突变性预测。 |

DOI：`10.1021/acs.jcim.2c00532`

## 实验设置与结果分析

作者 data.py 提供 Train/Internal/External 分区和五折交叉验证；多任务模型按 Overall 标签分层。逐项结果分数仍待核对正式版表格。

五种菌株标签为模型提供不同突变敏感性的信息。代码 README 保留了投稿阶段说明；文献引用使用正式 JCIM 版本。

## 代码与参考资料

[代码与项目](https://github.com/VirSabando/MTL_DNN_Ames)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。正式版书目/摘要、作者 Mendeley v2 数据说明、代码 README 与 data.py；未完成正式版全部结果表核对。

- [正式版摘要](https://pubmed.ncbi.nlm.nih.gov/36066065/)
- [作者数据 v2](https://data.mendeley.com/datasets/ktc6gbfsbh/2)
- [作者代码](https://github.com/VirSabando/MTL_DNN_Ames)
