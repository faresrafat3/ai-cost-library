# سجل البحث | Research Log

## 2026-06-26 — Session 003

### ما تم بحثه وتدقيقه
- التحقق من أن المستودع كان موجوداً مسبقاً، ثم اختيار مسار التحديث المحافظ بناءً على توجيه المستخدم.
- مراجعة الفجوات البنيوية: كانت عدة مجلدات فرعية بلا README، وكانت `data/sources.json` و`data/claims.json` و`data/evidence.json` فارغة رغم وجود ادعاءات في ملفات Markdown.
- تطبيق سياسة **عدم المبالغة**: خُفضت بعض درجات الإثبات إلى ⭐⭐⭐ عندما كان الدليل قوياً على البناء والاختبار والاعتماد في المكتبات، لكن دليل النشر الإنتاجي المباشر لكل بوابة غير مكتمل.

### المصادر الأساسية المسجلة

| ID | Tier | Source |
|---|---|---|
| `SRC-GPTQ-2023` | Tier 1 | Frantar et al., "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", ICLR / arXiv, 2023, https://arxiv.org/abs/2210.17323 |
| `SRC-AWQ-2024` | Tier 1 | Lin et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", MLSys / arXiv, 2024, https://arxiv.org/abs/2306.00978 |
| `SRC-SMOOTHQUANT-2023` | Tier 1 | Xiao et al., "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models", ICML / arXiv, 2023, https://arxiv.org/abs/2211.10438 |
| `SRC-LLMINT8-2022` | Tier 1 | Dettmers et al., "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale", NeurIPS / arXiv, 2022, https://arxiv.org/abs/2208.07339 |
| `SRC-SPECDEC-2023` | Tier 1 | Leviathan, Kalman, and Matias, "Fast Inference from Transformers via Speculative Decoding", ICML / arXiv, 2023, https://arxiv.org/abs/2211.17192 |
| `SRC-ORCA-2022` | Tier 1 | Yu et al., "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI, 2022, https://www.usenix.org/conference/osdi22/presentation/yu |
| `SRC-VLLM-2023` | Tier 1 | Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", SOSP / arXiv, 2023, https://arxiv.org/abs/2309.06180 |
| `SRC-SGLANG-2023` | Tier 2 | Zheng et al., "SGLang: Efficient Execution of Structured Language Model Programs", arXiv, 2023, https://arxiv.org/abs/2312.07104 |
| `SRC-LORA-2022` | Tier 1 | Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR / arXiv, 2022, https://arxiv.org/abs/2106.09685 |
| `SRC-QLORA-2023` | Tier 1 | Dettmers et al., "QLoRA: Efficient Finetuning of Quantized LLMs", NeurIPS / arXiv, 2023, https://arxiv.org/abs/2305.14314 |
| `SRC-PROMPTCACHE-2023` | Tier 2 | Gim et al., "Prompt Cache: Modular Attention Reuse for Low-Latency Inference", arXiv, 2023, https://arxiv.org/abs/2311.04934 |
| `SRC-OPENAI-PROMPT-CACHING` | Tier 2 | OpenAI, "Prompt Caching documentation", Official documentation, 2024, https://platform.openai.com/docs/guides/prompt-caching |
| `SRC-ANTHROPIC-PROMPT-CACHING` | Tier 2 | Anthropic, "Prompt caching documentation", Official documentation, 2024, https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching |

### قرارات تصنيفية
- بقيت كل إدخالات البذرة الحالية ضمن **📘 Practical** لأنها تملك تطبيقات عامة ومكتبات أو أوراقاً معيارية، لكن ليست كلها **Production-Proven**.
- أضيفت فئة **Energy and Sustainability** كفئة مزروعة بلا إدخالات حتى تُوثق لاحقاً بأدلة MLPerf/Green AI/قياسات طاقة مباشرة.

### مخاطر علمية متبقية
- بعض ملفات الإدخالات القديمة ما زالت تحتوي صياغات قوية في بوابات النشر؛ يجب في الجلسة التالية ربط كل بوابة بمصدر مباشر أو تخفيض العبارة.
- لا توجد إدخالات ناشئة أو نظرية بعد؛ يجب إضافتها لتوازن المكتبة.
