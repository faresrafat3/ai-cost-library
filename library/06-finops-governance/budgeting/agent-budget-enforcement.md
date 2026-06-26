---
id: entry-budgetlimits-001
title_ar: حدود الإنفاق التلقائية لوكلاء الذكاء الاصطناعي
title_en: "Automatic Budget Enforcement for AI Agents"
type: practical
status: deployed
category: finops-governance
subcategory: budgeting
cost_dimensions: [api-cost, token-cost, inference-cost]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 3
created: 2026-06-26
---

# 📘 حدود الإنفاق التلقائية | Agent Budget Enforcement

> **التصنيف:** 📘 عملية | **الإثبات:** ⭐⭐⭐

## المحتوى العربي

### المشكلة

بدون حدود إنفاق، وكيل واحد يمكن أن يُنفق آلاف الدولارات في جلسة واحدة:
- **حلقات لا نهائية:** الوكيل يعيد المحاولة بلا توقف
- **تفجير السياق:** كل خطوة تُضيف توكنات والسياق ينمو أسياً
- **أدوات مكلفة:** استدعاء API خارجي يكلف $1+ لكل مرة

### الحلول المتاحة (2026)

#### 1. حد التوكن لكل جلسة
```
if cumulative_tokens > MAX_TOKENS_PER_SESSION:
    terminate_session("Budget exceeded")
```
- أبسط حل — لكن لا يميز بين توكنات مفيدة وهدر

#### 2. حد التكلفة الدولاري لكل مهمة
```
if cumulative_cost_usd > MAX_COST_PER_TASK:
    return partial_result_with_warning()
```
- أدق — يأخذ في الاعتبار اختلاف أسعار النماذج

#### 3. حد الخطوات لكل جلسة
```
if steps > MAX_STEPS:
    force_synthesis()  # اجبر الوكيل على تجميع ما لديه
```
- يمنع الحلقات اللانهائية

### الأدوات

| الأداة | الإمكانية |
|--------|----------|
| **Waxell** | إنفاذ ميزانية لكل جلسة وكيل — يوقف قبل التجاوز |
| **Pay-i** | تتبع + إنفاذ ميزانية AI مع تكامل API |
| **enzu (مفتوح المصدر)** | عقود ميزانية مُكتوبة — budget hard-stop |
| **LangSmith** | تتبع تكلفة لكل trace (بدون إنفاذ تلقائي) |

### أرقام من الصناعة

- Uber: حد **$1,500/موظف/شهر/أداة** (بعد تجاوز ميزانية سنة في 4 أشهر)
- Microsoft: إلغاء تراخيص Claude Code عبر قسم كامل (يونيو 2026)
- **التوصية:** ابدأ بحد خطوات (سهل) → أضف حد تكلفة (أدق) → أضف تنبيهات (وقائي)

---

## المصادر

1. **[Tier 2]** Waxell AI, "AI Agent FinOps: Cost Enforcement", April 2026. https://www.waxell.ai/blog/ai-agent-finops-cost-enforcement
2. **[Tier 2]** Digital Applied, "The AI Cost Reckoning", June 2026. Uber/Microsoft case studies.
3. **[Tier 3]** enzu (OSS), budget hard-stop demo. https://github.com/teilomillet/enzu
