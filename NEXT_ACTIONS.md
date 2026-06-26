# الإجراءات التالية | Next Actions

## أولوية عالية
1. راجع كل ملف إدخال في `library/` وعدّل قسم **Evidence Gates** بحيث يحتوي كل باب على مصدر مباشر أو يوسم بـ `[⚠️ غير متحقق]`.
2. أضف إدخالين ناشئين على الأقل، مثل: Mixture-of-Depths، Early Exit/Layer Skipping، أو KV Cache Compression، بعد بحث مباشر.
3. أضف إدخالاً نظرياً واحداً على الأقل مع حدود واضحة.
4. املأ فئات Pruning وDistillation بإدخالات عملية/ناشئة موثقة.

## أولوية متوسطة
5. أضف بيانات MLPerf أو HELM عند توفرها لتدعيم المقارنات.
6. أنشئ سكربت تحقق يقرأ JSON ويتأكد من اتساق العدادات والروابط.
7. حسّن المعجم بإضافة المصطلحات الجديدة المستخرجة من الإدخالات.

## قاعدة قبل أي دفع جديد
حدّث دائماً: `README.md`, `TREE.md`, `GLOSSARY.md`, `RESEARCH_LOG.md`, `AGENT_STATE.md`, `NEXT_ACTIONS.md`, `SESSION_LOG.md`, `CONTINUATION_PROTOCOL.md`, وملفات JSON في `data/`.
