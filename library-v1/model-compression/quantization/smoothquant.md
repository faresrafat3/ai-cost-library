---
id: "entry-smoothquant-001"
title_ar: "التكمية الملساء (SmoothQuant)"
title_en: "SmoothQuant"
type: "Practical"
status: "Deployed"
category: "Model Compression"
subcategory: "Quantization"
tree_path: ["Model Compression", "Quantization", "SmoothQuant"]
cost_dimensions: ["memory", "inference-cost", "latency"]
proof_score: 4
sources_count: 3
---

# التكمية الملساء | SmoothQuant

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary

التكمية الملساء (SmoothQuant) هي تقنية تكمية بعد التدريب (PTQ) تُحوّل أوزان النماذج اللغوية الكبيرة وتنشيطاتها إلى دقة 8 بت (W8A8) مع الحفاظ على الدقة الأصلية. تعتمد الفكرة على معالجة القيم الشاذة (Outliers) في التنشيطات التي تُصعّب التكمية: يتم "تنعيم" هذه القيم عبر معامل تناسبي يُطبّق على القنوات، ثم تُنقل الصعوبة إلى الأوزان التي تتحملها بسهولة. النتيجة هي تمكين التكمية الكاملة على مستوى العتاد دون فقدان ملحوظ في الدقة.

أظهرت النتائج أن SmoothQuant يحافظ على دقة 71.1% على نموذج OPT-175B مقارنة بـ 71.6% في دقة FP16، مع تقليل متطلبات الذاكرة إلى النصف (من 16 وحدة GPU إلى 8 وحدات) دون تغيير الكمون.

## 📌 English Summary

SmoothQuant is a post-training quantization (PTQ) method that compresses both weights and activations of LLMs to INT8 (W8A8) with negligible accuracy loss. The core insight addresses the fundamental challenge of activation outliers in Transformers — a few features can be 100× larger than average, destroying quantization quality.

SmoothQuant mathematically "smooths" these outliers by applying per-channel scaling factors, transferring the quantization difficulty from activations (hard to quantize) to weights (easier to quantize). This enables efficient INT8 matrix multiplication across entire layers without mixed-precision overhead.

Experimental results show SmoothQuant maintains 71.1% accuracy on OPT-175B vs 71.6% FP16, while halving GPU requirements (16→8 A100s) at nearly identical latency.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected

- **تكلفة الذاكرة (Memory Cost):** تقليل الذاكرة بمقدار 2× (INT8 vs FP16). نموذج MT-NLG 530B يعمل على عقدة واحدة (8× A100 80GB) بدلاً من عقدتين.
- **الكمون (Latency):** مماثل لـ FP16 — 1689ms مقابل 1707ms لطول تسلسل 1024 (فرق <1%).
- **تكلفة الاستدلال (Inference Cost):** تحسين بنسبة تصل إلى 1.45× في الإنتاجية عبر الاستفادة الكاملة من وحدات Tensor Cores التي تدعم INT8.

## 🛡️ بوابات الأدلة | Evidence Gates

- ✅ **Gate 1 (Built):** كود مفتوح المصدر (mit-han-lab/smoothquant) مع دعم Llama-2/3, Falcon, Mistral, Mixtral.
- ✅ **Gate 2 (Tested):** مُختبر على 7 معايير صفرية + WikiText perplexity.
- ✅ **Gate 3 (Deployed):** مُدمج في FasterTransformer و PyTorch، ومستخدَم في نشر نماذج 175B+.
- ✅ **Gate 4 (Saved):** 2× توفير في الذاكرة مع ≤0.5% فقدان دقة على نماذج حتى 530B.

## ⚠️ القيود والمخاطر | Limitations & Risks

- يتطلب مجموعة معايرة (~512 جملة) لحساب معاملات التنعيم.
- الدقة تنخفض عند التكمية إلى 4 بت (W4A4): من 65.26% إلى 38.41% على LLaMA-1-7B.
- SmoothQuant+ (الامتداد 4 بت) يعالج المشكلة لكنه يتطلب أنوية CUDA مخصصة.
- لا يحل مشكلة استهلاك KV Cache.

## 📚 المصادر | Sources

- [1] Xiao et al., "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models", ICML, 2023. DOI: [arXiv:2211.10438](https://arxiv.org/abs/2211.10438)
- [2] Pan et al., "SmoothQuant+: Accurate and Efficient 4-bit Post-Training Quantization", arXiv, 2023. DOI: [arXiv:2312.03788](https://arxiv.org/abs/2312.03788)
- [3] Intel Analytics, "Enhanced SmoothQuant Approach for LLMs", 2023. [URL](https://medium.com/intel-analytics-software/effective-post-training-quantization-for-large-language-models-with-enhanced-smoothquant-approach-93e9d104fb98)

## 🔗 إدخالات ذات صلة | Related Entries

- [GPTQ](./gptq.md)
- [AWQ](./awq.md)
- [LLM.int8()](./llm-int8.md)
