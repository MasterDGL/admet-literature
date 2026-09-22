# 按方法汇总

[English](../en/docs/methods.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [按端点对比](comparison.md) · [数据集字典](datasets.md)

集中查看 **8 种实现**的输入表示、训练方式与任务覆盖。当前收录 **22 个 TDC 任务、128 条成绩**；横向汇总使用 **6 个方法共同覆盖的 19 个任务**。核对日期：**2026-09-22**。

[汇总 CSV](../data/method_summary.csv) · [逐任务排名 CSV](../data/method_task_ranks.csv)

## 输入表示与训练方式

| 方法实现 | 输入表示 | 训练方式 | 收录任务数 |
| --- | --- | --- | --- |
| [MolE](../papers/admet/mole-2024.md)<br>已发表 · [代码](https://github.com/recursionpharma/mole_public) | 分子图、原子环境与图中相对位置 | 解耦注意力 Transformer；自监督预训练、活性任务监督预训练、端点微调。 | 22/22 |
| [KPGT](../papers/admet/kpgt-2023.md)<br>已发表 · [代码](https://github.com/lihan97/KPGT) | 分子线图、分子指纹与理化描述符 | LiGhT Transformer；知识引导预训练与下游微调。 | 20/22 |
| [MapLight](../papers/admet/maplight-2023.md)<br>🟠 预印本 · [代码](https://github.com/maplightrx/MapLight-TDC) | ECFP、Avalon、ErG 指纹及理化描述符 | 组合固定分子特征，用 CatBoost 训练端点模型。 | 21/22 |
| [MapLight + GNN](../papers/admet/maplight-2023.md)<br>🟠 预印本 · [代码](https://github.com/maplightrx/MapLight-TDC) | MapLight 特征加预训练 GIN 表示 | 将 GIN 特征与分子指纹、描述符组合后输入 CatBoost。 | 21/22 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md)<br>已发表 · [代码](https://github.com/chemprop/chemprop) | 有向键分子图与 RDKit 描述符 | D-MPNN 聚合有向键消息，结合分子描述符预测端点。 | 21/22 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md)<br>已发表 · [代码](https://github.com/OpenDrugAI/AttentiveFP) | 原子与化学键构成的分子图 | 图注意力聚合原子邻域，并用注意力读出分子表示。 | 21/22 |
| [CaliciBoost](../papers/admet/caliciboost-2025.md)<br>已发表 · [代码](https://github.com/Calici/CaliciBoost) | 筛选后的 PaDEL 理化描述符 | 先比较分子表示与 AutoML 模型，再对 XGBoost 进行特征筛选和调参。 | 1/22 |
| [MolMapNet-D](../papers/foundations/molmapnet-2021.md)<br>已发表 · [代码](https://github.com/shenwanxiang/bidd-molmap) | 将分子描述符排列成二维特征图 | 卷积神经网络学习描述符特征图与端点之间的关系。 | 1/22 |

任务数表示本仓库已收录的成绩数量，论文中的完整实验范围见单篇笔记。代码链接指向论文项目；本表对应的提交实现见下文。

## 所收录结果的平均排名

19 个任务均使用同一组 6 种实现，按报告均值排名：MAE 越低越好，AUROC、AUPRC 和 Spearman 越高越好。相同均值取所占名次的平均值，各任务等权。**平均排名越低，整体名次越靠前。** Top-3 统计平均并列名次 ≤ 3 的任务数。

各来源报告采用 [TDC 骨架划分、20% 留出测试协议](https://tdcommons.ai/benchmark/admet_group/overview/)。这里汇总榜单提交与论文表格的结果；预训练数据和调参预算各异，本仓库未重新训练模型。排名反映这组已收录成绩的相对位置，均值与标准差本身不构成显著性检验。

| 方法 | 平均排名 ↓ | 共同任务数 | Top-3 任务数 | 逐任务名次范围 |
| --- | --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 2.13 | 19 | 16 | 1–5 |
| [KPGT](../papers/admet/kpgt-2023.md) | 2.26 | 19 | 15 | 1–5 |
| [MapLight](../papers/admet/maplight-2023.md) | 2.87 | 19 | 14 | 1–6 |
| [MolE](../papers/admet/mole-2024.md) | 3.50 | 19 | 7 | 1–6 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 4.47 | 19 | 2 | 2–6 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 5.76 | 19 | 0 | 3.5–6 |

## 共同任务的逐项排名

每列对应一种实现。点击端点可查看原始成绩及出处。

| 端点 | 指标 | MapLight + GNN | KPGT | MapLight | MolE | Chemprop-RDKit | AttentiveFP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Caco-2](comparison.md#caco2_wang) | MAE ↓ | 3 | 2 | 1 | 4 | 5 | 6 |
| [HIA](comparison.md#hia_hou) | AUROC ↑ | 1 | 4 | 2 | 3 | 5 | 6 |
| [P-gp inhibition](comparison.md#pgp_broccatelli) | AUROC ↑ | 1.5 | 1.5 | 3.5 | 3.5 | 6 | 5 |
| [logD](comparison.md#lipophilicity_astrazeneca) | MAE ↓ | 4 | 2 | 5 | 1 | 3 | 6 |
| [Solubility](comparison.md#solubility_aqsoldb) | MAE ↓ | 5 | 1 | 6 | 3.5 | 2 | 3.5 |
| [BBB](comparison.md#bbb_martins) | AUROC ↑ | 2 | 3 | 1 | 4 | 5 | 6 |
| [VDss](comparison.md#vdss_lombardo) | Spearman ↑ | 1 | 4 | 2 | 3 | 5 | 6 |
| [CYP2C9 inhibition](comparison.md#cyp2c9_veith) | AUPRC ↑ | 1 | 2 | 3 | 4 | 5 | 6 |
| [CYP2D6 inhibition](comparison.md#cyp2d6_veith) | AUPRC ↑ | 1 | 2 | 3 | 4 | 5 | 6 |
| [CYP3A4 inhibition](comparison.md#cyp3a4_veith) | AUPRC ↑ | 1 | 2 | 3 | 4.5 | 4.5 | 6 |
| [CYP2C9 substrate](comparison.md#cyp2c9_substrate_carbonmangels) | AUPRC ↑ | 2 | 1 | 3 | 4 | 5 | 6 |
| [CYP2D6 substrate](comparison.md#cyp2d6_substrate_carbonmangels) | AUPRC ↑ | 2 | 1 | 3 | 4 | 5 | 6 |
| [Half-life](comparison.md#half_life_obach) | Spearman ↑ | 3 | 4 | 2 | 1 | 5 | 6 |
| [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | Spearman ↑ | 1 | 5 | 2 | 3 | 4 | 6 |
| [Microsomal clearance](comparison.md#clearance_microsome_az) | Spearman ↑ | 3 | 1 | 4 | 2 | 5 | 6 |
| [LD50](comparison.md#ld50_zhu) | MAE ↓ | 5 | 1 | 3 | 2 | 4 | 6 |
| [hERG blockade](comparison.md#herg) | AUROC ↑ | 1 | 3 | 2 | 5 | 4 | 6 |
| [Mutagenicity](comparison.md#ames) | AUROC ↑ | 1 | 2.5 | 2.5 | 5 | 4 | 6 |
| [Liver injury](comparison.md#dili) | AUROC ↑ | 2 | 1 | 3.5 | 6 | 3.5 | 5 |

## 相对名次最好与最差的端点

按方法在固定参评组中的名次选择端点，保留全部并列项；各指标的原始数值分别展示，不跨指标比较大小。数值为原始均值 ± 标准差，点击数值查看出处。

### MapLight + GNN

| 相对位置 | 端点 | 名次 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- | --- |
| 最好 | [HIA](comparison.md#hia_hou) | 1 | AUROC | [0.989 ± 0.001](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| 最好 | [VDss](comparison.md#vdss_lombardo) | 1 | Spearman | [0.713 ± 0.007](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| 最好 | [CYP2C9 inhibition](comparison.md#cyp2c9_veith) | 1 | AUPRC | [0.859 ± 0.001](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| 最好 | [CYP2D6 inhibition](comparison.md#cyp2d6_veith) | 1 | AUPRC | [0.790 ± 0.001](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| 最好 | [CYP3A4 inhibition](comparison.md#cyp3a4_veith) | 1 | AUPRC | [0.916 ± 0.000](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| 最好 | [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | 1 | Spearman | [0.498 ± 0.009](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| 最好 | [hERG blockade](comparison.md#herg) | 1 | AUROC | [0.880 ± 0.002](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| 最好 | [Mutagenicity](comparison.md#ames) | 1 | AUROC | [0.869 ± 0.002](https://tdcommons.ai/benchmark/admet_group/21ames/) |
| 最差 | [Solubility](comparison.md#solubility_aqsoldb) | 5 | MAE | [0.789 ± 0.003](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| 最差 | [LD50](comparison.md#ld50_zhu) | 5 | MAE | [0.633 ± 0.003](https://tdcommons.ai/benchmark/admet_group/19ld50/) |

### KPGT

| 相对位置 | 端点 | 名次 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- | --- |
| 最好 | [Solubility](comparison.md#solubility_aqsoldb) | 1 | MAE | [0.714 ± 0.011](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| 最好 | [CYP2C9 substrate](comparison.md#cyp2c9_substrate_carbonmangels) | 1 | AUPRC | [0.450 ± 0.044](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| 最好 | [CYP2D6 substrate](comparison.md#cyp2d6_substrate_carbonmangels) | 1 | AUPRC | [0.737 ± 0.016](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| 最好 | [Microsomal clearance](comparison.md#clearance_microsome_az) | 1 | Spearman | [0.637 ± 0.010](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| 最好 | [LD50](comparison.md#ld50_zhu) | 1 | MAE | [0.545 ± 0.010](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| 最好 | [Liver injury](comparison.md#dili) | 1 | AUROC | [0.929 ± 0.013](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| 最差 | [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | 5 | Spearman | [0.424 ± 0.019](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |

### MapLight

| 相对位置 | 端点 | 名次 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- | --- |
| 最好 | [Caco-2](comparison.md#caco2_wang) | 1 | MAE | [0.276 ± 0.005](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| 最好 | [BBB](comparison.md#bbb_martins) | 1 | AUROC | [0.916 ± 0.001](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| 最差 | [Solubility](comparison.md#solubility_aqsoldb) | 6 | MAE | [0.792 ± 0.002](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |

### MolE

| 相对位置 | 端点 | 名次 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- | --- |
| 最好 | [logD](comparison.md#lipophilicity_astrazeneca) | 1 | MAE | [0.406 ± 0.009](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| 最好 | [Half-life](comparison.md#half_life_obach) | 1 | Spearman | [0.578 ± 0.032](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| 最差 | [Liver injury](comparison.md#dili) | 6 | AUROC | [0.852 ± 0.022](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |

### Chemprop-RDKit

| 相对位置 | 端点 | 名次 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- | --- |
| 最好 | [Solubility](comparison.md#solubility_aqsoldb) | 2 | MAE | [0.761 ± 0.025](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| 最差 | [P-gp inhibition](comparison.md#pgp_broccatelli) | 6 | AUROC | [0.886 ± 0.016](https://tdcommons.ai/benchmark/admet_group/03pgp/) |

### AttentiveFP

| 相对位置 | 端点 | 名次 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- | --- |
| 最好 | [Solubility](comparison.md#solubility_aqsoldb) | 3.5 | MAE | [0.776 ± 0.008](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| 最差 | [Caco-2](comparison.md#caco2_wang) | 6 | MAE | [0.401 ± 0.032](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| 最差 | [HIA](comparison.md#hia_hou) | 6 | AUROC | [0.974 ± 0.007](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| 最差 | [logD](comparison.md#lipophilicity_astrazeneca) | 6 | MAE | [0.572 ± 0.007](https://tdcommons.ai/benchmark/admet_group/05lipo/) |
| 最差 | [BBB](comparison.md#bbb_martins) | 6 | AUROC | [0.855 ± 0.011](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| 最差 | [VDss](comparison.md#vdss_lombardo) | 6 | Spearman | [0.241 ± 0.145](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| 最差 | [CYP2C9 inhibition](comparison.md#cyp2c9_veith) | 6 | AUPRC | [0.749 ± 0.004](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| 最差 | [CYP2D6 inhibition](comparison.md#cyp2d6_veith) | 6 | AUPRC | [0.646 ± 0.014](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| 最差 | [CYP3A4 inhibition](comparison.md#cyp3a4_veith) | 6 | AUPRC | [0.851 ± 0.006](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| 最差 | [CYP2C9 substrate](comparison.md#cyp2c9_substrate_carbonmangels) | 6 | AUPRC | [0.375 ± 0.032](https://tdcommons.ai/benchmark/admet_group/13cyp2c9s/) |
| 最差 | [CYP2D6 substrate](comparison.md#cyp2d6_substrate_carbonmangels) | 6 | AUPRC | [0.574 ± 0.030](https://tdcommons.ai/benchmark/admet_group/14cyp2d6s/) |
| 最差 | [Half-life](comparison.md#half_life_obach) | 6 | Spearman | [0.085 ± 0.068](https://tdcommons.ai/benchmark/admet_group/16halflife/) |
| 最差 | [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | 6 | Spearman | [0.289 ± 0.022](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| 最差 | [Microsomal clearance](comparison.md#clearance_microsome_az) | 6 | Spearman | [0.365 ± 0.055](https://tdcommons.ai/benchmark/admet_group/18clmicro/) |
| 最差 | [LD50](comparison.md#ld50_zhu) | 6 | MAE | [0.678 ± 0.012](https://tdcommons.ai/benchmark/admet_group/19ld50/) |
| 最差 | [hERG blockade](comparison.md#herg) | 6 | AUROC | [0.825 ± 0.007](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| 最差 | [Mutagenicity](comparison.md#ames) | 6 | AUROC | [0.814 ± 0.008](https://tdcommons.ai/benchmark/admet_group/21ames/) |

## 其他已收录成绩

以下任务保留在端点表中，本次共同任务汇总未纳入：

- [Bioavailability_Ma](comparison.md#bioavailability_ma): 榜单中多项均值与标准差和 P-gp 页面相同；相关记录未收录，六方法数据不完整。
- [PPBR_AZ](comparison.md#ppbr_az): KPGT 补充材料写为 1,614 个分子，TDC 为 1,797；该方法的这项成绩未纳入对比。
- [CYP3A4_Substrate_CarbonMangels](comparison.md#cyp3a4_substrate_carbonmangels): KPGT 补充表标为 AUPRC，TDC 使用 AUROC；该方法的这项成绩未纳入对比。

未进入固定参评组的方法保留各自成绩，综合平均排名记为 N/A。

| 方法 | 端点 | 指标 | 均值 ± 标准差 |
| --- | --- | --- | --- |
| [CaliciBoost](../papers/admet/caliciboost-2025.md) | [Caco-2](comparison.md#caco2_wang) | MAE | [0.256 ± 0.006](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [MolMapNet-D](../papers/foundations/molmapnet-2021.md) | [Caco-2](comparison.md#caco2_wang) | MAE | [0.287 ± 0.005](https://tdcommons.ai/benchmark/admet_group/01caco2/) |

## 实现设置与成绩来源

**[MolE](../papers/admet/mole-2024.md)** — 约 8.42 亿分子自监督预训练，再用 ChEMBL 活性数据训练；作者从两阶段训练数据中排除 TDC 测试分子。汇总采用 Table 1 的微调模型。 [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1)。

**[KPGT](../papers/admet/kpgt-2023.md)** — 约 200 万个 ChEMBL29 分子预训练；采用 Supplementary Table 8 的 TDC 实验。原文报告骨架 7:1:2 划分、五次运行。 [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf)。

**[MapLight](../papers/admet/maplight-2023.md)** — 使用作者的 TDC 榜单提交成绩；与增加 GNN 特征的变体分别统计。 [TDC 逐端点成绩](comparison.md)。

**[MapLight + GNN](../papers/admet/maplight-2023.md)** — 作者实现通过 molfeat 提取 GIN supervised-masking 特征；这是增加图表示的 CatBoost 变体。 [TDC 逐端点成绩](comparison.md)。

**[Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md)** — 采用名为 Chemprop-RDKit 的 TDC 提交；其成绩与原论文中的其他划分及 Chemprop 变体分别记录。 [TDC 逐端点成绩](comparison.md)。

**[AttentiveFP](../papers/foundations/attentivefp-2019.md)** — 采用 TDC 榜单中的 AttentiveFP 实现成绩；原论文的随机划分实验保留在论文笔记中。 [TDC 逐端点成绩](comparison.md)。

**[CaliciBoost](../papers/admet/caliciboost-2025.md)** — 榜单模型为 XGBoost 回归器；采用五个种子的 0.256±0.006，而非论文单次实验的 0.2525。 [TDC 逐端点成绩](comparison.md)。

**[MolMapNet-D](../papers/foundations/molmapnet-2021.md)** — D 为描述符分支；特征布局由大规模分子数据学习。这里只收录该实现的 Caco-2 榜单成绩。 [TDC 逐端点成绩](comparison.md)。

CSV 保留平均排名的完整精度及每条成绩的来源，未计算的汇总值留空。
