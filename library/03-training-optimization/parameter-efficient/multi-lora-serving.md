---
id: entry-multilora-001
title_ar: خدمة LoRA متعددة المستأجرين — مئات النماذج على GPU واحد
title_en: "Multi-LoRA Serving: Hundreds of Fine-Tuned Models on One GPU"
type: practical
status: deployed
category: training-optimization
subcategory: parameter-efficient
cost_dimensions: [hardware-cost, inference-cost, memory, serving-cost]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 5
created: 2026-06-26
scoring:
  A1: 8
  A2: 8
  A3: 8
  A4: 9
  B1: 8
  B2: 3
  B3: 8
  B4: 7
  C1: 6
  C2: 7
  C3: 9
  C4: 8
research_review:
  papers_scanned: 6
  papers_read: 3
  decision: "يُضاف — تقنية إنتاجية ناضجة تُقلل تكلفة العتاد بشكل كبير"
---

# 📘 خدمة LoRA متعددة المستأجرين | Multi-LoRA Serving

> **التصنيف:** 📘 عملية | **الإثبات:** ⭐⭐⭐
>
> **المسار:** المكتبة ← تحسين التدريب ← الضبط الموفّر

---

## المحتوى العربي

### المشكلة الاقتصادية

لديك 100 عميل، كل منهم يحتاج نموذج مُخصص. بدون Multi-LoRA:
- **100 GPU مُخصصة** — تكلفة خيالية
- أو تبديل النماذج يدوياً — بطيء ومعقد

مع Multi-LoRA:
- **نموذج أساسي واحد في الذاكرة** (99% من المعاملات)
- **محولات LoRA صغيرة لكل عميل** (1% من المعاملات)
- تبديل المحول في **5-10 مللي ثانية** (NVMe → VRAM)
- **GPU واحد يخدم 100+ عميل**

### كيف يعمل؟

```
ذاكرة GPU:
┌──────────────────────────────────┐
│  النموذج الأساسي (ثابت - 14GB)   │ ← يُحمّل مرة واحدة
├──────────────────────────────────┤
│  مخبأة LoRA (ساخنة - 2GB)        │ ← أكثر المحولات استخداماً
├──────────────────────────────────┤
│  KV Cache (ديناميكية - 8GB)      │ ← للطلبات النشطة
└──────────────────────────────────┘

ذاكرة CPU: مئات المحولات (دافئة)
NVMe SSD: آلاف المحولات (باردة)
```

### الأبحاث المُراجعة

#### 1. ServerlessLoRA (مايو 2025) — قُرئ
- مشاركة النموذج الأساسي عبر دوال معزولة
- **89% تقليل تكلفة** مقابل الحلول التقليدية
- **86% تقليل TTFT** عبر التحميل المسبق

#### 2. Prism — Multi-LLM Serving (مايو 2025) — قُرئ
- "Memory Ballooning" — ذاكرة GPU تتمدد وتنكمش ديناميكياً
- **2× تقليل تكلفة** أو 3.5× طلبات أكثر بنفس GPUs
- مبني على SGLang، مُختبر بـ 32 H100

#### 3. Compress then Serve (2025) — قُرئ
- يضغط 1000 محول LoRA في أساس مشترك + مصفوفات تكبير
- **80% من إنتاجية خدمة محول واحد** مع 1000 محول!

#### 4. LoRAServe (نوفمبر 2025)
- يُراعي اختلاف رتب المحولات (rank-aware)
- **50% تقليل GPU** مقابل S-LoRA

### الأرقام

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| عدد المستأجرين على GPU واحد | **100-1000+** | S-LoRA, Compress then Serve |
| تكلفة تبديل المحول | **5-10ms** | NVMe → VRAM |
| تقليل تكلفة العتاد | **89%** | ServerlessLoRA |
| إنتاجية مع 1000 محول | **80%** من محول واحد | Compress then Serve |
| تقليل GPU مع rank-awareness | **50%** | LoRAServe |

### متى تستخدم

- ✅ منصات SaaS تخدم عملاء متعددين بنماذج مُخصصة
- ✅ شركات بها أقسام مختلفة، كل قسم له نموذج
- ✅ خدمات API تقدم LoRA-as-a-Service

### المخاطر

1. **تداخل الأداء:** محولات كبيرة الرتبة تُبطئ المحولات الصغيرة
2. **إدارة الذاكرة:** تحتاج نظام eviction ذكي
3. **تعقيد التشغيل:** أكثر تعقيداً من خدمة نموذج واحد

---

## المصادر

1. **[Tier 2]** "ServerlessLoRA: Minimizing Latency and Cost", arXiv:2505.14468, May 2025. 89% cost reduction.
2. **[Tier 2]** "Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning", arXiv:2505.04021, May 2025. 2× cost reduction.
3. **[Tier 2]** "Compress then Serve: Serving Thousands of LoRA Adapters", arXiv:2407.00066v4, 2025. 80% throughput with 1000 LoRAs.
4. **[Tier 2]** "LoRAServe: Serving Heterogeneous LoRA Adapters", arXiv:2511.22880, November 2025. 50% GPU savings.
5. **[Tier 2]** "S-LoRA: Scalable LoRA Serving", 2024-2026. Unified paging + custom kernels.
