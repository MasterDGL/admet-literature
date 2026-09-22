# admetSAR3.0: a comprehensive platform for exploration, prediction and optimization of chemical ADMET properties

**English** | [简体中文](../../../papers/admet/admetsar-3-2024.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Nucleic Acids Research · 2024-04-22* · Published · Further reading

**Overview:** Integrates ADMET data search, property prediction and structural optimization suggestions to help identify suitable candidates.

Topics: ADMET, Platform, Structural optimization.

| Field | Details |
| --- | --- |
| Publication and date | Nucleic Acids Research 52(W1), W432–W438; online 2024-04-22; July 2024 issue. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Users need both property predictions and ways to find similar compounds and structural modifications that improve ADMET. |
| Datasets | More than 370,000 experimental records covering 104,652 distinct compounds and 119 ADMET endpoints. |
| Method | CLMGraph first uses QED-based molecular pairs from ten million small molecules for contrastive pretraining, followed by multi-task ADMET fine-tuning. The platform also integrates similarity search, scaffold hopping and matched-pair transformation rules. |
| Findings | Mean AUC across 90 classification endpoints is 0.870; over 82% of regression endpoints have Pearson r>0.70. Half-life and mean residence time perform less well. Experimental-data search and structure optimization complement prediction. |

DOI: `10.1093/nar/gkae298`

## Experimental setup and analysis

**Design.** Fivefold cross-validation and external validation; CLMGraph uses BCE for classification and MSE for regression. Pretraining constructs contrastive pairs using QED information from ten million molecules.

**Results.** Results presentation reports mean AUC 0.870 across 90 classification endpoints and Pearson r>0.70 for over 82% of regression endpoints. Renal-clearance classification, half-life and mean residence time perform less well. The main text does not itemize external-set sizes and scores; these averages are recorded as overall reported results, not as external-validation averages.

**Optimization.** ADMETopt2 extracts transformation rules for 21 endpoints. Its example connects suggestions to previously published structural modifications and measurements (Supplementary Text S1, Table S1). Table 1 mainly compares platform coverage, functionality and speed.

Endpoint model reports are needed to separate cross-validation and external results. The optimization example is retrospective, rather than experimental validation of every generated suggestion.

## Code and references

The web platform is freely accessible and ADMETopt2 transformation rules are downloadable from figshare; the paper does not link a full predictor training-code and weights repository

Sources reviewed: **2026-09-22**. Checked full-text Model building, Results presentation, the optimization example and data availability

- [Publisher paper](https://doi.org/10.1093/nar/gkae298)
- [Platform](http://lmmd.ecust.edu.cn/admetsar3/)
- [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223829/)
- [ADMETopt2 transformation rules](https://figshare.com/articles/dataset/ADMETopt2Transformation_Rules/25472317)
