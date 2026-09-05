# مصفوفة اتخاذ القرار | Decision Matrix

> **آخر تحديث: 2026-09-04 (round 78)**
>
> **ملاحظة عن drift (2026-09-04)**: عمود "Try First" يحوي **نفس النص الإنجليزي** الموجود في عمود "جرّب أولاً". هذا ليس تكراراً مقصوداً — بل drift ناتج عن أن `data/decision_matrix.json` يحوي حقل `try_first` بـ **أسماء إنجليزية فقط** (لا يوجد `try_first_ar`). الجدول يحاول أن يكون ثنائي اللغة لكن المصدر يخل بتوازن `_ar` / `_en`:
>
> | field | لغة | حالة |
> |---|---|---|
> | `scenario_ar` / `scenario_en` | AR + EN | ✅ متوازن |
> | `try_first` | EN فقط | ⚠️ يحوي أسماء تقنيات بالإنجليزية، لا توجد ترجمة عربية في الـ JSON |
> | `avoid_when_ar` | AR فقط | ⚠️ لا يوجد `avoid_when_en` |
>
> الإصلاح الصحيح (out of scope لهذه الجلسة): إضافة `try_first_ar` و`avoid_when_en` إلى كل entry في `data/decision_matrix.json`، ثم إعادة بناء الجدول ليعرض الأسماء العربية في عمود "جرّب أولاً" والإنجليزية في "Try First". حالياً الجدول يخفي drift بإظهار الإنجليزية في كلا العمودين.
>
> **Drift note (2026-09-04)**: The "Try First" column shows the **same English text** as the "جرّب أولاً" column. This is not intentional duplication — it's drift caused by `data/decision_matrix.json` having a `try_first` field with **English-only technique names** (no `try_first_ar`). The table tries to be bilingual but the source data is unbalanced:
>
> | field | language | state |
> |---|---|---|
> | `scenario_ar` / `scenario_en` | AR + EN | ✅ balanced |
> | `try_first` | EN only | ⚠️ has English technique names, no Arabic translation in JSON |
> | `avoid_when_ar` | AR only | ⚠️ no `avoid_when_en` |
>
> The proper fix (out of scope for this session): add `try_first_ar` and `avoid_when_en` to each entry in `data/decision_matrix.json`, then rebuild the table to show Arabic in the "جرّب أولاً" column and English in "Try First". The current table hides the drift by showing English in both columns.

| السيناريو | Scenario | جرّب أولاً (en only — see drift note) | Try First (en only — see drift note) | متى تتجنب؟ (ar only — see drift note) |
|---|---|---|---|---|
| تقليل تكلفة API لنموذج لغوي | Reduce LLM API cost | prompt-caching, model-routing, prompt-shortening | prompt-caching, model-routing, prompt-shortening | إذا كانت البوادئ غير متكررة أو قصيرة جداً. |
| استضافة نموذج 7B-13B على GPU واحد | Self-host 7B-13B on one GPU | AWQ/GPTQ, vLLM/PagedAttention, continuous-batching | AWQ/GPTQ, vLLM/PagedAttention, continuous-batching | إذا كانت الدقة في مهام حساسة تتدهور بعد التكمية. |
| ضبط دقيق منخفض الميزانية | Low-budget fine-tuning | QLoRA, LoRA, gradient-checkpointing | QLoRA, LoRA, gradient-checkpointing | إذا كان المطلوب تعديل كل أوزان النموذج أو تدريب من الصفر. |
| زمن استجابة مرتفع في الاستدلال | High inference latency | speculative-decoding, continuous-batching, KV-cache reuse | speculative-decoding, continuous-batching, KV-cache reuse | إذا لم يتوفر نموذج مسودة جيد أو كانت الطلبات قصيرة جداً. |
