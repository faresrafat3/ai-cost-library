# الإجراءات التالية | Next Actions

> **بعد إعادة هيكلة التصنيف v2.0**

## أولوية قصوى — ملء الفجوات الحرجة
1. **اقتصاديات الوكلاء (الفئة 5):** أضف 3 إدخالات:
   - مضاعف التوكن الوكيلي (5-30× — Gartner 2026)
   - تحسين سلاسل الوكلاء (تقليل خطوات، تخزين مؤقت بين الخطوات)
   - RAG Cost vs Long Context Cost (نقل من المقارنات + تعميق)

2. **البنية التحتية (الفئة 4):** أضف إدخالين:
   - مقارنة GPU للاستدلال (H100 vs H200 vs B200 vs A100)
   - سحابي vs محلي vs هجين (بأرقام نقطة التعادل)

3. **الحوكمة المالية (الفئة 6):** أضف إدخالاً:
   - AI FinOps: المراقبة والإسناد (أدوات: Vantage, Datadog AI Costs, CloudZero)

## أولوية عالية
4. أضف إدخالات ناقصة في التدريب: DeepSpeed ZeRO, FSDP, Mixed Precision Training
5. أضف Mixture-of-Experts (MoE) في البنية الفعّالة — DeepSeek V3 كدراسة حالة
6. أضف مقارنة Cloud API Pricing (OpenAI vs Anthropic vs Google vs open-source)
7. حدّث DECISION_MATRIX.md بالكامل ليعكس التصنيف الجديد

## أولوية متوسطة
8. أضف playbooks جديدة: "How to Build a Model Routing Pipeline", "Agent Cost Governance"
9. أضف IndexCache (2026) — تقنية ناشئة
10. أضف Attention Residuals (Moonshot AI) — تقنية ناشئة
11. أنشئ سكربت تحقق يتأكد من اتساق الروابط بعد إعادة الهيكلة
12. حدّث data/tree.json ليعكس التصنيف الجديد بالكامل

## أولوية منخفضة
13. أضف فئة "Rejected" — تقنيات ادّعت تقليل تكلفة بدون أساس
14. أضف اقتصاديات السوق: مفارقة الاستدلال (280× انخفاض سعر + 320% ارتفاع إنفاق)
15. نظّف library-v1/ (احذفها بعد التأكد من نقل كل شيء)

## قاعدة قبل أي دفع جديد
حدّث: `README.md`, `TREE.md`, `GLOSSARY.md`, `RESEARCH_LOG.md`, `AGENT_STATE.md`, `NEXT_ACTIONS.md`, `SESSION_LOG.md`, `CONTINUATION_PROTOCOL.md`, وملفات JSON في `data/`.
