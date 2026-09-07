# 03 Evaluation Foundations

> 从“模型会不会”转向“如何科学地证明它会不会”。

## 核心对象

```text
Evaluation Target
    ↓
Capability / Behavior
    ↓
Task / Eval Case
    ↓
Dataset / Golden Set
    ↓
Ground Truth / Rubric
    ↓
Grader
    ↓
Metric
```

## 学习内容

- Evaluation Target：到底评什么
- Task / Eval Case：一个可执行评估问题
- Dataset / Eval Set / Golden Set：一组评估任务
- Ground Truth / Reference：什么才算正确
- Rubric：开放式任务如何定义质量
- Grader：Rule / Code / Human / Model-based
- Metric：如何把结果聚合成指标
- Benchmark / Evaluation Suite：如何组织规模化评估
- Coverage / Difficulty / Representativeness
- Dataset Versioning

## 核心原则

能用确定性规则验证，就不要优先使用 LLM Judge；能执行验证，就不要只做主观阅读。

## 出口

能够从一个业务目标独立设计一套最小 Evaluation：目标、数据、标准、Grader、Metric 和结果解释全部说得清楚。
