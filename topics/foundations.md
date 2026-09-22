# 基础方法与基准

[English](../en/topics/foundations.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [知识地图](../docs/knowledge-map.md) · [筛选规则](../docs/curation.md) · [下载 CSV](../data/papers.csv)

这些文献介绍分子表示、公共数据与评测方法，为阅读 ADMET 研究提供基础。MoleculeACE 专门讨论生物活性悬崖。

本专题共 **4 篇**，按发表日期从新到旧排列。点击论文名查看一句话概括、实验设置、结果分析和资料来源。

| 发表时间 | 论文与分类 | 期刊/会议与时间 | 主要痛点 | 数据集 | 方法 | 结论 |
| --- | --- | --- | --- | --- | --- | --- |
| 2022-12-01 | [MoleculeACE](../papers/foundations/moleculeace-2022.md) · [原文](https://doi.org/10.1021/acs.jcim.2c01073)<br>数据与基准 | Journal of Chemical Information and Modeling 62(23), 5938–5951；2022-12-01；附 2023 年勘误 | 整体平均误差不能充分反映模型处理活性悬崖的能力，而这些分子对先导优化很重要。 | 30 个大分子靶标的整理后生物活性数据集，比较 24 种机器学习策略；作者库提供数据和评测流程。 | 定义相似结构但活性差异大的分子对，同时报告整体 RMSE 与悬崖分子 RMSEcliff，比较描述符模型和图/序列神经网络。 | 在所测活性悬崖场景中，多种描述符机器学习方法优于更复杂深度模型；性能随靶标而变，支持单独报告悬崖指标。 |
| 2019-07-30 | [Chemprop / D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md) · [原文](https://doi.org/10.1021/acs.jcim.9b00237)<br>基础方法 | Journal of Chemical Information and Modeling 59(8), 3370–3388；2019-07-30 | 学习得到的分子表示是否优于手工描述符，尤其能否推广到工业数据和新化学空间，缺少充分比较。 | 19 个公开与 16 个工业私有数据集，覆盖多类化学端点。 | 有向键消息传递网络 D-MPNN，结合分子级计算特征及超参数优化；与固定描述符方法及已有图网络比较。 | 在论文所测公开/工业任务中达到或超过多种对照，显示学习表示的实际价值；仍未达到实验重复性水平，结果取决于任务与划分。 |
| 2019 | [AttentiveFP](../papers/foundations/attentivefp-2019.md) · [原文](https://doi.org/10.1021/acs.jmedchem.9b00959)<br>基础方法 | Journal of Medicinal Chemistry 63(16), 8749–8760；2019 年在线，2020-08-27 卷期 | 分子表示需要捕捉局部及较远结构联系，同时让模型关注的化学特征更容易检查。 | 论文配套作者库提供 BBBP、HIV、BACE、ClinTox、SIDER、Tox21、ToxCast、ESOL（delaney）、FreeSolv（SAMPL）、Lipophilicity、QM9 等数据文件，以及芳香性解释示例，覆盖 ADMET、活性、理化与量子化学任务。 | 在分子图消息聚合和图级读出中使用注意力，构建可学习的分子指纹，并通过注意力可视化分析结构信息。 | 作者报告在所测任务上取得当时先进表现，并通过可视化展示模型学习非局部分子内联系的例子。 |
| 2017-10-31 | [MoleculeNet](../papers/foundations/moleculenet-2018.md) · [原文](https://doi.org/10.1039/C7SC02664A)<br>数据与基准 | Chemical Science 9(2), 513–530（2018 卷期）；2017-10-31 在线 | 不同研究自选数据、指标与实现，难以判断算法改进来自模型还是评测设置。 | 整合量子化学、理化、生物物理及生理相关公开数据；包括 ESOL、FreeSolv、Lipophilicity、BBBP、Tox21、ClinTox、SIDER、BACE、HIV、QM 系列等，按任务设置评价指标和划分。 | 以 DeepChem 提供数据加载、分子特征化和学习算法实现，系统比较固定描述符与学习表示。 | 学习表示在多类任务上有效，但小样本和类别不均衡仍困难；量子/生物物理任务中，符合物理背景的特征可能比算法选择更关键。 |
