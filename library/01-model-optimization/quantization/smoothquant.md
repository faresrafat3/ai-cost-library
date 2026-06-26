---
id: entry-smoothquant-001
title_ar: التكميم الأملس — SmoothQuant
title_en: "SmoothQuant: Smooth Activations for INT8 Quantization"
type: practical
status: deployed
category: model-optimization
subcategory: quantization
cost_dimensions: [inference-cost, throughput, memory]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 2
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 8
  A2: 10
  A3: 9
  A4: 5
  B1: 7
  B2: 0
  B3: 7
  B4: 6
  C1: 6
  C2: 7
  C3: 8
  C4: 7
---

# 📘 SmoothQuant — تنعيم التفعيلات للتكميم الصحيح

> **التصنيف:** 📘 عملية | **الإثبات:** ⭐⭐⭐

---

## المحتوى العربي

### ما هو SmoothQuant؟

SmoothQuant — وهو تقنية تكميم W8A8 (أوزان 8-bit + تفعيلات 8-bit) تحل مشكلة أن **التفعيلات أصعب في التكميم من الأوزان** لأنها تحتوي قيماً شاذة كبيرة.

### الفكرة الأساسية — "نقل الصعوبة"

```
المشكلة: التفعيلات لها قيم شاذة → تكميمها مباشرة يُدمّر الجودة
         الأوزان سلسة → تكميمها سهل

SmoothQuant: يُضرب التفعيلات في عامل تنعيم s⁻¹ (يُقلل القيم الشاذة)
             ويُضرب الأوزان في s (يُعوّض — الأوزان تتحمل هذا أفضل)
             
النتيجة: X' = X / s   (أسهل في التكميم)
         W' = W × s   (مازالت قابلة للتكميم)
         Y = X'W' = (X/s)(Ws) = XW   (النتيجة متطابقة رياضياً)
```

### الأرقام

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| دقة INT8 مع SmoothQuant | **~99% من FP16** | Xiao et al., ICML 2023 |
| تسريع الاستدلال | **حتى 1.56×** | مقابل FP16 على GPU |
| تقليل الذاكرة | **~2×** | W8A8 مقابل W16A16 |

### موقعه في 2026

SmoothQuant مهم تاريخياً — أثبت أن W8A8 ممكن بجودة عالية. لكن في 2026:
- **FP8 تجاوزه على Hopper/Blackwell** (دعم أصلي + أسهل)
- **AWQ/GPTQ 4-bit أفضل ضغطاً** (ربع بدلاً من نصف)
- **مازال مفيداً** على عتاد بدون FP8 عندما تحتاج W8A8

### متى يُستخدم في 2026

- ✅ تكميم أوزان **وتفعيلات** معاً (W8A8) — وليس أوزان فقط
- ✅ عتاد بدون دعم FP8 يحتاج INT8 أصلي
- ✅ يُدمج في TensorRT-LLM لتسريع hardware

### القاعدة

```
Hopper+    → FP8 (يتضمن تنعيم ضمني)
ما قبل     → SmoothQuant W8A8 (لأقصى جودة 8-bit)
            أو AWQ 4-bit (لأقصى ضغط)
```

---

## المصادر

1. **[Tier 1]** Xiao, G., et al., "SmoothQuant: Accurate and Efficient Post-Training Quantization for LLMs", **ICML 2023**. MIT + NVIDIA.
2. **[Tier 2]** Zylos AI, "LLM Inference Optimization 2026", January 2026. INT8 quality retention ~97-99%.

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **LLM.int8()** | **يُكمل** — LLM.int8() W8A16، SmoothQuant W8A8 |
| **FP8** | **بديل أفضل** على Hopper+ (FP8 يتضمن تنعيم ضمني) |
| **TensorRT-LLM** | **يُدمج** — SmoothQuant مدمج في TensorRT-LLM |
| **AWQ/GPTQ** | **أقل ضغطاً** — SQ = 2× مقابل 4× لـ AWQ/GPTQ |

### ملاحظة: SmoothQuant في 2026 مُدمج في TensorRT-LLM كخيار تكميم W8A8 — لا يحتاج تطبيق يدوي.
