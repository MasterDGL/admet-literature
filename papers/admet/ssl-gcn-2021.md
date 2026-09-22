# Chemical toxicity prediction based on semi-supervised learning and graph convolutional neural network

[English](../../en/papers/admet/ssl-gcn-2021.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Cheminformatics · 2021-11-27* · 已发表 · 专题补读

**内容概述：** 让图神经网络同时学习有毒性标签和无标签的分子，利用半监督学习改善 Tox21 毒性预测。

主题：毒性、半监督学习、Tox21。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 13, 93；2021-11-27 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 毒性实验标签有限，大量分子只有结构信息；仅用有标签样本训练图网络，难以充分利用这些分子。 |
| 数据集 | Tox21：7,831 个分子、12 个毒性端点；另从 ClinTox、SIDER、ToxCast 和 HIV 收集分子，移除标签并去除与 Tox21 重复的结构，得到 50,527 个无标签分子。 |
| 方法 | 以 GCN 编码分子图，采用 Mean Teacher 框架：学生模型学习毒性标签，教师参数由学生参数的指数移动平均更新，并用扰动前后的预测一致性利用无标签数据。 |
| 结论 | 论文报告最佳平均 ROC-AUC 为 0.757，优于所比较传统机器学习模型约 0.71 的水平。无标签数据能够改善预测，但最佳加入比例随毒性端点变化。 |

DOI：`10.1186/s13321-021-00570-8`

## 实验设置与结果分析

Tox21 按分子骨架划分为训练/验证/测试集，比例为 80%/10%/10%，重复运行 5 次。比较监督式 SL-GCN、基于 ECFP4 的 KNN、神经网络、随机森林、SVM、XGBoost，以及 DeepChem 模型；测试无标签/有标签样本比例 0.5、1、2、3、4。

12 个端点的标签完整性和类别比例不同。阅读结果时应同时看各端点 AUROC 与无标签比例实验；增加无标签样本并非在所有端点上都持续提高成绩。

## 代码与参考资料

[代码与项目](https://github.com/chen709847237/SSL-GCN)

作者提供训练与预测脚本，README 链接数据和模型压缩包。

资料核对：**2026-09-22**。已核对出版社全文中的数据、骨架划分、Mean Teacher 方法和结果，以及作者仓库 README。。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-021-00570-8)
- [作者代码](https://github.com/chen709847237/SSL-GCN)
