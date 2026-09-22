# A hierarchical interaction message net for accurate molecular property prediction

**English** | [简体中文](../../../papers/admet/himnet-2026.md)

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

*Communications Chemistry · 2026-02-14* · Published · Further reading

**Overview:** Exchanges information across atoms, substructures and whole molecules in a hierarchical graph network for property and selected ADMET predictions.

Topics: Hierarchical GNN, Metabolic stability.

| Field | Details |
| --- | --- |
| Publication and date | Communications Chemistry 9, 150; 2026-02-14 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Limited interaction across atom, substructure and molecular levels can leave property-relevant information out of single-level representations. |
| Datasets | 11 datasets: 8 MoleculeNet subsets plus Malaria, LMC and MetStab. BBBP, Tox21, SIDER, ClinTox and metabolic-stability tasks directly concern ADMET; others assess broader properties or bioactivity. |
| Method | Hierarchical message passing and attention combine directed message paths, cross-level interactions and consistency information from multiple fingerprints. |
| Findings | Reported BBBP AUROC is 0.954±0.020, ESOL RMSE 0.710±0.016, and metabolic-stability AUROC 0.896±0.008. Ablations probe the task-dependent contributions of hierarchical message passing and fusion modules. |

DOI: `10.1038/s42004-026-01922-x`

## Experimental setup and analysis

**Design.** Eleven datasets use 8:1:1 scaffold splits. The text describes three independent splits and ten initializations per split; the ablation discussion separately describes three-run summaries. Adam runs for 100 epochs, with batch size 64, learning rate 0.0001 and hidden size 512 (Table 5). Metrics are AUROC and RMSE.

| Task | HimNet | Comparator | Location |
| --- | --- | --- | --- |
| BBBP, AUROC ↑ | 0.954±0.020 | FH-GNN 0.949±0.016 | Table 1 |
| ESOL, RMSE ↓ | 0.710±0.016 | FH-GNN 0.904±0.070 | Table 1 |
| MetStab, AUROC ↑ | 0.896±0.008 | FH-GNN 0.876±0.014 | Table 2 |
| Multi-species LMC, mean RMSE ↓ | 111.0±9.8 | HiMol 117.085±10.1 | Table 2 |

Table 1 reruns FH-GNN; other baseline scores are taken from their original publications, so their original evaluation settings also affect the comparison.

Descriptions of run aggregation differ between sections; reproduction should follow the specific table and released implementation. LMC covers human, rat and mouse clearance, and its RMSE is on that dataset’s scale.

## Code and references

[Code and project](https://github.com/Hugh415/HimNet)

Author code and data are public under MIT, with an additional Zenodo archive

Sources reviewed: **2026-09-22**. Checked experiment descriptions, Tables 1–2 and 5–6, and code/data availability statements

- [Publisher full text](https://www.nature.com/articles/s42004-026-01922-x)
- [Author code and data](https://github.com/Hugh415/HimNet)
- [Code archive](https://doi.org/10.5281/zenodo.18030100)
- [Model comparison, Table 1](https://www.nature.com/articles/s42004-026-01922-x/tables/1)
