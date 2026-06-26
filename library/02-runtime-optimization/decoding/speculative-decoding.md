---
id: entry-specdec-001
title_ar: فك الترميز التخميني
title_en: "Speculative Decoding: Draft-then-Verify for Faster Inference"
type: practical
status: production-proven
category: runtime-optimization
subcategory: decoding
cost_dimensions: [latency, throughput, inference-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 8
  A2: 9
  A3: 8
  A4: 7
  B1: 6
  B2: 0
  B3: 0
  B4: 7
  C1: 5
  C2: 7
  C3: 7
  C4: 7
---

# 📘 فك الترميز التخميني | Speculative Decoding

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐

---

## المحتوى العربي

### ما هو فك الترميز التخميني؟

فك الترميز التخميني (Speculative Decoding) — وهو تقنية تستخدم نموذج مسودة صغير وسريع (draft model) لتوليد عدة توكنات مُرشحة، ثم النموذج الكبير (target model) يتحقق منها جميعاً دفعة واحدة. لأن التحقق من عدة توكنات بنفس تكلفة توليد واحد (في النماذج الكثيفة)، هذا يُسرّع التوليد **بدون تغيير المخرجات** (lossless).

### كيف يعمل؟

```
بدون speculative decoding:
  النموذج الكبير: [tok1] → [tok2] → [tok3] → [tok4] → [tok5]
  5 خطوات، كل خطوة تحمّل 70B معامل

مع speculative decoding:
  المسودة (1B): [tok1, tok2, tok3, tok4, tok5] → سريع جداً
  النموذج الكبير: [تحقق من 5 دفعة واحدة] → خطوة واحدة!
  قَبِل: tok1 ✅, tok2 ✅, tok3 ✅, tok4 ❌ → أعاد من tok4
  النتيجة: 3 توكنات بخطوة واحدة بدلاً من 3
```

### الأرقام (2026)

| الإصدار | التسريع | معدل القبول | ملاحظة |
|---------|---------|------------|--------|
| الأصلي (Leviathan 2023) | 2-3× | ~70% | النموذج المرجعي |
| **EAGLE-3 (2025-2026)** | **1.6×** (70B vLLM) | ~35% | **الأحدث — انظر entry-eagle3-001** |
| PayPal + EAGLE-3 | 22-49% throughput | 35.5% | **دراسة حالة إنتاجية** |
| ConFu (أبريل 2026) | 8-21% فوق EAGLE-3 | أعلى | أحدث preprint |

### العلاقة بالتطورات الأحدث

```
Speculative Decoding (2023) ← المبدأ الأساسي
    │
    ├── EAGLE-3 (2025) ← أحدث وأسرع — انظر entry-eagle3-001
    │
    ├── MoE-Spec (2026) ← حل مشكلة MoE — انظر entry-moespec-001
    │
    ├── ConFu (2026) ← يتفوق على EAGLE-3 بـ 8-21%
    │
    └── SpecVLM (2025) ← لنماذج Vision-Language
```

### القيود الأساسية

1. **فعالية تتناقص مع الدفعات الكبيرة:** batch > 56 → مكاسب ضئيلة
2. **MoE مشكلة:** كل توكن مُسوَّد يُفعّل خبراء مختلفين → MoE-Spec يحل هذا
3. **يحتاج draft model:** إعداد إضافي (EAGLE-3 يُبسط هذا)

---

## المصادر

1. **[Tier 1]** Leviathan, Y., et al., "Fast Inference from Transformers via Speculative Decoding", ICML 2023.
2. **[Tier 1]** Chen, C., et al., "Accelerating Large Language Model Decoding with Speculative Sampling", 2023.
3. **[Tier 2]** Li, Y., et al., "EAGLE-3: Scaling up Inference Acceleration", arXiv:2503.01840, 2025.

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **EAGLE-3** | **أحدث تطوير** — أسرع + مُدمج في vLLM |
| **MoE-Spec** | **يحل مشكلة MoE** — speculative decoding على MoE |
| **Continuous Batching** | **تكاملي** — يُحسّن كل طلب داخل الدفعة |
| **Inference-Time Compute** | **عكسي** — speculative يُسرّع التوليد، TTC يُبطئه عمداً |

### الحكم في 2026

> Speculative Decoding الأصلي = المبدأ الأساسي. للإنتاج استخدم **EAGLE-3** (مُدمج في vLLM).
> لنماذج MoE أضف **MoE-Spec**. لأقصى أداء (preprint) جرّب **ConFu**.
