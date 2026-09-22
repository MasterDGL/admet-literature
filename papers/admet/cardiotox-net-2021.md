# CardioTox net

[English](../../en/papers/admet/cardiotox-net-2021.md) | **简体中文**

**CardioTox net: a robust predictor for hERG channel blockade based on deep learning meta-feature ensembles**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**一句话概括：** 融合不同分子表示的神经网络预测，改善 hERG 阻断剂识别，并在三个外部测试集上检验效果。

分类：专题补读。主题：hERG、集成、外部验证。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 13, 60；2021-08-16 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 单一分子表示可能遗漏信息，多模型直接合并又难兼顾灵敏度、特异度和预测精度。 |
| 数据集 | BindingDB、ChEMBL 和文献数据整理为 12,620 个训练分子（6,643 阻断剂、5,977 非阻断剂）；三个外部集分别为 44、41、839 个分子，采用 IC50 10 μM 分类判据。 |
| 方法 | 五个基神经网络处理不同化学特征，再用独立神经网络组合其预测；训练数据按 70/10/10/10 分别用于基模型训练/验证和元模型训练/验证。 |
| 结论 | 三个外部集报告 MCC 0.599/0.452/0.220，准确率 0.810/0.755/0.746；相对所选旧方法改善多项指标，但第三个不平衡外部集 PPV 仅 0.113。 |

DOI：`10.1186/s13321-021-00541-z`

## 实验设置与结果分析

Data preparation 说明训练与三个外部集的构建，并分析它们的化学相似性。

两个外部集较小，第三个集阳性比例低；其 PPV 0.113 反映了不平衡筛选中的误报问题，可与召回率一起分析。

## 代码与参考资料

[代码与项目](https://github.com/Abdulk084/CardioTox)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。书目、正文相关方法与结果及列出的官方资源。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-021-00541-z)
- [作者代码](https://github.com/Abdulk084/CardioTox)
