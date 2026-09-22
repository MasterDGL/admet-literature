# Dataset dictionary

**English** | [简体中文](../../docs/datasets.md)

[Home](../../README.md) · [Comparisons](comparison.md) · [CSV](../../data/datasets.csv)

The first edition covers all 22 TDC ADMET benchmarks and eight commonly used MoleculeNet subsets. Counts refer to those named benchmark releases, rather than current database totals. Paper-specific curated datasets are described in each paper’s dataset field. Reviewed: **2026-09-22**.

TDC pages with “Not Specified” are recorded as unspecified even when a CC link appears beside the text. MoleculeNet aggregates data from multiple providers; entries marked “See original provider” do not yet have a separately recorded data license. Library code licenses and data licenses are separate.

## TDC ADMET Group

| Dataset | Size | Endpoints | Task | Data license | Access |
| --- | --- | --- | --- | --- | --- |
| [Caco2_Wang](https://tdcommons.ai/benchmark/admet_group/overview/) | 906 | 1 | Caco-2 | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Caco2_Wang')` |
| [HIA_Hou](https://tdcommons.ai/benchmark/admet_group/overview/) | 578 | 1 | HIA | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('HIA_Hou')` |
| [Pgp_Broccatelli](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,212 | 1 | P-gp inhibition | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Pgp_Broccatelli')` |
| [Bioavailability_Ma](https://tdcommons.ai/benchmark/admet_group/overview/) | 640 | 1 | Bioavailability | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Bioavailability_Ma')` |
| [Lipophilicity_AstraZeneca](https://tdcommons.ai/benchmark/admet_group/overview/) | 4,200 | 1 | logD | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Lipophilicity_AstraZeneca')` |
| [Solubility_AqSolDB](https://tdcommons.ai/benchmark/admet_group/overview/) | 9,982 | 1 | Solubility | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Solubility_AqSolDB')` |
| [BBB_Martins](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,975 | 1 | BBB | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('BBB_Martins')` |
| [PPBR_AZ](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,797 | 1 | PPBR | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('PPBR_AZ')` |
| [VDss_Lombardo](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,130 | 1 | VDss | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('VDss_Lombardo')` |
| [CYP2C9_Veith](https://tdcommons.ai/benchmark/admet_group/overview/) | 12,092 | 1 | CYP2C9 inhibition | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2C9_Veith')` |
| [CYP2D6_Veith](https://tdcommons.ai/benchmark/admet_group/overview/) | 13,130 | 1 | CYP2D6 inhibition | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2D6_Veith')` |
| [CYP3A4_Veith](https://tdcommons.ai/benchmark/admet_group/overview/) | 12,328 | 1 | CYP3A4 inhibition | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP3A4_Veith')` |
| [CYP2C9_Substrate_CarbonMangels](https://tdcommons.ai/benchmark/admet_group/overview/) | 666 | 1 | CYP2C9 substrate | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2C9_Substrate_CarbonMangels')` |
| [CYP2D6_Substrate_CarbonMangels](https://tdcommons.ai/benchmark/admet_group/overview/) | 664 | 1 | CYP2D6 substrate | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP2D6_Substrate_CarbonMangels')` |
| [CYP3A4_Substrate_CarbonMangels](https://tdcommons.ai/benchmark/admet_group/overview/) | 667 | 1 | CYP3A4 substrate | [CC BY 4.0](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('CYP3A4_Substrate_CarbonMangels')` |
| [Half_Life_Obach](https://tdcommons.ai/benchmark/admet_group/overview/) | 667 | 1 | Half-life | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Half_Life_Obach')` |
| [Clearance_Hepatocyte_AZ](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,020 | 1 | Hepatocyte clearance | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Clearance_Hepatocyte_AZ')` |
| [Clearance_Microsome_AZ](https://tdcommons.ai/benchmark/admet_group/overview/) | 1,102 | 1 | Microsomal clearance | [Not specified](https://tdcommons.ai/single_pred_tasks/adme/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/adme/)<br>`admet_group().get('Clearance_Microsome_AZ')` |
| [LD50_Zhu](https://tdcommons.ai/benchmark/admet_group/overview/) | 7,385 | 1 | LD50 | [Not specified](https://tdcommons.ai/single_pred_tasks/tox/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('LD50_Zhu')` |
| [hERG](https://tdcommons.ai/benchmark/admet_group/overview/) | 648 | 1 | hERG blockade | [Not specified](https://tdcommons.ai/single_pred_tasks/tox/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('hERG')` |
| [AMES](https://tdcommons.ai/benchmark/admet_group/overview/) | 7,255 | 1 | Mutagenicity | [Not specified](https://tdcommons.ai/single_pred_tasks/tox/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('AMES')` |
| [DILI](https://tdcommons.ai/benchmark/admet_group/overview/) | 475 | 1 | Liver injury | [Not specified](https://tdcommons.ai/single_pred_tasks/tox/) | [Download / loader](https://tdcommons.ai/single_pred_tasks/tox/)<br>`admet_group().get('DILI')` |

## MoleculeNet

| Dataset | Size | Endpoints | Task | Data license | Access |
| --- | --- | --- | --- | --- | --- |
| [Tox21](https://doi.org/10.1039/C7SC02664A) | 7,831 | 12 | Toxicity | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#tox21-datasets)<br>`dc.molnet.load_tox21()` |
| [SIDER](https://doi.org/10.1039/C7SC02664A) | 1,427 | 27 | Adverse reactions | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#sider-datasets)<br>`dc.molnet.load_sider()` |
| [ClinTox](https://doi.org/10.1039/C7SC02664A) | 1,478 | 2 | Clinical toxicity / FDA approval | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#clintox-datasets)<br>`dc.molnet.load_clintox()` |
| [HIV](https://doi.org/10.1039/C7SC02664A) | 41,127 | 1 | HIV replication inhibition | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#hiv-datasets)<br>`dc.molnet.load_hiv()` |
| [BBBP](https://doi.org/10.1039/C7SC02664A) | 2,039 | 1 | BBB | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#bbbp-datasets)<br>`dc.molnet.load_bbbp()` |
| [ESOL](https://doi.org/10.1039/C7SC02664A) | 1,128 | 1 | Solubility | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#delaney-esol-datasets)<br>`dc.molnet.load_delaney()` |
| [FreeSolv](https://doi.org/10.1039/C7SC02664A) | 642 | 1 | Hydration free energy | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#freesolv-datasets)<br>`dc.molnet.load_freesolv()` |
| [Lipophilicity](https://doi.org/10.1039/C7SC02664A) | 4,200 | 1 | logD | [See original provider](https://doi.org/10.1039/C7SC02664A) | [Download / loader](https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html#lipo-datasets)<br>`dc.molnet.load_lipo()` |

## Loading the benchmark splits

```python
from tdc.benchmark_group import admet_group
group = admet_group(path="data/")
benchmark = group.get("Caco2_Wang")
train_val, test = benchmark["train_val"], benchmark["test"]
```

Use `benchmark_group` for the comparison protocol; calling a single-task loader with its defaults can produce a different split. BBBP (MoleculeNet, 2,039) and BBB_Martins (TDC, 1,975) retain distinct entries. HIV measures antiviral activity and is included as a representation-learning benchmark.
