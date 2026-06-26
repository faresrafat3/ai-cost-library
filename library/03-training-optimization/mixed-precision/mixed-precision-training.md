---
id: entry-mixedprec-001
title_ar: التدريب بالدقة المختلطة (BF16/FP8)
title_en: "Mixed Precision Training: BF16 as Standard, FP8 as Frontier"
type: practical
status: production-proven
category: training-optimization
subcategory: mixed-precision
cost_dimensions: [training-cost, memory, compute, energy, throughput]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 10
  A3: 10
  A4: 6
  B1: 0
  B2: 8
  B3: 8
  B4: 7
  C1: 8
  C2: 10
  C3: 10
  C4: 10
---

# 📘 التدريب بالدقة المختلطة | Mixed Precision Training

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐

---

## المحتوى العربي

### ما هو التدريب بالدقة المختلطة؟

التدريب بالدقة المختلطة — وهو استخدام دقة عددية مختلفة لأجزاء مختلفة من عملية التدريب: الأوزان والتفعيلات بدقة منخفضة (BF16 أو FP8) لتسريع الحساب وتقليل الذاكرة، مع الاحتفاظ بنسخة FP32 من الأوزان للتحديثات الدقيقة.

### المستويات الثلاثة (2026)

| المستوى | الاستخدام | التأثير | الحالة |
|---------|----------|---------|--------|
| **FP32 → BF16** | كل شيء: forward + backward + optimizer | **2× ذاكرة أقل + 1.5-2× أسرع** | ✅ المعيار منذ 2022 |
| **BF16 → FP8 Training** | forward + backward | **2× إضافي أسرع** | ✅ ناضج (Hopper+) |
| **FP8 Optimizer States** | حالة المُحسِّن | وفر إضافي | 🧪 ناشئ |

### لماذا BF16 وليس FP16؟

| | FP16 | **BF16** |
|---|------|---------|
| المدى الديناميكي | ±65,504 | **±3.4×10³⁸** (مثل FP32!) |
| الدقة | أعلى (10-bit mantissa) | أقل (7-bit) |
| خطر الانفجار/الانهيار | **عالٍ** (يحتاج loss scaling) | **لا يحتاج** |
| الحكم | تجنبه للتدريب | **الاختيار الصحيح** |

> BF16 يحافظ على نفس المدى الديناميكي لـ FP32 — يتجنب مشاكل التدرجات المتلاشية/المتفجرة بدون حيل.

### FP8 Training — الحدود الجديدة (2025-2026)

| المشروع | ماذا أثبت |
|---------|----------|
| **DeepSeek-V3** | أول تدريب FP8 ناجح على 671B معامل — أثبت الجدوى |
| **InfiR2 (arXiv:2510.22536)** | وصفة FP8 كاملة للتعلم التعزيزي مع التفكير — مستقر |
| **LMSYS (2025)** | FP8 للتعلم التعزيزي مع MoE — حل مشاكل KL loss |

### الكود (سطران!)

```python
# BF16 — سطر واحد في PyTorch
model = model.to(dtype=torch.bfloat16)

# FP8 — مع NVIDIA Transformer Engine
import transformer_engine.pytorch as te
model = te.TransformerLayer(..., fp8_recipe=te.FP8Recipe())
```

### التأثير الاقتصادي — أرقام حقيقية

| المقياس | FP32 | BF16 | FP8 |
|---------|------|------|-----|
| ذاكرة لنموذج 7B (أوزان فقط) | 28 GB | **14 GB** | **7 GB** |
| سرعة التدريب (H100) | أساس | **1.5-2×** | **2-3×** |
| تكلفة تدريب 70B (تقريبي) | $X | **$X/2** | **$X/3** |
| DeepSeek-V3 training cost | — | — | **$5.6M** (مقابل ~$15M+ بدون FP8) |

### العلاقة بتقنيات أخرى

| التقنية | العلاقة |
|---------|---------|
| **DeepSpeed ZeRO / FSDP** | **تكاملي** — mixed precision + distributed = أقصى كفاءة |
| **LoRA / QLoRA** | **تكاملي** — QLoRA يستخدم NF4 base + BF16 adapters |
| **FP8 Inference** | **نفس المبدأ** — لكن التدريب أصعب (تحتاج استقرار التدرجات) |
| **MoE** | **تكاملي** — DeepSeek-V3 يجمع FP8 + MoE + MLA |

---

## المصادر

1. **[Tier 1]** Micikevicius, P., et al., "Mixed Precision Training", **ICLR 2018**. NVIDIA. الورقة المؤسسة.
2. **[Tier 2]** "InfiR2: FP8 Training Recipe for Reasoning LLMs", arXiv:2510.22536, 2025. FP8 RL stability.
3. **[Tier 1]** DeepSeek-AI, "DeepSeek-V3 Technical Report", 2024-2026. First 671B FP8 training.
