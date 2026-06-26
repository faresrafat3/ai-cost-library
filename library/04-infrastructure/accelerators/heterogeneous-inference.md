---
id: entry-hetero-001
title_ar: الاستدلال على عتاد متنوع
title_en: "Heterogeneous Hardware Inference (GPU + NPU + Specialized)"
type: emerging
status: tested
category: infrastructure
subcategory: accelerators
tree_path: "AI Cost Library → Infrastructure → Accelerators → Heterogeneous Inference"
cost_dimensions:
  - hardware-cost
  - inference-cost
  - throughput
  - energy
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
research_review:
  papers_scanned: 4
  papers_read: 2
  decision: "يُضاف — اتجاه مهم يشمل GPU متنوعة + أجهزة محمولة + مسرّعات متخصصة"
---

# 🧪 الاستدلال على عتاد متنوع | Heterogeneous Hardware Inference

> **التصنيف:** 🧪 ناشئة | **الإثبات:** ⭐⭐
>
> **المسار:** المكتبة ← البنية التحتية ← المسرّعات

---

## المحتوى العربي

### ما هو الاستدلال المتنوع العتاد؟

بدلاً من استخدام GPUs متطابقة، هذا النهج يجمع أنواع مختلفة من المعالجات (GPU + CPU + NPU + مسرّعات متخصصة) لتنفيذ الاستدلال بأقل تكلفة.

### ثلاثة اتجاهات مُراجعة

#### 1. HeteroLLM — GPU + NPU على الأجهزة المحمولة
**arXiv:2501.14794 — 2025**

- أول محرك يتجاوز **1000 توكن/ثانية في مرحلة Prefill** على هاتف محمول
- يستغل GPU + NPU + CPU معاً على Qualcomm 8 Gen 3
- تقسيم الحوسبة على مستوى المصفوفات (tensor-level) وليس فقط الطبقات
- **تسريع 7.27× مقابل MLC** و **3.18× مقابل MNN**

#### 2. خدمة GPU غير متجانسة — تقليل التكلفة
**arXiv:2502.00722 — "Demystifying Cost-Efficiency in LLM Serving over Heterogeneous GPUs"**

- يُوزّع النموذج على خليط من GPUs مختلفة (مثل A100 + RTX 4090 + T4)
- يستخدم MILP (برمجة عدد صحيح مختلط) لإيجاد التوزيع الأمثل
- يدعم pipeline parallelism غير متماثل (طبقات أكثر على GPU الأقوى)
- **هدف:** تقليل التكلفة الإجمالية مع الحفاظ على SLA

#### 3. PLENA — مسرّع متخصص مع تصميم مشترك
**arXiv:2509.09505 — 2025**

- تصميم مشترك عتاد-برمجيات (hardware-software co-design)
- مصفوفة انقباضية مسطحة (flattened systolic array) مع دعم أصيل لـ FlashAttention
- **النتائج:** 2.24× إنتاجية أعلى من A100 + 3.85× أعلى من TPU v6e
- سيكون مفتوح المصدر

### التأثير على التكلفة

| السيناريو | التوفير |
|-----------|---------|
| خلط GPUs رخيصة + غالية بدلاً من كلها غالية | 30-60% تقليل تكلفة العتاد |
| استخدام NPU + GPU على المحمول | 7× تسريع → أقل وقت حوسبة |
| مسرّعات متخصصة (PLENA) | 2-4× إنتاجية أعلى لنفس الطاقة |

### المخاطر

1. **تعقيد التشغيل:** إدارة عتاد متنوع أصعب بكثير
2. **البرمجيات:** كل نوع عتاد يحتاج مكتبات مختلفة
3. **نضج محدود:** معظمها preprints أو protypes

---

## English Content

Heterogeneous inference combines different processor types (GPU + CPU + NPU + specialized accelerators). HeteroLLM achieves 7.27× speedup on mobile. Mixed-GPU serving reduces cost 30-60%. PLENA achieves 2.24× over A100.

---

## المصادر | Sources

1. **[Tier 2]** "HeteroLLM: Accelerating LLM Inference on Mobile SoCs with Heterogeneous Processors", arXiv:2501.14794, January 2025.
2. **[Tier 2]** "Demystifying Cost-Efficiency in LLM Serving over Heterogeneous GPUs", arXiv:2502.00722, February 2025.
3. **[Tier 2]** "PLENA: Hardware-Software Co-Designed System for Long-Context LLM Inference", arXiv:2509.09505, September 2025.

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **CPU-GPU Collaborative** | **حالة خاصة** — CPU+GPU = أبسط شكل من العتاد المتنوع |
| **Decentralized Inference** | **يُوسّع** — لامركزي = عتاد متنوع عبر الإنترنت |
| **Self-Host vs API** | **يُؤثر** — عتاد متنوع يُقلل نقطة التعادل |

### شجرة القرار — أي عتاد (2026)

```
ميزانية غير محدودة + أداء أقصى → H100/B200 متجانسة
ميزانية معقولة + أحمال مختلطة   → خلط GPU أنواع (Heterogeneous)
عتاد محمول + تطبيق محلي        → GPU + NPU (HeteroLLM)
بدون GPU + نموذج صغير           → CPU فقط (llama.cpp)
```
