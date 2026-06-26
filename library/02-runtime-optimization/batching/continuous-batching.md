---
id: entry-contbatching-001
title_ar: التجميع المستمر
title_en: "Continuous Batching: The Single Biggest Inference Lever"
type: practical
status: production-proven
category: runtime-optimization
subcategory: batching
cost_dimensions: [inference-cost, throughput, compute]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 8
  A3: 10
  A4: 7
  B1: 9
  B2: 0
  B3: 3
  B4: 10
  C1: 8
  C2: 10
  C3: 10
  C4: 10
---

# 📘 التجميع المستمر | Continuous Batching

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐
>
> **"أكبر رافعة واحدة لتقليل تكلفة الاستدلال"** — Spheron 2026

---

## المحتوى العربي

### ما هو التجميع المستمر؟

التجميع المستمر (Continuous Batching) — وهو تقنية جدولة ديناميكية تُدخل طلبات جديدة وتُخرج طلبات مُنتهية في كل خطوة توليد (iteration)، بدلاً من انتظار اكتمال الدفعة بأكملها.

### لماذا هو الأهم؟

**بدون تجميع مستمر:**
```
الطلب 1: [████████████████░░░░░░░░] (طويل)
الطلب 2: [████░░░░░░░░░░░░░░░░░░░] (قصير — لكن GPU ينتظر الطلب 1!)
الطلب 3: [ينتظر...                 ] (لا يبدأ حتى تنتهي الدفعة)
→ GPU مُستغل ~20%
```

**مع تجميع مستمر:**
```
الطلب 1: [████████████████]
الطلب 2: [████] → الطلب 4: [████████]
الطلب 3:    [██████████████]
→ GPU مُستغل ~70-80%
```

### الأرقام

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| تحسن استغلال GPU | من <20% إلى **70-80%** | Spheron 2026 |
| تقليل التكلفة الفعلية لكل توكن | **3-4×** | Spheron 2026, Mirantis 2026 |
| NVIDIA + Amdocs | 60% تقليل توكنات + 40% تقليل استدلال + 80% تقليل زمن | NVIDIA case study |
| NVIDIA + Snap/Screenshop | 3× إنتاجية + ~66% تقليل تكلفة | NVIDIA (TensorRT) |

### كيف يعمل؟

1. **طابور ديناميكي:** طلبات جديدة تدخل فوراً بدون انتظار
2. **إنهاء مبكر:** الطلبات القصيرة تُحرَّر فوراً
3. **جدولة على مستوى الخطوة:** كل iteration = فرصة لإدخال/إخراج طلبات
4. **KV Cache منفصل:** كل طلب له كتل KV مستقلة (عبر PagedAttention)

### التوافر — مدمج في كل محرك

| المحرك | الحالة | ملاحظات |
|--------|--------|---------|
| vLLM | ✅ مُفعَّل افتراضياً | الخيار الأول |
| TensorRT-LLM | ✅ مُفعَّل | أسرع مع Triton |
| SGLang | ✅ مُفعَّل | + RadixAttention |
| TGI | ✅ مُفعَّل | HuggingFace |

### العلاقة بتقنيات أخرى

| التقنية | العلاقة |
|---------|---------|
| PagedAttention | **تبعية** — التجميع المستمر يعمل أفضل بكثير مع PagedAttention |
| FP8/INT4 | **تكاملي** — تكميم يُحرر ذاكرة → دفعات أكبر → استغلال أعلى |
| Speculative Decoding | **تكاملي** — يُحسّن كل طلب داخل الدفعة |
| EAGLE-3 | **تكاملي** — EAGLE-3 يعمل ضمن continuous batching في vLLM |

### لماذا ⭐⭐⭐⭐؟

- ✅ Gate 1: مبني في كل محرك استدلال حديث
- ✅ Gate 2: معايير شاملة مع أرقام واضحة
- ✅ Gate 3: مُنشَر في كل خدمة استدلال إنتاجية
- ✅ Gate 4: 3-4× تقليل تكلفة — أكبر رافعة واحدة

---

## English Content

Continuous batching dynamically inserts and removes requests at each decode iteration instead of waiting for batch completion. It raises GPU utilization from <20% to 70-80%, reducing effective cost per token by 3-4×. Built into vLLM, TensorRT-LLM, SGLang, and TGI — the single biggest inference optimization lever.

---

## المصادر | Sources

1. **[Tier 2]** Spheron, "AI Inference Cost Economics 2026", April 2026. "The single biggest lever."
2. **[Tier 2]** Mirantis, "Optimizing Inference Costs: The Complete Guide", March 2026. NVIDIA case studies.
3. **[Tier 1]** Yu, G., et al., "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI 2022. Original continuous batching.
