# إعادة تصميم التصنيف | Taxonomy Redesign

> **الجلسة:** session-005 | **التاريخ:** 2026-06-26
> **السبب:** التصنيف القديم عام جداً ولا يعكس المشهد الحقيقي لتكاليف الذكاء الاصطناعي في 2026.

---

## لماذا التغيير؟ | Why the Change?

### المشاكل في التصنيف القديم:
1. **فئات عامة جداً** — "Hardware and Systems" و"Data Efficiency" و"Operations and Monitoring" فئات واسعة بدون تحديد واضح
2. **لا يعكس المشهد الحديث** — لا يوجد مكان واضح لتكاليف الوكلاء (Agentic AI)، أو اقتصاديات Inference-time Compute، أو AI FinOps
3. **لا يتبع إطار علمي** — التصنيف لم يُبنَ على أبعاد التكلفة الفعلية في دورة حياة الذكاء الاصطناعي

### الأساس العلمي للتصنيف الجديد:
يُبنى التصنيف الجديد على **أربع طبقات مُثبتة في الأدبيات** (Spheron 2026, TrueFoundry 2026, Mirantis 2026):

```
الطبقة 1: النموذج (Model Layer)        — ماذا نشغّل؟
الطبقة 2: التشغيل (Runtime Layer)      — كيف نشغّله؟
الطبقة 3: البنية التحتية (Infra Layer) — على ماذا نشغّله؟
الطبقة 4: الحوكمة (Governance Layer)   — كيف نتحكم في الإنفاق؟
```

بالإضافة إلى **بُعدين عرضيين**:
- **التدريب** — تكاليف بناء النماذج وضبطها
- **النظام البيئي** — تكاليف الوكلاء والتطبيقات المركبة

---

## التصنيف الجديد المقترح

```
مكتبة تكلفة الذكاء الاصطناعي
│
├── 1. تحسين النموذج | Model Optimization
│   ├── 1.1 التكميم | Quantization
│   │   ├── FP8, INT8, INT4 (GPTQ, AWQ, SmoothQuant, LLM.int8())
│   │   └── FP4/NVFP4 (ناشئ)
│   ├── 1.2 ضغط النموذج | Model Compression
│   │   ├── استخلاص المعرفة | Knowledge Distillation
│   │   ├── القصّ | Pruning (ShortGPT, structured/unstructured)
│   │   └── الدمج | Merging (ناشئ)
│   ├── 1.3 اختيار النموذج المناسب | Right-Sizing
│   │   ├── قوانين التحجيم | Scaling Laws (Chinchilla)
│   │   ├── توجيه النماذج | Model Routing (RouteLLM)
│   │   └── التوجيه المتتالي | Cascading
│   └── 1.4 بنية النموذج الفعّالة | Efficient Architecture
│       ├── مزيج الخبراء | Mixture-of-Experts (MoE)
│       ├── مزيج الأعماق | Mixture-of-Depths
│       └── الإنهاء المبكر | Early Exit (LayerSkip)
│
├── 2. تحسين التشغيل | Runtime Optimization
│   ├── 2.1 التجميع | Batching
│   │   ├── التجميع المستمر | Continuous Batching
│   │   └── التجميع الدفعي | Batch APIs
│   ├── 2.2 فك الترميز | Decoding
│   │   ├── فك الترميز التخميني | Speculative Decoding
│   │   └── الانتباه الخطي | Linear Attention (ناشئ)
│   ├── 2.3 إدارة ذاكرة KV | KV Cache Management
│   │   ├── PagedAttention / FlashAttention
│   │   ├── RadixAttention
│   │   ├── ضغط KV Cache | KV Cache Compression
│   │   └── إخراج KV Cache | KV Cache Offloading
│   ├── 2.4 التخزين المؤقت | Caching
│   │   ├── تخزين البادئات | Prompt/Prefix Caching
│   │   ├── التخزين الدلالي | Semantic Caching
│   │   └── IndexCache (ناشئ)
│   └── 2.5 محركات الاستدلال | Serving Engines
│       └── (مقارنة: vLLM, TensorRT-LLM, SGLang, TGI)
│
├── 3. تحسين التدريب | Training Optimization
│   ├── 3.1 الضبط الموفّر | Parameter-Efficient Fine-Tuning
│   │   ├── LoRA / QLoRA
│   │   └── DoRA, IA3 (ناشئ)
│   ├── 3.2 التدريب الموزّع الفعّال | Efficient Distributed Training
│   │   ├── DeepSpeed ZeRO
│   │   └── FSDP
│   ├── 3.3 البيانات الاصطناعية | Synthetic Data
│   │   └── توليد بيانات التدريب من نماذج أخرى
│   └── 3.4 تقنيات التدريب المختلط | Mixed Precision Training
│       └── BF16, FP8 Training
│
├── 4. البنية التحتية والعتاد | Infrastructure & Hardware
│   ├── 4.1 اختيار المسرّعات | Accelerator Selection
│   │   ├── GPU (H100, H200, B200)
│   │   ├── مسرّعات الاستدلال المتخصصة | Inference Chips (Groq, Cerebras, TPU)
│   │   └── مقارنة تكلفة/أداء
│   ├── 4.2 استراتيجيات النشر | Deployment Strategies
│   │   ├── سحابي vs محلي vs هجين
│   │   ├── Spot vs On-Demand
│   │   └── Serverless GPU
│   └── 4.3 كفاءة الطاقة | Energy Efficiency
│       ├── الجدولة الواعية بالكربون | Carbon-Aware Scheduling
│       └── مقاييس الكفاءة (FLOPS/Watt)
│
├── 5. اقتصاديات الوكلاء | Agentic AI Economics [جديد]
│   ├── 5.1 مضاعف التوكن الوكيلي | Agent Token Multiplier
│   │   └── 5-30× أكثر من المحادثة البسيطة (Gartner 2026)
│   ├── 5.2 تحسين سلاسل الوكلاء | Agent Chain Optimization
│   │   ├── تقليل الخطوات | Step Reduction
│   │   ├── تخزين مؤقت بين الخطوات | Inter-step Caching
│   │   └── توجيه المهام الفرعية | Sub-task Routing
│   └── 5.3 تكلفة الأدوات والاسترجاع | Tool & RAG Costs
│       ├── RAG vs سياق طويل | RAG vs Long Context
│       └── تحسين نافذة السياق | Context Window Optimization
│
├── 6. الحوكمة المالية | AI FinOps & Governance [جديد]
│   ├── 6.1 المراقبة والإسناد | Observability & Attribution
│   │   ├── تتبع التكلفة لكل مهمة | Cost-per-Task Tracking
│   │   └── أدوات AI FinOps
│   ├── 6.2 الميزانية والحدود | Budgeting & Limits
│   │   ├── حدود الإنفاق التلقائية | Automatic Spend Limits
│   │   └── الميزانية القائمة على النتائج | Outcome-Based Budgeting
│   └── 6.3 تقييم العائد | ROI Assessment
│       ├── تكلفة المهمة الناجحة | Cost per Successful Task
│       └── مقاييس القيمة المُنتَجة
│
└── 7. اقتصاديات السوق | Market Economics [جديد]
    ├── 7.1 اتجاهات أسعار التوكن | Token Pricing Trends
    │   └── 280× انخفاض في سنتين (Stanford HAI)
    ├── 7.2 مقارنة مزودي الخدمة | Provider Comparison
    │   └── OpenAI vs Anthropic vs Google vs Open-Source
    └── 7.3 مفارقة الاستدلال | Inference Paradox
        └── الأسعار تنخفض 10× لكن الإنفاق يرتفع 320%
```

---

## مقارنة التصنيف القديم vs الجديد

| القديم | المشكلة | الجديد |
|--------|---------|--------|
| Model Compression | ضيق جداً — لا يشمل اختيار النموذج أو البنية | 1. تحسين النموذج (يشمل كل ما يخص النموذج) |
| Efficient Inference | يخلط بين تقنيات مختلفة | 2. تحسين التشغيل (مُنظَّم بوضوح) |
| Efficient Training | مقبول لكن ناقص | 3. تحسين التدريب (أشمل) |
| Hardware and Systems | فارغ وعام | 4. البنية التحتية (محدد وعملي) |
| Data Efficiency | فارغ | مُدمج في 3.3 و5.3 |
| Model Selection and Routing | ضيق | مُدمج في 1.3 (جزء من تحسين النموذج) |
| Operations and Monitoring | فارغ وعام | 6. الحوكمة المالية (أكثر تحديداً) |
| Token and Prompt Cost | ضيق | مُوزَّع: 2.4 (تخزين مؤقت) + 5.3 (سياق) |
| Retrieval and Context | ضيق | مُدمج في 5.3 |
| Energy and Sustainability | فارغ | مُدمج في 4.3 |
| ❌ غير موجود | — | 5. اقتصاديات الوكلاء (حديث وحرج) |
| ❌ غير موجود | — | 7. اقتصاديات السوق (سياق ضروري) |

---

## خطة التنفيذ

### المرحلة 1: إعادة هيكلة المجلدات (هذه الجلسة)
- إنشاء الهيكل الجديد
- نقل الملفات الموجودة إلى مواقعها الجديدة
- تحديث جميع الروابط والمراجع

### المرحلة 2: ملء الفجوات (الجلسات القادمة)
- إضافة إدخالات لـ Agentic AI Economics
- إضافة إدخالات لـ AI FinOps
- إضافة إدخالات لـ Infrastructure & Hardware
- إضافة Market Economics

### المرحلة 3: التعميق (مستمر)
- إضافة إدخالات ناشئة ونظرية
- تحديث المقارنات
- إضافة playbooks جديدة
