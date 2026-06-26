---
id: entry-promptcache-001
title_ar: تخزين البادئات مؤقتاً
title_en: "Prompt/Prefix Caching: 90% Cost Reduction on Cached Portions"
type: practical
status: production-proven
category: runtime-optimization
subcategory: caching
cost_dimensions: [api-cost, token-cost, inference-cost, latency]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 7
  A3: 9
  A4: 8
  B1: 9
  B2: 0
  B3: 0
  B4: 3
  C1: 9
  C2: 9
  C3: 9
  C4: 10
---

# 📘 تخزين البادئات مؤقتاً | Prompt/Prefix Caching

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐

---

## المحتوى العربي

### ما هو تخزين البادئات؟

تخزين البادئات مؤقتاً (Prompt/Prefix Caching) — وهو إعادة استخدام حسابات مرحلة Prefill لبادئات الموجّهات المتكررة (system prompt, few-shot examples, مستندات مرجعية) بدلاً من إعادة حسابها مع كل طلب.

### كيف يوفر المال؟

| السيناريو | بدون تخزين | مع تخزين | التوفير |
|-----------|-----------|---------|---------|
| system prompt 2K tokens × 1000 طلب | 2M tokens مدفوعة | 2K + 999 مُخزَّنة | **~99.9%** على البادئة |
| Anthropic cached tokens | سعر كامل | **90% أرخص** | 90% على الجزء المُخزَّن |
| OpenAI cached tokens | سعر كامل | **50% أرخص** | 50% على الجزء المُخزَّن |

### التوفر عبر المزودين (يونيو 2026)

| المزود | الآلية | التوفير | TTL | الحد الأدنى |
|--------|--------|---------|-----|-----------|
| **Anthropic** | `cache_control` صريح | **90%** | 5 دقائق (يتجدد) | 1,024 tokens |
| **OpenAI** | تلقائي على البادئات | **50%** | ~5-10 دقائق | 1,024 tokens |
| **Google Gemini** | `cached_content` API | **75%** | قابل للتخصيص | — |
| **vLLM** | `enable_prefix_caching=True` | حوسبة كاملة | لا حد | — |
| **SGLang** | RadixAttention (تلقائي) | حوسبة كاملة | لا حد | — |

### دراسة حالة — ProjectDiscovery

| المقياس | قبل | بعد |
|---------|------|------|
| نسبة إصابة التخزين المؤقت | **7%** | **84%** |
| توكنات مُقدَّمة من التخزين | — | **9.8 مليار** |
| تقليل تكلفة LLM | — | **59%** |

**كيف؟** نقل الذاكرة العاملة الديناميكية خارج system prompt → البادئة أصبحت ثابتة → نسبة الإصابة ارتفعت من 7% إلى 84%.

### نصائح عملية لتعظيم الإصابة

1. **ضع الثابت أولاً:** system prompt → few-shot → context → user query
2. **لا تغيّر البادئة:** أي تغيير يُبطل التخزين
3. **اجمع الطلبات المتشابهة:** نفس البادئة = إصابة أعلى
4. **راقب نسبة الإصابة:** أقل من 20% = التصميم يحتاج تعديل

### العلاقة بتقنيات أخرى

| التقنية | العلاقة |
|---------|---------|
| **Semantic Caching** | **تكميلي** — Prefix caching = نفس البادئة. Semantic = نفس المعنى |
| **Model Routing** | **تكاملي** — نفس الموجّه يُرسل لنفس النموذج = إصابة أعلى |
| **RAG** | **تكاملي** — مستندات مرجعية ثابتة = بادئة مثالية للتخزين |
| **Continuous Batching** | **تبعية** — التخزين يعمل ضمن محرك الاستدلال |

---

## English Content

Prompt/prefix caching reuses Prefill computations for repeated prompt prefixes. Anthropic: 90% discount. OpenAI: 50%. ProjectDiscovery: raised hit rate from 7% to 84%, saving 59% LLM cost. Key: put static content first, never change the prefix.

---

## المصادر

1. **[Tier 2]** Anthropic, "Prompt Caching Documentation", 2025-2026. 90% discount, 5-min TTL.
2. **[Tier 2]** Digital Applied, "The AI Cost Reckoning", June 2026. ProjectDiscovery case study.
3. **[Tier 2]** OpenAI, "Prompt Caching Documentation", 2025-2026. 50% automatic discount.
