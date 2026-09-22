# Out-of-the-box deep learning prediction of pharmaceutical properties by broadly learned knowledge-based molecular representations

[English](../../en/papers/foundations/molmapnet-2021.md) | **简体中文**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.zh-CN.md)

*Nature Machine Intelligence · 2021-03-01* · 已发表 · 基础方法

**内容概述：** 把分子描述符和指纹排成二维特征图，再用卷积网络预测理化、药代和毒性相关性质。

主题：描述符、分子指纹、卷积网络、基线。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nature Machine Intelligence 3, 334–343；2021-03-01 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 人工积累的描述符与指纹包含丰富化学信息，但普通向量输入难以利用特征间关系；逐任务调参也增加建模成本。 |
| 数据集 | 26 个药物研究相关基准及一个新测试集。特征关系来自 8,506,205 个分子；ADMET 相关数据包括 CYP450（16,896 个化合物，5 种酶）、人/鼠/大鼠肝微粒体清除率（共 8,755 个化合物）、BBBP、ESOL、Tox21、SIDER 和 ClinTox。规模见补充表 S9。 |
| 方法 | MolMap 将 1,456 个描述符和 16,204 个指纹特征按相似关系嵌入二维网格。MolMapNet 用 CNN 学习特征图，提供描述符单路 D、指纹单路 F 和双路 B 模型，并比较默认参数与调参版本。 |
| 结论 | 描述符与指纹的特征图能形成有效的性质预测模型。补充表 S5 中，双路模型在一组 ESOL 划分上的 RMSE 由默认 0.575 降至调参后 0.544；另一组划分上为 0.543→0.512，而 AttentiveFP 为 0.486。模型优劣与实验设置有关。 |

DOI：`10.1038/s42256-021-00301-6`

## 实验设置与结果分析

**划分。** 补充表 S9 分别记录：CYP450 按 assay ID 划分，LMC 随机划分，BBBP 骨架划分，ESOL/Tox21/SIDER/ClinTox 随机划分。

| ESOL 实验组（补充表 S5） | MolMapNet-B 默认 | 调参后 | 对照 RMSE |
| --- | --- | --- | --- |
| MoleculeNet/Chemprop 设置 | 0.575 | 0.544 | Chemprop 0.555 |
| AttentiveFP 设置 | 0.543 | 0.512 | AttentiveFP 0.486 |

**后续 TDC 提交。** MolMapNet-D 在 Caco2_Wang 上的 MAE 为 0.287 ± 0.005，来自 TDC 榜单；对应描述符单路实现，与上表双路模型分开记录。

本仓库将其作为知识描述符与深度学习结合的基础方法。预先学习特征布局的数据规模与下游监督数据规模分别记录，避免把它们当作同一训练集。

## 代码与参考资料

[代码与项目](https://github.com/shenwanxiang/bidd-molmap)

作者公开 MolMap/MolMapNet 代码、训练示例；ChemBench v0 提供数据与划分索引。

资料核对：**2026-09-22**。核对 Crossref、出版社摘要、正式补充表 S5/S9、作者代码和 TDC 提交记录；表 S5 已查看 PDF 原页。

- [出版社摘要与发表信息](https://www.nature.com/articles/s42256-021-00301-6)
- [正式补充材料：表 S5、S9](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-021-00301-6/MediaObjects/42256_2021_301_MOESM1_ESM.pdf)
- [作者代码与示例](https://github.com/shenwanxiang/bidd-molmap)
- [原文数据与划分版本](https://github.com/shenwanxiang/ChemBench/tree/v0)
- [TDC Caco-2 提交成绩](https://tdcommons.ai/benchmark/admet_group/01caco2/)
