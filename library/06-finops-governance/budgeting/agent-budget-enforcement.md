---
id: entry-budgetlimits-001
title_ar: حدود الإنفاق التلقائية لوكلاء الذكاء الاصطناعي
title_en: "Agent Budget Enforcement: Preventing Runaway AI Costs"
type: practical
status: deployed
category: finops-governance
subcategory: budgeting
cost_dimensions: [api-cost, token-cost, inference-cost]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 6
  A2: 5
  A3: 5
  A4: 10
  B1: 5
  B2: 0
  B3: 0
  B4: 0
  C1: 7
  C2: 7
  C3: 7
  C4: 6
---

# 📘 حدود الإنفاق التلقائية | Agent Budget Enforcement

> **التصنيف:** 📘 عملية | **الإثبات:** ⭐⭐⭐
>
> **"التنبيهات بعد الإنفاق لا تعمل — تحتاج حدود تُوقف قبل التجاوز."** — Waxell 2026

---

## المحتوى العربي

### لماذا هذا حرج؟

بدون حدود إنفاق، وكيل واحد يمكن أن يُولّد فاتورة كارثية:

| السيناريو الكابوسي | ماذا يحدث |
|-------------------|----------|
| **حلقة لا نهائية** | الوكيل يعيد نفس الخطوة 100+ مرة |
| **تفجير السياق** | كل خطوة تُضيف 5K توكن → الخطوة 20 = 100K+ سياق |
| **أدوات مكلفة** | كل استدعاء أداة = $0.50-5.00 |
| **إعادة محاولات بدون توقف** | فشل → إعادة → فشل → إعادة... |

**أمثلة حقيقية (2026):**
- **Uber:** استنفد ميزانية **سنة كاملة** لأدوات AI في **4 أشهر** → فرض حد $1,500/موظف/شهر
- **Microsoft:** ألغت تراخيص Claude Code عبر **قسم كامل** (يونيو 2026)
- **Gartner:** توقع **40%+** من مشاريع الوكلاء تُلغى بحلول 2027 بسبب التكاليف

### ثلاث طبقات حماية

#### الطبقة 1: حد الخطوات (أبسط — ابدأ هنا)
```python
MAX_STEPS = 25

for step in range(MAX_STEPS):
    result = agent.step()
    if result.is_done:
        break
else:
    # بلغ الحد → اجبر الوكيل على تجميع ما لديه
    result = agent.force_synthesis("Summarize findings so far")
```
**الوفر:** يمنع الحلقات اللانهائية. **التكلفة:** صفر. **القيد:** لا يميز بين خطوات رخيصة وغالية.

#### الطبقة 2: حد التكلفة الدولاري (أدق)
```python
MAX_COST_USD = 2.00  # لكل مهمة

def track_cost(response):
    cost = (response.input_tokens * INPUT_PRICE + 
            response.output_tokens * OUTPUT_PRICE)
    session.cumulative_cost += cost
    
    if session.cumulative_cost > MAX_COST_USD:
        return force_early_termination()
```
**الوفر:** حماية دقيقة. **التكلفة:** يحتاج تتبع أسعار النماذج. **القيد:** الأسعار تتغير.

#### الطبقة 3: حد تلقائي مع تنبيهات (الأمثل)
```python
# Waxell-style: ميزانية لكل جلسة مع إنفاذ فوري
config = {
    "max_cost_per_session": 5.00,
    "max_steps": 30,
    "alert_at": [0.50, 0.80],  # تنبيه عند 50% و80%
    "on_exceed": "terminate_with_partial_result"
}
```

### الأدوات المتاحة (2026)

| الأداة | النوع | ماذا تفعل | مناسبة لـ |
|--------|-------|-----------|----------|
| **Waxell** | تجاري | إنفاذ ميزانية لكل جلسة وكيل — real-time | فرق وكلاء |
| **Pay-i** | تجاري | تتبع + إنفاذ عبر مزودين متعددين | مؤسسات |
| **enzu** (OSS) | مفتوح | عقود ميزانية مُكتوبة — hard stop | مطورون |
| **LangSmith** | تجاري | تتبع تكلفة لكل trace (بدون إنفاذ تلقائي) | تشخيص |
| **Anthropic API** | مزود | `max_tokens` لكل استدعاء (ليس لكل جلسة) | أساسي |

### خطة تطبيق عملية

```
الأسبوع 1: أضف حد خطوات (MAX_STEPS=25) → يمنع الكوارث
الأسبوع 2: أضف تتبع تكلفة (Helicone/LangSmith) → تعرف أين المال
الأسبوع 3: أضف تنبيهات (50%, 80% من الميزانية) → إنذار مبكر
الأسبوع 4: أضف إنفاذ تلقائي (Waxell/Pay-i) → حماية كاملة
```

### العلاقة بتقنيات أخرى

| التقنية | العلاقة |
|---------|---------|
| **Model Routing** | **تكاملي** — وجّه المهام الفرعية لنماذج أرخص |
| **AgentDiet** | **تكاملي** — قلل التوكنات → الميزانية تكفي أكثر |
| **CPST** | **يعتمد عليه** — بدون CPST لا تعرف هل الميزانية كافية |
| **AI FinOps** | **أساسي** — البوابة بدون مراقبة = عمياء |

---

## المصادر

1. **[Tier 2]** Waxell AI, "The $400M AI FinOps Gap: Cost Enforcement", April 2026. Per-session enforcement.
2. **[Tier 2]** Digital Applied, "The AI Cost Reckoning", June 2026. Uber $1,500/employee cap.
3. **[Tier 3]** enzu (OSS), "Budget Hardstop Demo", 2026. github.com/teilomillet/enzu
4. **[Tier 2]** FinOps Foundation, "FinOps for AI: Tools Considerations", April 2026. Gateway guardrails.
