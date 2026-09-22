# HERGAI: an artificial intelligence tool for structure-based prediction of hERG inhibitors

[English](../../en/papers/admet/hergai-2025.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Cheminformatics · 2025-07-24* · 已发表 · 核心论文

**内容概述：** 结合分子对接与集成模型，从大量候选分子中识别可能阻断 hERG 心脏离子通道的化合物。

主题：hERG、对接、类别不均衡。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 17, 110；2025-07-24 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 小规模或阳性富集的测试集不能充分反映筛选中大量阴性、少量 hERG 阻断剂的场景。 |
| 数据集 | PubChem/ChEMBL 清洗后 299,927 个分子：1,937 阳性、297,990 阴性；采用 IC50 20 μM 判据，按 Bemis–Murcko 骨架成组分配约 3:1 训练/测试集。 |
| 方法 | Smina 对接后选择结合姿势，提取蛋白–配体 PLEC 指纹；RF、XGBoost、DNN 作为基模型，DNN 作为堆叠集成元学习器；在训练折内过采样。 |
| 结论 | 作者报告测试集对 IC50≤20 μM 阻断剂的召回约 86%，对≤1 μM 阻断剂约 94%；筛选富集优于论文比较的通用对接打分方案。 |

DOI：`10.1186/s13321-025-01063-8`

## 实验设置与结果分析

**实验设计。** 以 IC50≤20 μM 定义阻断剂，按 Bemis–Murcko 骨架成组分配约 3:1 的训练/测试集。Table 1 给出训练 224,945 个分子（1,453 阳性），测试 74,982 个（484 阳性）。训练集内五折验证同时选择模型超参数和决策阈值；过采样仅用于训练折，随机种子为 42。

**核心结果。** 最终 DNN 堆叠模型 HERGAI 在测试集的阳性召回率为 0.864；对 IC50≤1 μM 阻断剂的召回率为 94.29%。对照包括单个 RF/XGBoost/DNN 模型、对接打分函数，以及在同一测试集运行的 CardioTox net 和 AttenhERG。论文同时报告特异度、平衡准确率、ROC-AUC 和前 0.1%/1% 富集因子（Results and Discussion、Table 2、Conclusions）。

该测试集是同一整理数据源中的留出骨架集合。测试集筛选表现还参与了对接姿势打分方案选择，因此后续复现宜另设独立外部集检验完整流程。高召回应与特异度、富集率一起解读。

## 代码与参考资料

[代码与项目](https://github.com/vktrannguyen/HERGAI)

作者代码与数据可访问；仓库于 2026-01-01 归档。

资料核对：**2026-09-22**。已核对 Table 1 样本数、训练折过采样、阈值选择和测试集结果。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-025-01063-8)
- [作者代码](https://github.com/vktrannguyen/HERGAI)
