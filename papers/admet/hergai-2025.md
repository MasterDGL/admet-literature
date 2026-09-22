# HERGAI

[English](../../en/papers/admet/hergai-2025.md) | **简体中文**

**HERGAI: an artificial intelligence tool for structure-based prediction of hERG inhibitors**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 结合分子对接与集成模型，从大量候选分子中识别可能阻断 hERG 心脏离子通道的化合物。

分类：核心论文。主题：hERG、对接、类别不均衡。

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

训练集五折交叉验证调参，报告召回、特异度、平衡准确率和筛选富集；86%/94% 对应两档活性阈值下的阳性召回。

测试集筛选表现参与了对接姿势打分方案的选择。高召回伴随误报，实际筛选需结合特异度和富集率；预测流程包含对接与结构指纹计算。

## 代码与参考资料

[代码与项目](https://github.com/vktrannguyen/HERGAI)

作者代码与数据可访问；仓库于 2026-01-01 归档。

资料核对：**2026-09-22**。书目、正文相关方法与结果及列出的官方资源。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-025-01063-8)
- [作者代码](https://github.com/vktrannguyen/HERGAI)
