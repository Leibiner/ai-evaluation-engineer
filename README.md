# AI Evaluation Engineer

> 一条从传统软件测试出发，系统进入 AI Evaluation / AI Quality Engineering 的学习与实战路线。

## 这个仓库解决什么问题

很多 AI 学习路线从模型 API、Prompt、RAG、Agent 开始，结果是“会用 AI”，却不知道 AI 为什么会错，更不知道如何证明一个 AI 系统真的变好了。

本仓库反过来学习：

```text
理解 AI
  ↓
理解模型如何学习与产生行为
  ↓
理解 LLM 与 AI System
  ↓
定义“什么叫好”
  ↓
构造 Evaluation Dataset
  ↓
设计 Grader
  ↓
重复实验 + Metrics + Statistics
  ↓
Failure Analysis
  ↓
Regression
  ↓
Production Evaluation
  ↓
AI Quality Engineering
```

核心目标不是培养算法研究员，而是培养能够回答下面问题的工程师：

- AI 为什么会错？
- 错误来自数据、模型、Prompt、Context、Retrieval、Tool、Memory 还是 Agent Loop？
- 什么才是正确答案？
- 如何构造可信的 Eval Dataset？
- 如何选择 Grader？
- 一次结果是否可信？是否需要重复 Trial？
- 指标变化是真提升还是随机波动？
- 如何把离线评估变成持续 Regression？
- 如何把模型质量连接到线上业务质量？

## 核心认知

传统软件测试：

```text
需求 → 规则 → 代码 → 确定性行为 → Expected / Actual → Pass / Fail
```

AI 系统：

```text
Data / Model / Prompt / Context / Tools
              ↓
          AI Behavior
              ↓
       Outcome + Trace
              ↓
      Grader / Metrics
              ↓
 Statistical Evidence + Failure Analysis
              ↓
        Regression / Production
```

所以 AI Evaluation 不是“给 Prompt 写测试用例”，而是**用数据、实验、评估器和统计证据研究 AI 系统行为**。

## 学习路线

| 阶段 | 模块 | 目标 |
|---|---|---|
| 01 | [AI / ML Foundations](01-ai-ml-foundations/) | 建立模型学习与泛化的因果认知 |
| 02 | [LLM Foundations](02-llm-foundations/) | 理解 Token、Embedding、Transformer、Inference |
| 03 | [Evaluation Foundations](03-evaluation-foundations/) | 学会定义 Target、Dataset、Grader、Metric |
| 04 | [LLM Evaluation](04-llm-evaluation/) | 评估正确性、事实性、鲁棒性、一致性等 |
| 05 | [RAG Evaluation](05-rag-evaluation/) | 分层评估 Retrieval / Context / Generation |
| 06 | [Agent Evaluation](06-agent-evaluation/) | 评估 Planning、Tool、Trajectory、Recovery、Outcome |
| 07 | [Safety / Multimodal / Reliability](07-safety-multimodal-reliability/) | 扩展到安全、多模态和可靠性 |
| 08 | [Evaluation Engineering](08-evaluation-engineering/) | 把评估变成可运行的软件工程系统 |
| 09 | [Production AI Quality](09-production-ai-quality/) | Drift、Online Eval、Regression、业务质量 |

## 每个模块怎么学

每个模块都遵循同一闭环：

```text
Concept
  ↓
Why it matters
  ↓
Concrete example
  ↓
Experiment
  ↓
Implementation
  ↓
Evaluation
  ↓
Failure analysis
  ↓
Review
```

不追求“看过很多概念”，而追求每一章结束后都能留下：**一个能解释的模型、一个能运行的实验、一个能验证的结论。**

## 第一阶段：先把 AI 学明白

第一章不会直接跳到 Transformer 公式、RAG 或 Agent，而是先回答：

```text
AI 是什么？
ML 为什么叫“学习”？
Dataset 在学习中做什么？
Model 到底是什么？
Prediction 为什么会错？
Loss 为什么能让模型改变？
Training 到底发生了什么？
为什么训练得越好，真实任务不一定越好？
```

第一章的主线：

```text
AI
 ↓
ML
 ↓
Dataset + Label
 ↓
Model
 ↓
Prediction
 ↓
Loss / Error
 ↓
Parameter Update
 ↓
Training Loop
 ↓
Validation / Test
 ↓
Generalization
 ↓
Distribution Shift / Leakage / Contamination
 ↓
为什么需要 Evaluation
```

## 能力地图

完整能力地图见 [`roadmap/capability-map.md`](roadmap/capability-map.md)。

路线不是按“热门技术名词”堆砌，而按**认知依赖关系**组织：先理解 AI，再理解 AI System，再学习 Evaluation，最后进入工程化与生产质量。

## 学习进度

见 [`roadmap/learning-progress.md`](roadmap/learning-progress.md)。

进度只记录真正完成的内容：理解、实验、代码、评估、复盘，而不是简单打勾。

## 适合谁

- 传统软件测试工程师
- AI Test / AI Evaluation Engineer
- LLM / RAG / Agent Quality Engineer
- 希望从“测试功能”升级到“评估 AI 系统”的工程师

## 不以什么为目标

- 不以训练大模型为主线
- 不以刷 Prompt 技巧为主线
- 不要求一开始掌握复杂数学推导
- 不把“会调用 API”当成 AI 工程能力

## 最终目标

最终希望形成这样的能力链：

```text
Tester
  ↓
AI-aware Tester
  ↓
AI Evaluation Engineer
  ↓
Evaluation Engineer
  ↓
AI Quality Engineer
```

并能独立完成：

```text
定义质量目标
→ 设计 Dataset
→ 设计 Grader
→ 执行 Evaluation
→ 统计结果
→ 分析失败
→ 定位根因
→ 建立 Regression
→ 监控线上质量
```

## License

MIT
