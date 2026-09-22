"""Build the public literature catalog from data/papers.json (Python 3.10+)."""
from __future__ import annotations

import argparse
import csv
import io
import json
import posixpath
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import build_en

ROOT = Path(__file__).resolve().parents[1]
GROUPS = ['核心论文', '专题补读', '基础方法', '数据与基准', '综述', '观点文章', '预印本']
TOPICS = {'admet': 'ADMET 与药代动力学', 'foundations': '基础方法与基准'}
REQUIRED = ['id', 'name', 'title', 'one_liner', 'topic', 'group', 'publication', 'tags',
            'pain_point', 'datasets', 'method', 'conclusion', 'limitations',
            'evaluation', 'paper_url', 'sources', 'verified_on', 'verification_scope']


def validate(papers):
    ids, titles = set(), set()
    for p in papers:
        for key in REQUIRED:
            if not p.get(key):
                raise ValueError(f'{p.get("id")}: missing {key}')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', p['id']):
            raise ValueError(f'Invalid id: {p["id"]}')
        if p['id'] in ids or p['title'].casefold() in titles:
            raise ValueError(f'Duplicate: {p["id"]}')
        ids.add(p['id']); titles.add(p['title'].casefold())
        if not p['one_liner'].strip():
            raise ValueError(f'{p["id"]}: missing one_liner for README')
        if p['group'] not in GROUPS or p['topic'] not in TOPICS:
            raise ValueError(f'Unsupported group/topic: {p["id"]}')
        pub = p['publication']
        for k in ['venue', 'year', 'date', 'date_basis', 'status', 'citation']:
            if not pub.get(k):
                raise ValueError(f'{p["id"]}: missing publication.{k}')
        if not re.fullmatch(r'\d{4}(-\d{2}){0,2}', pub['date']):
            raise ValueError(f'Invalid publication date: {p["id"]}')
        if int(pub['date'][:4]) != pub['year']:
            raise ValueError(f'Inconsistent publication year: {p["id"]}')
        parts = pub['date'].split('-')
        date(*([int(v) for v in parts] + [1] * (3 - len(parts))))
        date.fromisoformat(p['verified_on'])
        if pub['status'] not in ['journal', 'conference', 'preprint']:
            raise ValueError(f'Invalid publication status: {p["id"]}')
        if (pub['status'] == 'preprint') != (p['group'] == '预印本'):
            raise ValueError(f'Preprint classification mismatch: {p["id"]}')
        urls = [p['paper_url']] + [s['url'] for s in p['sources']] + [p.get('code_url')]
        for url in filter(None, urls):
            parsed = urlparse(url)
            if parsed.scheme not in ['https', 'http'] or not parsed.netloc:
                raise ValueError(f'Invalid URL: {url}')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')


def table(headers, rows):
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows])


def note_path(p):
    return f'papers/{p["topic"]}/{p["id"]}.md'


def card(p):
    pub = p['publication']
    status = {'journal': '正式期刊论文', 'conference': '正式会议论文', 'preprint': '预印本'}[pub['status']]
    if pub['status'] == 'conference' and 'Workshop' in pub['venue']:
        status = '会议 Workshop 论文'
    fields = [['发表期刊/会议与时间', pub['citation']],
              ['日期口径', pub['date_basis']], ['发表状态', status],
              ['主要痛点', p['pain_point']], ['数据集', p['datasets']],
              ['方法', p['method']], ['结论', p['conclusion']]]
    sources = '\n'.join(f'- [{s["label"]}]({s["url"]})' for s in p['sources'])
    code = (f'[代码与项目]({p["code_url"]})\n\n{p["code_status"]}。'
            if p.get('code_url') else p['code_status'] + '。')
    doi = f'\nDOI：`{p["doi"]}`\n' if p.get('doi') else ''
    return f'''# {p['name']}

**{p['title']}**

[返回{TOPICS[p['topic']]}总表](../../topics/{p['topic']}.md) · [返回首页](../../README.md)

**一句话概括：** {p['one_liner']}

分类：{p['group']}。主题：{'、'.join(p['tags'])}。

{table(['字段', '内容'], fields)}
{doi}
## 实验设置与结果分析

{p['evaluation']}

{p['limitations']}

## 代码与参考资料

{code}

资料核对：**{p['verified_on']}**。{p['verification_scope']}。

{sources}
'''


def build(papers):
    artifacts = {note_path(p): card(p) for p in papers}
    count = Counter(p['group'] for p in papers)
    topic_count = Counter(p['topic'] for p in papers)
    latest = max(p['verified_on'] for p in papers)
    formal_research = sum(p['publication']['status'] != 'preprint' and p['group'] not in ['观点文章', '综述'] for p in papers)
    nav = table(['专题', '当前内容', '入口'], [
        ['ADMET 与药代动力学', f'{topic_count["admet"]} 篇', '[论文总表](topics/admet.md)'],
        ['基础方法与基准', f'{topic_count["foundations"]} 篇；分子表示、数据与评测', '[基础阅读](topics/foundations.md)'],
        ['其他 AIDD 方向', '扩展计划，尚未纳入独立专题', '[研究范围](docs/scope.md)']])
    core = table(['论文', '期刊/会议', '发表时间', '一句话概括'], [
        [f'[{p["name"]}]({note_path(p)})', p['publication']['venue'], p['publication']['date'], p['one_liner']]
        for p in papers if p['group'] == '核心论文'])
    overview = []
    for group in GROUPS:
        overview.append(f'### {group}')
        for p in papers:
            if p['group'] != group:
                continue
            links = f'[论文原文]({p["paper_url"]}) · [详细解读]({note_path(p)})'
            if p.get('code_url'):
                links += f' · [代码/项目]({p["code_url"]})'
            fields = [['发表期刊/会议与时间', p['publication']['citation']],
                      ['主要痛点', p['pain_point']], ['数据集', p['datasets']],
                      ['方法', p['method']], ['结论', p['conclusion']]]
            overview.append(f'#### {p["name"]}\n\n**{p["title"]}**\n\n'
                            f'**一句话概括：** {p["one_liner"]}\n\n'
                            + table(['字段', '内容'], fields) + '\n\n' + links)
    readme_papers = '\n\n'.join(overview)
    artifacts['README.md'] = f'''# ADMET 文献整理

ADMET literature notes, with supporting methods and benchmarks for AI-aided drug discovery.

梳理 **ADMET 与药代动力学预测** 的研究进展，整理代表论文、数据集与代码资源。每篇用一句话介绍研究内容，再展开 **发表期刊/会议与时间、主要痛点、数据集、方法和结论**。分子表示与基准文献提供相关基础知识。

目前收录 **{len(papers)} 篇**：**{topic_count['admet']} 篇 ADMET 与药代动力学**、**{topic_count['foundations']} 篇基础方法与基准**，其中 {count['核心论文']} 篇列为核心精读。正式研究与数据论文 {formal_research} 篇、综述 {count['综述']} 篇、观点文章 {count['观点文章']} 篇、预印本 {count['预印本']} 篇。最近一批资料核对日期：**{latest}**；各篇记录具体来源和核对日期。

## AIDD 知识地图

![AIDD 五层知识地图：自下而上为数据与研究问题、分子与蛋白表示、预测任务、设计与优化、实验验证与迭代；ADMET 是当前重点，实验结果反馈到数据。](assets/aidd-knowledge-pyramid.svg)

从数据和分子表示出发，逐步了解性质预测、分子设计与实验验证。ADMET 是当前阅读主线，也是多参数优化的重要依据；实验结果再反馈到数据与模型。[查看各层说明与阅读路线](docs/knowledge-map.md)。

## 导航

- [ADMET 论文总表](topics/admet.md)：按研究用途分类，逐篇保留五项核心信息。
- [基础方法与基准](topics/foundations.md)：Chemprop、AttentiveFP、MoleculeNet、MoleculeACE。
- [知识地图说明](docs/knowledge-map.md)：从研究问题找到方法、任务和阅读入口。
- [优先精读](#优先精读)：先建立研究问题、数据和方法的认识。
- [论文梳理](#论文梳理)：直接在本页查看全部 {len(papers)} 篇的一句话概括、发表信息、痛点、数据集、方法和结论。
- [选文与整理方法](docs/curation.md)：选文标准、实验比较和资料来源。
- [AIDD 研究范围](docs/scope.md)：当前覆盖与后续专题。
- [贡献方式](CONTRIBUTING.md)：推荐论文、纠正信息或补充实验依据。
- [结构化数据](data/papers.json) · [CSV 总表](data/papers.csv)。

{nav}

## 优先精读

{core}

建议顺序：**真实场景评测 → 单端点与人体 PK → 表示学习与多任务方法 → 平台应用**。专题总表另列数据基准、综述、观点文章和预印本，方便按阅读目的查找。

## 阅读与比较

比较模型时，重点看 **预测任务、数据来源、训练/测试划分、指标和对照方法**。单篇解读会列出这些实验设置，说明结果及其对后续研究的启发。历史榜单成绩附查询日期，预印本与正式发表版本分别标注。

## 论文梳理

[核心论文](#核心论文) · [专题补读](#专题补读) · [基础方法](#基础方法) · [数据与基准](#数据与基准) · [综述](#综述) · [观点文章](#观点文章) · [预印本](#预印本)

下列条目介绍每篇论文的研究问题、方法与主要发现；实验设置、结果分析和参考资料见详细解读。

{readme_papers}

## 数据与维护

`data/papers.json` 保存共享元数据与中文笔记，`data/papers.en.json` 按论文 ID 保存英文翻译。中英文页面一起生成，使用 Python 3.10 或更新版本，无第三方依赖：

```bash
python scripts/build.py
python scripts/build.py --check
```

第一条命令更新双语首页、专题总表、单篇解读及 CSV；第二条检查必填字段、重复记录、日期、URL、内部链接、翻译覆盖与同步状态，以及生成文件一致性。翻译维护步骤见[贡献方式](CONTRIBUTING.md)。

## 参考与致谢

组织方式参考 [awesome-AIDD](https://github.com/daiyun02211/awesome-AIDD) 的主题导航、[Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) 的论文与代码索引，以及 [OpenADMET](https://github.com/OpenADMET) 的开放数据与评测实践。

原创整理内容和维护脚本采用 [MIT License](LICENSE)。所引用论文、数据与第三方代码遵循各自的许可；本仓库提供链接与原创摘要，不分发论文全文。
'''
    for topic, title in TOPICS.items():
        sections = []
        for group in GROUPS:
            entries = sorted([p for p in papers if p['topic'] == topic and p['group'] == group],
                             key=lambda p: p['publication']['date'], reverse=True)
            if not entries:
                continue
            rows = [[f'[{p["name"]}](../{note_path(p)}) · [原文]({p["paper_url"]})',
                     p['publication']['citation'], p['pain_point'], p['datasets'], p['method'], p['conclusion']]
                    for p in entries]
            sections.append(f'## {group}\n\n' + table(['论文与解读', '期刊/会议与时间', '主要痛点', '数据集', '方法', '结论'], rows))
        intro = ('ADMET 指吸收、分布、代谢、排泄和毒性；相关理化性质与人体 PK 也在本专题范围内。'
                 if topic == 'admet' else
                 '这些文献介绍分子表示、公共数据与评测方法，为阅读 ADMET 研究提供基础。MoleculeACE 专门讨论生物活性悬崖。')
        artifacts[f'topics/{topic}.md'] = f'''# {title}

[返回首页](../README.md) · [知识地图](../docs/knowledge-map.md) · [筛选规则](../docs/curation.md) · [下载 CSV](../data/papers.csv)

{intro}

本专题共 **{topic_count[topic]} 篇**，组内按发表日期倒序排列。点击论文名查看一句话概括、实验设置、结果分析和资料来源。

''' + '\n\n'.join(sections) + '\n'
    buf = io.StringIO(newline='')
    writer = csv.writer(buf, lineterminator='\n')
    writer.writerow(['ID','论文简称','完整题名','一句话概括','专题','分类','主题','期刊或会议','发表时间','日期口径','发表状态','主要痛点','数据集','方法','结论','评测设置','限制','原文URL','代码URL','代码状态','核验日期','核对范围'])
    for p in papers:
        pub = p['publication']
        writer.writerow([p['id'],p['name'],p['title'],p['one_liner'],TOPICS[p['topic']],p['group'],'; '.join(p['tags']),pub['venue'],pub['date'],pub['date_basis'],pub['status'],p['pain_point'],p['datasets'],p['method'],p['conclusion'],p['evaluation'],p['limitations'],p['paper_url'],p.get('code_url') or '',p['code_status'],p['verified_on'],p['verification_scope']])
    artifacts['data/papers.csv'] = '\ufeff' + buf.getvalue()
    return artifacts


def check_links(artifacts):
    for relative, text in artifacts.items():
        if not relative.endswith('.md'):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', text):
            target = target.split('#')[0]
            if not target or urlparse(target).scheme:
                continue
            resolved = (ROOT / relative).parent.joinpath(target).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                raise ValueError(f'Broken local link in {relative}: {target}')


def bilingual(papers, translations):
    chinese = {}
    for path, content in build(papers).items():
        if path.endswith('.md'):
            content = content.replace('README.md)', 'README.zh-CN.md)')
        chinese['README.zh-CN.md' if path == 'README.md' else path] = content
    english = build_en.build(build_en.localize(papers, translations), table)
    for en_path in list(english):
        if not en_path.endswith('.md'):
            continue
        zh_path = 'README.zh-CN.md' if en_path == 'README.md' else en_path.removeprefix('en/')
        for path, other, store, lang in [(en_path, zh_path, english, 'en'), (zh_path, en_path, chinese, 'zh')]:
            target = posixpath.relpath(other, posixpath.dirname(path) or '.')
            switch = f'**English** | [简体中文]({target})' if lang == 'en' else f'[English]({target}) | **简体中文**'
            heading, body = store[path].split('\n', 1)
            store[path] = heading + '\n\n' + switch + '\n' + body
    return chinese | english


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--translation-hash', metavar='PAPER_ID', help='Print the current source hash after reviewing a translation.')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    papers = catalog['papers']
    validate(papers)
    if args.translation_hash:
        matches = [p for p in papers if p['id'] == args.translation_hash]
        if not matches:
            raise SystemExit('Unknown paper ID: ' + args.translation_hash)
        print(build_en.source_hash(matches[0]))
        return
    translations = json.loads((ROOT / 'data/papers.en.json').read_text(encoding='utf-8'))['papers']
    artifacts = bilingual(papers, translations)
    stale = []
    for relative, content in artifacts.items():
        dest = ROOT / relative
        if args.check:
            if not dest.exists() or dest.read_bytes() != content.encode('utf-8'):
                stale.append(relative)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content.encode('utf-8'))
    if stale:
        raise SystemExit('Generated files differ: ' + ', '.join(stale))
    all_markdown = {f.relative_to(ROOT).as_posix(): f.read_text(encoding='utf-8') for f in ROOT.rglob('*.md')}
    check_links(all_markdown)
    for directory in ['papers', 'en/papers']:
        for f in (ROOT / directory).rglob('*.md'):
            if f.relative_to(ROOT).as_posix() not in artifacts:
                raise ValueError(f'Unexpected paper file: {f.name}')
    print(f'{len(papers)} records validated; {len(artifacts)} generated files checked.' if args.check else f'Built {len(papers)} paper cards and catalog.')


if __name__ == '__main__':
    main()
