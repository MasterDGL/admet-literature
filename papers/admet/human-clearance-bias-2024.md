# Prediction of Human Clearance Using In Silico Models with Reduced Bias

[English](../../en/papers/admet/human-clearance-bias-2024.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Molecular Pharmaceutics · 2024-01-29* · 已发表 · 专题补读

**内容概述：** 排除测试分子的同类和高相似训练化合物，检验人体清除率模型对新化学结构的预测能力。

主题：人体清除率、泛化、共形预测、随机森林。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Molecular Pharmaceutics 21(3), 1192–1203；2024-01-29 在线发表，2024-03-04 卷期。 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 训练集中的结构近邻和治疗类别关联会影响泛化评估，需要衡量远离已有化学系列时的清除率预测误差。 |
| 数据集 | 汇编 1,340 个具有人体静脉 PK 数据的化合物；Test343 是含 343 个化合物的准前瞻性测试集。预测人体清除率，单位 mL/min/kg。 |
| 方法 | 分子描述符随机森林，比较 ChemProp 和 PLS；R4 针对每个测试分子，移除同一结构–治疗类别或 Tanimoto 相似度 >0.7 的训练化合物，再单独训练模型。另用共形预测估计区间。 |
| 结论 | Test343 上 RF 的 GMFE 从 R3 的 3.11 变为严格排除近邻后 R4 的 3.33，两倍误差内比例从 44% 降至 41%；这一对照量化了训练集组成对评估的影响。 |

DOI：`10.1021/acs.molpharmaceut.3c00812`

## 实验设置与结果分析

**实验设计。** R3 对 Test343 使用一个以 Lombardo 2014 数据训练的模型；R4 为 343 个测试分子分别筛除近邻并训练，共 343 个模型。

| 模型 | GMFE ↓ | 两倍误差内比例 ↑ | 三倍误差内比例 ↑ |
| --- | --- | --- | --- |
| RF R3 | 3.11 | 44% | 60% |
| RF R4 | 3.33 | 41% | 57% |
| ChemProp CP4 | 3.27 | 39% | 57% |
| PLS4 | 4.80 | 36% | 53% |

来源：Table S9。CP4/PLS4 采用对应的逐分子排除设置。Table S8 中 R4 对清除率 >20.7 mL/min/kg 的 47 个分子 GMFE 为 11.66，显示整体均值之外的高误差子群。

不同清除机制和清除率区间的误差差别较大。R4 的逐测试分子重训协议与单个固定模型的测试需要分别解释。

## 代码与参考资料

[代码与项目](https://acs.figshare.com/articles/dataset/25104249)

出版社附件公开 KNIME 工作流 ZIP 和数据 XLSX；已核对文件内容入口，未执行工作流。

资料核对：**2026-09-22**。已核对正式摘要、补充 Tables S3、S8、S9、数据 XLSX 及 KNIME 工作流压缩包；未复现模型。

- [正式摘要与出版日期](https://pubmed.ncbi.nlm.nih.gov/38285644/)
- [正式补充材料：Tables S3、S8、S9](https://acs.figshare.com/articles/journal_contribution/25104243)
- [人体清除率数据 XLSX](https://acs.figshare.com/articles/dataset/25104246)
- [作者 KNIME 工作流](https://acs.figshare.com/articles/dataset/25104249)
