# ضغط النماذج | Model Compression

![Category Status](https://img.shields.io/badge/Status-Active-green)

## 📌 نظرة عامة | Overview

ضغط النماذج (Model Compression) هو مجموعة تقنيات تهدف إلى تقليل حجم النماذج اللغوية الكبيرة ومتطلباتها الحسابية مع الحفاظ على أدائها قدر الإمكان. تشمل ثلاث طرق رئيسية: التكمية (Quantization)، التقليم (Pruning)، والتقطير (Distillation).

Model Compression encompasses techniques that reduce LLM size and computational requirements while preserving performance. It includes three primary approaches: Quantization, Pruning, and Distillation.

## 🌿 الفئات الفرعية | Subcategories

| الفئة الفرعية | Subcategory | الإدخالات | Entries | الحالة |
|---|---|---|---|---|
| التكمية | Quantization | 5 | GPTQ, AWQ, SmoothQuant, LLM.int8(), SmoothQuant+ | ✅ نشطة |
| التقليم | Pruning | 0 | — | 🔜 قادمة |
| التقطير | Distillation | 0 | — | 🔜 قادمة |

## 📘 الإدخالات التطبيقية | Practical Entries

| الإدخال | النوع | درجة الإثبات | الحالة |
|---|---|---|---|
| [GPTQ](./quantization/gptq.md) | تكمية أوزان بعد التدريب | ⭐⭐⭐⭐ | Deployed |
| [AWQ](./quantization/awq.md) | تكمية أوزان معتمدة على التنشيط | ⭐⭐⭐⭐ | Deployed |
| [SmoothQuant](./quantization/smoothquant.md) | تكمية ملساء W8A8 | ⭐⭐⭐⭐ | Deployed |
| [LLM.int8()](./quantization/llm-int8.md) | تكمية مختلطة الدقة | ⭐⭐⭐⭐ | Deployed |

## 🔗 صفحات المقارنة | Comparison Pages

- [مقارنة طرق التكمية](../../comparisons/quantization-methods.md)
- [التقليم مقابل التقطير](../../comparisons/pruning-vs-distillation.md)

## 🎯 لماذا ضغط النماذج مهم لتقليل التكلفة؟

- **توفير الذاكرة:** تقليل VRAM بنسبة 50-75% يُمكّن تشغيل نماذج أكبر على عتاد أقل.
- **توفير النطاق الترددي:** نماذج أصغر = نقل بيانات أقل = استهلاك طاقة أقل.
- **توفير التخزين:** نقاط تفتيش أصغر = تكاليف تخزين سحابي أقل.
