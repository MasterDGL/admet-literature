# DCPM-ADMET

**DCPM-ADMET: fusion of dual-component pre-trained model and molecular fingerprints to enhance drug ADMET properties prediction**

[返回ADMET 与药代动力学总表](../../topics/admet.md) · [返回首页](../../README.md)

**一句话概括：** 将两种预训练模型学到的分子表示与化学指纹结合，用于预测 97 项 ADMET 性质。

分类：核心论文。主题：综合ADMET、预训练、融合。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Cheminformatics 18, 126；2026-06-20 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 单一分子表示难以同时覆盖语义、结构和理化信息；ADMET 标签稀疏且端点异质。 |
| 数据集 | 基于约 1.11 亿条 PubChem 数据预训练；ADMET 建模集合包含 97 个端点，43 个回归、54 个分类，共 465,470 条记录；另评估 10 个 MoleculeNet 数据集。记录数不等于去重后的分子数。 |
| 方法 | 融合 XLNet 语义表示、包含 SMILES→InChI 与性质学习的 GRU 组件，以及 ECFP 指纹；结合单任务随机森林、多任务神经网络和参数优化。 |
| 结论 | 论文报告在 67/97 个端点优于 ECFP 对照；在所比较的 10 个 MoleculeNet 任务中，5 个取得最佳结果。 |

DOI：`10.1186/s13321-026-01244-z`

## 评测与结论适用范围

采用骨架划分及模型/特征对照；67/97 指相对于 ECFP 对照，不是 67 个任务的公开榜单首位。

重点看数据构建、融合消融及外部比较。67/97 是相对于论文的 ECFP 对照，不能改写为“67 个任务达到全球 SOTA”。平台的 133 项输出包括 97 项模型预测与 36 项计算属性，也不能写成 133 个独立训练任务。

## 代码与证据

[代码或项目入口](https://github.com/zhangzhangleilei/DCPM-ADMET)

代码状态：存在作者代码/项目入口；未独立验证安装、权重及实验复现。复现状态：本仓库未独立复现实验。

内容核验日期：**2026-09-19**。核对范围：书目、正文关键部分及相关官方资源。

- [出版社全文](https://link.springer.com/article/10.1186/s13321-026-01244-z)
- [作者代码](https://github.com/zhangzhangleilei/DCPM-ADMET)
