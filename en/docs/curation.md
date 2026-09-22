# Selection and curation

**English** | [简体中文](../../docs/curation.md)

[Home](../../README.md)

## Selection criteria

Prioritize ADMET and pharmacokinetic studies with clear research questions, substantial methodological or data contributions, and traceable experimental information. Classic methods explain technical development, recent studies introduce new questions and advances, and benchmarks and platforms provide practical entry points.

Each entry includes a brief overview, publication information, research problem, datasets, method and findings, with experimental settings, analysis, paper and code links. Selection also considers how a paper complements existing topics.

## Publication information

- Record journal online-publication dates and, where useful, issue dates.
- Record conference names and years at the precision provided by the source.
- Record preprint versions and update dates, linking later journal or conference versions.
- Classify algorithms, benchmarks, platforms, reviews and perspectives by their research role. Identify workshop papers by the specific workshop name.

## Experimental comparisons

Align prediction tasks, data versions, labels, units, train/test splits and metrics before comparing models. Analysis focuses on:

1. **Generalization:** what random, scaffold, temporal and OOD splits test, and how models perform on external data.
2. **Data use:** overlap between pretraining and test data, and the data used for tuning and model selection.
3. **Stability:** single models versus ensembles, run counts, random seeds and uncertainty ranges.
4. **Practical use:** false negatives and positives in classification, regression error magnitudes and experimental validation of candidates.
5. **Metric definitions:** AUROC, AUPRC, MAE, RMSE and R², with calculation details for custom aggregate scores.

When citing SOTA or leaderboard results, specify the task, metric, comparison methods and date so readers can track progress.

## ADMET data conventions

The [TDC ADMET Benchmark Group](https://tdcommons.ai/benchmark/admet_group/overview/) contains 22 tasks: 13 classification and 9 regression tasks. `Pgp_Broccatelli` is an inhibitor-classification task; inhibition and transport-substrate status are evaluated separately.

Distinguish experimental records, unique molecules and positive/negative counts. Platform outputs include model predictions, calculated properties and rule-based assessments. MoleculeACE evaluates bioactivity cliffs and is classified under methods and benchmarks.

## Sources and updates

Prioritize publisher/conference papers, author preprints, official benchmarks and code. Crossref and similar metadata support title, venue and date checks; methods, results and supplementary materials support the scientific notes.

`sources` stores reference links; `verification_scope` and `verified_on` record what was reviewed and when. Code status describes access to implementations, weights and environments. These are literature notes: experimental results come from the papers, and the repository has not independently reproduced the experiments.

Corrections update the sources and review record. Editorial changes retain the original source-review date. Track version changes and corresponding results when a preprint is published or data/code are revised. English and Chinese entries share metadata and are updated together through the [contribution workflow](../CONTRIBUTING.md).
