---
id: entry-mixedprec-001
title_ar: التدريب بالدقة المختلطة (BF16/FP8)
title_en: Mixed Precision Training (BF16/FP8)
type: practical
status: production-proven
category: training-optimization
subcategory: mixed-precision
cost_dimensions: [training-cost, memory, compute, energy]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 2
created: 2026-06-26
---

# 📘 التدريب بالدقة المختلطة | Mixed Precision Training

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐

## المحتوى العربي

### ما هو التدريب بالدقة المختلطة؟

التدريب بالدقة المختلطة — وهو استخدام دقة عددية أقل (BF16 بدلاً من FP32، أو FP8 بدلاً من BF16) لتسريع التدريب وتقليل استهلاك الذاكرة مع الحفاظ على جودة النموذج.

### التأثير على التكلفة

| التقنية | تقليل الذاكرة | تسريع التدريب | فقدان الجودة |
|---------|--------------|-------------|-------------|
| FP32 → BF16 | **2×** | **1.5-2×** | ضئيل جداً |
| BF16 → FP8 Training | **2×** إضافي | **1.3-1.8×** | يحتاج وصفات خاصة |

### الحالة في 2026

- **BF16:** المعيار الافتراضي لتدريب جميع النماذج الكبيرة (Llama 3, GPT-4, DeepSeek)
- **FP8 Training:** ناضج على Hopper/Blackwell، مُستخدم في LMSYS وDeepSeek. وصفة InfiR2 (arXiv:2510.22536) تُثبت استقرار FP8 للتدريب التعزيزي.

### بوابات الإثبات

| البوابة | BF16 | FP8 Training |
|---------|------|-------------|
| 🏗️ مبني | ✅ PyTorch, DeepSpeed | ✅ Transformer Engine, DeepGEMM |
| 🧪 مُختبر | ✅ | ✅ InfiR2 |
| 🚀 مُنشَر | ✅ كل نموذج كبير | ✅ LMSYS, DeepSeek |
| 💰 وفَّر | ✅ 2× ذاكرة + 1.5-2× سرعة | ✅ 2× إضافي |

---

## المصادر

1. **[Tier 1]** Micikevicius, P., et al., "Mixed Precision Training", ICLR 2018. NVIDIA.
2. **[Tier 2]** "InfiR2: A Comprehensive FP8 Training Recipe for Reasoning-Enhanced LLMs", arXiv:2510.22536, 2025.
