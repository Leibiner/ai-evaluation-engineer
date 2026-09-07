# Phase 01｜AI / ML Foundations

> **第一阶段目标：建立 AI 的底层因果模型。**
>
> 这一阶段不是为了把你训练成算法工程师，而是让传统软件测试工程师真正理解：**AI 是怎么产生结果的、为什么会错、错误可能来自哪里，以及为什么最终必须通过 Evaluation 判断 AI 是否可靠。**

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

不要把本阶段理解成“背 12 个 AI 名词”。

真正要建立的是下面这套因果关系：

> **AI 从哪里获得学习材料 → 模型如何学习 → 模型如何产生结果 → 为什么结果会错 → 为什么训练集上的好成绩不代表真实世界表现好 → 测试工程师如何判断模型到底好不好。**

---

# 二、学习范围总览

本阶段共 **12 个模块**，按照“先理解 AI → 再理解模型 → 再理解训练 → 最后理解为什么需要 Evaluation”的顺序学习。

| 模块 | 学习主题 | 要解决的核心问题 |
|---|---|---|
| 01 | AI / ML / DL | AI、机器学习、深度学习到底是什么？ |
| 02 | Dataset | 模型到底从什么数据中学习？ |
| 03 | Label / Ground Truth | AI 的“正确答案”从哪里来？ |
| 04 | Model / Parameter | 模型到底是什么？ |
| 05 | Prediction / Inference | 模型是怎么得到结果的？ |
| 06 | Error / Loss | 模型怎么衡量自己预测得好不好？ |
| 07 | Optimization | 模型怎么根据错误调整自己？ |
| 08 | Training | 一个模型到底是怎么训练出来的？ |
| 09 | Validation / Test | 为什么训练得好不代表真的好？ |
| 10 | Generalization | 模型为什么学会了训练数据，却不会做新数据？ |
| 11 | Distribution Shift | 为什么模型上线以后可能越来越差？ |
| 12 | Data Leakage / Test Contamination | 为什么评测结果可能看起来很好，但其实不可信？ |

---

# 三、模块详细学习内容

## 01｜AI、ML、DL 到底是什么

### 必须理解

```text
Artificial Intelligence
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Neural Network
        ↓
Transformer
        ↓
现代 LLM 的重要基础
```

### 学习内容

- AI（Artificial Intelligence）
- Machine Learning
- Deep Learning
- Neural Network
- Transformer 的位置和作用（只建立概念，不深入架构细节）
- Rule-based System vs Machine Learning
- Traditional Program vs Learning System
- 为什么机器学习不是“写更多 if / else”
- 什么叫“从数据中学习”

### 测试工程师必须理解

传统程序主要依赖人写出的明确规则；机器学习系统通过数据训练模型，使模型学习能够用于新输入的规律。

### 学习出口

能够用自己的话解释：

> **机器学习里的“学习”到底发生在哪里？**

---

## 02｜Dataset：模型到底从什么东西学习

### 必须理解

```text
Dataset
 ↓
Sample
 ↓
Input / Feature
```

### 学习内容

- Dataset
- Sample
- Feature
- Input
- Training Set
- Validation Set
- Test Set
- 数据分布（Data Distribution）
- 数据质量（Data Quality）
- 数据偏差（Data Bias）
- 数据代表性（Representativeness）

### 测试工程师必须理解

模型不是凭空学习的。模型最终学到什么，很大程度取决于有什么数据、数据是否正确、数据是否覆盖真实场景，以及数据分布是否合理。

### 学习出口

能够解释：

> **为什么数据质量本身就是 AI 系统质量的一部分？**

---

## 03｜Label / Annotation：AI 的正确答案从哪里来

### 必须理解

```text
Input
 ↓
Label / Ground Truth
```

### 学习内容

- Label
- Target
- Ground Truth
- Annotation
- Human Annotation
- Reference
- Label Quality
- Label Noise
- Annotation Consistency
- 标注规范（Annotation Guideline）基本概念

### 必须纠正的一个误区

不是：

> “系统告诉模型：你错了，正确答案是垃圾。”

而是：

```text
训练数据
 ↓
Input + Target / Label
 ↓
Model Prediction
 ↓
Loss Function 比较 Prediction 与 Target
 ↓
Optimization
```

### 与传统测试的连接

```text
传统测试：Expected Result
AI：       Ground Truth / Reference
```

但二者并不完全等价，因为 AI 的很多任务不存在唯一字符串答案。

### 学习出口

能够回答：

> **什么是 Ground Truth？为什么“正确答案”本身也可能不可靠？**

---

## 04｜Model：模型到底是什么

### 必须理解

```text
Input
 ↓
Model
 ↓
Prediction
```

### 学习内容

- Model
- Model Architecture
- Parameter
- Weight
- Bias
- Feature 与 Parameter 的区别
- 模型如何表示复杂关系
- 模型为什么不是固定业务规则
- Black Box 与可解释性的基本概念

### 测试工程师必须理解

不要把模型理解成一堆 if / else，而应该建立：

```text
Model
= Architecture + Parameters
```

的基本认知。

### 学习出口

能够用自己的话解释：

> **Model 是什么？Parameter 是什么？训练到底改变了什么？**

---

## 05｜Prediction / Inference：模型如何得到结果

### 必须理解

```text
Input
 ↓
Model
 ↓
Prediction
```

### 学习内容

- Prediction
- Inference
- Probability
- Score
- Classification
- Regression
- Prediction Error
- Training vs Inference
- Deterministic 与非确定性输出的基本区别

### 贯穿案例

```text
Input：
恭喜中奖100万

Model Prediction：
正常：60%
垃圾：40%

Ground Truth：
垃圾
```

于是：

```text
Prediction ≠ Ground Truth
```

### 学习出口

能够解释：

> **模型从 Input 到 Prediction，中间发生了什么？Training 和 Inference 又有什么区别？**

---

## 06｜Error / Loss：模型怎么衡量预测错误

### 核心链路

```text
Prediction
    ↓
与 Target / Ground Truth 比较
    ↓
Error / Loss
```

### 学习内容

- Error
- Loss
- Loss Function
- Target
- Prediction Error
- 为什么需要 Loss
- Loss 的基本含义
- 不同任务为什么使用不同 Loss
- Classification Loss 的基本概念
- Regression Loss 的基本概念

### 重点理解

Loss 不是一句“你错了”的提示，而是一个可以计算的优化信号。

```text
Prediction
    ↓
Loss Function
    ↓
Loss
    ↓
用于后续 Optimization
```

### 学习出口

能够解释：

> **Loss 在模型训练中到底起什么作用？**

---

## 07｜Optimization：模型怎么根据错误改进

### 核心链路

```text
Prediction
    ↓
Loss
    ↓
Gradient
    ↓
Optimizer
    ↓
Parameter Update
```

### 学习内容

- Gradient
- Gradient Descent
- Learning Rate
- Optimizer
- Parameter Update
- Backpropagation
- 为什么 Gradient 能指导参数调整
- Learning Rate 太大 / 太小的基本影响

### 学习深度要求

第一阶段以**建立正确直觉和因果关系**为主，不要求一开始手算复杂神经网络反向传播公式。

但是必须知道：

```text
Loss
 ↓
Gradient
 ↓
Optimizer
 ↓
更新 Parameters
```

### 学习出口

能够解释：

> **模型为什么能够根据错误不断调整自己？**

---

## 08｜Training：模型到底怎么训练出来

### 核心训练循环

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
Backward / Backpropagation
   ↓
Optimizer
   ↓
Parameter Update
   ↓
Repeat
```

### 学习内容

- Training
- Training Loop
- Forward Pass
- Backward Pass
- Backpropagation
- Batch
- Batch Size
- Iteration / Step
- Epoch
- Optimizer
- Learning Rate
- Training Loss

### 学习出口

能够完整讲清楚：

> **一个模型从拿到训练数据，到逐渐学会任务，中间到底经历了哪些步骤？**

---

## 09｜Validation / Test：训练得好就代表好吗

### 必须理解

```text
Training Set
      ↓
训练模型

Validation Set
      ↓
开发阶段检查 / 调参

Test Set
      ↓
最终独立评估
```

### 学习内容

- Training Set
- Validation Set
- Test Set
- 三者的目的和区别
- 为什么不能只看 Training Loss
- 为什么需要独立 Test Set
- 数据划分的基本原则
- Data Leakage 的基本概念
- Test Set Independence

### 与传统测试建立连接

```text
传统软件：
Input → Expected → Actual → Pass / Fail

机器学习：
Input → Prediction → Ground Truth → Evaluation
```

### 学习出口

能够解释：

> **为什么训练集 99% 准确率，仍然不能证明模型真实能力很好？**

---

## 10｜Generalization：为什么模型学会了却不会做

### 核心问题

```text
Training Data
      ↓
表现很好
      ↓
New Data
      ↓
表现下降
```

### 学习内容

- Generalization
- Overfitting
- Underfitting
- Bias / Variance 基本概念
- Memorization 与 Generalization 的区别
- 为什么模型需要在未见过的数据上保持能力

### 学习出口

能够解释：

> **“记住训练数据”和“真正学会规律”有什么区别？**

---

## 11｜Distribution Shift：真实世界为什么会让模型失效

### 核心结构

```text
Training Distribution
        ↓
      Model
        ↓
Real-world Distribution
```

### 学习内容

- Distribution
- Distribution Shift
- Data Drift
- Concept Drift
- Covariate Shift 的基本概念
- 训练数据与线上数据的差异
- 为什么离线评测很好，线上表现仍然可能下降

### 学习出口

能够解释：

> **为什么一个在离线 Test Set 上表现优秀的模型，到了真实线上环境仍然可能失效？**

---

## 12｜Data Leakage / Test Contamination：为什么测试结果可能是假的

### 必须理解

```text
正常：
Training Data
       ↓
     Model
       ↓
Independent Test Data
       ↓
   Evaluation
```

如果 Test Data 已经通过某种方式进入训练或模型开发过程：

```text
Test Data
   ↓
训练 / 调参 / 模型选择
   ↓
Evaluation
```

最终分数可能被高估。

### 学习内容

- Data Leakage
- Test Contamination
- Train/Test Contamination
- 为什么 Test Set 必须尽量独立
- 数据泄漏的基本类型
- Test Contamination 为什么会导致虚假的高分
- Evaluation Trustworthiness

### 学习出口

能够识别：

> **测试数据为什么必须保持独立？什么情况下一个看起来很高的评测分数其实不可信？**

---

# 四、12 个模块之间不是并列关系

必须按照下面这条因果链理解整个阶段：

```text
01 AI / ML / DL
       ↓
02 Dataset
       ↓
03 Input + Label / Ground Truth
       ↓
04 Model + Parameters
       ↓
05 Training
       ↓
06 Prediction / Inference
       ↓
07 Error / Loss
       ↓
08 Gradient / Optimization
       ↓
09 Parameter Update
       ↓
10 Training Loop
       ↓
11 Validation / Test
       ↓
12 Generalization
       ↓
13 Distribution Shift
       ↓
14 Data Leakage / Test Contamination
       ↓
15 Evaluation
```

这里的编号是**知识依赖关系**，不是文章数量。

真正学习时应该形成一个完整闭环：

```text
数据
 ↓
模型学习
 ↓
模型产生预测
 ↓
预测可能错误
 ↓
训练过程利用 Loss 改进模型
 ↓
模型需要在未见数据上验证
 ↓
还要考虑真实世界的数据变化
 ↓
最终才能判断模型到底好不好
```

---

# 五、这一阶段明确“不学什么”

为了避免从“零基础测试工程师”变成“算法课程学习者”，以下内容**不是本阶段重点**：

- 不要求手推复杂神经网络数学公式
- 不要求从零实现 Transformer
- 不要求从零训练 LLM
- 不要求深入 CUDA / GPU 编程
- 不要求深入研究模型架构优化
- 不要求成为算法工程师
- 不要求一开始掌握 PyTorch 全部 API

但以下内容必须建立**概念级理解**：

```text
Model
Parameter
Training
Inference
Loss
Gradient
Optimization
Generalization
Distribution Shift
```

因为这些概念直接决定你以后能不能真正理解 AI Evaluation。

---

# 六、第一阶段必须完成的实践

不能只看文章。

至少完成以下实践：

## Practice 01｜手工走一遍分类模型

给定：

```text
Input：恭喜中奖100万
Label：垃圾
```

理解并画出：

```text
Input
 ↓
Model
 ↓
Prediction
 ↓
Ground Truth
 ↓
Loss / Error
```

---

## Practice 02｜观察 Training / Validation / Test

准备一个简单分类数据集，理解：

```text
Training Set
Validation Set
Test Set
```

分别承担什么作用。

---

## Practice 03｜观察 Overfitting

使用一个简单机器学习模型，让它分别在：

```text
Training Data
New / Test Data
```

上进行预测，观察训练表现与泛化表现的差异。

---

## Practice 04｜模拟 Data Leakage

故意让测试数据参与训练，再比较：

```text
正常 Test
vs
Contaminated Test
```

观察为什么污染后的评测结果可能虚高。

---

## Practice 05｜完成一次 AI Failure Analysis

针对一个模型错误，例如：

```text
Input：恭喜中奖100万
Prediction：正常
Ground Truth：垃圾
```

不能只写：

> 模型预测错误。

而要至少从以下方向分析：

```text
Data
Label
Model
Training
Inference
Generalization
Distribution
Evaluation
```

---

# 七、第一阶段完成标准

这一阶段不是“看完 12 个模块”就算完成。

必须达到下面的能力。

## Level 1｜能解释概念

能够不用背定义解释：

- AI / ML / DL
- Dataset / Sample / Feature / Input
- Label / Ground Truth / Annotation
- Model / Parameter / Weight / Bias
- Training / Inference
- Prediction / Error / Loss
- Gradient / Optimization / Parameter Update
- Epoch / Batch / Step
- Training / Validation / Test
- Generalization
- Overfitting / Underfitting
- Distribution Shift
- Data Leakage / Test Contamination

## Level 2｜能解释因果关系

能够回答：

> 数据为什么会影响模型？

> Label 为什么重要？

> 模型为什么会犯错？

> Loss 为什么能够帮助训练？

> Gradient 和 Parameter Update 在干什么？

> 为什么 Training Set 分数高不代表模型真的好？

> 为什么模型上线后可能因为 Distribution Shift 而退化？

> 为什么 Test Contamination 会让 Evaluation 失去可信度？

## Level 3｜能做 AI Failure Analysis

给你一个模型错误：

```text
Input
 ↓
Prediction
 ↓
Ground Truth
```

你能够进一步分析：

```text
数据问题？
 ↓
标签问题？
 ↓
模型能力问题？
 ↓
训练问题？
 ↓
泛化问题？
 ↓
分布变化？
 ↓
评测设计问题？
```

达到这个 Level，才算真正完成第一阶段。

---

# 八、第一阶段最终要形成的能力

完成 Phase 01 后，你应该已经从：

> **“AI 是一个黑盒，我只能看它输出对不对。”**

升级到：

> **“我知道 AI 的结果是如何产生的，也知道一个错误可能从数据、标签、模型、训练、泛化和分布等多个层面产生。”**

最终能够建立这条完整认知：

```text
Data
 ↓
Label / Ground Truth
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
Optimization
 ↓
Generalization
 ↓
Distribution Shift
 ↓
Evaluation
```

这就是后续学习 **Evaluation Dataset → Metrics → LLM Evaluation → RAG Evaluation → Agent Evaluation → Multi-Agent Evaluation → Safety / Security → Evaluation Engineering → Production Evaluation** 的基础。

**Phase 01 的目标不是让你会训练模型，而是让你不再把 AI 当成一个普通黑盒软件。**
