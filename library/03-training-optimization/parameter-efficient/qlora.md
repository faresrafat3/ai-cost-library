---
id: entry-qlora-001
title_ar: الضبط الدقيق المُكمَّم — QLoRA
title_en: "QLoRA: Quantized Low-Rank Adaptation"
type: practical
status: production-proven
category: training-optimization
subcategory: parameter-efficient
cost_dimensions: [training-cost, memory, hardware-cost]
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 2
created: 2026-06-26
updated: 2026-06-26
scoring:
  A1: 10
  A2: 10
  A3: 10
  A4: 6
  B1: 2
  B2: 10
  B3: 10
  B4: 0
  C1: 9
  C2: 9
  C3: 7
  C4: 10
---

# 📘 QLoRA — الضبط الدقيق المُكمَّم

> **التصنيف:** 📘 عملية — إنتاج مُثبت | **الإثبات:** ⭐⭐⭐⭐

---

## المحتوى العربي

### ما هو QLoRA؟

QLoRA (Quantized LoRA) — وهو تقنية تجمع بين تكميم النموذج الأساسي إلى 4-bit (NF4) والضبط الدقيق بمحولات LoRA منخفضة الرتبة. هذا يسمح بضبط نماذج 65B على **GPU واحد بـ 48GB** بدلاً من عدة GPUs.

### الابتكارات الثلاثة

1. **NF4 (Normal Float 4-bit):** تنسيق 4-bit مُحسَّن للتوزيع الطبيعي للأوزان — أدق من INT4
2. **Double Quantization:** تكميم ثوابت التكميم نفسها — يوفر 0.37 bit/param إضافية
3. **Paged Optimizers:** ينقل حالة المُحسِّن إلى CPU عند نفاد ذاكرة GPU

### التأثير على التكلفة

| المقياس | Full Fine-tuning | LoRA | **QLoRA** |
|---------|-----------------|------|----------|
| ذاكرة لنموذج 65B | ~780 GB | ~160 GB | **~48 GB** |
| عدد GPUs | 8+ A100 80GB | 2 A100 | **1 A100 48GB** أو RTX 4090 |
| تكلفة تقريبية (سحابي) | ~$200/ساعة | ~$50/ساعة | **~$3-6/ساعة** |
| المعاملات المُدرَّبة | 100% | ~0.1-1% | ~0.1-1% |
| الجودة مقابل Full FT | أساس | ~96-99% | ~93-97% |

### أمثلة عملية

- **ضبط Llama 2 70B:** على RTX 4090 (24GB) — مستحيل بأي طريقة أخرى
- **Guanaco 65B:** أول نموذج محادثة 65B مُضبط على GPU واحد (نتيجة QLoRA الأصلية)
- **آلاف النماذج على HuggingFace:** QLoRA هو المعيار للضبط على عتاد المستهلك

### القاعدة السريعة (2026)

```
ميزانية غير محدودة + أداء أقصى → Full Fine-tuning
ميزانية معقولة + أداء ممتاز     → LoRA (FP16/BF16)
GPU واحد + نموذج كبير           → QLoRA (الخيار الوحيد)
```

### المخاطر

1. **جودة أقل قليلاً:** NF4 base + LoRA = تراكم خطأين
2. **استدلال أبطأ:** النموذج المُكمَّم يحتاج de-quantization
3. **LoRA artifacts:** قد تظهر عيوب LoRA على مهام خارج التوزيع

---

## المصادر

1. **[Tier 1]** Dettmers, T., et al., "QLoRA: Efficient Finetuning of Quantized Language Models", NeurIPS 2023. arXiv:2305.14314.
2. **[Tier 1]** Hu, E., et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022. (الأساس).
