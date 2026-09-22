# BBB MegaMolBART

**Predicting blood–brain barrier permeability of molecules with a large language model and machine learning**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.md)

**一句话概括：** 用分子语言模型和 XGBoost 预测血脑屏障通透性，并用人源三维 BBB 球体检验部分候选。

分类：专题补读。主题：BBB、分子语言模型、体外验证。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Scientific Reports 14, 15844；2024-07-09 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | BBB 标注数据有限，分子预训练表示能否改善预测并得到体外实验支持仍需检验。 |
| 数据集 | B3DB 7,807 个分子（4,956 BBB+、2,851 BBB−），CMUH 2,499 个分子（105 BBB+、2,394 BBB−）；B3DB 中 1,058 个有 logBB 数值。另选择 21 个预测可透过和 5 个不可透过候选做球体实验，并设置对照。 |
| 方法 | MegaMolBART 编码 SMILES，再用 XGBoost 分类/回归；与 Morgan 指纹比较。人脑微血管内皮细胞、周细胞及星形胶质细胞构成 BBB 球体，以 LC–MS/MS 测定通透性。 |
| 结论 | 作者报告最终留出测试 AUROC 0.88，所选候选的球体实验与预测方向一致，支持该流程用于 BBB 筛选探索。 |

DOI：`10.1038/s41598-024-66897-y`

## 评测与结论适用范围

原文比较 B3DB 单独训练、CMUH 外测及混合数据方案；最终分类流程将 B3DB/CMUH 数据按 80/10/10 分配。0.88 不能直接当作完全独立 CMUH 外测成绩。

实验候选来自极高/极低预测分数，不能估计所有候选的无偏准确率。体外球体结果不等于人体 BBB 通透性或临床有效性；数据合并与预训练重叠也需审计。

## 代码与证据

原文列出 B3DB 和 MegaMolBART 组件；本次未确认本文端到端训练实现，组件不等于论文完整代码

代码状态：原文列出 B3DB 和 MegaMolBART 组件；本次未确认本文端到端训练实现，组件不等于论文完整代码。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-22**。核对范围：书目、正文相关方法与结果及列出的官方资源。

- [出版社全文及补充材料](https://www.nature.com/articles/s41598-024-66897-y)
- [B3DB 数据来源](https://github.com/theochem/B3DB)
