# 🌳 شجرة التصنيفات | Library Classification Tree

> آخر تحديث: 2026-06-26 | الإصدار: 2.0 | **44 إدخال مُقيَّم**

```
مكتبة تكلفة الذكاء الاصطناعي · AI Cost Library (44 إدخال)
│
├── 1. تحسين النموذج | Model Optimization (14 إدخال)
│   ├── 1.1 التكميم | Quantization (5)
│   │   ├── 📘 LLM.int8() ⭐⭐⭐⭐
│   │   ├── 📘 GPTQ ⭐⭐⭐⭐
│   │   ├── 📘 AWQ ⭐⭐⭐⭐
│   │   ├── 📘 SmoothQuant ⭐⭐⭐
│   │   └── 📘 FP8 Quantization ⭐⭐⭐⭐
│   ├── 1.2 الضغط | Compression (2)
│   │   ├── 📘 Knowledge Distillation ⭐⭐⭐⭐
│   │   └── 🧪 ShortGPT ⭐⭐
│   ├── 1.3 اختيار النموذج | Right-Sizing (2)
│   │   ├── 📘 Model Routing (RouteLLM) ⭐⭐⭐
│   │   └── 📐 Chinchilla Scaling Laws ⭐⭐⭐
│   └── 1.4 البنية الفعّالة | Efficient Architecture (5)
│       ├── 📘 MoE Economics (DeepSeek-V3) ⭐⭐⭐⭐ 🆕
│       ├── 📘 LayerSkip ⭐⭐⭐
│       ├── 🧪 Mixture-of-Depths ⭐⭐
│       └── 📐 Architecture-Aware Scaling Laws ⭐⭐⭐
│
├── 2. تحسين التشغيل | Runtime Optimization (12 إدخال)
│   ├── 2.1 التجميع | Batching (1)
│   │   └── 📘 Continuous Batching ⭐⭐⭐⭐
│   ├── 2.2 فك الترميز | Decoding (3)
│   │   ├── 📘 Speculative Decoding ⭐⭐⭐
│   │   ├── 📘 EAGLE-3 ⭐⭐⭐ 🆕 (PayPal production)
│   │   └── 🧪 MoE-Spec ⭐⭐
│   ├── 2.3 ذاكرة KV | KV Cache (4)
│   │   ├── 📘 PagedAttention ⭐⭐⭐⭐
│   │   ├── 📘 FlashAttention ⭐⭐⭐⭐
│   │   ├── 📘 RadixAttention ⭐⭐⭐
│   │   └── 🧪 KV Cache Compression (4 أبحاث) ⭐⭐
│   ├── 2.4 التخزين المؤقت | Caching (2)
│   │   ├── 📘 Prompt Caching ⭐⭐⭐⭐
│   │   └── 📘 Semantic Caching ⭐⭐⭐
│   ├── 2.5 محركات الاستدلال → comparisons/inference-engines.md
│   └── 2.6 حوسبة وقت الاستدلال | Inference-Time Compute (1) 🆕
│       └── 📘 Inference-Time Compute Economics ⭐⭐⭐
│
├── 3. تحسين التدريب | Training Optimization (5 إدخالات)
│   ├── 📘 LoRA ⭐⭐⭐⭐ · 📘 QLoRA ⭐⭐⭐⭐
│   ├── 📘 DeepSpeed ZeRO + FSDP ⭐⭐⭐⭐
│   ├── 📘 Synthetic Data ⭐⭐⭐
│   └── 📘 Mixed Precision Training ⭐⭐⭐⭐
│
├── 4. البنية التحتية | Infrastructure (5 إدخالات)
│   ├── 🧪 CPU-GPU Collaborative ⭐⭐ · 🧪 Heterogeneous HW ⭐⭐ · 🧪 Decentralized ⭐⭐
│   ├── 📘 Local vs Cloud (IPW) ⭐⭐⭐
│   └── 🧪 Babbling Suppression ⭐⭐
│
├── 5. اقتصاديات الوكلاء | Agentic Economics (5 إدخالات) 🆕
│   ├── 📘 Agent Token Multiplier ⭐⭐⭐ (5-30× مضاعف)
│   ├── 🧪 AgentDiet ⭐⭐ (FSE 2026) · 🧪 SkillReducer ⭐⭐
│   ├── 🧪 Context Compression ⭐⭐ (5 تقنيات) 🆕
│   └── 📘 RAG Cost Optimization ⭐⭐⭐
│
├── 6. الحوكمة المالية | AI FinOps (3 إدخالات) 🆕
│   ├── 📘 AI FinOps Observability ⭐⭐⭐
│   ├── 📘 Agent Budget Enforcement ⭐⭐⭐
│   └── 📘 Cost per Successful Task ⭐⭐⭐
│
└── 7. اقتصاديات السوق | Market Economics (2 إدخالات) 🆕
    ├── 📐 Price of Progress ⭐⭐⭐ (5-10× سنوياً)
    └── 📘 LLM API Pricing June 2026 ⭐⭐⭐
```

## إحصائيات

| | العدد |
|---|------|
| 📘 عملية | 26 |
| 🧪 ناشئة | 14 |
| 📐 نظرية | 3 |
| **الإجمالي** | **44** |
| 🔬 أبحاث مُراجعة | **45+** |
| 🏆 تقييمات (12 بُعد) | **44 × 12 = 528** |
