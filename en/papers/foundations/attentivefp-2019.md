# AttentiveFP

**English** | [简体中文](../../../papers/foundations/attentivefp-2019.md)

**Pushing the Boundaries of Molecular Representation for Drug Discovery with the Graph Attention Mechanism**

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

**In one sentence:** Learns which atoms and neighborhoods to emphasize when aggregating molecular information for property prediction and structural attribution.

Category: Foundational methods. Topics: Molecular graphs, Attention, Molecular representations.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Medicinal Chemistry 63(16), 8749–8760; online in 2019; issue date 2020-08-27. |
| Date basis | Online publication year; exact-date fields conflict, with issue date listed separately |
| Publication status | Journal article |
| Research problem | Representations must capture local and longer-range structural relationships while making model-selected chemical features easier to inspect. |
| Datasets | The authors' repository provides BBBP, HIV, BACE, ClinTox, SIDER, Tox21, ToxCast, ESOL (delaney), FreeSolv (SAMPL), Lipophilicity, QM9 and aromaticity examples, covering ADMET, activity, physicochemical and quantum-chemical tasks. |
| Method | Attention in molecular-graph message aggregation and graph-level readout produces learned fingerprints; attention visualization explores structural information. |
| Findings | Reports advanced performance at publication on the tested tasks and visual examples of learned nonlocal intramolecular relationships. |

DOI: `10.1021/acs.jmedchem.9b00959`

## Experimental setup and analysis

The data directory includes classification, regression and aromaticity examples. Comparisons require aligned splits and training configurations.

Attention visualizations show structures emphasized by the model. Online-date fields differ: Crossref/ACS page header gives 2019-08-13, while ACS history gives 2019-08-27; the catalog records the year.

## Code and references

[Code and project](https://github.com/OpenDrugAI/AttentiveFP)

Author code and accompanying data are accessible; rebuild the original Code Ocean environment following the reproduction instructions.

Sources reviewed: **2026-09-22**. Metadata and conflicting dates, original abstract, author implementation, data directory and REPRODUCING.md; dataset-level result tables have not been fully checked.

- [Published paper](https://doi.org/10.1021/acs.jmedchem.9b00959)
- [Bibliographic metadata](https://api.crossref.org/works/10.1021/acs.jmedchem.9b00959)
- [Author implementation](https://github.com/OpenDrugAI/AttentiveFP)
- [Author data directory](https://github.com/OpenDrugAI/AttentiveFP/tree/master/data)
