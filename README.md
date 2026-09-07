# AI Evaluation Engineer

> 从传统软件测试出发，系统学习 AI Evaluation / AI Quality Engineering。
>
> **当前只学习第一阶段。** 其他阶段先明确路线，不提前展开。

## 这套学习路线解决什么问题

传统软件测试主要验证：

```text
需求 → 规则 → 代码 → 确定性行为 → Expected / Actual → Pass / Fail
```

AI 系统的核心链路则是：

```text
Data → Model → Training → Inference → Behavior → Evaluation
```

因此，AI Evaluation Engineer 不能只停留在：

- 会调用模型 API
- 会写 Prompt
- 会做功能测试

而需要逐步理解：

```text
AI 为什么能做这件事？
        ↓
模型为什么会产生这个结果？
        ↓
为什么会错？
        ↓
怎么证明它变好了？
        ↓
怎么持续验证？
```

---

# 学习总路线

整个路线分为 **9 个阶段**。现在只打开第一阶段，后续阶段按顺序学习。

| 阶段 | 学习主题 | 这一阶段要解决的问题 |
|---|---|---|
| **01** | **AI / ML 基础** | AI、ML、DL 到底是什么？模型如何从数据中学习？为什么会犯错？ |
| **02** | **LLM 基础** | Token、Embedding、Transformer、Attention、LLM 到底是什么？ |
| **03** | **LLM Inference & Behavior** | 模型如何生成答案？Context、Decoding、Temperature、Top-p 如何影响结果？为什么同一个问题可能得到不同答案？ |
| **04** | **LLM Reasoning & AI System** | 推理、Planning、Reflection、Context Management，以及一个 LLM 应用是如何工作的？ |
| **05** | **RAG & Agent** | Retrieval、Tool Use、Function Calling、Memory、Trajectory、Agent Loop、Long Horizon 是什么？ |
| **06** | **AI Evaluation** | 什么叫“好”？如何设计 Dataset、Ground Truth、Grader、Metric 和 Evaluation？ |
| **07** | **专项 Evaluation** | LLM、RAG、Agent、多模态、安全、可靠性分别怎么评测？ |
| **08** | **Evaluation Engineering** | 如何把评测做成 Dataset、Runner、Grader、Report、Regression 等工程系统？ |
| **09** | **Production AI Quality** | 如何进行线上评测、质量监控、Drift、Regression、业务指标关联和持续质量治理？ |

最终形成：

```text
AI / ML 基础
    ↓
LLM 基础
    ↓
Inference / Behavior
    ↓
Reasoning / AI System
    ↓
RAG / Agent
    ↓
Evaluation
    ↓
Evaluation Engineering
    ↓
Production AI Quality
```

---

# Phase 01：AI / ML 基础

## 这一阶段的目标

这一阶段**不是学算法，也不是为了成为机器学习算法工程师**。

目标只有一个：

> **真正理解“模型是如何学习、如何产生预测、为什么会犯错，以及为什么需要 Evaluation”。**

你需要把传统测试工程师的思维从：

```text
输入 → 代码 → 输出 → 判断对错
```

升级成：

```text
数据
 ↓
模型
 ↓
训练
 ↓
预测
 ↓
误差
 ↓
参数更新
 ↓
再次训练
 ↓
验证 / 测试
 ↓
泛化
 ↓
评估
```

---

## 01. AI、ML、DL 到底是什么

先建立最基本的概念关系：

```text
AI
└── Machine Learning
    └── Deep Learning
        └── Neural Network
```

需要理解：

- AI 是什么
- Machine Learning 是什么
- Deep Learning 是什么
- Neural Network 是什么
- 规则系统与机器学习有什么本质区别
- 为什么机器学习不是简单的“写更多 if/else”

### 学完要能回答

> 如果一个系统以前靠人工写规则判断垃圾短信，现在改成模型根据历史数据自动判断，这个“学习”到底发生在哪里？

---

## 02. Dataset：模型到底从什么东西学习

理解机器学习之前，先理解 **Data**。

重点学习：

- Dataset
- Sample
- Feature
- Label
- Training Set
- Validation Set
- Test Set
- 数据分布
- 数据质量
- 数据偏差

建立最简单的认知：

```text
Dataset
   ↓
输入 X + 正确答案 Y
   ↓
模型学习 X 与 Y 之间的关系
```

例如：

```text
输入：恭喜中奖100万
Label：垃圾
```

这里真正重要的不是这句话，而是：

> **模型为什么需要大量这样的“输入 + 正确答案”？**

---

## 03. Model：模型到底是什么

不要把 Model 理解成一个黑盒 API。

需要理解：

- Model 是什么
- Parameter 是什么
- Feature 与 Parameter 的区别
- 模型为什么可以表示复杂关系
- 模型为什么不是一套固定业务规则
- 模型输入、模型内部状态、模型输出之间的关系

建立这个核心认知：

```text
Input
  ↓
Model
  ↓
Prediction
```

模型本质上是在学习一个从输入到输出的映射。

---

## 04. Prediction：模型为什么会预测错

开始真正理解 AI 的“不确定性”。

例如：

```text
输入：恭喜中奖100万

模型预测：
正常 60%
垃圾 40%
```

正确答案：

```text
垃圾
```

于是出现：

```text
Prediction ≠ Label
```

需要理解：

- Prediction
- Probability / Score
- Classification
- Regression
- Error
- Incorrect Prediction

这里要建立一个非常重要的测试认知：

> **AI 的错误不是传统程序那种简单的“代码执行错了”，而是模型对输入做出了错误判断。**

---

## 05. Loss / Error：模型怎么知道自己错了

这是第一阶段最关键的知识之一。

理解：

```text
Prediction
    ↓
与正确答案比较
    ↓
Error / Loss
```

例如：

```text
正确答案 = 垃圾
模型预测 = 正常 60% / 垃圾 40%
                ↓
              Loss
```

需要理解：

- Error
- Loss
- 为什么需要 Loss Function
- Loss 大意味着什么
- Loss 小意味着什么
- 为什么 Loss 能用于训练模型

暂时**不要求深入数学推导**，先搞懂因果关系。

---

## 06. Parameter Update：模型到底怎么“学会”

这是理解 Machine Learning 的核心。

完整过程：

```text
输入数据
  ↓
模型预测
  ↓
计算 Loss
  ↓
根据 Loss 调整 Parameters
  ↓
再次预测
  ↓
再次计算 Loss
  ↓
继续调整
```

这就是“学习”的核心过程。

需要知道这些词是什么意思：

- Parameter
- Optimization
- Gradient
- Gradient Descent
- Learning Rate
- Backpropagation

第一阶段只要求建立**概念级因果链**，不是马上手算梯度。

---

## 07. Training：模型是怎么训练出来的

把前面的知识串起来：

```text
Dataset
   ↓
Training
   ↓
Prediction
   ↓
Loss
   ↓
Parameter Update
   ↓
Training Loop
   ↓
Better Model
```

需要理解：

- Training 是什么
- Batch
- Epoch
- Training Loop
- Optimization
- 为什么训练不是“一次完成”
- 为什么模型训练时间可能非常长

最终能够解释：

> 一个模型从数据到能够进行预测，中间到底发生了什么？

---

## 08. Validation / Test：模型训练得好就代表好了吗

这里正式进入**测试工程师最应该关注的问题**。

模型可能出现：

```text
训练数据表现很好
        ↓
真实数据表现很差
```

需要理解：

- Training Set
- Validation Set
- Test Set
- 为什么不能只看 Training Loss
- 为什么需要独立 Test Set
- 什么叫 Generalization

核心问题：

> **模型是在“学习规律”，还是只是“记住了训练数据”？**

---

## 09. Generalization：为什么模型学会了却不会做

理解机器学习最重要的现象之一：

```text
训练数据
  ↓
模型表现很好

新数据
  ↓
模型表现变差
```

重点理解：

- Generalization
- Overfitting
- Underfitting
- Bias / Variance 的基本概念
- 为什么训练集高分不代表真实世界高质量

这会直接连接到以后学习的：

```text
LLM Evaluation
RAG Evaluation
Agent Evaluation
Production AI Quality
```

---

## 10. Distribution Shift：真实世界为什么会让模型失效

训练数据和真实世界的数据可能不同：

```text
Training Distribution
        ↓
      Model
        ↓
Real-world Distribution
```

需要理解：

- Distribution
- Distribution Shift
- Data Drift
- Concept Drift 的基本概念
- 为什么线上模型可能越来越差

这是以后学习 **Production AI Quality** 的基础。

---

## 11. Data Leakage / Test Contamination：为什么测试结果可能是假的

需要理解两个重要问题：

### Data Leakage

测试信息不应该提前进入训练过程，却被模型间接获得。

### Test Contamination

模型在训练或其他过程中已经接触过测试内容，导致测试结果虚高。

核心认知：

> **测试数据不再独立，Evaluation 就可能失去可信度。**

这会直接连接到后面的 Evaluation Dataset 设计。

---

## 12. 从 Machine Learning 走向 Evaluation

第一阶段最后把所有知识串起来：

```text
Dataset
   ↓
Model
   ↓
Training
   ↓
Inference / Prediction
   ↓
Error
   ↓
Loss
   ↓
Parameter Update
   ↓
Better Model
   ↓
Validation / Test
   ↓
Generalization
   ↓
Distribution Shift
   ↓
Evaluation
```

最终要理解一个非常重要的问题：

> **为什么 AI 系统不能只说“能运行”，而必须讨论“质量”？**

因为 AI 的核心不是：

```text
能不能执行
```

而是：

```text
结果是否正确？
是否稳定？
是否能泛化？
在什么数据上会失败？
失败概率是多少？
```

这就是从**传统软件测试**进入 **AI Evaluation** 的第一座桥梁。

---

# Phase 01 学习完成标准

完成第一阶段后，不要求你会训练大型模型，但必须能够不用背稿解释清楚：

1. AI、ML、DL 分别是什么。
2. Dataset、Label、Model、Parameter 分别是什么。
3. 模型为什么需要 Training。
4. Prediction 为什么会错。
5. Loss 为什么能够帮助模型学习。
6. Parameter Update 在做什么。
7. Training Loop 是什么。
8. Training / Validation / Test 有什么区别。
9. 什么是 Generalization。
10. 什么是 Overfitting。
11. 什么是 Distribution Shift。
12. 为什么 Data Leakage / Test Contamination 会让评测结果失真。
13. 为什么 AI 系统最终必须进入 Evaluation。

如果这些问题还不能用自己的话讲清楚，**就不要进入 Phase 02。**

---

# 后续阶段怎么进入

当前只学习：

```text
Phase 01
AI / ML 基础
```

之后按照这个顺序继续：

```text
Phase 01  AI / ML 基础
   ↓
Phase 02  LLM 基础
   ↓
Phase 03  LLM Inference & Behavior
   ↓
Phase 04  LLM Reasoning & AI System
   ↓
Phase 05  RAG & Agent
   ↓
Phase 06  AI Evaluation
   ↓
Phase 07  专项 Evaluation
   ↓
Phase 08  Evaluation Engineering
   ↓
Phase 09  Production AI Quality
```

**现在不展开后面的课程，只保留路线。学习完成 Phase 01 后，再进入 Phase 02。**

---

## 学习原则

每一个阶段都不采用“看概念 → 打勾”的方式，而采用：

```text
理解概念
  ↓
理解为什么存在
  ↓
看具体例子
  ↓
自己做实验
  ↓
观察结果
  ↓
解释结果
  ↓
分析失败
  ↓
形成自己的认知
```

最终目标不是“知道 AI 有哪些名词”，而是能够站在测试工程师的角度回答：

> **AI 系统为什么这样工作？为什么会失败？我如何用工程和数据证明它到底好不好？**
