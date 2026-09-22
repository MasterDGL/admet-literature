# AttentiveFP

**Pushing the Boundaries of Molecular Representation for Drug Discovery with the Graph Attention Mechanism**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.md)

**一句话概括：** 让图神经网络在汇总分子信息时学习关注哪些原子和邻域，用于性质预测与结构归因。

分类：基础方法。主题：分子图、注意力、分子表示。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Medicinal Chemistry 63(16), 8749–8760；2019 年在线，2020-08-27 卷期 |
| 日期口径 | 在线年份；精确在线日存在来源字段冲突，卷期日期另列 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 分子表示需要捕捉局部及较远结构联系，同时让模型关注的化学特征更容易检查。 |
| 数据集 | 论文配套作者库提供 BBBP、HIV、BACE、ClinTox、SIDER、Tox21、ToxCast、ESOL（delaney）、FreeSolv（SAMPL）、Lipophilicity、QM9 等数据文件，以及芳香性解释示例；覆盖分类与回归，并非全部都是 ADMET 任务。 |
| 方法 | 在分子图消息聚合和图级读出中使用注意力，构建可学习的分子指纹，并通过注意力可视化分析结构信息。 |
| 结论 | 作者报告在所测任务上取得当时先进表现，并展示学习非局部分子内联系的例子；这里将其收录为图注意力基线。 |

DOI：`10.1021/acs.jmedchem.9b00959`

## 评测与结论适用范围

本条不引用跨数据集汇总排名；各数据集、划分和训练配置需按原论文及版本逐项对齐后再比较。

注意力权重是模型解释线索，不是已证明的因果机制。日期存在源字段冲突：Crossref/ACS 页首为 2019-08-13，检索到的 ACS history 为 2019-08-27，因此在线时间保留到年。

## 代码与证据

[代码或项目入口](https://github.com/OpenDrugAI/AttentiveFP)

代码状态：作者代码与配套数据可访问；复现说明提示原 Code Ocean 环境不可直接下载，需重建环境；未独立复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-22**。核对范围：书目与日期冲突、原始摘要、作者实现和数据目录、REPRODUCING.md；未完整复核逐数据集结果表。

- [正式论文](https://doi.org/10.1021/acs.jmedchem.9b00959)
- [书目元数据](https://api.crossref.org/works/10.1021/acs.jmedchem.9b00959)
- [作者实现](https://github.com/OpenDrugAI/AttentiveFP)
- [作者配套数据目录](https://github.com/OpenDrugAI/AttentiveFP/tree/master/data)
