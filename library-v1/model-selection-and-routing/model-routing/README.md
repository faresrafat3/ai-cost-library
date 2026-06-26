# توجيه النماذج | Model Routing

> **المسار:** مكتبة تكلفة الذكاء الاصطناعي ← اختيار وتوجيه النماذج ← توجيه النماذج
>
> **Tree Path:** AI Cost Library → Model Selection and Routing → Model Routing

## نظرة عامة | Overview

يشمل هذا القسم تقنيات توجيه طلبات الاستدلال تلقائياً إلى النموذج الأنسب من حيث التكلفة والجودة، بدلاً من إرسال جميع الطلبات إلى نموذج واحد عالي التكلفة.

This section covers techniques for automatically routing inference requests to the most cost-appropriate model based on query complexity, rather than sending all requests to a single expensive model.

## الإدخالات | Entries

| المعرف | التقنية | التصنيف | الإثبات |
|--------|---------|---------|---------|
| [entry-routing-001](model-routing.md) | توجيه النماذج الذكي (RouteLLM) | 📘 عملية | ⭐⭐⭐ منشور |

## أبعاد التكلفة المتأثرة | Affected Cost Dimensions

- تكلفة واجهة البرمجة (api-cost)
- تكلفة التوكن (token-cost)
- تكلفة الاستدلال (inference-cost)
- زمن الاستجابة (latency)
