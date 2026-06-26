# سجل البحث | Research Log

## الجلسة 4 — 2026-06-26

### الأبحاث المُنجزة

#### 1. Mixture-of-Depths (MoD)
- **المصدر الأساسي**: Raposo et al., DeepMind, arXiv:2404.02258 (أبريل 2024)
- **النتائج**: MoD يطابق النماذج الأساسية iso-FLOP، تسريع أخذ عينات حتى ≈50%
- **الحالة**: بحثي فقط، لا نشر إنتاجي مؤكد → تصنيف Emerging ⭐⭐
- **مصدر ثانوي**: Graphcore Research Blog (مايو 2024) — ملخص وتحليل
- **تنبيه**: تنفيذات GitHub غير رسمية — ليست موثقة إنتاجياً

#### 2. LayerSkip
- **المصدر الأساسي**: Elhoushi et al., Meta FAIR, ACL 2024, DOI: 10.18653/v1/2024.acl-long.681
- **النتائج**: 2.16× تسريع على CNN/DM، 1.82× على الترميز، 2.0× على TOPv2
- **الأدلة**: كود مفتوح على GitHub، نماذج على HuggingFace → تصنيف Practical ⭐⭐⭐
- **ملاحظة**: لا توجد تقارير نشر شركات كبرى → ليس ⭐⭐⭐⭐

#### 3. ShortGPT
- **المصدر الأساسي**: Men et al., arXiv:2403.03853 (مارس 2024)
- **النتائج**: قصّ ~25% طبقات مع الحفاظ على 85% أداء
- **الأدلة**: معايير واضحة لكن لا نشر إنتاجي → تصنيف Emerging ⭐⭐
- **مصدر تكميلي**: E3-Pruner (arXiv:2511.17205) — يتفوق على ShortGPT (58.3 vs 37.0)

#### 4. Knowledge Distillation
- **المصادر الأساسية**:
  - DistilBERT (Sanh et al., NeurIPS 2019 Workshop, arXiv:1910.01108) — 40% أصغر، 60% أسرع، 97% GLUE
  - DeepSeek-R1 Distills (DeepSeek AI, HuggingFace, يناير 2025) — 6 نماذج، 8B يطابق 235B MoE
  - MiniLLM (Gu et al., ICLR 2024) — يتفوق على KL القياسي
  - NVIDIA Minitron — 1/40 رموز تدريب، +16% MMLU
  - AWS Bedrock deployment (فبراير 2025)
  - Federal Reserve Feds (ديسمبر 2025) — Active Distillation مع 80% تخفيض عينات
- **الأدلة**: نشر إنتاجي واسع، أرقام مفصلة، حزم متاحة → تصنيف Practical ⭐⭐⭐⭐

#### 5. FlashAttention
- **المصادر الأساسية**:
  - FA-1: Dao et al., NeurIPS 2022 — 2-4× أسرع، 10-20× أقل ذاكرة
  - FA-2: Dao et al., ICLR 2024 — ~2× أسرع، 50-73% استخدام A100
  - FA-3: Shah et al., NeurIPS 2024 (Spotlight) — 740 TFLOPs/s على H100
  - FA-4: 2026 — 1613 TFLOPs/s على B200
  - Lambda Cloud benchmarks — 90% تخفيض تكلفة تدريب GPT-3
  - MLPerf Inference v4.1
- **الأدلة**: مُستخدَم في vLLM، TensorRT-LLM، Megatron-LM، HuggingFace → تصنيف Practical ⭐⭐⭐⭐

#### 6. Serving Engines Comparison
- **المصادر**:
  - GMICloud (أبريل 2026) — vLLM vs TensorRT-LLM vs Triton
  - Yottalabs (يونيو 2026) — تحديث 2026
  - BentoML (يونيو 2024) — معايير متعددة
  - NVIDIA Developer Blog (سبتمبر 2024) — MLPerf v4.1
  - HotCarbon 2025 — استهلاك الطاقة
- **النتائج**: TensorRT-LLM 15-30% أسرع من vLLM على H100

### قرارات التصنيف
1. DistilBERT → ⭐⭐⭐⭐ (نشر واسع + أرقام مفصلة + حزم رسمية)
2. DeepSeek-R1 Distills → ⭐⭐⭐⭐ (نشر على Bedrock + Fireworks)
3. FlashAttention → ⭐⭐⭐⭐ (دمج في كل البنى التحتية الرئيسية)
4. LayerSkip → ⭐⭐⭐ (كود مفتوح + معايير واضحة، لا تقارير إنتاج شركات)
5. ShortGPT → ⭐⭐ (معايير بحثية فقط، لا نشر)
6. MoD → ⭐⭐ (ورقة بحثية فقط)
