# AIDD 知识地图与阅读路线

[English](../en/docs/knowledge-map.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [ADMET 总表](../topics/admet.md) · [基础方法与基准](../topics/foundations.md)

![AIDD 五层知识地图](../assets/aidd-knowledge-pyramid.svg)

这张图将 AIDD 研究分为五个阅读层次：先了解数据与研究问题，再学习分子表示和预测方法，进而理解分子设计与实验验证。每层都提供对应的研究问题和论文入口。

## 五层分别解决什么问题

| 层级（自下而上） | 读者要回答的问题 | 当前入口与覆盖 |
| --- | --- | --- |
| 数据与研究问题 | 预测对象是什么？标签来自什么实验？训练与测试如何分开？ | [MoleculeNet](../papers/foundations/moleculenet-2018.md)、[TDC](../papers/admet/tdc-2021.md)、[PharmaBench](../papers/admet/pharmabench-2024.md)；[MoleculeACE](../papers/foundations/moleculeace-2022.md)帮助检查活性悬崖 |
| 分子与蛋白表示 | 如何将结构、序列、构象与背景信息转换成可学习输入？ | [Chemprop/D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md)、[AttentiveFP](../papers/foundations/attentivefp-2019.md)、[KPGT](../papers/admet/kpgt-2023.md)；蛋白表示与结构专题待扩展 |
| 预测任务 | 分子是否有活性、能否到达目标部位、是否存在安全性风险？ | 当前主线是 [ADMET 与 PK](../topics/admet.md)，含毒性、吸收/分布、代谢与药代预测；结合、对接和虚拟筛选待扩展 |
| 设计与优化 | 如何提出兼顾活性、ADMET 与可合成性的候选？ | 计划扩展分子生成、多参数优化、反应预测和合成规划；目前没有独立专题 |
| 实验验证与迭代 | 预测是否经新实验支持？结果如何用于下一轮研究？ | [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md)提供体外验证案例；完整设计–制备–测试–分析闭环待扩展 |

ADMET 位于预测层，为分子设计提供吸收、分布、代谢、排泄和毒性方面的约束。设计产生候选，实验检验预测，新增数据再用于改进模型；图中的反馈箭头表示这一研究循环。

基准、误差分析、不确定性和复现贯穿整个流程。MoleculeACE 以生物活性悬崖为例，帮助读者理解相似分子的预测难点，因此放在基础评测入口。

## 从哪里开始读

1. **建立数据与方法基础**：MoleculeNet → Chemprop/D-MPNN → AttentiveFP → TDC。先区分任务、标签、特征、划分和指标。
2. **进入具体 ADMET 问题**：hERG 可读 [CardioTox net](../papers/admet/cardiotox-net-2021.md) → [HERGAI](../papers/admet/hergai-2025.md)；转运体读 [MC-PGP](../papers/admet/mc-pgp-2025.md)；致突变性读 [AMES 多任务 DNN](../papers/admet/ames-multitask-2022.md) → [AmesNet](../papers/admet/amesnet-2026.md)。沿同一主题比较数据、模型和实验设计的变化。
3. **检查可靠性和实验支持**：结合 [ADMET 可靠性评测](../papers/admet/admet-reliability-2026.md)、MoleculeACE 与 BBB 实验案例，分析平均指标是否掩盖失败情形、结论是否适用于新分子。

专题入口：用 [AI 药物毒性预测综述](../papers/admet/ai-toxicity-review-2023.md)了解毒性任务、数据和工具；沿 [SSL-GCN](../papers/admet/ssl-gcn-2021.md)学习如何利用无标签分子，沿 [Domain-aware / pBRICS](../papers/admet/domain-aware-pbrics-2023.md)了解化学片段与模型解释，沿 [Uni-QSAR](../papers/admet/uni-qsar-2023.md)了解多种分子表示的自动选择与集成。

不确定性估计可从[毒性深度共形预测](../papers/admet/tox21-conformal-2021.md)开始，理解置信水平、覆盖率与单标签预测比例；[Tox21 10K 化合物库](../papers/admet/tox21-library-2020.md)介绍毒性数据的实验来源和质量控制。横向比较见[方法对比](comparison.md)，获取数据见[数据集字典](datasets.md)。

## 后续扩展方式

新专题按研究问题接入对应层，相关论文可以跨层引用。每篇保持“一句话概括、发表信息、痛点、数据集、方法、结论”的结构，并附实验分析与参考资料。

图的可编辑源文件为 [SVG](../assets/aidd-knowledge-pyramid.svg)，无需外部图床；通过 README 的图片链接可打开大图。
