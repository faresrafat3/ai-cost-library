# مصفوفة اتخاذ القرار | Decision Matrix

## 📌 دليل الاختيار | Selection Guide

تُساعد هذه المصفوفة في اختيار التقنية الأنسب لتقليل تكلفة الذكاء الاصطناعي بناءً على السيناريو والموارد المتاحة.

This matrix helps select the most appropriate AI cost-reduction technique based on scenario and available resources.

---

## 🗺️ المصفوفة | Matrix

| السيناريو | Scenario | الأولوية الأولى | Priority 1 | الأولوية الثانية | Priority 2 | الأولوية الثالثة | Priority 3 |
|---|---|---|---|---|---|---|---|
| استدلال نموذج 70B+ على API | LLM 70B+ via API | Prompt Caching | Model Routing | Batch API | Speculative Decoding |
| استدلال نموذج 70B+ ذاتي | Self-hosted 70B+ | vLLM (PagedAttention) | AWQ/GPTQ (INT4) | Continuous Batching |
| استدلال نموذج 7-13B على GPU واحد | 7-13B on single GPU | AWQ (INT4) | vLLM | Speculative Decoding |
| ضبط دقيق بميزانية < $100 | Fine-tuning <$100 | QLoRA (NF4) | LoRA (r=16) | Gradient Checkpointing |
| ضبط متعدد المهام | Multi-task fine-tuning | LoRA | LoRAFusion | SLoRA (serving) |
| تطبيق RAG + Agent | RAG + Agent app | RadixAttention (SGLang) | Prompt Caching | Re-ranking |
| نشر على جهاز طرفي | Edge deployment | AWQ (INT4) | SmoothQuant+ | Distillation |
| نشر على خادم إنتاج | Production server | vLLM/SGLang | Continuous Batching | SmoothQuant |
| أحمال غير متزامنة (Batch) | Async batch workloads | Batch API | Continuous Batching | Quantization |
| تطبيقات تفاعلية (Chatbot) | Interactive chatbots | Speculative Decoding | RadixAttention | Prefix Caching |

## 📊 أولويات التنفيذ حسب الأثر | Implementation Priority by Impact

### الأثر الفوري (Immediate Impact — 1-3 أيام)
1. **Prompt Caching** — تفعيل في API أو vLLM (سطر واحد)
2. **Continuous Batching** — مفعّل افتراضياً في vLLM و SGLang
3. **Model Routing** — توجيه الطلبات البسيطة لنماذج أرخص

### الأثر المتوسط (Medium Impact — 1-2 أسابيع)
4. **Quantization (INT8/INT4)** — AWQ أو GPTQ أو SmoothQuant
5. **PagedAttention / RadixAttention** — اختيار المحرك المناسب
6. **LoRA / QLoRA** — ضبط دقيق بدلاً من تدريب كامل

### الأثر الطويل (Long-term Impact — 1-3 أشهر)
7. **Speculative Decoding** — إعداد نموذج مسودة متوافق
8. **Distillation** — تدريب نموذج أصغر
9. **Infrastructure Optimization** — تخطيط العتاد والبنية
