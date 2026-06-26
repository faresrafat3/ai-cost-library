---
id: "entry-contbatching-001"
title_ar: "التجميع المستمر"
title_en: "Continuous Batching"
type: "Practical"
status: "Deployed"
category: "Efficient Inference"
subcategory: "Batching"
cost_dimensions: ["throughput", "inference-cost"]
proof_score: 4
sources_count: 2
---

# Continuous Batching

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary
التجميع المستمر (Continuous Batching أو Iteration-level scheduling) هو أسلوب متقدم لجدولة طلبات الاستدلال (Inference) للنماذج اللغوية الكبيرة. بدلاً من انتظار انتهاء جميع الطلبات في الدفعة (Static Batching)، يقوم المجدول بإزالة الطلب الذي انتهى توليده وإدخال طلب جديد فوراً في نفس الدورة (Iteration). هذا يقضي على وقت الفراغ (Padding) ويرفع كفاءة استخدام البطاقة الرسومية (GPU) إلى أقصى حد.

## 📌 English Summary
Continuous Batching (or dynamic batching / iteration-level scheduling) optimizes LLM serving by operating at the iteration level rather than the request level. As soon as a sequence emits its end-of-sequence token, its slot is freed, and a new waiting request is inserted into the batch for the next decoding step. This eliminates padding waste and drastically improves throughput.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected
- **الإنتاجية (Throughput):** مضاعفة عدد الطلبات التي يمكن للخادم معالجتها في نفس الوقت.
- **تكلفة الاستدلال (Inference Cost):** خفض تكلفة الخادم لكل طلب (Cost per query) بسبب الاستغلال الأمثل للموارد العتادية، وتجنب الهدر الناجم عن اختلاف أطوال المخرجات.

## 🛡️ بوابات الأدلة | Evidence Gates
- ✅ **Gate 1 (Built):** مطبقة بشكل قياسي في `vLLM`، `TGI`، ومحركات `Anyscale`.
- ✅ **Gate 2 (Tested):** أظهرت ورقة Orca الأصلية (OSDI 2022) تحسناً بمقدار 36.9 ضعفاً مقارنة بالمحركات الأقدم.
- ✅ **Gate 3 (Deployed):** التقنية الأساسية وراء كل واجهات برمجة التطبيقات (APIs) السحابية للنماذج اللغوية اليوم.
- ✅ **Gate 4 (Saved):** تُظهر القياسات العملية زيادة في الإنتاجية (Throughput) تصل إلى 23x مقارنة بالتجميع الثابت الافتراضي، ما يعني القدرة على خدمة نفس عدد المستخدمين باستخدام عدد أقل بكثير من خوادم GPU.

## ⚠️ القيود والمخاطر | Limitations & Risks
- تتطلب إدارة معقدة للذاكرة، لذلك عادة ما تُدمج مع تقنية PagedAttention لكي لا تتعطل بسبب تجزئة الذاكرة (Memory Fragmentation).
- فعاليتها تنخفض إذا كانت كل الطلبات تصدر مخرجات بنفس الطول بالضبط (نادر في التطبيقات الحقيقية).

## 📚 المصادر | Sources
- [1] Yu et al., "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI, 2022.
- [2] Anyscale Blog, "Achieve 23x LLM Inference Throughput & Reduce p50 Latency", 2026. [URL](https://www.anyscale.com/blog/continuous-batching-llm-inference)
