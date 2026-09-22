# DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction

[English](../../en/papers/admet/dcpm-admet-2026.md) | **简体中文**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.zh-CN.md)

*Journal of Cheminformatics · 2026-06-20* · 已发表 · 核心论文

**内容概述：** 将两种预训练模型学到的分子表示与化学指纹结合，用于预测 97 项 ADMET 性质。

主题：综合ADMET、预训练、融合。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 18, 126；2026-06-20 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 单一分子表示难以同时覆盖语义、结构和理化信息；ADMET 标签稀疏且端点异质。 |
| 数据集 | 基于约 1.11 亿条 PubChem 数据预训练；ADMET 建模集合包含 97 个端点，43 个回归、54 个分类，共 465,470 条记录；另评估 10 个 MoleculeNet 数据集。数量按端点记录统计。 |
| 方法 | 融合 XLNet 语义表示、包含 SMILES→InChI 与性质学习的 GRU 组件，以及 ECFP 指纹；结合单任务随机森林、多任务神经网络和参数优化。 |
| 结论 | 相对 ECFP 对照，97 个端点中的 67 个改善（39 个分类、28 个回归）；平均分类 AUC 由 0.812 提高到 0.831，平均回归 Pearson r 由 0.661 提高到 0.701。 |

DOI：`10.1186/s13321-026-01244-z`

## 实验设置与结果分析

**实验设计。** Bemis–Murcko 骨架划分，训练/验证/测试为 8:1:1，独立运行 5 次。冻结预训练编码器，将 XLNet 的 512 维表示、RNN 的 512 维表示和 512 位 ECFP 拼接；单任务采用随机森林，多任务采用 DNN。TPE 执行 50 次超参数搜索，并比较冻结与全参数微调。

| 97 端点集合上的比较 | ECFP 对照 | DCPM-ADMET |
| --- | --- | --- |
| 54 个分类任务平均 AUC ↑ | 0.812 | 0.831 |
| 43 个回归任务平均 Pearson r ↑ | 0.661 | 0.701 |
| 优于 ECFP 的任务数 | — | 39/54 分类；28/43 回归 |

原文位置：Fine-tuning、ADMET prediction models；逐端点结果索引为 Supplementary Tables S6–S7。另有 10 个 MoleculeNet 数据集上的比较，不能与 97 端点汇总混为一组。

上述增益衡量融合表示相对本文 ECFP 基线的效果。平台 133 项输出由 97 个预测模型和 36 个计算属性组成；端点记录数不等于去重化合物数。

## 代码与参考资料

[代码与项目](https://github.com/zhangzhangleilei/DCPM-ADMET)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。已核对正文训练协议、97 端点汇总结果及补充表索引。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-026-01244-z)
- [作者代码](https://github.com/zhangzhangleilei/DCPM-ADMET)
