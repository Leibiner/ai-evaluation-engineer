# Evaluation Engineering

这一层开始把 Evaluation 从“脚本”变成工程系统。

## 核心抽象

```text
EvalCase
  ↓
Runner
  ↓
Trial
  ↓
Trace
  ↓
Grader
  ↓
Metric
  ↓
Report
```

## 设计原则

1. Dataset 与 Runner 解耦
2. Grader 与 Model Provider 解耦
3. Trial 是独立执行单元
4. Trace 是可审计证据
5. Metrics 支持聚合与统计分析
6. 所有评估结果可版本化
7. 失败结果必须能够定位到具体层级

后续将在这里实现最小 Evaluation Harness。
