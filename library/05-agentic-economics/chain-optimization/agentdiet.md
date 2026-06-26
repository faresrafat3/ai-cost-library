---
id: entry-agentdiet-001
title_ar: تقليص مسارات الوكلاء (AgentDiet)
title_en: Agent Trajectory Reduction (AgentDiet)
type: emerging
status: peer-reviewed
category: agentic-economics
subcategory: chain-optimization
tree_path: "AI Cost Library → Agentic Economics → Chain Optimization → AgentDiet"
cost_dimensions:
  - token-cost
  - inference-cost
  - compute
proof_score: "⭐⭐ نموذج أولي مُراجع | Peer-Reviewed Prototype"
sources_count: 1
created: 2026-06-26
updated: 2026-06-26
research_review:
  paper_read: true
  abstract_read: true
  full_paper_scanned: true
  decision: "يُضاف — بحث Tier 1 (FSE 2026) مع نتائج كمية واضحة"
  limitations_noted: "مُطبّق على وكيل ترميز فقط، لم يُختبر في بيئات إنتاج عامة"
---

# 🧪 تقليص مسارات الوكلاء (AgentDiet) | Agent Trajectory Reduction

> **التصنيف:** 🧪 ناشئة — مُراجعة من أقران | **الإثبات:** ⭐⭐ نموذج أولي
>
> **المسار:** المكتبة ← اقتصاديات الوكلاء ← تحسين السلاسل ← AgentDiet

---

## المحتوى العربي

### ما هو AgentDiet؟

AgentDiet — وهو نظام لتقليص مسارات الوكلاء الذكية أثناء التنفيذ عن طريق حذف المعلومات عديمة الفائدة والمكررة والمنتهية الصلاحية تلقائياً من سياق المحادثة المتراكم، دون المساس بأداء الوكيل.

### المشكلة التي يحلها

في أنظمة الوكلاء متعددة الأدوار، كل خطوة تُضيف محتوى جديداً إلى "المسار" (trajectory). بعد 10-20 خطوة، يصبح السياق ضخماً ومليئاً بـ:
- **معلومات عديمة الفائدة:** مخرجات أوامر فارغة أو رسائل خطأ لم تعد ذات صلة
- **معلومات مكررة:** نفس الكود أو النص يُعاد في خطوات متعددة
- **معلومات منتهية الصلاحية:** حالة ملف قبل تعديله لم تعد صحيحة

### كيف يعمل؟

1. **نافذة منزلقة:** عند الوصول للخطوة s، يُراجع الخطوة s-a (قبل خطوتين مثلاً).
2. **نموذج تأمل خفيف:** يستخدم نموذجاً لغوياً أرخص (LLM_reflect) لضغط المحتوى.
3. **عتبة الطول:** لا يُعالج الخطوات الأقصر من θ=500 توكن (المكسب لا يبرر التكلفة).
4. **استبدال:** إذا كان الضغط كافياً، يُستبدل المحتوى الأصلي بالنسخة المُختصرة.

### الأدلة والنتائج

| الادعاء | القيمة | المصدر | الثقة |
|---------|--------|--------|-------|
| تقليل توكنات الإدخال | 39.9%-59.7% | FSE 2026 (مُراجع) | عالية |
| تقليل التكلفة الحوسبية الإجمالية | 21.1%-35.9% | FSE 2026 (مُراجع) | عالية |
| التأثير على أداء الوكيل | -1% إلى +2% (ضمن الهامش) | FSE 2026 (مُراجع) | عالية |
| تكلفة إضافية لنموذج التأمل | 5.2%-14.8% | FSE 2026 | عالية |

**تفاصيل التقييم:**
- المعايير: SWE-bench Verified + Multi-SWE-bench Flash
- النماذج: Claude 4 Sonnet + Gemini 2.5 Pro
- نوع المهام: إصلاح أخطاء برمجية في مستودعات حقيقية

### لماذا ⭐⭐ وليس أعلى؟

- ✅ **بوابة 1 (مبني):** نعم — كود ونتائج منشورة
- ✅ **بوابة 2 (مُختبر):** نعم — معايير أكاديمية مُراجعة من أقران (FSE 2026)
- ❌ **بوابة 3 (مُنشَر):** لا — لم يُثبت في بيئة إنتاج حقيقية
- ❌ **بوابة 4 (وفَّر):** لا — لا توجد أرقام وفر فعلية من شركات

### المخاطر والقيود

1. **مُختبر على وكلاء ترميز فقط** — قد لا ينطبق مباشرة على وكلاء المحادثة أو الأعمال.
2. **يحتاج نموذج إضافي** — تكلفة إضافية 5-15% لنموذج التأمل.
3. **ضبط المعاملات** — θ, a, b تحتاج ضبطاً لكل حالة استخدام.
4. **خطر فقدان سياق مهم** — ضغط مفرط قد يحذف معلومات ضرورية لخطوات لاحقة.

---

## English Content

### What is AgentDiet?

AgentDiet automatically removes useless, redundant, and expired information from LLM agent trajectories during execution, reducing input token costs by 40-60% without performance loss. It uses a lightweight "reflection" LLM to compress past steps via a sliding window.

### Evidence (FSE 2026 — Peer-Reviewed)

- Input token reduction: 39.9%-59.7%
- Total computational cost reduction: 21.1%-35.9%
- Performance impact: -1% to +2% (within noise)
- Evaluated on SWE-bench Verified + Multi-SWE-bench Flash with Claude 4 Sonnet and Gemini 2.5 Pro

### Why ⭐⭐ and not higher?

Built and tested (Gates 1-2 ✅), but not deployed in production environments (Gates 3-4 ❌). Only validated on coding agents.

---

## المصادر | Sources

1. **[Tier 1]** Xiao, Y.-A., Gao, P., Peng, C., Xiong, Y., "Reducing Cost of LLM Agents with Trajectory Reduction", **FSE 2026** (مقبول), arXiv:2509.23586. DOI: 10.1145/3797084

### أعمال مرتبطة (2025-2026)

| البحث | ماذا يفعل | النتيجة | العلاقة بـ AgentDiet |
|-------|-----------|---------|---------------------|
| **AgentPrune** (Zhang et al., 2024) | يحذف الرسائل الزائدة في أنظمة multi-agent | 28-73% تقليل توكنات | مُكمّل — يعمل بين الوكلاء، AgentDiet داخل الوكيل |
| **RedundancyBench** (arXiv:2605.29893, 2026) | معيار لاكتشاف الخطوات الزائدة | يُثبت أن LLMs ضعيفة في اكتشاف التكرار | يُحدد المشكلة — الاكتشاف التلقائي صعب |
| **Simple Masking** (Emergent Mind 2025) | حذف مخرجات أدوات طويلة بدون تلخيص | تكلفة $0.61 مقابل $1.29 (52% وفر) | أبسط من AgentDiet لكن أقل ذكاءً |

> **ملاحظة:** Simple Masking (حذف مخرجات الأدوات الطويلة) يتفوق أحياناً على التلخيص بـ LLM لأن التلخيص يُطيل المسار عبر إخفاء إشارات الفشل.

---

## مصادر إضافية

2. **[Tier 2]** "RedundancyBench: Detecting Redundant Steps in LLM Agent Trajectories", arXiv:2605.29893, May 2026.
3. **[Tier 2]** Emergent Mind, "Efficient LLM Agent Deployment: Cost Analysis", 2025-2026. Simple masking comparison.
