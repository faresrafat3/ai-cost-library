---
id: entry-ipw-001
title_ar: الاستدلال المحلي مقابل السحابي — الذكاء لكل واط
title_en: "Local vs Cloud Inference: Intelligence per Watt (IPW)"
type: practical
status: validated
category: infrastructure
subcategory: deployment-strategies
tree_path: "AI Cost Library → Infrastructure → Deployment Strategies → Local vs Cloud"
cost_dimensions:
  - energy
  - compute
  - inference-cost
  - hardware-cost
  - latency
proof_score: "⭐⭐⭐ مُتحقق | Validated"
sources_count: 1
created: 2026-06-26
updated: 2026-06-26
research_review:
  paper_read: true
  abstract_fully_read: true
  results_section_read: true
  decision: "يُضاف — أكبر دراسة تجريبية (1M+ استعلام, 20+ نموذج, 8 مسرّعات), Stanford (Hennessy + Ré)"
  limitations_noted: "single-turn فقط, لا يشمل وكلاء, preprint"
---

# 📘 الاستدلال المحلي مقابل السحابي | Local vs Cloud Inference (IPW)

> **التصنيف:** 📘 عملية — بيانات تجريبية واسعة | **الإثبات:** ⭐⭐⭐ مُتحقق
>
> **المسار:** المكتبة ← البنية التحتية ← استراتيجيات النشر

---

## المحتوى العربي

### ما هو هذا البحث؟

أكبر دراسة تجريبية لقياس قابلية الاستدلال المحلي (على أجهزة المستخدم) كبديل للسحابي. يقدم مقياس **Intelligence per Watt (IPW)** — الذكاء لكل واط — كمقياس موحّد للقدرة والكفاءة.

**الفريق:** Stanford (Christopher Ré — مبتكر FlashAttention، John Hennessy — مبتكر RISC ورئيس Alphabet السابق)

### النتائج الأساسية

| الادعاء | القيمة | التفاصيل |
|---------|--------|----------|
| نسبة الاستعلامات التي تجيبها النماذج المحلية بنجاح | **88.7%** | على 1M+ استعلام حقيقي |
| تحسّن IPW خلال 2023-2025 | **5.3×** | تقدم خوارزمي (3.2×) + عتادي (1.7×) |
| نمو تغطية الاستعلامات القابلة للخدمة محلياً | 23.2% → 71.3% | من 2023 إلى 2025 |
| كفاءة المسرّعات المحلية مقابل السحابية | **1.4× أفضل محلياً** | IPW أعلى على نفس النماذج |
| وفر أنظمة هجينة (محلي + سحابي) | **40-65%** | في الطاقة والتكلفة والحوسبة |

### المقياس الجديد: IPW (الذكاء لكل واط)

```
IPW = دقة المهمة / القدرة الكهربائية المستهلكة (واط)
```

لماذا هذا المقياس مهم:
- يجمع بين **القدرة** (هل النموذج يجيب صحيحاً؟) و**الكفاءة** (بكم طاقة؟) في رقم واحد
- يسمح بمقارنة تجهيزات مختلفة (نموذج + مسرّع) بشكل عادل

### ماذا يعني عملياً؟

1. **71% من الاستعلامات يمكن خدمتها محلياً** — لا تحتاج سحابة
2. **الأنظمة الهجينة هي المستقبل:** نموذج محلي للأغلبية + سحابي للمعقد = 40-65% وفر
3. **IPW تتحسن 5× كل سنتين** — المحلي يصبح أقوى بسرعة
4. **Apple M4 Max وأمثاله** كافية لتشغيل نماذج ≤20B بزمن تفاعلي

### حجم الدراسة

| المقياس | القيمة |
|---------|--------|
| عدد الاستعلامات | 1,000,000+ |
| عدد النماذج | 20+ |
| عدد المسرّعات | 8 (محلية وسحابية) |
| الفترة الزمنية | 2023-2025 |
| المعايير | MMLU Pro, SuperGPQA, محادثات حقيقية |

### لماذا ⭐⭐⭐ وليس ⭐⭐⭐⭐؟

- ✅ أكبر دراسة من نوعها
- ✅ فريق Stanford من الدرجة الأولى
- ✅ بيانات تجريبية ضخمة
- ❌ single-turn فقط — لا يشمل وكلاء أو محادثات متعددة
- ❌ preprint (لكن v4 — نضج عالٍ)
- ❌ لا يوجد نشر إنتاجي موثق لنظام هجين بناءً على هذا البحث

---

## English Content

The largest empirical study of local vs cloud inference (1M+ queries, 20+ models, 8 accelerators, Stanford team including John Hennessy and Christopher Ré).

Key findings: Local LMs answer 88.7% of queries. IPW improved 5.3× from 2023-2025. Hybrid systems achieve 40-65% savings.

---

## المصادر | Sources

1. **[Tier 2]** Saad-Falcon, J., Narayan, A., ..., Hennessy, J., Mirhoseini, A., Ré, C., "Intelligence per Watt: Measuring Intelligence Efficiency of Local AI", arXiv:2511.07885v4, November 2025 (revised May 2026). Stanford University.
