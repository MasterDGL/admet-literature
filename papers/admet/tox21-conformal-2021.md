# Deep Learning-Based Conformal Prediction of Toxicity

[English](../../en/papers/admet/tox21-conformal-2021.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Chemical Information and Modeling · 2021-05-27* · 已发表 · 专题补读

**内容概述：** 给毒性模型加入共形预测，让用户按置信水平得到单一类别或多个候选类别，并评估漏检与不确定性。

主题：毒性、不确定性、共形预测。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Chemical Information and Modeling 61(6), 2648–2657；2021-05-27 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 单个毒性类别或概率难以直接说明预测可靠性，类别不均衡又容易导致模型漏检少数有毒分子。 |
| 数据集 | Tox21 挑战数据的 12 个核受体与应激反应端点；每个端点按活性/非活性单独建模，样本数见原文表 1。 |
| 方法 | 结合 DNN、GCN、GAT、其他图网络、随机森林和 LightGBM，使用独立校准集构建 Mondrian 共形预测器；比较有效性、单标签预测比例、平衡准确率与 MCC。 |
| 结论 | GCN 共形预测在 90% 置信水平下，对有毒类别的单标签预测比例超过 80%。多种基础模型的有毒分子召回增加，同时假阳性也增加。 |

DOI：`10.1021/acs.jcim.1c00208`

## 实验设置与结果分析

10 折分层交叉验证；每折训练部分先留出 10% 验证集，再从剩余部分划出 20% 校准集。比较不同显著性水平下的有效性和效率，并单独报告阳性与阴性类别。

覆盖保证依赖数据可交换性；单标签预测比例与正确率是不同指标。外推到新化学空间时，应另外检查校准后的实际覆盖率。

## 代码与参考资料

[代码与项目](https://github.com/FredrikSvenssonUK/tox21_conformal)

作者公开建模 Python 代码，论文给出 Tox21 数据入口。

资料核对：**2026-09-22**。已核对作者接受稿的数据、方法、实验与结论，以及出版社和 Crossref 日期；核对作者代码入口。。

- [出版社论文](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00208)
- [作者接受稿全文](https://discovery.ucl.ac.uk/id/eprint/10129421/3/Svensson_Zhang_etal_s2_r1.pdf)
- [作者代码](https://github.com/FredrikSvenssonUK/tox21_conformal)
