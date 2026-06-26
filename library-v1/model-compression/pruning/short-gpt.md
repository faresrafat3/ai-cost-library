---
id: entry-shortgpt-001
title_ar: "ShortGPT — قصّ طبقات النماذج اللغوية الكبيرة"
title_en: "ShortGPT: Layer Pruning in Large Language Models"
type: emerging
status: emerging
category: model-compression
subcategory: pruning
tree_path: model-compression/pruning/short-gpt.md
cost_dimensions:
  - inference-cost
  - compute
  - memory
  - energy
proof_score: 2
sources_count: 3
created: 2026-06-26
last_reviewed: 2026-06-26
---

# ShortGPT — قصّ طبقات النماذج اللغوية الكبيرة

## العربية

### الملخص التنفيذي

**ShortGPT** — وهو منهج لقصّ الطبقات في النماذج اللغوية الكبيرة يعتمد على مقياس "أهمية الطبقة" (Block Importance أو BI) المشتق من إنتروبيا الاهتمام. الفكرة الأساسية: الطبقات في نماذج المحوّل زائدة عن الحاجة بشكل كبير، وإزالة الطبقات الأقل أهمية يحافظ على الأداء مع تقليل المعاملات والحوسبة.

### آلية العمل

1. حساب درجة أهمية (BI score) لكل طبقة بناءً على إنتروبيا آليات الاهتمام.
2. ترتيب الطبقات تنازلياً حسب الأهمية.
3. إزالة الطبقات ذات الدرجات الأقل حتى الوصول لنسبة قصّ مستهدفة.
4. النموذج المُقصَّر يعمل مباشرة بدون إعادة تدريب (zero-shot pruning).

### الأرقام الموثقة

| النموذج | نسبة القصّ | متوسط الاحتفاظ بالأداء | التسريع |
|---------|-----------|------------------------|---------|
| Llama-2-7B | ~25% | 85.10% | ~1.63× |
| Llama-2-13B | ~25% | 85.10% | ~1.63× |
| Llama-2-70B | ~30% | 91% | ~1.8× |

### حالة الأدلة

- **النموذج الأولي** ✅: ورقة بحثية (Men et al., 2024) مع كود متاح.
- **الاختبار** ✅: معايير قياسية (MMLU, CMMLU) مع أرقام مفصلة.
- **النشر الإنتاجي** ⏳: لا توجد تقارير رسمية عن نشر ShortGPT في إنتاج واسع.
- **التوفير المقاس** ✅: أرقام التسريع واضحة ومكررة في دراسات لاحقة (E3-Pruner).

### متى تستخدمه

- ضغط نماذج Llama/Baichuan للاستخدام المحلي
- البيئات ذات الموارد المحدودة (Edge deployment)
- عندما تكون البساطة أفضل من التعقيد (إزالة طبقات مباشرة)

### متى تتجنبه

- النماذج الحساسة جداً للدقة (تدهور 10-15% في المتوسط)
- المهام المعقدة التي تحتاج كل الطبقات (الاستدلال الرياضي العميق)
- البنى غير المحوّلة (Mamba, RWKV — ShortGPT صُمم للمحوّلات)

### القيود والمخاطر

- [⚠️ غير مُتحقق إنتاجياً] لا توجد تقارير نشر رسمية من شركات كبرى.
- تدهور الأداء يزداد مع نسبة القصّ (أكثر من 30% يسبب فقداناً كبيراً).
- لا يعمل بشكل جيد مع جميع البنى (الأفضل للمحوّلات المتجانسة).
- يتكامل مع التكميم (orthogonal to quantization) لكن التأثير المشترك غير مُختبر بشكل شامل.

### المصادر

[Tier 2] Men et al., "ShortGPT: Layers in Large Language Models are More Redundant Than You Expect", arXiv:2403.03853, 2024  
[Tier 2] "E3-Pruner: Towards Efficient, Economical, and Effective Layer Pruning for LLMs", arXiv:2511.17205, 2025  
[Tier 3] MarkTechPost, "ShortGPT: Novel AI Approach to Pruning LLMs", March 2024

---

## English

### Executive Summary

**ShortGPT** — A layer pruning approach for LLMs based on "Block Importance" (BI) scores derived from attention entropy. Core idea: transformer layers are highly redundant, and removing less important layers preserves performance while reducing parameters and compute.

### Mechanism

1. Compute BI score for each layer based on attention mechanism entropy.
2. Rank layers in descending order of importance.
3. Remove lowest-scoring layers until target pruning ratio is reached.
4. The pruned model runs directly without retraining (zero-shot pruning).

### Documented Numbers

| Model | Pruning Ratio | Avg. Performance Retained | Speedup |
|-------|--------------|--------------------------|---------|
| Llama-2-7B | ~25% | 85.10% | ~1.63× |
| Llama-2-13B | ~25% | 85.10% | ~1.63× |
| Llama-2-70B | ~30% | 91% | ~1.8× |

### Evidence Status

- **Prototype** ✅: Research paper (Men et al., 2024) with available code.
- **Testing** ✅: Standard benchmarks (MMLU, CMMLU) with detailed numbers.
- **Production Deployment** ⏳: No official deployment reports from major companies.
- **Measured Savings** ✅: Speedup numbers clear and replicated in subsequent studies (E3-Pruner).

### When to Use

- Compressing Llama/Baichuan models for local use
- Resource-constrained environments (edge deployment)
- When simplicity beats complexity (direct layer removal)

### When to Avoid

- Accuracy-sensitive models (10-15% average degradation)
- Complex tasks requiring all layers (deep mathematical reasoning)
- Non-transformer architectures (Mamba, RWKV — ShortGPT designed for transformers)

### Limitations and Risks

- [⚠️ Not production-verified] No official deployment reports from major companies.
- Performance degradation increases with pruning ratio (>30% causes significant loss).
- Doesn't work well with all architectures (best for homogeneous transformers).
- Orthogonal to quantization but combined effect not comprehensively tested.

### Sources

[Tier 2] Men et al., "ShortGPT: Layers in Large Language Models are More Redundant Than You Expect", arXiv:2403.03853, 2024  
[Tier 2] "E3-Pruner: Towards Efficient, Economical, and Effective Layer Pruning for LLMs", arXiv:2511.17205, 2025  
[Tier 3] MarkTechPost, "ShortGPT: Novel AI Approach to Pruning LLMs", March 2024
