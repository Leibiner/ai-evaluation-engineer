# AI Evaluation Engineer

> 从传统软件测试出发，系统学习 AI Evaluation / AI Quality Engineering。
>
> **当前只学习第一阶段。** 其他阶段先明确路线，不提前展开。

## 这套学习路线解决什么问题

传统软件测试主要验证：

```text
需求 → 规则 → 代码 → 确定性行为 → Expected / Actual → Pass / Fail
```

AI 系统则需要进一步理解：

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
| **01** | **AI / ML 基础** | AI、ML、DL 到底是什么？数据、模型、训练、预测、错误和泛化之间是什么关系？ |
| **02** | **LLM 基础** | Token、Embedding、Transformer、Attention、LLM 到底是什么？ |
| **03** | **LLM Inference & Behavior** | 模型如何生成答案？Context、Decoding、Temperature、Top-p 如何影响结果？为什么同一个问题可能得到不同答案？ |
| **04** | **LLM Reasoning & AI System** | Reasoning、Planning、Reflection、Context Management，以及一个 LLM 应用如何工作？ |
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

## 一、这一阶段的目标

这一阶段**不是为了成为算法工程师**，而是为后面的 LLM、Reasoning、RAG、Agent 和 Evaluation 建立底层认知。

目标只有一个：

> **真正理解模型如何从数据中学习、如何产生预测、为什么会犯错，以及为什么需要 Evaluation。**

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

# 二、第一阶段学习内容

## 01. AI、ML、DL 到底是什么

先建立 AI 世界的基本地图：

```text
AI
└── Machine Learning
    └── Deep Learning
        └── Neural Network
```

进一步知道：

```text
Neural Network
      ↓
Transformer
      ↓
现代 LLM 的主要基础架构
      ↓
GPT / Claude / Qwen 等模型家族
```

这里重点学习：

- AI 是什么
- Machine Learning 是什么
- Deep Learning 是什么
- Neural Network 是什么
- 规则系统与机器学习有什么区别
- 为什么机器学习不是简单地写更多 if/else
- 模型和传统程序有什么区别

### 学完要能回答

> 如果一个系统以前靠人工规则判断垃圾短信，现在改成模型根据历史数据自动判断，这个“学习”到底发生在哪里？

---

## 02. Dataset：模型到底从什么东西学习

机器学习不是凭空产生能力，它需要数据。

重点学习：

- Dataset
- Sample
- Feature
- Input
- Label
- Training Set
- Validation Set
- Test Set
- 数据分布
- 数据质量
- 数据偏差

建立最基本的认知：

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

关键不是记住这个例子，而是理解：

> **模型为什么需要大量这样的“输入 + 正确答案”？**

---

## 03. Label / Annotation：正确答案从哪里来

这一部分单独学习，因为后面的 AI Evaluation 会大量使用：

```text
Label
Annotation
Ground Truth
Reference
Human Evaluation
```

例如：

```text
Input：
“恭喜中奖100万”

Ground Truth：
垃圾
```

模型可能预测：

```text
正常：60%
垃圾：40%
```

于是：

```text
Prediction ≠ Ground Truth
```

需要理解：

- Label
- Ground Truth
- Annotation
- Human Annotation
- Label Quality
- Label Noise
- 标注一致性

并建立与传统测试的对应关系：

```text
传统测试：Expected Result
AI：       Ground Truth / Reference
```

---

## 04. Model：模型到底是什么

不要把 Model 理解成一个黑盒 API。

需要理解：

- Model 是什么
- Parameter 是什么
- Weight / Bias 是什么
- Feature 与 Parameter 的区别
- Model Architecture 是什么
- 模型为什么可以表示复杂关系
- 模型为什么不是一套固定业务规则

建立核心认知：

```text
Input
  ↓
Model
  ↓
Prediction
```

模型本质上是一个通过参数表达规律的计算系统。

---

## 05. Prediction / Inference：模型如何得到结果

开始理解模型真正运行时发生了什么：

```text
Input
 ↓
Model
 ↓
Inference
 ↓
Prediction
```

例如：

```text
输入：恭喜中奖100万

模型预测：
正常 60%
垃圾 40%
```

最终模型可能选择：

```text
Prediction = 正常
```

但：

```text
Ground Truth = 垃圾
```

于是：

```text
Prediction ≠ Ground Truth
```

需要理解：

- Prediction
- Probability / Score
- Classification
- Regression
- Error
- Incorrect Prediction
- Training 与 Inference 的区别

核心认知：

> **训练是让模型学习参数；Inference 是训练完成后使用模型产生输出。**

---

## 06. Loss / Error：模型怎么知道自己错了

模型预测错了，需要一种方式量化错误。

核心链路：

```text
Prediction
    ↓
与 Ground Truth 比较
    ↓
Error / Loss
```

例如：

```text
Ground Truth = 垃圾
Prediction = 正常 60% / 垃圾 40%
                ↓
              Loss
```

需要理解：

- Error
- Loss
- Loss Function
- 为什么需要 Loss Function
- Loss 大意味着什么
- Loss 小意味着什么
- 为什么 Loss 可以用于训练模型

第一阶段暂时**不要求大量数学推导**，先搞懂因果关系。

注意：不是“系统口头告诉模型你错了”，而是训练数据提供 Target / Label，Loss Function 对 Prediction 与 Target 进行计算，再用于后续优化。

---

## 07. Optimization：模型怎么根据错误改进

有了 Loss，接下来解决：

> **模型怎么变得更好？**

核心链路：

```text
Prediction
    ↓
Loss
    ↓
Gradient
    ↓
Parameter Update
    ↓
新的 Model
```

需要知道：

- Gradient
- Gradient Descent
- Optimizer
- Learning Rate
- Parameter Update
- Backpropagation

第一阶段只要求理解概念级因果链，不要求马上手算复杂梯度。

---

## 08. Training：模型到底怎么训练出来

把前面的知识串起来：

```text
Dataset
   ↓
Input + Label
   ↓
Model
   ↓
Prediction
   ↓
Loss
   ↓
Backpropagation
   ↓
Parameter Update
   ↓
Repeat
```

需要理解：

- Training
- Training Loop
- Epoch
- Batch
- Iteration / Step
- Forward Pass
- Backward Pass
- Backpropagation
- Optimizer
- Learning Rate
- 为什么训练不是一次完成

最终能够解释：

> **一个模型从数据到能够进行预测，中间到底发生了什么？**

---

## 09. Validation / Test：训练得好就代表好吗

模型可能出现：

```text
训练数据表现很好
        ↓
真实数据表现很差
```

因此需要：

```text
Training Set
     ↓
训练模型

Validation Set
     ↓
选择 / 调整模型

Test Set
     ↓
最终验证
```

需要理解：

- Training Set
- Validation Set
- Test Set
- 三者的区别
- 为什么不能只看 Training Loss
- 为什么需要独立 Test Set
- 为什么测试集应该尽量独立

这一步开始正式连接你的传统测试经验。

---

## 10. Generalization：为什么模型学会了却不会做

模型可能：

```text
Training Accuracy = 99%
```

但：

```text
真实数据 Accuracy = 70%
```

因为模型可能只是记住了训练数据，而没有真正学会可泛化的规律。

重点学习：

- Generalization
- Overfitting
- Underfitting
- Bias / Variance 的基本概念
- 为什么训练集高分不代表真实世界质量高

核心认知：

> **模型在已知数据上表现好，不代表在未知数据上表现好。**

---

## 11. Distribution Shift：真实世界为什么会让模型失效

训练数据和真实世界的数据可能发生变化：

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

这会直接连接后面的 Production AI Quality。

---

## 12. Data Leakage / Test Contamination：为什么测试结果可能是假的

需要理解两个问题：

### Data Leakage

测试信息或未来信息不应该提前进入训练过程，却被模型间接获得。

### Test Contamination

模型在训练或其他过程中已经接触测试内容，导致测试结果虚高。

核心认知：

> **测试数据不再独立，Evaluation 就可能失去可信度。**

这会直接连接后面的 Evaluation Dataset 设计。

---

# 三、第一阶段必须形成的一条主线

学完以上内容，你脑子里不能是 12 个孤立的知识点，而应该形成这一条完整因果链：

```text
AI
 ↓
Machine Learning
 ↓
Dataset
 ↓
Input + Label
 ↓
Model
 ↓
Training
 ↓
Prediction / Inference
 ↓
Error
 ↓
Loss
 ↓
Gradient / Optimization
 ↓
Parameter Update
 ↓
Training Loop
 ↓
Validation / Test
 ↓
Generalization
 ↓
Distribution Shift
 ↓
Evaluation
```

这条链是第一阶段最重要的学习成果。

---

# 四、第一阶段完成标准

完成 Phase 01 后，不要求你成为算法工程师，也不要求你能够从零训练大型模型。

但必须能够不用背稿解释清楚：

1. AI、ML、DL 分别是什么。
2. Dataset、Sample、Feature、Label 分别是什么。
3. Ground Truth 和 Annotation 是什么。
4. Model 和 Parameter 是什么。
5. Training 和 Inference 有什么区别。
6. Prediction 为什么会错。
7. Loss 为什么能够帮助模型学习。
8. Gradient、Optimization、Parameter Update 在做什么。
9. Training Loop 是什么。
10. Training / Validation / Test 有什么区别。
11. 什么是 Generalization。
12. 什么是 Overfitting / Underfitting。
13. 什么是 Distribution Shift。
14. 为什么 Data Leakage / Test Contamination 会让评测结果失真。
15. 为什么 AI 系统最终必须进入 Evaluation。

### 最终能力标准

给你一个 AI 问题，例如：

> “为什么这个模型把‘恭喜中奖100万’判断成正常？”

你应该能够从：

```text
Data
 ↓
Label
 ↓
Model
 ↓
Training
 ↓
Parameters
 ↓
Inference
 ↓
Prediction
 ↓
Error / Loss
 ↓
Generalization
 ↓
Evaluation
```

逐层分析可能原因，而不是简单回答：

> “模型有 Bug。”

**如果这套能力还没有建立，就不要进入 Phase 02。**

---

# 五、后续学习路线

当前只学习：

```text
Phase 01
AI / ML 基础
```

之后严格按照依赖关系继续：

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

> **当前仓库只维护第一阶段的详细学习内容。后续阶段先定义路线，等第一阶段完成后再逐阶段展开。**
