# مصفوفة اتخاذ القرار | Decision Matrix

| السيناريو | Scenario | جرّب أولاً | Try First | متى تتجنب؟ |
|---|---|---|---|---|
| تقليل تكلفة API لنموذج لغوي | Reduce LLM API cost | prompt-caching, model-routing, prompt-shortening | prompt-caching, model-routing, prompt-shortening | إذا كانت البوادئ غير متكررة أو قصيرة جداً. |
| استضافة نموذج 7B-13B على GPU واحد | Self-host 7B-13B on one GPU | AWQ/GPTQ, vLLM/PagedAttention, continuous-batching | AWQ/GPTQ, vLLM/PagedAttention, continuous-batching | إذا كانت الدقة في مهام حساسة تتدهور بعد التكمية. |
| ضبط دقيق منخفض الميزانية | Low-budget fine-tuning | QLoRA, LoRA, gradient-checkpointing | QLoRA, LoRA, gradient-checkpointing | إذا كان المطلوب تعديل كل أوزان النموذج أو تدريب من الصفر. |
| زمن استجابة مرتفع في الاستدلال | High inference latency | speculative-decoding, continuous-batching, KV-cache reuse | speculative-decoding, continuous-batching, KV-cache reuse | إذا لم يتوفر نموذج مسودة جيد أو كانت الطلبات قصيرة جداً. |
