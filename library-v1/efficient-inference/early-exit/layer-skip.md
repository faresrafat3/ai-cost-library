---
id: entry-layerskip-001
title_ar: "LayerSkip — قفز الطبقات مع فك الترميز التخميني الذاتي"
title_en: "LayerSkip: Self-Speculative Decoding with Layer Skipping"
type: practical
status: validated
category: efficient-inference
subcategory: early-exit
tree_path: efficient-inference/early-exit/layer-skip.md
cost_dimensions:
  - inference-cost
  - latency
  - compute
  - energy
proof_score: 3
sources_count: 3
created: 2026-06-26
last_reviewed: 2026-06-26
---

# LayerSkip — قفز الطبقات مع فك الترميز التخميني الذاتي

## العربية

### الملخص التنفيذي

**LayerSkip** هو حل متكامل من Meta AI (FAIR) يجمع بين تسريب الطبقات أثناء التدريب (layer dropout) وفك الترميز التخميني الذاتي (self-speculative decoding) لتسريع استدلال نماذج اللغات الكبيرة. بدلاً من استخدام نموذج مسودة منفصل، يستفيد LayerSkip من الطبقات الأولى للنموذج نفسه لتوليد رموز مسودة، ثم يتحقق منها باستخدام الطبقات المتبقية.

### آلية العمل

1. **وصفة التدريب**: يُطبَّق تسريب طبقات بمعدلات منخفضة للطبقات الأولى ومرتفعة للأخيرة، مع خسارة إنهاء مبكر مشتركة بين جميع الطبقات.
2. **استراتيجية الاستدلال**: الخروج المبكر عند الطبقات الأولى لتقليل التكلفة الحسابية دون المساس بالدقة.
3. **فك الترميز التخميني الذاتي**: التنبؤات تُنتَج عند الطبقات المبكرة، ثم تُتحقَّق وتُصحَّح بالطبقات المتبقية من نفس النموذج.

### الأرقام الموثقة

| المهمة | النموذج | التسريع | المصدر |
|--------|--------|---------|--------|
| التلخيص (CNN/DM) | Llama 2-7B | 2.16× | ACL 2024 |
| الترميز | CodeLlama | 1.82× | ACL 2024 |
| التحليل الدلالي (TOPv2) | Llama 2-7B | 2.0× | ACL 2024 |
| تقليل البصصة الذاكرية | — | 15-25% | مقارنة مع SD التقليدي |

### بوابات الأدلة

- **Gate 1 (مبني)** ✅: كود مفتوح المصدر على GitHub: `facebookresearch/LayerSkip` ونماذج على HuggingFace.
- **Gate 2 (مختبر)** ✅: معايير ACL 2024 (Elhoushi et al.) مع أرقام تسريع محددة.
- **Gate 3 (منشور)** ✅: نماذج LayerSkip متاحة للاستخدام عبر HuggingFace مع 6 نقاط تفتيش.
- **Gate 4 (توفير)** ✅: تسريع حتى 2.16× مع الحفاظ على الدقة.

### متى تستخدمه

- نماذج Llama مُدرَّبة مسبقاً وتحتاج تسريع استدلال
- بيئات ذات ذاكرة GPU محدودة (لا يحتاج نموذج مسودة منفصل)
- مهام توليد نصوص مع أنماط متوقعة

### متى تتجنبه

- النماذج غير المُدرَّبة بطريقة LayerSkip (لن تعمل بشكل فعال)
- المهام التي تتطلب دقة قصوى بدون أي تنازل
- البنى غير المحوّلة (non-Transformer)

### القيود والمخاطر

- [⚠️ محدود التحقق] الأرقام محصورة بنماذج Llama المدربة بوصفة LayerSkip.
- يحتاج إعادة تدريب أو تدريب مستمر (continual pretraining).
- الأداء حساس لاختيار طبقة الخروج (exit_layer) وطول التخمين (num_speculations).
- لا يعمل بشكل جيد مع جميع المهام (الاستفادة تختلف حسب نوع المهمة).

### المصادر

[Tier 1] Elhoushi et al., "LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding", ACL 2024, DOI: 10.18653/v1/2024.acl-long.681  
[Tier 2] Meta FAIR, "LayerSkip GitHub Repository", https://github.com/facebookresearch/LayerSkip  
[Tier 2] Meta, "LayerSkip HuggingFace Collection", https://huggingface.co/collections/facebook/layerskip-666b25c50c8ae90e1965727a

---

## English

### Executive Summary

**LayerSkip** is an end-to-end solution from Meta AI (FAIR) combining layer dropout during training with self-speculative decoding to accelerate LLM inference. Instead of using a separate draft model, LayerSkip leverages the model's own early layers to generate draft tokens, then verifies them with the remaining layers.

### Mechanism

1. **Training Recipe**: Layer dropout with low rates for early layers and higher rates for later ones, plus a shared early-exit loss across all transformer layers.
2. **Inference Strategy**: Early exit at shallower layers to reduce compute without sacrificing accuracy.
3. **Self-Speculative Decoding**: Predictions are generated at early layers, then verified and corrected by the remaining layers of the same model.

### Documented Numbers

| Task | Model | Speedup | Source |
|------|-------|---------|--------|
| Summarization (CNN/DM) | Llama 2-7B | 2.16× | ACL 2024 |
| Coding | CodeLlama | 1.82× | ACL 2024 |
| Semantic Parsing (TOPv2) | Llama 2-7B | 2.0× | ACL 2024 |
| Memory footprint reduction | — | 15-25% | vs. traditional SD |

### Evidence Gates

- **Gate 1 (Built)** ✅: Open-source code at `facebookresearch/LayerSkip` + HuggingFace models.
- **Gate 2 (Tested)** ✅: ACL 2024 benchmarks (Elhoushi et al.) with specific speedup numbers.
- **Gate 3 (Deployed)** ✅: 6 LayerSkip checkpoints available on HuggingFace for public use.
- **Gate 4 (Saved)** ✅: Up to 2.16× speedup while maintaining accuracy.

### When to Use

- Pre-trained Llama models needing inference acceleration
- GPU-constrained environments (no separate draft model needed)
- Text generation tasks with predictable patterns

### When to Avoid

- Models not trained with the LayerSkip recipe (won't work effectively)
- Tasks requiring maximum accuracy with zero compromise
- Non-Transformer architectures

### Limitations and Risks

- [⚠️ Limited verification] Numbers are specific to Llama models trained with LayerSkip recipe.
- Requires retraining or continual pretraining.
- Performance is sensitive to exit_layer and num_speculations hyperparameters.
- Does not work well for all tasks (benefit varies by task type).

### Sources

[Tier 1] Elhoushi et al., "LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding", ACL 2024, DOI: 10.18653/v1/2024.acl-long.681  
[Tier 2] Meta FAIR, "LayerSkip GitHub Repository", https://github.com/facebookresearch/LayerSkip  
[Tier 2] Meta, "LayerSkip HuggingFace Collection", https://huggingface.co/collections/facebook/layerskip-666b25c50c8ae90e1965727a
