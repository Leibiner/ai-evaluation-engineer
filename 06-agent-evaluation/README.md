# 06 Agent Evaluation

> Agent 的质量不是“最终答对没有”这么简单，而是 Goal → Plan → Action → Observation → State → Outcome 的完整行为。

## 评估对象

- Goal / Task Success
- Planning / Decomposition
- Decision
- Tool Selection
- Tool Arguments
- Tool Result Handling
- State / Memory
- Trajectory / Trace
- Recovery / Retry
- Long-horizon Reliability
- Steps / Tokens / Latency / Cost
- Safety / Excessive Agency

## 核心模型

```text
Goal
 ↓
Planning
 ↓
Decision
 ↓
Tool / Action
 ↓
Observation
 ↓
State Update
 ↺
 ↓
Outcome
```

## 核心原则

`Outcome + Trace` 必须一起看。最终成功不代表过程可靠；一次成功也不代表长链路稳定。

## 出口

能够构造可控 Agent 环境，记录完整 Trace，并分别评估计划、工具、轨迹、恢复能力和最终任务成功率。
