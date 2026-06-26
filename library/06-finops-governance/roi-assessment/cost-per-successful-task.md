---
id: entry-cpst-001
title_ar: تكلفة المهمة الناجحة — المقياس الصحيح لعام 2026
title_en: "Cost per Successful Task (CPST): The Right Metric for 2026"
type: practical
status: emerging-practice
category: finops-governance
subcategory: roi-assessment
cost_dimensions: [inference-cost, api-cost, engineering-cost]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 5
  A2: 6
  A3: 4
  A4: 10
  B1: 0
  B2: 0
  B3: 0
  B4: 0
  C1: 5
  C2: 10
  C3: 10
  C4: 3
---

# 📘 تكلفة المهمة الناجحة | Cost per Successful Task (CPST)

> **التصنيف:** 📘 ممارسة ناشئة | **الإثبات:** ⭐⭐⭐
>
> **"تحسين المقياس الخطأ هو كيف تُقلل تكلفة التوكن بينما التكلفة الحقيقية ترتفع بصمت."** — Digital Applied 2026

---

## المحتوى العربي

### لماذا تكلفة التوكن مقياس مُضلل؟

تكلفة التوكن تقيس **سعر الوحدة** — لكنها لا تجيب: "كم كلفني **إنجاز مهمة بنجاح**؟"

### ثلاثة أمثلة تُثبت المشكلة

#### مثال 1: نموذجان بنفس التكلفة الفعلية
| | النموذج الرخيص | النموذج الغالي |
|---|--------------|-------------|
| سعر التوكن | $0.001 | $0.005 |
| محاولات للنجاح | 5 | 1 |
| توكنات لكل محاولة | 1,000 | 1,000 |
| **CPST** | **$0.005** | **$0.005** |
| الحكم | **متساويان!** | |

#### مثال 2: "Overthinking Tax" — الأصغر أغلى
**من OckBench (arXiv:2511.05722):**
| | DeepSeek-R1 7B | DeepSeek-R1 14B |
|---|--------------|----------------|
| سعر التوكن | $0.05/M | $0.10/M |
| توكنات لكل استعلام | 41,415 | 13,211 |
| **CPST** | **$2.07** | **$1.32** |
| الحكم | **أغلى 57%!** | |

#### مثال 3: Bain Survey — الوهم الكبير
**Bain & Company (951 شركة, 2026):**
- استهدفوا 11-20% وفر من AI
- **40% حققوا أقل من 10%** فعلياً
- السبب: يقيسون تكلفة التوكن بدلاً من القيمة المُنتَجة

### كيف تُحسب CPST؟

```
CPST = الإنفاق الكلي / المهام المُنجزة بنجاح

الإنفاق الكلي يشمل:
  + توكنات الإدخال (كل المحاولات — ناجحة وفاشلة)
  + توكنات الإخراج
  + تكلفة الأدوات (API خارجية, بحث, استرجاع)
  + تكلفة إعادة المحاولات الفاشلة
  + (اختياري) وقت المهندس للتدخل اليدوي

المهام الناجحة:
  = تذاكر محلولة / PRs مدمجة / عملاء مؤهلون / إجابات صحيحة
```

### لماذا CPST أفضل من بدائله؟

| المقياس | ماذا يقيس | المشكلة |
|---------|-----------|---------|
| $/M tokens | سعر الحوسبة الخام | لا يقيس النجاح |
| $/query | تكلفة الطلب | لا يميز نجاح/فشل |
| $/API call | تكلفة الاستدعاء | وكيل = 10-20 استدعاء |
| **$/successful task** | **القيمة المُنتَجة** | **✅ الوحيد الذي يربط التكلفة بالقيمة** |

### كيف تُطبقه عملياً؟

1. **حدد المهمة:** ما يُعتبر "نجاح"؟
   - خدمة عملاء: تذكرة مُغلقة بدون تصعيد
   - كود: PR مُدمج يجتاز الاختبارات
   - محتوى: مقال مُنشور بدون تعديل بشري
   
2. **أدوات التتبع:**
   - Helicone: يتتبع التكلفة لكل trace
   - LangSmith: يربط التكلفة بنتيجة المهمة
   - مُخصص: tag كل استدعاء بـ task_id + outcome
   
3. **اجمع أسبوعياً:** CPST لكل نموذج × نوع مهمة
4. **قارن:** أي نموذج أرخص **لكل مهمة ناجحة** (وليس لكل توكن)

### من يستخدم CPST (2026)

- **Digital Applied:** يوصي به كـ "North Star Metric"
- **Uber:** بعد تجاوز الميزانية — بدأ يقيس تكلفة لكل PR
- **FinOps Foundation:** يُدرجه في إطار AI FinOps

---

## English Content

Cost per Successful Task = total spend (including retries, failures, tool calls) ÷ successful completions. A 7B model at $0.05/M tokens costs 57% MORE than a 14B model at $0.10/M per successful task due to "overthinking." Bain survey of 951 companies: 40% achieved <10% AI savings because they optimized the wrong metric.

---

## المصادر

1. **[Tier 2]** Digital Applied, "The AI Cost Reckoning", June 2026. "Cost per successful task" as North Star.
2. **[Tier 2]** "OckBench: Measuring LLM Reasoning Efficiency", arXiv:2511.05722, 2025-2026. Overthinking Tax data.
3. **[Tier 2]** Bain & Company, "Automation and AI Pathfinder Survey 2026" (n=951). 40% underperformed.
4. **[Tier 2]** TechTimes, "Enterprise AI Budgets: 5-Driver Audit", June 2026. 65% spend recoverable.
