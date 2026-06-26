---
id: entry-distillation-001
title_ar: "استخلاص المعرفة — من DistilBERT إلى DeepSeek-R1"
title_en: "Knowledge Distillation — From DistilBERT to DeepSeek-R1"
type: practical
status: production-proven
category: model-compression
subcategory: distillation
tree_path: model-compression/distillation/distillation.md
cost_dimensions:
  - training-cost
  - inference-cost
  - compute
  - memory
  - energy
proof_score: 4
sources_count: 5
created: 2026-06-26
last_reviewed: 2026-06-26
---

# استخلاص المعرفة — من DistilBERT إلى DeepSeek-R1

## العربية

### الملخص التنفيذي

**استخلاص المعرفة (Knowledge Distillation)** هو عملية تدريب نموذج "طالب" أصغر على تقليد سلوك نموذج "معلّم" أكبر. المعلّم يولّد بيانات تدريب (soft targets أو سلاسل تفكير) والطالب يتعلم منها. النتيجة: نموذج أصغر بكثير بأسرع استدلال وأقل تكلفة تشغيل، مع الحفاظ على معظم قدرات المعلّم.

### التقنيات الرئيسية

| التقنية | المعلم → الطالب | الضغط | الاحتفاظ بالجودة |
|---------|----------------|-------|-------------------|
| DistilBERT (2019) | BERT → DistilBERT | 40% أصغر | 97% من GLUE |
| TinyBERT (2020) | BERT → TinyBERT-4 | 7.5× أصغر | 96.8% |
| MiniLLM (ICLR 2024) | GPT-2/LLaMA → 120M-13B | متنوعة | يتفوق على KL القياسي |
| NVIDIA Minitron (2024) | 15B → 8B/4B | قصّ+استخلاص | +16% MMLU vs. من الصفر |
| DeepSeek-R1 Distills (2025) | 671B → 1.5B-70B | 6 نماذج | 8B يطابق 235B MoE في الاستدلال |

### الأرقام الموثقة (حالات بارزة)

1. **DistilBERT**: 40% أصغر، 60% أسرع في الاستدلال، 97% من دقة BERT على GLUE. تدريب على 8 GPUs لمدة 90 ساعة (≈700 ساعة GPU) مقابل ≈24,000 ساعة لRoBERTa.

2. **DeepSeek-R1 Distills**:
   - R1-Distill-Qwen-8B يطابق Qwen3-235B-thinking في معايير الاستدلال
   - 60-70% تخفيض تكلفة الاستدلال مقارنة بنماذج 30B+
   - 20-40 رمز/ثانية على أجهزة استهلاكية (16GB VRAM)
   - متاحة على AWS Bedrock كنماذج مخصصة

3. **NVIDIA Minitron**: 1/40 من رموز التدريب مقارنة بالتدريب من الصفر، مع +16% MMLU.

### بوابات الأدلة

- **Gate 1 (مبني)** ✅: DistilBERT (HuggingFace), DeepSeek-R1 Distills (HuggingFace, Apache 2.0), Minitron (NVIDIA).
- **Gate 2 (مختبر)** ✅: معايير GLUE، MMLU، AIME، GPQA مع أرقام مفصلة.
- **Gate 3 (منشور)** ✅: DistilBERT في إنتاج واسع، DeepSeek-R1 Distills على Bedrock و Fireworks AI.
- **Gate 4 (توفير)** ✅: 18× تخفيض تكلفة (8B vs 405B), 60% أسرع استدلال.

### متى تستخدمه

- تقليل تكلفة الاستدلال مع الحفاظ على جودة مقبولة
- نماذج تحتاج نشر على أجهزة محدودة (edge, mobile)
- عندما يكون لديك نموذج معلم كبير متاح
- تدريب نماذج متخصصة بميزانية منخفضة

### متى تتجنبه

- عندما تحتاج أعلى دقة ممكنة (بدون أي تنازل)
- البيانات شديدة التخصص التي لا يغطيها المعلم
- النماذج التي تحتاج قدرات إبداعية غير موجودة في المعلم

### القيود والمخاطر

- الطالب يرث تحيزات المعلم وأخطاءه
- استخلاص سلاسل التفكير (CoT) قد لا ينقل القدرة على الاستدلال العام
- النماذج المُستخلصة (Distills) تفتقر للعموم مقارنة بالمعلم
- تكلفة استخلاص البيانات الأولية (teacher-generated data) قد تكون عالية لمجموعات بيانات ضخمة
- [✅ موثق جيداً] DistilBERT لا يدعم مهام التوليد (BERT مشفر فقط)

### المصادر

[Tier 1] Sanh et al., "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter", NeurIPS Workshop 2019, arXiv:1910.01108  
[Tier 2] Hinton et al., "Distilling the Knowledge in a Neural Network", NeurIPS 2015 Workshop  
[Tier 1] Gu et al., "MiniLLM: Knowledge Distillation of Large Language Models", ICLR 2024  
[Tier 2] NVIDIA, "Minitron: Pruning and Distillation for Efficient LLMs", 2024  
[Tier 1] DeepSeek AI, "DeepSeek-R1 Distilled Models", HuggingFace, January 2025  
[Tier 2] AWS, "Deploy DeepSeek-R1 distilled Llama models with Amazon Bedrock", February 2025  
[Tier 2] Federal Reserve Feds, "LLM on a Budget: Active Knowledge Distillation", December 2025

---

## English

### Executive Summary

**Knowledge Distillation** trains a smaller "student" model to mimic a larger "teacher" model's behavior. The teacher generates training data (soft targets or reasoning chains) and the student learns from it. Result: a much smaller model with faster inference and lower operating cost, while preserving most of the teacher's capabilities.

### Key Techniques

| Technique | Teacher → Student | Compression | Quality Retention |
|-----------|------------------|-------------|-------------------|
| DistilBERT (2019) | BERT → DistilBERT | 40% smaller | 97% of GLUE |
| TinyBERT (2020) | BERT → TinyBERT-4 | 7.5× smaller | 96.8% |
| MiniLLM (ICLR 2024) | GPT-2/LLaMA → 120M-13B | Varied | Outperforms standard KL |
| NVIDIA Minitron (2024) | 15B → 8B/4B | Pruning+distillation | +16% MMLU vs. from-scratch |
| DeepSeek-R1 Distills (2025) | 671B → 1.5B-70B | 6 models | 8B matches 235B MoE on reasoning |

### Documented Numbers (Notable Cases)

1. **DistilBERT**: 40% smaller, 60% faster inference, 97% BERT accuracy on GLUE. Trained on 8 GPUs for ~90 hours (≈700 GPU hours) vs. ~24,000 hours for RoBERTa.

2. **DeepSeek-R1 Distills**:
   - R1-Distill-Qwen-8B matches Qwen3-235B-thinking on reasoning benchmarks
   - 60-70% inference cost reduction vs. 30B+ models
   - 20-40 tokens/sec on consumer hardware (16GB VRAM)
   - Available on AWS Bedrock as custom models

3. **NVIDIA Minitron**: 1/40 training tokens vs. from-scratch, with +16% MMLU.

### Evidence Gates

- **Gate 1 (Built)** ✅: DistilBERT (HuggingFace), DeepSeek-R1 Distills (HuggingFace, Apache 2.0), Minitron (NVIDIA).
- **Gate 2 (Tested)** ✅: GLUE, MMLU, AIME, GPQA benchmarks with detailed numbers.
- **Gate 3 (Deployed)** ✅: DistilBERT in wide production, DeepSeek-R1 Distills on Bedrock and Fireworks AI.
- **Gate 4 (Saved)** ✅: 18× per-token cost reduction (8B vs 405B), 60% faster inference.

### When to Use

- Reducing inference cost with acceptable quality
- Models needing edge/mobile deployment
- When a large teacher model is available
- Training specialized models on a low budget

### When to Avoid

- When maximum accuracy is required (zero compromise)
- Highly specialized data not covered by the teacher
- Models needing creative capabilities not present in the teacher

### Limitations and Risks

- Student inherits teacher's biases and errors
- CoT distillation may not transfer general reasoning ability
- Distilled models lack general-purpose breadth compared to teachers
- Cost of generating teacher data can be high for large datasets
- [✅ Well-documented] DistilBERT does not support generation tasks (BERT is encoder-only)

### Sources

[Tier 1] Sanh et al., "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter", NeurIPS Workshop 2019, arXiv:1910.01108  
[Tier 2] Hinton et al., "Distilling the Knowledge in a Neural Network", NeurIPS 2015 Workshop  
[Tier 1] Gu et al., "MiniLLM: Knowledge Distillation of Large Language Models", ICLR 2024  
[Tier 2] NVIDIA, "Minitron: Pruning and Distillation for Efficient LLMs", 2024  
[Tier 1] DeepSeek AI, "DeepSeek-R1 Distilled Models", HuggingFace, January 2025  
[Tier 2] AWS, "Deploy DeepSeek-R1 distilled Llama models with Amazon Bedrock", February 2025  
[Tier 2] Federal Reserve Feds, "LLM on a Budget: Active Knowledge Distillation", December 2025
