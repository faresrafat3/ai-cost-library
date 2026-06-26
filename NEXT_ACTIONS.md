# الإجراءات التالية | Next Actions

## أولوية عالية
1. أضف إدخالات لفئات فارغة: hardware-and-systems (مثل NVIDIA Blackwell، TPU v5)، data-efficiency (مثل Synthetic Data، Data Deduplication).
2. أضف إدخالات ناشئة/نظرية إضافية: Neural Architecture Search for Efficiency، Mixture-of-Experts (MoE) cost analysis.
3. أنشئ مقارنة جديدة: Cloud API Pricing (OpenAI vs Anthropic vs Google vs open-source hosting).
4. حدّث DECISION_MATRIX.md ليشمل FP8، Model Routing، Semantic Caching، Chinchilla.
5. أنشئ playbook جديد: "How to Build a Model Routing Pipeline" (خطوات عملية).

## أولوية متوسطة
6. أضف إدخالات لفئة retrieval-and-context-efficiency (مثل RAG Cost Optimization، Context Window Management).
7. أضف إدخالات لفئة operations-and-monitoring (مثل GPU FinOps، Cost Attribution).
8. أضف إدخالات لفئة energy-and-sustainability (مثل Carbon-Aware Scheduling).
9. أضف بيانات MLPerf أو HELM لتدعيم المقارنات.
10. أنشئ سكربت تحقق يقرأ JSON ويتأكد من اتساق العدادات والروابط.

## أولوية منخفضة
11. أضف فئة "Rejected" — تقنيات ادّعت تقليل تكلفة بدون أساس علمي.
12. أضف فئة "Pending" — تقنيات واعدة بدون بحث كافٍ.
13. وسّع playbooks لتشمل: semantic-caching deployment, model routing configuration.
14. أضف IndexCache (2026) — تقنية ناشئة لإعادة استخدام فهارس الانتباه.
15. أضف Attention Residuals (Moonshot AI) — تقنية ناشئة لتقليل حوسبة التدريب 1.25×.

## قاعدة قبل أي دفع جديد
حدّث دائماً: `README.md`, `TREE.md`, `GLOSSARY.md`, `RESEARCH_LOG.md`, `AGENT_STATE.md`, `NEXT_ACTIONS.md`, `SESSION_LOG.md`, `CONTINUATION_PROTOCOL.md`, وملفات JSON في `data/`.
