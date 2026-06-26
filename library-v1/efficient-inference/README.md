# الاستدلال الفعّال | Efficient Inference

![Category Status](https://img.shields.io/badge/Status-Active-green)

## 📌 نظرة عامة | Overview

الاستدلال الفعّال (Efficient Inference) يشمل تقنيات تحسين أداء تقديم النماذج اللغوية في بيئات الإنتاج، مع التركيز على تقليل الكمون (Latency)، زيادة الإنتاجية (Throughput)، وتحسين استخدام موارد العتاد.

Efficient Inference covers techniques that optimize LLM serving in production environments, focusing on reducing latency, increasing throughput, and improving hardware utilization.

## 🌿 الفئات الفرعية | Subcategories

| الفئة الفرعية | Subcategory | الإدخالات | Entries | الحالة |
|---|---|---|---|---|
| استراتيجيات فك التشفير | Decoding Strategies | 1 | Speculative Decoding | ✅ نشطة |
| التجميع | Batching | 1 | Continuous Batching | ✅ نشطة |
| تحسين KV Cache | KV Cache Optimization | 2 | PagedAttention, RadixAttention | ✅ نشطة |
| أنظمة التقديم | Serving Systems | 0 | — | 🔜 قادمة |

## 📘 الإدخالات التطبيقية | Practical Entries

| الإدخال | النوع | درجة الإثبات | الحالة |
|---|---|---|---|
| [فك التشفير التكهني](./decoding/speculative-decoding.md) | استراتيجية فك تشفير | ⭐⭐⭐⭐ | Deployed |
| [التجميع المستمر](./batching/continuous-batching.md) | تقنية جدولة | ⭐⭐⭐⭐ | Deployed |
| [PagedAttention](./kv-cache/paged-attention.md) | إدارة ذاكرة KV | ⭐⭐⭐⭐ | Deployed |
| [RadixAttention](./kv-cache/radix-attention.md) | إعادة استخدام KV | ⭐⭐⭐⭐ | Deployed |

## 🔗 صفحات المقارنة | Comparison Pages

- [فك التشفير التكهني مقابل التجميع المستمر](../../comparisons/speculative-decoding-vs-batching.md)
- [محركات الاستدلال](../../comparisons/inference-engines.md)

## 🎯 لماذا الاستدلال الفعّال مهم لتقليل التكلفة؟

- **الإنتاجية:** تحسين 23× يعني خدمة نفس عدد المستخدمين بـ GPU أقل بكثير.
- **الكمون:** تقليل TTFT بنسبة 70% يُحسّن تجربة المستخدم ويقلل وقت اتصال الجلسة.
- **استخدام العتاد:** رفع GPU utilization من 30% إلى 85% يعني توفير 65% من تكلفة العتاد.
