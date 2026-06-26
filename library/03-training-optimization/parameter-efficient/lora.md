---
id: entry-lora-001
title_ar: التكيف منخفض الرتبة — LoRA
title_en: "LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning"
type: practical
status: production-proven
category: training-optimization
subcategory: parameter-efficient
cost_dimensions: [training-cost, memory, hardware-cost, serving-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 10
  A3: 10
  A4: 6
  B1: 2
  B2: 10
  B3: 9
  B4: 0
  C1: 9
  C2: 9
  C3: 8
  C4: 10
---

# 📘 LoRA — التكيف منخفض الرتبة

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐
>
> **الأساس الذي بُنيت عليه صناعة الضبط الدقيق الفعّال بالكامل**

---

## المحتوى العربي

### ما هو LoRA؟

LoRA (Low-Rank Adaptation) — وهو تقنية تُجمّد أوزان النموذج الأصلي وتُضيف مصفوفتين صغيرتين قابلتين للتدريب (A و B) بجانب كل طبقة مُستهدفة. بدلاً من تحديث مليارات المعاملات، تُدرِّب فقط **0.1-1%** منها.

```
الأصلي: y = Wx          (W مُجمَّد — لا يتغير)
LoRA:   y = Wx + BAx     (B: d×r, A: r×d — r صغير جداً مثل 8 أو 16)
المعاملات الإضافية: 2 × d × r  (مقابل d × d للطبقة الكاملة)
```

### لماذا LoRA ثوري اقتصادياً؟

| المقياس | Full Fine-Tuning | **LoRA (r=16)** |
|---------|-----------------|----------------|
| المعاملات المُدرَّبة | 100% (مثلاً 7B) | **0.1-1%** (~10-70M) |
| ذاكرة GPU لنموذج 7B | ~28 GB (أوزان) + ~56 GB (تدرجات + محسّن) | ~28 GB (أوزان مُجمَّدة) + **~1-2 GB** (LoRA فقط) |
| تكلفة الضبط (سحابي) | ~$50-200/ساعة | **~$5-15/ساعة** |
| حجم المحول المحفوظ | ~14 GB (7B كامل) | **~10-50 MB** |
| خدمة متعددة المستأجرين | نموذج كامل لكل عميل | **نموذج أساسي واحد + محولات صغيرة** |

### النتائج — 90-99% من أداء Full FT

| المعيار | Full FT | LoRA | الفرق |
|---------|---------|------|-------|
| GLUE (متوسط) | 85-88% | 86-88% | **< 1%** |
| MT-Bench | أساس | 96-99% | **1-4%** |
| ARD-LoRA (أحدث 2025) | أساس | **99.3%** بـ 0.32% معاملات | **0.7%** فقط |

### تطورات LoRA الحديثة (2025-2026)

| الابتكار | ماذا يفعل | النتيجة |
|---------|-----------|---------|
| **DoRA (2024)** | يفصل الحجم عن الاتجاه في التحديث | جودة أعلى بنفس المعاملات |
| **ARD-LoRA (2025)** | رتبة ديناميكية لكل رأس انتباه | 99.3% FT بـ 0.32% معاملات + 41% أقل ذاكرة |
| **LoRA-FA (2026)** | تمثيل منخفض الرتبة فعّال | يُطابق Full FT على GLUE |
| **LoRASuite (2025)** | نقل المحولات بين إصدارات النموذج | 5.5 GB أقل + 78% أسرع |
| **Multi-LoRA Serving** | مئات المحولات على GPU واحد | → انظر entry-multilora-001 |

### Amazon الاكتشاف العملي (2026)

دراسة من Amazon Science:
- **o_proj فقط** هو الأفضل كإعداد افتراضي لـ LoRA
- ضمن 2% من أفضل تكوين مع **22.6% زمن استجابة أقل**
- إضافة fc2 تُحسّن المهام الصعبة بـ +15% لكن مع زمن أعلى

### متى تستخدم LoRA

- ✅ أي ضبط دقيق لنموذج موجود (الاختيار الافتراضي في 2026)
- ✅ خدمة متعددة المستأجرين (→ Multi-LoRA)
- ✅ تجريب سريع (محول صغير = تبديل سريع)
- ✅ ميزانية محدودة (10× أرخص من Full FT)

### متى لا تستخدم

- ❌ تغيير جوهري في سلوك النموذج (مثل تعليم لغة جديدة بالكامل)
- ❌ الحاجة لأقصى أداء مُمكن بدون أي تنازل
- ❌ نماذج صغيرة جداً (< 1B) — LoRA overhead نسبياً أكبر

---

## English Content

LoRA freezes base weights and adds trainable low-rank matrices (A, B) — training 0.1-1% of parameters. Achieves 90-99% of full fine-tuning quality at 10× lower cost. Foundation for QLoRA, Multi-LoRA serving, DoRA, ARD-LoRA. Amazon 2026: o_proj-only is the optimal default (2% accuracy gap, 22.6% lower latency).

---

## المصادر | Sources

1. **[Tier 1]** Hu, E., et al., "LoRA: Low-Rank Adaptation of Large Language Models", **ICLR 2022**. Microsoft. The foundational paper.
2. **[Tier 2]** Shinwari et al., "ARD-LoRA: Per-Head Dynamic Rank", June 2025. 99.3% of FT with 0.32% params.
3. **[Tier 2]** Amazon Science, "Optimizing LoRA Target Module Selection", 2026. o_proj best default.
4. **[Tier 2]** Emergent Mind, "LoRA Adaptation: Efficient Low-Rank Fine-Tuning", December 2025. Comprehensive survey of 20+ variants.
