# Deep Learning-Based Conformal Prediction of Toxicity

**English** | [简体中文](../../../papers/admet/tox21-conformal-2021.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Journal of Chemical Information and Modeling · 2021-05-27* · Published · Further reading

**Overview:** Adds conformal prediction to toxicity models, returning one or multiple candidate labels at a chosen confidence level and assessing uncertainty and missed toxic compounds.

Topics: Toxicity, Uncertainty, Conformal prediction.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Chemical Information and Modeling 61(6), 2648–2657; 2021-05-27 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | A class label or score does not directly quantify prediction reliability, while class imbalance can cause toxic minority compounds to be missed. |
| Datasets | Twelve nuclear-receptor and stress-response endpoints from the Tox21 challenge, modeled as separate active/inactive tasks; endpoint sample counts appear in Table 1. |
| Method | Combines DNNs, GCN, GAT, other graph models, random forests and LightGBM with Mondrian conformal prediction using a held-out calibration set. Evaluates validity, single-label efficiency, balanced accuracy and MCC. |
| Findings | GCN-based conformal prediction achieves over 80% single-label efficiency for the toxic class at 90% confidence. Several underlying models retrieve more toxic compounds, with an accompanying increase in false positives. |

DOI: `10.1021/acs.jcim.1c00208`

## Experimental setup and analysis

Ten-fold stratified cross-validation; each fold reserves 10% of training data for validation and 20% of the remainder for calibration. Validity and efficiency are evaluated across significance levels and separately by class.

Coverage guarantees require exchangeability. Single-label efficiency is distinct from accuracy; application to new chemical spaces requires checking empirical calibrated coverage.

## Code and references

[Code and project](https://github.com/FredrikSvenssonUK/tox21_conformal)

The authors publish Python modeling code and identify the Tox21 data portal.

Sources reviewed: **2026-09-22**. Reviewed the accepted manuscript’s data, methods, results and conclusions; checked publisher/Crossref dates and the author code entry.

- [Publisher article](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00208)
- [Author accepted manuscript](https://discovery.ucl.ac.uk/id/eprint/10129421/3/Svensson_Zhang_etal_s2_r1.pdf)
- [Author code](https://github.com/FredrikSvenssonUK/tox21_conformal)
