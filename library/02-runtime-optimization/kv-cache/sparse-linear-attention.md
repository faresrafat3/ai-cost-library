---
id: entry-sparseatt-001
title_ar: الانتباه المتناثر والخطي — تسريع السياقات الطويلة 10×
title_en: "Sparse & Linear Attention: 10× Prefill Speedup for Long Contexts"
type: emerging
status: active-research
category: runtime-optimization
subcategory: kv-cache
cost_dimensions: [inference-cost, memory, throughput, latency]
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 5
created: 2026-06-26
scoring:
  A1: 4
  A2: 8
  A3: 7
  A4: 10
  B1: 8
  B2: 2
  B3: 8
  B4: 8
  C1: 3
  C2: 6
  C3: 7
  C4: 4
research_review:
  papers_scanned: 5
  papers_read: 3
  decision: "يُضاف — مجال بحثي حرج ونشط جداً (5+ أبحاث يونيو 2026). يحل المشكلة التربيعية."
---

# 🧪 الانتباه المتناثر والخطي | Sparse & Linear Attention

> **التصنيف:** 🧪 ناشئة — بحث نشط جداً | **الإثبات:** ⭐⭐
>
> **المشكلة الأساسية: الانتباه التقليدي = O(L²) — سياق 128K أغلى 16× من 32K**

---

## المحتوى العربي

### لماذا هذا حرج اقتصادياً؟

```
الانتباه التقليدي (Self-Attention):
  سياق 4K:   حوسبة = 16M عملية
  سياق 32K:  حوسبة = 1,024M عملية (64×!)
  سياق 128K: حوسبة = 16,384M عملية (1,024×!!)
  سياق 1M:   حوسبة = 1,000,000M عملية (💸💸💸)

مع انتشار سياقات 1M+ (DeepSeek V4, Llama 4 Scout 10M):
  → الانتباه التربيعي = عنق الزجاجة الأساسي
```

### 5 أبحاث حديثة جداً (مايو-يونيو 2026)

#### 1. SparDA — NVIDIA (يونيو 2026)
**arXiv:2606.04511 — NVIDIA Labs — قُرئ:**

- يُضيف projection رابع: **Forecast** (بجانب Q, K, V)
- Forecast يتنبأ بكتل KV المطلوبة **للطبقة التالية** → prefetch من CPU
- يتداخل النقل مع الحوسبة الحالية → لا انتظار

| الادعاء | القيمة |
|---------|--------|
| تسريع Prefill | **1.25×** |
| تسريع Decode | **1.7×** |
| تسريع Throughput (batch أكبر) | **حتى 5.3×** |
| معاملات إضافية | **< 0.5%** |
| يحتاج تدريب النموذج؟ | **لا** — يُدرَّب Forecast فقط |

#### 2. DLA — Dynamic Linear Attention (يونيو 2026)
**arXiv:2606.10650 — قُرئ:**

- انتباه خطي مع ذاكرة متعددة الحالات (multi-state)
- **المشكلة:** الطرق السابقة تدمج الحالات بسياسة ثابتة → تفقد توكنات مهمة
- **الحل:** دمج ديناميكي واعٍ بالمعلومات:
  - يحافظ على دقة عالية حول التحولات الدلالية
  - يضغط بشدة في المناطق المستقرة
- **التقييم:** 16 مجموعة بيانات × 3 فئات

#### 3. DHSA — Dynamic Hierarchical Sparse Attention (مايو 2026)
**arXiv:2510.24606:**

- يتنبأ بتناثر الانتباه online بينما النموذج مُجمَّد
- توجيه هرمي: chunk-level → token-level
- **النتائج:**
  - **10× تسريع Prefill** عند 128K سياق
  - **12-20% تحسن دقة** مقابل Block Sparse Attention
  - LLaMA-3.1-8B (4-bit) يعمل على **24GB GPU واحد عند 100K سياق** (بدون DHSA يفشل!)

#### 4. RetrievalAttention — بحث متجهي لـ KV Cache (2025)

- يُخرّج KV إلى CPU ويستخدم **ANNS (بحث الجار الأقرب)** لاسترجاع 1-3% فقط
- **4.9× تسريع** مقابل KNN الدقيق
- **128K tokens على RTX 4090 واحد (24GB)** — أول نظام يحقق هذا

#### 5. SALE — تقدير تناثر بـ 4-bit (مايو 2025)

- يستخدم Q,K مُكمّمة (4-bit) لتقدير أهمية كتل الانتباه بسرعة
- overhead التقدير = **11% فقط** من الانتباه الكامل
- يُحدد sparsity adaptively لكل إدخال

### خريطة المشهد

```
┌─────────────────────────────────────────────────┐
│              حلول السياق الطويل                   │
├────────────┬────────────┬───────────────────────┤
│  Sparse    │  Linear    │  Hybrid               │
│  Attention │  Attention │  (Transformer + SSM)   │
├────────────┼────────────┼───────────────────────┤
│ DHSA       │ DLA        │ Mamba-3 (ICLR 2026)   │
│ SparDA     │ Mamba/SSM  │ Falcon-H1R            │
│ SALE       │ RWKV       │ Jamba                  │
│ Retrieval  │            │                        │
│ Attention  │            │                        │
├────────────┼────────────┼───────────────────────┤
│ Training-  │ يحتاج      │ يحتاج                 │
│ free ✅    │ pretraining │ pretraining            │
│ O(L·k)    │ O(L)        │ O(L)                   │
└────────────┴────────────┴───────────────────────┘
```

### لماذا ⭐⭐ وليس أعلى؟

- ✅ مجال حرج — يحل أكبر عنق زجاجة (O(L²))
- ✅ أبحاث من NVIDIA + جامعات كبرى
- ❌ كلها preprints (يونيو 2026)
- ❌ لم تُنشر في محركات الإنتاج (vLLM/SGLang) بعد
- ❌ Sparse attention training-free ممتاز — لكن linear attention يحتاج pretraining

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **PagedAttention** | **يُكمل** — PagedAttention يُدير الذاكرة، Sparse يُقلل الحوسبة |
| **FlashAttention** | **يُكمل** — FlashAttention يُسرّع الانتباه الكثيف، Sparse يتجنب حسابه |
| **KV Cache Compression** | **بديل جزئي** — الاثنان يُقللان KV، بأساليب مختلفة |
| **Mamba-3 (SSM)** | **نهج مختلف** — SSM يتجنب الانتباه كلياً، Sparse يُبقيه لكن يُقلله |
| **Inference-Time Compute** | **تكاملي** — Sparse يجعل "التفكير الطويل" أرخص |

---

## المصادر

1. **[Tier 2]** Fu, Y., et al., "SparDA: Sparse Decoupled Attention", arXiv:2606.04511, June 2026. NVIDIA. 5.3× throughput.
2. **[Tier 2]** Wang, X., et al., "DLA: Dynamic Linear Attention", arXiv:2606.10650, June 2026. Dynamic multi-state memory.
3. **[Tier 2]** Xiong, S., et al., "DHSA: Dynamic Hierarchical Sparse Attention", arXiv:2510.24606, 2025-2026. 10× prefill, 100K on 24GB.
4. **[Tier 2]** "RetrievalAttention: ANNS for KV Cache", arXiv:2409.10516v2, 2024-2025. 128K on single RTX 4090.
5. **[Tier 2]** "SALE: Low-bit Estimation for Sparse Attention", arXiv:2505.24179, May 2025. 4-bit estimation, 11% overhead.
