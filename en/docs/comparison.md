# Method comparisons

**English** | [简体中文](../../docs/comparison.md)

[Home](../../README.md) · [Dataset dictionary](datasets.md)

6 endpoint families, 25 results from selected catalog methods. Latest snapshot: **2026-09-22**. Each table uses one TDC dataset, metric and scaffold-test protocol. Scores and standard deviations are reported leaderboard submissions, not independent reruns.

TDC holds out 20% for testing and uses scaffold splits. The method names identify specific implementations, including Chemprop-RDKit and MapLight + GNN. This selection compares catalog methods rather than reproducing the complete leaderboard. AUROC and AUPRC increase with performance; MAE decreases.

[TDC protocol](https://tdcommons.ai/benchmark/admet_group/overview/) · [CSV](../../data/comparison.csv) · [Interactive table (download and open in a browser)](../../docs/comparison.html)

## Caco-2 — Caco2_Wang

906 molecules · MAE ↓ · 2026-09-22 · [Scores](https://tdcommons.ai/benchmark/admet_group/01caco2/)

| Method | Publication | Mean ± SD |
| --- | --- | --- |
| [CaliciBoost](../papers/admet/caliciboost-2025.md) | Published | 0.256 ± 0.006 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.276 ± 0.005 |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.287 ± 0.005 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.330 ± 0.024 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.401 ± 0.032 |

## P-gp — Pgp_Broccatelli

1,212 molecules · AUROC ↑ · 2026-09-22 · [Scores](https://tdcommons.ai/benchmark/admet_group/03pgp/)

| Method | Publication | Mean ± SD |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.938 ± 0.002 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.930 ± 0.002 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.892 ± 0.012 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.886 ± 0.016 |

## BBB — BBB_Martins

1,975 molecules · AUROC ↑ · 2026-09-22 · [Scores](https://tdcommons.ai/benchmark/admet_group/07bbb/)

| Method | Publication | Mean ± SD |
| --- | --- | --- |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.916 ± 0.001 |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.913 ± 0.001 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.869 ± 0.027 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.855 ± 0.011 |

## CYP2C9 — CYP2C9_Veith

12,092 molecules · AUPRC ↑ · 2026-09-22 · [Scores](https://tdcommons.ai/benchmark/admet_group/10cyp2c9i/)

| Method | Publication | Mean ± SD |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.859 ± 0.001 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.783 ± 0.002 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.777 ± 0.003 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.749 ± 0.004 |

## hERG — hERG

648 molecules · AUROC ↑ · 2026-09-22 · [Scores](https://tdcommons.ai/benchmark/admet_group/20herg/)

| Method | Publication | Mean ± SD |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.880 ± 0.002 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.871 ± 0.004 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.840 ± 0.007 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.825 ± 0.007 |

## AMES — AMES

7,255 molecules · AUROC ↑ · 2026-09-22 · [Scores](https://tdcommons.ai/benchmark/admet_group/21ames/)

| Method | Publication | Mean ± SD |
| --- | --- | --- |
| [MapLight + GNN](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.869 ± 0.002 |
| [MapLight](../papers/admet/maplight-2023.md) | 🟠 **Preprint** | 0.868 ± 0.002 |
| [Chemprop-RDKit](../papers/foundations/chemprop-dmpnn-2019.md) | Published | 0.850 ± 0.004 |
| [AttentiveFP](../papers/foundations/attentivefp-2019.md) | Published | 0.814 ± 0.008 |

## Reading other experiments

HERGAI uses its own curated hERG data; MC-PGP uses separate inhibitor and substrate sets; BBB MegaMolBART uses B3DB/CMUH; AmesNet models strain/S9 conditions. Their results remain in the individual notes because the test sets and labels differ from these TDC benchmarks. Uni-QSAR table values are retained in its paper notes, with the paper’s own evaluation context.
