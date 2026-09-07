# 09 Production AI Quality

> 最终目标：让 AI 质量进入持续交付和生产运营。

## 线上质量闭环

```text
Offline Eval
 ↓
Release Gate
 ↓
Production
 ↓
Telemetry / User Feedback
 ↓
Online Evaluation
 ↓
Drift Detection
 ↓
Failure Mining
 ↓
New Eval Cases
 ↓
Regression
 ↺
```

## 核心能力

- Offline / Online Evaluation
- Model / Prompt / Dataset Versioning
- Data / Behavior Drift
- Production Sampling
- Feedback Mining
- Failure Clustering
- Regression Management
- Release Gate
- Quality SLO / SLA
- Cost / Latency / Quality Trade-off
- Business KPI Alignment

## Meta-Evaluation

在生产阶段继续验证 Evaluation 本身：Judge 是否稳定、指标是否有效、Eval Set 是否过时、指标是否与真实用户体验相关。

## 出口

能够把 AI Evaluation 从一次性的离线报告升级为持续的质量系统，并解释技术指标如何影响业务指标。
