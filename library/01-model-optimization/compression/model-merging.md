---
id: entry-merging-001
title_ar: دمج النماذج — بديل رخيص للتدريب المتعدد المهام
title_en: "Model Merging: Zero-Cost Multi-Task Combination (TIES, DARE, Model Soup)"
type: practical
status: deployed
category: model-optimization
subcategory: compression
cost_dimensions: [training-cost, serving-cost, engineering-cost]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 3
created: 2026-06-26
scoring:
  A1: 7
  A2: 9
  A3: 9
  A4: 8
  B1: 3
  B2: 9
  B3: 0
  B4: 0
  C1: 8
  C2: 7
  C3: 6
  C4: 9
research_review:
  papers_scanned: 5
  papers_read: 2
  decision: "يُضاف — بديل مجاني تقريباً للتدريب المتعدد المهام. MergeBench (2025) يُعطي إرشادات عملية."
---

# 📘 دمج النماذج | Model Merging

> **التصنيف:** 📘 عملية | **الإثبات:** ⭐⭐⭐
>
> **أرخص طريقة لنموذج متعدد المهام: ادمج نماذج مُخصصة بدون إعادة تدريب**

---

## المحتوى العربي

### ما هو دمج النماذج؟

دمج النماذج (Model Merging) — وهو تقنية تجمع أوزان عدة نماذج مُضبطة (fine-tuned) في نموذج واحد بدون إعادة تدريب. بدلاً من تدريب نموذج واحد على كل المهام (مكلف)، تضبط نماذج منفصلة ثم تدمجها.

### لماذا يُقلل التكلفة؟

| النهج | التكلفة | المرونة |
|-------|---------|---------|
| تدريب متعدد المهام | عالية (كل البيانات + GPU ساعات) | منخفضة |
| خدمة نماذج منفصلة | عالية (GPU لكل نموذج) | عالية |
| **دمج النماذج** | **صفر تقريباً** (عملية حسابية فقط) | **عالية** |

### الطرق الأساسية (مرتبة بالتوصية — MergeBench 2025)

| الطريقة | الفكرة | التكلفة | التوصية |
|---------|--------|---------|---------|
| **Model Soup** | متوسط بسيط للأوزان | **صفر** — لا تدريب ولا ضبط | ✅ **ابدأ هنا** |
| **Task Arithmetic** | طرح الأساس + جمع التعديلات | منخفض | ✅ مع بيانات تحقق |
| **TIES** | حذف التعديلات الصغيرة + توحيد الإشارات | متوسط (ضبط عتبة) | ✅ لأداء أعلى |
| **DARE** | إسقاط عشوائي + إعادة تحجيم | متوسط | ⚠️ أقل استقراراً |
| **Localize-and-Stitch** | أقنعة ثنائية مُدرَّبة | أعلى (تدريب أقنعة) | ✅ لأعلى أداء |

### نتائج MergeBench (2025) — الإرشادات العملية

من أكبر دراسة مقارنة (Llama + Gemma، 2B-9B، 8 طرق، 5 مجالات):

1. **Model Soup أولاً** — صفر تكلفة، نتائج معقولة
2. **النماذج الأكبر تستفيد أكثر** — الدمج أفضل على 8B+ مقابل 2B
3. **النماذج المضبطة أساساً أفضل** — instruction-tuned base + دمج = أفضل نتيجة
4. **DARE أقل استقراراً** — الإسقاط العشوائي يُضر النماذج الكبيرة

### MergeMoE — الحدود الجديدة (2025)

يمكن دمج نماذج LoRA مختلفة في نموذج **MoE**:
- كل LoRA adapter = خبير
- **TIES/DARE على non-FFN layers** يتفوق على الدمج البسيط
- **النتيجة:** MoE من نماذج موجودة بدون تدريب MoE!

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **LoRA/QLoRA** | **تكاملي** — اضبط بـ LoRA ثم ادمج |
| **Multi-LoRA Serving** | **بديل** — Multi-LoRA = خدمة منفصلة، Merging = نموذج واحد |
| **Knowledge Distillation** | **بديل أبسط** — الدمج لا يحتاج بيانات تدريب |
| **MoE Economics** | **يُمكّن** — MergeMoE = MoE من نماذج موجودة |

---

## المصادر

1. **[Tier 2]** "MergeBench: A Benchmark for Merging Domain-Specialized LLMs", arXiv:2505.10833, May 2025. 8 methods, 5 domains, practical guidelines.
2. **[Tier 2]** "MergeME: Model Merging for Homogeneous and Heterogeneous MoE", arXiv:2502.00997, February 2025. TIES/DARE merging into MoE.
3. **[Tier 2]** "Mixup Model Merge (M3)", arXiv:2502.15434, February 2025. Improved contribution ratios.
