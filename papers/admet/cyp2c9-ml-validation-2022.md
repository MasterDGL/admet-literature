# Machine learning-driven identification of drugs inhibiting cytochrome P450 2C9

[English](../../en/papers/admet/cyp2c9-ml-validation-2022.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*PLOS Computational Biology · 2022-01-26* · 已发表 · 专题补读

**内容概述：** 结合分子描述符和 CYP2C9 多构象对接筛选抑制剂，并通过新实验检验候选药物。

主题：CYP2C9、结构信息、集成对接、实验验证。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | PLOS Computational Biology 18(1), e1009820；2022-01-26。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | CYP2C9 抑制受到配体性质和蛋白柔性的共同影响，计算筛选需要与抑制实验衔接。 |
| 数据集 | PubChem/ChEMBL 经清洗、药物样过滤和聚类后保留 8,141 个化合物：4,840 抑制剂、3,301 非抑制剂。按类别随机 80/20 留出；另筛选 4,480 个药物，选择 18 个进行实验。 |
| 方法 | 36 个 MOE 描述符与 7 个蛋白构象的对接能，训练 RF/SVM；结合模型共识、对接能阈值与多样性筛选，进行 HepG2 和 CYP2C9 supersome 实验。 |
| 结论 | Table 3 的 RF 平衡准确率为 84.33%、敏感度 89.97%。18 个候选经实验检验，确认四种较强抑制剂；vatalanib 的 IC50 为 0.067 μM。 |

DOI：`10.1371/journal.pcbi.1009820`

## 实验设置与结果分析

**实验设计。** 论文称为“external”的模型验证集来自同一汇编集的分层随机留出；新候选的实验验证另行开展。

| 模型（Table 3） | 平衡准确率 ↑ | 敏感度 ↑ | 特异度 ↑ |
| --- | --- | --- | --- |
| RF，36 MOE＋7 IE | 84.33% | 89.97% | 78.69% |
| SVM，36 MOE＋7 IE | 83.35% | 89.87% | 76.83% |

Table 3 的 Accuracy 列按正文定义为平衡准确率。Table 5 的 supersome IC50：vatalanib 0.067、piriqualone 10.9、ticagrelor 11.8、cloperidone 17.7 μM。

CYP2C9 酶抑制和体内药物相互作用是不同评价层次；实验结果支持所测条件下的抑制活性。模型依赖 MOE 描述符与对接计算。

## 代码与参考资料

正文与补充材料提供数据和实验细节；论文未列出独立代码仓库。

资料核对：**2026-09-22**。已核对正式全文、数据过滤与 80/20 划分、模型特征、Tables 3/5 及候选筛选和实验流程。

- [正式全文、方法与 Tables 3、5](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009820)
- [开放全文与补充材料](https://pmc.ncbi.nlm.nih.gov/articles/PMC8820617/)
