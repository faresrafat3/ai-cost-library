---
id: "entry-specdec-001"
title_ar: "فك التشفير التكهني"
title_en: "Speculative Decoding"
type: "Practical"
status: "Deployed"
category: "Efficient Inference"
subcategory: "Decoding Strategies"
cost_dimensions: ["latency", "inference-cost"]
proof_score: 4
sources_count: 1
---

# Speculative Decoding

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary
فك التشفير التكهني (Speculative Decoding) هي استراتيجية تهدف إلى تسريع عملية استدلال النماذج اللغوية دون فقدان الدقة. تعتمد الطريقة على استخدام نموذج صغير وسريع لتوليد عدة رموز (Tokens) كمسودة (Draft)، ثم يقوم النموذج الكبير بمراجعة واعتماد هذه الرموز في خطوة واحدة متوازية.

## 📌 English Summary
Speculative Decoding is an exact decoding strategy that accelerates LLM inference without altering the output distribution. A smaller "draft" model generates multiple speculative tokens, which are then verified in parallel by the target large model.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected
- **الكمون / التأخير (Latency):** تحسين ملحوظ (تسريع 2x إلى 3x).
- **تكلفة الاستدلال (Inference Cost):** زيادة الإنتاجية (Throughput) وتقليل وقت حجز الموارد.

## 🛡️ بوابات الأدلة | Evidence Gates
- ✅ **Gate 1 (Built):** متاح في أنظمة مثل `vLLM` و `TGI`.
- ✅ **Gate 2 (Tested):** أثبتت الدراسات تسريعاً يبلغ من 2 إلى 3 أضعاف.
- ✅ **Gate 3 (Deployed):** مستخدم في خدمات API لشركات كبرى لتسريع الاستجابات.
- ✅ **Gate 4 (Saved):** يقلل وقت المعالجة الكلي للطلبات بنسب تصل إلى 60٪.

## ⚠️ القيود والمخاطر | Limitations & Risks
- يتطلب توفر نموذج مسودة (Draft Model) متوافق في مفرداته (Vocabulary) مع النموذج الرئيسي.
- يستهلك ذاكرة إضافية لتحميل النموذج الصغير.
- الفعالية تنخفض إذا كان النموذج الصغير سيئاً في التوقع.

## 📚 المصادر | Sources
- [1] Leviathan et al., "Fast Inference from Transformers via Speculative Decoding", ICML, 2023. [URL](https://arxiv.org/abs/2211.17192)
