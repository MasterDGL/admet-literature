# Chemprop / D-MPNN

[English](../../en/papers/foundations/chemprop-dmpnn-2019.md) | **简体中文**

**Analyzing Learned Molecular Representations for Property Prediction**

[返回基础方法与基准总表](../../topics/foundations.md) · [返回首页](../../README.zh-CN.md)

**内容概述：** 通过沿有向化学键传递信息来学习分子表示，并在公开和工业数据上检验性质预测。

分类：基础方法。主题：分子图、D-MPNN、工业数据。

| 字段 | 内容 |
| --- | --- |
| 发表期刊/会议与时间 | Journal of Chemical Information and Modeling 59(8), 3370–3388；2019-07-30 |
| 日期口径 | 出版社在线发表日期 |
| 发表状态 | 正式期刊论文 |
| 主要痛点 | 学习得到的分子表示是否优于手工描述符，尤其能否推广到工业数据和新化学空间，缺少充分比较。 |
| 数据集 | 19 个公开与 16 个工业私有数据集，覆盖多类化学端点。 |
| 方法 | 有向键消息传递网络 D-MPNN，结合分子级计算特征及超参数优化；与固定描述符方法及已有图网络比较。 |
| 结论 | 在论文所测公开/工业任务中达到或超过多种对照，显示学习表示的实际价值；仍未达到实验重复性水平，结果取决于任务与划分。 |

DOI：`10.1021/acs.jcim.9b00237`

## 实验设置与结果分析

比较随机、骨架和可用的时间划分，分析新化学空间及工业数据上的泛化表现。

2019 年论文奠定了 Chemprop 的方法基础；项目后续持续更新，复现实验时应固定软件版本、分子特征和数据划分。

## 代码与参考资料

[代码与项目](https://github.com/chemprop/chemprop)

作者代码/项目入口已公开。

资料核对：**2026-09-22**。书目、正文相关方法与结果及列出的官方资源。

- [正式论文](https://doi.org/10.1021/acs.jcim.9b00237)
- [作者公开稿](https://arxiv.org/abs/1904.01561)
- [作者 PDF](https://people.csail.mit.edu/tommi/papers/acs.jcim.9b00237.pdf)
- [Chemprop 项目](https://github.com/chemprop/chemprop)
