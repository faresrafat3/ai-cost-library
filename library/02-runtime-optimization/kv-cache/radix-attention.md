---
id: entry-radixattention-001
title_ar: شجرة الانتباه المتفرعة — RadixAttention (SGLang)
title_en: "RadixAttention: Prefix Sharing via Radix Tree KV Cache"
type: practical
status: deployed
category: runtime-optimization
subcategory: kv-cache
cost_dimensions: [inference-cost, throughput, latency, memory]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 8
  A2: 8
  A3: 8
  A4: 8
  B1: 7
  B2: 0
  B3: 6
  B4: 8
  C1: 7
  C2: 6
  C3: 8
  C4: 7
---

# 📘 RadixAttention — مشاركة البادئات عبر شجرة Radix

> **التصنيف:** 📘 عملية — مُنشَر | **الإثبات:** ⭐⭐⭐
>
> **الميزة التنافسية الأساسية لـ SGLang مقابل vLLM**

---

## المحتوى العربي

### ما هو RadixAttention؟

RadixAttention — وهو تقنية تُخزّن مؤقتات KV في شجرة Radix (شجرة بادئات مضغوطة) بدلاً من تخزين مستقل لكل طلب. عندما يتشارك طلبان بادئة (system prompt, أمثلة, تاريخ محادثة)، يُعاد استخدام حسابات البادئة بدلاً من إعادتها من الصفر.

### الفرق عن Prefix Caching العادي

| | Prefix Caching (vLLM) | RadixAttention (SGLang) |
|---|---------------------|----------------------|
| البنية | قائمة مسطحة | **شجرة متفرعة** |
| مشاركة | بادئات كاملة فقط | **متعددة المستويات** (أي نقطة تفرع) |
| الجدولة | FIFO عادي | **واعية بالتخزين المؤقت** (depth-first) |
| المحادثات المتعددة | محدود | **ممتاز** (شجرة تنمو مع المحادثة) |
| الوكلاء + أدوات | محدود | **ممتاز** (فروع لكل أداة) |

### الأرقام — أين يتفوق SGLang بسبب RadixAttention

#### إنتاجية مع مشاركة بادئات

| حمل العمل | طول البادئة | vLLM | SGLang | **التسريع** |
|-----------|------------|------|--------|-----------|
| بدون بادئة مشتركة | 0 | 2,500 | 2,800 | 1.12× |
| Few-shot (5 أمثلة) | 1,000 | 800 | 3,200 | **4×** |
| Few-shot (10 أمثلة) | 2,000 | 500 | 5,000 | **10×!** |
| وكيل + أدوات | 1,500 | 800 | 4,000 | **5×** |
| محادثة متعددة | 500-2K | 1,200 | 3,600 | **3×** |

*المصدر: معايير مُجمّعة من SGLang paper + AI Research Skills + PremAI*

> **القاعدة:** بادئات أطول = تسريع أكبر. بدون بادئات = لا فائدة تقريباً.

#### زمن الاستجابة (TTFT) لأحمال الوكلاء

| المقياس | vLLM | SGLang | التحسن |
|---------|------|--------|--------|
| الطلب الأول (بارد) | 1.8s | 1.8s | **متساوٍ** |
| الطلبات اللاحقة | 1.8s | **0.35s** | **5× أسرع** |
| P50 (100 طلب) | 1.8s | 0.42s | 4.3× |
| P99 | 2.1s | 0.58s | 3.6× |

#### كفاءة الذاكرة

100 طلب × 2,000 توكن بادئة مشتركة:
- **بدون RadixAttention:** 200K توكن مُخزَّنة = ~1.5 GB (8B FP16)
- **مع RadixAttention:** 2K توكن (مرة واحدة) + فريد = **~15 MB**
- **التوفير: 99%** للأجزاء المشتركة

### نسب الإصابة في الإنتاج

| نوع حمل العمل | نسبة الإصابة النموذجية |
|-------------|---------------------|
| وكلاء (system prompt + أدوات ثابتة) | **75-95%** |
| محادثات متعددة الأدوار | **50-85%** |
| RAG (نفس المستندات) | **60-90%** |
| عمليات دفعية فريدة | **< 5%** (لا فائدة) |

### ما يقتل نسبة الإصابة

1. **حرف واحد مختلف في البادئة** → إخفاق كامل (الشجرة تُطابق بايت-بايت)
2. **ترتيب غير ثابت للأمثلة** → فروع جديدة لكل ترتيب
3. **FIFO scheduling** → يُخرج بادئات مفيدة مبكراً (SGLang يحل هذا بجدولة واعية)

### من يستخدم SGLang في الإنتاج (2026)

| الشركة | الاستخدام |
|--------|----------|
| **xAI** | Grok 3 — تريليونات التوكنات |
| **Microsoft Azure** | نقاط نهاية Azure AI |
| **Cursor** | إكمال الكود (بادئات طويلة متكررة) |
| **LinkedIn** | ميزات AI |
| **DeepSeek** | المحرك الرسمي الموصى — 3.1× أسرع من vLLM لـ V3 |
| **Oracle Cloud** | خدمات الاستدلال |

### العلاقة بتقنيات أخرى

```
PagedAttention (أساس الذاكرة) ──→ RadixAttention (يُضيف شجرة مشاركة فوقه)
                                        │
                                        ├── Prefix Caching (حالة خاصة أبسط)
                                        ├── Prompt Caching APIs (Anthropic/OpenAI — نفس المبدأ على الخادم)
                                        └── Semantic Caching (مشاركة بالمعنى، RadixAttention بالنص الحرفي)
```

---

## English Content

RadixAttention stores KV cache in a radix tree, enabling multi-level prefix sharing. 4-10× speedup over vLLM on prefix-heavy workloads. 75-95% cache hit rates for agents. 99% memory savings for shared portions. Used by xAI (Grok 3), Microsoft Azure, Cursor, DeepSeek (3.1× faster than vLLM for V3).

---

## المصادر | Sources

1. **[Tier 1]** Zheng, L., et al., "SGLang: Efficient Execution of Structured Language Model Programs", 2024. UC Berkeley.
2. **[Tier 2]** Spheron, "SGLang Production Deployment Guide: RadixAttention", March 2026. Cache hit rates + configuration.
3. **[Tier 2]** Particula Tech, "SGLang vs vLLM in 2026: Benchmarks", March 2026. Head-to-head comparison.
4. **[Tier 2]** RunPod, "SGLang in Production: RadixAttention", April 2026. 6.4× throughput, production deployment.
