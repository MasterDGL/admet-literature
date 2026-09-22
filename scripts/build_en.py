"""English catalog rendering and translation synchronization checks."""
from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
import re

GROUPS = {
    '核心论文': 'Core papers', '专题补读': 'Further reading',
    '基础方法': 'Foundational methods', '数据与基准': 'Data and benchmarks',
    '综述': 'Reviews', '观点文章': 'Perspectives', '预印本': 'Preprints',
}
TOPICS = {'admet': 'ADMET and pharmacokinetics', 'foundations': 'Methods and benchmarks'}
FIELDS = ['name', 'one_liner', 'tags', 'pain_point', 'datasets', 'method',
          'conclusion', 'evaluation', 'limitations', 'code_status', 'verification_scope']


def publication_label(paper, en=True):
    pub = paper['publication']
    if pub['status'] == 'preprint':
        return '🟠 **Preprint**' if en else '🟠 **预印本**'
    if 'Workshop' in pub['venue']:
        return 'Workshop'
    return 'Published' if en else '已发表'


def recent_first(papers):
    return sorted(papers, key=lambda p: p['publication']['date'], reverse=True)


def source_hash(paper):
    raw = json.dumps(paper, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()


def localize(papers, translations):
    if set(translations) != {p['id'] for p in papers}:
        raise ValueError('English translations must match all catalog IDs exactly.')
    result = []
    for p in papers:
        t = translations[p['id']]
        if t.get('source_sha256') != source_hash(p):
            raise ValueError(f'{p["id"]}: English translation needs review against the updated source.')
        expected = set(FIELDS) | {'publication', 'source_labels', 'source_sha256'}
        if set(t) != expected or any(not t.get(k) for k in expected):
            raise ValueError(f'{p["id"]}: missing or unsupported translation field.')
        if any(not isinstance(t[k], str) or not t[k].strip() for k in FIELDS if k != 'tags'):
            raise ValueError(f'{p["id"]}: empty or invalid English text.')
        if not isinstance(t['tags'], list) or not all(isinstance(v, str) and v.strip() for v in t['tags']):
            raise ValueError(f'{p["id"]}: invalid English tags.')
        if set(t['publication']) != {'citation', 'date_basis'} or not all(t['publication'].values()):
            raise ValueError(f'{p["id"]}: incomplete publication translation.')
        if len(t['source_labels']) != len(p['sources']) or not all(t['source_labels']):
            raise ValueError(f'{p["id"]}: source-label count mismatch.')
        if re.search(r'[\u4e00-\u9fff]', json.dumps(t, ensure_ascii=False)):
            raise ValueError(f'{p["id"]}: untranslated Chinese in English fields.')
        q = copy.deepcopy(p)
        q.update({k: t[k] for k in FIELDS})
        q['publication'].update(t['publication'])
        for source, label in zip(q['sources'], t['source_labels']):
            source['label'] = label
        result.append(q)
    return result


def note(p):
    return f'papers/{p["topic"]}/{p["id"]}.md'


def core_fields(p):
    return [['Publication and date', p['publication']['citation']],
            ['Research problem', p['pain_point']], ['Datasets', p['datasets']],
            ['Method', p['method']], ['Findings', p['conclusion']]]


def build(papers, table):
    papers = recent_first(papers)
    artifacts = {}
    for p in papers:
        pub = p['publication']
        status = {'journal': 'Journal article', 'conference': 'Conference paper', 'preprint': 'Preprint'}[pub['status']]
        if pub['status'] == 'conference' and 'Workshop' in pub['venue']:
            status = 'Workshop paper'
        if pub['status'] == 'preprint':
            status = '🟠 **Preprint**'
        fields = core_fields(p)
        fields[1:1] = [['Date basis', pub['date_basis']], ['Publication status', status]]
        sources = '\n'.join(f'- [{s["label"]}]({s["url"]})' for s in p['sources'])
        code = (f'[Code and project]({p["code_url"]})\n\n' if p.get('code_url') else '') + p['code_status']
        doi = f'\nDOI: `{p["doi"]}`\n' if p.get('doi') else ''
        artifacts['en/' + note(p)] = f'''# {p['name']}

**{p['title']}**

[{TOPICS[p['topic']]} index](../../topics/{p['topic']}.md) · [Home](../../../README.md)

**In one sentence:** {p['one_liner']}

Category: {GROUPS[p['group']]}. Topics: {', '.join(p['tags'])}.

{table(['Field', 'Details'], fields)}
{doi}
## Experimental setup and analysis

{p['evaluation']}

{p['limitations']}

## Code and references

{code}

Sources reviewed: **{p['verified_on']}**. {p['verification_scope']}

{sources}
'''
    overview = []
    year = None
    for p in papers:
        if p['publication']['year'] != year:
            year = p['publication']['year']
            overview.append(f'### {year}')
        links = f'[Paper]({p["paper_url"]}) · [Detailed notes](en/{note(p)})'
        if p.get('code_url'):
            links += f' · [Code/project]({p["code_url"]})'
        overview.append(f'#### {p["name"]}\n\n**{p["title"]}**\n\n'
                        f'Date: **{p["publication"]["date"]}** · {publication_label(p)} · Category: {GROUPS[p["group"]]}.\n\n'
                        f'**In one sentence:** {p["one_liner"]}\n\n'
                        + table(['Field', 'Details'], core_fields(p)) + '\n\n' + links)
    core = table(['Paper', 'Journal/conference', 'Date', 'In one sentence'], [
        [f'[{p["name"]}](en/{note(p)})', p['publication']['venue'], p['publication']['date'], p['one_liner']]
        for p in papers if p['group'] == '核心论文'])
    counts = {t: sum(p['topic'] == t for p in papers) for t in TOPICS}
    formal = sum(p['publication']['status'] != 'preprint' and p['group'] not in ['观点文章', '综述'] for p in papers)
    reviews = sum(p['group'] == '综述' for p in papers)
    perspectives = sum(p['group'] == '观点文章' for p in papers)
    preprints = sum(p['group'] == '预印本' for p in papers)
    core_count = sum(p['group'] == '核心论文' for p in papers)
    latest = max(p['verified_on'] for p in papers)
    overview_text = '\n\n'.join(overview)
    year_nav = ' · '.join(f'[{year}](#{year})' for year in dict.fromkeys(p['publication']['year'] for p in papers))
    artifacts['README.md'] = f'''# ADMET Literature

Research notes on **ADMET and pharmacokinetic prediction**, with representative papers, datasets and code. Each entry starts with a one-sentence summary and covers **publication venue and date, research problem, datasets, method and findings**. Papers on molecular representations and benchmarks provide the foundations.

The collection contains **{len(papers)} papers**: **{counts['admet']} on ADMET and pharmacokinetics** and **{counts['foundations']} on methods and benchmarks**, including {core_count} core readings. Publication types: {formal} published research/data papers, {reviews} review, {perspectives} perspective and {preprints} preprints. Most recent batch of source reviews: **{latest}**; each entry records its own sources and review date.

## AIDD knowledge map

![Five levels of AIDD research: data and research questions, representations, prediction, design, and experimental validation. ADMET is the current focus; experiments feed back into data.](assets/aidd-knowledge-pyramid.en.svg)

Start with data and molecular representations, then explore property prediction, molecular design and experimental validation. ADMET is the main reading focus and an input to multiparameter optimization; experimental results feed back into data and models. [Explore the map and reading routes](en/docs/knowledge-map.md).

## Navigation

- [ADMET paper index](en/topics/admet.md): papers ordered from newest to oldest, with all five core fields.
- [Method comparisons](en/docs/comparison.md): endpoint-specific TDC scores, an interactive table and CSV.
- [Dataset dictionary](en/docs/datasets.md): sizes, endpoints, sources, licenses and loading instructions.
- [Methods and benchmarks](en/topics/foundations.md): Chemprop, AttentiveFP, MoleculeNet and MoleculeACE.
- [Knowledge map](en/docs/knowledge-map.md): connect research questions, methods and reading routes.
- [Core reading](#core-reading): a starting point for research questions, data and methods.
- [Paper notes](#paper-notes): one-sentence summaries and all five fields for every paper, directly on this page.
- [Selection and curation](en/docs/curation.md): selection criteria, experimental comparisons and sources.
- [Research scope](en/docs/scope.md): current coverage and planned topics.
- [Discussions](https://github.com/MasterDGL/admet-literature/discussions): questions and paper recommendations.
- [Maintenance](en/docs/maintenance.md): automated validation, link checks and data updates.
- [Contributing](en/CONTRIBUTING.md): recommend papers, correct metadata or add experimental details.
- [Shared catalog](data/papers.json) · [English translations](data/papers.en.json) · [English CSV](data/papers.en.csv).

| Topic | Coverage | Entry point |
| --- | --- | --- |
| ADMET and pharmacokinetics | {counts['admet']} papers | [Paper index](en/topics/admet.md) |
| Methods and benchmarks | {counts['foundations']} papers on representations, data and evaluation | [Foundational reading](en/topics/foundations.md) |
| Other AIDD areas | Planned topics | [Research scope](en/docs/scope.md) |

## Core reading

{core}

Suggested route: **practical evaluation → individual endpoints and human PK → representation learning and multitask methods → platforms**. The index lists all papers from newest to oldest and labels their research categories.

## Reading and comparison

Compare **prediction tasks, data sources, train/test splits, metrics and baselines**. Detailed notes describe the experiments, findings and implications for further research. Historical leaderboard results include snapshot dates; preprints and published versions are identified separately.

## Paper notes

{year_nav}

Papers below are ordered by publication date, newest first. Each entry explains the research problem, method and main findings. Follow the detailed notes for experimental settings, analysis and references.

{overview_text}

## Data and maintenance

`data/papers.json` holds shared metadata and Chinese notes; `data/papers.en.json` holds English translations linked by paper ID. Both versions are generated together with Python 3.10+ and no third-party dependencies:

```bash
python scripts/build.py
python scripts/build.py --check
```

The build updates both homepages, topic indexes, paper notes and CSV exports. Checks cover required fields, duplicate records, dates, URLs, local links, translation coverage, source synchronization and generated-file consistency. See [Contributing](en/CONTRIBUTING.md) for the translation workflow.

## How to cite

Use [CITATION.cff](CITATION.cff) or GitHub's "Cite this repository" sidebar entry when citing these literature notes. Cite the original papers for methods and experimental findings, and record the commit used when reusing notes.

```bibtex
@misc{{du_admet_literature,
  author = {{Du, Guangliang}},
  title = {{ADMET Literature: Bilingual Research Notes}},
  year = {{2026}},
  url = {{https://github.com/MasterDGL/admet-literature}}
}}
```

## References and acknowledgments

The organization draws on topic navigation in [awesome-AIDD](https://github.com/daiyun02211/awesome-AIDD), paper/code indexing in [Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection), and the open-data and evaluation work of [OpenADMET](https://github.com/OpenADMET).

Original notes and maintenance scripts use the [MIT License](LICENSE). Referenced papers, datasets and third-party code retain their own licenses; this repository provides links and original summaries.
'''
    for topic, title in TOPICS.items():
        entries = [p for p in papers if p['topic'] == topic]
        rows = [[p['publication']['date'],
                 f'[{p["name"]}](../{note(p)}) · [Paper]({p["paper_url"]})<br>{publication_label(p)} · {GROUPS[p["group"]]}',
                 p['publication']['citation'], p['pain_point'], p['datasets'], p['method'], p['conclusion']]
                for p in entries]
        listing = table(['Date', 'Paper and category', 'Publication and date', 'Research problem', 'Datasets', 'Method', 'Findings'], rows)
        intro = ('ADMET covers absorption, distribution, metabolism, excretion and toxicity. Related physicochemical properties and human PK are also included.'
                 if topic == 'admet' else
                 'These papers introduce molecular representations, public datasets and evaluation methods for reading ADMET research. MoleculeACE focuses on bioactivity cliffs.')
        artifacts[f'en/topics/{topic}.md'] = f'''# {title}

[Home](../../README.md) · [Knowledge map](../docs/knowledge-map.md) · [Curation](../docs/curation.md) · [Download CSV](../../data/papers.en.csv)

{intro}

**{counts[topic]} papers**, sorted by publication date, newest first. Follow a paper title for its summary, experiments, analysis and sources.

''' + listing + '\n'
    buf = io.StringIO(newline='')
    writer = csv.writer(buf, lineterminator='\n')
    writer.writerow(['ID', 'Short name', 'Full title', 'One-sentence summary', 'Topic', 'Category', 'Tags', 'Journal/conference', 'Publication date', 'Date basis', 'Publication status', 'Research problem', 'Datasets', 'Method', 'Findings', 'Experimental setup', 'Analysis', 'Paper URL', 'Code URL', 'Code status', 'Review date', 'Review scope'])
    for p in papers:
        pub = p['publication']
        writer.writerow([p['id'], p['name'], p['title'], p['one_liner'], TOPICS[p['topic']], GROUPS[p['group']], '; '.join(p['tags']), pub['venue'], pub['date'], pub['date_basis'], pub['status'], p['pain_point'], p['datasets'], p['method'], p['conclusion'], p['evaluation'], p['limitations'], p['paper_url'], p.get('code_url') or '', p['code_status'], p['verified_on'], p['verification_scope']])
    artifacts['data/papers.en.csv'] = '\ufeff' + buf.getvalue()
    return artifacts
