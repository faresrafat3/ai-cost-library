---
id: entry-gpuecon-001
title_ar: اقتصاديات GPU للاستدلال — مقارنة H100 vs B200 vs H200 (2026)
title_en: "GPU Inference Economics 2026: H100 vs B200 vs H200 Cost-per-Token"
type: practical
status: current-market-data
category: infrastructure
subcategory: accelerators
cost_dimensions: [hardware-cost, inference-cost, throughput, energy]
proof_score: "⭐⭐⭐ بيانات سوقية | Market Data"
sources_count: 4
created: 2026-06-26
scoring:
  A1: 9
  A2: 7
  A3: 8
  A4: 10
  B1: 9
  B2: 3
  B3: 5
  B4: 9
  C1: 4
  C2: 8
  C3: 9
  C4: 7
research_review:
  sources_read: 4
  decision: "يُضاف — بيانات MLPerf + أسعار سوق فعلية. ضرورية لقرارات العتاد."
---

# 📘 اقتصاديات GPU للاستدلال (2026) | GPU Inference Economics

> **التصنيف:** 📘 بيانات سوقية حالية | **الإثبات:** ⭐⭐⭐
>
> ⚠️ الأسعار تتغير — هذه لقطة يونيو 2026

---

## المحتوى العربي

### الجدول الشامل — تكلفة لكل مليون توكن (Llama 70B)

| GPU | $/ساعة (On-demand) | $/ساعة (Spot) | tok/s (FP8) | **$/M tokens (On-demand)** | **$/M tokens (Spot)** |
|-----|---------------------|---------------|-------------|---------------------------|----------------------|
| **H100 SXM** | $2.50 | $1.03 | ~3,066 | $0.227 | **$0.093** |
| **H200 SXM** | $4.54 | $1.77 | ~4,374 | $0.288 | $0.112 |
| **B200 (FP8)** | $6.03 | $2.12 | ~6,972 | $0.240 | **$0.084** |
| **B200 (FP4)** | $6.03 | $2.12 | ~12,841 | $0.130 | **$0.046** |

*المصدر: Spheron + MLPerf v6.0 (أبريل 2026)*

### الاكتشاف الأهم

> **B200 بسعر أعلى 2.4× لكل ساعة... لكن أرخص بسبب 4× إنتاجية!**
>
> - B200 FP4 Spot = **$0.046/M tokens** — أرخص خيار في السوق
> - H100 Spot = **$0.093/M** — ضعف B200 FP4 لكن أنضج
> - B200 On-demand FP8 = **$0.240/M** — أغلى من H100 On-demand!

### شجرة القرار — أي GPU (يونيو 2026)

```
نموذج ≤ 13B؟
├── نعم → L40S ($0.72/hr) أو RTX 5090 ($0.76/hr)
│         كافي مع INT4/FP8 + كثير من KV cache headroom
└── لا (70B+)
    │
    ├── تحمل Spot interruptions؟
    │   ├── نعم → B200 FP4 Spot ($2.12/hr) ← **الأرخص لكل توكن**
    │   │         17,500 tok/s (MLPerf v6.0)
    │   └── لا → هل 80GB كافية؟
    │           ├── نعم → H100 On-demand ($2.50/hr) ← **الأنضج والأرخص/ساعة**
    │           └── لا → B200 On-demand ($6.03/hr) ← 192GB + FP4
    │
    ├── تحتاج سياق 128K+؟
    │   └── نعم → B200 (192GB) أو H200 (141GB) ← KV cache يحتاج ذاكرة
    │
    └── نموذج 200B+ (DeepSeek-V3/V4)؟
        └── GB200 NVL72 ← rack-scale ($756-1944/hr للـ 72 GPU)
```

### أرقام Blackwell B200 — MLPerf v6.0 (أبريل 2026)

| المقياس | H100 | **B200** | التحسن |
|---------|------|---------|--------|
| tok/s (Llama 70B, offline) | ~3,000 | **~17,500** | **5.8×** |
| VRAM | 80 GB | **192 GB** | 2.4× |
| Memory BW | 3.35 TB/s | **8 TB/s** | 2.4× |
| FP4 Support | ❌ | ✅ أصلي | — |
| 70B على GPU واحد (FP16)? | ❌ (يحتاج 2) | **✅** | — |

### NVIDIA Rubin (R100) — القادم (H2 2026)

| المقياس | B200 | **R100 (متوقع)** |
|---------|------|-----------------|
| VRAM | 192 GB HBM3e | **288 GB HBM4** |
| Memory BW | 8 TB/s | **22 TB/s** |
| FP4 TFLOPS | 9,000 | **~50,000** |
| السعر المتوقع | $6-8/hr | **$8-12/hr spot** |
| التوفر | متاح الآن | **H2 2026** |

### المخاطر

1. **B200 supply محدود:** ~3.6M وحدة في قائمة الانتظار
2. **FP4 ليس لكل شيء:** يحتاج أوزان مُعايرة (calibrated) — لا يعمل مع أي نموذج
3. **Spot = انقطاع:** لا يصلح لـ APIs بـ SLA
4. **الأسعار تتغير شهرياً:** هذا الجدول = يونيو 2026

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **FP8 Quantization** | **تبعية** — B200 يستفيد أقصى من FP8/FP4 |
| **Self-Host vs API** | **يُحدد نقطة التعادل** — B200 Spot يُقلل العتبة |
| **GPU DVFS** | **تكاملي** — Decode memory-bound = خفض التردد يوفر طاقة |
| **MoE Economics** | **تكاملي** — B200 192GB يتسع لـ MoE أكبر |

---

## المصادر

1. **[Tier 2]** Spheron, "NVIDIA B200 Specs and Benchmarks", May 2026. MLPerf v6.0 data, pricing.
2. **[Tier 2]** Spheron, "Best GPU for AI Inference 2026", April 2026. Cost-per-token comparison.
3. **[Tier 2]** Inworld AI, "NVIDIA B200 GPU Guide", April 2026. $0.02/M tokens claim.
4. **[Tier 2]** Spheron, "NVIDIA Rubin vs Blackwell vs Hopper", March 2026. Generational comparison.
