# Domain-aware / pBRICS

[English](../../en/papers/admet/domain-aware-pbrics-2023.md) | **简体中文**

**Domain-aware representation of small molecules for explainable property prediction models**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**一句话概括：** 按化学官能团对分子进行片段化，让图模型在预测 ADMET 性质时指出哪些片段影响结果。

分类：专题补读。主题：片段表示、可解释性、多任务学习。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | ICLR 2023 Machine Learning for Drug Discovery (MLDD) Workshop；2023 |
| 日期口径 | 会议官方录用目录所列年份 |
| 发表状态 | 会议 Workshop 论文 |
| 主要痛点 | 原子级重要性难以直接对应药物化学中的官能团和结构改造；通用分子切分又可能破坏有解释意义的化学片段。 |
| 数据集 | 从 ADMETlab 2.0 数据整理的 23 个分类端点，覆盖 Ames、致癌性、CYP、眼部与呼吸毒性、BBBP 和 Tox21；另用 ChEMBL 分子分析片段化效果，以 BBBP 的 102 对匹配分子对（110 个独立分子）等案例检查解释。 |
| 方法 | pBRICS 在 BRICS 切分后结合官能团规则整理骨架和取代基，使用 MACCS 与 ECFP2 片段指纹构建片段图；比较单任务和多任务 GCN/RGCN，通过 Grad-CAM 给片段赋予重要性，并分析匹配分子对。 |
| 结论 | 表 2 中，多任务片段 RGCN 在 23 个端点上的平均 AUROC 为 84.47%，高于用 ADMETlab 2.0 源码训练的对照模型 83.35%，提升 1.12 个百分点；片段解释展示了官能团变化与 BBBP、Ames 预测的联系。 |

## 实验设置与结果分析

训练/验证/测试比例为 80%/10%/10%，正文未指明随机或骨架划分。表 2 比较 MT-FraGCN、MT-FraRGCN、ST-FraGCN 和 ADMETlab 2.0 对照；第 3.3–3.4 节分析 BBBP 与 Ames 匹配分子对。

匹配分子对分析发现，骨架相关性有时会主导预测，局部片段解释合理的分子仍可能分类错误。同团队相关期刊研究 pBRICS（10.1021/acs.jcim.3c00689）扩展到 40 个性质；本条的 23 任务与 84.47% 结果对应 Workshop 版本。

## 代码与参考资料

论文及会议目录未提供配套代码链接。

资料核对：**2026-09-22**。已核对会议官方录用记录及其链接的 13 页 PDF，包括片段表示、数据划分、表 2 和匹配分子对分析；另核对相关期刊研究的书目信息与任务数。。

- [会议官方录用目录](https://sites.google.com/view/mldd-2023/accepted-papers_1)
- [会议目录链接的论文全文](https://drive.google.com/file/d/102YpAC8_5EapFnaoJE1CCwjFgOP_I45U/view)
- [OpenReview 论文入口](https://openreview.net/forum?id=C9WW17wQF7p)
- [相关 pBRICS 期刊研究](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.3c00689)
