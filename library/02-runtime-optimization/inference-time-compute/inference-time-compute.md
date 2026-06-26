---
id: entry-ttc-001
title_ar: اقتصاديات حوسبة وقت الاستدلال (Inference-Time Compute)
title_en: "Inference-Time Compute Economics: When Thinking More Costs Less"
type: practical
status: deployed
category: runtime-optimization
subcategory: inference-time-compute
cost_dimensions: [inference-cost, token-cost, compute, latency]
proof_score: "⭐⭐⭐ منشور | Deployed"
sources_count: 5
created: 2026-06-26
scoring:
  A1: 9
  A2: 9
  A3: 7
  A4: 10
  B1: 5
  B2: 0
  B3: 0
  B4: 0
  C1: 4
  C2: 7
  C3: 7
  C4: 6
research_review:
  papers_scanned: 5
  papers_read: 3
  decision: "يُضاف — اتجاه حرج في 2025-2026. المفارقة: التفكير أكثر = أرخص أحياناً."
---

# 📘 اقتصاديات حوسبة وقت الاستدلال | Inference-Time Compute Economics

> **التصنيف:** 📘 عملية — مُنشر | **الإثبات:** ⭐⭐⭐
>
> **المسار:** المكتبة ← تحسين التشغيل ← حوسبة وقت الاستدلال

---

## المحتوى العربي

### ما هي حوسبة وقت الاستدلال؟

حوسبة وقت الاستدلال (Test-Time Compute / Inference-Time Compute) — وهي تخصيص حوسبة إضافية أثناء الاستدلال (سلاسل تفكير أطول، عينات متعددة، تحقق ذاتي) لتحسين جودة الإجابة. النماذج مثل o3, DeepSeek-R1, Claude مع "extended thinking" تستخدم هذا النهج.

### المفارقة الاقتصادية الأساسية

> **"نموذج أصغر يُفكّر أكثر" قد يكون أرخص من "نموذج أكبر يُجيب فوراً"**

| النهج | التكلفة | الجودة | مناسب لـ |
|-------|---------|--------|---------|
| نموذج كبير + إجابة فورية | عالية لكل طلب | عالية | مهام بسيطة-متوسطة |
| نموذج صغير + تفكير طويل | منخفضة لكل توكن، عالية إجمالاً | عالية جداً | مهام معقدة (رياضيات، كود) |
| نموذج صغير + تفكير + توقف مبكر | **الأرخص** | عالية (إذا مُعاير جيداً) | مهام معقدة مع حد ميزانية |

### الأبحاث الحديثة المُراجعة

#### 1. Overthinking Tax — النموذج الأصغر ليس دائماً أرخص!
**OckBench (arXiv:2511.05722, 2025-2026) — قُرئ:**

اكتشاف صادم: DeepSeek-R1-Distill-7B يُنتج **3.13×** توكنات أكثر من نسخة 14B لنفس المهمة.
- 7B: $0.05/M token × 41,415 tokens = **$2.07 لكل استعلام**
- 14B: $0.10/M token × 13,211 tokens = **$1.32 لكل استعلام**
- **النموذج "الأرخص" أغلى 57% فعلياً!**

**السبب:** النماذج الأصغر "تُفرط في التفكير" — تُنتج سلاسل تفكير أطول بكثير لتعويض قدرتها المحدودة.

#### 2. Kinetics Scaling Law — قانون تحجيم جديد (يونيو 2025)
**arXiv:2506.05333 — قُرئ:**

- قوانين التحجيم السابقة بالغت في تقدير فعالية النماذج الصغيرة
- **الاكتشاف:** في حوسبة وقت الاستدلال، الانتباه (Attention) وليس المعاملات هو التكلفة المهيمنة
- **الحل:** Sparse Attention يُقلل تكلفة التوكن → يسمح بتفكير أطول بنفس الميزانية
- **النتيجة:** +60 نقطة في الأنظمة منخفضة التكلفة مع Sparse Attention

#### 3. Sleep-Time Compute — التفكير المُسبق (أبريل 2025)
**arXiv:2504.13171 — قُرئ:**

- بدلاً من التفكير وقت الطلب، "فكّر مسبقاً" عن السياق (offline)
- **النتيجة:** 5× تقليل في حوسبة وقت الاستدلال لنفس الدقة
- مع أسئلة متعددة عن نفس السياق: **2.5× تقليل تكلفة المتوسط**

#### 4. Falcon-H1R — توقف مبكر ذكي (يناير 2026)
**arXiv:2601.02346:**

- DeepConf: يُوقف التفكير مبكراً عندما يكون النموذج واثقاً
- **النتيجة:** 96.7% دقة على AIME25 مع **38% توكنات أقل** من DeepSeek-R1

### القواعد العملية

1. **لا تفترض أن "أصغر = أرخص"** — قِس تكلفة المهمة الناجحة (CPST) وليس تكلفة التوكن
2. **استخدم التوقف المبكر** — DeepConf/budget forcing يوفر 30-40%
3. **Sleep-time compute لأسئلة متكررة** — فكّر مسبقاً عن المستندات الثابتة
4. **Sparse Attention ضروري** — يُفتح المجال لتفكير أطول بتكلفة أقل

### المخاطر

1. **تكلفة غير متوقعة:** سلاسل التفكير قد تتفجر (o3: $3,000 لمهمة واحدة على ARC-AGI)
2. **Overthinking Tax:** النماذج الأصغر تُفرط في التفكير — قد تكون أغلى
3. **لا تعمل لكل مهمة:** المهام البسيطة لا تستفيد من التفكير الإضافي
4. **زمن الاستجابة:** التفكير الطويل = ثوانٍ-دقائق من الانتظار

---

## English Content

Inference-time compute (test-time scaling) allocates extra compute during inference — longer chain-of-thought, multiple samples, self-verification. Key economic finding: smaller models "overthink" and may cost 57% MORE than larger models per successful task (OckBench). Sleep-time compute can reduce test-time cost by 5× by "thinking" offline about contexts. Kinetics scaling law shows sparse attention is essential for cost-effective inference-time scaling.

---

## المصادر | Sources

1. **[Tier 2]** "OckBench: Measuring the Efficiency of LLM Reasoning", arXiv:2511.05722v2, 2025-2026. Overthinking Tax discovery.
2. **[Tier 2]** "Kinetics: Rethinking Test-Time Scaling Laws", arXiv:2506.05333, June 2025. Sparse attention for TTS.
3. **[Tier 2]** "Sleep-time Compute: Beyond Inference Scaling at Test-time", arXiv:2504.13171, April 2025. 5× reduction.
4. **[Tier 2]** "Falcon-H1R: Reasoning-Optimized 7B Model", arXiv:2601.02346, January 2026. DeepConf early stopping.
5. **[Tier 2]** Emerge.haus, "Test-Time Compute in Generative AI: An AI Atlas Report", April 2025. Comprehensive overview.
