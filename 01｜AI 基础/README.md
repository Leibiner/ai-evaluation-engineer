# 阶段 01｜AI 基础

> **第一阶段目标：建立 AI 的底层因果模型。**
>
> 这一阶段不是为了把你训练成算法工程师，而是让传统软件测试工程师真正理解：**AI 是怎么产生结果的、为什么会错、错误可能来自哪里，以及后续如何判断 AI 是否可靠。**

---

# 一、这一阶段到底要学什么？

第一阶段围绕一条主线展开：

```text
数据
 ↓
Input + Label
 ↓
Model
 ↓
Training
 ↓
Parameter Update
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

不要把本阶段理解成“背一堆 AI 名词”。

真正要建立的是下面这套因果关系：

> **AI 从哪里获得学习材料 → 模型如何学习 → 模型如何产生结果 → 为什么结果会错 → 为什么训练集上的好成绩不代表真实世界表现好。**

---

# 二、学习目录

| 篇 | 学习主题 | 要解决的核心问题 |
|---|---|---|
| **01** | **AI、ML、DL 到底是什么？** | AI、机器学习、深度学习到底是什么？ |
| **02** | **Dataset 到底是什么？** | 模型到底从什么数据中学习？ |
| **03** | **Label / Ground Truth 到底是什么？** | AI 的“正确答案”从哪里来？ |
| **04** | **Model 到底是什么？** | 模型和参数到底是什么？ |
| **05** | **Prediction / Inference 是什么？** | 模型是怎么得到结果的？ |
| **06** | **Error / Loss 是什么？** | 模型怎么衡量自己预测得好不好？ |
| **07** | **Optimization 是什么？** | 模型怎么根据错误调整自己？ |
| **08** | **Training 是怎么进行的？** | 一个模型到底是怎么训练出来的？ |
| **09** | **Validation / Test 是什么？** | 为什么训练得好不代表真的好？ |
| **10** | **Generalization 是什么？** | 模型为什么需要在新数据上保持能力？ |
| **11** | **Distribution Shift 是什么？** | 为什么模型上线后可能越来越差？ |
| **12** | **Data Leakage / Test Contamination 是什么？** | 为什么评测结果可能看起来很好，但其实不可信？ |

---

# 三、阶段学习方式

每一篇都按照同一条学习路径推进：

```text
理解概念
   ↓
建立因果关系
   ↓
具体案例
   ↓
动手实验
   ↓
Failure Analysis
   ↓
复盘
   ↓
形成能力
```

每篇最终都要回答四个问题：

1. **What**：它是什么？
2. **Why**：为什么需要它？
3. **How**：它如何工作？
4. **Evidence**：如何证明自己的理解和结论？

---

# 四、阶段完成标准

完成阶段 01 后，不要求成为算法工程师，而要求能够建立最基本的 AI Failure Analysis 能力：

> **我知道 AI 的结果是如何产生的，也知道一个错误可能来自数据、标签、模型、训练、泛化或分布变化。**

完成标准分三层：

- **Level 1：概念理解** —— 能准确解释核心概念。
- **Level 2：因果理解** —— 能把数据、模型、训练、推理、错误等串成完整链路。
- **Level 3：Failure Analysis** —— 面对一个 AI 错误结果，能够分析可能的原因。

---

# 当前进度

```text
阶段 01｜AI 基础

01｜AI、ML、DL 到底是什么？   ← 当前
02｜Dataset 到底是什么？
03｜Label / Ground Truth 到底是什么？
04｜Model 到底是什么？
05｜Prediction / Inference 是什么？
06｜Error / Loss 是什么？
07｜Optimization 是什么？
08｜Training 是怎么进行的？
09｜Validation / Test 是什么？
10｜Generalization 是什么？
11｜Distribution Shift 是什么？
12｜Data Leakage / Test Contamination 是什么？
```

当前第一篇：

**[→ 01｜AI、ML、DL 到底是什么？](./01｜AI、ML、DL 到底是什么？.md)**
