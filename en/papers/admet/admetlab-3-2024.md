# ADMETlab 3.0: an updated comprehensive online ADMET prediction platform enhanced with broader coverage, improved performance, API functionality and decision support

**English** | [简体中文](../../../papers/admet/admetlab-3-2024.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Nucleic Acids Research · 2024-04-04* · Published · Further reading

**Overview:** Provides online ADMET and physicochemical predictions with uncertainty estimates, an API and decision-support tools.

Topics: ADMET, Platform, Uncertainty.

| Field | Details |
| --- | --- |
| Publication and date | Nucleic Acids Research 52(W1), W422–W431; online 2024-04-04; July 2024 issue. |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Limited property coverage, inconvenient access and point predictions alone constrain platform support for compound selection. |
| Datasets | Over 400,000 modeling records covering 77 learned endpoints (59 classification, 18 regression). The 119 platform outputs also include 34 directly computed endpoints and eight rules. Endpoint counts are detailed in Supplementary Table S1. |
| Method | Multitask directed message passing and descriptor-based modeling, combined with predictive uncertainty, API access and decision support. |
| Findings | Under common data and splits, the DMPNN models outperform MGA on 47/59 classification tasks. The platform combines 77 learned endpoints with calculated properties, rules, uncertainty estimates and an API. |

DOI: `10.1093/nar/gkae236`

## Experimental setup and analysis

**Design.** Each endpoint uses random 8:1:1 splits, repeated five times; Adam and Bayesian hyperparameter optimization train DMPNN and DMPNN-Des. MGA is retrained on the same data and splits. Classification uses AUC, ACC and MCC; regression uses R², RMSE and MAE.

**Results and locations.** The text reports that the DMPNN models outperform MGA on 47/59 classification tasks (Fig. 3). Supplementary Tables S4 and S5 contain classification and regression scores, respectively. LC50FM reaches R² 0.68; the new half-life regression endpoint reaches approximately 0.7. S6–S7 describe uncertainty strata and thresholds.

**Access.** Web and API services are provided. API users can choose DMPNN or DMPNN-Des and obtain predictions with confidence categories. Random-split evaluations are distinct from TDC scaffold benchmarks.

The 119 outputs include 77 learned endpoints. Coverage and speed inform tool selection; predictive accuracy is assessed for each endpoint and evaluation split.

## Code and references

Web service and API documentation are available; the paper does not link a public repository containing the complete training code and model weights

Sources reviewed: **2026-09-22**. Checked full-text model construction, Fig. 3, endpoint counts and references to Supplementary Tables S1–S7

- [Publisher paper](https://doi.org/10.1093/nar/gkae236)
- [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11223840/)
- [Web platform and API](https://admetlab3.scbdd.com/)
