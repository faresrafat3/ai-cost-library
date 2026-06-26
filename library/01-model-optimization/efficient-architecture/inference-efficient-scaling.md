---
id: entry-iescaling-001
title_ar: قوانين التحجيم المعماري لكفاءة الاستدلال
title_en: Architecture-Aware Scaling Laws for Inference-Efficient LLMs
type: theoretical
status: peer-reviewed
category: model-optimization
subcategory: efficient-architecture
tree_path: "AI Cost Library → Model Optimization → Efficient Architecture → Inference-Efficient Scaling"
cost_dimensions:
  - inference-cost
  - throughput
  - training-cost
proof_score: "⭐⭐⭐ مُراجع أقران | Peer-Reviewed"
sources_count: 1
created: 2026-06-26
updated: 2026-06-26
research_review:
  paper_read: true
  full_text_scanned: true
  venue: "ICLR 2026 (Tier 1)"
  decision: "يُضاف — بحث Tier 1 مع 200+ نموذج مُدرَّب ونتائج كمية قوية"
  limitations_noted: "نظري — لا توجد نماذج إنتاجية تجارية مبنية عليه بعد"
---

# 📐 قوانين التحجيم المعماري لكفاءة الاستدلال

> **التصنيف:** 📐 نظرية — مُراجعة أقران (ICLR 2026) | **الإثبات:** ⭐⭐⭐
>
> **المسار:** المكتبة ← تحسين النموذج ← البنية الفعّالة

---

## المحتوى العربي

### ما هو هذا البحث؟

هذا البحث يوسّع قوانين Chinchilla ليشمل **عوامل معمارية** تؤثر على كفاءة الاستدلال. بدلاً من السؤال "كم معامل وكم بيانات؟" فقط، يسأل أيضاً "ما الشكل الأمثل للنموذج؟":

- **حجم البُعد المخفي** (hidden size): أكبر = إنتاجية أعلى (لأن عدد الطبقات أقل)
- **نسبة MLP إلى الانتباه** (mlp-to-attention ratio): أعلى = إنتاجية أعلى + KV cache أصغر
- **الانتباه الجماعي** (GQA — Grouped-Query Attention): مجموعات أكثر = إنتاجية أعلى

### النتائج الأساسية

| الادعاء | القيمة | التفاصيل |
|---------|--------|----------|
| تحسن الدقة مقابل LLaMA-3.2 بنفس ميزانية التدريب | +2.1% | على معايير MMLU, HellaSwag, ARC |
| تحسن إنتاجية الاستدلال | +42% | tokens/s على نفس العتاد |
| عدد النماذج المُدرَّبة للتحقق | 200+ | من 80M إلى 3B معامل |
| مصدر المؤتمر | ICLR 2026 | مراجعة أقران — Tier 1 |

### لماذا هذا مهم؟

قوانين Chinchilla تقول "كم؟" — هذا البحث يقول "بأي شكل؟". مع نفس عدد المعاملات ونفس ميزانية التدريب:
- نموذج "عريض وقصير" (hidden كبير، طبقات أقل) أسرع في الاستدلال من نموذج "ضيق وطويل"
- زيادة نسبة MLP/Attention تقلل حجم KV cache وتحسّن الإنتاجية

### الآلية: قانون التحجيم الشرطي

البحث يقدم صيغة رياضية تتنبأ بخسارة التدريب كدالة في:
- N (عدد المعاملات)
- D (عدد توكنات التدريب)
- d_model (حجم البُعد المخفي)
- r_mlp/attn (نسبة MLP إلى الانتباه)

هذا يسمح بالبحث عن البنية المثلى التي تُوازن بين الدقة وكفاءة الاستدلال **قبل التدريب**.

### لماذا ⭐⭐⭐ وليس أعلى؟

- ✅ مُراجع من أقران في ICLR 2026 (أعلى مؤتمرات التعلم الآلي)
- ✅ نتائج مُكررة على 200+ نموذج
- ❌ لا توجد نماذج تجارية مبنية صراحة على هذه القوانين بعد
- ❌ الاختبار على نماذج حتى 3B فقط — التعميم على 70B+ غير مؤكد

### المخاطر والقيود

1. **التعميم:** القوانين مُستخرجة من نماذج 80M-3B — قد لا تنطبق بدقة على نماذج أكبر.
2. **تفاعلات مع التقنيات الأخرى:** لم يُدرس التفاعل مع التكميم أو MoE.
3. **تكلفة التطبيق:** تحسين البنية يتطلب إعادة تدريب كاملة — لا يمكن تطبيقه على نماذج موجودة.

---

## English Content

### What is this research?

This paper extends Chinchilla scaling laws with architectural factors affecting inference efficiency. It introduces a conditional scaling law that predicts optimal model shape (hidden size, MLP-to-attention ratio, GQA) for simultaneously maximizing accuracy and inference throughput.

### Key Results

- +2.1% accuracy and +42% inference throughput vs LLaMA-3.2 at the same training budget
- Validated across 200+ trained models (80M to 3B parameters)
- Published at ICLR 2026 (Tier 1 venue)

### Why ⭐⭐⭐?

Peer-reviewed at a top venue with strong empirical validation, but no commercial models built on these laws yet, and validation limited to ≤3B models.

---

## المصادر | Sources

1. **[Tier 1]** Bian, S., Yu, T., Venkataraman, S., Park, Y., "Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs", **ICLR 2026**, arXiv:2510.18245. UW-Madison + Amazon Web Services.
