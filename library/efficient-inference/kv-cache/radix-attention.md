---
id: "entry-radixattention-001"
title_ar: "الانتباه الشجري (RadixAttention)"
title_en: "RadixAttention — Tree-Based KV Cache Reuse"
type: "Practical"
status: "Deployed"
category: "Efficient Inference"
subcategory: "KV Cache Optimization"
tree_path: ["Efficient Inference", "KV Cache Optimization", "RadixAttention"]
cost_dimensions: ["api-cost", "latency", "throughput", "memory"]
proof_score: 4
sources_count: 4
---

# الانتباه الشجري | RadixAttention

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary

الانتباه الشجري (RadixAttention) هو خوارزمية متقدمة لإعادة استخدام الذاكرة المؤقتة للمفاتيح والقيم (KV Cache) عبر الطلبات التي تتشارك سوابق نصية مشتركة. يُخزّن KV Cache في شجرة شجعية (Radix Tree) مُفهرسة بتسلسلات الرموز، مما يمكّن من مشاركة الأجزاء المشتركة بين الطلبات المختلفة بدلاً من إعادة حسابها.

على عكس التخزين المؤقت البسيط (Prefix Caching) الذي يطابق فقط السوابق الثابتة، يتعامل RadixAttention مع أي بنية مشتركة متعددة المستويات: تعليمات النظام، وثائق RAG، وسجلات المحادثة. يحقق معدلات إصابة (Hit Rate) بنسبة 70-95% لأحمال الوكلاء وRAG، مما يقلل تكلفة Prefill بنسبة 80-90%.

## 📌 English Summary

RadixAttention is an advanced algorithm for reusing KV caches across requests with shared text prefixes. It stores KV entries in a radix tree indexed by token sequences, enabling arbitrary common sub-sequence sharing across different requests.

Unlike simple Prefix Caching that matches only fixed leading prefixes, RadixAttention handles multi-level shared structures: system prompts, RAG documents, and conversation histories. It achieves 70-95% cache hit rates for agent and RAG workloads, reducing Prefill compute costs by 80-90%.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected

- **تكلفة الـ API (API Cost):** تقليل 80-90% في تكلفة Prefill عندما تكون Hit Rate ≥90%.
- **الكمون (Latency):** TTFT أقل بـ 3-4× على الطلبات ذات السوابق المشتركة (من ~280ms إلى ~80-120ms).
- **الإنتاجية (Throughput):** حتى 6.4× تحسين على أحمال الوكلاء وRAG مقارنة بمحركات بدون إعادة استخدام.
- **تكلفة الذاكرة (Memory Cost):** مشاركة الصفحات الفيزيائية تقلل استهلاك HBM بنسبة تصل إلى 90% للطلبات ذات البادئات المشتركة.

## 🛡️ بوابات الأدلة | Evidence Gates

- ✅ **Gate 1 (Built):** مُدمج في SGLang (مفتوح المصدر، مدعوم من xAI/LMSYS/UC Berkeley).
- ✅ **Gate 2 (Tested):** مُختبر على Llama-7B (A10G), Mixtral-8x7B (8× A10G), و Llama-3.3-70B (H100).
- ✅ **Gate 3 (Deployed):** يُستخدم في الإنتاج من قبل xAI (Grok) على 100K+ GPU.
- ✅ **Gate 4 (Saved):** 5× إنتاجية أعلى على أحمال MMLU (إعادة استخدام أمثلة 5-shot). 6.4× على أحمال RAG. 80-90% توفير في تكلفة Prefill.

## ⚠️ القيود والمخاطر | Limitations & Risks

- الفعالية تعتمد على نسبة مشاركة السوابق — أحمال الأوامر الفريدة لا تستفيد.
- تغيير حرف واحد في تعليمات النظام يُبطِل الذاكرة المؤقتة بالكامل (Byte-exact matching).
- يحتاج إدارة LRU فعّالة لتجنب ازدحام الشجرة بالمدخلات القديمة.
- أقل فعالية على أحمال التوليد المحتوى الفريد (Content generation).

## 📚 المصادر | Sources

- [1] Zheng et al., "SGLang: Efficient Execution of Structured Language Model Programs", arXiv, 2023. DOI: [arXiv:2312.07104](https://arxiv.org/abs/2312.07104)
- [2] LMSYS Blog, "Fast and Expressive LLM Inference with RadixAttention and SGLang", 2024. [URL](https://www.lmsys.org/blog/2024-01-17-sglang/)
- [3] Spheron, "SGLang Production Deployment Guide", 2026. [URL](https://www.spheron.network/blog/sglang-production-deployment-guide/)
- [4] Particula, "SGLang vs vLLM in 2026: Benchmarks", 2026. [URL](https://particula.tech/blog/sglang-vs-vllm-inference-engine-comparison)

## 🔗 إدخالات ذات صلة | Related Entries

- [PagedAttention](./paged-attention.md)
- [تخزين الموجهات المؤقت](../../token-and-prompt-cost/prompt-caching.md)
- [التجميع المستمر](../batching/continuous-batching.md)
