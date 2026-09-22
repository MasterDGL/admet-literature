# Methods at a glance

**English** | [简体中文](../../docs/methods.md)

[Home](../../README.md) · [Endpoint comparisons](comparison.md) · [Dataset dictionary](datasets.md)

Compare the inputs, learning strategies and task coverage of **8 implementations**. The catalog contains **128 scores across 22 TDC tasks**; the fixed-cohort summary uses **6 methods on 19 shared tasks**. Reviewed: **2026-09-22**.

[Summary CSV](../../data/method_summary.csv) · [Task ranks CSV](../../data/method_task_ranks.csv)

## Representations and learning strategies

| Implementation | Input | Learning strategy | Collected tasks |
| --- | --- | --- | --- |
| [MolE](../papers/admet/mole-2024.md)<br>Published · [Code](https://github.com/recursionpharma/mole_public) | Molecular graphs, atom environments and relative graph positions | Disentangled-attention Transformer; self-supervised pretraining, activity-supervised pretraining and endpoint fine-tuning. | 22/22 |
| [KPGT](../papers/admet/kpgt-2023.md)<br>Published · [Code](https://github.com/lihan97/KPGT) | Molecular line graphs, fingerprints and physicochemical descriptors | LiGhT Transformer with knowledge-guided pretraining and downstream fine-tuning. | 20/22 |
| [MapLight](../papers/admet/maplight-2023.md)<br>🟠 Preprint · [Code](https://github.com/maplightrx/MapLight-TDC) | ECFP, Avalon and ErG fingerprints plus physicochemical descriptors | CatBoost endpoint models trained on combined molecular features. | 21/22 |
| [MapLight + GNN](../papers/admet/maplight-2023.md)<br>🟠 Preprint · [Code](https://github.com/maplightrx/MapLight-TDC) | MapLight features plus pretrained GIN representations | CatBoost using GIN features together with fingerprints and descriptors. | 21/22 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md)<br>Published · [Code](https://github.com/chemprop/chemprop) | Directed-bond molecular graphs and RDKit descriptors | D-MPNN aggregates directed-bond messages and combines them with molecular descriptors. | 21/22 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md)<br>Published · [Code](https://github.com/OpenDrugAI/AttentiveFP) | Molecular graphs with atom and bond features | Graph attention aggregates atomic neighborhoods and reads out a molecular representation. | 21/22 |
| [CaliciBoost](../papers/admet/caliciboost-2025.md)<br>Published · [Code](https://github.com/Calici/CaliciBoost) | Selected PaDEL physicochemical descriptors | Representation and AutoML screening followed by feature selection and XGBoost tuning. | 1/22 |
| [MolMapNet-D](../papers/foundations/molmapnet-2021.md)<br>Published · [Code](https://github.com/shenwanxiang/bidd-molmap) | Molecular descriptors arranged into two-dimensional feature maps | A convolutional neural network predicts endpoints from descriptor maps. | 1/22 |

Coverage counts scores collected in this repository, not the total number of tasks studied by the authors. Code links lead to the paper projects; submission-specific settings are described below.

## Mean rank of collected results

Each of the 19 tasks compares the same 6 implementations, using reported means: MAE lower is better; AUROC, AUPRC and Spearman higher is better. Equal reported means receive the average of their occupied ranks. All tasks have equal weight. **Lower mean rank is better.** Top-3 counts tasks with an assigned rank ≤ 3, including ties under that rule.

The sources report the [TDC scaffold protocol with 20% held-out test data](https://tdcommons.ai/benchmark/admet_group/overview/). This is a descriptive aggregation of leaderboard submissions and paper tables. Pretraining data and tuning budgets differ, and this repository has not rerun the models. Rankings describe this fixed set of collected results; mean ± SD alone does not establish statistical significance.

| Method | Mean rank ↓ | Shared tasks | Top-3 tasks | Task-rank range |
| --- | --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 2.13 | 19 | 16 | 1–5 |
| [KPGT](../papers/admet/kpgt-2023.md) | 2.26 | 19 | 15 | 1–5 |
| [MapLight](../papers/admet/maplight-2023.md) | 2.87 | 19 | 14 | 1–6 |
| [MolE](../papers/admet/mole-2024.md) | 3.50 | 19 | 7 | 1–6 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | 4.47 | 19 | 2 | 2–6 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | 5.76 | 19 | 0 | 3.5–6 |

## Rank on each shared task

Each column is one implementation. Follow an endpoint to see its original scores and sources.

| Endpoint | Metric | MapLight + GNN | KPGT | MapLight | MolE | Chemprop-RDKit | AttentiveFP |
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

## Highest and lowest relative ranks

Endpoints are selected by each method’s rank among the fixed competitors, not by comparing raw scores across metrics. All ties are listed. Values are the original mean ± SD; each value links to its source.

### MapLight + GNN

| Relative position | Endpoint | Rank | Metric | Mean ± SD |
| --- | --- | --- | --- | --- |
| Highest | [HIA](comparison.md#hia_hou) | 1 | AUROC | [0.989 ± 0.001](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| Highest | [VDss](comparison.md#vdss_lombardo) | 1 | Spearman | [0.713 ± 0.007](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| Highest | [CYP2C9 inhibition](comparison.md#cyp2c9_veith) | 1 | AUPRC | [0.859 ± 0.001](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| Highest | [CYP2D6 inhibition](comparison.md#cyp2d6_veith) | 1 | AUPRC | [0.790 ± 0.001](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| Highest | [CYP3A4 inhibition](comparison.md#cyp3a4_veith) | 1 | AUPRC | [0.916 ± 0.000](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| Highest | [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | 1 | Spearman | [0.498 ± 0.009](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| Highest | [hERG blockade](comparison.md#herg) | 1 | AUROC | [0.880 ± 0.002](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| Highest | [Mutagenicity](comparison.md#ames) | 1 | AUROC | [0.869 ± 0.002](https://tdcommons.ai/benchmark/admet_group/21ames/) |
| Lowest | [Solubility](comparison.md#solubility_aqsoldb) | 5 | MAE | [0.789 ± 0.003](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| Lowest | [LD50](comparison.md#ld50_zhu) | 5 | MAE | [0.633 ± 0.003](https://tdcommons.ai/benchmark/admet_group/19ld50/) |

### KPGT

| Relative position | Endpoint | Rank | Metric | Mean ± SD |
| --- | --- | --- | --- | --- |
| Highest | [Solubility](comparison.md#solubility_aqsoldb) | 1 | MAE | [0.714 ± 0.011](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| Highest | [CYP2C9 substrate](comparison.md#cyp2c9_substrate_carbonmangels) | 1 | AUPRC | [0.450 ± 0.044](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| Highest | [CYP2D6 substrate](comparison.md#cyp2d6_substrate_carbonmangels) | 1 | AUPRC | [0.737 ± 0.016](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| Highest | [Microsomal clearance](comparison.md#clearance_microsome_az) | 1 | Spearman | [0.637 ± 0.010](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| Highest | [LD50](comparison.md#ld50_zhu) | 1 | MAE | [0.545 ± 0.010](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| Highest | [Liver injury](comparison.md#dili) | 1 | AUROC | [0.929 ± 0.013](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| Lowest | [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | 5 | Spearman | [0.424 ± 0.019](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |

### MapLight

| Relative position | Endpoint | Rank | Metric | Mean ± SD |
| --- | --- | --- | --- | --- |
| Highest | [Caco-2](comparison.md#caco2_wang) | 1 | MAE | [0.276 ± 0.005](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| Highest | [BBB](comparison.md#bbb_martins) | 1 | AUROC | [0.916 ± 0.001](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| Lowest | [Solubility](comparison.md#solubility_aqsoldb) | 6 | MAE | [0.792 ± 0.002](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |

### MolE

| Relative position | Endpoint | Rank | Metric | Mean ± SD |
| --- | --- | --- | --- | --- |
| Highest | [logD](comparison.md#lipophilicity_astrazeneca) | 1 | MAE | [0.406 ± 0.009](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| Highest | [Half-life](comparison.md#half_life_obach) | 1 | Spearman | [0.578 ± 0.032](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| Lowest | [Liver injury](comparison.md#dili) | 6 | AUROC | [0.852 ± 0.022](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |

### Chemprop-RDKit

| Relative position | Endpoint | Rank | Metric | Mean ± SD |
| --- | --- | --- | --- | --- |
| Highest | [Solubility](comparison.md#solubility_aqsoldb) | 2 | MAE | [0.761 ± 0.025](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| Lowest | [P-gp inhibition](comparison.md#pgp_broccatelli) | 6 | AUROC | [0.886 ± 0.016](https://tdcommons.ai/benchmark/admet_group/03pgp/) |

### AttentiveFP

| Relative position | Endpoint | Rank | Metric | Mean ± SD |
| --- | --- | --- | --- | --- |
| Highest | [Solubility](comparison.md#solubility_aqsoldb) | 3.5 | MAE | [0.776 ± 0.008](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| Lowest | [Caco-2](comparison.md#caco2_wang) | 6 | MAE | [0.401 ± 0.032](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| Lowest | [HIA](comparison.md#hia_hou) | 6 | AUROC | [0.974 ± 0.007](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| Lowest | [logD](comparison.md#lipophilicity_astrazeneca) | 6 | MAE | [0.572 ± 0.007](https://tdcommons.ai/benchmark/admet_group/05lipo/) |
| Lowest | [BBB](comparison.md#bbb_martins) | 6 | AUROC | [0.855 ± 0.011](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| Lowest | [VDss](comparison.md#vdss_lombardo) | 6 | Spearman | [0.241 ± 0.145](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| Lowest | [CYP2C9 inhibition](comparison.md#cyp2c9_veith) | 6 | AUPRC | [0.749 ± 0.004](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| Lowest | [CYP2D6 inhibition](comparison.md#cyp2d6_veith) | 6 | AUPRC | [0.646 ± 0.014](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| Lowest | [CYP3A4 inhibition](comparison.md#cyp3a4_veith) | 6 | AUPRC | [0.851 ± 0.006](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| Lowest | [CYP2C9 substrate](comparison.md#cyp2c9_substrate_carbonmangels) | 6 | AUPRC | [0.375 ± 0.032](https://tdcommons.ai/benchmark/admet_group/13cyp2c9s/) |
| Lowest | [CYP2D6 substrate](comparison.md#cyp2d6_substrate_carbonmangels) | 6 | AUPRC | [0.574 ± 0.030](https://tdcommons.ai/benchmark/admet_group/14cyp2d6s/) |
| Lowest | [Half-life](comparison.md#half_life_obach) | 6 | Spearman | [0.085 ± 0.068](https://tdcommons.ai/benchmark/admet_group/16halflife/) |
| Lowest | [Hepatocyte clearance](comparison.md#clearance_hepatocyte_az) | 6 | Spearman | [0.289 ± 0.022](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| Lowest | [Microsomal clearance](comparison.md#clearance_microsome_az) | 6 | Spearman | [0.365 ± 0.055](https://tdcommons.ai/benchmark/admet_group/18clmicro/) |
| Lowest | [LD50](comparison.md#ld50_zhu) | 6 | MAE | [0.678 ± 0.012](https://tdcommons.ai/benchmark/admet_group/19ld50/) |
| Lowest | [hERG blockade](comparison.md#herg) | 6 | AUROC | [0.825 ± 0.007](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| Lowest | [Mutagenicity](comparison.md#ames) | 6 | AUROC | [0.814 ± 0.008](https://tdcommons.ai/benchmark/admet_group/21ames/) |

## Other collected results

The following tasks remain in the endpoint tables but are outside this fixed cohort:

- [Bioavailability_Ma](comparison.md#bioavailability_ma): Several leaderboard means and standard deviations repeat P-gp entries. Those rows are excluded, leaving incomplete coverage for the six methods.
- [PPBR_AZ](comparison.md#ppbr_az): KPGT lists 1,614 molecules, versus 1,797 in TDC; its result is excluded from the comparison.
- [CYP3A4_Substrate_CarbonMangels](comparison.md#cyp3a4_substrate_carbonmangels): KPGT labels the metric AUPRC, while TDC uses AUROC; its result is excluded from the comparison.

Methods outside the fixed cohort retain their collected scores below; their overall mean rank is N/A.

| Method | Endpoint | Metric | Mean ± SD |
| --- | --- | --- | --- |
| [CaliciBoost](../papers/admet/caliciboost-2025.md) | [Caco-2](comparison.md#caco2_wang) | MAE | [0.256 ± 0.006](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [MolMapNet-D](../papers/foundations/molmapnet-2021.md) | [Caco-2](comparison.md#caco2_wang) | MAE | [0.287 ± 0.005](https://tdcommons.ai/benchmark/admet_group/01caco2/) |

## Implementation and result sources

**[MolE](../papers/admet/mole-2024.md)** — Self-supervised pretraining on about 842 million molecules, followed by ChEMBL activity training. The authors remove TDC test molecules from both training stages. Results use the fine-tuned model in Table 1. [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1).

**[KPGT](../papers/admet/kpgt-2023.md)** — Pretrained on about two million ChEMBL29 molecules. Results use the TDC experiments in Supplementary Table 8, reported with a 7:1:2 scaffold split and five runs. [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf).

**[MapLight](../papers/admet/maplight-2023.md)** — Uses the authors' TDC leaderboard submission, tracked separately from the variant with GNN features. [TDC endpoint tables](comparison.md).

**[MapLight + GNN](../papers/admet/maplight-2023.md)** — The authors' implementation obtains GIN supervised-masking features through molfeat. This is the CatBoost variant augmented with graph representations. [TDC endpoint tables](comparison.md).

**[Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md)** — Uses the TDC submission named Chemprop-RDKit, distinct from other splits and Chemprop variants in the original paper. [TDC endpoint tables](comparison.md).

**[AttentiveFP](../papers/foundations/attentivefp-2019.md)** — Uses the AttentiveFP implementation on the TDC leaderboard. Original-paper random-split experiments remain in the paper note. [TDC endpoint tables](comparison.md).

**[CaliciBoost](../papers/admet/caliciboost-2025.md)** — The submitted model is an XGBoost regressor. The score is 0.256±0.006 over five seeds; the paper's single-run 0.2525 is a separate result. [TDC endpoint tables](comparison.md).

**[MolMapNet-D](../papers/foundations/molmapnet-2021.md)** — D denotes the descriptor branch; feature layout is learned from a large molecular collection. This catalog currently records its Caco-2 leaderboard result. [TDC endpoint tables](comparison.md).

The CSV exports preserve full precision for mean ranks and include original provenance for every ranked score. Missing aggregate values are blank in CSV.
