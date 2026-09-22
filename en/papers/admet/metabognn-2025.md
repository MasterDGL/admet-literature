# MetaboGNN: predicting liver metabolic stability with graph neural networks and cross-species data

**English** | [简体中文](../../../papers/admet/metabognn-2025.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Cheminformatics · 2025-09-03* · Published · Further reading

**Overview:** Combines graph contrastive pretraining with human–mouse metabolic differences to predict the parent fraction remaining after 30 minutes in liver microsomes.

Topics: Metabolic stability, Cross-species, Graph contrastive learning.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Cheminformatics 17, 140; published online 2025-09-03. |
| Date basis | Publisher online publication date. |
| Publication status | Journal article |
| Research problem | Limited stability labels require representations that capture both molecular structure and species-dependent metabolism. |
| Datasets | The 2023 South Korea drug-discovery challenge: 3,981 compounds, with fixed training/test sets of 3,498/483 and paired human/mouse microsomal remaining percentages. Pretraining uses about 2.58 million unlabeled molecules. |
| Method | Contrastively pretrains molecular graphs with ring information, then predicts mouse stability and the human–mouse difference jointly to derive human stability. |
| Findings | Adding the species-difference task reduces HLM/MLM RMSE from 30.14/28.72 to 27.91/27.86 percentage points on this dataset. |

DOI: `10.1186/s13321-025-01089-y`

## Experimental setup and analysis

**Design.** The challenge uses structural clustering followed by stratified splitting within clusters. Author code randomly holds out another 20% of training data for validation. The paper reports 30 independent runs; parentheses are 95% confidence intervals.

| Setting | HLM RMSE ↓ | MLM RMSE ↓ |
| --- | --- | --- |
| From scratch | 30.94 (30.52–31.35) | 29.48 (29.29–29.67) |
| Contrastive pretraining | 30.14 (29.89–30.39) | 28.72 (28.55–28.88) |
| Pretraining + species-difference task | 27.91 (27.76–28.06) | 27.86 (27.69–28.03) |

Source: Tables 1–2. RMSE is in percentage points of parent compound remaining. Inference predicts both species from structure.

Testing uses the same challenge collection with within-cluster splitting. Microsomal remaining-fraction errors do not establish human clearance or clinical half-life accuracy.

## Code and references

[Code and project](https://github.com/qwon135/MetaboGNN)

Training, inference, pretraining scripts and train/test CSVs are public; the validation split was checked in code.

Sources reviewed: **2026-09-22**. Checked the full text, dataset and species-difference task, Tables 1–3, and training code; models were not retrained.

- [Full text, methods and Tables 1–3](https://pmc.ncbi.nlm.nih.gov/articles/PMC12409945/)
- [Author implementation and data](https://github.com/qwon135/MetaboGNN)
- [Author training and validation split](https://github.com/qwon135/MetaboGNN/blob/main/train.py)
- [Challenge dataset](https://dacon.io/competitions/official/236127/overview/description)
