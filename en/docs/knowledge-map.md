# AIDD knowledge map and reading routes

**English** | [简体中文](../../docs/knowledge-map.md)

[Home](../../README.md) · [ADMET index](../topics/admet.md) · [Methods and benchmarks](../topics/foundations.md)

![Five-level AIDD knowledge map](../../assets/aidd-knowledge-pyramid.en.svg)

The map organizes AIDD into five reading levels: understand the data and research questions, learn molecular representations and prediction methods, then connect them to molecular design and experimental validation. Each level provides research questions and reading entry points.

## What each level addresses

| Level, from bottom to top | Questions to explore | Current coverage and reading |
| --- | --- | --- |
| Data and research questions | What is predicted? Which experiments produce the labels? How are training and testing separated? | [MoleculeNet](../papers/foundations/moleculenet-2018.md), [TDC](../papers/admet/tdc-2021.md), [PharmaBench](../papers/admet/pharmabench-2024.md); [MoleculeACE](../papers/foundations/moleculeace-2022.md) examines activity cliffs |
| Molecular and protein representations | How do structures, sequences, conformations and context become model inputs? | [Chemprop/D-MPNN](../papers/foundations/chemprop-dmpnn-2019.md), [AttentiveFP](../papers/foundations/attentivefp-2019.md), [KPGT](../papers/admet/kpgt-2023.md); protein representations and structure are planned topics |
| Prediction tasks | Is a molecule active? Can it reach the intended site? What safety risks does it present? | [ADMET and PK](../topics/admet.md) is the current focus, covering toxicity, absorption/distribution, metabolism and PK; binding, docking and virtual screening are planned |
| Design and optimization | How can candidates balance activity, ADMET and synthetic accessibility? | Planned topics: molecular generation, multiparameter optimization, reaction prediction and synthesis planning |
| Experimental validation and iteration | Do new experiments support predictions? How do results guide the next study? | [BBB MegaMolBART](../papers/admet/bbb-megamolbart-2024.md) provides an in vitro example; full design–make–test–analyze cycles are planned |

ADMET sits in the prediction layer and supplies absorption, distribution, metabolism, excretion and toxicity constraints for design. Design proposes candidates, experiments test predictions, and new data improve models. The feedback arrow represents this research cycle.

Benchmarks, error analysis, uncertainty and reproducibility span the entire workflow. MoleculeACE uses bioactivity cliffs to examine prediction challenges among similar molecules, so it belongs to foundational evaluation.

## Where to start

The five-level map connects areas of research. The [five thematic reading routes](reading-routes.md) start from concrete questions, with a suggested sequence, comparison questions and papers listed from newest to oldest.

| Your question | Reading route | Map levels |
| --- | --- | --- |
| Can a molecule be absorbed, enter the brain or interact with transporters? | [Absorption and distribution](../topics/absorption-distribution.md) | Data, prediction, validation |
| How is a molecule metabolized, and can human exposure-related parameters be predicted? | [Metabolism and pharmacokinetics](../topics/metabolism-pk.md) | Data, prediction |
| Are there hERG, mutagenicity or other safety risks? | [Toxicity prediction](../topics/toxicity.md) | Data, prediction |
| What do fingerprints, descriptors, molecular graphs and pretraining contribute? | [Representations and learning](../topics/representations-learning.md) | Representations, prediction |
| When can predictions be trusted, and how can errors and experiments test them? | [Reliability and validation](../topics/reliability-validation.md) | Across all levels |

For a first pass, read MoleculeNet → [MolMapNet](../papers/foundations/molmapnet-2021.md) → Chemprop/D-MPNN → TDC to connect data, descriptors and graph models, then choose an ADMET endpoint. The reliability route connects [MoleculeACE](../papers/foundations/moleculeace-2022.md), [atom-level uncertainty](../papers/foundations/atom-uncertainty-2023.md) and the BBB experiments to distinguish what average scores, predictive confidence and experimental observations establish.

Topic entry points: use the [AI drug toxicity review](../papers/admet/ai-toxicity-review-2023.md) to explore toxicity tasks, data and tools; read [SSL-GCN](../papers/admet/ssl-gcn-2021.md) for learning from unlabeled molecules, [Domain-aware / pBRICS](../papers/admet/domain-aware-pbrics-2023.md) for chemical fragments and model interpretation, and [Uni-QSAR](../papers/admet/uni-qsar-2023.md) for automatic selection and integration of molecular representations.

For uncertainty estimation, start with [deep conformal toxicity prediction](../papers/admet/tox21-conformal-2021.md) to distinguish confidence, coverage and single-label efficiency. The [Tox21 10K library](../papers/admet/tox21-library-2020.md) explains experimental origins and quality control. See [method comparisons](comparison.md) for benchmark results and the [dataset dictionary](datasets.md) for access.

## Extending the map

Connect new topics to the relevant level and cross-reference papers across levels. Each entry retains the overview, publication information, research problem, datasets, method and findings, followed by experimental analysis and sources.

The editable [English SVG](../../assets/aidd-knowledge-pyramid.en.svg) is stored in the repository. Open the README image for a larger view.
