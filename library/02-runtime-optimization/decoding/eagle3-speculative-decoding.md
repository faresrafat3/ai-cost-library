---
id: entry-eagle3-001
title_ar: فك الترميز التخميني EAGLE-3
title_en: "EAGLE-3: State-of-the-Art Speculative Decoding"
type: practical
status: deployed
category: runtime-optimization
subcategory: decoding
cost_dimensions: [inference-cost, latency, throughput]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 3
created: 2026-06-26
scoring:
  A1: 8
  A2: 8
  A3: 9
  A4: 10
  B1: 7
  B2: 0
  B3: 0
  B4: 9
  C1: 7
  C2: 8
  C3: 8
  C4: 9
research_review:
  papers_scanned: 4
  papers_read: 2
  decision: "يُضاف — أحدث وأقوى تقنية speculative decoding. مُنشَر في PayPal."
---

# 📘 فك الترميز التخميني EAGLE-3

> **التصنيف:** 📘 عملية — مُنشَر | **الإثبات:** ⭐⭐⭐

---

## المحتوى العربي

### ما هو EAGLE-3؟

EAGLE-3 — وهو أحدث إصدار من سلسلة EAGLE لفك الترميز التخميني، يستخدم رأس مسودة خفيف (lightweight draft head) يدمج ميزات من طبقات منخفضة ومتوسطة وعالية للنموذج الأصلي للتنبؤ بالتوكنات القادمة بدقة عالية.

### لماذا EAGLE-3 وليس Speculative Decoding الأصلي؟

| | Speculative Decoding الأصلي | EAGLE-3 |
|---|--------------------------|---------|
| المسودة | نموذج مستقل أصغر | رأس مدمج في النموذج |
| الدقة | متوسطة | عالية (ميزات متعددة الطبقات) |
| التسريع (70B) | ~1.3× | **1.60×** |
| التكامل مع vLLM | ⚠️ | ✅ مدمج |

### الأدلة — PayPal دراسة حالة إنتاجية (مارس 2026)

PayPal نشرت EAGLE-3 على وكيلها التجاري (Commerce Agent) مع Nemotron-8B:

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| تحسن الإنتاجية (gamma=3) | **22-49%** | PayPal (arXiv:2604.19767) |
| تقليل زمن الاستجابة | **18-33%** | PayPal |
| معدل القبول (gamma=3) | ~35.5% (ثابت عبر كل الظروف) | PayPal |
| تقليل تكلفة GPU | **50%** (H100 واحد يُعادل NIM على اثنين) | PayPal |
| التأثير على جودة المخرجات | **صفر** (LLM-as-Judge) | PayPal |
| تسريع على Llama-3.3-70B عبر vLLM | **1.60×** | JarvisLabs benchmark |

### ConFu — أحدث من EAGLE-3 (أبريل 2026)

**arXiv:2603.08899:** يتفوق على EAGLE-3 بـ **8-21%** إضافية عبر "التأمل المستقبلي" — لكنه preprint.

### متى تستخدم

- ✅ أي خدمة استدلال حيث الزمن مهم
- ✅ مدمج في vLLM — تفعيل بسطر واحد
- ✅ لا يُغير مخرجات النموذج (lossless)

### متى لا تستخدم

- ❌ دفعات كبيرة جداً (batch > 56 — التسريع يتضاءل)
- ❌ نماذج MoE بدون MoE-Spec (يفقد كفاءته — انظر entry-moespec-001)

---

## المصادر

1. **[Tier 2]** Qin, A., et al., "Accelerating PayPal's Commerce Agent with EAGLE3", arXiv:2604.19767, March 2026. **دراسة حالة إنتاجية.**
2. **[Tier 2]** Li, Y., et al., "EAGLE-3: Scaling up Inference Acceleration", arXiv:2503.01840, March 2025.
3. **[Tier 2]** "ConFu: Contemplate the Future for Better Speculative Sampling", arXiv:2603.08899, April 2026. 8-21% over EAGLE-3.
