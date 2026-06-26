# الإجراءات التالية | Next Actions

## أولوية عالية
1. أضف إدخالات نظرية (Theoretical) — مثل: Neural Architecture Search for Efficiency, Compute-Optimal Training (Chinchilla scaling), Synthetic Data for Distillation.
2. أضف إدخالات Pruning و Distillation مع بوابات أدلة مفصلة (هذه الجلسة بدأت ذلك).
3. أنشئ مقارنة جديدة: Serving Engines (vLLM vs TensorRT-LLM vs TGI vs LMDeploy).
4. أضف ملف README لكل subcategory فارغة (hardware-and-systems, data-efficiency, model-selection-routing, operations-monitoring, retrieval-context-efficiency, energy-sustainability).
5. حدّث ملف DECISION_MATRIX.md ليشمل LayerSkip, ShortGPT, Distillation, FlashAttention.

## أولوية متوسطة
6. أضف بيانات MLPerf أو HELM لتدعيم المقارنات.
7. أنشئ سكربت تحقق يقرأ JSON ويتأكد من اتساق العدادات والروابط.
8. حسّن المعجم بإضافة المصطلحات الجديدة المستخرجة من الإدخالات.

## أولوية منخفضة
9. أضف فئة "Rejected" — تقنيات ادّعت تقليل تكلفة بدون أساس علمي.
10. أضف فئة "Pending" — تقنيات واعدة بدون بحث كافٍ.
11. وسّع playbooks لتشمل:蒸馏-based deployment, early-exit configuration, FlashAttention tuning.

## قاعدة قبل أي دفع جديد
حدّث دائماً: `README.md`, `TREE.md`, `GLOSSARY.md`, `RESEARCH_LOG.md`, `AGENT_STATE.md`, `NEXT_ACTIONS.md`, `SESSION_LOG.md`, `CONTINUATION_PROTOCOL.md`, وملفات JSON في `data/`.
