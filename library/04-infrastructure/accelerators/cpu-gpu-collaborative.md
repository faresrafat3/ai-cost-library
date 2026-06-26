---
id: entry-cpugpu-001
title_ar: الاستدلال التعاوني بين المعالج ووحدة الرسومات
title_en: "CPU-GPU Collaborative Inference for LLMs"
type: emerging
status: peer-reviewed
category: infrastructure
subcategory: accelerators
tree_path: "AI Cost Library → Infrastructure → Accelerators → CPU-GPU Collaborative"
cost_dimensions:
  - hardware-cost
  - memory
  - inference-cost
  - throughput
proof_score: "⭐⭐ نموذج أولي مُراجع | Peer-Reviewed Prototype"
sources_count: 3
created: 2026-06-26
updated: 2026-06-26
research_review:
  papers_scanned: 3
  papers_read: 2
  decision: "يُضاف — مجال نشط مع 3+ أبحاث، مقبول في ASP-DAC 2026"
  limitations_noted: "مُختبر على عتاد محدود، لم يُنشر تجارياً"
---

# 🧪 الاستدلال التعاوني CPU-GPU | CPU-GPU Collaborative Inference

> **التصنيف:** 🧪 ناشئة — مُراجعة أقران | **الإثبات:** ⭐⭐
>
> **المسار:** المكتبة ← البنية التحتية ← المسرّعات

---

## المحتوى العربي

### ما هو الاستدلال التعاوني CPU-GPU؟

الاستدلال التعاوني بين المعالج المركزي (CPU) ووحدة معالجة الرسومات (GPU) — وهو نهج يستغل كلا المعالجين معاً بدلاً من الاعتماد على GPU فقط، خاصة عندما لا تتسع ذاكرة GPU لكامل النموذج.

### لماذا هذا مهم؟

- نماذج MoE مثل Mixtral 8x7B تحتاج ~90 جيجابايت — أكثر من RTX 4090 (24GB)
- الطريقة التقليدية: نقل الأوزان بين CPU وGPU (بطيء جداً عبر PCIe)
- **الحل الجديد:** بدلاً من النقل، CPU يحسب مباشرة للأجزاء غير الموجودة على GPU

### الأبحاث المُراجعة

#### 1. MoE CPU-GPU Collaborative (ASP-DAC 2026 — مُراجع أقران)
**arXiv:2512.16473 — ELSA Lab**

**ماذا يفعل:**
- يُخزّن الخبراء الأكثر استخداماً على GPU (expert cache)
- عند إصابة التخزين المؤقت: GPU يحسب (سريع)
- عند إخفاق: CPU يحسب بالتوازي + ينقل الخبير إلى GPU للمستقبل
- يستغل تعدد مسارات CPU (multithreading)

**النتائج:**
- إنتاجية تتجاوز GPU-only (لأن CPU يعمل أثناء انتظار النقل)
- 30-50% احتمال إعادة استخدام الخبير في الخطوة التالية (Mixtral)
- لا يحتاج تعديل النموذج أو تحليل مسبق للبيانات

#### 2. HGCA — Hybrid GPU-CPU Attention (2025)
**arXiv:2507.03153**

**ماذا يفعل:**
- يُفرّغ أجزاء من KV cache إلى ذاكرة CPU
- CPU ينفذ انتباه متناثر (sparse) بالتوازي مع GPU
- يُحوّل CPU من "مخزن بيانات" إلى "شريك حوسبي"

**النتائج:**
- يُمكّن سياق أطول بكثير على GPU واحد
- أداء مقارب لـ 2 GPU باستخدام GPU واحد + CPU

#### 3. SKIP Profiler — تشخيص أحمال CPU-GPU (2025)
**arXiv:2504.11750**

- أداة تحليل لفهم أين ينتقل حمل العمل من CPU-bound إلى GPU-bound
- يحدد "منطقة العتبة الحرجة" لكل نموذج وعتاد

### التأثير على التكلفة

| الادعاء | القيمة |
|---------|--------|
| تشغيل Mixtral 8x7B على RTX 4090 (24GB) | ممكن (بدلاً من GPU 80GB+) |
| تقليل تكلفة العتاد | ~4× (RTX 4090 vs A100 80GB) |
| تحسن الإنتاجية مقابل GPU-only offloading | تتجاوزه (CPU يحسب بدلاً من الانتظار) |

### المخاطر والقيود

1. **سرعة PCIe:** عنق زجاجة أساسي — PCIe 4.0/5.0 أبطأ بكثير من NVLink
2. **قدرة CPU:** FP16/BF16 على CPU أبطأ 10-100× من GPU — مناسب للأجزاء الصغيرة فقط
3. **تعقيد البرمجة:** يحتاج إدارة ذاكرة دقيقة وجدولة بين المعالجين
4. **ليس للخدمة عالية التزامن:** مناسب لطلب واحد أو عدد قليل على عتاد محدود

---

## English Content

CPU-GPU collaborative inference uses both processors together instead of GPU-only, especially when the model exceeds GPU memory. Instead of slow CPU-GPU data transfers, the CPU directly computes on non-cached portions while GPU handles cached data.

**Key paper:** MoE CPU-GPU Collaborative (ASP-DAC 2026) — runs Mixtral 8x7B on RTX 4090 by caching hot experts on GPU and computing cold experts on CPU.

---

## المصادر | Sources

1. **[Tier 1]** "Efficient CPU-GPU Collaborative Inference for MoE-based LLMs on Consumer-Grade Hardware", **ASP-DAC 2026** (مقبول), arXiv:2512.16473. ELSA Lab.
2. **[Tier 2]** "HGCA: Hybrid GPU-CPU Attention for Long Context LLM Inference", arXiv:2507.03153, July 2025.
3. **[Tier 2]** "Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures", arXiv:2504.11750, April 2025.
