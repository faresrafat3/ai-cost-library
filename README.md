# مكتبة تكلفة الذكاء الاصطناعي · AI Cost Library

> **مكتبة علمية ثنائية اللغة، قائمة على الأدلة، لتوثيق وتقييم طرق تقليل تكلفة الذكاء الاصطناعي.**
>
> A bilingual, evidence-based scientific library and decision-support system for AI cost reduction methods.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.0-3B82F6.svg)](CHANGELOG.md)
[![Language: Arabic + English](https://img.shields.io/badge/language-العربية%20%2B%20English-10B981.svg)](#)
[![No-Hype Policy](https://img.shields.io/badge/policy-no--hype-F59E0B.svg)](NO_HYPE_POLICY.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-8B5CF6.svg)](CONTRIBUTING.md)
[![Citation](https://img.shields.io/badge/cite-CITATION.cff-E2E8F0.svg)](CITATION.cff)

![Dashboard](assets/dashboard.svg)

---

## 🎯 لماذا هذه المكتبة؟ | Why this library?

مع التوسع المتسارع في الـ LLMs والـ AI agents، أصبحت تكلفة الاستدلال والتدريب تحديًا حقيقيًا للشركات والمطورين. الإشكالية: هناك عشرات الطرق لتقليل التكلفة (تكميم، تجميع، توجيه، تخزين مؤقت...) لكن كل منها لها **تنازلات** (tradeoffs) لا يذكرها المسوّقون.

هذه المكتبة تجمع الطرق المعروفة، تصنّفها حسب **قوة الدليل** (وليس حسب حجم الضجيج التسويقي)، وتوضح **متى تُستخدم ومتى تُتجنب**.

> **المبدأ الحاكم**: *"عدم اليقين الصادق أفضل من يقين مُختلق."*
> *"Better an honest unknown than a fabricated certainty."* — [NO_HYPE_POLICY.md](NO_HYPE_POLICY.md)

---

## 📊 ما الذي بداخلها؟ | What's inside?

| | |
|---|---|
| 📝 **60 إدخال** موثّق عبر 7 فئات كبرى | 🔗 **213 مصدر** موثّق (Tier 1-3) |
| 📘 **40 تطبيقية** (مُثبتة في إنتاج) | 🧪 **17 ناشئة** (واعدة لكن غير مثبتة) |
| 📐 **3 نظرية** (أساس علمي) | 📚 **58 مصطلح** في المعجم العلمي |
| 🧾 **25 ادعاء** مسجل مع مستويات ثقة | 🛠️ **5 أدلة تطبيقية** + **6 مقارنات** تفصيلية |

---

## 🚀 البدء السريع | Quick Start

### للمستخدم الذي يبحث عن حل لمشكلة معينة

اذهب مباشرة إلى [**مصفوفة اتخاذ القرار**](DECISION_MATRIX.md) — تجد سيناريو شبيه بمشكلتك والحلول الموصى بها.

### للقارئ الذي يريد فهم صورة السوق

1. اقرأ [**شجرة التصنيفات**](TREE.md) لفهم الهيكل العام
2. تصفّح [**التصنيف العادل متعدد المعايير**](RANKING.md) لمعرفة التقنيات الأعلى تقييمًا
3. اطّلع على [**ترتيب التقنيات حسب نوع المستخدم**](USER_RANKINGS.md) (مطور فردي / شركة / باحث / مطور وكلاء)

### للباحث الذي يريد التعمق

- [**المنهجية**](METHODOLOGY.md) — بوابات الأدلة الأربعة
- [**نظام التقييم الشامل**](SCORING_SYSTEM.md) — 12 بُعد × 5 ملفات مستخدم
- [**سجل الأدلة**](EVIDENCE_LEDGER.md) و [**سجل الادعاءات**](CLAIMS.md)
- [**خريطة العلاقات بين التقنيات**](RELATIONSHIPS.md)

### للمطور الذي يريد التطبيق

- [**أدلة التنفيذ**](playbooks/) — خطوات عملية قابلة للتطبيق
- [**المقارنات**](comparisons/) — جداول مقارنة بين البدائل
- [**المعجم العلمي**](GLOSSARY.md) — مصطلحات ثنائية اللغة

### للأتمتة / الـ CI

```bash
# مزامنة بيانات JSON من شجرة Markdown
python3 scripts/sync_metadata.py

# توليد ملف التصنيف العادل RANKING.md
python3 scripts/generate_fair_ranking.py

# توليد لوحة القيادة assets/dashboard.svg
python3 scripts/generate_dashboard.py
```

> السكربتات تعتمد على stdlib فقط — يمكن تشغيلها في أي بيئة Python 3.9+ بدون `pip install`.

---

## 🏗️ التصنيف الجديد (v2.0)

يُبنى التصنيف على **أربع طبقات مُثبتة علميًا** في أدبيات تكاليف AI، مع بُعدين إضافيين للتحديات الحديثة (الوكلاء + الحوكمة المالية):

```
┌─────────────────────────────────────────────────────────┐
│  7. اقتصاديات السوق    6. الحوكمة المالية 🆕           │
│  (سياق + أسعار)        (تحكم + مراقبة)                │
├─────────────────────────────────────────────────────────┤
│  5. اقتصاديات الوكلاء 🆕                              │
│  (5-30× مضاعف التوكن — التحدي الأكبر في 2026)         │
├───────────┬───────────┬────────────────────────────────┤
│ 1. النموذج│ 2. التشغيل│ 3. التدريب                     │
│ (ماذا؟)  │ (كيف؟)   │ (كيف نبنيه؟)                  │
├───────────┴───────────┴────────────────────────────────┤
│  4. البنية التحتية والعتاد                              │
│  (GPU, TPU, سحابي vs محلي, طاقة)                       │
└─────────────────────────────────────────────────────────┘
```

| # | الفئة | الوصف | الإدخالات | الوفر النموذجي |
|---|-------|-------|----------|---------------|
| 1 | [تحسين النموذج](library/01-model-optimization/) | تكميم، ضغط، اختيار، بنية | 19 | 30-75% |
| 2 | [تحسين التشغيل](library/02-runtime-optimization/) | تجميع، ذاكرة، تخزين، محركات | 14 | 40-80% |
| 3 | [تحسين التدريب](library/03-training-optimization/) | LoRA, QLoRA, موزّع | 3 | متغير |
| 4 | [البنية التحتية](library/04-infrastructure/) | مسرّعات، نشر، طاقة | 8 | 40-65% |
| 5 | [اقتصاديات الوكلاء](library/05-agentic-economics/) | مضاعف التوكن، سلاسل، RAG | 5 | حرج |
| 6 | [الحوكمة المالية](library/06-finops-governance/) | مراقبة، ميزانية، عائد | 3 | حوكمة |
| 7 | [اقتصاديات السوق](library/07-market-economics/) | أسعار، مزودون، مفارقات | 2 | سياق |

التفاصيل الكاملة في [**TAXONOMY_REDESIGN.md**](TAXONOMY_REDESIGN.md).

---

## 🎓 حالات الاستخدام | Use Cases

### 1. مطور يريد تقليل تكلفة API لـ LLM
→ راجع [playbooks/reduce-llm-api-cost.md](playbooks/reduce-llm-api-cost.md) + [comparisons/rag-cost-vs-long-context-cost.md](comparisons/rag-cost-vs-long-context-cost.md)

### 2. شركة تريد استضافة نموذج 70B على GPU واحد
→ راجع [playbooks/reduce-gpu-memory.md](playbooks/reduce-gpu-memory.md) + [comparisons/quantization-methods.md](comparisons/quantization-methods.md)

### 3. باحث يريد ضبط دقيق بميزانية محدودة
→ راجع [playbooks/fine-tune-on-low-budget.md](playbooks/fine-tune-on-low-budget.md) + [comparisons/lora-vs-qlora-vs-full-finetuning.md](comparisons/lora-vs-qlora-vs-full-finetuning.md)

### 4. فريق يريد نشر استدلال رخيص
→ راجع [playbooks/deploy-cheaper-inference.md](playbooks/deploy-cheaper-inference.md) + [comparisons/inference-engines.md](comparisons/inference-engines.md)

### 5. مطور وكلاء يريد التحكم في مضاعف التوكن
→ راجع [library/05-agentic-economics/](library/05-agentic-economics/) — التحدي الأكبر في 2026 (5-30× تكلفة إضافية)

---

## 🏆 آخر الإضافات | Latest Additions

| المعرف | التقنية | التصنيف | الإثبات | الفئة |
|--------|---------|---------|---------|-------|
| `entry-fp8-001` | FP8 Quantization | 📘 عملية | ⭐⭐⭐⭐ إنتاج | تكميم |
| `entry-routing-001` | توجيه النماذج الذكي | 📘 عملية | ⭐⭐⭐ منشور | اختيار النموذج |
| `entry-semcache-001` | التخزين المؤقت الدلالي | 📘 عملية | ⭐⭐⭐ منشور | تخزين مؤقت |
| `entry-chinchilla-001` | قوانين Chinchilla | 📐 نظرية | ⭐⭐⭐ مُتحقق | اختيار النموذج |
| — | مقارنة محركات الاستدلال | مقارنة | — | محركات |
| — | إعادة هيكلة التصنيف v2.0 | هيكلي | — | المكتبة |

---

## 📚 الفهرس الكامل | Full Index

### المكتبة والتصنيف
- [🏆 التصنيف العادل متعدد المعايير](RANKING.md) — Fair MCDA ranking (60 إدخال)
- [🥇 الترتيب حسب نوع المستخدم](USER_RANKINGS.md) — Top 10 لكل persona
- [📚 المكتبة الكاملة](library/)
- [🌳 شجرة التصنيفات](TREE.md)
- [📋 وثيقة إعادة التصنيف](TAXONOMY_REDESIGN.md)

### المنهجية والجودة
- [المنهجية](METHODOLOGY.md) — بوابات الأدلة الأربعة
- [نظام التقييم الشامل (12 بُعد × 5 ملفات مستخدم)](SCORING_SYSTEM.md)
- [خريطة العلاقات بين التقنيات](RELATIONSHIPS.md)
- [المعجم العلمي](GLOSSARY.md)
- [سياسة عدم المبالغة](NO_HYPE_POLICY.md)
- [قائمة الجودة](QUALITY_CHECKLIST.md)
- [دليل المصطلحات العربية](ARABIC_TERMINOLOGY_GUIDE.md)

### الأدلة والادعاءات
- [سجل الأدلة](EVIDENCE_LEDGER.md)
- [سجل الادعاءات](CLAIMS.md)
- [مصفوفة اتخاذ القرار](DECISION_MATRIX.md)

### أدلة التنفيذ والمقارنات
- [أدلة التنفيذ](playbooks/) — خطوات عملية
- [المقارنات](comparisons/) — جداول مقارنة

### خارطة الطريق والسجل
- [خارطة الطريق](ROADMAP.md)
- [سجل التغييرات](CHANGELOG.md)
- [سجل البحث](RESEARCH_LOG.md)
- [دليل المساهمة](CONTRIBUTING.md)

### الملفات الإدارية (داخلية)
- [📁 مجلد `internal/`](internal/) — حالة الوكيل، الإجراءات التالية، سجل الجلسات، بروتوكول الاستمرار

---

## 🤝 المساهمة | Contributing

نرحب بالمساهمات! اقرأ [CONTRIBUTING.md](CONTRIBUTING.md) قبل البدء.

**أنواع المساهمات المقبولة:**
- إضافة طريقة جديدة (مع مصادر موثّقة)
- تحسين الترجمة العربية
- إضافة playbook أو مقارنة
- تصحيح أخطاء في الإدخالات الموجودة

**معايير القبول:**
- ✅ ثنائي اللغة (عربي + إنجليزي)
- ✅ مصادر موثّقة لكل ادعاء رقمي
- ✅ ذكر التنازلات والمخاطر بصراحة
- ✅ الالتزام بـ [NO_HYPE_POLICY.md](NO_HYPE_POLICY.md)

---

## 📜 الترخيص | License

[MIT License](LICENSE) — مفتوح المصدر للجميع.

## 📫 الاقتباس | Citing

إذا استخدمت هذه المكتبة في بحث أو مشروع، يرجى الإشارة إليها كما هو موضح في [CITATION.cff](CITATION.cff). GitHub يوفر زر "Cite this repository" لإنتاج BibTeX تلقائيًا.

## 📧 التواصل | Contact

- GitHub: [@faresrafat3](https://github.com/faresrafat3)
- Issues: [open a new issue](https://github.com/faresrafat3/ai-cost-library/issues/new/choose)

---

<p align="center">
  <em>"عدم اليقين الصادق أفضل من يقين مُختلق."<br>Better an honest unknown than a fabricated certainty.</em>
</p>
