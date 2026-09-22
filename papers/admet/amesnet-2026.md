# AmesNet: A Task-Conditioned Deep Learning Model with Enhanced Sensitivity and Generalization in Ames Mutagenicity Prediction

[English](../../en/papers/admet/amesnet-2026.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Chemical Research in Toxicology · 2026-06-29* · 已发表 · 核心论文

**内容概述：** 将分子结构、菌株与代谢活化条件一起输入模型，提高陌生化学结构的 Ames 致突变性识别能力。

主题：AMES、实验条件、分布外预测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Chemical Research in Toxicology；2026-06-29 在线发表 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 模型在训练域外容易漏检致突变化合物，单纯提高灵敏度又可能造成大量误报。 |
| 数据集 | Lui 等汇编的菌株/S9 条件数据，经正式版清洗后训练/验证共 40,129 条记录、测试 4,208 条记录；每条记录对应一个化合物–菌株–S9 组合。另评估缺少菌株/S9 信息的 Foil 数据。 |
| 方法 | 分子编码器与菌株/±S9 条件通道构成双分支；比较单任务、普通/分组多任务，并对 ChemProp/GROVER 等编码器加入条件通道做对照。 |
| 结论 | 正式版主 OOD 评测报告灵敏度 0.72（95% CI 0.68–0.76）、平衡准确率 0.81（0.78–0.83）；Foil 补充评测平衡准确率 0.72。 |

DOI：`10.1021/acs.chemrestox.6c00082`

## 实验设置与结果分析

**实验设计。** 正式版 Lui 数据经去重后有 40,129 条训练/验证记录和 4,208 条测试记录；记录单位为化合物–菌株–S9 组合。沿用来源研究的 OOD 分区并移除跨分区相同非立体 SMILES。对照包含 STL、普通/分组多任务模型及为 ChemProp、GROVER、RF 添加条件通道的版本。

| 测试 | AmesNet | 对照 | 来源 |
| --- | --- | --- | --- |
| Lui OOD 灵敏度 | 0.72（95% CI 0.68–0.76） | DeepAmes 重实现 0.69（0.64–0.73） | 正式版主结果 |
| Lui OOD 平衡准确率 | 0.81（0.78–0.83） | DeepAmes 重实现 0.76（0.73–0.78） | 正式版主结果 |
| Foil 平衡准确率 | 0.72（0.71–0.73） | STL-GROVER 0.70（0.69–0.71） | 补充 Fig. S1 |
| Foil 灵敏度 | 0.64（0.62–0.66） | STL-DeepAmes 0.97（0.96–0.98） | 补充 Fig. S1 |

Foil 实验使用 1,000 次分层 bootstrap 计算区间。STL-DeepAmes 在该集灵敏度高，但平衡准确率为 0.51，表明只看灵敏度会遗漏误报问题。

正式版主测试集为 4,208 条记录；预印本 v2 为 4,528 条。两版数据清洗和成绩有所变化，本文采用正式版。Foil 数据缺少菌株/S9 信息，作为独立场景单列。

## 代码与参考资料

[代码与项目](https://github.com/Model-Medicines/TCL-Ames)

作者库公开比较模型的训练代码、部分检查点、AmesNet 预测值及 bootstrap 分析；仓库未列出 AmesNet 主模型训练代码和权重入口。

资料核对：**2026-09-22**。已核对正式摘要、可检索主结果段、正式补充 Fig. S1 及作者代码树；正文训练细节结合已有版本记录。

- [正式版](https://pubs.acs.org/crtoec/article/doi/10.1021/acs.chemrestox.6c00082/5170705/AmesNet-A-Task-Conditioned-Deep-Learning-Model)
- [正式摘要](https://pubmed.ncbi.nlm.nih.gov/42371678/)
- [正式补充材料](https://doi.org/10.1021/acs.chemrestox.6c00082.s001)
- [作者代码与预测数据](https://github.com/Model-Medicines/TCL-Ames)
- [正式补充材料 Fig. S1](https://acs.figshare.com/articles/journal_contribution/32825956)
