# Uni-QSAR

[English](../../en/papers/admet/uni-qsar-2023.md) | **简体中文**

**Uni-QSAR: an Auto-ML Tool for Molecular Property Prediction**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 自动组合分子指纹、描述符和一维至三维预训练表示，通过调参与堆叠集成完成多种 ADMET 性质预测。

分类：预印本。主题：AutoML、多模态表示、模型集成。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | arXiv:2304.12239，v1；2023-04-24 |
| 日期口径 | arXiv v1 提交日期 |
| 发表状态 | 🟠 **预印本** |
| 主要痛点 | 不同性质依赖不同分子特征，手动选择表示、模型和超参数成本高；偏态回归标签和分类不均衡进一步增加建模难度。 |
| 数据集 | TDC ADMET Benchmark Group 的 22 个任务：9 个回归、13 个分类；另做 CNS 穿透性案例，训练集 940 个化合物（315 个阳性、625 个阴性），外部测试集 117 个化合物。 |
| 方法 | 融合指纹、描述符、K-BERT 等一维表示、GROVER/MolCLR/KPGT 等二维表示与 Uni-Mol 三维表示；结合目标值变换、不均衡学习、贝叶斯超参数优化和两层堆叠集成，并用 dflow 并行执行。 |
| 结论 | 表 1–2 报告 Caco-2 MAE 0.273、BBBP AUROC 0.925；按表内 TDC 排名行统计，22 项中 17 项排名第一。CNS 案例 AUROC 为 0.980，消融实验支持三维表示、堆叠和目标值变换的贡献。 |

## 实验设置与结果分析

TDC 实验沿用文中所引基准报告的设置，与 Chemprop、DeepAutoQSAR 和 DeepPurpose 比较；部分基线成绩引用既有报告或榜单。正文没有逐任务列出划分和随机种子。表 1 回归任务有 8/9 项排名第一，表 2 分类任务有 9/13 项排名第一；这是论文发表时的表格记录。

摘要写“21/22 项达到 SOTA”，而表 1–2 的 TDC 排名行合计为 17/22 项第一。笔记采用结果表中的任务指标和排名计数；摘要与表格的统计口径未在文中解释。

## 代码与参考资料

[代码与项目](https://github.com/deepmodeling/unimol_tools)

公开的相关组件为 Uni-Mol Tools，提供 Uni-Mol 表示与性质预测功能；该入口不是论文完整的多表示堆叠流程。

资料核对：**2026-09-22**。已核对 arXiv v1 全文、表 1–2、CNS 案例和消融实验，并检查 Uni-Mol Tools README 的论文引用与功能说明。。

- [arXiv 版本记录](https://arxiv.org/abs/2304.12239)
- [v1 全文与结果表](https://arxiv.org/html/2304.12239v1)
- [相关组件 Uni-Mol Tools](https://github.com/deepmodeling/unimol_tools)
