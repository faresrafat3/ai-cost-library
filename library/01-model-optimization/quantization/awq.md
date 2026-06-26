---
id: entry-awq-001
title_ar: التكميم المُدرك للتفعيل — AWQ
title_en: "AWQ: Activation-Aware Weight Quantization"
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
  A2: 9
  A3: 10
  A4: 6
  B1: 8
  B2: 0
  B3: 9
  B4: 7
  C1: 8
  C2: 8
  C3: 9
  C4: 10
---

# 📘 AWQ — التكميم المُدرك للتفعيل

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐
>
> **المسار:** المكتبة ← تحسين النموذج ← التكميم

---

## المحتوى العربي

### ما هو AWQ؟

AWQ (Activation-Aware Weight Quantization) — وهو خوارزمية تكميم 4-bit تحمي الأوزان الأكثر أهمية (المرتبطة بقنوات التفعيل العالية) من التكميم الخشن، مما يحافظ على جودة أعلى بكثير من GPTQ.

### لماذا AWQ أفضل من GPTQ في الجودة؟

GPTQ يُكمّم كل الأوزان بنفس الطريقة. AWQ يكتشف أن **1% من الأوزان** (المرتبطة بأكبر قيم التفعيل) مسؤولة عن معظم أداء النموذج — فيحميها.

### الأرقام الحديثة (2026)

#### الجودة — AWQ هو الأفضل في 4-bit

| النموذج | FP16 | **AWQ 4-bit** | GPTQ 4-bit | GGUF Q4_K_M |
|---------|------|-------------|-----------|-------------|
| Llama 3.1 8B | 87.5 | **86.8 (-0.7)** | 84.7 (-2.8) | 85.9 (-1.6) |
| Mistral 7B | 85.3 | **84.6 (-0.7)** | 83.1 (-2.2) | 83.8 (-1.5) |
| Qwen 2.5 14B | 88.1 | **86.6 (-1.5)** | 86.0 (-2.1) | 87.0 (-1.1) |

> **AWQ يحتفظ بـ ~95% من جودة FP16** — الأفضل بين جميع طرق 4-bit على GPU.

#### الإنتاجية (مع Marlin)

| | إنتاجية | TTFT | مقابل FP16 |
|---|---------|------|-----------|
| FP16 | 461 tok/s | 57.7ms | أساس |
| **Marlin-AWQ** | **741 tok/s** | 73.5ms | **1.61×** |
| Marlin-GPTQ | 712 tok/s | 51.9ms | 1.54× |

> **AWQ+Marlin = أعلى إنتاجية + أعلى جودة** بين جميع طرق 4-bit.

#### على RTX 4090 (Qwen 2.5 14B)

| | إنتاجية | تحسن |
|---|---------|------|
| BF16 | 3,869 tok/s | أساس |
| **AWQ** | **5,653 tok/s** | **+46%** |
| GPTQ Marlin | 5,026 tok/s | +30% |

### متى تستخدم AWQ

- ✅ **الاختيار الافتراضي لـ 4-bit على GPU** (ما قبل Hopper)
- ✅ مهام حساسة للجودة (كتابة إبداعية، كود، استدلال)
- ✅ مع Marlin kernel لأقصى سرعة
- ✅ HuggingFace Hub: آلاف النماذج المُكمّمة جاهزة

### متى لا تستخدم

- ❌ **Hopper/Blackwell** → FP8 أفضل (جودة 99% مقابل 95%)
- ❌ **CPU/Mac** → GGUF أفضل (AWQ مُصمم لـ GPU)
- ❌ **ذاكرة ضيقة جداً** → GPTQ 3-bit (جودة أقل لكن أصغر)

### مقابل FP8 — متى كل واحد؟

| المعيار | AWQ 4-bit | FP8 8-bit |
|---------|----------|----------|
| الذاكرة | **نصف FP8** | ضعف AWQ |
| الجودة | 95% من FP16 | **99% من FP16** |
| العتاد | أي GPU | Hopper+ فقط |
| الحكم | أفضل ضغط | أفضل جودة |

---

## English Content

AWQ protects the 1% most important weights (linked to high-activation channels), achieving ~95% FP16 quality retention — best among all 4-bit methods. AWQ+Marlin delivers 1.61× FP16 throughput.

**2026 rule:** Hopper GPU → FP8. Pre-Hopper → AWQ+Marlin.

---

## المصادر | Sources

1. **[Tier 1]** Lin, J., et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", MLSys 2024. MIT.
2. **[Tier 2]** JarvisLabs, "Complete Guide to LLM Quantization with vLLM", January 2026. Marlin-AWQ benchmarks.
3. **[Tier 2]** GPUStack, "Impact of Quantization on vLLM Performance", 2026. RTX 4090 data.
4. **[Tier 2]** LocalAimaster, "GGUF vs GPTQ vs AWQ 2026", May 2026. Quality comparison across 3 models.
