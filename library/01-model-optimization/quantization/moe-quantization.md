---
id: entry-moequant-001
title_ar: تكميم نماذج مزيج الخبراء (MoE Quantization)
title_en: "MoE Quantization: Compressing Expert Models to Ultra-Low Bits"
type: emerging
status: active-research
category: model-optimization
subcategory: quantization
cost_dimensions: [memory, inference-cost, hardware-cost, throughput]
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 4
created: 2026-06-26
scoring:
  A1: 3
  A2: 8
  A3: 7
  A4: 10
  B1: 7
  B2: 0
  B3: 9
  B4: 7
  C1: 3
  C2: 6
  C3: 7
  C4: 4
research_review:
  papers_scanned: 5
  papers_read: 3
  decision: "يُضاف — مجال بحثي نشط جداً (4+ أبحاث في 2026). حرج لنشر DeepSeek/Llama4/Qwen3 MoE."
  limitations_noted: "كلها preprints. لم تُنشر إنتاجياً بعد."
---

# 🧪 تكميم نماذج MoE | MoE Quantization

> **التصنيف:** 🧪 ناشئة — بحث نشط | **الإثبات:** ⭐⭐
>
> **المشكلة: MoE يحتاج كل الخبراء في الذاكرة — حتى غير المُفعَّلين**

---

## المحتوى العربي

### لماذا تكميم MoE أصعب من التكميم العادي؟

نموذج MoE مثل DeepSeek-V3 (671B) يُفعّل فقط 37B لكل توكن — لكن **كل الـ671B يجب أن تكون في الذاكرة!**

| النموذج | معاملات كلية | مُفعَّلة | **ذاكرة مطلوبة (FP16)** |
|---------|-------------|---------|---------------------|
| DeepSeek-V3 | 671B | 37B | **~1.2 TB** |
| Llama 4 Maverick | 400B | 17B | **~800 GB** |
| Qwen3-235B | 235B | 22B | **~470 GB** |

> التكميم هو الطريقة الوحيدة لتشغيل هذه النماذج على عتاد معقول.

### الأبحاث الحديثة المُراجعة (2026)

#### 1. BitsMoE — تكميم MoE بالطاقة الطيفية (مايو 2026)
**arXiv:2606.00079 — قُرئ:**

**الفكرة:** يفكك كل طبقة MoE بـ SVD إلى:
- **أساس مشترك** بين الخبراء → لا يُكمَّم (يحافظ على البنية المشتركة)
- **عوامل طيفية خاصة بكل خبير** → تُكمَّم بدقة متغيرة

**النتائج على Qwen3-30B-A3B (2-bit):**

| الادعاء | القيمة |
|---------|--------|
| تحسن الدقة مقابل GPTQ عند 2-bit | **+27.83 نقطة مئوية** |
| تسريع التكميم | **12.3×** |
| تسريع فك الترميز | **1.76×** |

> **27.83 نقطة تحسن = الفرق بين نموذج مُدمَّر ونموذج يعمل عند 2-bit!**

#### 2. MoE Mixed-Precision بضمانات نظرية (أبريل 2026)
**arXiv:2604.06515 — قُرئ:**

- يُخصص دقة (bits) لكل خبير حسب **تغيّر norm التوجيه أثناء التدريب**
- الخبراء ذات التغيّر الأقل (تلتقط ميزات نادرة ومهمة) → دقة أعلى
- **النتيجة:** دقة أعلى من الطرق السابقة + تقليل تكلفة الاستدلال

#### 3. MoBiE — تحويل خبراء MoE إلى ثنائي (1-bit!) (أبريل 2026)
**arXiv:2604.06798:**

- أول محاولة لتحويل خبراء MoE إلى **1-bit** (ثنائي)
- يستخدم SVD مشترك + حجب خطأ التكميم في الفضاء الفارغ (null space)
- **المشكلة المُكتشفة:** التكميم يُسبب "انزياح الخبراء" (expert-shift) — التوكنات تتحول لخبراء مختلفين

#### 4. Expert-Divergence Loss — تحسين تخصص الخبراء (ICLR 2026)
**مُراجع أقران:**

- بدلاً من توازن الحمل (load balancing) الذي يُجانس الخبراء، يُعظّم التباعد بينهم
- خبراء أكثر تخصصاً = تكميم أسهل (كل خبير أبسط)
- **مقبول في ICLR 2026**

### ملخص المشهد البحثي

```
تكميم Dense LLM (GPTQ/AWQ/FP8) ← ناضج ✅
تكميم MoE LLM ← نشط جداً 🧪
  ├── Mixed-Precision لكل خبير ← واعد (أبريل 2026)
  ├── SVD + Spectral (BitsMoE) ← أقوى نتيجة (مايو 2026)
  ├── 1-bit/Binary (MoBiE) ← مبكر جداً
  └── تحسين التخصص (ICLR 2026) ← يُسهّل التكميم
```

### لماذا ⭐⭐ وليس أعلى؟

- ✅ مجال حرج — كل النماذج الحدودية MoE
- ✅ نتائج أكاديمية قوية (BitsMoE: +27.83 نقطة!)
- ❌ كلها preprints (باستثناء Expert-Divergence ICLR 2026)
- ❌ لم تُنشر إنتاجياً بعد
- ❌ التوافق مع محركات الاستدلال (vLLM/SGLang) محدود

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **GPTQ/AWQ** | **الأساس** — BitsMoE يبني على مبادئ مشابهة لكن مُكيَّفة لـ MoE |
| **FP8** | **بديل أبسط** — FP8 يعمل على MoE لكن 2× ذاكرة مقابل 4-bit |
| **MoE Economics** | **يُمكّن** — التكميم يجعل DeepSeek-V3 يعمل على عتاد أقل |
| **MoE-Spec** | **تكاملي** — speculative decoding + تكميم MoE = أقصى كفاءة |
| **CPU-GPU Collaborative** | **تكاملي** — خبراء مُكمّمة = أسهل للتخزين المؤقت على GPU |

---

## المصادر

1. **[Tier 2]** Zhao, J., et al., "BitsMoE: Spectral Energy-Guided Bit Allocation for MoE Quantization", arXiv:2606.00079, May 2026. +27.83pp accuracy, 12.3× faster quantization. **قُرئ.**
2. **[Tier 2]** Chowdhury, M., et al., "Efficient Quantization of MoE with Theoretical Guarantees", arXiv:2604.06515, April 2026. Router-norm guided mixed precision. **قُرئ.**
3. **[Tier 2]** "MoBiE: Efficient Inference of Mixture of Binary Experts", arXiv:2604.06798, April 2026. 1-bit expert binarization. **ملخص مقروء.**
4. **[Tier 1]** "Expert-Divergence Loss for MoE Training", **ICLR 2026**. Improving specialization for better quantization.
