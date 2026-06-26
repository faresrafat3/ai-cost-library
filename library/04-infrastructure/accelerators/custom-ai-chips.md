---
id: entry-customchips-001
title_ar: شرائح الذكاء الاصطناعي المتخصصة — Trainium/Inferentia vs TPU vs GPU
title_en: "Custom AI Chips: AWS Trainium/Inferentia vs Google TPU vs NVIDIA GPU"
type: practical
status: deployed
category: infrastructure
subcategory: accelerators
cost_dimensions: [hardware-cost, training-cost, inference-cost, energy]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 3
created: 2026-06-26
scoring:
  A1: 7
  A2: 6
  A3: 6
  A4: 9
  B1: 7
  B2: 7
  B3: 3
  B4: 6
  C1: 3
  C2: 5
  C3: 7
  C4: 4
---

# 📘 شرائح AI المتخصصة | Custom AI Chips vs NVIDIA GPU

> **التصنيف:** 📘 عملية | **الإثبات:** ⭐⭐⭐

---

## المحتوى العربي

### الخيارات الثلاثة في 2026

| الشريحة | المُصنِّع | التخصص | المنصة |
|---------|----------|--------|--------|
| **NVIDIA GPU** (H100/B200) | NVIDIA | عام | كل السحابات |
| **AWS Trainium/Inferentia** | Amazon | تدريب/استدلال LLM | AWS فقط |
| **Google TPU** (v5e/v6e) | Google | تدريب/استدلال | GCP فقط |

### مقارنة التكلفة الشاملة

| المقياس | Trainium (AWS) | TPU v5e (GCP) | H100 (NVIDIA) |
|---------|---------------|---------------|---------------|
| $/ساعة لكل شريحة | ~$1.34 | ~$1.20 | **~$2.50-12.84** |
| تكلفة تدريب 1B tokens | ~$10K | ~$8K | ~$15K |
| Llama 70B tok/s (8 chips) | ~1,500 (est.) | 2,175 | **4,000+** |
| $/M tokens (استدلال 70B) | ~$0.40 (est.) | ~$0.30 (committed) | ~$0.23 (on-demand) |
| كفاءة الطاقة (perf/W) | **ممتازة** (2× A100) | **ممتازة** (5× أقل من H100) | جيدة |

### متى تختار كل واحد؟

```
هل أنت على AWS بالفعل + ميزانية محدودة؟
  ├── نعم → Inferentia2 (استدلال) أو Trainium (تدريب)
  │         50% أرخص من GPU instances على نفس المنصة
  └── لا

هل تحتاج أقصى مرونة + أوسع دعم؟
  ├── نعم → NVIDIA GPU — كل إطار عمل يدعمه
  └── لا

هل تدريبك ضخم (>100B tokens) وأنت على GCP؟
  ├── نعم → TPU v5e — 4-10× أكفأ تكلفة للتدريب الكبير
  └── لا → NVIDIA GPU (الخيار الآمن)
```

### ⚠️ المحاذير الحرجة

1. **Neuron SDK / XLA ≠ CUDA:** يحتاج تعديل كود + تجميع + اختبار
2. **ليس كل نموذج مدعوم:** تحقق من التوافق أولاً
3. **قفل المُورِّد:** Trainium = AWS فقط، TPU = GCP فقط
4. **GPU = الخيار الآمن:** إذا شككت، اختر NVIDIA
5. **Trainium2 (2026):** AWS تدّعي 25% من تكلفة H100 — يحتاج تحقق مستقل

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **GPU Inference Economics** | **يُكمل** — يُضيف بُعد الشرائح المتخصصة |
| **Self-Host vs API** | **يُؤثر** — Inferentia يُقلل نقطة التعادل على AWS |
| **DeepSeek V4/Llama 4** | **يعتمد** — بعض النماذج لا تعمل على Trainium/TPU بعد |

---

## المصادر

1. **[Tier 2]** StackPulsar, "AWS Trainium and Inferentia: A Production Guide", June 2026. Inferentia2 vs H100 comparison.
2. **[Tier 2]** CloudExpat, "AWS Trainium vs Google TPU v5e vs Azure H100", March 2026. Three-way comparison.
3. **[Tier 2]** Cerebrium, "AWS Trn1 & Inf2: Better Price-Performance", June 2026. Inference benchmarks.
