# Pushing the Boundaries of Molecular Representation for Drug Discovery with the Graph Attention Mechanism

**English** | [简体中文](../../../papers/foundations/attentivefp-2019.md)

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

*Journal of Medicinal Chemistry · 2019* · Published · Foundational methods

**Overview:** Learns which atoms and neighborhoods to emphasize when aggregating molecular information for property prediction and structural attribution.

Topics: Molecular graphs, Attention, Molecular representations.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Medicinal Chemistry 63(16), 8749–8760; online in 2019; issue date 2020-08-27. |
| Date basis | Online publication year; exact-date fields conflict, with issue date listed separately |
| Publication status | Journal article |
| Research problem | Representations must capture local and longer-range structural relationships while making model-selected chemical features easier to inspect. |
| Datasets | Published Supplementary Tables 1/6 include BBBP 2,053; Tox21 8,014 (12 tasks); ToxCast 8,615 (617 tasks); SIDER 1,427 (27 tasks); ClinTox 1,491 (two tasks); ESOL 1,128; FreeSolv 643; and Lipophilicity 4,200 molecules, plus bioactivity and QM9 tasks. |
| Method | Attention in molecular-graph message aggregation and graph-level readout produces learned fingerprints; attention visualization explores structural information. |
| Findings | The published supplement reports BBBP AUROC 0.920±0.015, Tox21 AUROC 0.858±0.014 and ESOL RMSE 0.503±0.076. Atom-level and molecular-readout attention support structural visualization. |

DOI: `10.1021/acs.jmedchem.9b00959`

## Experimental setup and analysis

**Setup.** The author’s BBBP, Tox21 and ESOL notebooks randomly sample 10% for testing, then 1/9 of the remainder for validation, giving approximately 8:1:1 random splits. Supplementary Table 6 separates training, validation and test scores; the excerpts below use its Test column.

| Dataset | Molecules | Metric | Test |
| --- | --- | --- | --- |
| BBBP | 2,053 | AUROC ↑ | 0.920±0.015 |
| Tox21 | 8,014 | AUROC ↑ | 0.858±0.014 |
| SIDER | 1,427 | AUROC ↑ | 0.637±0.017 |
| ClinTox | 1,491 | AUROC ↑ | 0.940±0.018 |
| ESOL | 1,128 | RMSE ↓ | 0.503±0.076 |
| FreeSolv | 643 | RMSE ↓ | 0.736±0.037 |

These scores use the authors’ original data versions. Later TDC curation and scaffold evaluations are listed separately on the comparison page and are not pooled into the same ranking.

Attention visualizations show model emphasis rather than establish chemical causality. The ACS header/Crossref and publication history give different online dates, 2019-08-13 and 2019-08-27; the index retains the confirmed online year.

## Code and references

[Code and project](https://github.com/OpenDrugAI/AttentiveFP)

Author code and accompanying data are accessible; rebuild the original Code Ocean environment following the reproduction instructions.

Sources reviewed: **2026-09-22**. Checked published Supplementary Tables 1 and 6, author BBBP/Tox21/ESOL splitting code, and conflicting date fields

- [Published paper](https://doi.org/10.1021/acs.jmedchem.9b00959)
- [Bibliographic metadata](https://api.crossref.org/works/10.1021/acs.jmedchem.9b00959)
- [Author implementation](https://github.com/OpenDrugAI/AttentiveFP)
- [Author data directory](https://github.com/OpenDrugAI/AttentiveFP/tree/master/data)
- [Published supplement, Tables 1 and 6](https://acs.figshare.com/articles/journal_contribution/9733613)
- [Author BBBP experiment](https://github.com/OpenDrugAI/AttentiveFP/blob/master/code/2_Physiology_or_Toxicity_BBBP.ipynb)
