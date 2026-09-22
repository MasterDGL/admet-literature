# 基础方法与基准

[返回首页](../README.md) · [知识地图](../docs/knowledge-map.md) · [筛选规则](../docs/curation.md) · [下载 CSV](../data/papers.csv)

这些文献提供分子表示、数据与评测基础，不作为当前 ADMET SOTA 排名。MoleculeACE 主要研究生物活性悬崖。

本专题共 **4 篇**。组内按记录的发表日期倒序；内容核验日期与范围见各篇。点击论文名查看一句话概括、评测设置和限制。

## 基础方法

| 论文与解读 | 期刊/会议与时间 | 主要痛点 | 数据集 | 方法 | 结论 |
| --- | --- | --- | --- | --- | --- |
| [Chemprop / D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md) · [原文](https://doi.org/10.1021/acs.jcim.9b00237) | Journal of Chemical Information and Modeling 59(8), 3370–3388；2019-07-30 | 学习得到的分子表示是否优于手工描述符，尤其能否推广到工业数据和新化学空间，缺少充分比较。 | 19 个公开与 16 个工业私有数据集，覆盖多类化学端点；不是 35 个 ADMET 数据集，工业数据也并非全部公开。 | 有向键消息传递网络 D-MPNN，结合分子级计算特征及超参数优化；与固定描述符方法及已有图网络比较。 | 在论文所测公开/工业任务中达到或超过多种对照，显示学习表示的实际价值；仍未达到实验重复性水平，结果取决于任务与划分。 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) · [原文](https://doi.org/10.1021/acs.jmedchem.9b00959) | Journal of Medicinal Chemistry 63(16), 8749–8760；2019 年在线，2020-08-27 卷期 | 分子表示需要捕捉局部及较远结构联系，同时让模型关注的化学特征更容易检查。 | 论文配套作者库提供 BBBP、HIV、BACE、ClinTox、SIDER、Tox21、ToxCast、ESOL（delaney）、FreeSolv（SAMPL）、Lipophilicity、QM9 等数据文件，以及芳香性解释示例；覆盖分类与回归，并非全部都是 ADMET 任务。 | 在分子图消息聚合和图级读出中使用注意力，构建可学习的分子指纹，并通过注意力可视化分析结构信息。 | 作者报告在所测任务上取得当时先进表现，并展示学习非局部分子内联系的例子；这里将其收录为图注意力基线。 |

## 数据与基准

| 论文与解读 | 期刊/会议与时间 | 主要痛点 | 数据集 | 方法 | 结论 |
| --- | --- | --- | --- | --- | --- |
| [MoleculeACE](../papers/foundations/moleculeace-2022.md) · [原文](https://doi.org/10.1021/acs.jcim.2c01073) | Journal of Chemical Information and Modeling 62(23), 5938–5951；2022-12-01；附 2023 年勘误 | 整体平均误差不能充分反映模型处理活性悬崖的能力，而这些分子对先导优化很重要。 | 30 个大分子靶标的整理后生物活性数据集，比较 24 种机器学习策略；不是 30 个 ADMET 端点，作者库提供数据和评测流程。 | 定义相似结构但活性差异大的分子对，同时报告整体 RMSE 与悬崖分子 RMSEcliff，比较描述符模型和图/序列神经网络。 | 在所测活性悬崖场景中，多种描述符机器学习方法优于更复杂深度模型；性能随靶标而变，支持单独报告悬崖指标。 |
| [MoleculeNet](../papers/foundations/moleculenet-2018.md) · [原文](https://doi.org/10.1039/C7SC02664A) | Chemical Science 9(2), 513–530（2018 卷期）；2017-10-31 在线 | 不同研究自选数据、指标与实现，难以判断算法改进来自模型还是评测设置。 | 整合量子化学、理化、生物物理及生理相关公开数据；包括 ESOL、FreeSolv、Lipophilicity、BBBP、Tox21、ClinTox、SIDER、BACE、HIV、QM 系列等，按任务设置评价指标和划分。 | 以 DeepChem 提供数据加载、分子特征化和学习算法实现，系统比较固定描述符与学习表示。 | 学习表示在多类任务上有效，但小样本和类别不均衡仍困难；量子/生物物理任务中，符合物理背景的特征可能比算法选择更关键。 |
