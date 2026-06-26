---
id: "entry-llmint8-001"
title_ar: "التكمية المختلطة الدقة للنماذج اللغوية (LLM.int8())"
title_en: "LLM.int8() — Mixed-Precision Decomposition for LLMs"
type: "Practical"
status: "Deployed"
category: "Model Compression"
subcategory: "Quantization"
tree_path: ["Model Compression", "Quantization", "LLM.int8()"]
cost_dimensions: ["memory", "inference-cost"]
proof_score: 4
sources_count: 3
---

# التكمية المختلطة الدقة للنماذج اللغوية | LLM.int8()

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary

LLM.int8() هي تقنية تكمية بعد التدريب تهدف إلى تمكين استدلال النماذج اللغوية الكبيرة (حتى 175B معامل) بدقة 8 بت دون فقدان الدقة. الاكتشاف الجوهري هو أن بنية المحوّل (Transformer) تحتوي على عدد صغير من "الميزات الشاذة" (Outlier Features) — أبعاد تنشيط أكبر بـ 100 مرة من المتوسط — والتي عند تكميتها مباشرة تُسبب انهياراً في الأداء.

الحل هو "التفكيك مختلط الدقة" (Mixed-Precision Decomposition): عزل أبعاد القيم الشاذة ومعالجتها بدقة 16 بت بينما تُكمّل بقية 99.9% من القيم بدقة 8 بت. النتيجة هي تقليل استهلاك الذاكرة بنسبة ~50% مع الحفاظ على الدقة الأصلية.

## 📌 English Summary

LLM.int8() is a post-training quantization technique enabling 8-bit inference for LLMs up to 175B parameters with zero accuracy degradation. The key discovery is that Transformer architectures contain a small number of "outlier features" — activation dimensions up to 100× larger than average — which, when quantized directly, cause catastrophic accuracy collapse.

The solution is "mixed-precision decomposition": isolating outlier dimensions and processing them in FP16 while quantizing the remaining 99.9% of values to INT8. This yields approximately 50% memory reduction while preserving original model accuracy.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected

- **تكلفة الذاكرة (Memory Cost):** تقليل الذاكرة بنسبة ~50%. نموذج BLOOM-176B يقل من ~350GB إلى ~178GB (1.96× تقليل).
- **تكلفة الاستدلال (Inference Cost):** تمكين استدلال نماذج 175B على خادم واحد ببطاقات GPU استهلاكية.

## 🛡️ بوابات الأدلة | Evidence Gates

- ✅ **Gate 1 (Built):** مُدمجة في مكتبة `bitsandbytes` و `Hugging Face Transformers` عبر `from_pretrained(load_in_8bit=True)`.
- ✅ **Gate 2 (Tested):** دقة 66.7% على OPT-175B (W8A8) مقارنة بـ 66.9% (FP16) عبر 7 معايير.
- ✅ **Gate 3 (Deployed):** مُستخدمة في Hugging Face Transformers، Petals، وأنظمة الاستدلال الموزعة.
- ✅ **Gate 4 (Saved):** 1.96× تقليل في الذاكرة لنماذج 175B+ مع صفر فقدان دقة.

## ⚠️ القيود والمخاطر | Limitations & Risks

- أبطأ من SmoothQuant لأنها تستخرج أعمدة القيم الشاذة ديناميكياً أثناء التشغيل.
- لا تدعم التكمية إلى أقل من 8 بت (مثل 4 بت) — يتطلب تقنيات أخرى كـ GPTQ أو AWQ.
- التفكيك المختلط يعتمد على أنوية CUDA مخصصة قد لا تكون محسّنة لجميع المنصات.

## 📚 المصادر | Sources

- [1] Dettmers et al., "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale", NeurIPS, 2022. DOI: [arXiv:2208.07339](https://arxiv.org/abs/2208.07339)
- [2] Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs", NeurIPS, 2023. DOI: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- [3] Meta Intelligence, "Model Quantization Guide: Run 70B LLMs in 4 Bits", 2025. [URL](https://www.meta-intelligence.tech/en/insight-quantization)

## 🔗 إدخالات ذات صلة | Related Entries

- [SmoothQuant](./smoothquant.md)
- [GPTQ](./gptq.md)
- [AWQ](./awq.md)
- [QLoRA](../../efficient-training/parameter-efficient/qlora.md)
