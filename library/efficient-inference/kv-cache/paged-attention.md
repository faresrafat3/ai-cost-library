---
id: "entry-pagedattention-001"
title_ar: "الانتباه المرقّم (PagedAttention)"
title_en: "PagedAttention — Virtual Memory for LLM KV Caches"
type: "Practical"
status: "Deployed"
category: "Efficient Inference"
subcategory: "KV Cache Optimization"
tree_path: ["Efficient Inference", "KV Cache Optimization", "PagedAttention"]
cost_dimensions: ["memory", "throughput", "inference-cost", "hardware-cost"]
proof_score: 4
sources_count: 4
---

# الانتباه المرقّم | PagedAttention

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary

الانتباه المرقّم (PagedAttention) هو خوارزمية إدارة ذاكرة مبتكرة تُعامل الذاكرة المؤقتة للمفاتيح والقيم (KV Cache) في النماذج اللغوية الكبيرة بنفس الطريقة التي تتعامل بها أنظمة التشغيل مع الذاكرة الافتراضية. بدلاً من تخصيص كتل متجاورة من الذاكرة مسبقاً لكل طلب (مما يسبّب هدراً بنسبة 60-80%)، يُقسّم PagedAttention الذاكرة إلى صفحات ثابتة الحجم ويخصّصها عند الحاجة فقط.

النتيجة: استخدام ذاكرة يقترب من المثالي (<4% هدر)، وإنتاجية أعلى بـ 2-4× مقارنة بالأنظمة التقليدية، وقدرة على خدمة طلبات متزامنة أكثر بكثير.

## 📌 English Summary

PagedAttention is an innovative memory management algorithm that treats LLM KV caches the same way operating systems handle virtual memory. Instead of pre-allocating contiguous memory blocks per request (causing 60-80% waste), it divides memory into fixed-size pages allocated on-demand.

The result: near-optimal memory utilization (<4% waste), 2-4× higher throughput vs traditional systems, and the ability to serve significantly more concurrent requests.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected

- **تكلفة الذاكرة (Memory Cost):** تقليل الهدر من 60-80% إلى <4%. نموذج 70B على A100 80GB يخدم 40 طلباً متزامناً بدلاً من 8.
- **الإنتاجية (Throughput):** تحسين 2-4× مقارنة بالأنظمة التقليدية (FasterTransformer, Hugging Face Transformers).
- **تكلفة العتاد (Hardware Cost):** يمكن خفض عدد GPUs المطلوبة بنسبة 50-75% لنفس الحمل.
- **تكلفة الاستدلال (Inference Cost):** 36.9× إنتاجية مقارنة بالتجميع الثابت (عند دمج PagedAttention مع التجميع المستمر).

## 🛡️ بوابات الأدلة | Evidence Gates

- ✅ **Gate 1 (Built):** الخوارزمية الأساسية في `vLLM` (مفتوح المصدر، >50K نجمة على GitHub).
- ✅ **Gate 2 (Tested):** مُختبر على نماذج OPT-1.3B, OPT-13B, LLaMA-7B, LLaMA-13B بمقاييس شاملة.
- ✅ **Gate 3 (Deployed):** مُستخدم في الإنتاج من قبل Anyscale, Together.AI, Fireworks AI, وxAI (Grok).
- ✅ **Gate 4 (Saved):** 2-4× إنتاجية أعلى مع <4% هدر ذاكرة. 5× تحسين في استخدام GPU.

## ⚠️ القيود والمخاطر | Limitations & Risks

- يتطلب إدارة جدول صفحات (Page Table) مما يزيد التعقيد البرمجي.
- أقل فعالية في الأحمال منخفضة التزامن حيث يكون الهدر الأصلي صغيراً.
- لا يحل مشكلة حجم KV Cache المطلق في السياقات الطويلة جداً (128K+).
- يعتمد على توفر GPU ذاكرة كافية للنموذج الأساسي.

## 📚 المصادر | Sources

- [1] Kwon et al., "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention", OSDI, 2023. DOI: [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)
- [2] CalibreOS, "Advanced KV Cache: RadixAttention, LMCache, and Context Parallelism", 2024. [URL](https://www.calibreos.com/learn/genai-kv-cache-management)
- [3] Spheron, "LLM Serving Optimization: Continuous Batching, PagedAttention", 2026. [URL](https://www.spheron.network/blog/llm-serving-optimization-continuous-batching-paged-attention/)
- [4] EmergentMind, "vLLM System: Efficient LLM Serving", 2026. [URL](https://www.emergentmind.com/topics/vllm-system)

## 🔗 إدخالات ذات صلة | Related Entries

- [التجميع المستمر](../batching/continuous-batching.md)
- [RadixAttention](./radix-attention.md)
- [تخزين الموجهات المؤقت](../../token-and-prompt-cost/prompt-caching.md)
