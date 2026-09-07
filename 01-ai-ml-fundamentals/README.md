# 01 AI / ML Fundamentals

> **从传统软件测试工程师进入 AI Evaluation 的第一阶段：先建立 AI 技术地图，再理解模型为什么会产生行为。**

本章不是为了把学习者培养成算法工程师，而是解决一个更基础的问题：

> **AI 系统和传统软件到底有什么不同？模型为什么能“学习”？这些差异为什么会改变测试与质量工程的方法？**

---

## 一、这一章的学习目标

学完本章，不要求能够训练一个大模型，但必须能够：

1. 说清楚 **AI、ML、DL、Neural Network、Transformer、LLM** 分别是什么，以及它们之间的关系。
2. 理解传统规则驱动软件与机器学习系统的核心区别。
3. 用一个简单分类问题解释 **Dataset → Label → Prediction → Error/Loss → Parameter Update → Training** 的基本学习闭环。
4. 理解神经网络在深度学习中的位置，不把“深度学习”“神经网络”“Transformer”“LLM”混为一谈。
5. 理解 **Training / Validation / Test** 为什么需要分离，以及模型为什么会出现过拟合与泛化问题。
6. 初步理解 **Distribution Shift / Data Leakage / Contamination** 为什么会影响评估可信度。
7. 从测试工程师视角理解：AI 测试为什么不能只依赖 `Expected == Actual`，而需要逐渐进入 **Evaluation**。

---

# 二、学习路线

这一章按照“先建立地图 → 再理解学习 → 最后连接测试”的顺序学习，不提前跳进复杂数学公式。

```text
01. AI 到底是什么？
        ↓
02. 传统程序 vs Machine Learning
        ↓
03. ML 到底是怎么“学习”的？
        ↓
04. Dataset / Label / Model / Prediction
        ↓
05. Loss / Parameter / Training Loop
        ↓
06. Deep Learning / Neural Network
        ↓
07. Transformer 到底处于什么位置？
        ↓
08. LLM 是什么？
        ↓
09. Training / Validation / Test
        ↓
10. Generalization / Overfitting / Underfitting
        ↓
11. Distribution Shift / Leakage / Contamination
        ↓
12. 为什么 AI 改变了测试？
        ↓
13. 从 Testing 进入 Evaluation
```

---

# 三、Lesson 01：AI、ML、DL 到底是什么？

## 必须理解

建立第一张 AI 技术地图：

```text
AI
│
├── 传统 AI 方法
│
└── Machine Learning
      │
      ├── 传统机器学习
      │
      └── Deep Learning
             │
             └── Neural Network
                    │
                    ├── CNN
                    ├── RNN
                    └── Transformer
                           │
                           └── 现代 LLM 的重要技术基础
```

必须明确：

- AI 是大的领域，不等于 ChatGPT。
- ML 是让机器从数据中学习规律的一类方法。
- DL 是机器学习的重要分支，主要利用深度神经网络学习复杂表示。
- Neural Network 是模型结构家族。
- Transformer 是一种神经网络架构。
- LLM 是大语言模型这一类模型；现代主流 LLM 大多以 Transformer 为重要基础，但 **LLM ≠ Transformer**。

## 测试工程师视角

传统软件更接近：

```text
Input
  ↓
Human-written Rules
  ↓
Code
  ↓
Expected Output
```

机器学习系统则更接近：

```text
Dataset
  ↓
Training
  ↓
Model
  ↓
Inference
  ↓
Output
  ↓
Evaluation
```

第一课的最终认知不是背概念，而是理解：

> **当系统的行为来自模型学习，而不是完全来自人工编写的规则，测试对象和测试方法就会发生变化。**

---

# 四、Lesson 02：Dataset——AI 为什么这么依赖数据？

## 必须理解

从第一课的分类例子继续向下拆：

```text
Dataset
├── Input / Feature
├── Label
├── Training Set
├── Validation Set
└── Test Set
```

重点理解：

- 什么是样本、特征、标签。
- 什么是监督学习。
- 为什么数据质量会直接影响模型质量。
- 为什么训练集、验证集、测试集不能随意混用。
- 什么是数据泄漏。
- 什么是数据污染（Contamination）。
- 为什么测试数据必须尽可能代表真实任务。

## 测试工程师视角

开始建立一个核心意识：

> **如果 Dataset 有问题，模型测试结果可能从一开始就是不可信的。**

---

# 五、Lesson 03：Model——模型到底是什么？

## 必须理解

模型不要再理解成一个神秘的“黑盒”。需要建立：

```text
Input
  ↓
Model
  ↓
Prediction
```

以及：

```text
Model
=
Parameters + Structure + Learned Relationship
```

重点理解：

- Parameter / Weight 是什么。
- Model 为什么能够表达输入与输出之间的关系。
- Classification / Regression 的基本区别。
- 为什么模型大小、参数量与能力不能简单画等号。

## 测试工程师视角

开始从“接口返回了什么”升级到：

> **这个输出是模型能力、数据、Prompt、上下文还是其他系统组件造成的？**

---

# 六、Lesson 04：Training——模型到底是怎么学会的？

这是本章最重要的基础之一。

用最简单的分类问题理解训练闭环：

```text
Training Data
      ↓
Model Prediction
      ↓
Compare with Label
      ↓
Loss / Error
      ↓
Parameter Update
      ↓
New Prediction
      ↓
Repeat
```

例如：

```text
输入：恭喜中奖100万

第一次预测：
正常 60%
垃圾 40%

真实标签：
垃圾

        ↓

计算误差
        ↓

调整参数
        ↓

再次预测

正常 2%
垃圾 98%
```

这里需要理解：

- Prediction
- Label
- Loss
- Parameter
- Optimization
- Training Loop

不要求第一阶段掌握复杂梯度公式，但必须知道“模型为什么会改变”。

---

# 七、Lesson 05：Validation / Test——模型怎么知道自己学得好不好？

训练集表现好，不代表模型真的好。

建立基本分层：

```text
Training Set
    ↓
用于学习参数

Validation Set
    ↓
用于模型/超参数选择

Test Set
    ↓
用于最终、相对独立的泛化评估
```

重点理解：

- 为什么不能只看 Training Accuracy。
- 为什么需要独立 Test Set。
- 为什么反复使用 Test Set 也可能导致评估污染。
- Benchmark 为什么需要明确的数据、协议和指标。

---

# 八、Lesson 06：Generalization——为什么模型“学会了”却不会做？

这是从机器学习进入 Evaluation 的关键一步。

重点理解：

```text
Training Performance
        ≠
Real-world Performance
```

核心概念：

- Generalization
- Overfitting
- Underfitting
- Bias / Variance 的基础直觉
- Train / Validation / Test Gap

用测试工程师语言理解：

> **模型在你准备好的测试题上表现很好，不代表它在真实用户场景里也好。**

---

# 九、Lesson 07：Distribution Shift——为什么线上和测试环境会不一样？

模型训练和测试时看到的数据，与真实世界可能存在差异。

```text
Training Distribution
        ↓
       Model
        ↓
Test Distribution
        ↓
Production Distribution
```

重点理解：

- Distribution
- Distribution Shift
- Out-of-Distribution（OOD）
- Data Drift 的基础概念
- 为什么线上数据变化会导致模型能力下降。

测试工程师开始需要问：

> **我们的 Eval Set 到底能不能代表真实用户？**

---

# 十、Lesson 08：Data Leakage / Contamination——为什么“高分”也可能是假的？

重点理解两类典型问题：

### Data Leakage

不应该被模型看到的信息进入了训练或评估流程，导致结果虚高。

### Benchmark Contamination

评估数据或其高度相似内容进入了模型训练数据，使模型可能“见过题”，从而导致 Benchmark 分数不能代表真正的泛化能力。

测试工程师需要学会：

```text
高分
 ↓
是真的能力提升？
还是
 ↓
数据泄漏 / 污染 / 评估设计问题？
```

---

# 十一、Lesson 09：为什么 AI 改变了传统测试？

这是本章从“AI 基础”进入“AI Evaluation”的桥梁。

传统软件：

```text
Input
 ↓
Code
 ↓
Expected
 ↓
Actual
 ↓
PASS / FAIL
```

AI 系统：

```text
Input
 ↓
Model / Prompt / Context / Tool
 ↓
Output
 ↓
Evaluation Criteria
 ↓
Score / Judgment
```

原因包括：

- 输出可能不是唯一正确答案。
- 输出具有概率性和随机性。
- 同一个任务可能存在多个合理答案。
- 模型可能出现幻觉。
- 模型能力具有任务和数据分布依赖。
- 模型升级可能提升一个能力、损害另一个能力。

因此测试开始从：

> **“结果是不是等于 Expected？”**

逐渐走向：

> **“这个结果是否满足我们定义的质量标准？”**

---

# 十二、Lesson 10：从 Testing 进入 Evaluation

这一节只做概念上的收口，不提前进入完整 Evaluation Science。

建立最基本的 Evaluation 思维：

```text
Capability
   ↓
Evaluation Target
   ↓
Eval Task
   ↓
Dataset
   ↓
Trial
   ↓
Output
   ↓
Grader
   ↓
Metric
   ↓
Conclusion
```

例如一个 LLM 的回答，不一定要求与标准答案逐字一致，而可以评价：

- Correctness
- Relevance
- Completeness
- Faithfulness
- Safety
- Robustness

这里的目的不是马上学会设计完整 Eval Harness，而是先建立一个关键认知：

> **AI 的质量不是“看一眼输出觉得还行”，而应该通过明确的任务、数据、标准、指标和实验得到证据。**

---

# 十三、本章不要求学习什么

为了防止学习路线再次发散，本章明确不提前深入：

- Transformer 数学公式
- Attention 矩阵计算
- Embedding
- Tokenization
- RLHF / DPO
- LoRA / PEFT
- RAG
- Agent
- LLM-as-a-Judge
- Evaluation Harness
- 复杂统计学

这些内容放到后续能力域。

本章只负责建立：

```text
AI
 ↓
ML
 ↓
DL
 ↓
Model
 ↓
Training
 ↓
Evaluation
```

以及最重要的一条因果链：

```text
数据
 ↓
训练
 ↓
模型
 ↓
模型行为
 ↓
泛化
 ↓
评估
```

---

# 十四、最终学习出口

完成本章后，应该能够不用背稿回答下面的问题：

### 基础概念

1. AI、ML、DL 有什么关系？
2. Neural Network 是什么？
3. Transformer 是什么？为什么它和 LLM 有关？
4. LLM 和 Transformer 是不是一回事？

### 模型学习

5. 模型到底是怎么“学习”的？
6. Dataset、Label、Model、Prediction、Loss、Parameter 分别是什么？
7. Training、Validation、Test 为什么要分开？
8. 什么是 Overfitting？
9. 什么是 Generalization？
10. 什么是 Distribution Shift？
11. 什么是 Data Leakage / Contamination？

### 测试与 Evaluation

12. 为什么传统 `Expected == Actual` 在 LLM 场景下不够？
13. 什么是 Evaluation？
14. 为什么 AI 测试需要 Dataset、Grader、Metric？
15. 一个模型分数提高了，为什么不能直接认为模型变好了？

如果这些问题能够用自己的语言解释清楚，本章才算真正完成。

---

# 十五、本章最终形成的认知

```text
传统软件

需求
 ↓
规则
 ↓
代码
 ↓
确定性行为
 ↓
测试 Expected / Actual
```

而机器学习系统：

```text
数据
 ↓
训练
 ↓
模型
 ↓
概率性 / 数据依赖的行为
 ↓
泛化到新数据
 ↓
Evaluation
```

因此，AI Evaluation Engineer 并不是：

> **“会给 ChatGPT 写 Prompt 的测试工程师。”**

而是逐渐具备这样的能力：

> **理解模型为什么产生当前行为，并能够通过数据、实验、指标和统计证据判断这种行为是否可靠。**

这就是整个 `ai-evaluation-engineer` 学习路线的起点。

---

## 下一章

**02 Dataset：AI 为什么这么依赖数据？**

下一章不再继续堆 AI 名词，而是从一个最基本的问题开始：

> **如果模型是从数据中学习的，那么“什么数据给模型学习”本身，是不是就已经属于测试问题？**

从这里开始，逐步进入真正属于 AI Evaluation 的核心能力：**Dataset、Golden Set、Coverage、Representativeness、Data Quality、Leakage、Contamination 与 Versioning。**
