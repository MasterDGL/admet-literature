"""Summarize reviewed result records using an explicit, fixed comparison cohort."""
import json
from datetime import date
from pathlib import Path
from statistics import mean

from build_resources import csv_text, validate as validate_resources

ROOT = Path(__file__).resolve().parents[1]


def average_ranks(scores, direction):
    """Rank reported means; exact ties share the average of occupied positions."""
    if direction not in {'lower', 'higher'}:
        raise ValueError('Unknown metric direction')
    ordered = sorted(scores, key=lambda name: scores[name], reverse=direction == 'higher')
    result = {}
    start = 0
    while start < len(ordered):
        end = start + 1
        while end < len(ordered) and scores[ordered[end]] == scores[ordered[start]]:
            end += 1
        rank = (start + 1 + end) / 2
        for name in ordered[start:end]:
            result[name] = rank
        start = end
    return result


def validate(config, records, datasets, papers):
    validate_resources(datasets, records, papers)
    date.fromisoformat(config['reviewed_on'])
    if config['schema_version'] != 1:
        raise ValueError('Unsupported method schema')
    methods = config['methods']
    names = [m['name'] for m in methods]
    if len(names) != len(set(names)) or set(names) != {r['method'] for r in records}:
        raise ValueError('Method metadata must match all result implementations')
    for method in methods:
        if {r['paper_id'] for r in records if r['method'] == method['name']} != {method['paper_id']}:
            raise ValueError('Method paper does not match its result records')
        for lang in ['zh', 'en']:
            if not all(isinstance(method.get(lang, {}).get(k), str) and method[lang][k].strip()
                       for k in ['representation', 'learning', 'setting']):
                raise ValueError('Incomplete bilingual method metadata')
    cohort = config['cohort']
    for key in ['methods', 'datasets']:
        if not cohort[key] or len(cohort[key]) != len(set(cohort[key])):
            raise ValueError('Cohort must contain unique methods and datasets')
    if len(cohort['methods']) < 2 or not set(cohort['methods']) <= set(names):
        raise ValueError('Cohort needs at least two known methods')
    excluded = cohort['excluded_datasets']
    excluded_ids = [d['id'] for d in excluded]
    available = {r['dataset'] for r in records}
    if (len(excluded_ids) != len(set(excluded_ids))
            or set(excluded_ids) & set(cohort['datasets'])
            or set(excluded_ids) | set(cohort['datasets']) != available):
        raise ValueError('Cohort and exclusions must partition the available tasks')
    if any(not all(d.get(lang, '').strip() for lang in ['zh', 'en']) for d in excluded):
        raise ValueError('Each excluded task needs a bilingual reason')
    by_key = {(r['dataset'], r['method']): r for r in records}
    for dataset in cohort['datasets']:
        for name in cohort['methods']:
            if (dataset, name) not in by_key:
                raise ValueError('Missing result in fixed cohort: ' + dataset + ' / ' + name)
            record = by_key[dataset, name]
            if any(record[k] != cohort[k] for k in ['protocol', 'split']):
                raise ValueError('Result does not match the reviewed cohort protocol')


def summarize(config, records, datasets, papers):
    validate(config, records, datasets, papers)
    cohort = config['cohort']
    by_key = {(r['dataset'], r['method']): r for r in records}
    ranked = []
    for dataset in cohort['datasets']:
        entries = [by_key[dataset, name] for name in cohort['methods']]
        ranks = average_ranks({r['method']: r['mean'] for r in entries}, entries[0]['direction'])
        for r in entries:
            ranked.append({'cohort': cohort['id'], **r, 'rank': ranks[r['method']]})
    summaries = []
    for method in config['methods']:
        name = method['name']
        selected = [r for r in ranked if r['method'] == name]
        summaries.append({
            'method': name, 'paper_id': method['paper_id'],
            'collected_tasks': sum(r['method'] == name for r in records),
            'cohort': cohort['id'] if selected else '', 'ranked_tasks': len(selected),
            'mean_rank': mean(r['rank'] for r in selected) if selected else '',
            'top3_tasks': sum(r['rank'] <= 3 for r in selected) if selected else '',
            'best_rank': min(r['rank'] for r in selected) if selected else '',
            'worst_rank': max(r['rank'] for r in selected) if selected else '',
        })
    return summaries, ranked


def build(papers, table):
    config = json.loads((ROOT / 'data/methods.json').read_text(encoding='utf-8'))
    records = json.loads((ROOT / 'data/comparison.json').read_text(encoding='utf-8'))['records']
    datasets = json.loads((ROOT / 'data/datasets.json').read_text(encoding='utf-8'))['datasets']
    summaries, ranked = summarize(config, records, datasets, papers)
    by_paper = {p['id']: p for p in papers}
    by_summary = {s['method']: s for s in summaries}
    by_rank = {(r['dataset'], r['method']): r for r in ranked}
    cohort = config['cohort']
    total_tasks = len({r['dataset'] for r in records})
    task_count, method_count = len(cohort['datasets']), len(cohort['methods'])
    ordered = sorted([s for s in summaries if s['ranked_tasks']], key=lambda s: (s['mean_rank'], s['method']))
    artifacts = {'data/method_summary.csv': csv_text(summaries), 'data/method_task_ranks.csv': csv_text(ranked)}
    for en in [False, True]:
        lang = 'en' if en else 'zh'
        prefix, data_prefix = ('en/', '../../data/') if en else ('', '../data/')
        switch = '**English** | [简体中文](../../docs/methods.md)' if en else '[English](../en/docs/methods.md) | **简体中文**'
        home = '[Home](../../README.md)' if en else '[返回首页](../README.zh-CN.md)'
        title = 'Methods at a glance' if en else '按方法汇总'
        text = f'# {title}\n\n{switch}\n\n{home} · '
        text += '[Endpoint comparisons](comparison.md) · [Dataset dictionary](datasets.md)\n\n' if en else '[按端点对比](comparison.md) · [数据集字典](datasets.md)\n\n'
        text += (f'Compare the inputs, learning strategies and task coverage of **{len(summaries)} implementations**. The catalog contains **{len(records)} scores across {total_tasks} TDC tasks**; the fixed-cohort summary uses **{method_count} methods on {task_count} shared tasks**. Reviewed: **{config["reviewed_on"]}**.\n\n' if en else
                 f'集中查看 **{len(summaries)} 种实现**的输入表示、训练方式与任务覆盖。当前收录 **{total_tasks} 个 TDC 任务、{len(records)} 条成绩**；横向汇总使用 **{method_count} 个方法共同覆盖的 {task_count} 个任务**。核对日期：**{config["reviewed_on"]}**。\n\n')
        text += f'[{"Summary CSV" if en else "汇总 CSV"}]({data_prefix}method_summary.csv) · [{"Task ranks CSV" if en else "逐任务排名 CSV"}]({data_prefix}method_task_ranks.csv)\n\n'

        def paper_link(name):
            p = by_paper[by_summary[name]['paper_id']]
            return f'[{name}](../papers/{p["topic"]}/{p["id"]}.md)'

        def task_link(r):
            return f'[{r["endpoint"]}](comparison.md#{r["dataset"].lower()})'

        text += '## Representations and learning strategies\n\n' if en else '## 输入表示与训练方式\n\n'
        rows = []
        for method in config['methods']:
            name, meta = method['name'], method[lang]
            p = by_paper[method['paper_id']]
            status = ('🟠 Preprint' if en else '🟠 预印本') if p['publication']['status'] == 'preprint' else ('Published' if en else '已发表')
            code = f'[{"Code" if en else "代码"}]({p["code_url"]})' if p.get('code_url') else ('Not listed' if en else '未收录')
            rows.append([paper_link(name) + f'<br>{status} · {code}', meta['representation'], meta['learning'], f'{by_summary[name]["collected_tasks"]}/{total_tasks}'])
        text += table(['Implementation' if en else '方法实现', 'Input' if en else '输入表示', 'Learning strategy' if en else '训练方式', 'Collected tasks' if en else '收录任务数'], rows) + '\n\n'
        text += ('Coverage counts scores collected in this repository, not the total number of tasks studied by the authors. Code links lead to the paper projects; submission-specific settings are described below.\n\n' if en else
                 '任务数表示本仓库已收录的成绩数量，论文中的完整实验范围见单篇笔记。代码链接指向论文项目；本表对应的提交实现见下文。\n\n')

        text += '## Mean rank of collected results\n\n' if en else '## 所收录结果的平均排名\n\n'
        text += (f'Each of the {task_count} tasks compares the same {method_count} implementations, using reported means: MAE lower is better; AUROC, AUPRC and Spearman higher is better. Equal reported means receive the average of their occupied ranks. All tasks have equal weight. **Lower mean rank is better.** Top-3 counts tasks with an assigned rank ≤ 3, including ties under that rule.\n\n' if en else
                 f'{task_count} 个任务均使用同一组 {method_count} 种实现，按报告均值排名：MAE 越低越好，AUROC、AUPRC 和 Spearman 越高越好。相同均值取所占名次的平均值，各任务等权。**平均排名越低，整体名次越靠前。** Top-3 统计平均并列名次 ≤ 3 的任务数。\n\n')
        text += ('The sources report the [TDC scaffold protocol with 20% held-out test data](https://tdcommons.ai/benchmark/admet_group/overview/). This is a descriptive aggregation of leaderboard submissions and paper tables. Pretraining data and tuning budgets differ, and this repository has not rerun the models. Rankings describe this fixed set of collected results; mean ± SD alone does not establish statistical significance.\n\n' if en else
                 '各来源报告采用 [TDC 骨架划分、20% 留出测试协议](https://tdcommons.ai/benchmark/admet_group/overview/)。这里汇总榜单提交与论文表格的结果；预训练数据和调参预算各异，本仓库未重新训练模型。排名反映这组已收录成绩的相对位置，均值与标准差本身不构成显著性检验。\n\n')
        rows = [[paper_link(s['method']), f'{s["mean_rank"]:.2f}', s['ranked_tasks'], s['top3_tasks'], f'{s["best_rank"]:g}–{s["worst_rank"]:g}'] for s in ordered]
        text += table(['Method' if en else '方法', 'Mean rank ↓' if en else '平均排名 ↓', 'Shared tasks' if en else '共同任务数', 'Top-3 tasks' if en else 'Top-3 任务数', 'Task-rank range' if en else '逐任务名次范围'], rows) + '\n\n'

        text += '## Rank on each shared task\n\n' if en else '## 共同任务的逐项排名\n\n'
        text += ('Each column is one implementation. Follow an endpoint to see its original scores and sources.\n\n' if en else '每列对应一种实现。点击端点可查看原始成绩及出处。\n\n')
        rows = []
        for dataset in cohort['datasets']:
            first = by_rank[dataset, cohort['methods'][0]]
            rows.append([task_link(first), first['metric'] + (' ↓' if first['direction'] == 'lower' else ' ↑')] + [f'{by_rank[dataset, s["method"]]["rank"]:g}' for s in ordered])
        text += table(['Endpoint' if en else '端点', 'Metric' if en else '指标'] + [s['method'] for s in ordered], rows) + '\n\n'

        text += '## Highest and lowest relative ranks\n\n' if en else '## 相对名次最好与最差的端点\n\n'
        text += ('Endpoints are selected by each method’s rank among the fixed competitors, not by comparing raw scores across metrics. All ties are listed. Values are the original mean ± SD; each value links to its source.\n\n' if en else
                 '按方法在固定参评组中的名次选择端点，保留全部并列项；各指标的原始数值分别展示，不跨指标比较大小。数值为原始均值 ± 标准差，点击数值查看出处。\n\n')
        for s in ordered:
            rows = []
            for key in ['best_rank', 'worst_rank']:
                matches = [r for r in ranked if r['method'] == s['method'] and r['rank'] == s[key]]
                label = ('Highest' if en else '最好') if key == 'best_rank' else ('Lowest' if en else '最差')
                for r in matches:
                    rows.append([label, task_link(r), f'{r["rank"]:g}', r['metric'], f'[{r["mean"]:.3f} ± {r["std"]:.3f}]({r["source"]})'])
            text += f'### {s["method"]}\n\n'
            text += table(['Relative position' if en else '相对位置', 'Endpoint' if en else '端点', 'Rank' if en else '名次', 'Metric' if en else '指标', 'Mean ± SD' if en else '均值 ± 标准差'], rows) + '\n\n'

        text += '## Other collected results\n\n' if en else '## 其他已收录成绩\n\n'
        text += ('The following tasks remain in the endpoint tables but are outside this fixed cohort:\n\n' if en else '以下任务保留在端点表中，本次共同任务汇总未纳入：\n\n')
        for d in cohort['excluded_datasets']:
            text += f'- [{d["id"]}](comparison.md#{d["id"].lower()}): {d[lang]}\n'
        text += ('\nMethods outside the fixed cohort retain their collected scores below; their overall mean rank is N/A.\n\n' if en else '\n未进入固定参评组的方法保留各自成绩，综合平均排名记为 N/A。\n\n')
        rows = [[paper_link(r['method']), task_link(r), r['metric'], f'[{r["mean"]:.3f} ± {r["std"]:.3f}]({r["source"]})'] for r in records if r['method'] not in cohort['methods']]
        text += table(['Method' if en else '方法', 'Endpoint' if en else '端点', 'Metric' if en else '指标', 'Mean ± SD' if en else '均值 ± 标准差'], rows) + '\n\n'

        text += '## Implementation and result sources\n\n' if en else '## 实现设置与成绩来源\n\n'
        for method in config['methods']:
            name = method['name']
            entries = [r for r in records if r['method'] == name]
            sources = list(dict.fromkeys((r['source_kind'], r['source_location'], r['source']) for r in entries))
            # Leaderboard sources vary by endpoint; the score tables link every record.
            if all(kind == 'leaderboard' for kind, _, _ in sources):
                source = '[TDC endpoint tables](comparison.md)' if en else '[TDC 逐端点成绩](comparison.md)'
            else:
                source = ' · '.join(f'[{location}]({url})' for _, location, url in sources)
            text += f'**{paper_link(name)}** — {method[lang]["setting"]} {source}{"." if en else "。"}\n\n'
        text += ('The CSV exports preserve full precision for mean ranks and include original provenance for every ranked score. Missing aggregate values are blank in CSV.\n' if en else
                 'CSV 保留平均排名的完整精度及每条成绩的来源，未计算的汇总值留空。\n')
        artifacts[prefix + 'docs/methods.md'] = text
    return artifacts
