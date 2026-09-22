# Trimole-Hybrid

**English** | [简体中文](../../../papers/admet/trimole-hybrid-2026.md)

**A multimodal representation learning platform for accurate molecular ADMET prediction**

[ADMET and pharmacokinetics index](../../topics/admet.md) · [Home](../../../README.md)

**Overview:** Fuses sequences, molecular graphs, 3D structures and chemical priors, selecting prediction models or ensembles for each ADMET task.

Category: Preprints. Topics: Multimodal learning, Model ensembles.

| Field | Details |
| --- | --- |
| Publication and date | bioRxiv preprint; Crossref publication date 2026-08-25; the DOI contains 08-24. The author repository labels it under review. |
| Date basis | Crossref preprint publication date; DOI date recorded separately |
| Publication status | 🟠 **Preprint** |
| Research problem | A single representation may not suit all endpoints; complementary modalities must be combined with a controlled model-selection process. |
| Datasets | 22 TDC ADMET tasks. |
| Method | Combines SMILES, molecular graphs, 3D geometry and chemical priors with task-specific prediction heads, model selection and ensembles. |
| Findings | Reports scores above the top entry on 10/22 tasks and within the top ten on 21/22 tasks in the selected public leaderboard snapshot. |

DOI: `10.64898/2026.08.24.746660`

## Experimental setup and analysis

Evaluates multimodal combinations on 22 TDC tasks against the public leaderboard snapshot selected in the paper.

The repository provides implementation and review materials. Complete trained weights, official datasets and cached representations require separate preparation.

## Code and references

[Code and project](https://github.com/dchen0212/trimole_hybrid)

Implementation and review materials are public; complete trained weights, official datasets and cached representations are not included.

Sources reviewed: **2026-09-19**. Bibliographic metadata, abstract and accessible project documentation.

- [Preprint](https://www.biorxiv.org/content/10.64898/2026.08.24.746660v1)
- [Author code](https://github.com/dchen0212/trimole_hybrid)
