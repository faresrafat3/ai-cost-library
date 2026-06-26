---
id: entry-chinchilla-001
title_ar: قوانين التحجيم الأمثل حوسبياً (Chinchilla)
title_en: Compute-Optimal Scaling Laws (Chinchilla)
type: theoretical
status: validated
category: efficient-training
subcategory: compute-optimal
tree_path: "AI Cost Library → Efficient Training → Compute-Optimal → Chinchilla Scaling"
cost_dimensions:
  - training-cost
  - compute
  - energy
  - hardware-cost
proof_score: "⭐⭐⭐ مُتحقق | Validated"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
---

# 📐 قوانين التحجيم الأمثل حوسبياً | Compute-Optimal Scaling Laws (Chinchilla)

> **التصنيف:** 📐 نظرية (ذات تأثير عملي واسع) | **الإثبات:** ⭐⭐⭐ مُتحقق
>
> **المسار:** مكتبة تكلفة الذكاء الاصطناعي ← التدريب الفعّال ← التدريب الأمثل حوسبياً

---

## المحتوى العربي

### ما هي قوانين التحجيم الأمثل حوسبياً؟

قوانين التحجيم الأمثل حوسبياً (Chinchilla Scaling Laws) — وهي نتيجة بحثية من DeepMind (2022) تُثبت أن النماذج اللغوية الكبيرة السابقة كانت تُدرَّب بحجم كبير جداً مقابل بيانات قليلة جداً. القانون يقول: لتحقيق أفضل أداء ضمن ميزانية حوسبية ثابتة، يجب أن يتناسب حجم النموذج (عدد المعاملات) مع حجم بيانات التدريب (عدد التوكنات) بنسبة 1:20 تقريباً.

### المبدأ الأساسي

بدلاً من تدريب نموذج ضخم (280 مليار معامل) على 300 مليار توكن، يمكن تدريب نموذج أصغر (70 مليار معامل) على 1.4 تريليون توكن بنفس ميزانية الحوسبة والحصول على أداء أفضل.

**القاعدة:** لكل معامل في النموذج، يجب تدريبه على ~20 توكناً.

### التأثير على التكلفة

| الادعاء | القيمة | المصدر | الثقة |
|---------|--------|--------|-------|
| Chinchilla (70B) تفوق على Gopher (280B) بنفس ميزانية الحوسبة | نعم | Hoffmann et al. (2022) | عالية |
| توفير في تكلفة الاستدلال (نموذج أصغر 4×) | ~75% | استنتاج منطقي | عالية |
| تأثير على Llama 2 (تدريب على 2T توكن لنموذج 70B) | موثق | Meta (2023) | عالية |

### أبعاد التكلفة المتأثرة

| البُعد بالعربية | البُعد بالإنجليزية | التأثير |
|-----------------|-------------------|---------|
| تكلفة التدريب | Training Cost | ↕ إعادة توزيع (ليس تقليل مباشر) |
| تكلفة الاستدلال | Inference Cost | ↓↓ نموذج أصغر = استدلال أرخص |
| الحوسبة | Compute | ↕ نفس الميزانية، أداء أفضل |
| تكلفة العتاد | Hardware Cost | ↓ نموذج أصغر يحتاج عتاد أقل للنشر |

### حالة البحث والتطور

- **2020:** قوانين Kaplan (OpenAI) — اقترحت تكبير النموذج أولاً.
- **2022:** قوانين Chinchilla (DeepMind) — صححت التوازن لصالح البيانات.
- **2023-2024:** Llama 2/3، Mistral — طبّقت مبدأ "التدريب الزائد" (Over-training): تدريب نموذج أصغر على بيانات أكثر بكثير من نسبة Chinchilla، لأن تكلفة الاستدلال أهم من تكلفة التدريب.
- **2025-2026:** الاتجاه الحالي هو "التدريب الزائد المتعمد" حيث يُدرَّب نموذج 8B على 15+ تريليون توكن. هذا يُخالف نسبة Chinchilla لكنه يُحسِّن التكلفة الإجمالية (تدريب + استدلال مدى الحياة).

### ملاحظة مهمة

قوانين Chinchilla تحسِّن **تكلفة التدريب فقط**. في الواقع، تكلفة الاستدلال تمثل 70-90% من التكلفة الإجمالية على مدى حياة النموذج. لذلك، الاتجاه الحديث يفضِّل نماذج أصغر مُدرَّبة على بيانات أكثر بكثير — حتى لو كانت "مُبذِّرة" حوسبياً في التدريب — لأنها أرخص في الاستدلال.

### المخاطر والقيود

1. **افتراض ثبات العتاد:** القوانين لا تأخذ في الاعتبار تغيّر تكاليف العتاد.
2. **جودة البيانات:** الحصول على بيانات كافية بجودة عالية تحدٍّ عملي.
3. **التطبيق المباشر محدود:** القوانين إرشادية وليست وصفة دقيقة.
4. **تغيّر المشهد:** Over-training أصبح هو المعيار، مما يُضعف الالتزام الحرفي بنسبة 1:20.

---

## English Content

### What are Compute-Optimal Scaling Laws?

Chinchilla Scaling Laws (Hoffmann et al., DeepMind, 2022) demonstrated that previous LLMs were trained with too many parameters on too little data. The key finding: for a fixed compute budget, model size and training data should scale proportionally at approximately a 1:20 ratio (parameters to tokens).

### Core Principle

Instead of training a huge model (280B params) on 300B tokens, training a smaller model (70B params) on 1.4T tokens with the same compute budget yields better performance.

### Important Nuance (2025-2026)

Chinchilla optimizes training cost alone. Since inference represents 70-90% of lifetime cost, the current trend favors "over-training": training smaller models on far more data than Chinchilla prescribes (e.g., Llama 3 8B on 15T+ tokens). This is compute-wasteful during training but yields cheaper inference at scale.

---

## المصادر | Sources

1. **[Tier 1]** Hoffmann, J., et al., "Training Compute-Optimal Large Language Models", NeurIPS 2022, DeepMind. arXiv:2203.15556
2. **[Tier 1]** Kaplan, J., et al., "Scaling Laws for Neural Language Models", OpenAI, 2020. arXiv:2001.08361
3. **[Tier 1]** Touvron, H., et al., "Llama 2: Open Foundation and Fine-Tuned Chat Models", Meta, 2023. arXiv:2307.09288
4. **[Tier 2]** Epoch AI, "How persistent is the inference cost burden?", March 2026. https://epochai.substack.com/p/how-persistent-is-the-inference-cost
