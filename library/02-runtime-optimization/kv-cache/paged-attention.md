---
id: entry-pagedattention-001
title_ar: الانتباه المُقسَّم للصفحات — PagedAttention
title_en: "PagedAttention: Virtual Memory for KV Cache"
type: practical
status: production-proven
category: runtime-optimization
subcategory: kv-cache
cost_dimensions: [memory, throughput, inference-cost, serving-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 9
  A3: 10
  A4: 7
  B1: 7
  B2: 0
  B3: 9
  B4: 8
  C1: 8
  C2: 10
  C3: 10
  C4: 10
---

# 📘 PagedAttention — الذاكرة الافتراضية لـ KV Cache

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐
>
> **الاختراع الذي أسس vLLM وغيّر صناعة الاستدلال**

---

## المحتوى العربي

### المشكلة التي يحلها

ذاكرة KV المؤقتة تنمو خطياً مع طول السياق. التخصيص التقليدي (المتجاور) يُهدر **60-80%** من الذاكرة:

```
التخصيص التقليدي:
  الطلب 1: [████████░░░░░░░░░░░░] ← مُخصص لأقصى طول، لكن يستخدم نصفه فقط
  الطلب 2: [████░░░░░░░░░░░░░░░░] ← هدر 80%!
  الطلب 3: [لا توجد مساحة!        ] ← مرفوض رغم وجود ذاكرة خاملة
  → استغلال الذاكرة: ~20-40%

PagedAttention:
  الطلب 1: [صفحة1][صفحة2][صفحة3][صفحة4]
  الطلب 2: [صفحة5][صفحة6]
  الطلب 3: [صفحة7][صفحة8][صفحة9]
  → استغلال الذاكرة: ~96%+ (تجزئة < 4%)
```

### كيف يعمل؟

مستوحى من **الذاكرة الافتراضية** في أنظمة التشغيل:
1. **تقسيم KV cache إلى صفحات** (blocks) بحجم ثابت (مثلاً 16 توكن)
2. **تخصيص عند الطلب** — لا تُخصَّص صفحات حتى تُستخدم فعلاً
3. **عدم التجاور** — الصفحات يمكن أن تكون متفرقة في الذاكرة
4. **مشاركة الصفحات** — بادئات مشتركة تُشارك نفس الصفحات (copy-on-write)

### الأرقام (2025-2026)

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| تقليل هدر ذاكرة KV | من 60-80% إلى **< 4%** | vLLM SOSP 2023 + Introl 2026 |
| تحسن الإنتاجية | **2-4×** | Introl 2026, أكاديمي |
| تحسن مقابل TGI (تزامن عالٍ) | حتى **24×** | arXiv:2511.17593 |
| تقليل ذاكرة GPU مقابل TGI | **19-27%** | arXiv:2511.17593 |
| استغلال GPU | vLLM: **85-92%** مقابل TGI: 68-74% | arXiv:2511.17593 |
| حجم KV cache لنموذج 70B (8K سياق) | ~20 GB لكل طلب | Introl 2026 |
| دفعة 32 طلب × 70B | ~640 GB KV cache | Introl 2026 |

### لماذا PagedAttention هو الأهم عملياً؟

> **"PagedAttention وحده يُعادل مضاعفة أو أربعة أضعاف استثمار GPU — بدون شراء عتاد إضافي."**
> — Introl, مارس 2026

KV cache غالباً **يتجاوز حجم أوزان النموذج نفسها** في الذاكرة عند السياقات الطويلة والدفعات الكبيرة. PagedAttention يحل هذا.

### التوافر — أساس كل محرك حديث

| المحرك | الحالة |
|--------|--------|
| vLLM | ✅ الاختراع الأصلي — مُفعَّل افتراضياً |
| SGLang | ✅ مُفعَّل + RadixAttention (امتداد) |
| TensorRT-LLM | ✅ تطبيق مُحسَّن |
| TGI | ✅ مدعوم |

### التطورات الحديثة (2025-2026)

| التطور | ماذا يفعل |
|--------|-----------|
| **PagedEviction** | إخراج صفحات كاملة حسب الأهمية — بدون تعديل CUDA |
| **FP8 KV Cache** | تكميم الصفحات إلى FP8 → نصف الذاكرة إضافي |
| **FlexAttention** | واجهة برمجية لـ "paged attention" مُخصصة — < 2% overhead |
| **KV-Compress** | ضغط متغير لكل رأس انتباه — > 90% دقة بـ 10% ذاكرة |

### العلاقة بتقنيات أخرى

```
PagedAttention ←── أساس ──→ Continuous Batching (يعملان معاً حصرياً)
      │
      ├── يُمكّن ──→ Prefix Caching (مشاركة صفحات البادئة)
      ├── يُحسَّن بـ ──→ FP8 KV (نصف حجم الصفحات)
      ├── يمتد إلى ──→ RadixAttention (شجرة بادئات)
      └── يُضغط بـ ──→ KV Cache Compression (صفحات أقل)
```

---

## English Content

PagedAttention applies OS virtual memory concepts to KV cache: fixed-size blocks allocated on-demand, non-contiguous, shareable. Reduces memory waste from 60-80% to <4%, enabling 2-4× throughput. Foundation of vLLM and all modern serving engines. KV cache at 70B×8K = 20GB per request — PagedAttention makes this manageable.

---

## المصادر | Sources

1. **[Tier 1]** Kwon, W., et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", **SOSP 2023**. UC Berkeley — the original vLLM paper.
2. **[Tier 2]** Introl, "KV Cache Optimization: Memory Efficiency for Production LLMs", March 2026. "Equivalent to 2-4× GPU investment."
3. **[Tier 2]** Kolluru, "Comparative Analysis of LLM Inference Serving Frameworks", arXiv:2511.17593, November 2025. vLLM vs TGI benchmarks.
4. **[Tier 2]** Brenndörfer, M., "PagedAttention: Solving LLM KV Cache Memory Fragmentation", January 2026. Visual explanation + simulation.
