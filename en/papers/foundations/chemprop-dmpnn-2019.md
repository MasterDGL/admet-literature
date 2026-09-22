# Chemprop / D-MPNN

**English** | [简体中文](../../../papers/foundations/chemprop-dmpnn-2019.md)

**Analyzing Learned Molecular Representations for Property Prediction**

[Methods and benchmarks index](../../topics/foundations.md) · [Home](../../../README.md)

**Overview:** Learns molecular representations by passing messages along directed chemical bonds and evaluates property prediction on public and industrial data.

Category: Foundational methods. Topics: Molecular graphs, D-MPNN, Industrial data.

| Field | Details |
| --- | --- |
| Publication and date | Journal of Chemical Information and Modeling 59(8), 3370–3388; 2019-07-30 |
| Date basis | Publisher online publication date |
| Publication status | Journal article |
| Research problem | Evidence was limited on whether learned representations outperform handcrafted descriptors and generalize to industrial data and new chemical space. |
| Datasets | 19 public and 16 private industrial datasets spanning multiple chemical endpoints. |
| Method | Directed-bond message passing (D-MPNN), molecular-level computed features and hyperparameter optimization, compared with fixed descriptors and earlier graph networks. |
| Findings | Matches or exceeds several baselines on the evaluated public/industrial tasks, demonstrating the practical value of learned representations. Performance remains below experimental reproducibility and varies by task and split. |

DOI: `10.1021/acs.jcim.9b00237`

## Experimental setup and analysis

Compares random, scaffold and available temporal splits to assess generalization to new chemical space and industrial data.

The 2019 paper establishes Chemprop's methodological foundation. Later software development makes version, feature and split control important for reproduction.

## Code and references

[Code and project](https://github.com/chemprop/chemprop)

The authors provide a public code/project page.

Sources reviewed: **2026-09-22**. Bibliographic metadata, relevant methods and results, and the listed official resources.

- [Published paper](https://doi.org/10.1021/acs.jcim.9b00237)
- [Author manuscript](https://arxiv.org/abs/1904.01561)
- [Author PDF](https://people.csail.mit.edu/tommi/papers/acs.jcim.9b00237.pdf)
- [Chemprop project](https://github.com/chemprop/chemprop)
