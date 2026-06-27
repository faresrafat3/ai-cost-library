# التصنيف العادل متعدد المعايير | Fair Multi-Criteria Ranking
> إصدار خوارزمية: **v2.0 Calibrated MCDA** | تاريخ الإصدار: 2026-06-27 | عدد المداخل: **60** | المصدر: `data/entries.json`.

## لماذا v2؟

الإصدار الأول كان مفيدًا كبداية، لكنه كان **متفائلًا أكثر من اللازم**: درجات كثيرة فوق 90 أعطت انطباعًا خاطئًا أن المكتبة وصلت إلى إجابة نهائية أو أن التقنيات العليا تصلح لكل الحالات. لذلك يستخدم هذا الإصدار خوارزمية أعمق وأكثر محافظة: يعطي التقنية حقها إذا كانت ممتازة في سيناريو محدد، لكنه لا يسمح لها بالفوز عالميًا لمجرد أنها قوية في محور واحد.

## الخوارزمية

نُبقي المحاور التسعة المطلوبة، لكن نحسب درجتين: **المنفعة الخام** ثم **الدرجة المعايرة**. الدرجة المعايرة هي المستخدمة في الترتيب العام.

```text
Raw Utility = 10 × Σ(axis_score × axis_weight)
Confidence = (0.40E + 0.25M + 0.15T + 0.10P + 0.10G) / 10
Calibrated Score = Raw×0.88 + ExcellenceBonus - UncertaintyPenalty - RiskPenalty - ComplexityPenalty - ScopePenalty - MaturityPenalty
ثم تُطبَّق بوابات نضج: النظري والناشئ لا يتجاوزان سقفًا معينًا عالميًا، لكن يمكنهما الفوز في أقسام السيناريو.
```

### الأوزان الأساسية — لم تتغير

| الرمز | المحور | الوزن |
|---|---|---:|
| E | Evidence Strength / قوة الدليل | 20% |
| C | Cost Reduction Magnitude / مقدار الخفض | 25% |
| M | Maturity & Readiness / النضج | 15% |
| I | Ease of Implementation / السهولة | 10% |
| R | Risk & Limitations, inverse / المخاطر عكسيًا | 10% |
| G | Generalizability / التعميم | 5% |
| T | Community & Tooling / الأدوات | 5% |
| S | Sustainability / الاستدامة | 5% |
| P | Production Compatibility / توافق الإنتاج | 5% |

### طبقات المعايرة الجديدة

| الطبقة | الهدف | لماذا تمنع المبالغة؟ |
|---|---|---|
| خصم الثقة | يقلل الدرجة إذا كان الدليل/النضج/الأدوات أضعف | لا نساوي بين ورقة واعدة وتقنية في vLLM/PyTorch. |
| عقوبة المخاطر | تفصل الأثر عن قابلية الاعتماد | التكميم، MoE، التخزين الدلالي، والتوجيه لها مخاطر جودة/تعقيد. |
| عقوبة التعقيد | تعاقب التقنيات التي تحتاج إعادة هندسة أو عتادًا خاصًا | حتى لو وفرت كثيرًا، قد لا تكون اختيارًا عامًا. |
| عقوبة ضيق النطاق | تخفض التقنيات الخاصة بمهمة/نموذج/عتاد | تحفظ فرص التقنيات العامة في الترتيب العام. |
| بوابات النضج | سقف أعلى للنظري والناشئ في الترتيب العام | يمنع "بحث واعد" من تجاوز ممارسة إنتاجية مثبتة. |
| مكافأة تميز صغيرة | تعطي نقاطًا محدودة لميزة قوية جدًا | لا تغيّر العالم وحدها، لكنها تمنع دفن التقنيات المتخصصة. |

## جدول التصنيف العام المعاير

| الرتبة | ID | العنوان | الدرجة المعايرة | الخام | الثقة | شارات التميز | E | C | M | I | R | G | T | S | P |
|---:|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `entry-lora-001` | LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning<br><span dir="rtl">التكيف منخفض الرتبة — LoRA</span> | **86.1** | 95.5 | 0.98 | ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي | 10 | 10 | 10 | 9 | 9 | 9 | 10 | 7 | 9 |
| 2 | `entry-qlora-001` | QLoRA: Quantized Low-Rank Adaptation<br><span dir="rtl">الضبط الدقيق المُكمَّم — QLoRA</span> | **86.1** | 95.5 | 0.98 | ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي | 10 | 10 | 10 | 9 | 9 | 9 | 10 | 7 | 9 |
| 3 | `entry-pagedattention-001` | PagedAttention: Virtual Memory for KV Cache<br><span dir="rtl">الانتباه المُقسَّم للصفحات — PagedAttention</span> | **82.9** | 92.5 | 0.96 | خفض ذاكرة قوي | 9 | 9 | 10 | 8 | 10 | 10 | 10 | 8 | 10 |
| 4 | `entry-contbatching-001` | Continuous Batching: The Single Biggest Inference Lever<br><span dir="rtl">التجميع المستمر</span> | **82.8** | 93.0 | 0.92 | إنتاجية استدلال عالية، خفض API سريع التبني | 8 | 10 | 10 | 8 | 10 | 10 | 10 | 8 | 10 |
| 5 | `entry-mixedprec-001` | Mixed Precision Training: BF16 as Standard, FP8 as Frontier<br><span dir="rtl">التدريب بالدقة المختلطة (BF16/FP8)</span> | **82.5** | 91.5 | 1.00 | استدامة/طاقة | 10 | 8 | 10 | 8 | 9 | 10 | 10 | 9 | 10 |
| 6 | `entry-gptq-001` | GPTQ: Post-Training Quantization for GPUs<br><span dir="rtl">التكميم بعد التدريب — GPTQ</span> | **82.3** | 92.0 | 0.98 | خفض ذاكرة قوي | 10 | 9 | 10 | 8 | 9 | 8 | 10 | 7 | 10 |
| 7 | `entry-deepspeed-001` | Distributed Training: DeepSpeed ZeRO & PyTorch FSDP<br><span dir="rtl">التدريب الموزّع — DeepSpeed ZeRO و FSDP</span> | **81.8** | 90.5 | 0.99 | ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي | 10 | 9 | 10 | 6 | 9 | 9 | 10 | 7 | 10 |
| 8 | `entry-flashattn-001` | FlashAttention: I/O-Aware Exact Attention<br><span dir="rtl">FlashAttention — الانتباه المُحسَّن للذاكرة</span> | **81.7** | 91.5 | 1.00 | — | 10 | 8 | 10 | 8 | 10 | 10 | 10 | 7 | 10 |
| 9 | `entry-awq-001` | AWQ: Activation-Aware Weight Quantization<br><span dir="rtl">التكميم المُدرك للتفعيل — AWQ</span> | **80.1** | 90.0 | 0.94 | خفض ذاكرة قوي | 9 | 9 | 10 | 8 | 9 | 8 | 10 | 7 | 10 |
| 10 | `entry-batchapi-001` | Batch API + Structured Output: 50-80% API Cost Reduction<br><span dir="rtl">واجهة الدفعات وتحسين المخرجات — 50-80% تقليل تكلفة API</span> | **79.7** | 90.0 | 0.91 | خفض API سريع التبني | 8 | 9 | 10 | 9 | 10 | 9 | 10 | 6 | 10 |
| 11 | `entry-distillation-001` | Knowledge Distillation — From DistilBERT to DeepSeek-R1<br><span dir="rtl">استخلاص المعرفة — من DistilBERT إلى DeepSeek-R1</span> | **76.7** | 87.0 | 0.94 | — | 10 | 9 | 10 | 5 | 8 | 8 | 8 | 8 | 9 |
| 12 | `entry-promptcache-001` | Prompt/Prefix Caching: 90% Cost Reduction on Cached Portions<br><span dir="rtl">تخزين البادئات مؤقتاً</span> | **76.6** | 87.0 | 0.87 | خفض API سريع التبني | 7 | 9 | 10 | 9 | 9 | 9 | 10 | 6 | 10 |
| 13 | `entry-llmint8-001` | LLM.int8(): Mixed-Precision INT8 with Outlier Handling<br><span dir="rtl">التكميم الصحيح 8-بت مع معالجة القيم الشاذة — LLM.int8()</span> | **76.5** | 87.0 | 0.93 | — | 10 | 8 | 9 | 9 | 8 | 8 | 9 | 7 | 9 |
| 14 | `entry-qwen3-001` | Qwen3 Efficiency: Thinking/Non-Thinking Fusion & Budget Control<br><span dir="rtl">كفاءات Qwen3 — دمج التفكير واللا-تفكير في نموذج واحد</span> | **76.0** | 86.5 | 0.92 | — | 9 | 8 | 10 | 8 | 9 | 8 | 9 | 7 | 9 |
| 15 | `entry-gguf-001` | Local GGUF/llama.cpp Inference: Zero API Cost on Consumer Hardware<br><span dir="rtl">الاستدلال المحلي بـ GGUF — صفر تكلفة API</span> | **75.5** | 86.0 | 0.82 | خفض API سريع التبني، استدامة/طاقة | 7 | 9 | 10 | 10 | 8 | 6 | 10 | 9 | 8 |
| 16 | `entry-dsv4-001` | DeepSeek V4 Economics: The Cheapest Frontier Model (2026)<br><span dir="rtl">اقتصاديات DeepSeek V4 — أرخص نموذج حدودي في 2026</span> | **75.1** | 86.5 | 0.82 | إنتاجية استدلال عالية، خفض API سريع التبني | 7 | 10 | 10 | 8 | 8 | 8 | 8 | 8 | 9 |
| 17 | `entry-fp8-001` | FP8 Quantization<br><span dir="rtl">التكميم بدقة FP8</span> | **74.4** | 85.0 | 0.90 | — | 9 | 8 | 10 | 8 | 8 | 7 | 9 | 7 | 9 |
| 18 | `entry-routing-001` | Intelligent Model Routing (RouteLLM)<br><span dir="rtl">توجيه النماذج الذكي</span> | **73.6** | 84.5 | 0.84 | خفض API سريع التبني | 9 | 10 | 8 | 7 | 7 | 8 | 8 | 7 | 8 |
| 19 | `entry-llama4-001` | Llama 4 MoE Economics: 400B Knowledge at 17B Inference Cost<br><span dir="rtl">اقتصاديات Llama 4 — مثال عملي على قوة MoE المفتوحة</span> | **72.6** | 83.0 | 0.84 | خفض API سريع التبني، ميزة معمارية ضخمة لكن معقّدة | 7 | 9 | 10 | 7 | 8 | 8 | 9 | 7 | 9 |
| 20 | `entry-moe-001` | Mixture-of-Experts Economics: The Dominant Architecture of 2026<br><span dir="rtl">اقتصاديات مزيج الخبراء (MoE)</span> | **71.5** | 84.5 | 0.91 | ضبط/تدريب منخفض التكلفة | 10 | 10 | 10 | 3 | 6 | 7 | 7 | 8 | 9 |
| 21 | `entry-merging-001` | Model Merging: Zero-Cost Multi-Task Combination (TIES, DARE, Model Soup)<br><span dir="rtl">دمج النماذج — بديل رخيص للتدريب المتعدد المهام</span> | **70.6** | 81.5 | 0.81 | ضبط/تدريب منخفض التكلفة | 9 | 9 | 7 | 8 | 8 | 7 | 9 | 6 | 7 |
| 22 | `entry-eagle3-001` | EAGLE-3: State-of-the-Art Speculative Decoding<br><span dir="rtl">فك الترميز التخميني EAGLE-3</span> | **69.9** | 80.5 | 0.82 | إنتاجية استدلال عالية | 8 | 9 | 8 | 7 | 7 | 8 | 9 | 7 | 8 |
| 23 | `entry-synthdata-001` | Synthetic Data for Cost-Efficient Training & Distillation<br><span dir="rtl">البيانات الاصطناعية لتقليل تكلفة التدريب</span> | **68.5** | 79.5 | 0.81 | ضبط/تدريب منخفض التكلفة | 8 | 9 | 9 | 6 | 7 | 8 | 7 | 6 | 8 |
| 24 | `entry-gpuecon-001` | GPU Inference Economics 2026: H100 vs B200 vs H200 Cost-per-Token<br><span dir="rtl">اقتصاديات GPU للاستدلال — مقارنة H100 vs B200 vs H200 (2026)</span> | **66.5** | 77.5 | 0.78 | إنتاجية استدلال عالية، استدامة/طاقة | 7 | 9 | 9 | 4 | 7 | 8 | 7 | 9 | 9 |
| 25 | `entry-multilora-001` | Multi-LoRA Serving: Hundreds of Fine-Tuned Models on One GPU<br><span dir="rtl">خدمة LoRA متعددة المستأجرين — مئات النماذج على GPU واحد</span> | **65.2** | 77.0 | 0.79 | — | 8 | 8 | 8 | 6 | 8 | 7 | 8 | 7 | 8 |
| 26 | `entry-radixattention-001` | RadixAttention: Prefix Sharing via Radix Tree KV Cache<br><span dir="rtl">شجرة الانتباه المتفرعة — RadixAttention (SGLang)</span> | **64.1** | 76.0 | 0.77 | — | 8 | 8 | 8 | 7 | 7 | 6 | 7 | 7 | 8 |
| 27 | `entry-smoothquant-001` | SmoothQuant: Smooth Activations for INT8 Quantization<br><span dir="rtl">التكميم الأملس — SmoothQuant</span> | **64.1** | 75.0 | 0.81 | — | 9 | 7 | 8 | 6 | 7 | 7 | 7 | 7 | 8 |
| 28 | `entry-semcache-001` | Semantic Caching<br><span dir="rtl">التخزين المؤقت الدلالي</span> | **61.3** | 74.5 | 0.74 | — | 7 | 9 | 8 | 6 | 6 | 7 | 7 | 6 | 8 |
| 29 | `entry-specdec-001` | Speculative Decoding: Draft-then-Verify for Faster Inference<br><span dir="rtl">فك الترميز التخميني</span> | **59.8** | 72.0 | 0.80 | — | 9 | 7 | 8 | 5 | 6 | 7 | 7 | 6 | 7 |
| 30 | `entry-breakeven-001` | Self-Host vs API: The Break-Even Analysis (2026)<br><span dir="rtl">نقطة تعادل الاستضافة الذاتية مقابل API</span> | **56.4** | 69.5 | 0.72 | — | 6 | 8 | 9 | 3 | 7 | 8 | 6 | 6 | 8 |
| 31 | `entry-ttc-001` | Inference-Time Compute Economics: When Thinking More Costs Less<br><span dir="rtl">اقتصاديات حوسبة وقت الاستدلال (Inference-Time Compute)</span> | **54.3** | 65.5 | 0.78 | — | 8 | 5 | 9 | 4 | 7 | 7 | 6 | 5 | 7 |
| 32 | `entry-ragcost-001` | RAG Cost Optimization: Reducing Token Waste in Retrieval<br><span dir="rtl">تحسين تكلفة الاسترجاع المعزز (RAG)</span> | **51.4** | 65.0 | 0.65 | — | 6 | 7 | 7 | 6 | 6 | 7 | 6 | 6 | 7 |
| 33 | `entry-ipw-001` | Local vs Cloud Inference: Intelligence per Watt (IPW)<br><span dir="rtl">الاستدلال المحلي مقابل السحابي — الذكاء لكل واط</span> | **50.4** | 64.0 | 0.64 | — | 7 | 7 | 6 | 5 | 6 | 7 | 5 | 7 | 6 |
| 34 | `entry-finops-001` | AI Cost Observability & Attribution (AI FinOps)<br><span dir="rtl">مراقبة تكلفة الذكاء الاصطناعي وإسنادها (AI FinOps)</span> | **49.3** | 62.0 | 0.67 | قياس/حوكمة قرار | 6 | 6 | 7 | 5 | 6 | 8 | 7 | 5 | 7 |
| 35 | `entry-sleeptime-001` | Sleep-time Compute<br><span dir="rtl">حوسبة وقت النوم</span> | **45.0** | 61.0 | 0.68 | — | 8 | 6 | 5 | 6 | 4 | 7 | 6 | 5 | 7 |
| 36 | `entry-layerskip-001` | LayerSkip: Self-Speculative Decoding with Layer Skipping<br><span dir="rtl">LayerSkip — قفز الطبقات مع فك الترميز التخميني الذاتي</span> | **43.4** | 59.5 | 0.64 | — | 8 | 6 | 6 | 4 | 5 | 5 | 4 | 6 | 6 |
| 37 | `entry-budgetlimits-001` | Agent Budget Enforcement: Preventing Runaway AI Costs<br><span dir="rtl">حدود الإنفاق التلقائية لوكلاء الذكاء الاصطناعي</span> | **40.6** | 53.5 | 0.57 | قياس/حوكمة قرار | 5 | 4 | 6 | 7 | 6 | 7 | 6 | 4 | 6 |
| 38 | `entry-customchips-001` | Custom AI Chips: AWS Trainium/Inferentia vs Google TPU vs NVIDIA GPU<br><span dir="rtl">شرائح الذكاء الاصطناعي المتخصصة — Trainium/Inferentia vs TPU vs GPU</span> | **39.5** | 58.5 | 0.58 | — | 6 | 7 | 7 | 3 | 4 | 5 | 4 | 8 | 6 |
| 39 | `entry-chinchilla-001` | Compute-Optimal Scaling Laws (Chinchilla)<br><span dir="rtl">قوانين التحجيم الأمثل حوسبياً (Chinchilla)</span> | **38.9** | 60.5 | 0.73 | — | 10 | 6 | 7 | 2 | 3 | 8 | 1 | 5 | 6 |
| 40 | `entry-sparseatt-001` | Sparse & Linear Attention: 10× Prefill Speedup for Long Contexts<br><span dir="rtl">الانتباه المتناثر والخطي — تسريع السياقات الطويلة 10×</span> | **37.5** | 59.0 | 0.59 | بحث واعد عالي الأثر | 8 | 8 | 4 | 3 | 3 | 6 | 4 | 7 | 5 |
| 41 | `entry-moequant-001` | MoE Quantization: Compressing Expert Models to Ultra-Low Bits<br><span dir="rtl">تكميم نماذج مزيج الخبراء (MoE Quantization)</span> | **36.6** | 59.0 | 0.57 | خفض ذاكرة قوي، بحث واعد عالي الأثر، ميزة معمارية ضخمة لكن معقّدة | 8 | 9 | 3 | 3 | 2 | 6 | 4 | 7 | 5 |
| 42 | `entry-apipricing-001` | LLM API Pricing Comparison (June 2026)<br><span dir="rtl">مقارنة أسعار واجهات برمجة النماذج اللغوية (يونيو 2026)</span> | **36.6** | 49.5 | 0.73 | قياس/حوكمة قرار | 7 | 1 | 10 | 1 | 6 | 10 | 1 | 3 | 8 |
| 43 | `entry-ctxcompress-001` | Context Compression & Token Reduction for Agents<br><span dir="rtl">ضغط السياق وتقليل التوكنات</span> | **36.2** | 56.5 | 0.57 | — | 7 | 7 | 4 | 5 | 3 | 6 | 5 | 6 | 5 |
| 44 | `entry-agentdiet-001` | Agent Trajectory Reduction (AgentDiet)<br><span dir="rtl">تقليص مسارات الوكلاء (AgentDiet)</span> | **34.6** | 56.0 | 0.56 | — | 9 | 7 | 3 | 5 | 3 | 4 | 3 | 5 | 4 |
| 45 | `entry-subquad-001` | Sub-Quadratic Models: Mamba-3 and Transformer Alternatives for Inference Efficiency<br><span dir="rtl">النماذج دون التربيعية — Mamba-3 وبدائل Transformer</span> | **34.1** | 58.0 | 0.60 | بحث واعد عالي الأثر | 9 | 8 | 4 | 2 | 2 | 5 | 3 | 7 | 5 |
| 46 | `entry-kvcachecompress-001` | KV Cache Compression & Eviction<br><span dir="rtl">ضغط ذاكرة KV المؤقتة</span> | **34.0** | 56.0 | 0.48 | خفض ذاكرة قوي | 7 | 9 | 2 | 3 | 3 | 6 | 3 | 7 | 5 |
| 47 | `entry-dvfs-001` | GPU Frequency Scaling (DVFS): 42% Energy Savings at 1-3% Latency Cost<br><span dir="rtl">تخفيض تردد GPU لتوفير الطاقة (DVFS)</span> | **30.9** | 49.0 | 0.55 | — | 7 | 3 | 3 | 7 | 4 | 7 | 5 | 7 | 5 |
| 48 | `entry-moespec-001` | MoE-Spec: Expert Budgeting for Efficient Speculative Decoding<br><span dir="rtl">فك الترميز التخميني الموفّر لنماذج MoE</span> | **30.8** | 54.0 | 0.47 | ميزة معمارية ضخمة لكن معقّدة | 6 | 8 | 3 | 5 | 2 | 5 | 4 | 7 | 5 |
| 49 | `entry-cpst-001` | Cost per Successful Task (CPST): The Right Metric for 2026<br><span dir="rtl">تكلفة المهمة الناجحة — المقياس الصحيح لعام 2026</span> | **28.5** | 41.5 | 0.54 | قياس/حوكمة قرار | 5 | 1 | 5 | 5 | 5 | 10 | 3 | 3 | 7 |
| 50 | `entry-cpugpu-001` | CPU-GPU Collaborative Inference for LLMs<br><span dir="rtl">الاستدلال التعاوني بين المعالج ووحدة الرسومات</span> | **28.4** | 53.0 | 0.55 | — | 8 | 7 | 4 | 3 | 2 | 4 | 3 | 6 | 4 |
| 51 | `entry-agentmultiplier-001` | Agent Token Multiplier: Why Agents Cost 5-30× More<br><span dir="rtl">مضاعف التوكن الوكيلي</span> | **27.7** | 43.0 | 0.62 | — | 5 | 1 | 9 | 1 | 5 | 10 | 1 | 3 | 8 |
| 52 | `entry-shortgpt-001` | ShortGPT: Layer Pruning in Large Language Models<br><span dir="rtl">ShortGPT — قصّ طبقات النماذج اللغوية الكبيرة</span> | **27.6** | 49.5 | 0.49 | — | 7 | 6 | 3 | 4 | 3 | 5 | 3 | 6 | 4 |
| 53 | `entry-bagen-001` | BAGEN: Budget-Aware LLM Agents — Teaching Agents to Stop Wasting Money<br><span dir="rtl">الوكلاء الواعية بالميزانية — BAGEN</span> | **24.7** | 46.0 | 0.44 | — | 6 | 6 | 2 | 4 | 3 | 6 | 3 | 5 | 4 |
| 54 | `entry-iescaling-001` | Architecture-Aware Scaling Laws for Inference-Efficient LLMs<br><span dir="rtl">قوانين التحجيم المعماري لكفاءة الاستدلال</span> | **24.3** | 49.0 | 0.55 | — | 9 | 6 | 3 | 1 | 2 | 6 | 1 | 6 | 4 |
| 55 | `entry-skillreducer-001` | SkillReducer: Optimizing LLM Agent Skills for Token Efficiency<br><span dir="rtl">ضغط مهارات الوكلاء (SkillReducer)</span> | **21.8** | 44.0 | 0.41 | — | 6 | 5 | 2 | 6 | 3 | 4 | 3 | 5 | 3 |
| 56 | `entry-hetero-001` | Heterogeneous Hardware Inference (GPU + NPU + Specialized)<br><span dir="rtl">الاستدلال على عتاد متنوع</span> | **19.2** | 46.5 | 0.45 | — | 6 | 7 | 4 | 2 | 1 | 4 | 2 | 6 | 4 |
| 57 | `entry-priceofprogress-001` | The Price of Progress: Why Token Prices Fall But Bills Rise<br><span dir="rtl">ثمن التقدم — لماذا الأسعار تنخفض والفواتير ترتفع</span> | **19.1** | 40.0 | 0.62 | قياس/حوكمة قرار | 8 | 1 | 5 | 1 | 3 | 10 | 1 | 3 | 6 |
| 58 | `entry-babbling-001` | Babbling Suppression: 44-89% Energy Savings by Stopping Unnecessary Generation<br><span dir="rtl">كبت الثرثرة — تقليل استهلاك الطاقة بمنع التوليد الزائد</span> | **17.8** | 41.0 | 0.43 | — | 7 | 3 | 2 | 7 | 2 | 4 | 2 | 6 | 3 |
| 59 | `entry-decentral-001` | Decentralized AI Inference: Peer-to-Peer GPU Networks<br><span dir="rtl">الحوسبة اللامركزية للاستدلال</span> | **15.6** | 42.5 | 0.44 | — | 6 | 6 | 3 | 2 | 1 | 4 | 3 | 5 | 4 |
| 60 | `entry-mod-001` | Mixture-of-Depths: Dynamically Allocating Compute in Transformers<br><span dir="rtl">Mixture-of-Depths — خلط الأعماق</span> | **15.3** | 40.5 | 0.43 | — | 7 | 5 | 2 | 2 | 2 | 4 | 2 | 5 | 3 |

## أفضل الطرق عمومًا — لكن ليست إجابة نهائية

1. **LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning** — **86.1/100**، الخام 95.5، الثقة 0.98. سبب التقدم: ضبط/تدريب منخفض التكلفة؛ خفض ذاكرة قوي.
2. **QLoRA: Quantized Low-Rank Adaptation** — **86.1/100**، الخام 95.5، الثقة 0.98. سبب التقدم: ضبط/تدريب منخفض التكلفة؛ خفض ذاكرة قوي.
3. **PagedAttention: Virtual Memory for KV Cache** — **82.9/100**، الخام 92.5، الثقة 0.96. سبب التقدم: خفض ذاكرة قوي.
4. **Continuous Batching: The Single Biggest Inference Lever** — **82.8/100**، الخام 93.0، الثقة 0.92. سبب التقدم: إنتاجية استدلال عالية؛ خفض API سريع التبني.
5. **Mixed Precision Training: BF16 as Standard, FP8 as Frontier** — **82.5/100**، الخام 91.5، الثقة 1.00. سبب التقدم: استدامة/طاقة.
6. **GPTQ: Post-Training Quantization for GPUs** — **82.3/100**، الخام 92.0، الثقة 0.98. سبب التقدم: خفض ذاكرة قوي.
7. **Distributed Training: DeepSpeed ZeRO & PyTorch FSDP** — **81.8/100**، الخام 90.5، الثقة 0.99. سبب التقدم: ضبط/تدريب منخفض التكلفة؛ خفض ذاكرة قوي.
8. **FlashAttention: I/O-Aware Exact Attention** — **81.7/100**، الخام 91.5، الثقة 1.00. سبب التقدم: توازن عام.
9. **AWQ: Activation-Aware Weight Quantization** — **80.1/100**، الخام 90.0، الثقة 0.94. سبب التقدم: خفض ذاكرة قوي.
10. **Batch API + Structured Output: 50-80% API Cost Reduction** — **79.7/100**، الخام 90.0، الثقة 0.91. سبب التقدم: خفض API سريع التبني.

## الأفضل حسب السيناريو

### تقليل ذاكرة GPU وتشغيل نماذج أكبر

- **QLoRA: Quantized Low-Rank Adaptation** (`entry-qlora-001`) — 86.1/100؛ ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي
- **PagedAttention: Virtual Memory for KV Cache** (`entry-pagedattention-001`) — 82.9/100؛ خفض ذاكرة قوي
- **GPTQ: Post-Training Quantization for GPUs** (`entry-gptq-001`) — 82.3/100؛ خفض ذاكرة قوي
- **AWQ: Activation-Aware Weight Quantization** (`entry-awq-001`) — 80.1/100؛ خفض ذاكرة قوي
- **LLM.int8(): Mixed-Precision INT8 with Outlier Handling** (`entry-llmint8-001`) — 76.5/100؛ —
- **Local GGUF/llama.cpp Inference: Zero API Cost on Consumer Hardware** (`entry-gguf-001`) — 75.5/100؛ خفض API سريع التبني، استدامة/طاقة

### خدمة استدلال عالية التزامن

- **PagedAttention: Virtual Memory for KV Cache** (`entry-pagedattention-001`) — 82.9/100؛ خفض ذاكرة قوي
- **Continuous Batching: The Single Biggest Inference Lever** (`entry-contbatching-001`) — 82.8/100؛ إنتاجية استدلال عالية، خفض API سريع التبني
- **FlashAttention: I/O-Aware Exact Attention** (`entry-flashattn-001`) — 81.7/100؛ —
- **EAGLE-3: State-of-the-Art Speculative Decoding** (`entry-eagle3-001`) — 69.9/100؛ إنتاجية استدلال عالية
- **RadixAttention: Prefix Sharing via Radix Tree KV Cache** (`entry-radixattention-001`) — 64.1/100؛ —
- **Speculative Decoding: Draft-then-Verify for Faster Inference** (`entry-specdec-001`) — 59.8/100؛ —

### تقليل فاتورة API بسرعة بدون امتلاك بنية تحتية

- **Batch API + Structured Output: 50-80% API Cost Reduction** (`entry-batchapi-001`) — 79.7/100؛ خفض API سريع التبني
- **Prompt/Prefix Caching: 90% Cost Reduction on Cached Portions** (`entry-promptcache-001`) — 76.6/100؛ خفض API سريع التبني
- **Intelligent Model Routing (RouteLLM)** (`entry-routing-001`) — 73.6/100؛ خفض API سريع التبني
- **Semantic Caching** (`entry-semcache-001`) — 61.3/100؛ —
- **RAG Cost Optimization: Reducing Token Waste in Retrieval** (`entry-ragcost-001`) — 51.4/100؛ —
- **Agent Budget Enforcement: Preventing Runaway AI Costs** (`entry-budgetlimits-001`) — 40.6/100؛ قياس/حوكمة قرار

### ضبط دقيق منخفض التكلفة

- **LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning** (`entry-lora-001`) — 86.1/100؛ ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي
- **QLoRA: Quantized Low-Rank Adaptation** (`entry-qlora-001`) — 86.1/100؛ ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي
- **Mixed Precision Training: BF16 as Standard, FP8 as Frontier** (`entry-mixedprec-001`) — 82.5/100؛ استدامة/طاقة
- **Distributed Training: DeepSpeed ZeRO & PyTorch FSDP** (`entry-deepspeed-001`) — 81.8/100؛ ضبط/تدريب منخفض التكلفة، خفض ذاكرة قوي
- **Model Merging: Zero-Cost Multi-Task Combination (TIES, DARE, Model Soup)** (`entry-merging-001`) — 70.6/100؛ ضبط/تدريب منخفض التكلفة
- **Synthetic Data for Cost-Efficient Training & Distillation** (`entry-synthdata-001`) — 68.5/100؛ ضبط/تدريب منخفض التكلفة

### توفير الطاقة والاستدامة

- **PagedAttention: Virtual Memory for KV Cache** (`entry-pagedattention-001`) — 82.9/100؛ خفض ذاكرة قوي
- **FlashAttention: I/O-Aware Exact Attention** (`entry-flashattn-001`) — 81.7/100؛ —
- **Local GGUF/llama.cpp Inference: Zero API Cost on Consumer Hardware** (`entry-gguf-001`) — 75.5/100؛ خفض API سريع التبني، استدامة/طاقة
- **Local vs Cloud Inference: Intelligence per Watt (IPW)** (`entry-ipw-001`) — 50.4/100؛ —
- **GPU Frequency Scaling (DVFS): 42% Energy Savings at 1-3% Latency Cost** (`entry-dvfs-001`) — 30.9/100؛ —
- **Babbling Suppression: 44-89% Energy Savings by Stopping Unnecessary Generation** (`entry-babbling-001`) — 17.8/100؛ —

### وكلاء LLM وتقليل تضخم التوكنات

- **RAG Cost Optimization: Reducing Token Waste in Retrieval** (`entry-ragcost-001`) — 51.4/100؛ —
- **Agent Budget Enforcement: Preventing Runaway AI Costs** (`entry-budgetlimits-001`) — 40.6/100؛ قياس/حوكمة قرار
- **Context Compression & Token Reduction for Agents** (`entry-ctxcompress-001`) — 36.2/100؛ —
- **Agent Trajectory Reduction (AgentDiet)** (`entry-agentdiet-001`) — 34.6/100؛ —
- **Agent Token Multiplier: Why Agents Cost 5-30× More** (`entry-agentmultiplier-001`) — 27.7/100؛ —
- **BAGEN: Budget-Aware LLM Agents — Teaching Agents to Stop Wasting Money** (`entry-bagen-001`) — 24.7/100؛ —

### ميزة معمارية كبيرة مع استعداد لتحمل التعقيد

- **DeepSeek V4 Economics: The Cheapest Frontier Model (2026)** (`entry-dsv4-001`) — 75.1/100؛ إنتاجية استدلال عالية، خفض API سريع التبني
- **Llama 4 MoE Economics: 400B Knowledge at 17B Inference Cost** (`entry-llama4-001`) — 72.6/100؛ خفض API سريع التبني، ميزة معمارية ضخمة لكن معقّدة
- **Mixture-of-Experts Economics: The Dominant Architecture of 2026** (`entry-moe-001`) — 71.5/100؛ ضبط/تدريب منخفض التكلفة
- **MoE Quantization: Compressing Expert Models to Ultra-Low Bits** (`entry-moequant-001`) — 36.6/100؛ خفض ذاكرة قوي، بحث واعد عالي الأثر، ميزة معمارية ضخمة لكن معقّدة
- **Sub-Quadratic Models: Mamba-3 and Transformer Alternatives for Inference Efficiency** (`entry-subquad-001`) — 34.1/100؛ بحث واعد عالي الأثر
- **Mixture-of-Depths: Dynamically Allocating Compute in Transformers** (`entry-mod-001`) — 15.3/100؛ —

### تخطيط استراتيجي وشراء عتاد أو اختيار مزود

- **GPU Inference Economics 2026: H100 vs B200 vs H200 Cost-per-Token** (`entry-gpuecon-001`) — 66.5/100؛ إنتاجية استدلال عالية، استدامة/طاقة
- **Self-Host vs API: The Break-Even Analysis (2026)** (`entry-breakeven-001`) — 56.4/100؛ —
- **Local vs Cloud Inference: Intelligence per Watt (IPW)** (`entry-ipw-001`) — 50.4/100؛ —
- **AI Cost Observability & Attribution (AI FinOps)** (`entry-finops-001`) — 49.3/100؛ قياس/حوكمة قرار
- **Custom AI Chips: AWS Trainium/Inferentia vs Google TPU vs NVIDIA GPU** (`entry-customchips-001`) — 39.5/100؛ —
- **LLM API Pricing Comparison (June 2026)** (`entry-apipricing-001`) — 36.6/100؛ قياس/حوكمة قرار

## كيف تقرأ النتائج؟

- **الدرجة المعايرة**: أفضل مؤشر للترتيب العام المحافظ.
- **الخام**: ماذا كانت ستسجل التقنية لو تجاهلنا عدم اليقين والسقوف.
- **الثقة**: قوة الثقة في موضع التقنية داخل الترتيب، لا ضمان نجاحها عندك.
- **الشارات**: المكان الذي قد تكون فيه التقنية ممتازة حتى لو لم تتصدر عالميًا.
- `R` عكسي: 10 يعني مخاطر قليلة، 1 يعني مخاطر عالية.

## حدود النسخة الحالية وما يجب تحسينه لاحقًا

1. إضافة قياسات موحدة من نفس العتاد والنماذج ستقوي محور الأثر.
2. فصل تكلفة التدريب عن الاستدلال في ترتيبين مستقلين قد يعطي عدالة أكبر لبعض المستخدمين.
3. يمكن إضافة تحليل حساسية للأوزان: ماذا يحدث لو زاد وزن المخاطر أو نقص وزن الأدلة؟
4. التقنيات المركبة مثل `PagedAttention + Continuous Batching + Quantization` تحتاج ترتيبًا خاصًا للحزم، لا للطرق الفردية فقط.
5. بعض الإدخالات هي مقاييس أو تحليلات سوق وليست طرق خفض مباشرة؛ أُبقيت في الجدول لأنها جزء من المكتبة، لكن وُضعت عليها سقوف محافظة.
