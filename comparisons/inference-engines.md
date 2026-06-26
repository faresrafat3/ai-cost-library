# مقارنة محركات الاستدلال | Inference Engines Comparison

## نظرة عامة | Overview

تقارن هذه الصفحة محركات الاستدلال الرئيسية للنماذج اللغوية الكبيرة في 2025-2026.

This page compares the major LLM inference engines in 2025-2026.

---

## 📊 جدول المقارنة التفصيلي | Detailed Comparison Table

| المعيار | vLLM | SGLang | TGI (HuggingFace) | TensorRT-LLM |
|---|---|---|---|---|
| **تقنية KV Cache** | PagedAttention | RadixAttention | Paged KV | Blocked KV |
| **Prefix Caching** | ✅ (ثابت) | ✅ (شجرة) | ✅ | ✅ |
| **Continuous Batching** | ✅ | ✅ | ✅ | ✅ |
| **التكمية** | GPTQ, AWQ, FP8 | GPTQ, AWQ, FP8, INT8 | GPTQ, AWQ | INT4, INT8, FP8 |
| **إعادة استخدام KV** | محدود | شامل (شجرة) | محدود | محدود |
| **تحسين الإنتاجية** | 2-4× | حتى 6.4× (مع إعادة استخدام) | 1.5-2× | 1.8× (NVIDIA فقط) |
| **تعدد العتاد** | ✅ (NVIDIA, AMD, CPU) | ✅ | ✅ | ❌ (NVIDIA فقط) |
| **سهولة النشر** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **أفضل لـ** | استخدام عام | وكلاء + RAG | HuggingFace stack | NVIDIA deployments |
| **الترخيص** | Apache 2.0 | Apache 2.0 | Apache 2.0 | NVIDIA |

## 📋 التوصيات | Recommendations

| السيناريو | المحرك الموصى به |
|---|---|
| استخدام عام + سهولة النشر | vLLM |
| وكلاء مستقلون (Agents) + RAG | SGLang |
| تكامل مع HuggingFace Hub | TGI |
| أقصى إنتاجية على NVIDIA | TensorRT-LLM |
