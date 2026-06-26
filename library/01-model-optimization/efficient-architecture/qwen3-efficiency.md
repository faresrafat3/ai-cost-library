---
id: entry-qwen3-001
title_ar: كفاءات Qwen3 — دمج التفكير واللا-تفكير في نموذج واحد
title_en: "Qwen3 Efficiency: Thinking/Non-Thinking Fusion & Budget Control"
type: practical
status: production-proven
category: model-optimization
subcategory: efficient-architecture
cost_dimensions: [inference-cost, api-cost, throughput, training-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 2
created: 2026-06-26
scoring:
  A1: 10
  A2: 9
  A3: 9
  A4: 10
  B1: 8
  B2: 7
  B3: 5
  B4: 7
  C1: 8
  C2: 8
  C3: 9
  C4: 9
---

# 📘 كفاءات Qwen3 — دمج التفكير واللا-تفكير

> **التصنيف:** 📘 عملية — إنتاج | **الإثبات:** ⭐⭐⭐⭐
>
> **نموذج واحد يعمل كروبوت محادثة سريع أو مُفكِّر عميق — حسب الطلب**

---

## المحتوى العربي

### ما الجديد في Qwen3 اقتصادياً؟

عادة تحتاج **نموذجين** منفصلين:
- نموذج محادثة سريع (مثل GPT-4o) للمهام البسيطة
- نموذج تفكير (مثل o3, R1) للمهام المعقدة

Qwen3 يدمجهما في **نموذج واحد** مع **مفتاح تحكم في ميزانية التفكير**:

```python
# نفس النموذج — وضعان مختلفان:

# وضع سريع (لا تفكير) — رخيص
response = qwen3.generate(prompt, thinking=False)  # → إجابة فورية

# وضع تفكير — أغلى لكن أدق
response = qwen3.generate(prompt, thinking=True)   # → سلسلة تفكير + إجابة

# ميزانية تفكير محددة — أوسط
response = qwen3.generate(prompt, thinking_budget=1000)  # → حد 1000 توكن تفكير
```

### التأثير الاقتصادي

| الميزة | التأثير على التكلفة |
|--------|-------------------|
| **نموذج واحد بدل اثنين** | نصف تكلفة النشر والصيانة |
| **ميزانية تفكير قابلة للضبط** | تدفع فقط على قدر التعقيد |
| **عائلة أحجام كاملة** | 0.6B إلى 235B — نموذج لكل ميزانية |

### العائلة الكاملة

| النموذج | النوع | المعاملات | أفضل لـ |
|---------|-------|----------|---------|
| Qwen3-0.6B | Dense | 0.6B | أجهزة طرفية |
| Qwen3-4B | Dense | 4B | محمول / منخفض التكلفة |
| Qwen3-8B | Dense | 8B | GPU واحد |
| Qwen3-32B | Dense | 32B | التوازن الأمثل |
| **Qwen3-30B-A3B** | **MoE** | 30B/3B active | **أرخص MoE** |
| **Qwen3-235B-A22B** | **MoE** | 235B/22B active | **الرائد** |

### Qwen3-235B-A22B — أرقام

| المعيار | Qwen3-235B | DeepSeek-V3 | o3-mini |
|---------|-----------|------------|---------|
| AIME'24 | 85.7% | 79.8% | 87.3% |
| LiveCodeBench v5 | 70.7% | 63.4% | 67.0% |
| BFCL v3 (أدوات) | 70.8% | 64.0% | — |

مع **22B مُفعَّلة فقط** — تكلفة استدلال ≈ نموذج 22B!

### لماذا "Thinking Budget" يُغيّر الاقتصاد؟

من بحث Qwen3 التقني:
> **زيادة ميزانية التفكير تُحسّن الأداء بشكل متسق عبر المهام.**

هذا يعني: يمكنك **ضبط نسبة التكلفة/الجودة لكل طلب** بدلاً من اختيار نموذج ثابت:
- استعلام بسيط → `thinking_budget=0` → رخيص
- استعلام معقد → `thinking_budget=2000` → أغلى لكن أدق
- **نفس النموذج، نفس النشر، نفس الـ GPU**

### التدريب — 36T tokens

| المقياس | القيمة |
|---------|--------|
| بيانات التدريب المسبق | **36T+ tokens** (أكبر من Llama 3 بـ 2.4×) |
| اللغات | 119 لغة |
| ابتكار التدريب | Thinking Mode Fusion — دمج التفكير في نموذج واحد عبر SFT مستمر |
| الاستخلاص | نماذج أصغر مُستخلصة من النموذج الرائد (أرخص من التدريب من الصفر) |

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **MoE Economics** | **يُطبّق** — Qwen3-235B = MoE 235B/22B active |
| **Inference-Time Compute** | **يُحل** — thinking budget = تحكم مباشر في TTC cost |
| **Overthinking Tax** | **يتجنب** — ميزانية تفكير تمنع الإفراط |
| **Model Routing** | **بديل جزئي** — نموذج واحد بوضعين بدل نموذجين |
| **Llama 4 / DeepSeek V4** | **منافسان** — كلهم MoE مفتوحة في 2026 |

---

## المصادر

1. **[Tier 1]** Qwen Team, "Qwen3 Technical Report", arXiv:2505.09388, May 2025. 36T tokens, thinking/non-thinking fusion.
2. **[Tier 2]** Apidog, "Best Qwen Models in 2026", January 2026. Practical comparison.
