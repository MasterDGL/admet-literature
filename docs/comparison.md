# 方法对比

[English](../en/docs/comparison.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [数据集字典](datasets.md)

覆盖 6 类端点、已收录方法的 25 条结果，最近快照日期：**2026-09-22**。每张表对应一个 TDC 数据集、指标和骨架测试协议；均值和标准差取自榜单提交记录。

TDC 使用骨架划分并保留 20% 作为测试集。方法名区分 Chemprop-RDKit、MapLight + GNN 等具体实现。表中选取仓库已收录的方法；AUROC/AUPRC 越高越好，MAE 越低越好。

[TDC 评测协议](https://tdcommons.ai/benchmark/admet_group/overview/) · [CSV](../data/comparison.csv) · [交互表（下载后用浏览器打开）](comparison.html)

## Caco-2 — Caco2_Wang

906 个分子 · MAE ↓ · 2026-09-22 · [成绩来源](https://tdcommons.ai/benchmark/admet_group/01caco2/)

| 方法 | 发表状态 | 均值 ± 标准差 |
| --- | --- | --- |
| [CaliciBoost](../papers/admet/caliciboost-2025.md) | 已发表 | 0.256 ± 0.006 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.276 ± 0.005 |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.287 ± 0.005 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 已发表 | 0.330 ± 0.024 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 已发表 | 0.401 ± 0.032 |

## P-gp — Pgp_Broccatelli

1,212 个分子 · AUROC ↑ · 2026-09-22 · [成绩来源](https://tdcommons.ai/benchmark/admet_group/03pgp/)

| 方法 | 发表状态 | 均值 ± 标准差 |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.938 ± 0.002 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.930 ± 0.002 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 已发表 | 0.892 ± 0.012 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 已发表 | 0.886 ± 0.016 |

## BBB — BBB_Martins

1,975 个分子 · AUROC ↑ · 2026-09-22 · [成绩来源](https://tdcommons.ai/benchmark/admet_group/07bbb/)

| 方法 | 发表状态 | 均值 ± 标准差 |
| --- | --- | --- |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.916 ± 0.001 |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.913 ± 0.001 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 已发表 | 0.869 ± 0.027 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 已发表 | 0.855 ± 0.011 |

## CYP2C9 — CYP2C9_Veith

12,092 个分子 · AUPRC ↑ · 2026-09-22 · [成绩来源](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/)

| 方法 | 发表状态 | 均值 ± 标准差 |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.859 ± 0.001 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.783 ± 0.002 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 已发表 | 0.777 ± 0.003 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 已发表 | 0.749 ± 0.004 |

## hERG — hERG

648 个分子 · AUROC ↑ · 2026-09-22 · [成绩来源](https://tdcommons.ai/benchmark/admet_group/20herg/)

| 方法 | 发表状态 | 均值 ± 标准差 |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.880 ± 0.002 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.871 ± 0.004 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 已发表 | 0.840 ± 0.007 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 已发表 | 0.825 ± 0.007 |

## AMES — AMES

7,255 个分子 · AUROC ↑ · 2026-09-22 · [成绩来源](https://tdcommons.ai/benchmark/admet_group/21ames/)

| 方法 | 发表状态 | 均值 ± 标准差 |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.869 ± 0.002 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **预印本** | 0.868 ± 0.002 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 已发表 | 0.850 ± 0.004 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 已发表 | 0.814 ± 0.008 |

## 其他实验怎么比较

HERGAI 使用自行整理的 hERG 数据，MC-PGP 区分抑制剂和底物集，BBB MegaMolBART 使用 B3DB/CMUH，AmesNet 保留菌株/S9 条件。这些实验的测试集与标签不同，结果见各篇解读。Uni-QSAR 的表格成绩也保留在单篇笔记中，按其原文实验设置解读。
