# 贡献方式

[English](en/CONTRIBUTING.md) | **简体中文**

欢迎推荐论文、纠正发表信息、补充实验设置和更新代码入口。

## 推荐一篇论文

请使用 [论文记录模板](templates/paper.md)，提供原文及 DOI/arXiv 标识、期刊或会议与日期、主要痛点、数据集、方法、结论。说明该工作与 AIDD 的关系，以及支持结论的原文表格或章节。

推荐时注明正式发表或预印本状态，并区分方法、综述、观点和数据基准。性能结论附原论文表格、补充材料或官方榜单来源。

## 更新记录

在 `data/papers.json` 维护共享元数据与中文笔记，在 `data/papers.en.json` 按相同论文 ID 维护英文翻译。题名、日期、DOI、链接和资料核对日期共用；摘要、五项核心信息、实验分析、代码状态和来源标签提供中英文内容。

每篇论文填写 `one_liner`，用一两句直白的中文说明“研究什么、主要怎么做”。README 以“内容概述”展示这段介绍及五项核心信息；实验结果使用具体任务、指标和对照方法描述。

核对英文内容与中文条目一致后，运行以下命令取得当前源记录的指纹，将输出填入对应英文条目的 `source_sha256`：

```bash
python scripts/build.py --translation-hash PAPER_ID
```

指纹用于发现源记录更新后需要复核的翻译。完成翻译后再更新指纹，然后生成并检查两版页面：

```bash
python scripts/build.py
python scripts/build.py --check
```

单篇笔记、首页、专题索引和 CSV 由脚本生成，不单独手工修改，以免与数据文件不一致。当前 `topic` 支持 `admet`（ADMET 与药代动力学）和 `foundations`（基础方法与基准）；新增其他专题时，同时扩展`scripts/build.py` 和 `scripts/build_en.py` 中的专题设置与说明。中文指南位于 `docs/`，英文指南位于 `en/docs/`；对应知识图为 `assets/aidd-knowledge-pyramid.svg` 和 `assets/aidd-knowledge-pyramid.en.svg`。默认首页是英文 `README.md`，中文首页为 `README.zh-CN.md`，各页顶部链接到对应语言版本。

`publication.date` 允许 `YYYY`、`YYYY-MM`、`YYYY-MM-DD` 三种精度，`date_basis` 说明会议年份、期刊在线日期、卷期月份或预印本日期。代码链接核实后填入；待补充时使用 `null`，并在 `code_status` 中说明进度。

资料核对日期对应实际查阅时间。代码可访问、环境运行成功、实验复现完成分别记录；数值结果附具体出处。

## 报告错误

提供条目名、错误字段、建议更正和原始来源链接。对数值更正，请注明数据版本、划分、指标、表格位置与原文版本。
