# AIDD 知识地图与阅读路线

[返回首页](../README.md) · [ADMET 总表](../topics/admet.md) · [基础方法与基准](../topics/foundations.md)

![AIDD 五层知识地图](../assets/aidd-knowledge-pyramid.svg)

这张图按照“研究依赖什么、产出能支持什么决策”组织论文。它是本仓库的导航方案，不是公认唯一的学科分类。由下到上更接近设计和实验决策；高度、面积和颜色不代表重要性、性能或证据等级。

## 五层分别解决什么问题

| 层级（自下而上） | 读者要回答的问题 | 当前入口与覆盖 |
| --- | --- | --- |
| 数据与研究问题 | 预测对象是什么？标签来自什么实验？训练与测试如何分开？ | [MoleculeNet](../papers/foundations/moleculenet-2018.md)、[TDC](../papers/admet/tdc-2021.md)、[PharmaBench](../papers/admet/pharmabench-2024.md)；[MoleculeACE](../papers/foundations/moleculeace-2022.md)帮助检查活性悬崖 |
| 分子与蛋白表示 | 如何将结构、序列、构象与背景信息转换成可学习输入？ | [Chemprop/D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md)、[AttentiveFP](../papers/foundations/attentivefp-2019.md)、[KPGT](../papers/admet/kpgt-2023.md)；蛋白表示与结构专题待扩展 |
| 预测任务 | 分子是否有活性、能否到达目标部位、是否存在安全性风险？ | 当前主线是 [ADMET 与 PK](../topics/admet.md)，含毒性、吸收/分布、代谢与药代预测；结合、对接和虚拟筛选待扩展 |
| 设计与优化 | 如何提出兼顾活性、ADMET 与可合成性的候选？ | 计划扩展分子生成、多参数优化、反应预测和合成规划；目前没有独立专题 |
| 实验验证与迭代 | 预测是否经新实验支持？结果如何用于下一轮研究？ | [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md)提供体外验证案例；完整设计–制备–测试–分析闭环待扩展 |

ADMET 位于预测层，同时是设计优化的重要约束。一次高分预测并不意味着候选一定有效或安全。设计可能回到数据与表示，实验结果也会产生新标签；图中的反馈箭头表示这种迭代关系。

基准、误差分析、不确定性和复现贯穿所有层，并不只在底层发生。MoleculeACE 的主体是生物活性评测，因此属于基础评测入口，不算 ADMET 专属端点数据集。

## 从哪里开始读

1. **建立数据与方法基础**：MoleculeNet → Chemprop/D-MPNN → AttentiveFP → TDC。先区分任务、标签、特征、划分和指标。
2. **进入具体 ADMET 问题**：hERG 可读 [CardioTox net](../papers/admet/cardiotox-net-2021.md) → [HERGAI](../papers/admet/hergai-2025.md)；转运体读 [MC-PGP](../papers/admet/mc-pgp-2025.md)；致突变性读 [AMES 多任务 DNN](../papers/admet/ames-multitask-2022.md) → [AmesNet](../papers/admet/amesnet-2026.md)。这表示主题上的阅读顺序，不表示后文全面替代前文。
3. **检查可靠性和实验支持**：结合 [ADMET 可靠性评测](../papers/admet/admet-reliability-2026.md)、MoleculeACE 与 BBB 实验案例，分析平均指标是否掩盖失败情形、结论是否适用于新分子。

## 后续扩展方式

保留本图的五层结构，将新专题接入对应层，必要时跨层引用。只为已有内容提供正式论文入口，待扩展方向明确标注。每篇仍保持“一句话概括、发表信息、痛点、数据集、方法、结论、评测边界”的结构。

图的可编辑源文件为 [SVG](../assets/aidd-knowledge-pyramid.svg)，无需外部图床；通过 README 的图片链接可打开大图。
