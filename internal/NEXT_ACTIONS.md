# الإجراءات التالية | Next Actions

**آخر تحديث:** 2026-06-26 (Session 5 — أوائل الـ ACL Polish)
**مراجعة Round 68:** 2026-09-04 (التحديثات الحالية: 61 إدخال، 29 ادعاء، 217 مصدر، 59 مصطلح، 1 pending)

> **ملاحظة Round 68:** الأولويات أدناه مرّت بمرور الوقت. الحالة الحالية:
> - الأولوية 1 (توسيع الادعاءات): **انخفضت** — حالياً 29 ادعاء لـ 61 إدخال (نسبة ~48%، أفضل من 25/59 = 42% قبل ذلك).
> - الأولوية 3 (إضافة Rejected/Pending): **بدأت** — يوجد 1 pending (`entry-model-router-cascade`)؛ لا يوجد rejected بعد.
> - الأولوية 6 (CI check): **مُنجزة** — `validate.yml` يتحقق من JSON و front matter.
> - الأولوية 11 (فصل المصادر): **لم تبدأ** — لا يزال في `sources.json` الموحَّد.

## أولوية قصوى

1. **توسيع سجل الادعاءات والأدلة**: عدد الإدخالات 61 بينما `data/claims.json` يحتوي 29 ادعاء فقط (نسبة ~48%)؛ أضف Claim IDs لكل رقم تكلفة/ذاكرة/زمن مهم.
2. **مراجعة المصادر Tier 3**: راجع الأرقام الحديثة جداً، ووسم غير المؤكد بـ `[⚠️ غير متحقق]`.
3. **إضافة إدخالات Rejected**: لا يوجد حالياً أي rejected، رغم أن `AGENT_STATE.md` ينص على دعمها. أضف إدخالاً قصيراً لمنهجية منتشرة بلا دليل قوي (مثل: "Model Merging عبر SLERP لدمج نماذج كبيرة بلا fine-tune" — ادعاء شائع بلا ورقة قابلة للتكرار).
4. **تدقيق الإدخالات الأساسية العشرة**: LLM.int8, GPTQ, AWQ, SmoothQuant, Speculative Decoding, Continuous Batching, PagedAttention, LoRA, QLoRA, Prompt Caching؛ تأكد أن كل رقم له مصدر مباشر في `CLAIMS.md`.

## أولوية عالية

5. **تحديث `EVIDENCE_LEDGER.md` آلياً/يدوياً** ليتطابق مع `data/evidence.json`.
6. ~~**إضافة تحقق CI**~~: **مُنجزة** (`.github/workflows/validate.yml` يفحص JSON + front matter).
7. **تحديث `assets/tree-visual.svg`** ليعكس 7 فئات و25 فئة فرعية و61 إدخال.
8. **استكمال مصطلحات المعجم** من الإدخالات الحديثة: FP8, MoE routing, semantic cache, budget-aware agents, sleep-time compute, deepconf, model router cascade.

## أولوية متوسطة

9. تحسين المقارنات العملية: `quantization-methods.md`, `inference-engines.md`, `rag-cost-vs-long-context-cost.md`.
10. إضافة أمثلة كود صغيرة في playbooks بدون مفاتيح أو أسرار.
11. فصل المصادر الآلية عن المصادر المعتمدة نهائياً: `data/sources_auto.json` و`data/sources.json`.

## أمر مفيد للمتابعة

```bash
python3 scripts/sync_metadata.py && git status --short
```

12. توسيع فئة `inference-time-compute/` بإدخالات مترابطة: Sleep-time Compute, DeepConf early stopping, Kinetics, Inference-time distillation.
13. **إضافة 2 rejected entries** لاختبار بوابات الرفض (تم تحديد البوابات في `NO_HYPE_POLICY.md`، لم تُستخدم بعد).
