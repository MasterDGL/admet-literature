# MoleculeNet

**MoleculeNet: a benchmark for molecular machine learning**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.md)

**一句话概括：** 把分散的分子数据集、划分、指标与算法组织成基准，让性质预测方法有共同的比较起点。

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

## 评测与结论适用范围

不同子集采用适合任务的指标/划分；使用时记录具体子集、数据版本、清洗和 split，不能将“MoleculeNet”当作单一任务。

不是所有子集都属于 ADMET。DeepChem 当前加载版本与原论文可能不同；Crossref 年份信息不如出版社精确，采用出版社 2017-10-31 在线日期并保留 2018 卷期。

## 代码与证据

[代码或项目入口](https://github.com/deepchem/deepchem)

代码状态：作者代码入口可访问；未验证完整安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-22**。核对范围：出版社书目、摘要/基准描述与 DeepChem 官方入口；未运行各子集。

- [出版社原文](https://pubs.rsc.org/en/content/articlelanding/2017/sc/c7sc02664a)
- [DeepChem](https://github.com/deepchem/deepchem)
