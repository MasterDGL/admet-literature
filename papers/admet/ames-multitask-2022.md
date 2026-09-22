# AMES 多任务 DNN

**Multitask Deep Neural Networks for Ames Mutagenicity Prediction**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.md)

**一句话概括：** 保留五种菌株各自的 Ames 结果进行多任务学习，而非只学习一个总体致突变标签。

分类：专题补读。主题：AMES、菌株级标签、多任务学习。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Chemical Information and Modeling 62(24), 6342–6351；2022-09-06 在线 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 将不同菌株的实验结果压成单一标签，会丢失可用于预测致突变性的菌株差异信息。 |
| 数据集 | 作者 Mendeley v2 数据：ISSSTY 整理的 5,536 个分子、1,360 个 Mordred 描述符；TA98、TA100、TA102、TA1535、TA1537 五种菌株标签及 Overall 标签，含未确定标签；提供 Train/Internal/External 分区。 |
| 方法 | 用共享表示的多任务 DNN 学习五种菌株结果，与总体标签单任务模型、各菌株单任务及其集成比较；保留部分标签未确定的化合物信息。 |
| 结论 | 正式摘要报告多任务策略优于总体标签单任务和菌株单任务集成；其贡献是利用实验标签结构，本条不补写未核实的最优分数。 |

DOI：`10.1021/acs.jcim.2c00532`

## 评测与结论适用范围

作者 data.py 实现 Train/Internal/External 分区及五折分层交叉验证；以 Overall 标签对多任务折分层。正式版各表具体分数未逐项复核，不宣称 TDC AMES 领先。

菌株级标签和 TDC 总体标签不是同一任务；不同菌株突变敏感性不能简单等同于代谢活化差异。作者代码 README 仍标投稿阶段，正式发表状态以 DOI 为准。

## 代码与证据

[代码或项目入口](https://github.com/VirSabando/MTL_DNN_Ames)

代码状态：作者代码入口可访问；未验证完整安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-22**。核对范围：正式版书目/摘要、作者 Mendeley v2 数据说明、代码 README 与 data.py；未完成正式版全部结果表核对。

- [正式版摘要](https://pubmed.ncbi.nlm.nih.gov/36066065/)
- [作者数据 v2](https://data.mendeley.com/datasets/ktc6gbfsbh/2)
- [作者代码](https://github.com/VirSabando/MTL_DNN_Ames)
