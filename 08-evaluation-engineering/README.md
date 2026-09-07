# 08 Evaluation Engineering

> 把一次评估实验，变成可以持续运行的软件系统。

## 核心链路

```text
Dataset
 ↓
Runner
 ↓
Model / App
 ↓
Trace
 ↓
Grader
 ↓
Metrics
 ↓
Report
 ↓
Regression
```

## 工程能力

- Eval Runner
- Provider / Model Adapter
- Dataset Loader / Validator
- Grader Interface
- Metric Aggregation
- Retry / Timeout / Concurrency
- Trace Schema
- Result Storage
- Report Generation
- Baseline / Compare
- Regression Threshold
- CI Integration
- Reproducibility

## 设计原则

评估代码本身也必须可测试。Dataset、Runner、Grader、Metric 和 Report 应有清晰接口，结果能够复现、比较和追踪版本。

## 出口

能够从零实现一个最小 Evaluation Harness，并让它支持批量任务、多 Trial、Grader、指标、失败样本和 Regression Report。
