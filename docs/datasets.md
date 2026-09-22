# 数据集字典

[English](../en/docs/datasets.md) | **简体中文**

[返回首页](../README.zh-CN.md) · [方法对比](comparison.md) · [CSV](../data/datasets.csv)

首版覆盖 TDC ADMET 的全部 22 个任务及 8 个常用 MoleculeNet 子集。规模对应表中基准版本，不代表数据库当前总量；论文自行整理的数据见各篇“数据集”字段。资料日期：**2026-09-22**。

TDC 页面同时出现“Not Specified”和 CC 链接时，许可记为“未明确”。MoleculeNet 汇集多个来源，标为“见原始提供方”的条目尚未单独录入数据许可。工具库的代码许可与数据许可分别记录。

## TDC ADMET Group

| 数据集 | 规模 | 端点数 | 任务 | 数据许可 | 获取方式 |
| --- | --- | --- | --- | --- | --- |
| [Caco2_Wang](https://tdcommons.ai/benchmark/admet_group/overview/) | 906 | 1 | Caco-2 | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Caco2_Wang')` |
| [HIA_Hou](https://tdcommons.ai/benchmark/admet_group/overview/) | 578 | 1 | HIA | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('HIA_Hou')` |
| [Pgp_Broccatelli](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,212 | 1 | P-gp inhibition | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Pgp_Broccatelli')` |
| [Bioavailability_Ma](https://tdcommons.ai/benchmark/admet_group/overview/) | 640 | 1 | Bioavailability | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Bioavailability_Ma')` |
| [Lipophilicity_AstraZeneca](https://tdcommons.ai/benchmark/admet_group/overview/) | 4,200 | 1 | logD | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Lipophilicity_AstraZeneca')` |
| [Solubility_AqSolDB](https://tdcommons.ai/benchmark/admet_group/overview/) | 9,982 | 1 | Solubility | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Solubility_AqSolDB')` |
| [BBB_Martins](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,975 | 1 | BBB | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('BBB_Martins')` |
| [PPBR_AZ](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,797 | 1 | PPBR | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('PPBR_AZ')` |
| [VDss_Lombardo](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,130 | 1 | VDss | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('VDss_Lombardo')` |
| [CYP2C9_Veith](https://tdcommons.ai/benchmark/admet_group/overview/) | 12,092 | 1 | CYP2C9 inhibition | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2C9_Veith')` |
| [CYP2D6_Veith](https://tdcommons.ai/benchmark/admet_group/overview/) | 13,130 | 1 | CYP2D6 inhibition | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2D6_Veith')` |
| [CYP3A4_Veith](https://tdcommons.ai/benchmark/admet_group/overview/) | 12,328 | 1 | CYP3A4 inhibition | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP3A4_Veith')` |
| [CYP2C9_Substrate_CarbonMangels](https://tdcommons.ai/benchmark/admet_group/overview/) | 666 | 1 | CYP2C9 substrate | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2C9_Substrate_CarbonMangels')` |
| [CYP2D6_Substrate_CarbonMangels](https://tdcommons.ai/benchmark/admet_group/overview/) | 664 | 1 | CYP2D6 substrate | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2D6_Substrate_CarbonMangels')` |
| [CYP3A4_Substrate_CarbonMangels](https://tdcommons.ai/benchmark/admet_group/overview/) | 667 | 1 | CYP3A4 substrate | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP3A4_Substrate_CarbonMangels')` |
| [Half_Life_Obach](https://tdcommons.ai/benchmark/admet_group/overview/) | 667 | 1 | Half-life | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Half_Life_Obach')` |
| [Clearance_Hepatocyte_AZ](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,020 | 1 | Hepatocyte clearance | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Clearance_Hepatocyte_AZ')` |
| [Clearance_Microsome_AZ](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,102 | 1 | Microsomal clearance | [未明确](https://tdcommons.ai/single_pred_tasks/adme/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Clearance_Microsome_AZ')` |
| [LD50_Zhu](https://tdcommons.ai/benchmark/admet_group/overview/) | 7,385 | 1 | LD50 | [未明确](https://tdcommons.ai/single_pred_tasks/tox/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('LD50_Zhu')` |
| [hERG](https://tdcommons.ai/benchmark/admet_group/overview/) | 648 | 1 | hERG blockade | [未明确](https://tdcommons.ai/single_pred_tasks/tox/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('hERG')` |
| [AMES](https://tdcommons.ai/benchmark/admet_group/overview/) | 7,255 | 1 | Mutagenicity | [未明确](https://tdcommons.ai/single_pred_tasks/tox/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('AMES')` |
| [DILI](https://tdcommons.ai/benchmark/admet_group/overview/) | 475 | 1 | Liver injury | [未明确](https://tdcommons.ai/single_pred_tasks/tox/) | [下载与加载说明](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('DILI')` |

## MoleculeNet

| 数据集 | 规模 | 端点数 | 任务 | 数据许可 | 获取方式 |
| --- | --- | --- | --- | --- | --- |
| [Tox21](https://doi.org/10.1039/C7SC02664A) | 7,831 | 12 | Toxicity | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#tox21-datasets)<br>`dc.molnet.load_tox21()` |
| [SIDER](https://doi.org/10.1039/C7SC02664A) | 1,427 | 27 | Adverse reactions | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#sider-datasets)<br>`dc.molnet.load_sider()` |
| [ClinTox](https://doi.org/10.1039/C7SC02664A) | 1,478 | 2 | Clinical toxicity / FDA approval | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#clintox-datasets)<br>`dc.molnet.load_clintox()` |
| [HIV](https://doi.org/10.1039/C7SC02664A) | 41,127 | 1 | HIV replication inhibition | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#hiv-datasets)<br>`dc.molnet.load_hiv()` |
| [BBBP](https://doi.org/10.1039/C7SC02664A) | 2,039 | 1 | BBB | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#bbbp-datasets)<br>`dc.molnet.load_bbbp()` |
| [ESOL](https://doi.org/10.1039/C7SC02664A) | 1,128 | 1 | Solubility | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#delaney-esol-datasets)<br>`dc.molnet.load_delaney()` |
| [FreeSolv](https://doi.org/10.1039/C7SC02664A) | 642 | 1 | Hydration free energy | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#freesolv-datasets)<br>`dc.molnet.load_freesolv()` |
| [Lipophilicity](https://doi.org/10.1039/C7SC02664A) | 4,200 | 1 | logD | [见原始提供方](https://doi.org/10.1039/C7SC02664A) | [下载与加载说明](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#lipo-datasets)<br>`dc.molnet.load_lipo()` |

## 加载基准划分

```python
from tdc.benchmark_group import admet_group
group = admet_group(path="data/")
benchmark = group.get("Caco2_Wang")
train_val, test = benchmark["train_val"], benchmark["test"]
```

方法对比使用 `benchmark_group` 的划分；单任务加载器的默认划分可能不同。BBBP（MoleculeNet，2,039）与 BBB_Martins（TDC，1,975）分别保留。HIV 测量抗病毒活性，在这里作为表示学习基准。
