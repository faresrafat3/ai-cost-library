---
id: entry-deepspeed-001
title_ar: التدريب الموزّع — DeepSpeed ZeRO و FSDP
title_en: "Distributed Training: DeepSpeed ZeRO & PyTorch FSDP"
type: practical
status: production-proven
category: training-optimization
subcategory: distributed-training
tree_path: "AI Cost Library → Training Optimization → Distributed Training → DeepSpeed/FSDP"
cost_dimensions:
  - training-cost
  - memory
  - hardware-cost
  - compute
proof_score: "⭐⭐⭐⭐ إنتاج | Production-Proven"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
research_review:
  decision: "يُضاف — أساسي لتدريب أي نموذج كبير، مُستخدم في Llama 3, DeepSeek, وغيرها"
---

# 📘 التدريب الموزّع — DeepSpeed ZeRO و FSDP

> **التصنيف:** 📘 عملية — إنتاج مُثبَت | **الإثبات:** ⭐⭐⭐⭐
>
> **المسار:** المكتبة ← تحسين التدريب ← التدريب الموزّع

---

## المحتوى العربي

### ما هو التدريب الموزّع؟

التدريب الموزّع — وهو توزيع عملية تدريب النموذج على عدة وحدات معالجة رسومية (GPU) لتسريع التدريب وتمكين تدريب نماذج أكبر من سعة ذاكرة GPU واحدة.

### الأنظمة الأساسية

#### DeepSpeed ZeRO (مايكروسوفت)
ZeRO (Zero Redundancy Optimizer) — وهو نظام يزيل التكرار في تخزين حالة المُحسِّن والتدرجات والمعاملات عبر GPUs:

| المرحلة | ما يُوزَّع | تقليل الذاكرة |
|---------|-----------|-------------|
| ZeRO-1 | حالة المُحسِّن فقط | ~4× |
| ZeRO-2 | + التدرجات | ~8× |
| ZeRO-3 | + المعاملات | الذاكرة تتناسب مع 1/N (عدد GPUs) |

#### PyTorch FSDP
FSDP (Fully Sharded Data Parallelism) — وهو تطبيق PyTorch الرسمي لنفس فكرة ZeRO-3:
- يُقسّم المعاملات عبر GPUs
- يجمعها عند الحاجة (all-gather) ثم يحررها
- **FSDPv2** يدعم الجلب المسبق (prefetching) لتداخل الحوسبة والاتصال

### التأثير على التكلفة

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| تقليل ذاكرة GPU المطلوبة | حتى 8× (ZeRO-3) | Microsoft DeepSpeed docs |
| تمكين تدريب 70B على 8 GPUs | ممكن (مع offloading) | Llama 2/3 training |
| تقليل عدد GPUs المطلوبة | خطّي مع عدد المعاملات | مُثبت عملياً |

### أرقام حديثة من الأبحاث

| البحث | النتيجة |
|-------|---------|
| DeepCompile (2025) | 1.28× تسريع فوق ZeRO-3 على Llama 3 70B |
| Hardware Scaling (2025) | FSDP: عوائد متناقصة >32 عقدة (30%+ فقدان كفاءة طاقة) |

### بوابات الإثبات

| البوابة | الحالة |
|---------|--------|
| 🏗️ مبني | ✅ — DeepSpeed (مفتوح المصدر، مايكروسوفت)، PyTorch FSDP (رسمي) |
| 🧪 مُختبر | ✅ — آلاف المعايير والتقارير |
| 🚀 مُنشَر | ✅ — Llama 2/3 (Meta)، DeepSeek، Qwen، وعشرات النماذج الأخرى |
| 💰 وفَّر | ✅ — يُمكّن تدريب نماذج تُساوي ملايين الدولارات على عتاد أقل |

### متى تستخدم

- ✅ أي تدريب لنموذج أكبر من سعة GPU واحدة
- ✅ ضبط دقيق لنماذج 7B+ على عدة GPUs
- ✅ عند الرغبة في تسريع التدريب بالتوزيع

### متى لا تستخدم

- ❌ نماذج صغيرة تتسع على GPU واحدة (التوزيع يضيف تعقيداً ولا يفيد)
- ❌ عند عدم توفر شبكة سريعة بين GPUs (الاتصال يصبح عنق الزجاجة)

---

## English Content

### DeepSpeed ZeRO & PyTorch FSDP

The two dominant frameworks for distributed LLM training. ZeRO eliminates redundancy across GPUs (optimizer state → gradients → parameters). FSDP is PyTorch's official implementation of the same idea.

**Used in production by:** Meta (Llama 2/3), DeepSeek, Qwen, Mistral, and virtually every large model trained since 2023.

---

## المصادر | Sources

1. **[Tier 1]** Rajbhandari, S., et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", SC 2020. Microsoft.
2. **[Tier 1]** Zhao, Y., et al., "PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel", VLDB 2023. Meta.
3. **[Tier 2]** Wei, Z., et al., "DeepCompile: A Compiler-Driven Approach to Optimizing Distributed Training", arXiv:2504.09983, 2025.
4. **[Tier 2]** Hagemann, B., et al., "Hardware Scaling Trends and Diminishing Returns in Large-Scale Distributed Training", arXiv:2411.13055, 2025.
