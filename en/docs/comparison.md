# Method comparisons

**English** | [简体中文](../../docs/comparison.md)

[Home](../../README.md) · [Dataset dictionary](datasets.md)

22 ADMET tasks, 128 results from selected catalog methods. Sources checked: **2026-09-22**. Each table groups results reported under the TDC scaffold protocol with 20% held out for testing. Each score links to its leaderboard record or original paper table.

Tables are sorted by mean performance: AUROC, AUPRC and Spearman ↑; MAE ↓. Values are mean ± standard deviation. Method names distinguish implementations such as Chemprop-RDKit and MapLight + GNN. Leaderboard scores describe those benchmark implementations; paper-table scores retain the authors’ experimental settings. Pretraining data and tuning budgets are described in the linked notes. The first row has the best mean among the methods collected here.

[TDC protocol](https://tdcommons.ai/benchmark/admet_group/overview/) · [CSV](../../data/comparison.csv)

## Find an endpoint

| Endpoint | Dataset | Metric | Methods |
| --- | --- | --- | --- |
| [Caco-2](#caco2_wang) | Caco2_Wang | MAE ↓ | 8 |
| [HIA](#hia_hou) | HIA_Hou | AUROC ↑ | 6 |
| [P-gp inhibition](#pgp_broccatelli) | Pgp_Broccatelli | AUROC ↑ | 6 |
| [Bioavailability](#bioavailability_ma) | Bioavailability_Ma | AUROC ↑ | 2 |
| [logD](#lipophilicity_astrazeneca) | Lipophilicity_AstraZeneca | MAE ↓ | 6 |
| [Solubility](#solubility_aqsoldb) | Solubility_AqSolDB | MAE ↓ | 6 |
| [BBB](#bbb_martins) | BBB_Martins | AUROC ↑ | 6 |
| [PPBR](#ppbr_az) | PPBR_AZ | MAE ↓ | 5 |
| [VDss](#vdss_lombardo) | VDss_Lombardo | Spearman ↑ | 6 |
| [CYP2C9 inhibition](#cyp2c9_veith) | CYP2C9_Veith | AUPRC ↑ | 6 |
| [CYP2D6 inhibition](#cyp2d6_veith) | CYP2D6_Veith | AUPRC ↑ | 6 |
| [CYP3A4 inhibition](#cyp3a4_veith) | CYP3A4_Veith | AUPRC ↑ | 6 |
| [CYP2C9 substrate](#cyp2c9_substrate_carbonmangels) | CYP2C9_Substrate_CarbonMangels | AUPRC ↑ | 6 |
| [CYP2D6 substrate](#cyp2d6_substrate_carbonmangels) | CYP2D6_Substrate_CarbonMangels | AUPRC ↑ | 6 |
| [CYP3A4 substrate](#cyp3a4_substrate_carbonmangels) | CYP3A4_Substrate_CarbonMangels | AUROC ↑ | 5 |
| [Half-life](#half_life_obach) | Half_Life_Obach | Spearman ↑ | 6 |
| [Hepatocyte clearance](#clearance_hepatocyte_az) | Clearance_Hepatocyte_AZ | Spearman ↑ | 6 |
| [Microsomal clearance](#clearance_microsome_az) | Clearance_Microsome_AZ | Spearman ↑ | 6 |
| [LD50](#ld50_zhu) | LD50_Zhu | MAE ↓ | 6 |
| [hERG blockade](#herg) | hERG | AUROC ↑ | 6 |
| [Mutagenicity](#ames) | AMES | AUROC ↑ | 6 |
| [Liver injury](#dili) | DILI | AUROC ↑ | 6 |

## Caco2_Wang

Caco-2 · 906 molecules · MAE ↓

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [CaliciBoost](../papers/admet/caliciboost-2025.md) | Published | 0.256 ± 0.006 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.276 ± 0.005 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.284 ± 0.009 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.287 ± 0.005 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [MolMapNet-D](../papers/foundations/molmapnet-2021.md) | Published | 0.287 ± 0.005 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.329 ± 0.008 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.330 ± 0.024 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.401 ± 0.032 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/01caco2/) |

## HIA_Hou

HIA · 578 molecules · AUROC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.989 ± 0.001 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.986 ± 0.000 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.984 ± 0.005 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.982 ± 0.004 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.981 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/02hia/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.974 ± 0.007 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/02hia/) |

## Pgp_Broccatelli

P-gp inhibition · 1,212 molecules · AUROC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.938 ± 0.004 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.938 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/03pgp/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.930 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/03pgp/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.930 ± 0.005 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.892 ± 0.012 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/03pgp/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.886 ± 0.016 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/03pgp/) |

## Bioavailability_Ma

Bioavailability · 640 molecules · AUROC ↑

This table uses KPGT Supplementary Table 8 and MolE Table 1. The TDC Bioavailability page repeats multiple P-gp entries with identical means and standard deviations; those leaderboard rows are excluded here.

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.750 ± 0.022 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.640 ± 0.046 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |

## Lipophilicity_AstraZeneca

logD · 4,200 molecules · MAE ↓

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.406 ± 0.009 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.446 ± 0.016 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.467 ± 0.006 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/05lipo/) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.525 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/05lipo/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.539 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/05lipo/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.572 ± 0.007 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/05lipo/) |

## Solubility_AqSolDB

Solubility · 9,982 molecules · MAE ↓

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.714 ± 0.011 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.761 ± 0.025 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.776 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.776 ± 0.019 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.789 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.792 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/06aqsol/) |

## BBB_Martins

BBB · 1,975 molecules · AUROC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.916 ± 0.001 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.913 ± 0.001 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.908 ± 0.005 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.903 ± 0.003 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.869 ± 0.027 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/07bbb/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.855 ± 0.011 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/07bbb/) |

## PPBR_AZ

PPBR · 1,797 molecules · MAE ↓

KPGT’s reported dataset size or metric differs for this task; see the [experimental details](../papers/admet/kpgt-2023.md).

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MolE](../papers/admet/mole-2024.md) | Published | 7.229 ± 0.168 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 7.526 ± 0.106 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/08ppbr/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 7.660 ± 0.058 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/08ppbr/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 8.288 ± 0.173 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/08ppbr/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 9.373 ± 0.335 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/08ppbr/) |

## VDss_Lombardo

VDss · 1,130 molecules · Spearman ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.713 ± 0.007 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.707 ± 0.009 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.644 ± 0.013 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.633 ± 0.016 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.389 ± 0.075 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/09vdss/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.241 ± 0.145 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/09vdss/) |

## CYP2C9_Veith

CYP2C9 inhibition · 12,092 molecules · AUPRC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.859 ± 0.001 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.797 ± 0.006 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.783 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.782 ± 0.001 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.777 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.749 ± 0.004 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/) |

## CYP2D6_Veith

CYP2D6 inhibition · 13,130 molecules · AUPRC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.790 ± 0.001 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.724 ± 0.008 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.723 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.679 ± 0.006 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.673 ± 0.007 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.646 ± 0.014 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/11cyp2d6i/) |

## CYP3A4_Veith

CYP3A4 inhibition · 12,328 molecules · AUPRC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.916 ± 0.000 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.894 ± 0.004 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.881 ± 0.001 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.876 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.876 ± 0.002 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.851 ± 0.006 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/12cyp3a4i/) |

## CYP2C9_Substrate_CarbonMangels

CYP2C9 substrate · 666 molecules · AUPRC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.450 ± 0.044 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.437 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/13cyp2c9s/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.415 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/13cyp2c9s/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.409 ± 0.014 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.400 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/13cyp2c9s/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.375 ± 0.032 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/13cyp2c9s/) |

## CYP2D6_Substrate_CarbonMangels

CYP2D6 substrate · 664 molecules · AUPRC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.737 ± 0.016 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.720 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/14cyp2d6s/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.713 ± 0.009 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/14cyp2d6s/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.692 ± 0.017 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.686 ± 0.031 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/14cyp2d6s/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.574 ± 0.030 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/14cyp2d6s/) |

## CYP3A4_Substrate_CarbonMangels

CYP3A4 substrate · 667 molecules · AUROC ↑

KPGT’s reported dataset size or metric differs for this task; see the [experimental details](../papers/admet/kpgt-2023.md).

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.692 ± 0.019 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.650 ± 0.006 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/15cyp3a4s/) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.647 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/15cyp3a4s/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.619 ± 0.030 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/15cyp3a4s/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.576 ± 0.025 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/15cyp3a4s/) |

## Half_Life_Obach

Half-life · 667 molecules · Spearman ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.578 ± 0.032 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.562 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/16halflife/) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.557 ± 0.034 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/16halflife/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.531 ± 0.030 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.239 ± 0.019 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/16halflife/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.085 ± 0.068 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/16halflife/) |

## Clearance_Hepatocyte_AZ

Hepatocyte clearance · 1,020 molecules · Spearman ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.498 ± 0.009 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.466 ± 0.012 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.456 ± 0.027 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.430 ± 0.021 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.424 ± 0.019 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.289 ± 0.022 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/17clhepa/) |

## Clearance_Microsome_AZ

Microsomal clearance · 1,102 molecules · Spearman ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.637 ± 0.010 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.632 ± 0.008 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.630 ± 0.010 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/18clmicro/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.626 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/18clmicro/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.599 ± 0.025 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/18clmicro/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.365 ± 0.055 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/18clmicro/) |

## LD50_Zhu

LD50 · 7,385 molecules · MAE ↓

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.545 ± 0.010 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.602 ± 0.016 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.621 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/19ld50/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.625 ± 0.022 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/19ld50/) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.633 ± 0.003 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/19ld50/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.678 ± 0.012 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/19ld50/) |

## hERG

hERG blockade · 648 molecules · AUROC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.880 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.871 ± 0.004 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.847 ± 0.024 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.840 ± 0.007 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/20herg/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.835 ± 0.018 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.825 ± 0.007 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/20herg/) |

## AMES

Mutagenicity · 7,255 molecules · AUROC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.869 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/21ames/) |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.868 ± 0.003 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.868 ± 0.002 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/21ames/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.850 ± 0.004 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/21ames/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.834 ± 0.015 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.814 ± 0.008 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/21ames/) |

## DILI

Liver injury · 475 molecules · AUROC ↑

| Method | Publication | Mean ± SD | Result source |
| --- | --- | --- | --- |
| [KPGT](../papers/admet/kpgt-2023.md) | Published | 0.929 ± 0.013 | [Supplementary Table 8](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-023-43214-1/MediaObjects/41467_2023_43214_MOESM1_ESM.pdf) |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.917 ± 0.005 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/22dili/) |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.887 ± 0.011 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/22dili/) |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.887 ± 0.006 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/22dili/) |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.886 ± 0.015 | [TDC leaderboard](https://tdcommons.ai/benchmark/admet_group/22dili/) |
| [MolE](../papers/admet/mole-2024.md) | Published | 0.852 ± 0.022 | [Table 1](https://www.nature.com/articles/s41467-024-53751-y/tables/1) |

## External validation and uncertainty

[PKSmart](../papers/admet/pksmart-2025.md) reports human PK on independent sources; [MC-PGP](../papers/admet/mc-pgp-2025.md) reports separate external inhibitor and substrate sets. [HERGAI](../papers/admet/hergai-2025.md) and [AmesNet](../papers/admet/amesnet-2026.md) define task-specific labels and test sets. Their notes include sample sizes, settings and results.

For confidence estimates, read [atom-based uncertainty](../papers/foundations/atom-uncertainty-2023.md) alongside [toxicity conformal prediction](../papers/admet/tox21-conformal-2021.md): calibration and interval/set coverage answer a different question from prediction accuracy.
