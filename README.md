# AI Evaluation Engineer

> 从传统软件测试出发，系统学习 AI Evaluation / AI Quality Engineering。

## 项目定位

这不是一份 AI 名词清单，而是一条按照**知识依赖关系**设计的学习路线。

核心目标：

> 从传统软件测试工程师，逐步成长为能够理解 AI、评估 LLM / RAG / Agent、建设 Evaluation Engineering，并最终负责 Production AI Quality 的工程师。

---

# 学习总路线

当前仓库只展开 **Phase 01**。后续阶段只保留学习大纲，等前一阶段真正完成后再展开。

| 阶段 | 主题 | 核心学习内容 | 最终能力 |
|---|---|---|---|
| **01** | **AI / ML Foundations** | AI、ML、DL、Dataset、Label、Model、Training、Inference、Loss、Optimization、Validation、Generalization、Distribution Shift | 理解模型如何学习、如何预测、为什么犯错 |
| **02** | **LLM Foundations** | Token、Tokenization、Embedding、Transformer、Attention、Context、Pre-training、Inference、Decoding | 理解现代 LLM 的基本工作机制 |
| **03** | **LLM Inference & Behavior** | Context、Sampling、Temperature、Top-p、Decoding、Prompt Sensitivity、Structured Output、Behavior | 理解 LLM 为什么会产生不同输出 |
| **04** | **LLM Reasoning & AI System** | Reasoning、Planning、Reflection、Context Management、Workflow、State、AI Application Architecture | 理解 LLM 如何参与复杂任务和 AI 应用 |
| **05** | **RAG & Agent** | Retrieval、Ranking、Context、Tool Use、Function Calling、Memory、Trajectory、Agent Loop、Long Horizon | 理解 RAG / Agent 系统如何工作 |
| **06** | **AI Evaluation** | Evaluation Target、Dataset、Ground Truth、Rubric、Grader、Metric、Benchmark、Statistics | 能把“好不好”变成可执行评估 |
| **07** | **专项 Evaluation** | LLM、RAG、Agent、多模态、安全、可靠性、Robustness | 能针对不同 AI 系统建立专项评测 |
| **08** | **Evaluation Engineering** | Runner、Dataset、Grader、Metric、Trace、Report、Regression、CI、Reproducibility | 能构建可持续运行的 Evaluation 系统 |
| **09** | **Production AI Quality** | Online Eval、Drift、Feedback、Failure Mining、Release Gate、Quality SLO、Business KPI | 能建立生产环境 AI Quality 闭环 |

---

# 学习依赖关系

不是简单地“学完一章就换一个主题”，而是逐层建立依赖：

```text
Phase 01
AI / ML
   ↓
Phase 02
LLM 基础
   ↓
Phase 03
Inference / Behavior
   ↓
Phase 04
Reasoning / AI System
   ↓
Phase 05
RAG / Agent
   ↓
Phase 06
Evaluation
   ↓
Phase 07
专项 Evaluation
   ↓
Phase 08
Evaluation Engineering
   ↓
Phase 09
Production AI Quality
```

因此：

> **没有 Phase 01 的 Model / Training / Inference 基础，不直接跳到 LLM Evaluation；没有 LLM / AI System 基础，不直接跳到 Agent Evaluation。**

---

# 每个阶段的学习方式

每个阶段最终都不是“看完文档”就算完成，而是：

```text
理解概念
   ↓
建立因果链
   ↓
真实案例
   ↓
动手实验
   ↓
最小代码实现
   ↓
产生数据
   ↓
Evaluation
   ↓
Failure Analysis
   ↓
复盘
```

每个阶段都必须回答四个问题：

1. **What**：它是什么？
2. **Why**：为什么需要它？
3. **How**：它如何工作？如何实验？
4. **Evidence**：如何证明自己的结论可信？

---

# 传统测试能力如何迁移

| 传统测试 | AI Evaluation |
|---|---|
| 测试需求 | Evaluation Target |
| 测试用例 | Eval Case |
| 测试数据 | Evaluation Dataset |
| Expected Result | Ground Truth / Reference |
| 断言 | Grader |
| Pass Rate | Evaluation Metric |
| 自动化测试 | Evaluation Runner / Harness |
| 回归测试 | Evaluation Regression |
| 缺陷分析 | Failure Analysis / Root Cause |
| 性能测试 | Latency / Token / Cost Evaluation |
| 安全测试 | Safety / Red Team Evaluation |

最终不是放弃测试，而是把测试能力迁移到**概率性、生成式、学习型系统**。

---

# 当前学习：Phase 01

## AI / ML Foundations

第一阶段是整个路线的地基。

当前只学习：

**[→ 进入 Phase 01：AI / ML Foundations](./01-ai-ml-foundations/README.md)**

第一阶段重点解决：

```text
AI 是什么？
   ↓
ML 为什么叫“学习”？
   ↓
数据在学习中扮演什么角色？
   ↓
Model 到底是什么？
   ↓
模型如何产生 Prediction？
   ↓
Prediction 为什么会错？
   ↓
Loss 如何衡量错误？
   ↓
模型如何根据错误更新参数？
   ↓
Training 是怎么循环起来的？
   ↓
如何验证模型真的学会了？
   ↓
什么是 Generalization？
   ↓
为什么真实世界会出现 Distribution Shift？
   ↓
为什么最终需要 Evaluation？
```

---

# 当前仓库结构

```text
ai-evaluation-engineer/
│
├── README.md
│   └── 总路线 + 全阶段大纲
│
└── 01-ai-ml-foundations/
    └── README.md
        └── 第一阶段详细学习内容
```

**当前只保留第一阶段。** 后续阶段不会提前建立文件，避免学习路线变成一堆尚未真正学习的空目录。

---

# 最终目标

最终形成完整能力链：

```text
理解 AI
  ↓
理解 LLM
  ↓
理解 Inference / Behavior
  ↓
理解 Reasoning / AI System
  ↓
理解 RAG / Agent
  ↓
设计 Evaluation
  ↓
执行专项 Evaluation
  ↓
建设 Evaluation Engineering
  ↓
负责 Production AI Quality
```

最终能力不是：

> **“我会多少 AI 工具。”**

而是：

> **“我能够解释 AI 系统为什么产生这个结果，并用可重复的实验、数据、指标和工程系统证明它到底好不好。”**
