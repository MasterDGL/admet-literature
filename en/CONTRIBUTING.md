# Contributing

**English** | [简体中文](../CONTRIBUTING.md)

[Home](../README.md)

Recommend papers, correct publication details, add experimental settings or update code links.

## Recommend a paper

Use the [paper template](templates/paper.md). Include the original paper and DOI/arXiv identifier, venue and date, research problem, datasets, method and findings. Explain its connection to AIDD and identify the original tables or sections supporting the findings.

Identify the publication status and distinguish methods, perspectives and benchmarks. Support performance claims with original tables, supplementary material or official leaderboards.

## Update the bilingual catalog

Edit shared metadata and Chinese notes in `data/papers.json`; edit the corresponding English entry in `data/papers.en.json`, keyed by the same paper ID. Titles, dates, DOI, URLs and source-review dates are shared. English fields translate the scientific notes, citation text, tags, code status and source labels.

Write `one_liner` as a direct explanation of what the study investigates and how it does so. Both READMEs display this sentence and the five core fields. Describe results through specific tasks, metrics and baselines.

After reviewing the English entry against its source, obtain the source fingerprint:

```bash
python scripts/build.py --translation-hash PAPER_ID
```

Copy the printed value into that translation's `source_sha256`, then build and check:

```bash
python scripts/build.py
python scripts/build.py --check
```

The fingerprint detects source changes that need translation review. The check also requires one English entry for every paper and checks generated files and local links. Update translated text before recording the new fingerprint.

Paper notes, homepages, topic indexes and CSV exports are generated together. Chinese paper paths remain under `papers/` and English paths under `en/papers/`; the homepages are `README.zh-CN.md` and `README.md`. The current topics are `admet` and `foundations`. New topics require updates to both renderers in `scripts/build.py` and `scripts/build_en.py`.

Maintain guide translations in `docs/` and `en/docs/`, and the two knowledge maps in `assets/aidd-knowledge-pyramid.svg` and `assets/aidd-knowledge-pyramid.en.svg`. Every page links to its counterpart.

`publication.date` accepts `YYYY`, `YYYY-MM` or `YYYY-MM-DD`; `date_basis` explains the date type. Add verified code URLs, or use `null` and describe progress in `code_status`.

Source-review dates reflect actual reading. Record code accessibility, successful environment setup and experiment reproduction separately. Attach precise sources to numerical results.

## Report an error

Provide the entry, field, proposed correction and original source. For numerical changes, identify the data version, split, metric, table location and paper version.
