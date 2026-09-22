# 维护说明

[English](../en/docs/maintenance.md) | **简体中文**

[返回首页](../README.zh-CN.md)

## 自动检查

每次 push 和 pull request 都在 Python 3.10、3.13 上检查生成文件、双语同步、内部链接及维护脚本。CI 检查已提交的生成结果，修改数据后先在本地生成：

```bash
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s scripts -p "test_*.py"
```

[查看构建记录](https://github.com/MasterDGL/admet-literature/actions/workflows/validate.yml)。

## 更新数据与方法对比

`data/datasets.json` 保存数据集字典；`data/comparison.json` 保存具体实现、数据集、协议、指标、均值、标准差、来源和查询日期。构建脚本生成双语说明、CSV 和交互表。更新一组比较时一起检查该数据集的所有行，保持协议与快照日期一致。

新增成绩先核对数据版本、标签、测试划分和指标。论文中的其他实验保留在单篇笔记；预印本状态由论文元数据生成，正式发表后同步更新双语条目。

## 代码链接巡检

每周一 02:23 UTC 自动检查，也可以在 [Check code links](https://github.com/MasterDGL/admet-literature/actions/workflows/links.yml) 中手动运行。CSV 报告保留 30 天，可从该次 Actions 运行的 Artifacts 下载。

本地运行：

```bash
python scripts/check_links.py --output reports/code-links.csv
```

- `reachable`：地址可访问，另记重定向后的地址。
- `unavailable`：两次请求均未恢复，最终返回 404/410；维护者检查迁移地址。
- `restricted_or_rate_limited`：401/403/429，表示访问限制或限流。
- `retry_needed`：网络或服务器错误，稍后重试。

每周工作流遇到 `unavailable` 时标记失败，并保留完整报告。HTTP 检查只验证入口是否可达；代码完整性、权重、依赖和复现结果由论文笔记记录。

## 参与

[Discussions](https://github.com/MasterDGL/admet-literature/discussions) 用于提问和推荐论文，[Issues](https://github.com/MasterDGL/admet-literature/issues) 用于具体更正；补充内容可以提交 pull request。
