# Awesome AIDD Papers

AI-aided drug discovery papers with structured, source-linked research notes.

面向 **AI 辅助药物发现（AIDD）** 的论文整理。每篇记录 **发表期刊/会议与时间、主要痛点、数据集、方法、结论**，并补充评测条件、原文与代码链接。

首个专题为 **ADMET 与药代动力学**。目前收录 **19 篇**：14 篇正式研究/数据基准论文、1 篇正式观点文章、4 篇预印本。其中 **8 篇**建议优先精读。首批内容核验日期为 **2026-09-19**；仓库整理日期为 **2026-09-21**。后续更新以各条目核验日期为准。

## 导航

- [ADMET 论文总表](topics/admet.md)：按研究用途分类，逐篇保留五项核心信息。
- [优先精读](#优先精读)：先建立研究问题、数据和方法的认识。
- [论文梳理](#论文梳理)：直接在本页查看全部 19 篇的一句话概括、发表信息、痛点、数据集、方法和结论。
- [筛选与 SOTA 判定](docs/curation.md)：如何判断结论可比、证据充分。
- [AIDD 研究范围](docs/scope.md)：当前覆盖与后续专题。
- [贡献方式](CONTRIBUTING.md)：推荐论文、纠正信息或补充实验依据。
- [结构化数据](data/papers.json) · [CSV 总表](data/papers.csv)。

| 专题 | 当前内容 | 入口 |
| --- | --- | --- |
| ADMET 与药代动力学 | 19 篇；其中 8 篇优先精读 | [论文总表](topics/admet.md) |
| 其他 AIDD 方向 | 扩展计划，尚未纳入独立专题 | [研究范围](docs/scope.md) |

## 优先精读

| 论文 | 期刊/会议 | 发表时间 | 一句话概括 |
| --- | --- | --- | --- |
| [ADMET可靠性评测](papers/admet/admet-reliability-2026.md) | Journal of Cheminformatics | 2026-05-18 | 在小样本、陌生分子结构和类别不均衡等条件下比较多类模型，检验 ADMET 预测在实际研究中是否可靠。 |
| [CaliciBoost](papers/admet/caliciboost-2025.md) | Journal of Cheminformatics | 2025-12-22 | 比较分子指纹和理化描述符，结合自动机器学习预测分子通过肠道细胞模型（Caco-2）的能力。 |
| [PKSmart](papers/admet/pksmart-2025.md) | Journal of Cheminformatics | 2025-09-26 | 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。 |
| [DCPM-ADMET](papers/admet/dcpm-admet-2026.md) | Journal of Cheminformatics | 2026-06-20 | 将两种预训练模型学到的分子表示与化学指纹结合，用于预测 97 项 ADMET 性质。 |
| [KPGT](papers/admet/kpgt-2023.md) | Nature Communications | 2023-11-21 | 把分子指纹和理化描述符融入图预训练，让模型学到更适合预测 ADMET 等性质的分子表示。 |
| [MolE](papers/admet/mole-2024.md) | Nature Communications | 2024-11-12 | 先在海量分子图上预训练，再利用生物学任务数据进一步训练，最后用于 ADMET 性质预测。 |
| [ADMET-AI](papers/admet/admet-ai-2024.md) | Bioinformatics | 2024-06-24 | 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。 |
| [MTGL-ADMET](papers/admet/mtgl-admet-2023.md) | iScience | 2023-11 | 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。 |

建议顺序：**真实场景评测 → 单端点与人体 PK → 表示学习与多任务方法 → 平台应用**。专题总表另列数据基准、观点文章和预印本，便于区分它们提供的证据。

## 怎样理解这里的 SOTA

领先结论必须对应 **任务、数据版本、数据划分、指标、比较对象和时间**。本仓库保留论文报告和公开榜单的适用范围，不将历史领先结果统一标为当前最优。所有条目均为文献整理，尚未由本仓库独立复现实验。

每篇论文有独立解读页；代码入口、权重可用性与实验复现分别记录。正式发表的 Perspective 也会明确标注，避免当作新模型的性能证据。

## 论文梳理

[核心论文](#核心论文) · [专题补读](#专题补读) · [数据与基准](#数据与基准) · [观点文章](#观点文章) · [预印本](#预印本)

下列内容均在本页展开。结论保留原文的比较范围；更完整的评测设置和局限见各条目的解读页。

### 核心论文

#### ADMET可靠性评测

**Revisiting ADMET prediction reliability under real-world challenges in the foundation model era**

**一句话概括：** 在小样本、陌生分子结构和类别不均衡等条件下比较多类模型，检验 ADMET 预测在实际研究中是否可靠。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 18, 95；2026-05-18 |
| 主要痛点 | 常规平均成绩不足以反映小样本、分布外预测、类别不均衡、超出五规则的分子及活性悬崖中的可靠性。 |
| 数据集 | 14 个性质/ADMET 相关数据集，涵盖 hERG、BBBP、Caco-2、半衰期、VDss、CYP 及肽性质等；另外使用 MoleculeACE 的 30 个生物活性任务。 |
| 方法 | 在统一实验框架中比较 KPGT、Uni-Mol、TabPFNv2、经典机器学习及 AutoML；采用随机、骨架和 Perimeter 划分，并研究重采样与集成。 |
| 结论 | 在所测小样本/OOD 场景中，TabPFNv2 常有优势；欠采样集成有助于不均衡问题；数据较充足时 KPGT 在环肽渗透性上表现突出；活性悬崖仍是共同难点。 |

[论文原文](https://link.springer.com/article/10.1186/s13321-026-01217-2) · [评测细节与局限](papers/admet/admet-reliability-2026.md) · [代码/项目](https://github.com/DonghaiZHAO-ZJU/Benchmark-ADMET-2025)

#### CaliciBoost

**CaliciBoost: Performance-driven evaluation of molecular representations for caco-2 permeability prediction**

**一句话概括：** 比较分子指纹和理化描述符，结合自动机器学习预测分子通过肠道细胞模型（Caco-2）的能力。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 17, 184；2025-12-22；此前有 2025 年预印本。 |
| 主要痛点 | Caco-2 渗透性数据少、实验条件不一致，不清楚哪些分子特征与建模策略最有效。 |
| 数据集 | TDC Caco2_Wang，906 个分子；另整理 OCHEM 数据，由 9,402 条原始记录经筛选清洗形成 5,481 条建模数据。两个来源的实验设置应分别阅读。 |
| 方法 | 系统比较分子指纹、RDKit/PaDEL/Mordred 描述符、CDDD 等表示；结合 AutoGluon、特征筛选、解释分析与超参数优化。 |
| 结论 | 精心选择的特征与集成学习在该端点上具有很强竞争力。核验日 TDC Caco-2 官方榜单列 CaliciBoost 的 MAE 为 0.256 ± 0.006、排名第一。 |

[论文原文](https://link.springer.com/article/10.1186/s13321-025-01137-7) · [评测细节与局限](papers/admet/caliciboost-2025.md) · [代码/项目](https://github.com/Calici/CaliciBoost)

#### PKSmart

**PKSmart: an open-source computational model to predict intravenous pharmacokinetics of small molecules**

**一句话概括：** 先预测动物体内的药代参数，再结合分子结构预测人体静脉给药后的清除率、分布容积和半衰期等指标。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 17, 147；2025-09-26 |
| 主要痛点 | 人体 PK 数据稀缺，单纯从结构学习困难；如何利用临床前物种信息提高人体参数预测？ |
| 数据集 | 1,283 个不同化合物的人体静脉 PK 数据，涉及 VDss、清除率、半衰期、游离分数和平均滞留时间；另有 371 个化合物的临床前动物数据，各端点标签数不同。 |
| 方法 | 两阶段建模：先由分子特征预测大鼠、犬和猴的相关 PK 参数，再将预测出的动物参数与分子特征结合，建立人体随机森林模型；使用重复嵌套交叉验证和外部验证。 |
| 结论 | 作者报告外部验证中 VDss、清除率的 R² 分别为 0.39、0.46，表明跨物种预测信息可改善部分人体 PK 端点。 |

[论文原文](https://link.springer.com/article/10.1186/s13321-025-01066-5) · [评测细节与局限](papers/admet/pksmart-2025.md) · [代码/项目](https://github.com/srijitseal/PKSmart)

#### DCPM-ADMET

**DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction**

**一句话概括：** 将两种预训练模型学到的分子表示与化学指纹结合，用于预测 97 项 ADMET 性质。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 18, 126；2026-06-20 |
| 主要痛点 | 单一分子表示难以同时覆盖语义、结构和理化信息；ADMET 标签稀疏且端点异质。 |
| 数据集 | 基于约 1.11 亿条 PubChem 数据预训练；ADMET 建模集合包含 97 个端点，43 个回归、54 个分类，共 465,470 条记录；另评估 10 个 MoleculeNet 数据集。记录数不等于去重后的分子数。 |
| 方法 | 融合 XLNet 语义表示、包含 SMILES→InChI 与性质学习的 GRU 组件，以及 ECFP 指纹；结合单任务随机森林、多任务神经网络和参数优化。 |
| 结论 | 论文报告在 67/97 个端点优于 ECFP 对照；在所比较的 10 个 MoleculeNet 任务中，5 个取得最佳结果。 |

[论文原文](https://link.springer.com/article/10.1186/s13321-026-01244-z) · [评测细节与局限](papers/admet/dcpm-admet-2026.md) · [代码/项目](https://github.com/zhangzhangleilei/DCPM-ADMET)

#### KPGT

**A knowledge-guided pre-training framework for improving molecular representation learning**

**一句话概括：** 把分子指纹和理化描述符融入图预训练，让模型学到更适合预测 ADMET 等性质的分子表示。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nature Communications 14, 7568；2023-11-21。作者另有 KDD 2022 前序版本，本条以期刊论文为准。 |
| 主要痛点 | 图预训练目标可能偏离下游任务需求；如何使表示保留化学知识并提高迁移能力？ |
| 数据集 | 约 200 万个 ChEMBL29 分子预训练；下游 63 个数据集，包括 11 个常用性质数据集、22 个 TDC ADMET 任务和 30 个 MoleculeACE 任务。 |
| 方法 | LiGhT 线图 Transformer，结合分子描述符和指纹进行知识引导预训练，再对下游任务微调。 |
| 结论 | 原文 Fig. 2c 与 Supplementary Table 8 报告，在当时比较的模型中，16/22 个 TDC ADMET 任务取得最佳表现。 |

[论文原文](https://www.nature.com/articles/s41467-023-43214-1) · [评测细节与局限](papers/admet/kpgt-2023.md) · [代码/项目](https://github.com/lihan97/KPGT)

#### MolE

**MolE: a foundation model for molecular graphs using disentangled attention**

**一句话概括：** 先在海量分子图上预训练，再利用生物学任务数据进一步训练，最后用于 ADMET 性质预测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nature Communications 15, 9431；2024-11-12。不能仅按其较早预印本年份记录。 |
| 主要痛点 | 怎样从超大规模无标签分子中学习可迁移表示，并与有标签的生物学任务信息结合？ |
| 数据集 | 约 8.42 亿个分子图用于自监督阶段，来自 ZINC20、ExCAPE-DB；随后进行监督多任务预训练；ADMET 评价覆盖 TDC 22 任务。 |
| 方法 | 引入解耦注意力，将原子内容信息与图中相对位置建模结合；先预测原子环境，再进行监督预训练和下游微调。 |
| 结论 | 作者报告相对于 2023 年 9 月的 TDC 已发表方法快照，在 10/22 个任务超过当时最佳成绩；实验报告多次运行的均值与标准差。 |

[论文原文](https://www.nature.com/articles/s41467-024-53751-y) · [评测细节与局限](papers/admet/mole-2024.md) · [代码/项目](https://github.com/recursionpharma/mole_public)

#### ADMET-AI

**ADMET-AI: a machine learning ADMET platform for evaluation of large-scale chemical libraries**

**一句话概括：** 将图神经网络用于网页和本地预测工具，一次预测多项 ADMET 性质，方便快速筛选大规模化合物库。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Bioinformatics 40(7), btae416；2024-06-24 在线发表，2024 年 7 月卷期。 |
| 主要痛点 | 大规模筛选需要兼顾多端点预测效果、吞吐量和本地部署能力。 |
| 数据集 | TDC 的 41 个预测任务：31 分类、10 回归；性能排名比较使用其中的 22 任务 ADMET Benchmark Group。 |
| 方法 | 论文版采用 Chemprop D-MPNN 与 200 个 RDKit 描述符；分别训练分类、回归多任务模型，并使用模型集成。 |
| 结论 | 作者在发表时报告 TDC ADMET 平均排名领先，并显示较高批量处理效率；提供网页与本地工具。 |

[论文原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11226862/) · [评测细节与局限](papers/admet/admet-ai-2024.md) · [代码/项目](https://github.com/swansonk14/admet_ai)

#### MTGL-ADMET

**ADMET property prediction via multi-task graph learning under adaptive auxiliary task selection**

**一句话概括：** 为每个 ADMET 预测任务自动挑选有帮助的辅助任务，减少多任务联合训练时的相互干扰。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | iScience 26(11), 108285；2023 年 11 月卷期。另有 RECOMB 2023 会议前序论文。 |
| 主要痛点 | 把所有 ADMET 任务放进同一个多任务模型可能产生负迁移；不同主任务需要不同的辅助任务。 |
| 数据集 | 从 8 篇文献汇集 24 个端点：18 分类、6 回归，共 43,291 个化合物；含吸收、分布、代谢、排泄、毒性和 2 个理化性质端点。 |
| 方法 | 以状态理论和最大流选择辅助任务，结合共享原子表示、任务特异注意力和以主任务为中心的门控模块。 |
| 结论 | 在论文所比较的多任务模型及消融实验中，自适应选任务和门控模块改善预测表现，支持“按主任务选择辅助任务”的设计。 |

[论文原文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10654589/) · [评测细节与局限](papers/admet/mtgl-admet-2023.md) · [代码/项目](https://github.com/dubingxue/MTGL-ADMET)

### 专题补读

#### HimNet

**A hierarchical interaction message net for accurate molecular property prediction**

**一句话概括：** 让原子、子结构和整个分子之间交换信息，用层级图神经网络预测分子性质及部分 ADMET 指标。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Communications Chemistry 9, 150；2026-02-14 |
| 主要痛点 | 原子、子结构与分子整体信息之间的交互不充分，单一层级的表示可能遗漏性质相关信息。 |
| 数据集 | 11 个数据集：8 个 MoleculeNet 子集及 Malaria、LMC、MetStab；其中 BBBP、Tox21、SIDER、ClinTox、代谢稳定性等与 ADMET 直接相关，其他任务属于更广泛性质/活性评价。 |
| 方法 | 层级消息传递与注意力，结合有向消息路径、跨层信息交互及多种指纹的一致性信息。 |
| 结论 | 原文 Tables 1–2 报告多个任务上的最佳或接近最佳成绩，支持层级融合的价值；不支持“全 ADMET 最优”。 |

[论文原文](https://www.nature.com/articles/s42004-026-01922-x) · [评测细节与局限](papers/admet/himnet-2026.md)

#### MolMCL

**Multi-channel learning for integrating structural hierarchies into context-dependent molecular representation**

**一句话概括：** 从分子整体、骨架和局部环境等层面学习表示，再按任务组合这些信息，用于性质和生物活性预测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nature Communications 16, 413；2025-01-06。DOI 中的 2024 不是正式发表年份。 |
| 主要痛点 | 不同任务依赖的分子结构层级不同，固定的图表示和读出方式难以适配所有任务。 |
| 数据集 | ZINC15 用于预训练；7 个 MoleculeNet 数据集及 MoleculeACE 的 30 个生物活性任务用于下游评价。 |
| 方法 | 分子、骨架和上下文相关的多通道学习，结合分子扰动、对比学习及提示引导的读出。 |
| 结论 | 多通道及任务适配改善所测分子任务的表示，活性悬崖实验显示该设计的价值；这些活性实验不是 30 项 ADMET 实验。 |

[论文原文](https://www.nature.com/articles/s41467-024-55082-4) · [评测细节与局限](papers/admet/molmcl-2025.md) · [代码/项目](https://github.com/yuewan2/MolMCL)

#### ADMETlab 3.0

**ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support**

**一句话概括：** 提供覆盖多类 ADMET 及理化性质的在线预测平台，并加入不确定性评估、API 和决策支持功能。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nucleic Acids Research 52(W1), W422–W431；2024-04-04 在线发表，2024 年 7 月卷期。 |
| 主要痛点 | 平台覆盖不足、调用不方便，且仅给出点预测难以支持化合物决策。 |
| 数据集 | 汇集超过 40 万条数据用于相关模型构建；平台共提供 119 项性质/评价输出，包括计算属性，不能等同于 119 个独立学习端点。 |
| 方法 | 多任务有向消息传递模型与描述符建模，结合预测不确定性、API 和决策支持功能。 |
| 结论 | 扩展了预测覆盖与使用方式；其主要价值包括平台整合，不能仅凭输出项目多就判定模型全面优于其他平台。 |

[论文原文](https://doi.org/10.1093/nar/gkae236) · [评测细节与局限](papers/admet/admetlab-3-2024.md)

#### admetSAR3.0

**admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties**

**一句话概括：** 把 ADMET 数据查询、性质预测和结构优化建议整合到一个平台，帮助寻找更合适的候选分子。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nucleic Acids Research 52(W1), W432–W438；2024-04-22 在线发表，2024 年 7 月卷期。 |
| 主要痛点 | 用户不仅需要性质预测，还需要查询相似化合物及寻找改善 ADMET 的结构修改方向。 |
| 数据集 | 超过 37 万条实验记录，涉及 104,652 个不同化合物、119 个 ADMET 端点。实验记录数与不同化合物数须分开。 |
| 方法 | 多任务图神经网络，结合数据库检索、相似性搜索及结构变换/骨架跃迁等优化功能。 |
| 结论 | 将探索、预测和优化整合到平台中；优化建议体现工具用途，不等于修改后的分子已经获得实验验证。 |

[论文原文](https://doi.org/10.1093/nar/gkae298) · [评测细节与局限](papers/admet/admetsar-3-2024.md)

### 数据与基准

#### TDC

**Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development**

**一句话概括：** 把药物发现中的多类数据和任务整理成统一接口与基准，让不同预测方法能够按共同规则比较。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | NeurIPS 2021 Datasets and Benchmarks Track。2022 年 Nature Chemical Biology 的相关论文是另一篇正式记录，不合并为同一次发表。 |
| 主要痛点 | 药物研究数据分散，任务接口、划分与评价缺乏统一，难以公平比较。 |
| 数据集 | 跨药物发现和开发任务的数据集合；本文聚焦其中 ADMET Benchmark Group 的 22 任务。会议论文整体覆盖范围大于 ADMET。 |
| 方法 | 建立任务定义、数据接口、标准化基准和公开榜单。 |
| 结论 | 为可比较的模型评价提供基础设施；TDC 本身不是一个可称作 SOTA 的预测模型。 |

[论文原文](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/3948ead63a9f2944218de038d8930b8f-Abstract-round2.html) · [评测细节与局限](papers/admet/tdc-2021.md)

#### PharmaBench

**PharmaBench: Enhancing ADMET benchmarks with large language models**

**一句话概括：** 用大语言模型辅助提取实验条件，再清洗和统一 ADMET 记录，构建条件更明确的评测数据集。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Scientific Data 11, 985；2024-09-10 |
| 主要痛点 | ADMET 数据中的测定条件和定义不统一，简单合并标签会损害基准质量。 |
| 数据集 | 从 14,401 个生物测定整合 156,618 条原始记录；经处理得到 52,482 条记录、11 个 ADMET 数据集。 |
| 方法 | 使用大语言模型辅助抽取测定信息，再进行结构、单位、重复项和实验条件的整理，提供建模划分。 |
| 结论 | 贡献是条件更明确的数据与基准建设；不是证明某个预测模型达到全面 SOTA。 |

[论文原文](https://www.nature.com/articles/s41597-024-03793-0) · [评测细节与局限](papers/admet/pharmabench-2024.md) · [代码/项目](https://github.com/mindrank-ai/PharmaBench)

### 观点文章

#### OpenADMET / Avoid-ome

**Mapping the avoid-ome: a systematic open-science approach to predictive ADMET**

**一句话概括：** 提出结合开放实验数据、蛋白质结构、主动学习和盲测挑战，从机制上改进 ADMET 预测的研究路线。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Nature Communications 17, 4644；2026-05-25；文章类型为 Perspective。 |
| 主要痛点 | 公开 ADMET 数据稀缺且测定不统一，结构层面的机制信息不足；传统模型难以给出可靠的结构优化依据。 |
| 数据集 | 讨论开放、机制导向的数据建设与实验计划，涉及 CYP、转运体、PXR、hERG 等；不是一个固定训练/测试表对应的新模型基准论文。 |
| 方法 | 将高通量化学、功能实验、结构生物学、主动学习和盲测挑战连接起来，研究影响 ADMET 的 anti-targets。 |
| 结论 | 提出通过系统开放数据与机制建模推进多参数药物设计的路线；文中倡议不能当作已完成的全面性能验证。 |

[论文原文](https://www.nature.com/articles/s41467-026-73410-8) · [评测细节与局限](papers/admet/openadmet-avoidome-2026.md) · [代码/项目](https://github.com/OpenADMET)

### 预印本

#### MapLight

**ADMET property prediction through combinations of molecular fingerprints**

**一句话概括：** 组合多种分子指纹和描述符，用 CatBoost 建立 ADMET 预测模型，检验传统特征方法的竞争力。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | arXiv 预印本，2023-09-29 首次提交；本次引用该版本，不填未经核实的正式期刊。 |
| 主要痛点 | 简单、计算成本较低的特征模型是否仍能与深度模型竞争？ |
| 数据集 | TDC ADMET 22 任务。 |
| 方法 | 组合 ECFP、Avalon、ErG 和分子描述符，使用 CatBoost；另有增加 GNN 表示的变体。 |
| 结论 | 组合指纹模型在多个 ADMET 端点表现强，是值得保留的基线；后续第三方审计报告也将 MapLight 两个版本列为通过其审计流程的方法。 |

[论文原文](https://arxiv.org/abs/2310.00174) · [评测细节与局限](papers/admet/maplight-2023.md) · [代码/项目](https://github.com/maplightrx/MapLight-TDC)

#### TDC模型审计

**Critical Assessment of ML models for ADMET Prediction in TDC leaderboards**

**一句话概括：** 检查 TDC 榜单领先模型能否运行、有无数据泄漏，以及报告的 ADMET 成绩能否复现。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | bioRxiv 预印本，2026 年；Crossref 发布日期为 2026-02-28，DOI 中含 02-26。此处不把 DOI 中日期直接当作发布日期。 |
| 主要痛点 | 排行榜领先成绩是否能复现，是否受到预训练泄漏、验证/测试重叠或环境问题影响？ |
| 数据集 | 从 TDC 22 任务的领先方法中选出 10 个方法进行审查；具体结论受其榜单快照与代码版本限制。 |
| 方法 | 分阶段检查环境可用性、预训练泄漏、验证/测试重叠和结果复现。 |
| 结论 | 作者报告仅 MapLight、MapLight+GNN 和 CaliciBoost 通过全部检查；其中 CaliciBoost 仅针对 Caco-2，并非覆盖全部 22 任务。 |

[论文原文](https://www.biorxiv.org/content/10.64898/2026.02.26.708193v1) · [评测细节与局限](papers/admet/tdc-audit-2026.md) · [代码/项目](https://github.com/receptor-ai/tdc-admet-bench)

#### Trimole-Hybrid

**A multimodal representation learning platform for accurate molecular ADMET prediction**

**一句话概括：** 融合分子序列、分子图、三维结构和化学先验，并按 ADMET 任务选择预测模型或集成方案。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | bioRxiv 预印本；Crossref 发布日期 2026-08-25，DOI 中含 08-24；仓库中的“under review”不等于正式录用。 |
| 主要痛点 | 单一分子表示不一定适合所有端点，如何结合互补模态并控制模型选择过程？ |
| 数据集 | TDC ADMET 22 任务。 |
| 方法 | 结合 SMILES、分子图、三维几何与化学先验，使用任务相关预测头和模型选择/集成。 |
| 结论 | 作者报告在所选公开榜单快照上 10/22 项超过首位成绩、21/22 项进入前十；属于待进一步独立确认的结果。 |

[论文原文](https://www.biorxiv.org/content/10.64898/2026.08.24.746660v1) · [评测细节与局限](papers/admet/trimole-hybrid-2026.md) · [代码/项目](https://github.com/dchen0212/trimole_hybrid)

#### ADMET-EvO

**ADMET-EvO: a self-evolving scientific agent for sustained research across heterogeneous tasks**

**一句话概括：** 让研究智能体针对不同 ADMET 任务探索特征和模型，并通过固定测试流程评价预测效果与研究效率。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | arXiv 预印本，2026-09-09 首次提交，2026-09-10 更新 v2。 |
| 主要痛点 | 不同端点需要不同特征、模型和优化过程，人工反复探索成本高；自动研究还需避免使用测试集指导选择。 |
| 数据集 | TDC ADMET 22 任务，另包含 43 个毒性任务。 |
| 方法 | 使用有证据门槛的研究智能体进行假设、特征与模型探索；论文描述冻结方案后进行留出测试评价及多随机种子验证。 |
| 结论 | 作者报告任务归一化综合得分 96.77，并在其指定比较和约束下减少累计模型拟合时间；这些数值需要按论文定义解读。 |

[论文原文](https://arxiv.org/abs/2609.10121) · [评测细节与局限](papers/admet/admet-evo-2026.md)

## 数据与维护

`data/papers.json` 是论文条目的维护入口。使用 Python 3.10 或更新版本，无第三方依赖：

```bash
python scripts/build.py
python scripts/build.py --check
```

第一条命令更新首页、专题总表、单篇解读及 CSV；第二条检查必填字段、重复记录、日期口径、URL 格式、内部链接和生成文件一致性。该检查不替代文献事实核验或外部链接在线检查。

## 参考与致谢

组织方式参考 [awesome-AIDD](https://github.com/daiyun02211/awesome-AIDD) 的主题导航、[Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) 的论文与代码索引。关注 [OpenADMET](https://github.com/OpenADMET) 的开放数据与评测实践。本仓库是独立的文献整理项目。

原创整理内容和维护脚本采用 [MIT License](LICENSE)。所引用论文、数据与第三方代码遵循各自的许可；本仓库提供链接与原创摘要，不分发论文全文。
