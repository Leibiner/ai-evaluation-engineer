# 阶段 01｜AI 基础

> **第一阶段目标：先把 AI 是怎么工作的搞明白。**
>
> 这一阶段不学习 LLM、RAG、Agent，也不急着学习 Evaluation Framework。
> 先建立一套最基础、最稳定的认知：**AI 从什么数据学习 → 模型如何学习 → 如何产生结果 → 为什么会出错 → 如何判断模型是否真的学会了。**

---

# 一、这一阶段到底要学什么？

第一阶段只围绕一条主线展开：

```text
数据
 ↓
Dataset
 ↓
Input + Label
 ↓
Model
 ↓
Parameter
 ↓
Training
 ↓
Inference
 ↓
Prediction
 ↓
Error / Loss
 ↓
Evaluation
 ↓
Generalization
```

不要把本阶段理解成“背一堆 AI 名词”。

真正要建立的是一条完整的因果关系：

> **AI 从哪里获得学习材料 → 模型是什么 → 模型如何从数据中学习 → 学完以后如何产生结果 → 结果为什么可能错误 → 为什么训练数据上的表现不能代表真实世界表现。**

这一阶段的核心不是数学推导，而是先把这条链真正理解清楚。

---

# 二、学习目录

## 01｜认识 AI

| 篇 | 学习主题 | 要解决的核心问题 |
|---|---|---|
| **01** | **AI、ML、DL 到底是什么？** | AI、机器学习、深度学习到底是什么关系？ |
| **02** | **Dataset 到底是什么？** | AI 到底拿什么东西学习？ |
| **03** | **Label / Ground Truth 到底是什么？** | AI 怎么知道什么是正确答案？ |

## 02｜理解模型是怎么学习的

| 篇 | 学习主题 | 要解决的核心问题 |
|---|---|---|
| **04** | **Model 到底是什么？** | 模型到底是什么？为什么能够根据输入产生结果？ |
| **05** | **Parameter 到底是什么？** | 模型里面真正被学习和调整的东西是什么？ |
| **06** | **Training 到底是怎么进行的？** | 模型到底是怎么“学会”的？ |
| **07** | **Error / Loss 是什么？** | 模型怎么知道自己预测得好不好？ |
| **08** | **Optimization 是什么？** | 模型怎么根据错误不断调整自己？ |

## 03｜理解模型如何产生和验证结果

| 篇 | 学习主题 | 要解决的核心问题 |
|---|---|---|
| **09** | **Inference / Prediction 是什么？** | 模型训练完成后，如何根据新输入产生结果？ |
| **10** | **Validation / Test 是什么？** | 为什么不能只看训练数据判断模型好不好？ |
| **11** | **Generalization 是什么？** | 模型为什么必须能够处理没见过的数据？ |
| **12** | **Distribution Shift 是什么？** | 为什么模型上线后面对真实数据可能表现下降？ |
| **13** | **Data Leakage / Test Contamination 是什么？** | 为什么模型可能看起来很好，但结果其实不可信？ |

---

# 三、必须真正打通的核心链路

完成本阶段时，至少应该能够自己解释下面这条链：

```text
Dataset
  ↓
Input + Label
  ↓
Model
  ↓
Prediction
  ↓
Error / Loss
  ↓
Parameter Update
  ↓
Training
  ↓
得到训练后的 Model
  ↓
Inference
  ↓
Prediction
  ↓
Evaluation
  ↓
Generalization
```

例如：

> 给模型大量“正常短信”和“垃圾短信”，模型通过训练不断调整参数。训练完成后，输入一条没有见过的新短信，模型进行 Inference，产生 Prediction，再通过 Evaluation 判断它在新数据上的表现。

如果这句话中的每一个环节你都能解释清楚，第一阶段才算真正入门。

---

# 四、每一篇怎么学

每篇文章不追求堆知识，而是固定回答四个问题：

### 1. What

**它是什么？**

先建立准确概念，避免把不同概念混在一起。

### 2. Why

**为什么需要它？**

理解这个技术或概念解决了什么问题。

### 3. How

**它到底怎么工作？**

尽量通过简单案例、流程和最小实验建立直觉。

### 4. Failure

**如果它出了问题，会发生什么？**

从错误结果反过来理解这个概念。

学习路径统一为：

```text
概念
 ↓
因果关系
 ↓
简单案例
 ↓
最小实验
 ↓
故意制造错误
 ↓
分析原因
 ↓
复盘
```

---

# 五、这一阶段暂时不学什么？

为了避免基础阶段不断扩张，以下内容全部放到后续阶段：

- Transformer
- Attention
- Token
- Embedding
- LLM
- Prompt
- RAG
- Agent
- Fine-tuning
- AI Agent Framework
- Evaluation Framework
- AI Safety / Security

不是这些内容不重要，而是**现在还不到学习它们的时候**。

先把最底层的“数据 → 模型 → 训练 → 推理 → 结果”理解清楚，再进入下一阶段。

---

# 六、阶段完成标准

完成阶段 01 后，不要求成为算法工程师，也不要求能够从零训练大型模型。

要求达到三个层次：

### Level 1｜概念理解

能够用自己的话准确解释：

- Dataset
- Label / Ground Truth
- Model
- Parameter
- Training
- Inference
- Prediction
- Error / Loss
- Evaluation
- Generalization

### Level 2｜因果理解

能够回答：

- AI 为什么需要数据？
- Model 和 Dataset 是什么关系？
- Training 和 Inference 有什么区别？
- Prediction 和 Evaluation 有什么区别？
- Loss 为什么能够帮助模型学习？
- 为什么不能只看训练集？
- 为什么模型在训练数据上表现很好，真实数据上却可能很差？

### Level 3｜问题分析

面对一个简单的 AI 错误结果，能够沿着：

```text
数据
 ↓
标签
 ↓
模型
 ↓
训练
 ↓
推理
 ↓
预测
 ↓
评估
 ↓
泛化
```

分析问题可能出在哪里。

---

# 七、阶段验收

最终能够解释这样一个完整问题：

> 一个模型原来预测准确率只有 60%，经过训练后变成 90%，这 30% 是怎么来的？

并且能够继续解释：

```text
训练数据
 ↓
Model
 ↓
Prediction
 ↓
计算 Error / Loss
 ↓
调整 Parameter
 ↓
重复 Training
 ↓
得到训练后的 Model
 ↓
面对新数据进行 Inference
 ↓
得到 Prediction
 ↓
在未参与训练的数据上 Evaluation
 ↓
判断 Generalization
```

**能够把这条链讲清楚，第一阶段才算打牢。**

---

# 当前进度

```text
阶段 01｜AI 基础

01｜AI、ML、DL 到底是什么？   ← 当前
02｜Dataset 到底是什么？
03｜Label / Ground Truth 到底是什么？
04｜Model 到底是什么？
05｜Parameter 到底是什么？
06｜Training 到底是怎么进行的？
07｜Error / Loss 是什么？
08｜Optimization 是什么？
09｜Inference / Prediction 是什么？
10｜Validation / Test 是什么？
11｜Generalization 是什么？
12｜Distribution Shift 是什么？
13｜Data Leakage / Test Contamination 是什么？
```

当前第一篇：

**[→ 01｜AI、ML、DL 到底是什么？](./01｜AI、ML、DL 到底是什么？.md)**
