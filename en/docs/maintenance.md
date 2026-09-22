# Maintenance

**English** | [简体中文](../../docs/maintenance.md)

[Home](../../README.md)

## Automated validation

Every push and pull request checks generated files, translation synchronization, internal links and maintenance scripts on Python 3.10 and 3.13. CI validates committed outputs; regenerate locally after editing source data:

```bash
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s scripts -p "test_*.py"
```

[Build history](https://github.com/MasterDGL/admet-literature/actions/workflows/validate.yml).

## Datasets and comparisons

`data/datasets.json` holds the dataset dictionary; `data/comparison.json` records implementations, datasets, protocols, metrics, means, standard deviations, sources and snapshot dates. The build generates bilingual pages, CSVs and the interactive table. Review all rows for a dataset together when updating its comparison, keeping protocol and snapshot date consistent.

Check data versions, labels, test splits and metrics before adding scores. Other experiments remain in individual paper notes. Publication labels come from paper metadata; update both language entries when a preprint is published.

## Code-link checks

Checks run every Monday at 02:23 UTC and can also be started manually through [Check code links](https://github.com/MasterDGL/admet-literature/actions/workflows/links.yml). CSV reports are retained for 30 days and can be downloaded from the run's Artifacts.

Run locally:

```bash
python scripts/check_links.py --output reports/code-links.csv
```

- `reachable`: accessible, with the final redirect address recorded.
- `unavailable`: neither attempt recovered and the final response was 404/410; check for a replacement address.
- `restricted_or_rate_limited`: HTTP 401/403/429.
- `retry_needed`: network or server failure; retry later.

The weekly workflow fails on `unavailable` results and retains the full report. HTTP checks establish accessibility; implementation completeness, weights, dependencies and reproduction results belong in the paper notes.

## Participation

Use [Discussions](https://github.com/MasterDGL/admet-literature/discussions) for questions and paper recommendations, [Issues](https://github.com/MasterDGL/admet-literature/issues) for specific corrections, and pull requests for contributions.
