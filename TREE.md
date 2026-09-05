# 🌳 شجرة التصنيفات | Library Tree — 60 Ranked Entries (+1 Pending)

> آخر تحديث: 2026-09-04 (تحديث Round 86) | **60 إدخال مُقيَّم + 1 قيد المراجعة** | v2.0
>
> **ملاحظة الصيانة (2026-09-04, round 86):** الأرقام في هذا الملف كانت مكتوبة يدوياً في 2026-06-26 لـ 55 إدخالاً، ثم نمت إلى 61 إدخالاً في `data/entries.json` دون تحديث `TREE.md`. الأرقام عالية المستوى (header + جدول الإحصائيات) تم تحديثها في round 69. الأرقام تحت كل فئة في الشجرة كانت قديمة بأرقام مثل 52 بدل 61 — تم التحقق منها وتحديثها في round 86 ضد الـ filesystem. المصدر الموثوق هو `data/categories.json` (01=19، 02=14، 03=6، 04=10، 05=7، 06=3، 07=2؛ المجموع=61). السكربت `scripts/sync_metadata.py` يولّد `data/tree.json` لكن لا يولّد `TREE.md` — التحديث اليدوي مطلوب.

```
مكتبة تكلفة الذكاء الاصطناعي (61 إدخال | 40,000+ كلمة | 217 مصادر)
│
├── 1. تحسين النموذج (19 إدخال)
│   ├── التكميم (6): LLM.int8⭐⭐⭐⭐ · GPTQ⭐⭐⭐⭐ · AWQ⭐⭐⭐⭐ · SmoothQuant⭐⭐⭐ · FP8⭐⭐⭐⭐ · MoE Quantization⭐⭐
│   ├── الضغط (3): Distillation⭐⭐⭐⭐ · Model Merging⭐⭐⭐ · ShortGPT⭐⭐
│   ├── اختيار النموذج (2): Model Routing⭐⭐⭐ · Chinchilla⭐⭐⭐
│   └── البنية الفعّالة (8): MoE Economics⭐⭐⭐⭐ · Llama 4 MoE⭐⭐⭐⭐🆕 · DeepSeek V4⭐⭐⭐⭐ · Qwen3⭐⭐⭐⭐
│       LayerSkip⭐⭐⭐ · MoD⭐⭐ · Arch Scaling(ICLR26)⭐⭐⭐ · Mamba-3(ICLR26)⭐⭐
│
├── 2. تحسين التشغيل (14 إدخال)
│   ├── التجميع (1): Continuous Batching⭐⭐⭐⭐
│   ├── فك الترميز (3): Speculative⭐⭐⭐ · EAGLE-3⭐⭐⭐ · MoE-Spec⭐⭐
│   ├── ذاكرة KV (5): PagedAttention⭐⭐⭐⭐ · FlashAttention⭐⭐⭐⭐
│   │   RadixAttention⭐⭐⭐ · KV Compression(4 أبحاث)⭐⭐ · Sparse/Linear Attention⭐⭐
│   ├── التخزين المؤقت (3): Prompt Caching⭐⭐⭐⭐ · Semantic Caching⭐⭐⭐ · Batch API + Structured Output⭐⭐⭐⭐
│   ├── محركات → comparisons/inference-engines.md (0 entries)
│   └── حوسبة الاستدلال (2): Inference-Time Compute⭐⭐⭐ · Sleep-time Compute⭐⭐
│
├── 3. تحسين التدريب (6 إدخالات)
│   ├── PEFT (3): LoRA⭐⭐⭐⭐ · QLoRA⭐⭐⭐⭐ · Multi-LoRA⭐⭐⭐
│   ├── التدريب الموزّع (1): DeepSpeed/FSDP⭐⭐⭐⭐
│   ├── البيانات الاصطناعية (1): Synthetic Data⭐⭐⭐
│   └── الدقة المختلطة (1): Mixed Precision⭐⭐⭐⭐
│
├── 4. البنية التحتية (10 إدخالات)
│   ├── المسرّعات (5): CPU-GPU⭐⭐ · Heterogeneous⭐⭐ · Decentralized⭐⭐
│   │   Custom AI Chips⭐⭐⭐ · GPU Economics 2026(H100/B200/H200)⭐⭐⭐
│   ├── النشر (3): Local vs Cloud(IPW)⭐⭐⭐ · Self-Host Breakeven⭐⭐⭐ · Local GGUF⭐⭐⭐⭐
│   └── الطاقة (2): Babbling Suppression⭐⭐ · GPU DVFS⭐⭐
│
├── 5. اقتصاديات الوكلاء (7 إدخالات)
│   ├── Model Router Cascade (قيد المراجعة ⏳)
│   ├── المضاعف (1): Agent Token Multiplier⭐⭐⭐
│   ├── تحسين السلاسل (4): AgentDiet(FSE26)⭐⭐ · SkillReducer⭐⭐
│   │   Budget-Aware Agents (BAGEN)⭐⭐ · Context Compression(5 تقنيات)⭐⭐
│   └── تكلفة الأدوات (1): RAG Cost⭐⭐⭐
│
├── 6. الحوكمة المالية (3 إدخالات)
│   ├── المراقبة (1): AI FinOps⭐⭐⭐
│   ├── الميزانية (1): Budget Enforcement⭐⭐⭐
│   └── العائد (1): Cost per Successful Task⭐⭐⭐
│
└── 7. اقتصاديات السوق (2 إدخالات)
    ├── مفارقة الاستدلال (1): Price of Progress⭐⭐⭐
    └── مقارنة المزودين (1): API Pricing June 2026⭐⭐⭐
```

## الإحصائيات

| | العدد |
|---|------|
| 📘 عملية | 40 |
| 🧪 ناشئة | 17 |
| 📐 نظرية | 3 |
| ⏳ قيد المراجعة | 1 |
| **الإجمالي (مُقيَّم + pending)** | **61** |
| 🔬 أبحاث مُراجعة | **60+** |
| 🏆 تقييمات | **720** (60×12) |
| 📖 كلمات | **40,000+** |
| 🔗 مصادر | **217** |
| 🟢 كل الإدخالات 100+ سطر | **60/60 مُقيَّم** ✅ |
