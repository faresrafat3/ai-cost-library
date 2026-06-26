---
id: "entry-promptcache-001"
title_ar: "تخزين الموجهات المؤقت"
title_en: "Prompt Caching"
type: "Practical"
status: "Deployed"
category: "Token and Prompt Cost Optimization"
subcategory: "Prompt Caching"
cost_dimensions: ["api-cost", "latency", "token-cost"]
proof_score: 4
sources_count: 1
---

# Prompt Caching

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary
تخزين الموجهات المؤقت (Prompt Caching) هي تقنية مدعومة من موفري واجهات برمجة التطبيقات (مثل Anthropic و OpenAI و Google) والأنظمة مفتوحة المصدر (مثل vLLM باستخدام RadixAttention)، تتيح إعادة استخدام العمليات الحسابية لمقاطع النصوص الطويلة (مثل تعليمات النظام، والأمثلة، وسياق RAG) عبر طلبات متعددة بدلاً من إعادة معالجتها في كل مرة. 

## 📌 English Summary
Prompt Caching is a technique supported by major API providers (Anthropic, OpenAI, Google) and open-source inference engines (e.g., vLLM with RadixAttention) that allows reusing the precomputed keys and values (KV) of shared context across multiple requests. This eliminates redundant computation for long system prompts or context blocks.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected
- **تكلفة واجهة برمجة التطبيقات (API Cost):** تقليل تكلفة المدخلات (Input Tokens) بشكل جذري.
- **الكمون / التأخير (Latency):** تسريع زمن الوصول لأول رمز (Time To First Token - TTFT) بشكل كبير نظراً لعدم الحاجة لمعالجة السياق (Prefill).

## 🛡️ بوابات الأدلة | Evidence Gates
- ✅ **Gate 1 (Built):** مدمجة في APIs الرسمية (OpenAI, Anthropic) و `vLLM` / `SGLang`.
- ✅ **Gate 2 (Tested):** أظهرت دراسة عام 2026 على مهام الوكلاء المستقلين (Agentic Tasks) تخفيضاً في وقت الاستجابة (TTFT) بنسبة 13% إلى 31%.
- ✅ **Gate 3 (Deployed):** معيار أساسي حالياً في جميع تطبيقات الذكاء الاصطناعي التي تعتمد على RAG أو الوكلاء متعددي الخطوات (Multi-turn agents).
- ✅ **Gate 4 (Saved):** توفير تكلفة الـ API بنسب تتراوح بين 41% إلى 80% في التطبيقات ذات السياق الطويل المتكرر، وفقاً للقياسات المستقلة.

## ⚠️ القيود والمخاطر | Limitations & Risks
- تتطلب من المطورين تنظيم الموجهات (Prompts) بحيث تكون الأجزاء الثابتة (مثل تعليمات النظام) في بداية الطلب، وتأخير الأجزاء المتغيرة (مثل مخرجات الأدوات Tool results) للنهاية لعدم إفساد الذاكرة المؤقتة (Cache Invalidation).
- بعض المزودين يفرضون حداً أدنى من الرموز (Tokens) لتفعيل التخزين المؤقت (مثلاً 1024 توكن).

## 📚 المصادر | Sources
- [1] Du et al., "Don’t Break the Cache: An Evaluation of Prompt Caching for Long-Horizon Agentic Tasks", arXiv (2601.06007), 2026. [URL](https://arxiv.org/abs/2601.06007)
