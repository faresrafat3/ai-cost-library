---
id: entry-subquad-001
title_ar: النماذج دون التربيعية — Mamba-3 وبدائل Transformer
title_en: "Sub-Quadratic Models: Mamba-3 and Transformer Alternatives for Inference Efficiency"
type: emerging
status: peer-reviewed
category: model-optimization
subcategory: efficient-architecture
cost_dimensions: [inference-cost, memory, throughput, latency]
proof_score: "⭐⭐ نموذج أولي مُراجع | Peer-Reviewed Prototype"
sources_count: 2
created: 2026-06-26
scoring:
  A1: 4
  A2: 10
  A3: 7
  A4: 10
  B1: 7
  B2: 5
  B3: 7
  B4: 8
  C1: 2
  C2: 5
  C3: 6
  C4: 3
research_review:
  paper_read: true
  abstract_fully_read: true
  decision: "يُضاف — ICLR 2026 (Tier 1). يُحدد حدود Pareto الجديدة للأداء/الاستدلال."
  limitations_noted: "لم تُنشر نماذج إنتاجية كبيرة بعد. الغالبية العظمى تبقى Transformer."
---

# 🧪 النماذج دون التربيعية — Mamba-3 | Sub-Quadratic Models

> **التصنيف:** 🧪 ناشئة — مُراجعة أقران | **الإثبات:** ⭐⭐
>
> **المسار:** المكتبة ← تحسين النموذج ← البنية الفعّالة

---

## المحتوى العربي

### المشكلة مع Transformer

الانتباه الذاتي (Self-Attention) في Transformer يتناسب **تربيعياً** مع طول السياق:
- سياق 4K: حوسبة ×1
- سياق 32K: حوسبة **×64**
- سياق 128K: حوسبة **×1024**

وذاكرة KV cache تنمو **خطياً** — مما يجعل السياقات الطويلة باهظة.

### Mamba-3 — الحل الجديد (ICLR 2026)

Mamba-3 يجمع 3 ابتكارات مستوحاة من نماذج فضاء الحالة (State Space Models):
1. **تكرار أكثر تعبيرية** (more expressive recurrence)
2. **قاعدة تحديث حالة مُعقدة** (complex state update) — تتبع حالة أغنى
3. **صياغة متعددة المدخلات والمخرجات** (MIMO) — استغلال أفضل للعتاد

### الميزة الاقتصادية الأساسية

| المعيار | Transformer | **Mamba-3** |
|---------|-------------|-----------|
| حوسبة التوليد | **خطية بطول السياق** (KV cache) | **ثابتة** (حالة ثابتة الحجم!) |
| ذاكرة التوليد | **خطية** (KV cache ينمو) | **ثابتة** |
| حوسبة Prefill | تربيعية | **خطية** |

> **النتيجة:** سياق 128K يكلف نفس تكلفة سياق 4K في مرحلة Decode!

### لماذا ⭐⭐ وليس أعلى؟

- ✅ ICLR 2026 — أعلى مؤتمرات التعلم الآلي
- ✅ يُحدد حدود Pareto جديدة (أداء أعلى لنفس ميزانية الاستدلال)
- ❌ لا توجد نماذج إنتاجية كبيرة (>7B) مبنية على Mamba-3 بعد
- ❌ Transformer مازال المعيار — كل النماذج الحدودية Transformer/MoE
- ❌ نظام بيئي محدود — أدوات الاستدلال مُحسّنة لـ Transformer

### Falcon-H1R — هجين ناجح (يناير 2026)

Falcon-H1R (7B) يجمع Transformer + Mamba:
- **96.7% دقة على AIME25** مع **38% توكنات أقل** من DeepSeek-R1
- يُثبت أن البنى الهجينة يمكن أن تتفوق على Transformer الصرف

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **KV Cache Compression** | **يُلغي الحاجة** — Mamba لا يحتاج KV cache |
| **PagedAttention** | **لا يحتاجه** — لا يوجد KV cache ليُدار |
| **Inference-Time Compute** | **تكاملي** — Mamba أكفأ للتفكير الطويل (ذاكرة ثابتة) |
| **Architecture-Aware Scaling** | **يُوسّع** — يُضيف بُعد "نوع البنية" للتحجيم |

### الحكم في 2026

> **مراقبة عن كثب.** Mamba-3 يحل مشكلة حقيقية (التكلفة التربيعية) لكن Transformer مازال مُهيمناً. البنى الهجينة (Transformer + SSM) هي الاتجاه الأكثر واقعية في المدى القريب.

---

## المصادر

1. **[Tier 1]** "Mamba-3", **ICLR 2026**. Sets Pareto frontier for performance under fixed inference budget.
2. **[Tier 2]** "Falcon-H1R: Reasoning-Optimized 7B Model", arXiv:2601.02346, January 2026. Hybrid Transformer-Mamba, 96.7% AIME25.
