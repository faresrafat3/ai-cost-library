---
id: entry-flashattn-001
title_ar: "FlashAttention — الانتباه المُحسَّن للذاكرة"
title_en: "FlashAttention: I/O-Aware Exact Attention"
type: practical
status: production-proven
category: efficient-inference
subcategory: kv-cache
tree_path: efficient-inference/kv-cache/flash-attention.md
cost_dimensions:
  - training-cost
  - inference-cost
  - memory
  - compute
  - energy
proof_score: 4
sources_count: 5
created: 2026-06-26
last_reviewed: 2026-06-26
---

# FlashAttention — الانتباه المُحسَّن للذاكرة

## العربية

### الملخص التنفيذي

**FlashAttention** — وهي عائلة من خوارزميات الانتباه المُدركة لدخول/خروج الذاكرة (I/O-aware) التي طوّرها Tri Dao وزملاؤه في جامعة ستانفورد. الفكرة الأساسية: بدلاً من حساب مصفوفة الانتباه الكاملة (O(N²)) وتخزينها في الذاكرة الرئيسية (HBM)، تُقسَّم العملية إلى بلاطات صغيرة (tiling) وتُنفَّذ على الذاكرة السريعة داخل الشريحة (SRAM/Registers) دون كتابة وسطاء. هذا يُقلل حركة البيانات بين الذاكرة والحساب بشكل جذري.

### تطور الإصدارات

| الإصدار | السنة | التحسين الرئيسي | الأداء |
|---------|-------|-----------------|--------|
| FlashAttention-1 | 2022 | تذكّر واعٍ للذاكرة (tiling + on-chip buffering) | 2-4× أسرع، 10-20× أقل ذاكرة |
| FlashAttention-2 | 2023 | توازي أفضل + دعم MQA/GQA | ~2× أسرع من v1، 50-73% استخدام A100 |
| FlashAttention-3 | 2024 | عدم تزامن Tensor Cores + FP8 | 740 TFLOPs/s على H100 (75-85%) |
| FlashAttention-4 | 2026 | MMA غير متزامن بالكامل + بلاطات أكبر | 1613 TFLOPs/s على B200 BF16 (71%) |

### الأرقام الموثقة

1. **التدريب**: تخفيض 30% في وقت تدريب Llama-2-7B مع نفس الدقة.
2. **الذاكرة**: تخفيض 40-50% في استهلاك الذاكرة (1,200 MB vs 2,400 MB).
3. **سياق أطول**: 2× سياق أطول على نفس العتاد (4096 vs 2048 رموز في اختبارات محددة).
4. **توليد GPT-3**: تخفيض وقت تدريب GPT-3-175B من 60,544 ساعة GPU إلى 21,132 (A100) أو 10,100 (H100) — تخفيض ~83% و~90% على التوالي.

### بوابات الأدلة

- **Gate 1 (مبني)** ✅: مكتبة مفتوحة المصدر `Dao-AILab/flash-attention` على GitHub، مدمجة في PyTorch 2.2+ وHuggingFace Transformers.
- **Gate 2 (مختبر)** ✅: معايير MLPerf Inference v4.1، NeurIPS 2024 spotlight، أرقام Lambda Cloud المُوثقة.
- **Gate 3 (منشور)** ✅: مُستخدَم في vLLM، TensorRT-LLM، Megatron-LM، HuggingFace — كل البنى التحتية الرئيسية.
- **Gate 4 (توفير)** ✅: 30% تخفيض وقت تدريب، 50% تخفيض ذاكرة، 90% تخفيض تكلفة تدريب GPT-3 (تقديري).

### متى تستخدمه

- تدريب نماذج Transformer (إلزامي تقريباً في 2024+)
- استدلال بسياق طويل (>4K tokens)
- بيئات H100/B200 (FlashAttention-3/4)
- أي نظام إنتاج يستخدم vLLM أو TensorRT-LLM (مدمج تلقائياً)

### متى تتجنبه

- الأجهزة القديمة جداً (قبل Ampere A100) — استخدم FA-1 أو SDPA
- عندما تحتاج دقة FP32 كاملة (FA-3/4 تستخدم FP8/BF16)
- نماذج غير Transformer (Mamba, RWKV)

### القيود والمخاطر

- [✅ موثق] FP8 في FA-3 يحافظ على دقة أعلى (2.6× أقل خطأ رقمي من baseline FP8).
- يعتمد على بنية GPU محددة (Hopper لـFA-3, Blackwell لـFA-4).
- الأبعاد الكبيرة جداً للرأس (>256) قد تقلل الكفاءة.
- يحتاج CUDA ≥ 12.3 لـ FlashAttention-3.

### المصادر

[Tier 1] Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", NeurIPS 2022  
[Tier 1] Dao et al., "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning", ICLR 2024  
[Tier 1] Shah et al., "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision", NeurIPS 2024 (Spotlight)  
[Tier 2] Lambda Cloud, "How FlashAttention-2 Accelerates LLMs on NVIDIA H100 and A100 GPUs", https://lambda.ai/blog/flashattention-2-lambda-cloud-h100-vs-a100  
[Tier 1] MLCommons, "MLPerf Inference v4.1 Benchmarks", 2024

---

## English

### Executive Summary

**FlashAttention** — A family of I/O-aware exact attention algorithms developed by Tri Dao and colleagues at Stanford. Core idea: instead of computing the full attention matrix (O(N²)) and storing it in HBM, operations are tiled and executed on fast on-chip SRAM/Registers without materializing intermediates. This dramatically reduces data movement between memory and compute.

### Version Evolution

| Version | Year | Key Improvement | Performance |
|---------|------|-----------------|-------------|
| FlashAttention-1 | 2022 | IO-aware tiling + on-chip buffering | 2-4× faster, 10-20× less memory |
| FlashAttention-2 | 2023 | Better parallelism + MQA/GQA support | ~2× faster than v1, 50-73% A100 utilization |
| FlashAttention-3 | 2024 | Tensor Core asynchrony + FP8 | 740 TFLOPs/s on H100 (75-85%) |
| FlashAttention-4 | 2026 | Fully async MMA + larger tiles | 1613 TFLOPs/s on B200 BF16 (71%) |

### Documented Numbers

1. **Training**: 30% reduction in Llama-2-7B training time with same accuracy.
2. **Memory**: 40-50% memory reduction (1,200 MB vs 2,400 MB).
3. **Longer Context**: 2× longer context on same hardware (4096 vs 2048 tokens in specific tests).
4. **GPT-3 Training**: Reduced GPT-3-175B training time from 60,544 GPU hours to 21,132 (A100) or 10,100 (H100) — ~83% and ~90% reduction respectively.

### Evidence Gates

- **Gate 1 (Built)** ✅: Open-source `Dao-AILab/flash-attention` on GitHub, integrated into PyTorch 2.2+ and HuggingFace Transformers.
- **Gate 2 (Tested)** ✅: MLPerf Inference v4.1, NeurIPS 2024 spotlight, Lambda Cloud benchmarks.
- **Gate 3 (Deployed)** ✅: Used in vLLM, TensorRT-LLM, Megatron-LM, HuggingFace — all major infrastructures.
- **Gate 4 (Saved)** ✅: 30% training time reduction, 50% memory reduction, ~90% GPT-3 training cost reduction (estimated).

### When to Use

- Training Transformer models (virtually mandatory in 2024+)
- Long-context inference (>4K tokens)
- H100/B200 environments (FlashAttention-3/4)
- Any production system using vLLM or TensorRT-LLM (auto-integrated)

### When to Avoid

- Very old hardware (pre-Ampere A100) — use FA-1 or SDPA
- When full FP32 precision is required (FA-3/4 uses FP8/BF16)
- Non-Transformer models (Mamba, RWKV)

### Limitations and Risks

- [✅ Well-documented] FP8 in FA-3 maintains higher accuracy (2.6× lower numerical error than baseline FP8).
- Depends on specific GPU architecture (Hopper for FA-3, Blackwell for FA-4).
- Very large head dimensions (>256) may reduce efficiency.
- Requires CUDA ≥ 12.3 for FlashAttention-3.

### Sources

[Tier 1] Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", NeurIPS 2022  
[Tier 1] Dao et al., "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning", ICLR 2024  
[Tier 1] Shah et al., "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision", NeurIPS 2024 (Spotlight)  
[Tier 2] Lambda Cloud, "How FlashAttention-2 Accelerates LLMs on NVIDIA H100 and A100 GPUs", https://lambda.ai/blog/flashattention-2-lambda-cloud-h100-vs-a100  
[Tier 1] MLCommons, "MLPerf Inference v4.1 Benchmarks", 2024
