# AI Evaluation 测试工程师能力地图 V2.1

> 从传统软件测试工程师 → AI Evaluation Engineer → AI Quality Engineer
>
> **核心路线：** 理解 AI → 理解 AI 系统 → 学会评测 → 学会构建 Eval → 学会验证 Eval → 进入生产质量 → 建立 AI Quality 能力

## 0. 能力地图总览

AI Evaluation Engineer 不是“给大模型写测试用例”，而是使用**工程化、统计学和实验方法**，对 AI 模型及 AI 应用系统的能力、质量、安全、可靠性和业务效果进行**可重复、可量化、可验证的评估**，并能够定位问题根因。

### AI System Quality Model

```text
                    AI System
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
      Model           Prompt          Context
        │               │               │
        └───────────────┼───────────────┘
                        ↓
                      RAG
                        │
              ┌─────────┴─────────┐
              ↓                   ↓
          Retrieval            Generation
              │                   │
              └─────────┬─────────┘
                        ↓
                      Agent
                        │
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
     Tool             Memory         Environment
       │                │                │
       └────────────────┼────────────────┘
                        ↓
                   E2E Outcome
```

**核心问题：** 为什么错？错在哪一层？如何证明？

---

# 一、基础认知层

## 01 AI / ML Fundamentals

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| AI/ML/DL 基础 | AI, ML, DL, supervised/unsupervised learning | AI、ML、DL关系及基本范式 | 能解释典型模型训练流程 | P0 | L2 |
| 神经网络 | Neural Network, Layer, Activation, Loss | 参数、激活、损失如何影响学习 | 阅读简单训练代码并定位基本问题 | P0 | L2 |
| 训练与微调 | Training, Fine-tuning, PEFT, LoRA | 预训练、微调、对齐的目的 | 理解微调前后行为变化 | P0 | L2 |
| 泛化 | Overfitting, Underfitting, Generalization | 训练集与真实任务表现差异 | 分析数据/模型导致的泛化问题 | P0 | L2 |
| 模型评估 | Validation, Test Set, Benchmark | 为什么需要独立评估集 | 设计基本模型评估实验 | P0 | L2 |
| 数据问题 | Distribution Shift, Leakage, Contamination | 数据分布与评估可信度 | 识别数据泄漏和污染风险 | P1 | L2 |

**目标：** 理解模型为什么产生当前行为，而不是把模型当作黑盒 API。

## 02 LLM Fundamentals

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Transformer | Attention, Self-Attention, Transformer | Transformer基本结构 | 能解释输入到输出的主要路径 | P0 | L2 |
| Token | Token, Tokenization, Vocabulary | 文本如何变成Token | 比较不同文本Token数量 | P0 | L3 |
| Embedding | Embedding, Vector, Semantic Similarity | 文本向量与语义空间 | 完成简单相似度实验 | P0 | L2 |
| Context | Context Window, Context Length | 上下文如何影响模型行为 | 设计上下文长度实验 | P0 | L3 |
| Inference | Inference, Decoding | 推理阶段发生什么 | 理解请求到生成的过程 | P0 | L2 |
| Sampling | Temperature, Top-p, Top-k | 随机性来源 | 做参数对输出稳定性的实验 | P0 | L3 |
| Model Parameters | Parameters, Weights | 参数与能力的关系 | 理解模型版本差异 | P1 | L2 |
| Structured Output | JSON Schema, Function Calling | 输出约束机制 | 验证结构化输出正确性 | P0 | L3 |

## 03 LLM Behavior

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| 指令遵循 | Instruction Following | 模型是否遵循任务要求 | 设计约束遵循测试 | P0 | L3 |
| 正确性 | Correctness, Accuracy | 输出是否正确 | 构建可验证答案集 | P0 | L3 |
| 事实性 | Factuality, Hallucination | 幻觉与事实错误 | 设计事实性评估 | P0 | L3 |
| 相关性 | Relevance | 是否回答用户问题 | 设计Relevance rubric | P0 | L3 |
| 完整性 | Completeness | 是否遗漏关键要求 | 构建完整性评估 | P0 | L3 |
| 一致性 | Consistency | 同一任务多次结果是否稳定 | 设计重复Trial | P0 | L3 |
| 鲁棒性 | Robustness | 输入变化是否导致异常行为 | 做扰动/边界测试 | P0 | L3 |
| 效率 | Reasoning Efficiency, Latency, Tokens | 能力与成本之间关系 | 统计Token/Latency | P1 | L2 |

## 04 Reasoning

> **Reasoning ≠ Chain-of-Thought ≠ Planning ≠ Agent。** 评估重点应放在可观察、可验证的行为、过程信号和最终结果，而不是要求暴露内部思维链。

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| 推理能力 | Reasoning, Multi-step Reasoning | 多步问题解决能力 | 设计多步骤Eval Task | P0 | L3 |
| 推理正确性 | Logical Correctness, Verifiable Result | 推理是否导向正确结论 | 使用程序/规则验证结果 | P0 | L3 |
| 复杂度 | Reasoning Depth, Difficulty | 任务难度与推理成本 | 按难度分层评估 | P1 | L3 |
| 稳定性 | Reasoning Consistency | 随机采样导致的波动 | 多Trial统计成功率 | P0 | L3 |
| 效率 | Token Efficiency, Latency, Cost | 推理质量与成本关系 | 做质量/成本分析 | P1 | L3 |

---

# 二、AI 系统理解层

## 05 AI System Architecture

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Prompt | System Prompt, User Prompt, Template | Prompt如何影响系统行为 | 设计Prompt对照实验 | P0 | L3 |
| Context | Context Management, State | 上下文注入与状态管理 | 分析上下文缺失/污染 | P0 | L3 |
| Tool Calling | Function Calling, Tool Schema | 模型如何选择和调用工具 | 验证工具选择和参数 | P0 | L3 |
| Memory | Short-term/Long-term Memory | 状态与记忆如何影响Agent | 分析记忆读写 | P1 | L2 |
| Environment | Environment, State Transition | Agent运行环境 | 设计环境状态测试 | P1 | L2 |
| 系统分层 | Model/Prompt/Context/Retrieval/Tool/Memory/Environment | 不同层的故障边界 | 做Root Cause Localization | P0 | L3 |
| Multimodal | Text/Image/Audio/Video | 多模态输入输出链路 | 定义多模态Eval Target | P1 | L2 |

---

# 三、Evaluation Science

## 06 Evaluation Fundamentals

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Evaluation Target | Capability, Behavior, Quality | 评什么必须先定义清楚 | 从业务目标拆Eval Target | P0 | L3 |
| Task/Case | Task, Eval Case | 单个评估问题/场景 | 编写Eval Task | P0 | L3 |
| Dataset | Dataset, Eval Set, Golden Set | 任务集合与黄金集 | 构建Golden Dataset | P0 | L3 |
| Benchmark | Benchmark, Protocol | 标准化比较方式 | 理解Benchmark设计 | P1 | L2 |
| Trial | Trial, Run | 单次执行与重复执行 | 实现多Trial | P0 | L3 |
| Ground Truth | Reference, Expected Output | 什么是可验证标准 | 建立Reference | P0 | L3 |
| Evaluation Suite | Suite, Capability Set | 按能力组织评估 | 设计Eval Suite | P1 | L3 |

### 核心区别

```text
Task / Eval Case = 一个评估问题
Dataset / Eval Set = 一组任务
Benchmark = 标准化的评估数据 + 协议 + 指标/比较方式
Evaluation Suite = 围绕能力/行为组织的一组评估
Trial / Run = 一次实际执行
```

## 07 Data Quality

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| 覆盖度 | Coverage | Dataset是否覆盖目标能力 | 做Coverage Matrix | P0 | L3 |
| 难度 | Difficulty | 简单题不能代表复杂能力 | 做Difficulty分层 | P0 | L3 |
| 平衡性 | Balance | 类别分布影响结果 | 检查类别比例 | P1 | L2 |
| 代表性 | Representativeness | Eval数据是否接近真实流量 | 做分布分析 | P0 | L3 |
| 歧义 | Ambiguity | 模糊题会污染指标 | 标记/清理Ambiguous Cases | P0 | L3 |
| 可解性 | Solvability | 无法回答的问题不应误判模型 | 做Solvability检查 | P0 | L3 |
| 污染 | Contamination, Leakage | Benchmark泄漏会导致虚高 | 检测数据污染 | P1 | L3 |
| 版本 | Dataset Versioning | 数据变更会影响结果 | 管理Dataset版本 | P0 | L3 |

## 08 Evaluation Methodology

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Rule Grader | Rule-based Grader | 确定性规则最可靠 | 编写规则Grader | P0 | L3 |
| Code Grader | Code-based Grader | 可执行验证优于主观判断 | 编写代码Grader | P0 | L3 |
| LLM Judge | Model-based Grader, LLM-as-a-Judge | 用模型评估开放式输出的边界 | 编写Judge + Rubric | P0 | L3 |
| Human Grader | Human Evaluation | 高价值主观问题需要人工 | 设计人工标注规范 | P1 | L3 |
| Pointwise | Pointwise Evaluation | 单结果绝对评分 | 实现评分Eval | P0 | L3 |
| Pairwise | Pairwise Evaluation | 两结果相对比较 | 实现A/B比较 | P0 | L3 |
| Listwise | Listwise Evaluation | 多结果排序 | 理解并实现基础排序 | P2 | L2 |
| Reference-based | Reference-based | 有标准答案的评估 | 实现Reference Grader | P0 | L3 |
| Reference-free | Reference-free | 没有标准答案时的评估 | 设计Judge Rubric | P1 | L3 |

**Grader原则：** 能用Rule验证，不要用LLM Judge；能执行验证，不要只看文本；主观开放问题，再考虑LLM Judge/Human。

## 09 Evaluation Science

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Sampling | Sampling, Representative Sample | 样本如何代表总体 | 设计采样方案 | P0 | L3 |
| Sample Size | Sample Size | 样本量影响结论稳定性 | 估算基础样本量 | P0 | L3 |
| Repeated Trials | Repeated Measures | AI输出具有随机性 | 运行多Trial | P0 | L3 |
| Variance | Variance | 结果波动 | 计算方差 | P0 | L3 |
| Standard Deviation | SD | 离散程度 | 计算/解释SD | P0 | L3 |
| Confidence Interval | CI | 结果不应只有单点 | 计算CI | P0 | L3 |
| Significance | Statistical Significance | 差异是否可能来自随机性 | 基础显著性检验 | P1 | L3 |
| Effect Size | Effect Size | 差异有多大 | 计算并解释Effect Size | P1 | L3 |
| Experimental Design | Controlled Experiment | 如何控制变量 | 设计模型/Prompt实验 | P0 | L3 |
| A/B Testing | A/B Test | 线上/离线版本比较 | 设计A/B评估 | P1 | L3 |
| Inter-rater Agreement | Cohen's Kappa, Agreement | 人工标注一致性 | 分析标注一致性 | P1 | L3 |

---

# 四、专项 Evaluation

## 10 LLM Evaluation

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Accuracy | Accuracy, Pass Rate | 基础正确率 | 实现Accuracy Grader | P0 | L3 |
| Error Rate | Error Rate | 错误类型与比例 | 统计错误分布 | P0 | L3 |
| Factuality | Hallucination | 事实性问题 | 构建事实性数据集 | P0 | L3 |
| Constraint Following | Constraint Satisfaction | 是否满足格式/约束 | 规则验证 | P0 | L3 |
| Robustness | Perturbation | 输入变化下的稳定性 | 做Prompt/Input变体 | P0 | L3 |
| Consistency | Multi-trial Consistency | 同题多次输出稳定性 | 统计多Trial | P0 | L3 |
| Judge Evaluation | Judge Agreement, Bias | Judge本身也需要评估 | 做Judge Calibration | P0 | L3 |

**实践要求：** Pointwise + Pairwise 两套评估方式，并支持重复Trial。

## 11 RAG Evaluation

```text
User Query
    ↓
Retrieval
    ├── Recall
    ├── Precision
    ├── Hit Rate
    ├── MRR
    └── NDCG
    ↓
Context
    ├── Context Recall
    ├── Context Precision
    ├── Context Relevance
    ├── Completeness
    ├── Noise
    └── Redundancy
    ↓
Generation
    ├── Faithfulness
    ├── Groundedness
    ├── Answer Relevance
    ├── Answer Correctness
    └── Completeness
    ↓
Final Answer
```

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Retrieval | Recall, Precision, Hit Rate | 检索是否找到正确文档 | 计算Retrieval指标 | P0 | L3 |
| Ranking | MRR, NDCG | 排序位置影响有效性 | 实现基础Ranking指标 | P0 | L3 |
| Context | Context Recall, Precision, Relevance | 找到不等于上下文可用 | 分析Context质量 | P0 | L3 |
| Noise | Noise, Redundancy, Completeness | 噪声会影响Generation | 构造Context质量测试 | P0 | L3 |
| Generation | Faithfulness, Groundedness | 答案是否基于Context | 实现Generation Eval | P0 | L3 |
| Answer | Correctness, Relevance, Completeness | 最终答案质量 | 构建E2E RAG Eval | P0 | L3 |
| Root Cause | Retrieval/Context/Generation Failure | 不同失败层不能混为一谈 | 定位RAG根因 | P0 | L4 |

**核心原则：** `Retrieval Failure ≠ Context Quality Failure ≠ Generation Failure ≠ E2E Answer Failure`。

## 12 Agent Architecture

```text
                    Goal
                     ↓
                  Planning
                     ↓
                 Decision
                     ↓
Observation ←──── Agent ────→ Action
    ↑                         ↓
    │                       Tool
    │                         ↓
    └──── Environment ←───────┘
               ↓
             State
               ↓
        State Transition
               ↓
            Outcome
```

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Goal | Goal, Task | Agent要完成什么 | 定义Agent任务 | P0 | L3 |
| Planning | Planning, Decomposition | 如何拆解任务 | 分析计划质量 | P0 | L3 |
| Decision | Policy, Decision | 下一步动作如何选择 | 分析Decision | P0 | L3 |
| Tool | Tool Calling, Tool Schema | 工具接口和能力边界 | 设计Tool Eval | P0 | L3 |
| State | State, Transition | Agent状态变化 | 记录State | P0 | L3 |
| Environment | Environment | 外部环境反馈 | 构建可控环境 | P1 | L3 |
| Memory | Working/Long-term Memory | 状态与历史信息 | 分析Memory依赖 | P1 | L3 |

## 13 Agent Evaluation

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Planning Quality | Plan Success, Decomposition | 计划是否有效 | 设计Planning Eval | P0 | L3 |
| Tool Selection | Tool Accuracy | 是否选对工具 | Rule/Code验证 | P0 | L3 |
| Arguments | Argument Correctness | 参数是否正确 | Schema/Value校验 | P0 | L3 |
| Tool Result | Result Handling | 能否正确处理工具结果 | 构造异常Result | P0 | L3 |
| Trajectory | Trajectory, Trace | 行为序列本身是重要证据 | 分析Trace | P0 | L4 |
| Outcome | Task Success, Goal Completion | 最终目标是否完成 | 构建Outcome Grader | P0 | L3 |
| Long Horizon | Long-horizon Task | 长链路错误累积 | 设计长任务Eval | P1 | L4 |
| Recovery | Retry, Recovery | 错误后能否恢复 | 构造故障环境 | P1 | L3 |
| Efficiency | Steps, Tokens, Latency, Cost | 成功不是唯一目标 | 统计效率指标 | P1 | L3 |
| Safety | Unsafe Action, Excessive Agency | Agent可执行性带来的风险 | 做Action Safety Eval | P0 | L3 |

**Agent Evaluation 必须同时关注 Outcome + Trace/Trajectory。** 最终成功不代表过程可靠。

## 14 Memory Evaluation

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Memory Recall | Recall | 是否正确记住信息 | 设计Recall Task | P1 | L3 |
| Memory Precision | Precision | 是否避免错误记忆 | 构造干扰信息 | P1 | L3 |
| Memory Update | Update/Overwrite | 新信息如何覆盖旧信息 | 测试更新行为 | P1 | L3 |
| Memory Isolation | Isolation | 用户/任务间不能串记忆 | 做Cross-session测试 | P0 | L3 |
| Memory Relevance | Relevance | 记忆是否真正有用 | 评估召回内容 | P1 | L3 |
| Memory Safety | Leakage, Privacy | 记忆可能造成数据泄漏 | 做敏感信息测试 | P0 | L3 |

## 15 Multimodal / Computer Use

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Vision | Image Understanding | 图像理解能力 | 设计视觉Eval | P0 | L3 |
| OCR | OCR Accuracy, CER, WER | 图像文字识别 | 构建OCR Dataset | P0 | L3 |
| Grounding | Bounding Box, Point, Grounding | 文本与视觉区域对应 | 评估Grounding | P0 | L3 |
| Screen Understanding | UI Element, Layout | GUI结构理解 | 构建Screen Eval | P0 | L3 |
| GUI Action | Click, Type, Scroll | 视觉到动作转换 | 测试Action Success | P0 | L3 |
| Computer Use | Computer-use Agent | Agent与真实GUI交互 | 构建Computer Use Eval | P1 | L3 |
| Audio/Video | ASR, VQA, Video Understanding | 多媒体评估基本范式 | 设计基础多模态Case | P1 | L2 |

## 16 Safety / Security

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Jailbreak | Jailbreak | 绕过安全限制的攻击 | 构建Jailbreak Eval | P0 | L3 |
| Prompt Injection | Direct Prompt Injection | 输入覆盖/操纵指令 | 构建Injection Cases | P0 | L3 |
| Indirect Injection | Indirect Prompt Injection | 外部内容也可能携带攻击指令 | 模拟恶意Context | P0 | L3 |
| Data Leakage | Sensitive Data Leakage | 模型/Agent可能泄漏数据 | 做泄漏测试 | P0 | L3 |
| Excessive Agency | Excessive Agency | Agent权限超过业务需要 | 做权限边界测试 | P0 | L3 |
| Tool Abuse | Tool Misuse | 工具调用可能成为攻击面 | 做Tool Abuse Eval | P0 | L3 |
| Privilege Escalation | Privilege Escalation | Agent权限提升风险 | 构造越权任务 | P1 | L3 |
| Safety Policy | Policy Compliance | 安全策略与业务规则 | 建立Safety Rubric | P0 | L3 |

## 17 Red Teaming

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Adversarial Testing | Adversarial Testing | 主动寻找系统失效点 | 设计攻击场景 | P0 | L3 |
| Attack Dataset | Attack Set | 攻击案例需要系统化积累 | 建立Attack Dataset | P0 | L3 |
| Attack Mutation | Mutation, Fuzzing | 单一攻击不能覆盖空间 | 实现变异策略 | P1 | L3 |
| Automated Attack | Automated Red Team | 自动化扩大攻击覆盖 | 构建攻击Runner | P1 | L3 |
| Safety Regression | Safety Regression | 安全修复可能回归 | 建立Safety Regression Suite | P0 | L3 |
| Human Red Team | Expert Testing | 高风险场景仍需专家 | 设计人工攻击流程 | P1 | L3 |

---

# 五、工程化与生产质量层

## 18 Reliability

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Stability | Stability | 同条件结果稳定性 | 多Trial统计 | P0 | L3 |
| Reliability | Reliability | 系统长期成功能力 | 建立Reliability指标 | P0 | L3 |
| Regression | Regression Eval | 新版本不能破坏已有能力 | 建Regression Suite | P0 | L4 |
| Stress | Stress Testing | 高负载/复杂任务下表现 | 设计Stress Eval | P1 | L3 |
| Drift | Model/Data/Behavior Drift | 生产行为可能变化 | 建立Drift检测 | P1 | L3 |
| Failure Rate | Failure Rate | 失败概率 | 统计Failure | P0 | L3 |
| Recovery | Recovery Rate | 失败后恢复能力 | 测试Retry/Recovery | P1 | L3 |

## 19 Evaluation Engineering

### 核心 Harness

```text
Dataset
   ↓
Runner
   ↓
Trial Executor
   ↓
Trace Collector
   ↓
Grader
   ↓
Metric Aggregator
   ↓
Statistical Analysis
   ↓
Report
```

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Runner | Evaluation Runner | 如何批量执行任务 | 自己实现Runner | P0 | L4 |
| Trial | Trial Executor | 单次运行与重试 | 实现Trial机制 | P0 | L4 |
| Grader Interface | Grader Contract | Grader需要统一接口 | 设计Grader抽象 | P0 | L4 |
| Metrics | Metric Aggregator | 单Case如何汇总为Suite指标 | 实现Metric层 | P0 | L4 |
| Trace | Trace Schema | Agent/RAG过程需要结构化记录 | 设计Trace Schema | P0 | L4 |
| Parallelism | Parallel Evaluation | 大规模Eval需要并发 | 实现并发Runner | P1 | L4 |
| Retry/Timeout | Retry, Timeout | 不稳定API不能阻塞整个Eval | 实现容错 | P0 | L4 |
| Versioning | Model/Prompt/Dataset Version | 结果必须可追溯 | 建版本记录 | P0 | L4 |
| Reproducibility | Seed, Config, Artifact | 实验需要复现 | 固化配置和Artifact | P0 | L4 |
| Reporting | Eval Report | 结果必须可解释 | 自动生成Report | P0 | L4 |

**目标：** 不依赖第三方框架，也能从 `Dataset → Runner → Trial → Trace → Grader → Metrics → Report` 跑通完整Evaluation Pipeline。

## 20 EvalOps / Toolchain

| 工具/能力 | 核心术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Python / pytest | Test Runner, Fixture, Parametrize | 传统测试工程能力如何迁移到Eval | 用pytest组织Eval | P0 | L4 |
| Promptfoo | Prompt Eval, Red Team | Prompt/Model批量比较 | 完成基础Eval | P1 | L2 |
| DeepEval | LLM Eval Framework | LLM指标与测试集 | 完成基础项目 | P1 | L2 |
| Ragas | RAG Evaluation | RAG指标体系 | 完成RAG Eval | P1 | L2 |
| TruLens | Feedback Functions | RAG/LLM反馈评估 | 理解核心范式 | P2 | L2 |
| LangSmith | Tracing, Dataset, Evaluation | Trace与Eval平台 | 完成基础Trace/Eval | P1 | L2 |
| Braintrust | Eval, Experiment, Trace | 实验管理 | 理解Eval workflow | P2 | L2 |
| Arize Phoenix | Observability, Tracing | LLM/RAG可观测性 | 完成基础观测 | P1 | L2 |
| W&B Weave | Tracing, Evaluation | 实验与评估 | 理解核心流程 | P2 | L2 |
| Label Studio | Annotation | 人工标注 | 建立标注任务 | P1 | L2 |

**原则：工具不是终点。** 必须理解工具背后的 Pipeline，并能自己实现核心Harness。

## 21 Meta-Evaluation

```text
System
   ↓
Evaluation
   ↓
Grader
   ↓
Metric
   ↓
结论
```

Meta-Evaluation 的核心问题：**我们的评估结果可信吗？**

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Eval Validity | Evaluation Validity | Eval是否真正测到了目标能力 | 做Validity分析 | P0 | L4 |
| Grader Reliability | Reliability | Grader是否稳定 | 重复评估Grader | P0 | L4 |
| Judge Calibration | Calibration | LLM Judge需要校准 | 用人工样本校准 | P0 | L4 |
| Human-Judge Agreement | Agreement | Judge与人工是否一致 | 计算Agreement | P0 | L4 |
| Inter-rater Agreement | Cohen's Kappa等 | 标注者是否一致 | 分析标注质量 | P1 | L3 |
| Statistical Power | Power | 实验是否有足够能力检测差异 | 做Power Analysis | P1 | L4 |
| Sample Size | Minimum Sample Size | 样本是否足够 | 估算Sample Size | P0 | L4 |
| Effect Size | Effect Size | 业务差异是否有实际意义 | 分析Effect Size | P1 | L4 |
| Eval Sensitivity | Sensitivity | Eval能否检测真实变化 | 做敏感性实验 | P0 | L4 |
| Rubric Ambiguity | Rubric Quality | 模糊标准会制造错误结论 | 优化Rubric | P0 | L4 |
| Judge Bias | Position/Verbosity/Style/Self-preference/Length Bias | LLM Judge并非中立 | 做Bias检测 | P0 | L4 |
| Judge Instability | Judge Variance | Judge自身也有随机性 | 多Trial验证Judge | P0 | L4 |

### LLM Judge 必须掌握的偏差

- Position Bias
- Verbosity Bias
- Style Bias
- Self-preference Bias
- Length Bias
- Judge Instability
- Rubric Ambiguity

## 22 Production Evaluation

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Online Evaluation | Online Eval | 线上系统不能只依赖离线Benchmark | 设计线上Eval | P0 | L4 |
| Production Trace | Production Trace | 真实行为需要可观测 | 采集并分析Trace | P0 | L4 |
| User Feedback | Feedback Loop | 用户反馈是质量信号 | 建立反馈数据 | P1 | L3 |
| Drift | Data/Model/Behavior Drift | 线上分布会变化 | 做Drift Detection | P1 | L4 |
| Continuous Evaluation | Continuous Eval | 每次变更都应自动评估 | 接入CI/CD | P0 | L4 |
| A/B Testing | Experimentation | 版本效果需要线上比较 | 设计A/B实验 | P1 | L4 |
| Monitoring | Quality Monitoring | 线上质量持续变化 | 建立Quality Dashboard | P0 | L4 |
| Release Gate | Quality Gate | Eval结果影响发布 | 实现自动Quality Gate | P0 | L4 |

## 23 AI Quality

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Quality Model | AI Quality Model | AI质量是多维度的 | 建立Quality Model | P0 | L4 |
| Quality Gate | Release Gate | 质量标准必须可执行 | 定义Gate | P0 | L4 |
| Model Validation | Model Validation | 模型变更需要系统验证 | 完成Model Validation | P0 | L4 |
| Failure Analysis | Failure Taxonomy | 失败需要分类 | 建立Failure Taxonomy | P0 | L4 |
| Root Cause Analysis | RCA | 找到错误发生层 | 完成Root Cause Analysis | P0 | L4 |
| Quality/Cost | Cost-Quality Trade-off | 质量提升有成本 | 做质量/成本分析 | P0 | L4 |
| Quality/Latency | Latency-Quality Trade-off | 延迟也是质量约束 | 做Latency分析 | P1 | L3 |
| Quality/Safety | Safety-Quality Trade-off | 质量不能脱离安全 | 做综合Quality Gate | P0 | L4 |

## 24 Business Alignment

| 二级能力 | 核心专业术语 | 必须理解 | 必须会做 | 优先级 | 深度 |
|---|---|---|---|---|---|
| Business Metric | Business KPI | 技术指标最终服务业务 | 将Eval连接业务KPI | P0 | L4 |
| Metric Alignment | Metric-to-Business Alignment | Eval指标不等于业务价值 | 建立指标映射 | P0 | L4 |
| User Satisfaction | CSAT, Task Success | 用户体验需要量化 | 设计用户质量指标 | P1 | L3 |
| Conversion | Conversion, Retention | AI能力可能影响业务结果 | 做关联分析 | P1 | L3 |
| Quality/Cost | Cost per Task, Token Cost | 质量提升必须考虑成本 | 建立单位任务成本 | P0 | L4 |
| Quality/Latency | Latency | 用户体验有延迟约束 | 建立SLO/SLA相关指标 | P1 | L3 |
| Risk | Business Risk, Model Risk | AI失败可能带来业务风险 | 建立风险分级 | P1 | L4 |
| Decision | Release Decision | Eval最终需要支持决策 | 输出Release Recommendation | P0 | L4 |

---

# 六、能力依赖关系

```text
01 AI / ML Fundamentals
        ↓
02 LLM Fundamentals
        ↓
03 LLM Behavior ─────→ 04 Reasoning
        ↓                    ↓
05 AI System Architecture ───┘
        ↓
06 Evaluation Fundamentals
        ↓
07 Data Quality
        ↓
08 Evaluation Methodology
        ↓
09 Evaluation Science
        ↓
 ┌──────┼────────┬─────────┐
 ↓      ↓        ↓         ↓
10 LLM  11 RAG   12 Agent  15 Multimodal
Eval     Eval     Arch      Eval
          ↓        ↓
          └────┬───┘
               ↓
        13 Agent Evaluation
               ↓
        14 Memory Evaluation

16 Safety ─→ 17 Red Teaming

18 Reliability
        ↓
19 Evaluation Engineering
        ↓
20 EvalOps / Toolchain
        ↓
21 Meta-Evaluation
        ↓
22 Production Evaluation
        ↓
23 AI Quality
        ↓
24 Business Alignment
```

---

# 七、Evaluation 生命周期

```text
Business Goal
     ↓
Define Capability
     ↓
Define Evaluation Target
     ↓
Design Task
     ↓
Build Dataset
     ↓
Validate Data Quality
     ↓
Define Rubric / Criteria
     ↓
Select Grader
     ↓
Build Evaluation Harness
     ↓
Run Trials
     ↓
Collect Output / Trace
     ↓
Grade
     ↓
Aggregate Metrics
     ↓
Statistical Analysis
     ↓
Root Cause Analysis
     ↓
Regression / Comparison
     ↓
Release Decision
     ↓
Production Monitoring
     ↓
Feedback
     ↓
New Evaluation Cases
     ↺
```

---

# 八、核心 Evaluation 原则

## 1. AI 是随机系统

传统测试经常假设：

```text
Input → Deterministic Output
```

AI Evaluation 更接近：

```text
Input + Model + Prompt + Context + Sampling
                    ↓
               Distribution
                    ↓
              Multiple Trials
                    ↓
             Statistical Result
```

因此必须掌握：**Repeated Trials、Variance、Confidence Interval、Effect Size、Statistical Significance**。

## 2. Capability Eval ≠ Regression Eval

- **Capability Evaluation：** 当前系统具备什么能力？
- **Regression Evaluation：** 新版本是否破坏已有能力？

二者的数据集、阈值和使用场景可以不同。

## 3. Agent Eval ≠ Model Eval

Agent Evaluation 评估的是：

```text
Model + Prompt + Tools + Memory + Environment + Harness
```

而不是单独评估模型。

## 4. Outcome ≠ Trace

Agent最终成功，不代表过程可靠；因此需要同时评估：

```text
Outcome
+
Trace / Trajectory
```

## 5. RAG 必须分层

```text
Retrieval Failure
≠ Context Quality Failure
≠ Generation Failure
≠ E2E Answer Failure
```

## 6. LLM Judge 不是天然可信

必须进行：

```text
Human Calibration
       ↓
Agreement Analysis
       ↓
Bias Detection
       ↓
Stability Test
       ↓
Judge Reliability
```

## 7. Meta-Evaluation 是 Evaluation 的质量保障

```text
System
  ↓
Eval
  ↓
Grader
  ↓
Metric
  ↓
Conclusion
```

如果Grader或Metric本身不可靠，最终结论也不可靠。

---

# 九、传统测试 → AI Evaluation 能力映射

| 传统软件测试 | AI Evaluation |
|---|---|
| Test Case | Evaluation Task |
| Test Suite | Evaluation Suite |
| Test Data | Evaluation Dataset |
| Expected Result | Ground Truth / Reference |
| Assertion | Grader |
| Test Execution | Trial |
| Test Report | Evaluation Report |
| Bug | Model / Prompt / RAG / Agent Failure |
| Regression Test | Regression Evaluation |
| UI Automation | Agent / Computer Use Evaluation |
| API Testing | LLM / Tool / API Evaluation |
| Performance Testing | Latency / Token / Cost Evaluation |
| Reliability Testing | Multi-trial / Stability Evaluation |
| Security Testing | AI Safety / Red Team |
| Monitoring | Production AI Evaluation |
| Test Framework | Evaluation Harness |
| CI/CD | Continuous Evaluation |
| QA | AI Quality Engineering |

### 你的传统能力如何迁移

已有能力：

```text
测试设计
自动化
Python
pytest
接口测试
Android / UI
性能测试
异常分析
工程化
```

需要新增：

```text
AI / ML Fundamentals
LLM Fundamentals
Reasoning
RAG
Agent
AI Evaluation
Evaluation Statistics
LLM Judge
Safety / Red Team
Evaluation Engineering
Meta-Evaluation
Production AI Quality
```

---

# 十、成熟度模型

| Level | 定义 | 能力表现 |
|---|---|---|
| L1 | 了解 | 能理解AI Evaluation概念、术语和常见指标 |
| L2 | 掌握 | 能独立设计Eval Case、Dataset、基础Grader |
| L3 | 熟练 | 能完成专项Evaluation和统计分析 |
| L4 | 工程化 | 能构建Evaluation Harness，完成RAG/Agent/Safety等系统评估 |
| L5 | 体系化 | 能建设Regression、EvalOps、Production Evaluation |
| L6 | AI Quality | 能完成Meta-Evaluation、Quality System和业务指标闭环 |

---

# 十一、优先级模型

## P0 — 必须掌握

01 AI/ML基础、02 LLM基础、03 LLM行为、04 Reasoning、05 AI System Architecture、06 Evaluation Fundamentals、07 Data Quality、08 Evaluation Methodology、09 Evaluation Science、10 LLM Evaluation、11 RAG Evaluation、12 Agent Architecture、13 Agent Evaluation、16 Safety/Security、18 Reliability、19 Evaluation Engineering、21 Meta-Evaluation、22 Production Evaluation、23 AI Quality、24 Business Alignment。

## P1 — 重点扩展

高级Planning、14 Memory Evaluation、15 Multimodal深度能力、17 Red Teaming、Drift、Online Evaluation、A/B Testing、Statistical Power、Observability、Advanced Judge Calibration、Business Experimentation。

## P2 — 高阶能力

Advanced Model Evaluation、Advanced Multimodal、Advanced Safety、Model Training Evaluation、Advanced Benchmark Design、Evaluation Platform Architecture、AI Governance、Model Risk Management。

---

# 十二、项目与能力对应关系

| 能力域 | 推荐实践项目 | 作品集证明 |
|---|---|---|
| LLM Evaluation | Pointwise + Pairwise Eval | LLM Evaluation Toolkit |
| Data Quality | Golden Dataset + Data Validator | Evaluation Dataset |
| Evaluation Science | Multi-trial + CI + Effect Size | Eval Statistics Module |
| RAG Evaluation | Retrieval + Generation Evaluation | RAG Evaluation Pipeline |
| Agent Evaluation | Trace Analyzer | Agent Evaluation Toolkit |
| Memory Evaluation | Memory Quality Eval | Agent Memory Evaluation |
| Safety | Jailbreak + Injection Dataset | Safety Evaluation Suite |
| Multimodal | OCR + Grounding Eval | Multimodal Evaluation |
| Computer Use | GUI Agent Eval | Computer Use Evaluation |
| Evaluation Engineering | Runner + Grader + Metrics | Evaluation Harness |
| EvalOps | Version + Regression + Dashboard | Eval Platform |
| Production | Online Eval + Drift | Production AI Quality System |

---

# 十三、最终作品集规模

目标不是只写Demo，而是完成一次接近真实工程规模的Evaluation实验：

```text
Model A
   ↓
Evaluation Harness
   ↓
1,000 Tasks
   ↓
5 Trials / Task
   ↓
5,000 Runs
   ↓
Multiple Graders
   ↓
Metrics
   ↓
Statistical Analysis
   ↓
Failure Clustering
   ↓
Root Cause
   ↓
Regression Report
```

最终能够回答：

1. 模型哪里好？
2. 模型哪里差？
3. 差多少？
4. 这个差异是否具有统计意义？
5. 差异来自Model、Prompt、Context、Retrieval、Tool、Memory还是Agent？
6. Grader本身可信吗？
7. 新版本是否Regression？
8. 线上质量是否发生Drift？
9. 质量、Latency、Token、Cost如何权衡？
10. 最终是否应该Release？

---

# 十四、最终成长路线

```text
传统测试工程师
      ↓
AI / ML Fundamentals
      ↓
LLM Fundamentals
      ↓
LLM Behavior
      ↓
Reasoning
      ↓
LLM Evaluation
      ↓
RAG Evaluation
      ↓
Agent Architecture
      ↓
Agent Evaluation
      ↓
Safety / Reliability
      ↓
Evaluation Engineering
      ↓
EvalOps
      ↓
Meta-Evaluation
      ↓
Production Evaluation
      ↓
AI Quality Engineer
```

---

# 十五、一句话定义

> **AI Evaluation Engineer = 用工程化、统计学和实验方法，对 AI 模型及 AI 应用系统的能力、质量、安全、可靠性和业务效果进行可重复、可量化、可验证的评估，并能够定位问题根因。**

---

# 十六、V2.1 相比 V2.0 的核心变化

```text
V2.0
= 我需要学什么？

V2.1
= 我需要学什么
+ 怎么评
+ 用什么方法评
+ 用什么工具
+ 怎么构建Eval
+ 怎么验证Eval可信
+ 怎么做统计分析
+ 怎么定位根因
+ 怎么进入生产
+ 怎么建立AI Quality
+ 怎么产生业务价值
```

**V2.1 的最终目标不是培养“会使用评测工具的人”，而是培养能够独立建立 AI Evaluation → AI Quality 完整质量体系的工程师。**
