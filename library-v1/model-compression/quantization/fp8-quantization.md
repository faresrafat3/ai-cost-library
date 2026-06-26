---
id: entry-fp8-001
title_ar: التكميم بدقة FP8
title_en: FP8 Quantization
type: practical
status: production-proven
category: model-compression
subcategory: quantization
tree_path: "AI Cost Library → Model Compression → Quantization → FP8 Quantization"
cost_dimensions:
  - memory
  - compute
  - inference-cost
  - throughput
  - hardware-cost
  - energy
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 5
created: 2026-06-26
updated: 2026-06-26
---

# 📘 التكميم بدقة FP8 | FP8 Quantization

> **التصنيف:** 📘 عملية — إنتاج مُثبَت | **الإثبات:** ⭐⭐⭐⭐ إنتاج
>
> **المسار:** مكتبة تكلفة الذكاء الاصطناعي ← ضغط النماذج ← التكميم ← FP8

---

## المحتوى العربي

### ما هو التكميم بدقة FP8؟

التكميم بدقة FP8 — وهو تمثيل الأوزان والتفعيلات في النموذج باستخدام 8 بتات بصيغة الفاصلة العائمة بدلاً من 16 أو 32 بتاً، مما يُنصِّف استهلاك الذاكرة ويُضاعف الإنتاجية تقريباً مع الحفاظ على جودة شبه مطابقة للدقة الكاملة.

يوجد تنسيقان رئيسيان:
- **E4M3:** 4 بتات للأُسّ و3 بتات للجزء العشري — أعلى دقة، مناسب للأوزان
- **E5M2:** 5 بتات للأُسّ و2 بتات للجزء العشري — مدى ديناميكي أوسع، مناسب للتدرجات

### لماذا FP8 هو المعيار الافتراضي في 2026؟

FP8 أصبح المعيار الافتراضي لنشر الاستدلال على معالجات H100/H200/B100/B200 لعدة أسباب:
1. **دعم عتادي أصيل:** معالجات NVIDIA Hopper وBlackwell تدعم FP8 في وحدات Tensor Core.
2. **تدهور جودة ضئيل:** انحدار 0.3-0.5 نقطة على MMLU-Pro مقابل FP16 — ضمن هامش الخطأ.
3. **مضاعفة الإنتاجية:** تحسن 1.4-1.7× في عدد التوكنات/ثانية.
4. **نصف الذاكرة:** نموذج 70B يحتاج ~35 جيجابايت بدلاً من ~140 جيجابايت (FP16) أو ~70 جيجابايت (INT8).

### الأدلة والنتائج

| الادعاء | القيمة | المصدر | الثقة |
|---------|--------|--------|-------|
| تدهور MMLU-Pro مقابل FP16 (6 نماذج 70B) | 0.3-0.5 نقطة | Digital Applied (أبريل 2026) | عالية |
| تحسن الإنتاجية على H100 | 1.4-1.7× | Digital Applied + NVIDIA | عالية |
| تقليل تكلفة المليون توكن على H100 (70B) | ~50% (من $1.90 إلى $0.95-1.10) | Spheron (2026) | عالية |
| تدهور DeepSeek-R1 FP8 مقابل الأساس | 0% فعلياً | arxiv:2505.02390 (2025) | عالية |
| تدهور DeepSeek-V3 FP8 مقابل Q4_K_M | 0% | arxiv:2505.02390 (2025) | عالية |
| تحسن السرعة (توكن/ثانية) لـ Mistral 7B FP8 | 33% | Zylos.ai (2026) | متوسطة |

### أبعاد التكلفة المتأثرة

| البُعد بالعربية | البُعد بالإنجليزية | التأثير |
|-----------------|-------------------|---------|
| الذاكرة | Memory | ↓↓ نصف الاستهلاك |
| الحوسبة | Compute | ↓↓ تحسن 1.4-1.7× |
| تكلفة الاستدلال | Inference Cost | ↓↓ تقليل ~50% |
| الإنتاجية | Throughput | ↑↑ تحسن 1.4-1.7× |
| تكلفة العتاد | Hardware Cost | ↓↓ نفس العتاد، إنتاجية أعلى |
| الطاقة | Energy | ↓ تقليل لكل توكن |

### بوابات الإثبات

| البوابة | الحالة | التفاصيل |
|---------|--------|----------|
| 🏗️ بوابة 1: مبني | ✅ | NVIDIA TensorRT-LLM، vLLM FP8، PyTorch FP8، DeepGEMM |
| 🧪 بوابة 2: مُختبَر | ✅ | معايير MMLU-Pro، HumanEval+، GPQA، MATH-500 عبر 6 نماذج |
| 🚀 بوابة 3: مُنشَر | ✅ | الوضع الافتراضي في معظم خدمات الاستدلال السحابية (2026) |
| 💰 بوابة 4: وفَّر | ✅ | ~50% تقليل في CPM على H100 (موثق) |

### متى تستخدم

- ✅ أي نشر استدلال جديد على H100/H200/B100/B200
- ✅ نماذج 70B+ حيث الذاكرة عامل محدِّد
- ✅ خدمات إنتاج حيث الإنتاجية أولوية
- ✅ كخطوة أولى قبل تجربة تكميم أعمق (INT4/FP4)

### متى لا تستخدم

- ❌ على عتاد لا يدعم FP8 أصلاً (A100 وما قبله — يمكن المحاكاة لكن بدون مكاسب)
- ❌ مهام طبية/قانونية/علمية حرجة بدون تقييم مسبق على مجموعة بيانات المجال
- ❌ إذا كان FP16 يفي بالمتطلبات والميزانية كافية

### المخاطر والقيود

1. **اعتماد العتاد:** المكاسب الحقيقية تتطلب معالجات Hopper/Blackwell.
2. **مهام الذيل الطويل:** بعض المهام النادرة قد تتأثر أكثر من المعايير العامة.
3. **الذاكرة المؤقتة KV:** تكميم ذاكرة KV إلى FP8 يوفر ذاكرة إضافية لكن يحتاج اختباراً منفصلاً.
4. **التدريب بـ FP8:** أقل نضجاً من الاستدلال؛ يحتاج وصفات خاصة (مثل InfiR2).

---

## English Content

### What is FP8 Quantization?

FP8 quantization represents model weights and activations using 8-bit floating-point numbers instead of 16 or 32 bits, halving memory consumption and roughly doubling throughput while maintaining near-full-precision quality.

Two main formats exist:
- **E4M3:** 4-bit exponent, 3-bit mantissa — higher precision, suitable for weights
- **E5M2:** 5-bit exponent, 2-bit mantissa — wider dynamic range, suitable for gradients

### Why FP8 is the 2026 Default

FP8 has become the default inference precision on H100/H200/B100/B200 GPUs because:
1. **Native hardware support:** NVIDIA Hopper and Blackwell Tensor Cores support FP8 natively.
2. **Minimal quality loss:** 0.3-0.5 point MMLU-Pro regression vs FP16 — within run-to-run noise.
3. **Throughput doubling:** 1.4-1.7× improvement in tokens/second.
4. **Half memory:** A 70B model needs ~35GB instead of ~140GB (FP16).

### Proof Gates

| Gate | Status | Details |
|------|--------|---------|
| 🏗️ Gate 1: Built | ✅ | NVIDIA TensorRT-LLM, vLLM FP8, PyTorch FP8, DeepGEMM |
| 🧪 Gate 2: Tested | ✅ | MMLU-Pro, HumanEval+, GPQA, MATH-500 benchmarks across 6 models |
| 🚀 Gate 3: Deployed | ✅ | Default in most cloud inference services (2026) |
| 💰 Gate 4: Saved | ✅ | ~50% CPM reduction on H100 (documented) |

---

## المصادر | Sources

1. **[Tier 1]** Digital Applied, "Quantization Tradeoffs: 4-bit vs 8-bit vs FP8 Data", April 2026. 6 models, 5 quantization levels, measured data on H100. https://www.digitalapplied.com/blog/quantization-tradeoffs-4bit-8bit-fp8-performance-data
2. **[Tier 1]** NVIDIA, "FP8 Formats for Deep Learning", NVIDIA Technical Blog, 2022-2026. TensorRT-LLM FP8 documentation.
3. **[Tier 2]** Spheron Network, "AI Inference Cost Economics in 2026", April 2026. FP8 on H100 CPM data. https://www.spheron.network/blog/ai-inference-cost-economics-2026/
4. **[Tier 1]** Chen, Y., et al., "Quantitative Analysis of Performance Drop in DeepSeek Model Quantization", arXiv:2505.02390, May 2025. FP8 vs lower precision analysis.
5. **[Tier 2]** LMSYS, "Unified FP8: Moving Beyond Mixed Precision for Stable and Accelerated MoE RL", November 2025. FP8 training research. https://www.lmsys.org/blog/2025-11-25-fp8-rl/
