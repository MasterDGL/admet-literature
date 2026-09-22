# Revisiting ADMET prediction reliability under real-world challenges in the foundation model era

[English](../../en/papers/admet/admet-reliability-2026.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Cheminformatics · 2026-05-18* · 已发表 · 核心论文

**内容概述：** 在小样本、陌生分子结构和类别不均衡等条件下比较多类模型，检验 ADMET 预测在实际研究中是否可靠。

主题：泛化、小样本、评测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 18, 95；2026-05-18 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 常规平均成绩不足以反映小样本、分布外预测、类别不均衡、超出五规则的分子及活性悬崖中的可靠性。 |
| 数据集 | 清洗后的 14 个性质数据集及 MoleculeACE 的 30 个活性任务。代表性规模：BBBP 3,873、hERG 9,673、Caco-2 842、半衰期 1,314、VDss 1,092、CycPept-PAMPA 6,637 个样本（Table 1）。这些是本文整理后的版本。 |
| 方法 | 在统一实验框架中比较 KPGT、Uni-Mol、TabPFNv2、经典机器学习及 AutoML；采用随机、骨架和 Perimeter 划分，并研究重采样与集成。 |
| 结论 | 在所测小样本/OOD 场景中，TabPFNv2 常有优势；欠采样集成有助于不均衡问题；数据较充足时 KPGT 在环肽渗透性上表现突出；活性悬崖仍是共同难点。 |

DOI：`10.1186/s13321-026-01217-2`

## 实验设置与结果分析

**实验设计。** 比较随机、骨架和 Perimeter 划分。每种划分使用 5 个划分种子，每个划分再训练 5 次，共 25 次结果；AutoGluon 每种划分给出 5 次结果。对照涵盖 KPGT、Uni-Mol、GEM、图网络、经典机器学习、TabPFNv2 和 AutoGluon。分类结合 AUROC、召回率、F1 和假阳性率分析；回归使用 R² 等指标。

| 场景 | 具体结果 | 原文位置 |
| --- | --- | --- |
| Tox21 NR ER 类别不均衡 | KPGT 加欠采样集成后，召回率由 0.22 提高到 0.60；假阳性率 0.27 | Fig. 4 |
| 环肽渗透性，6,637 个样本 | KPGT R² 0.627；GNNAK 0.605 | Fig. 5 |
| 活性悬崖分子 | KPGT R² 0.46；XGBoost + MorganCount 0.51 | Fig. 6b |
| 活性悬崖对识别 | MOLMCL 召回率 0.130，KPGT 0.128 | Fig. 6c |

结果说明模型选择需要结合数据量、分布变化和任务类型。活性悬崖实验来自生物活性数据；其中的结论用于分析表示学习能力，不能直接当作 ADMET 端点成绩。

## 代码与参考资料

[代码与项目](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。已核对正文 Methods、Table 1 和 Figs. 4–6 的实验设计与结果。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-026-01217-2)
- [作者代码](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)
