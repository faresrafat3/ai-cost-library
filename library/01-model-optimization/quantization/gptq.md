---
id: entry-gptq-001
title_ar: التكميم بعد التدريب — GPTQ
title_en: "GPTQ: Post-Training Quantization for GPUs"
type: practical
status: production-proven
category: model-optimization
subcategory: quantization
cost_dimensions: [memory, inference-cost, throughput, hardware-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 10
  A3: 10
  A4: 5
  B1: 8
  B2: 0
  B3: 9
  B4: 7
  C1: 8
  C2: 8
  C3: 9
  C4: 10
research_review:
  decision: "إدخال أساسي — مُعاد كتابته ببيانات 2026 شاملة (معايير vLLM + Marlin)"
---

# 📘 GPTQ — التكميم بعد التدريب للمعالجات الرسومية

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐
>
> **المسار:** المكتبة ← تحسين النموذج ← التكميم

---

## المحتوى العربي

### ما هو GPTQ؟

GPTQ — وهو خوارزمية تكميم بعد التدريب (Post-Training Quantization) تُقلل دقة أوزان النموذج إلى 4 أو 3 بتات باستخدام تقنية القطع الأمثل طبقة بطبقة (layer-wise optimal rounding). تعتمد على تقريب مصفوفة هيسيان العكسية لتقليل خطأ التكميم.

### الأرقام الحديثة (2026)

#### الجودة (مقابل FP16)

| النموذج | FP16 | GPTQ 4-bit | الانحراف | AWQ 4-bit (للمقارنة) |
|---------|------|-----------|---------|---------------------|
| Llama 3.1 8B | 87.5 | 84.7 (-2.8) | -3.2% | 86.8 (-0.7) |
| Mistral 7B | 85.3 | 83.1 (-2.2) | -2.6% | 84.6 (-0.7) |
| Qwen 2.5 14B | 88.1 | 86.0 (-2.1) | -2.4% | 86.6 (-1.5) |

*المصدر: LocalAimaster 2026 — MMLU/GSM8K/HumanEval composite*

> ⚠️ **ملاحظة مهمة:** GPTQ يفقد جودة أكثر من AWQ (-2.1 إلى -2.8 مقابل -0.7 إلى -1.5). لكنه أسرع مع نواة Marlin.

#### الإنتاجية (Llama 8B على GPU)

| التقنية | إنتاجية (tok/s) | TTFT (ms) | ملاحظة |
|---------|----------------|----------|--------|
| FP16 (أساس) | 461 | 57.7 | — |
| GPTQ (عادي) | 277 | 107.1 | **أبطأ من FP16!** |
| **Marlin-GPTQ** | **712** | **51.9** | **1.54× أسرع من FP16** |
| Marlin-AWQ | 741 | 73.5 | 1.61× أسرع |

*المصدر: JarvisLabs 2026 — ShareGPT benchmark*

> 🔑 **الدرس الأهم:** GPTQ بدون Marlin **أبطأ** من FP16! النواة (kernel) أهم من الخوارزمية.

#### على RTX 4090 (14B model)

| التقنية | إنتاجية | تحسن |
|---------|---------|------|
| BF16 | 3,869 tok/s | أساس |
| AWQ | 5,653 tok/s | **+46%** |
| GPTQ Marlin | 5,026 tok/s | **+30%** |

*المصدر: GPUStack 2026*

### الذاكرة

| الدقة | حجم نموذج 70B | GPU مطلوبة |
|-------|--------------|-----------|
| FP16 | ~140 GB | 2×A100 80GB |
| INT8 | ~70 GB | 1×A100 80GB |
| **GPTQ 4-bit** | **~35 GB** | **1×RTX 4090** أو A100 |
| GPTQ 3-bit | ~26 GB | 1×RTX 4090 |

### متى تستخدم GPTQ (2026)

- ✅ **مع Marlin kernel** — إنتاجية أعلى من FP16 مع ربع الذاكرة
- ✅ عتاد بدون دعم FP8 أصلي (ما قبل Hopper)
- ✅ نماذج كبيرة على عتاد محدود (70B على RTX 4090)
- ✅ أقصى ضغط (3-bit) عندما الجودة مقبولة

### متى لا تستخدم

- ❌ **على Hopper/Blackwell** — FP8 أفضل (جودة أعلى + سرعة مماثلة)
- ❌ **بدون Marlin** — GPTQ العادي أبطأ من FP16
- ❌ **مهام حساسة للجودة** — AWQ تحافظ على جودة أعلى

### GPTQ vs AWQ vs FP8 — القاعدة السريعة

```
Hopper/Blackwell GPU → FP8 (الأفضل)
ما قبل Hopper + جودة مهمة → AWQ + Marlin
ما قبل Hopper + أقصى إنتاجية → GPTQ + Marlin
عتاد محدود جداً → GPTQ 3-bit
CPU/Mac → GGUF (ليس GPTQ)
```

### المخاطر والقيود

1. **فقدان جودة أكبر من AWQ:** -2.1 إلى -2.8 نقطة مقابل -0.7 لـ AWQ
2. **بدون Marlin = بطيء:** النواة العادية أبطأ من FP16
3. **وقت التكميم:** يحتاج بيانات معايرة + ساعات للنماذج الكبيرة
4. **3-bit ينهار:** فقدان جودة كبير على المهام المعقدة

---

## English Content

### GPTQ in 2026

GPTQ is a post-training quantization method that reduces weights to 4-bit or 3-bit. **Critical insight:** vanilla GPTQ kernels are SLOWER than FP16. The Marlin kernel makes GPTQ 1.54× faster than FP16.

**Decision tree:** Hopper GPU → use FP8. Pre-Hopper + quality → AWQ. Pre-Hopper + max throughput → GPTQ+Marlin.

Quality loss: -2.1 to -2.8 points (vs -0.7 for AWQ). Speed with Marlin: 712 tok/s vs 461 baseline.

---

## المصادر | Sources

1. **[Tier 1]** Frantar, E., et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", ICLR 2023. arXiv:2210.17323.
2. **[Tier 2]** JarvisLabs, "The Complete Guide to LLM Quantization with vLLM: Benchmarks", January 2026. Marlin benchmark data.
3. **[Tier 2]** GPUStack, "The Impact of Quantization on vLLM Inference Performance", 2026. A100/RTX 4090 benchmarks.
4. **[Tier 2]** LocalAimaster, "GGUF vs GPTQ vs AWQ 2026: Which Quantization Should You Use?", May 2026. Quality comparison.
