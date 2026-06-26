---
id: entry-mod-001
title_ar: "Mixture-of-Depths — خلط الأعماق"
title_en: "Mixture-of-Depths: Dynamically Allocating Compute in Transformers"
type: emerging
status: emerging
category: efficient-training
subcategory: compute-allocation
tree_path: efficient-training/compute-allocation/mixture-of-depths.md
cost_dimensions:
  - training-cost
  - inference-cost
  - compute
  - energy
proof_score: 2
sources_count: 3
created: 2026-06-26
last_reviewed: 2026-06-26
---

# Mixture-of-Depths — خلط الأعماق

## العربية

### الملخص التنفيذي

**Mixture-of-Depths (MoD)** — وهو نهج ديناميكي لتخصيص الحوسبة في نماذج المحوّل (Transformer) يسمح للنموذج بتحديد أي الرموز (tokens) تحتاج إلى معالجة كاملة عبر الطبقات وأيها يمكنها تخطي الطبقات بتوصيلة متبقية (skip connection) ذات تكلفة صفرية. ينفّذ MoD موجِّهًا (router) من طبقة واحدة يختار أفضل-k رمزًا للمعالجة الكاملة، مع ميزانية حوسبة ثابتة.

### آلية العمل

1. في كل طبقة، يُقيّم موجِّه (router) أهمية كل رمز.
2. يختار أفضل-k رمزًا (أو نسبة B من الرموز) للمعالجة الكاملة.
3. الرموز غير المختارة تتخطى الطبقة عبر توصيلة متبقية مباشرة.
4. الميزانية k ثابتة → رسم حسابي ثابت مع هويات رموز متغيرة.
5. التدريب يتم بنهاية إلى نهاية (end-to-end) مع مُقدِّر تدرج (gradient estimator).

### الأرقام الموثقة

| المعيار | النتيجة | المصدر |
|---------|---------|--------|
| خسارة مكافئة (iso-FLOP) | MoD يطابق النماذج الأساسية | arXiv:2404.02258 |
| تسريع أخذ العينات | حتى ≈50% | arXiv:2404.02258 |
| تقليل FLOPs | أقل FLOPs لكل تمرير أمامي | Graphcore Research |

### حالة الأدلة

- **النموذج الأولي** ✅: ورقة بحثية من DeepMind (Raposo et al., أبريل 2024) مع تنفيذ غير رسمي متاح.
- **الاختبار** ✅: معايير iso-FLOP تُظهر تطابق الخسارة مع تقليل FLOPs.
- **النشر الإنتاجي** ⏳: لا توجد تقارير هندسية رسمية عن نشر MoD في إنتاج واسع النطاق حتى الآن.
- **التوفير المقاس** ⏳: أرقام التسريع من الورقة فقط، دون تقارير نشر مستقلة.

### متى تفكر فيه

- تدريب نماذج جديدة من الصفر مع قيود حوسبة
- بيئات بحثية تريد استكشاف التخصيص الديناميكي للحوسبة
- حالات تكون فيها تكلفة التدريب أعلى من تكلفة الاستدلال

### متى تتجنبه

- النماذج المدربة مسبقاً (يتطلب تدريب من الصفر)
- البيئات الإنتاجية التي تحتاج استقراراً مطلقاً
- الحالات التي تكون فيها البساطة أفضل من التعقيد

### القيود والمخاطر

- [⚠️ غير مُتحقق إنتاجياً] لا توجد تقارير نشر رسمية من شركات كبرى.
- يحتاج تعديل بنية التدريب بشكل جذري.
- تنفيذات المجتمع غير رسمية ولم تخضع لمراجعة أقران مستقلة.
- التوافق مع الأجهزة المحدودة (edge devices) غير مُختبر.
- الرسم البياني الثابت قد لا يستفيد من التباين الديناميكي الكامل.

### الأدوات والتنفيذات

- [⚠️ غير رسمي] تنفيذات مجتمعية على GitHub (kyegomez, astramind)
- لا توجد حزم PyPI رسمية حتى الآن

### المصادر

[Tier 2] Raposo et al., "Mixture-of-Depths: Dynamically allocating compute in transformer-based language models", arXiv:2404.02258, 2024  
[Tier 3] Graphcore Research, "TriForce, QuaRot, Mixture-of-Depths: Papers of the Month (Apr 2024)", https://www.graphcore.ai/posts/triforce-quarot-mixture-of-depths-papers-of-the-month-apr-2024  
[Tier 3] Community implementations, GitHub repositories (unofficial)

---

## English

### Executive Summary

**Mixture-of-Depths (MoD)** — A dynamic compute allocation approach for Transformer models that allows the model to decide which tokens need full processing through layers and which can skip layers via zero-cost skip connections. MoD implements a per-layer router that selects the top-k tokens for full processing, with a fixed compute budget.

### Mechanism

1. At each layer, a router evaluates the importance of each token.
2. Top-k tokens (or fraction B) are selected for full processing.
3. Unselected tokens bypass the layer via a direct skip connection.
4. Fixed budget k → static computational graph with varying token identities.
5. Training is end-to-end with a gradient estimator.

### Documented Numbers

| Metric | Result | Source |
|--------|--------|--------|
| Iso-FLOP parity | MoD matches vanilla baselines | arXiv:2404.02258 |
| Sampling speedup | Up to ≈50% | arXiv:2404.02258 |
| FLOPs reduction | Lower FLOPs per forward pass | Graphcore Research |

### Evidence Status

- **Prototype** ✅: Research paper from DeepMind (Raposo et al., April 2024) with unofficial implementations available.
- **Testing** ✅: Iso-FLOP benchmarks show matching loss with reduced FLOPs.
- **Production Deployment** ⏳: No official engineering reports of MoD deployed at production scale.
- **Measured Savings** ⏳: Speedup numbers from paper only, no independent deployment reports.

### When to Consider

- Training new models from scratch with compute constraints
- Research environments exploring dynamic compute allocation
- Scenarios where training cost dominates inference cost

### When to Avoid

- Already pre-trained models (requires training from scratch)
- Production environments needing absolute stability
- Cases where simplicity trumps complexity

### Limitations and Risks

- [⚠️ Not production-verified] No official deployment reports from major companies.
- Requires fundamental modification of training architecture.
- Community implementations are unofficial and lack independent peer review.
- Compatibility with edge/constrained hardware is untested.
- Static graph may not leverage full dynamic variance.

### Tools and Implementations

- [⚠️ Unofficial] Community implementations on GitHub (kyegomez, astramind)
- No official PyPI packages yet

### Sources

[Tier 2] Raposo et al., "Mixture-of-Depths: Dynamically allocating compute in transformer-based language models", arXiv:2404.02258, 2024  
[Tier 3] Graphcore Research, "TriForce, QuaRot, Mixture-of-Depths: Papers of the Month (Apr 2024)", https://www.graphcore.ai/posts/triforce-quarot-mixture-of-depths-papers-of-the-month-apr-2024  
[Tier 3] Community implementations, GitHub repositories (unofficial)
