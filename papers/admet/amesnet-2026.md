# AmesNet

**AmesNet: A Task-Conditioned Deep Learning Model with Enhanced Sensitivity and Generalization in Ames Mutagenicity Prediction**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.md)

**一句话概括：** 将分子结构、菌株与代谢活化条件一起输入模型，提高陌生化学结构的 Ames 致突变性识别能力。

分类：核心论文。主题：AMES、实验条件、分布外预测。

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

沿用来源研究的 OOD 分区，去除跨分区相同非立体 SMILES；主任务与 Foil 测试分别报告指标。国际 Ames/QSAR 挑战成绩用于研究背景比较。

正式版测试集为 4,208 条记录、灵敏度 0.72；预印本 v2 对应 4,528 条和 0.73。版本更新涉及数据清洗，本文采用正式版结果。

## 代码与参考资料

[代码与项目](https://github.com/Model-Medicines/TCL-Ames)

TCL 比较模型、预测数据与统计代码已公开；部分大文件另存 Hugging Face，未确认完整 AmesNet 实现与权重。

资料核对：**2026-09-22**。正式版书目/摘要、出版社可检索的方法段、补充材料、预印本 v2 方法与作者仓库；ACS 连续全文访问受限。

- [正式版](https://pubs.acs.org/crtoec/article/doi/10.1021/acs.chemrestox.6c00082/5170705/AmesNet-A-Task-Conditioned-Deep-Learning-Model)
- [正式摘要](https://pubmed.ncbi.nlm.nih.gov/42371678/)
- [正式补充材料](https://doi.org/10.1021/acs.chemrestox.6c00082.s001)
- [作者代码与预测数据](https://github.com/Model-Medicines/TCL-Ames)
