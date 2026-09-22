# MoleculeNet

[English](../../en/papers/foundations/moleculenet-2018.md) | **简体中文**

**MoleculeNet: a benchmark for molecular machine learning**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 把分散的分子数据集、划分、指标与算法组织成基准，让性质预测方法有共同的比较起点。

分类：数据与基准。主题：数据集、基准、评测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Chemical Science 9(2), 513–530（2018 卷期）；2017-10-31 在线 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 不同研究自选数据、指标与实现，难以判断算法改进来自模型还是评测设置。 |
| 数据集 | 整合量子化学、理化、生物物理及生理相关公开数据；包括 ESOL、FreeSolv、Lipophilicity、BBBP、Tox21、ClinTox、SIDER、BACE、HIV、QM 系列等，按任务设置评价指标和划分。 |
| 方法 | 以 DeepChem 提供数据加载、分子特征化和学习算法实现，系统比较固定描述符与学习表示。 |
| 结论 | 学习表示在多类任务上有效，但小样本和类别不均衡仍困难；量子/生物物理任务中，符合物理背景的特征可能比算法选择更关键。 |

DOI：`10.1039/C7SC02664A`

## 实验设置与结果分析

各子集按任务设置指标和划分；开展比较时记录具体子集、数据版本、清洗步骤与 split。

数据涵盖 ADMET、活性、理化及量子化学任务；DeepChem 随版本更新数据加载流程。发表时间采用出版社的 2017-10-31 在线日期，并列 2018 年卷期。

## 代码与参考资料

[代码与项目](https://github.com/deepchem/deepchem)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。出版社书目、摘要/基准描述与 DeepChem 官方入口；未运行各子集。

- [出版社原文](https://pubs.rsc.org/en/content/articlelanding/2017/sc/c7sc02664a)
- [DeepChem](https://github.com/deepchem/deepchem)
