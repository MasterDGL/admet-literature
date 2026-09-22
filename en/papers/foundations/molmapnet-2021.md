# Out-of-the-box deep learning prediction of pharmaceutical properties by broadly learned knowledge-based molecular representations

**English** | [简体中文](../../../papers/foundations/molmapnet-2021.md)

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

*Nature Machine Intelligence · 2021-03-01* · Published · Foundational methods

**Overview:** Arranges descriptors and fingerprints into 2D feature maps and trains CNNs to predict physicochemical, pharmacokinetic and toxicity-related properties.

Topics: Descriptors, Fingerprints, CNN, Baselines.

| Field | Details |
| --- | --- |
| Publication and date | Nature Machine Intelligence 3, 334–343; 2021-03-01 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Descriptor vectors leave feature relationships underused, while task-specific tuning adds modeling cost. |
| Datasets | Twenty-six pharmaceutical benchmarks and a new test set. Feature relationships are learned from 8,506,205 molecules. ADMET-related sets include CYP450 (16,896 compounds, five enzymes), liver microsomal clearance across human, mouse and rat (8,755 compounds), BBBP, ESOL, Tox21, SIDER and ClinTox (Supplementary Table S9). |
| Method | MolMap embeds 1,456 descriptors and 16,204 fingerprint features into 2D grids. CNN variants use descriptors (D), fingerprints (F), or both (B), with default and optimized settings. |
| Findings | Feature maps provide useful property predictors. In Supplementary Table S5, tuning improves MolMapNet-B ESOL RMSE from 0.575 to 0.544 in one setting and from 0.543 to 0.512 in another; AttentiveFP scores 0.486 in the latter setting. |

DOI: `10.1038/s42256-021-00301-6`

## Experimental setup and analysis

**Splits (Supplementary Table S9).** CYP450: assay IDs; LMC: random; BBBP: scaffold; ESOL/Tox21/SIDER/ClinTox: random.

| ESOL setting (Supplementary Table S5) | MolMapNet-B default | Optimized | Comparator RMSE |
| --- | --- | --- | --- |
| MoleculeNet/Chemprop setting | 0.575 | 0.544 | Chemprop 0.555 |
| AttentiveFP setting | 0.543 | 0.512 | AttentiveFP 0.486 |

**Later TDC submission.** MolMapNet-D achieves Caco2_Wang MAE 0.287 ± 0.005 on the leaderboard. This descriptor-only implementation is recorded separately from the dual-input models above.

Included as a foundation for combining chemical descriptors with deep learning. The feature-layout corpus and downstream supervised datasets serve different training roles.

## Code and references

[Code and project](https://github.com/shenwanxiang/bidd-molmap)

Author code and training examples are public; ChemBench v0 provides data and split indices.

Sources reviewed: **2026-09-22**. Checked Crossref, publisher abstract, official Supplementary Tables S5/S9, author code and the TDC submission; visually inspected the S5 PDF page

- [Publisher abstract and publication metadata](https://www.nature.com/articles/s42256-021-00301-6)
- [Official supplement: Tables S5 and S9](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42256-021-00301-6/MediaObjects/42256_2021_301_MOESM1_ESM.pdf)
- [Author code and examples](https://github.com/shenwanxiang/bidd-molmap)
- [Paper data and split version](https://github.com/shenwanxiang/ChemBench/tree/v0)
- [TDC Caco-2 submission](https://tdcommons.ai/benchmark/admet_group/01caco2/)
