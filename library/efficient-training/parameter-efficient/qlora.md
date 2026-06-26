---
id: "entry-qlora-001"
title_ar: "خوارزمية QLoRA"
title_en: "QLoRA Algorithm"
type: "Practical"
status: "Deployed"
category: "Efficient Training"
subcategory: "Parameter-Efficient Fine-Tuning"
cost_dimensions: ["training-cost", "memory", "hardware-cost"]
proof_score: 4
sources_count: 1
---

# QLoRA: Efficient Finetuning of Quantized LLMs

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary
خوارزمية QLoRA (التكيف منخفض الرتبة المكمم) هي تقنية تسمح بتوليف (Fine-tuning) النماذج اللغوية الكبيرة باستخدام ذاكرة أقل بكثير من خلال تكمية أوزان النموذج الأساسي إلى 4-بت (NormalFloat4) وتدريب محولات (Adapters) منخفضة الرتبة (LoRA) فوقها. 

## 📌 English Summary
QLoRA is a parameter-efficient fine-tuning technique that reduces memory usage by quantizing the base model to 4-bit (NF4) while backpropagating gradients into Low-Rank Adapters (LoRA). This allows fine-tuning massive models on a single GPU.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected
- **تكلفة التدريب (Training Cost):** يقلل من الحاجة لشراء أو استئجار شرائح VRAM ضخمة.
- **تكلفة الذاكرة (Memory Cost):** يخفض الذاكرة المطلوبة لتدريب نموذج 65B من >780 جيجابايت إلى أقل من 48 جيجابايت.

## 🛡️ بوابات الأدلة | Evidence Gates
- ✅ **Gate 1 (Built):** مدمجة في مكتبة `bitsandbytes` و `PEFT`.
- ✅ **Gate 2 (Tested):** أداء مقارب جداً للضبط الدقيق الكامل (Full Fine-tuning) على مهام متعددة.
- ✅ **Gate 3 (Deployed):** الخيار القياسي لضبط النماذج مفتوحة المصدر بتكلفة منخفضة.
- ✅ **Gate 4 (Saved):** مكنت آلاف المطورين من تدريب نماذج ضخمة على بطاقات شاشة المستهلكين (Consumer GPUs).

## ⚠️ القيود والمخاطر | Limitations & Risks
- أبطأ في التدريب بنسبة معينة مقارنة بالـ LoRA العادي بسبب أعباء حساب التكمية وفكها (Quant/Dequant overhead).
- قد يتطلب ضبط بعض المعاملات الفائقة (Hyperparameters) بعناية.

## 📚 المصادر | Sources
- [1] Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs", NeurIPS, 2023. [URL](https://arxiv.org/abs/2305.14314)
