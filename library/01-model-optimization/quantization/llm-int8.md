---
id: entry-llmint8-001
title_ar: التكميم الصحيح 8-بت مع معالجة القيم الشاذة — LLM.int8()
title_en: "LLM.int8(): Mixed-Precision INT8 with Outlier Handling"
type: practical
status: production-proven
category: model-optimization
subcategory: quantization
cost_dimensions: [memory, inference-cost, hardware-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 9
  A2: 10
  A3: 10
  A4: 4
  B1: 6
  B2: 0
  B3: 8
  B4: 5
  C1: 9
  C2: 8
  C3: 8
  C4: 9
---

# 📘 LLM.int8() — التكميم المختلط الدقة مع القيم الشاذة

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐

---

## المحتوى العربي

### ما هو LLM.int8()؟

LLM.int8() — وهو أول طريقة تكميم ناجحة للنماذج اللغوية الكبيرة (2022)، ابتكرها Tim Dettmers. الاكتشاف الأساسي: **~0.1% من قيم التفعيل** (القيم الشاذة / outliers) تُدمّر الجودة عند تكميمها. الحل: مسار مزدوج.

### كيف يعمل؟ — المسار المزدوج

```
مصفوفة الأوزان × مصفوفة التفعيل:

الأبعاد العادية (99.9%):     → INT8 × INT8 → سريع + ذاكرة أقل
الأبعاد الشاذة (0.1%):       → FP16 × FP16 → دقيق + بطيء

المخرج = دمج النتيجتين
```

### الأرقام

| المقياس | القيمة |
|---------|--------|
| تقليل الذاكرة | **~2×** (FP16 → INT8) |
| فقدان الجودة (على نماذج ≤ 175B) | **~0%** (ضمن الضوضاء) |
| تأثير السرعة | **أبطأ من FP16** على بعض العتاد (overhead المسار المزدوج) |
| نماذج تعمل على GPU واحد (24GB) | حتى **~13B** (مقابل ~7B بـ FP16) |

### موقعه في 2026 — كلاسيكي أساسي لكن تجاوزته البدائل

| المعيار | LLM.int8() | FP8 | AWQ 4-bit | GPTQ 4-bit |
|---------|-----------|-----|----------|-----------|
| الذاكرة | 2× أقل | 2× أقل | **4× أقل** | **4× أقل** |
| الجودة | ~99.9% | ~99.5% | ~95% | ~90% |
| السرعة | **أبطأ** من FP16 | **أسرع** 1.5× | **أسرع** 1.6× (Marlin) | **أسرع** 1.5× (Marlin) |
| العتاد | أي GPU | Hopper+ | أي GPU | أي GPU |
| الحكم في 2026 | 🟡 مُتجاوَز | ✅ الأفضل 8-bit | ✅ الأفضل 4-bit | ✅ أقصى ضغط |

### متى يُستخدم في 2026

- ✅ **أبسط طريقة** لتشغيل نموذج أكبر قليلاً — سطر واحد في `bitsandbytes`
- ✅ عتاد قديم بدون دعم FP8
- ✅ عندما الجودة أولوية مطلقة ولا يُقبل أي فقدان

### متى لا يُستخدم

- ❌ **Hopper/Blackwell** → FP8 أفضل بكل المقاييس
- ❌ **ذاكرة ضيقة** → AWQ/GPTQ 4-bit أفضل (ربع بدلاً من نصف)
- ❌ **إنتاجية مهمة** → المسار المزدوج يُبطئ

### الأهمية التاريخية

> LLM.int8() فتح الباب لتشغيل النماذج الكبيرة على عتاد المستهلك. بدونه لم يكن ممكناً تشغيل 13B على RTX 3090. أسس لـ QLoRA والتكميم الحديث.

---

## المصادر

1. **[Tier 1]** Dettmers, T., et al., "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale", **NeurIPS 2022**.
2. **[Tier 2]** bitsandbytes library documentation, 2022-2026. https://github.com/TimDettmers/bitsandbytes
3. **[Tier 2]** Zylos AI, "LLM Inference Optimization and Quantization 2026", January 2026. Comparison table.
