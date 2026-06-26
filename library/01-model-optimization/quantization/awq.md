---
id: "entry-awq-001"
title_ar: "تكمية الأوزان المعتمدة على التنشيط (AWQ)"
title_en: "Activation-aware Weight Quantization (AWQ)"
type: "Practical"
status: "Deployed"
category: "Model Compression"
subcategory: "Quantization"
cost_dimensions: ["memory", "inference-cost", "latency"]
proof_score: 4
sources_count: 2
---

# Activation-aware Weight Quantization (AWQ)

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary
تكمية الأوزان المعتمدة على التنشيط (AWQ) هي تقنية تكمية (Quantization) بعد التدريب صُممت خصيصاً للنماذج اللغوية الكبيرة. بدلاً من الاعتماد على حسابات معقدة للأوزان مثلما يفعل GPTQ، تلاحظ AWQ توزيع "التنشيطات" (Activations) أثناء الاستدلال وتستنتج أن حماية 1% فقط من "الأوزان البارزة" (Salient Weights) يقلل من خطأ التكمية بشكل هائل. توفر الخوارزمية دقة عالية وسرعة استدلال متفوقة بدون الحاجة إلى إعادة ترتيب البيانات (Data layout reordering)، مما يجعلها صديقة جداً للعتاد.

## 📌 English Summary
Activation-aware Weight Quantization (AWQ) is a hardware-friendly post-training quantization (PTQ) method that compresses LLMs to 3 or 4 bits. By observing activation distributions, AWQ scales to protect the 1% most salient weights, vastly reducing quantization error without relying on complex backpropagation or Hessian reconstruction. This yields superior inference speeds and avoids overfitting to calibration sets.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected
- **تكلفة الذاكرة (Memory Cost):** خفض الذاكرة بحوالي 3 إلى 4 مرات (تكمية النماذج إلى 4 بت). يُمكّن تشغيل Llama-13B على حاسوب محمول بذاكرة 8 جيجابايت.
- **الكمون / التأخير (Latency):** أسرع بنسبة 1.45x من GPTQ وأسرع بـ 1.85x من FP16 cuBLAS بفضل تجنب إعادة ترتيب البيانات في الذاكرة.
- **تكلفة الاستدلال (Inference Cost):** يرفع الكثافة الحسابية (Arithmetic Intensity) بمقدار 4x، مما يزيد عدد الرموز المستنتجة لكل دولار.

## 🛡️ بوابات الأدلة | Evidence Gates
- ✅ **Gate 1 (Built):** مدعومة بشكل أصلي (Native) في `vLLM`، `Hugging Face Transformers`، ونظام `TinyChat` الخاص بها.
- ✅ **Gate 2 (Tested):** أظهرت التجارب الرسمية تسريعاً يبلغ 2.7 إلى 3.9 أضعاف على شرائح 4090/Orin مقارنة بـ FP16.
- ✅ **Gate 3 (Deployed):** معتمدة واسعاً في النشر على الأجهزة الطرفية (On-Device/Edge) وكذلك الخوادم.
- ✅ **Gate 4 (Saved):** حافظت على دقة شبه مثالية لنماذج اللغة والرؤية المتعددة مع تقليل VRAM بأكثر من 65%، وتحسين سرعة المعالجة بنسبة تصل إلى 41x على أجهزة Apple Silicon (بواسطة أدوات مثل QRAF).

## ⚠️ القيود والمخاطر | Limitations & Risks
- تركز بشكل حصري على تكمية الأوزان (Weight-only)، بينما تظل التنشيطات (Activations) وذاكرة التخزين المؤقت (KV Cache) دون تكمية.
- مكاسب السرعة تعتمد في بعض الأحيان على كتابة أنوية CUDA مخصصة (Custom Kernels) قد تحتاج لتحديث مستمر للمنصات المختلفة.

## 📚 المصادر | Sources
- [1] Lin et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", arXiv (2306.00978) / MLSys, 2023-2024. [URL](https://arxiv.org/abs/2306.00978)
- [2] Wentao, "Summary: AWQ: Activation-Aware Weight Quantization", 2026 Review.
