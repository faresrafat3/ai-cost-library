# التصنيف العادل متعدد المعايير | Fair Multi-Criteria Ranking
> تاريخ الإصدار: 2026-06-27 | عدد المداخل المصنّفة: **60** | النطاق: كل ما في `data/entries.json`.

## الخلاصة التنفيذية

هذا الملف يرتّب طرق خفض تكلفة الذكاء الاصطناعي في المكتبة ترتيبًا عامًا من 1 إلى N باستخدام 9 محاور كمية. الهدف ليس اختيار التقنية "الأكثر لمعانًا"، بل الأكثر نفعًا عمليًا عند الموازنة بين قوة الدليل، مقدار التوفير، النضج، سهولة التطبيق، المخاطر، قابلية التعميم، الأدوات، الاستدامة، والتوافق الإنتاجي.

## الخوارزمية والأوزان

لم أغيّر الأوزان الافتراضية المطلوبة؛ استخدمت الأوزان كما هي لأن المكتبة تحتوي مزيجًا واسعًا من تقنيات تدريب/استدلال/حوكمة، وتغيير الأوزان كان سيجعل التصنيف العام منحازًا لسيناريو واحد. الدرجة النهائية معروضة من **100**، وهي تساوي: `10 × Σ(درجة المحور من 1 إلى 10 × الوزن)`.

| الرمز | المحور | الوزن | كيف حُسب عمليًا |
|---|---|---:|---|
| E | قوة الأدلة والتوثيق | 20% | جودة المصدر وقابلية التكرار وعدد المصادر وإشارات Tier 1/2/3. |
| C | مقدار خفض التكلفة الفعلي | 25% | أعلى أثر موثق بين خفض تكلفة الاستدلال/التدريب/الذاكرة/تحسين الإنتاجية. |
| M | النضج والجاهزية | 15% | نضج الإنتاج من بيانات المكتبة وحالة الإدخال. |
| I | سهولة التطبيق | 10% | مدى بساطة التبني: إعدادات/مكتبة جاهزة مقابل تعديل معماري أو عتاد خاص. |
| R | المخاطر والقيود، عكسي | 10% | درجة أعلى تعني مخاطر أقل؛ خُفّضت للنماذج الأولية، التقنيات النظرية، أو المخاطر المعروفة كفقد الدقة/التعقيد/الاعتماد على عتاد. |
| G | قابلية التعميم | 5% | قابلية العمل عبر نماذج ومهام وبيئات مختلفة. |
| T | الدعم المجتمعي والأدوات | 5% | وجود مكتبات ومحركات وخيارات مفتوحة المصدر وتوثيق. |
| S | الاستدامة والأثر البيئي | 5% | مشتقة من أثر التوفير والإنتاجية والذاكرة، مع مكافأة للعمل الصريح على الطاقة/الواط. |
| P | التوافق مع الإنتاج | 5% | قابلية النشر السحابي/API/محركات الاستدلال والتوسع. |

### ملاحظات العدالة

- التقنيات التدريبية مثل LoRA/QLoRA لا تُعاقَب لأنها لا تخفض تكلفة API مباشرة؛ محور الأثر يأخذ أقوى بُعد موثق لها.
- التقنيات النظرية/الناشئة يمكن أن تحصل على أثر مرتفع، لكنها تخسر نقاطًا في النضج والمخاطر والتوافق الإنتاجي.
- عند نقص المعلومات التفصيلية في ملف إدخال، استُخدمت درجات `data/scoring.json` والـ frontmatter ثم حُكم علمي محافظ، لذلك هذه قائمة قابلة للمراجعة وليست حكمًا نهائيًا.

## جدول التصنيف العام

| الرتبة | ID | العنوان | الدرجة | E | C | M | I | R | G | T | S | P |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `entry-lora-001` | LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning<br><span dir="rtl">التكيف منخفض الرتبة — LoRA</span> | **97.0** | 10 | 10 | 10 | 9 | 10 | 9 | 10 | 8 | 9 |
| 2 | `entry-qlora-001` | QLoRA: Quantized Low-Rank Adaptation<br><span dir="rtl">الضبط الدقيق المُكمَّم — QLoRA</span> | **96.5** | 10 | 10 | 10 | 9 | 10 | 9 | 10 | 8 | 8 |
| 3 | `entry-contbatching-001` | Continuous Batching: The Single Biggest Inference Lever<br><span dir="rtl">التجميع المستمر</span> | **95.5** | 9 | 10 | 10 | 8 | 10 | 10 | 10 | 9 | 10 |
| 4 | `entry-gptq-001` | GPTQ: Post-Training Quantization for GPUs<br><span dir="rtl">التكميم بعد التدريب — GPTQ</span> | **92.5** | 10 | 9 | 10 | 8 | 9 | 8 | 10 | 8 | 10 |
| 5 | `entry-mixedprec-001` | Mixed Precision Training: BF16 as Standard, FP8 as Frontier<br><span dir="rtl">التدريب بالدقة المختلطة (BF16/FP8)</span> | **92.5** | 10 | 8 | 10 | 8 | 10 | 10 | 10 | 9 | 10 |
| 6 | `entry-pagedattention-001` | PagedAttention: Virtual Memory for KV Cache<br><span dir="rtl">الانتباه المُقسَّم للصفحات — PagedAttention</span> | **92.5** | 9 | 9 | 10 | 8 | 10 | 10 | 10 | 8 | 10 |
| 7 | `entry-flashattn-001` | FlashAttention: I/O-Aware Exact Attention<br><span dir="rtl">FlashAttention — الانتباه المُحسَّن للذاكرة</span> | **92.0** | 10 | 8 | 10 | 8 | 10 | 10 | 10 | 8 | 10 |
| 8 | `entry-deepspeed-001` | Distributed Training: DeepSpeed ZeRO & PyTorch FSDP<br><span dir="rtl">التدريب الموزّع — DeepSpeed ZeRO و FSDP</span> | **91.0** | 10 | 9 | 10 | 6 | 9 | 9 | 10 | 8 | 10 |
| 9 | `entry-awq-001` | AWQ: Activation-Aware Weight Quantization<br><span dir="rtl">التكميم المُدرك للتفعيل — AWQ</span> | **90.5** | 9 | 9 | 10 | 8 | 9 | 8 | 10 | 8 | 10 |
| 10 | `entry-batchapi-001` | Batch API + Structured Output: 50-80% API Cost Reduction<br><span dir="rtl">واجهة الدفعات وتحسين المخرجات — 50-80% تقليل تكلفة API</span> | **90.5** | 8 | 9 | 10 | 9 | 10 | 9 | 10 | 7 | 10 |
| 11 | `entry-dsv4-001` | DeepSeek V4 Economics: The Cheapest Frontier Model (2026)<br><span dir="rtl">اقتصاديات DeepSeek V4 — أرخص نموذج حدودي في 2026</span> | **88.0** | 7 | 10 | 10 | 8 | 9 | 8 | 8 | 9 | 9 |
| 12 | `entry-llmint8-001` | LLM.int8(): Mixed-Precision INT8 with Outlier Handling<br><span dir="rtl">التكميم الصحيح 8-بت مع معالجة القيم الشاذة — LLM.int8()</span> | **88.0** | 10 | 8 | 9 | 9 | 9 | 8 | 9 | 8 | 8 |
| 13 | `entry-gguf-001` | Local GGUF/llama.cpp Inference: Zero API Cost on Consumer Hardware<br><span dir="rtl">الاستدلال المحلي بـ GGUF — صفر تكلفة API</span> | **87.5** | 7 | 9 | 10 | 10 | 9 | 6 | 10 | 10 | 8 |
| 14 | `entry-promptcache-001` | Prompt/Prefix Caching: 90% Cost Reduction on Cached Portions<br><span dir="rtl">تخزين البادئات مؤقتاً</span> | **87.5** | 7 | 9 | 10 | 9 | 9 | 9 | 10 | 7 | 10 |
| 15 | `entry-routing-001` | Intelligent Model Routing (RouteLLM)<br><span dir="rtl">توجيه النماذج الذكي</span> | **87.5** | 10 | 10 | 8 | 7 | 8 | 8 | 8 | 7 | 8 |
| 16 | `entry-distillation-001` | Knowledge Distillation — From DistilBERT to DeepSeek-R1<br><span dir="rtl">استخلاص المعرفة — من DistilBERT إلى DeepSeek-R1</span> | **87.0** | 10 | 9 | 10 | 5 | 8 | 8 | 8 | 8 | 9 |
| 17 | `entry-qwen3-001` | Qwen3 Efficiency: Thinking/Non-Thinking Fusion & Budget Control<br><span dir="rtl">كفاءات Qwen3 — دمج التفكير واللا-تفكير في نموذج واحد</span> | **87.0** | 9 | 8 | 10 | 8 | 9 | 8 | 9 | 8 | 9 |
| 18 | `entry-fp8-001` | FP8 Quantization<br><span dir="rtl">التكميم بدقة FP8</span> | **86.5** | 9 | 8 | 10 | 8 | 9 | 7 | 9 | 8 | 9 |
| 19 | `entry-moe-001` | Mixture-of-Experts Economics: The Dominant Architecture of 2026<br><span dir="rtl">اقتصاديات مزيج الخبراء (MoE)</span> | **85.0** | 10 | 10 | 10 | 3 | 6 | 7 | 7 | 9 | 9 |
| 20 | `entry-llama4-001` | Llama 4 MoE Economics: 400B Knowledge at 17B Inference Cost<br><span dir="rtl">اقتصاديات Llama 4 — مثال عملي على قوة MoE المفتوحة</span> | **83.5** | 7 | 9 | 10 | 7 | 8 | 8 | 9 | 8 | 9 |
| 21 | `entry-eagle3-001` | EAGLE-3: State-of-the-Art Speculative Decoding<br><span dir="rtl">فك الترميز التخميني EAGLE-3</span> | **82.0** | 8 | 9 | 8 | 7 | 8 | 8 | 9 | 8 | 8 |
| 22 | `entry-merging-001` | Model Merging: Zero-Cost Multi-Task Combination (TIES, DARE, Model Soup)<br><span dir="rtl">دمج النماذج — بديل رخيص للتدريب المتعدد المهام</span> | **82.0** | 9 | 9 | 7 | 8 | 8 | 7 | 9 | 7 | 7 |
| 23 | `entry-synthdata-001` | Synthetic Data for Cost-Efficient Training & Distillation<br><span dir="rtl">البيانات الاصطناعية لتقليل تكلفة التدريب</span> | **81.0** | 8 | 9 | 9 | 6 | 8 | 8 | 7 | 7 | 8 |
| 24 | `entry-gpuecon-001` | GPU Inference Economics 2026: H100 vs B200 vs H200 Cost-per-Token<br><span dir="rtl">اقتصاديات GPU للاستدلال — مقارنة H100 vs B200 vs H200 (2026)</span> | **78.0** | 7 | 9 | 9 | 4 | 7 | 8 | 7 | 10 | 9 |
| 25 | `entry-multilora-001` | Multi-LoRA Serving: Hundreds of Fine-Tuned Models on One GPU<br><span dir="rtl">خدمة LoRA متعددة المستأجرين — مئات النماذج على GPU واحد</span> | **76.5** | 8 | 8 | 8 | 6 | 7 | 7 | 8 | 8 | 8 |
| 26 | `entry-radixattention-001` | RadixAttention: Prefix Sharing via Radix Tree KV Cache<br><span dir="rtl">شجرة الانتباه المتفرعة — RadixAttention (SGLang)</span> | **76.5** | 8 | 8 | 8 | 7 | 7 | 6 | 7 | 8 | 8 |
| 27 | `entry-semcache-001` | Semantic Caching<br><span dir="rtl">التخزين المؤقت الدلالي</span> | **76.0** | 7 | 9 | 8 | 6 | 7 | 7 | 7 | 7 | 8 |
| 28 | `entry-smoothquant-001` | SmoothQuant: Smooth Activations for INT8 Quantization<br><span dir="rtl">التكميم الأملس — SmoothQuant</span> | **75.0** | 9 | 7 | 8 | 6 | 7 | 7 | 7 | 7 | 8 |
| 29 | `entry-specdec-001` | Speculative Decoding: Draft-then-Verify for Faster Inference<br><span dir="rtl">فك الترميز التخميني</span> | **72.5** | 9 | 7 | 8 | 5 | 6 | 7 | 7 | 7 | 7 |
| 30 | `entry-breakeven-001` | Self-Host vs API: The Break-Even Analysis (2026)<br><span dir="rtl">نقطة تعادل الاستضافة الذاتية مقابل API</span> | **70.0** | 6 | 8 | 9 | 3 | 7 | 8 | 6 | 7 | 8 |
| 31 | `entry-ragcost-001` | RAG Cost Optimization: Reducing Token Waste in Retrieval<br><span dir="rtl">تحسين تكلفة الاسترجاع المعزز (RAG)</span> | **67.0** | 7 | 7 | 7 | 6 | 6 | 7 | 6 | 6 | 7 |
| 32 | `entry-ttc-001` | Inference-Time Compute Economics: When Thinking More Costs Less<br><span dir="rtl">اقتصاديات حوسبة وقت الاستدلال (Inference-Time Compute)</span> | **65.5** | 8 | 5 | 9 | 4 | 7 | 7 | 6 | 5 | 7 |
| 33 | `entry-ipw-001` | Local vs Cloud Inference: Intelligence per Watt (IPW)<br><span dir="rtl">الاستدلال المحلي مقابل السحابي — الذكاء لكل واط</span> | **64.5** | 7 | 7 | 6 | 5 | 6 | 7 | 5 | 8 | 6 |
| 34 | `entry-chinchilla-001` | Compute-Optimal Scaling Laws (Chinchilla)<br><span dir="rtl">قوانين التحجيم الأمثل حوسبياً (Chinchilla)</span> | **63.5** | 10 | 7 | 7 | 2 | 3 | 8 | 1 | 6 | 6 |
| 35 | `entry-finops-001` | AI Cost Observability & Attribution (AI FinOps)<br><span dir="rtl">مراقبة تكلفة الذكاء الاصطناعي وإسنادها (AI FinOps)</span> | **63.0** | 6 | 6 | 7 | 5 | 6 | 8 | 7 | 6 | 8 |
| 36 | `entry-sleeptime-001` | Sleep-time Compute<br><span dir="rtl">حوسبة وقت النوم</span> | **62.5** | 8 | 6 | 5 | 6 | 5 | 7 | 6 | 6 | 7 |
| 37 | `entry-sparseatt-001` | Sparse & Linear Attention: 10× Prefill Speedup for Long Contexts<br><span dir="rtl">الانتباه المتناثر والخطي — تسريع السياقات الطويلة 10×</span> | **60.0** | 8 | 8 | 4 | 3 | 3 | 6 | 4 | 8 | 6 |
| 38 | `entry-layerskip-001` | LayerSkip: Self-Speculative Decoding with Layer Skipping<br><span dir="rtl">LayerSkip — قفز الطبقات مع فك الترميز التخميني الذاتي</span> | **59.5** | 8 | 6 | 6 | 4 | 5 | 5 | 4 | 6 | 6 |
| 39 | `entry-moequant-001` | MoE Quantization: Compressing Expert Models to Ultra-Low Bits<br><span dir="rtl">تكميم نماذج مزيج الخبراء (MoE Quantization)</span> | **59.5** | 8 | 9 | 3 | 3 | 2 | 6 | 4 | 8 | 5 |
| 40 | `entry-customchips-001` | Custom AI Chips: AWS Trainium/Inferentia vs Google TPU vs NVIDIA GPU<br><span dir="rtl">شرائح الذكاء الاصطناعي المتخصصة — Trainium/Inferentia vs TPU vs GPU</span> | **58.5** | 6 | 7 | 7 | 3 | 4 | 5 | 4 | 8 | 6 |
| 41 | `entry-subquad-001` | Sub-Quadratic Models: Mamba-3 and Transformer Alternatives for Inference Efficiency<br><span dir="rtl">النماذج دون التربيعية — Mamba-3 وبدائل Transformer</span> | **58.5** | 9 | 8 | 4 | 2 | 2 | 5 | 3 | 8 | 5 |
| 42 | `entry-ctxcompress-001` | Context Compression & Token Reduction for Agents<br><span dir="rtl">ضغط السياق وتقليل التوكنات</span> | **57.5** | 7 | 7 | 4 | 5 | 4 | 6 | 5 | 6 | 5 |
| 43 | `entry-agentdiet-001` | Agent Trajectory Reduction (AgentDiet)<br><span dir="rtl">تقليص مسارات الوكلاء (AgentDiet)</span> | **56.5** | 9 | 7 | 3 | 5 | 3 | 4 | 3 | 6 | 4 |
| 44 | `entry-budgetlimits-001` | Agent Budget Enforcement: Preventing Runaway AI Costs<br><span dir="rtl">حدود الإنفاق التلقائية لوكلاء الذكاء الاصطناعي</span> | **56.5** | 5 | 5 | 6 | 7 | 6 | 7 | 6 | 5 | 6 |
| 45 | `entry-kvcachecompress-001` | KV Cache Compression & Eviction<br><span dir="rtl">ضغط ذاكرة KV المؤقتة</span> | **56.5** | 7 | 9 | 2 | 3 | 3 | 6 | 3 | 8 | 5 |
| 46 | `entry-moespec-001` | MoE-Spec: Expert Budgeting for Efficient Speculative Decoding<br><span dir="rtl">فك الترميز التخميني الموفّر لنماذج MoE</span> | **54.5** | 6 | 8 | 3 | 5 | 2 | 5 | 4 | 8 | 5 |
| 47 | `entry-cpugpu-001` | CPU-GPU Collaborative Inference for LLMs<br><span dir="rtl">الاستدلال التعاوني بين المعالج ووحدة الرسومات</span> | **53.5** | 8 | 7 | 4 | 3 | 2 | 4 | 3 | 7 | 4 |
| 48 | `entry-iescaling-001` | Architecture-Aware Scaling Laws for Inference-Efficient LLMs<br><span dir="rtl">قوانين التحجيم المعماري لكفاءة الاستدلال</span> | **53.5** | 10 | 7 | 3 | 1 | 1 | 6 | 1 | 7 | 5 |
| 49 | `entry-hetero-001` | Heterogeneous Hardware Inference (GPU + NPU + Specialized)<br><span dir="rtl">الاستدلال على عتاد متنوع</span> | **50.0** | 7 | 7 | 4 | 2 | 2 | 4 | 2 | 7 | 4 |
| 50 | `entry-apipricing-001` | LLM API Pricing Comparison (June 2026)<br><span dir="rtl">مقارنة أسعار واجهات برمجة النماذج اللغوية (يونيو 2026)</span> | **49.5** | 7 | 1 | 10 | 1 | 6 | 10 | 1 | 3 | 8 |
| 51 | `entry-shortgpt-001` | ShortGPT: Layer Pruning in Large Language Models<br><span dir="rtl">ShortGPT — قصّ طبقات النماذج اللغوية الكبيرة</span> | **49.5** | 7 | 6 | 3 | 4 | 3 | 5 | 3 | 6 | 4 |
| 52 | `entry-dvfs-001` | GPU Frequency Scaling (DVFS): 42% Energy Savings at 1-3% Latency Cost<br><span dir="rtl">تخفيض تردد GPU لتوفير الطاقة (DVFS)</span> | **49.0** | 7 | 3 | 3 | 7 | 4 | 7 | 5 | 7 | 5 |
| 53 | `entry-bagen-001` | BAGEN: Budget-Aware LLM Agents — Teaching Agents to Stop Wasting Money<br><span dir="rtl">الوكلاء الواعية بالميزانية — BAGEN</span> | **46.5** | 6 | 6 | 2 | 4 | 3 | 6 | 3 | 6 | 4 |
| 54 | `entry-skillreducer-001` | SkillReducer: Optimizing LLM Agent Skills for Token Efficiency<br><span dir="rtl">ضغط مهارات الوكلاء (SkillReducer)</span> | **44.0** | 6 | 5 | 2 | 6 | 3 | 4 | 3 | 5 | 3 |
| 55 | `entry-agentmultiplier-001` | Agent Token Multiplier: Why Agents Cost 5-30× More<br><span dir="rtl">مضاعف التوكن الوكيلي</span> | **43.0** | 5 | 1 | 9 | 1 | 5 | 10 | 1 | 3 | 8 |
| 56 | `entry-decentral-001` | Decentralized AI Inference: Peer-to-Peer GPU Networks<br><span dir="rtl">الحوسبة اللامركزية للاستدلال</span> | **43.0** | 6 | 6 | 3 | 2 | 1 | 4 | 3 | 6 | 4 |
| 57 | `entry-cpst-001` | Cost per Successful Task (CPST): The Right Metric for 2026<br><span dir="rtl">تكلفة المهمة الناجحة — المقياس الصحيح لعام 2026</span> | **42.5** | 5 | 1 | 5 | 5 | 6 | 10 | 3 | 3 | 7 |
| 58 | `entry-babbling-001` | Babbling Suppression: 44-89% Energy Savings by Stopping Unnecessary Generation<br><span dir="rtl">كبت الثرثرة — تقليل استهلاك الطاقة بمنع التوليد الزائد</span> | **42.0** | 7 | 3 | 2 | 7 | 3 | 4 | 2 | 6 | 3 |
| 59 | `entry-mod-001` | Mixture-of-Depths: Dynamically Allocating Compute in Transformers<br><span dir="rtl">Mixture-of-Depths — خلط الأعماق</span> | **41.5** | 7 | 5 | 2 | 2 | 2 | 4 | 2 | 6 | 4 |
| 60 | `entry-priceofprogress-001` | The Price of Progress: Why Token Prices Fall But Bills Rise<br><span dir="rtl">ثمن التقدم — لماذا الأسعار تنخفض والفواتير ترتفع</span> | **40.0** | 8 | 1 | 5 | 1 | 3 | 10 | 1 | 3 | 6 |

## الطرق الأفضل عمومًا

1. **LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning** — **97.0/100**: توازن قوي بين الدليل (10/10)، الأثر (10/10)، النضج (10/10)، والأدوات (10/10).
2. **QLoRA: Quantized Low-Rank Adaptation** — **96.5/100**: توازن قوي بين الدليل (10/10)، الأثر (10/10)، النضج (10/10)، والأدوات (10/10).
3. **Continuous Batching: The Single Biggest Inference Lever** — **95.5/100**: توازن قوي بين الدليل (9/10)، الأثر (10/10)، النضج (10/10)، والأدوات (10/10).
4. **GPTQ: Post-Training Quantization for GPUs** — **92.5/100**: توازن قوي بين الدليل (10/10)، الأثر (9/10)، النضج (10/10)، والأدوات (10/10).
5. **Mixed Precision Training: BF16 as Standard, FP8 as Frontier** — **92.5/100**: توازن قوي بين الدليل (10/10)، الأثر (8/10)، النضج (10/10)، والأدوات (10/10).
6. **PagedAttention: Virtual Memory for KV Cache** — **92.5/100**: توازن قوي بين الدليل (9/10)، الأثر (9/10)، النضج (10/10)، والأدوات (10/10).
7. **FlashAttention: I/O-Aware Exact Attention** — **92.0/100**: توازن قوي بين الدليل (10/10)، الأثر (8/10)، النضج (10/10)، والأدوات (10/10).
8. **Distributed Training: DeepSpeed ZeRO & PyTorch FSDP** — **91.0/100**: توازن قوي بين الدليل (10/10)، الأثر (9/10)، النضج (10/10)، والأدوات (10/10).
9. **AWQ: Activation-Aware Weight Quantization** — **90.5/100**: توازن قوي بين الدليل (9/10)، الأثر (9/10)، النضج (10/10)، والأدوات (10/10).
10. **Batch API + Structured Output: 50-80% API Cost Reduction** — **90.5/100**: توازن قوي بين الدليل (8/10)، الأثر (9/10)، النضج (10/10)، والأدوات (10/10).

## الأفضل حسب السيناريو

### إذا كنت تريد تقليل ذاكرة GPU وتشغيل نماذج أكبر

- **QLoRA: Quantized Low-Rank Adaptation** (`entry-qlora-001`) — 96.5/100
- **GPTQ: Post-Training Quantization for GPUs** (`entry-gptq-001`) — 92.5/100
- **PagedAttention: Virtual Memory for KV Cache** (`entry-pagedattention-001`) — 92.5/100
- **AWQ: Activation-Aware Weight Quantization** (`entry-awq-001`) — 90.5/100
- **Local GGUF/llama.cpp Inference: Zero API Cost on Consumer Hardware** (`entry-gguf-001`) — 87.5/100

### إذا كنت تشغّل خدمة استدلال عالية التزامن

- **Continuous Batching: The Single Biggest Inference Lever** (`entry-contbatching-001`) — 95.5/100
- **PagedAttention: Virtual Memory for KV Cache** (`entry-pagedattention-001`) — 92.5/100
- **FlashAttention: I/O-Aware Exact Attention** (`entry-flashattn-001`) — 92.0/100
- **RadixAttention: Prefix Sharing via Radix Tree KV Cache** (`entry-radixattention-001`) — 76.5/100
- **Speculative Decoding: Draft-then-Verify for Faster Inference** (`entry-specdec-001`) — 72.5/100

### إذا كنت تريد تقليل فاتورة API بسرعة دون امتلاك بنية تحتية

- **Batch API + Structured Output: 50-80% API Cost Reduction** (`entry-batchapi-001`) — 90.5/100
- **Prompt/Prefix Caching: 90% Cost Reduction on Cached Portions** (`entry-promptcache-001`) — 87.5/100
- **Intelligent Model Routing (RouteLLM)** (`entry-routing-001`) — 87.5/100
- **Semantic Caching** (`entry-semcache-001`) — 76.0/100
- **RAG Cost Optimization: Reducing Token Waste in Retrieval** (`entry-ragcost-001`) — 67.0/100

### إذا كان هدفك الضبط الدقيق منخفض التكلفة

- **LoRA: Low-Rank Adaptation — The Foundation of Efficient Fine-Tuning** (`entry-lora-001`) — 97.0/100
- **QLoRA: Quantized Low-Rank Adaptation** (`entry-qlora-001`) — 96.5/100
- **Mixed Precision Training: BF16 as Standard, FP8 as Frontier** (`entry-mixedprec-001`) — 92.5/100
- **Distributed Training: DeepSpeed ZeRO & PyTorch FSDP** (`entry-deepspeed-001`) — 91.0/100
- **Synthetic Data for Cost-Efficient Training & Distillation** (`entry-synthdata-001`) — 81.0/100

### إذا كان هدفك الاستدامة والطاقة

- **PagedAttention: Virtual Memory for KV Cache** (`entry-pagedattention-001`) — 92.5/100
- **FlashAttention: I/O-Aware Exact Attention** (`entry-flashattn-001`) — 92.0/100
- **Local vs Cloud Inference: Intelligence per Watt (IPW)** (`entry-ipw-001`) — 64.5/100
- **GPU Frequency Scaling (DVFS): 42% Energy Savings at 1-3% Latency Cost** (`entry-dvfs-001`) — 49.0/100
- **Babbling Suppression: 44-89% Energy Savings by Stopping Unnecessary Generation** (`entry-babbling-001`) — 42.0/100

### إذا كنت تبني وكلاء LLM وتخشى تضخم التوكنات

- **RAG Cost Optimization: Reducing Token Waste in Retrieval** (`entry-ragcost-001`) — 67.0/100
- **Context Compression & Token Reduction for Agents** (`entry-ctxcompress-001`) — 57.5/100
- **Agent Budget Enforcement: Preventing Runaway AI Costs** (`entry-budgetlimits-001`) — 56.5/100
- **Agent Trajectory Reduction (AgentDiet)** (`entry-agentdiet-001`) — 56.5/100
- **Agent Token Multiplier: Why Agents Cost 5-30× More** (`entry-agentmultiplier-001`) — 43.0/100

### إذا كنت في مرحلة تخطيط استراتيجي أو شراء عتاد

- **GPU Inference Economics 2026: H100 vs B200 vs H200 Cost-per-Token** (`entry-gpuecon-001`) — 78.0/100
- **Self-Host vs API: The Break-Even Analysis (2026)** (`entry-breakeven-001`) — 70.0/100
- **Local vs Cloud Inference: Intelligence per Watt (IPW)** (`entry-ipw-001`) — 64.5/100
- **Custom AI Chips: AWS Trainium/Inferentia vs Google TPU vs NVIDIA GPU** (`entry-customchips-001`) — 58.5/100
- **LLM API Pricing Comparison (June 2026)** (`entry-apipricing-001`) — 49.5/100

## قراءة سريعة للمحاور

`E` الدليل، `C` الأثر، `M` النضج، `I` سهولة التطبيق، `R` المخاطر عكسيًا، `G` التعميم، `T` الأدوات، `S` الاستدامة، `P` توافق الإنتاج. كل محور من 1 إلى 10.

## حدود التقييم

هذا التصنيف عام. في قرار شراء أو هندسة فعلي يجب إعادة وزن المحاور حسب السياق: شركة API، فريق تدريب، باحث، أو مطور فردي. كما أن أرقام 2026 الخاصة بالأسعار والعتاد تتغير بسرعة، لذلك يفضّل تحديث التصنيف عند إضافة مصادر Tier 1 أو قياسات إنتاجية جديدة.
