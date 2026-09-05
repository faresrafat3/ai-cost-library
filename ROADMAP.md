# خارطة الطريق | Roadmap

> **آخر تحديث: 2026-09-04 (round 79)** + **round 98: mark "Automated Scoring" as done**
>
> **ملاحظة عن drift (2026-09-04)**: المرحلة 2 كانت موصوفة بأنها "الحالية 🔄" في 2026-06-26، لكن **جميع بنودها الـ 6 مكتملة فعلياً** في 2026-09-04. هذا drift حقيقي — checkbox `[ ]` يقول "غير مكتمل" لكن الملفات موجودة. تم إصلاحها في هذه الجولة بفحص كل بند ضد الـ filesystem.
>
> **بنود المرحلة 2 التي تم التحقق منها (round 79):**
> - LLM.int8 ✓ (`library/01-model-optimization/quantization/llm-int8.md`)
> - SmoothQuant ✓ (`library/01-model-optimization/quantization/smoothquant.md`)
> - LoRA ✓ (`library/03-training-optimization/parameter-efficient/lora.md`)
> - SLoRA/Multi-LoRA ✓ (`library/03-training-optimization/parameter-efficient/multi-lora-serving.md`)
> - PagedAttention ✓ (`library/02-runtime-optimization/kv-cache/paged-attention.md`)
> - RadixAttention ✓ (`library/02-runtime-optimization/kv-cache/radix-attention.md`)
> - MoE Serving ✓ (`llama4-moe-economics.md`, `moe-quantization.md`, `moe-speculative-decoding.md`)
> - Early Exit ✓ (`library/01-model-optimization/efficient-architecture/layer-skip.md`)
> - Token Pruning ✓ (`library/01-model-optimization/compression/short-gpt.md`)
> - Speculative Sampling ✓ (`library/02-runtime-optimization/decoding/speculative-decoding.md` + `eagle3-` + `moe-`)
> - 5 أدلة تطبيقية ✓ (5 ملفات في `playbooks/`: reduce-llm-api-cost, reduce-gpu-memory, fine-tune-on-low-budget, deploy-cheaper-inference, choose-quantization-method)
> - 6 صفحات مقارنة ✓ (6 ملفات في `comparisons/`: quantization-methods, inference-engines, rag-cost-vs-long-context-cost, speculative-decoding-vs-batching, pruning-vs-distillation, lora-vs-qlora-vs-full-finetuning) — كان ROADMAP يقول 5، لكن فعلاً 6
> - مصفوفة اتخاذ القرار ✓ (`DECISION_MATRIX.md`)
>
> **Drift note (2026-09-04)**: Phase 2 was marked "current 🔄" in 2026-06-26, but **all 6 of its items are now actually completed** as of 2026-09-04. This is real drift — checkboxes `[ ]` said "incomplete" but the files exist. Fixed in this round by checking each item against the filesystem.
>
> **Items verified (round 79):** [list above]
>
> Two of the items were slightly under-claimed in the original ROADMAP:
> - "5 صفحات مقارنة تفصيلية" → actually 6 (extra: pruning-vs-distillation)
> - "أدلة تطبيقية" mentioned 4 in roadmap but playbooks/ has 5

## 📅 المرحلة 1 — البنية الأساسية (مكتملة ✅)
- [x] إنشاء هيكل المستودع والملفات الأساسية
- [x] كتابة القوالب والمنهجيات
- [x] 6 إدخالات تطبيقية أولية (GPTQ, AWQ, QLoRA, Speculative Decoding, Continuous Batching, Prompt Caching)
- [x] دليل تطبيقي أولي (Reduce LLM API Cost)
- [x] المعجم العلمي الثنائي اللغة

## 📅 المرحلة 2 — التوسع في المحتوى (مكتملة ✅ بعد round 79)
- [x] إدخالات تطبيقية: LLM.int8, SmoothQuant, LoRA, Multi-LoRA, PagedAttention, RadixAttention
- [x] إدخالات ناشئة: Mixture of Experts (MoE) Serving, Early Exit (LayerSkip), Token Pruning (ShortGPT), Speculative Sampling
- [x] إدخالات نظرية: Neural Architecture Search for Cost (Arch Scaling ICLR26), Dynamic Compute Allocation (MoD)
- [x] 5+ أدلة تطبيقية: Deploy Cheaper Inference, Fine-tune on Low Budget, Reduce GPU Memory, Choose Quantization Method, Reduce LLM API Cost
- [x] 6 صفحات مقارنة (5 كانت في ROADMAP، زادت 1: pruning-vs-distillation)
- [x] مصفوفة اتخاذ القرار الكاملة (DECISION_MATRIX.md)

## 📅 المرحلة 3 — التحليل المتقدم (المقبلة 🔜)
- [ ] تحليلات التكلفة عبر السحابة (Cloud Cost Analytics)
- [ ] نماذج التنبؤ بالتكلفة (Cost Prediction Models)
- [ ] تكامل مع MLPerf Benchmarks
- [ ] دراسات حالة من شركات حقيقية
- [x] ~~نظام التقييم التلقائي (Automated Scoring)~~ — **مُنجَز**: `scripts/generate_fair_ranking.py` (v2.0 Calibrated MCDA, 9 axes)، `data/fair_ranking.json` (60 إدخال مُقيَّم + 1 pending مُتجاوز)، `RANKING.md` (الجدول + المنهجية)، `SCORING_SYSTEM.md` (12 بُعد). **Drift note (round 98)**: هذا البند كان مذكوراً كـ `[ ]` لكن الـ implementation الفعلي مكتمل ومُختبَر.

## 📅 المرحلة 4 — النظام البيئي (طويلة المدى 🚀)
- [ ] واجهة برمجة تطبيقات للاستعلام (Query API)
- [ ] أدوات حساب التكلفة التفاعلية (Interactive Cost Calculators)
- [ ] تكامل مع أدوات المراقبة (Monitoring Integrations)
- [ ] نسخ متعددة للغات إضافية
- [ ] تقارير سنوية لتوجهات تكلفة الذكاء الاصطناعي
