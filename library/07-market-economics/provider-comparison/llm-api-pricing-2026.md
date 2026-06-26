---
id: entry-apipricing-001
title_ar: مقارنة أسعار واجهات برمجة النماذج اللغوية (يونيو 2026)
title_en: "LLM API Pricing Comparison (June 2026)"
type: practical
status: current
category: market-economics
subcategory: provider-comparison
cost_dimensions: [api-cost, token-cost, inference-cost]
proof_score: "⭐⭐⭐ بيانات سوقية فعلية | Market Data"
sources_count: 3
created: 2026-06-26
research_review:
  decision: "يُضاف — بيانات أسعار فعلية من 3 مصادر مستقلة. ضرورية لاتخاذ قرارات التكلفة."
  limitations_noted: "الأسعار تتغير بسرعة — هذه لقطة يونيو 2026"
---

# 📘 مقارنة أسعار واجهات برمجة النماذج اللغوية | LLM API Pricing (June 2026)

> **التصنيف:** 📘 بيانات سوقية فعلية | **الحالة:** يونيو 2026
>
> **المسار:** المكتبة ← اقتصاديات السوق ← مقارنة المزودين

---

## المحتوى العربي

### ⚠️ تنبيه: الأسعار تتغير بسرعة — هذه لقطة يونيو 2026

### جدول الأسعار الشامل (مرتب من الأرخص)

| المزود | النموذج | الإدخال $/M | الإخراج $/M | السياق | الجودة* |
|--------|---------|-------------|-------------|--------|---------|
| Google | Gemini 2.0 Flash | $0.10 | $0.40 | 1M | ~65 |
| Mistral | Mistral Small | $0.10 | $0.30 | 128K | ~60 |
| DeepSeek | V4 Flash | **$0.14** | **$0.28** | 1M | ~70 |
| OpenAI | GPT-5.4-nano | $0.20 | $1.25 | 1M | ~68 |
| Google | Gemini 3.1 Flash-Lite | $0.25 | $1.50 | 1M | ~73 |
| MiniMax | M3 | $0.30 | $1.20 | 1M | ~65 |
| OpenAI | GPT-5.4-mini | $0.75 | $4.50 | 400K | ~75 |
| Anthropic | Claude Haiku 4.5 | $1.00 | $5.00 | 200K | ~73 |
| Moonshot | Kimi K2.6 | $0.95 | $4.00 | 256K | ~81 |
| Google | Gemini 3.5 Flash | $1.50 | $9.00 | 1M | ~86 |
| DeepSeek | V4 Pro (Max) | $1.74 | $3.48 | 1M | **88** |
| OpenAI | GPT-5.4 | $2.50 | $15.00 | 1M | ~80 |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $15.00 | 1M | ~82 |
| Anthropic | Claude Opus 4.8 | $5.00 | $25.00 | 1M | ~86 |
| OpenAI | GPT-5.5 | $5.00 | $30.00 | 1M | ~87 |
| Anthropic | Claude Fable 5 | $10.00 | $50.00 | 1M+ | **~85** |
| OpenAI | o3 | $10.00 | $40.00 | 200K | ~82 |

*الجودة: درجة تقريبية مُجمّعة من BenchLM (ليست معياراً رسمياً)*

### الأرقام الأهم

| المقياس | القيمة |
|---------|--------|
| **فرق السعر بين الأرخص والأغلى (إدخال)** | **150×** ($0.10 vs $15.00) |
| **فرق السعر بين الأرخص والأغلى (إخراج)** | **250×** ($0.28 vs $75.00) |
| **أفضل نسبة جودة/سعر** | DeepSeek V4 Pro Max (88 نقطة بـ $1.74) |
| **أرخص نموذج بسياق 1M** | DeepSeek V4 Flash ($0.14 إدخال) |
| **أرخص مزود حدودي** | DeepSeek V4 Pro ($1.74 مقابل $5+ لـ OpenAI/Anthropic) |

### استراتيجية التوجيه بناءً على الأسعار

| نوع المهمة | النموذج الموصى | التكلفة | السبب |
|-----------|--------------|---------|-------|
| تصنيف / استخراج | GPT-5.4-nano أو DeepSeek V4 Flash | $0.10-0.20/M | أرخص مع جودة كافية |
| تلخيص روتيني | Claude Haiku 4.5 أو GPT-5.4-mini | $0.75-1.00/M | توازن |
| استدلال متعدد الخطوات | DeepSeek V4 Pro أو Gemini 3.5 Flash | $1.50-1.74/M | أفضل جودة/سعر |
| تركيب سياق طويل | Claude Sonnet 4.6 أو GPT-5.4 | $2.50-3.00/M | سياق 1M + جودة |
| تنسيق وكلاء | Claude Opus 4.8 أو GPT-5.5 | $5.00/M | أعلى جودة مطلوبة |
| إبداعي / حكم دقيق | Claude Fable 5 | $10.00/M | أعلى مستوى |

### ⚠️ تحذيرات

1. **تكلفة الإخراج أعلى بكثير:** النسبة النموذجية 3-6× — نموذج رخيص الإدخال قد يكون غالي الإخراج
2. **الأسعار تنخفض بسرعة:** هذا الجدول صالح ليونيو 2026 — راجع المصادر للأحدث
3. **الجودة ≠ السعر:** DeepSeek V4 Pro يحقق 88 نقطة بثلث سعر GPT-5.5
4. **النماذج المفتوحة:** استضافة ذاتية لـ Qwen3.5 أو Llama قد تكون أرخص بـ 10×+ للأحمال الثابتة

---

## المصادر | Sources

1. **[Tier 2]** BenchLM, "LLM API Pricing Comparison 2026", June 2026. https://benchlm.ai/llm-pricing
2. **[Tier 2]** MorphLLM, "LLM API Providers 2026: 12 APIs Compared", June 2026. https://www.morphllm.com/llm-api
3. **[Tier 2]** PE Collective, "LLM API Pricing 2026: 20+ Models", April 2026. https://pecollective.com/blog/llm-api-pricing-comparison/
