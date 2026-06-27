# 📁 Internal Files — الملفات الداخلية

> هذا المجلد يحتوي على ملفات إدارية متعلقة بتطوير وصيانة المكتبة.
> لا تهم القارئ الخارجي لكنها ضرورية لاستمرارية العمل.

This folder contains administrative files related to the development and maintenance of the library. They are not relevant to external readers but are necessary for project continuity.

## الملفات

| File | Description |
|---|---|
| [`AGENT_STATE.md`](AGENT_STATE.md) | حالة الوكيل الحالية — نقطة استئناف الجلسات |
| [`NEXT_ACTIONS.md`](NEXT_ACTIONS.md) | الإجراءات التالية بأولوياتها |
| [`SESSION_LOG.md`](SESSION_LOG.md) | سجل الجلسات السابقة |
| [`CONTINUATION_PROTOCOL.md`](CONTINUATION_PROTOCOL.md) | بروتوكول استئناف العمل بين الجلسات |

## كيف يستأنف الوكيل الجديد العمل؟

1. اقرأ `CONTINUATION_PROTOCOL.md` للفلسفة العامة
2. اقرأ `AGENT_STATE.md` للحالة الحالية
3. اقرأ `NEXT_ACTIONS.md` للأولويات
4. شغّل `python3 ../scripts/sync_metadata.py` لتحديث الإحصائيات

> **ملاحظة**: ملف `RESEARCH_LOG.md` يبقى في الجذر لأنه يحتوي على تاريخ البحث وقد يهم القراء.
