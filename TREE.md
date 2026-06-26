# 🌳 شجرة تصنيفات المكتبة | Library Classification Tree

> آخر تحديث: 2026-06-26 | الجلسة: session-005

## الشجرة الكاملة

```
مكتبة تكلفة الذكاء الاصطناعي · AI Cost Library
│
├── 📦 ضغط النماذج | Model Compression
│   ├── 🔢 التكميم | Quantization
│   │   ├── 📘 LLM.int8() ⭐⭐⭐⭐
│   │   ├── 📘 GPTQ ⭐⭐⭐⭐
│   │   ├── 📘 AWQ ⭐⭐⭐⭐
│   │   ├── 📘 SmoothQuant ⭐⭐⭐
│   │   └── 📘 FP8 Quantization ⭐⭐⭐⭐ [جديد]
│   ├── ✂️ القصّ | Pruning
│   │   └── 🧪 ShortGPT ⭐⭐
│   └── 🎓 استخلاص المعرفة | Distillation
│       └── 📘 Knowledge Distillation ⭐⭐⭐⭐
│
├── ⚡ الاستدلال الفعّال | Efficient Inference
│   ├── 📦 التجميع | Batching
│   │   └── 📘 Continuous Batching ⭐⭐⭐⭐
│   ├── 🔮 فك الترميز | Decoding
│   │   └── 📘 Speculative Decoding ⭐⭐⭐
│   ├── 💾 ذاكرة KV المؤقتة | KV Cache
│   │   ├── 📘 PagedAttention ⭐⭐⭐⭐
│   │   ├── 📘 RadixAttention ⭐⭐⭐
│   │   └── 📘 FlashAttention ⭐⭐⭐⭐
│   ├── 🚪 الإنهاء المبكر | Early Exit
│   │   └── 📘 LayerSkip ⭐⭐⭐
│   └── 🖥️ الخدمة | Serving
│       └── (مقارنة محركات الاستدلال في comparisons/)
│
├── 🏋️ التدريب الفعّال | Efficient Training
│   ├── 🎯 الضبط الموفّر للمعاملات | Parameter-Efficient Fine-Tuning
│   │   ├── 📘 LoRA ⭐⭐⭐⭐
│   │   └── 📘 QLoRA ⭐⭐⭐⭐
│   ├── ⚖️ التخصيص الديناميكي للحوسبة | Compute Allocation
│   │   └── 🧪 Mixture-of-Depths ⭐⭐
│   └── 📐 التدريب الأمثل حوسبياً | Compute-Optimal Training [جديد]
│       └── 📐 Chinchilla Scaling Laws ⭐⭐⭐
│
├── 🔧 العتاد والأنظمة | Hardware and Systems
│   └── (قيد الإنشاء)
│
├── 📊 كفاءة البيانات | Data Efficiency
│   └── (قيد الإنشاء)
│
├── 🔀 اختيار وتوجيه النماذج | Model Selection and Routing
│   └── 🎯 توجيه النماذج | Model Routing [جديد]
│       └── 📘 Intelligent Model Routing (RouteLLM) ⭐⭐⭐
│
├── 📈 العمليات والمراقبة | Operations and Monitoring
│   └── (قيد الإنشاء)
│
├── 💰 تحسين تكلفة التوكن والموجِّهات | Token and Prompt Cost
│   ├── 🗄️ التخزين المؤقت للموجِّهات | Prompt Caching
│   │   └── 📘 Prompt Caching ⭐⭐⭐⭐
│   └── 🧠 التخزين المؤقت الدلالي | Semantic Caching [جديد]
│       └── 📘 Semantic Caching ⭐⭐⭐
│
├── 🔍 كفاءة الاسترجاع والسياق | Retrieval and Context Efficiency
│   └── (قيد الإنشاء)
│
└── 🌱 الطاقة والاستدامة | Energy and Sustainability
    └── (قيد الإنشاء)
```

## الإحصائيات

| المقياس | العدد |
|---------|-------|
| فئات كبرى (L1) | 10 |
| فئات فرعية (L2) | 17 |
| إدخالات عملية (📘) | 16 |
| إدخالات ناشئة (🧪) | 3 |
| إدخالات نظرية (📐) | 1 |
| إجمالي الإدخالات | 20 |

## التغييرات في الجلسة 5

- أُضيف: FP8 Quantization (📘 ⭐⭐⭐⭐) → model-compression/quantization/
- أُضيف: Intelligent Model Routing (📘 ⭐⭐⭐) → model-selection-and-routing/model-routing/
- أُضيف: Semantic Caching (📘 ⭐⭐⭐) → token-and-prompt-cost/semantic-caching/
- أُضيف: Chinchilla Scaling Laws (📐 ⭐⭐⭐) → efficient-training/compute-optimal/
- أُضيف: مقارنة محركات الاستدلال → comparisons/inference-engines.md
- أُنشئت فئات فرعية جديدة: model-routing, semantic-caching, compute-optimal
