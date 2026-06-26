# التدريب الفعّال | Efficient Training

![Category Status](https://img.shields.io/badge/Status-Active-green)

## 📌 نظرة عامة | Overview

التدريب الفعّال (Efficient Training) يشمل تقنيات تقليل تكاليف تدريب وضبط النماذج اللغوية الكبيرة، مع التركيز على تقليل المعاملات القابلة للتدريب، تحسين استخدام الذاكرة، وتسريع عملية التدريب.

Efficient Training covers techniques that reduce the cost of training and fine-tuning LLMs, focusing on reducing trainable parameters, optimizing memory usage, and accelerating the training process.

## 🌿 الفئات الفرعية | Subcategories

| الفئة الفرعية | Subcategory | الإدخالات | Entries | الحالة |
|---|---|---|---|---|
| الضبط الدقيق الموفّر للمعاملات | PEFT | 2 | LoRA, QLoRA | ✅ نشطة |
| كفاءة البيانات في التدريب | Data-Efficient Training | 0 | — | 🔜 قادمة |

## 📘 الإدخالات التطبيقية | Practical Entries

| الإدخال | النوع | درجة الإثبات | الحالة |
|---|---|---|---|
| [LoRA](./parameter-efficient/lora.md) | تكيّف منخفض الرتبة | ⭐⭐⭐⭐ | Deployed |
| [QLoRA](./parameter-efficient/qlora.md) | تكيّف منخفض الرتبة المكمّم | ⭐⭐⭐⭐ | Deployed |

## 🔗 صفحات المقارنة | Comparison Pages

- [LoRA مقابل QLoRA مقابل الضبط الكامل](../../comparisons/lora-vs-qlora-vs-full-finetuning.md)

## 🎯 لماذا التدريب الفعّال مهم لتقليل التكلفة؟

- **تكلفة التدريب:** LoRA يقلل المعاملات القابلة للتدريب 10,000×.
- **تكلفة الذاكرة:** QLoRA يُمكّن ضبط نموذج 65B على GPU واحد 48GB (بدلاً من >780GB).
- **تكلفة التخزين:** نقاط تفتيش بحجم 35MB بدلاً من 350GB لكل مهمة.
