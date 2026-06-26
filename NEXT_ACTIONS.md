# الإجراءات التالية | Next Actions

**آخر تحديث:** 2026-06-26

## أولوية قصوى

1. **توسيع سجل الادعاءات والأدلة**: عدد الإدخالات 59 بينما `data/claims.json` يحتوي 25 ادعاء فقط؛ أضف Claim IDs لكل رقم تكلفة/ذاكرة/زمن مهم.
2. **مراجعة المصادر Tier 3**: راجع الأرقام الحديثة جداً، ووسم غير المؤكد بـ `[⚠️ غير متحقق]`.
3. **إضافة فئة Rejected/Pending**: أنشئ إدخالات قصيرة لمنهجيات منتشرة بلا دليل قوي، مع سبب الرفض أو التعليق.
4. **تدقيق الإدخالات الأساسية العشرة**: LLM.int8, GPTQ, AWQ, SmoothQuant, Speculative Decoding, Continuous Batching, PagedAttention, LoRA, QLoRA, Prompt Caching؛ تأكد أن كل رقم له مصدر مباشر في `CLAIMS.md`.

## أولوية عالية

5. **تحديث `EVIDENCE_LEDGER.md` آلياً/يدوياً** ليتطابق مع `data/evidence.json`.
6. **إضافة تحقق CI**: سكربت يفشل إذا وُجد إدخال بلا front matter أو بلا قسم عربي/إنجليزي.
7. **تحديث `assets/tree-visual.svg`** ليعكس 7 فئات و25 فئة فرعية.
8. **استكمال مصطلحات المعجم** من الإدخالات الحديثة: FP8, MoE routing, semantic cache, budget-aware agents.

## أولوية متوسطة

9. تحسين المقارنات العملية: `quantization-methods.md`, `inference-engines.md`, `rag-cost-vs-long-context-cost.md`.
10. إضافة أمثلة كود صغيرة في playbooks بدون مفاتيح أو أسرار.
11. فصل المصادر الآلية عن المصادر المعتمدة نهائياً: `data/sources_auto.json` و`data/sources.json`.

## أمر مفيد للمتابعة

```bash
python3 scripts/sync_metadata.py && git status --short
```
