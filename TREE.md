# 🌳 شجرة تصنيفات المكتبة | Library Classification Tree

> آخر تحديث: 2026-06-26 | الجلسة: session-005 | الإصدار: 2.0

## ⚠️ إعادة هيكلة التصنيف (v2.0)

تم إعادة تصميم التصنيف بالكامل بناءً على أطر علمية حديثة (Spheron 2026, TrueFoundry 2026, Mirantis 2026, Gartner 2026). التصنيف القديم (10 فئات عامة) مُحتفظ به في `library-v1/` كمرجع. التفاصيل في `TAXONOMY_REDESIGN.md`.

## الشجرة الكاملة (v2.0)

```
مكتبة تكلفة الذكاء الاصطناعي · AI Cost Library
│
├── 1. تحسين النموذج | Model Optimization ─── "ماذا نشغّل؟"
│   ├── 1.1 التكميم | Quantization (5 إدخالات)
│   │   ├── 📘 LLM.int8() ⭐⭐⭐⭐
│   │   ├── 📘 GPTQ ⭐⭐⭐⭐
│   │   ├── 📘 AWQ ⭐⭐⭐⭐
│   │   ├── 📘 SmoothQuant ⭐⭐⭐
│   │   └── 📘 FP8 Quantization ⭐⭐⭐⭐
│   ├── 1.2 ضغط النموذج | Compression (2 إدخالات)
│   │   ├── 📘 Knowledge Distillation ⭐⭐⭐⭐
│   │   └── 🧪 ShortGPT ⭐⭐
│   ├── 1.3 اختيار النموذج المناسب | Right-Sizing (2 إدخالات)
│   │   ├── 📘 Model Routing (RouteLLM) ⭐⭐⭐
│   │   └── 📐 Chinchilla Scaling Laws ⭐⭐⭐
│   └── 1.4 البنية الفعّالة | Efficient Architecture (2 إدخالات)
│       ├── 📘 LayerSkip ⭐⭐⭐
│       └── 🧪 Mixture-of-Depths ⭐⭐
│
├── 2. تحسين التشغيل | Runtime Optimization ─── "كيف نشغّله؟"
│   ├── 2.1 التجميع | Batching (1 إدخال)
│   │   └── 📘 Continuous Batching ⭐⭐⭐⭐
│   ├── 2.2 فك الترميز | Decoding (1 إدخال)
│   │   └── 📘 Speculative Decoding ⭐⭐⭐
│   ├── 2.3 ذاكرة KV | KV Cache (3 إدخالات)
│   │   ├── 📘 PagedAttention ⭐⭐⭐⭐
│   │   ├── 📘 FlashAttention ⭐⭐⭐⭐
│   │   └── 📘 RadixAttention ⭐⭐⭐
│   ├── 2.4 التخزين المؤقت | Caching (2 إدخالات)
│   │   ├── 📘 Prompt Caching ⭐⭐⭐⭐
│   │   └── 📘 Semantic Caching ⭐⭐⭐
│   └── 2.5 محركات الاستدلال | Serving Engines
│       └── → مقارنة في comparisons/inference-engines.md
│
├── 3. تحسين التدريب | Training Optimization ─── "كيف نبني؟"
│   ├── 3.1 الضبط الموفّر | PEFT (2 إدخالات)
│   │   ├── 📘 LoRA ⭐⭐⭐⭐
│   │   └── 📘 QLoRA ⭐⭐⭐⭐
│   ├── 3.2 التدريب الموزّع | Distributed Training ⏳
│   ├── 3.3 البيانات الاصطناعية | Synthetic Data ⏳
│   └── 3.4 التدريب المختلط | Mixed Precision ⏳
│
├── 4. البنية التحتية | Infrastructure ─── "على ماذا نشغّل؟"
│   ├── 4.1 المسرّعات | Accelerators ⏳
│   ├── 4.2 استراتيجيات النشر | Deployment ⏳
│   └── 4.3 كفاءة الطاقة | Energy Efficiency ⏳
│
├── 5. اقتصاديات الوكلاء | Agentic Economics 🆕 ─── "التحدي الأحدث"
│   ├── 5.1 مضاعف التوكن | Token Multiplier ⏳
│   ├── 5.2 تحسين السلاسل | Chain Optimization ⏳
│   └── 5.3 تكلفة الأدوات | Tool & RAG Costs ⏳
│
├── 6. الحوكمة المالية | AI FinOps 🆕 ─── "كيف نتحكم؟"
│   ├── 6.1 المراقبة | Observability ⏳
│   ├── 6.2 الميزانية | Budgeting ⏳
│   └── 6.3 تقييم العائد | ROI Assessment ⏳
│
└── 7. اقتصاديات السوق | Market Economics 🆕 ─── "السياق"
    ├── 7.1 اتجاهات الأسعار | Pricing Trends ⏳
    ├── 7.2 مقارنة المزودين | Providers ⏳
    └── 7.3 مفارقة الاستدلال | Inference Paradox ⏳
```

## الإحصائيات

| المقياس | العدد |
|---------|-------|
| فئات رئيسية (L1) | 7 |
| فئات فرعية (L2) | 21 |
| فئات فرعية نشطة | 12 |
| فئات فرعية قيد البناء | 9 |
| 📘 إدخالات عملية | 16 |
| 🧪 إدخالات ناشئة | 3 |
| 📐 إدخالات نظرية | 1 |
| إجمالي الإدخالات | 20 |

## الرموز

| الرمز | المعنى |
|-------|--------|
| 📘 | عملية (مُنشَرة ومُختبرة) |
| 🧪 | ناشئة (واعدة لكن غير مُثبتة إنتاجياً) |
| 📐 | نظرية (بحث أكاديمي بدون نشر إنتاجي) |
| ⭐⭐⭐⭐ | إنتاج مُثبَت — جميع البوابات الأربع |
| ⭐⭐⭐ | مُنشَر أو مُتحقق |
| ⭐⭐ | نموذج أولي |
| ⏳ | قيد البناء |
| 🆕 | فئة جديدة في الإصدار 2.0 |
