---
id: entry-skillreducer-001
title_ar: ضغط مهارات الوكلاء (SkillReducer)
title_en: "SkillReducer: Optimizing LLM Agent Skills for Token Efficiency"
type: emerging
status: preprint
category: agentic-economics
subcategory: chain-optimization
tree_path: "AI Cost Library → Agentic Economics → Chain Optimization → SkillReducer"
cost_dimensions:
  - token-cost
  - inference-cost
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 1
created: 2026-06-26
updated: 2026-06-26
research_review:
  paper_read: true
  abstract_fully_read: true
  methodology_scanned: true
  decision: "يُضاف — مكمّل لـ AgentDiet. يضغط system prompts/skills بدلاً من المسارات."
  limitations_noted: "preprint مارس 2026، لم يُراجع. نتائج على نظام وكيل واحد."
---

# 🧪 ضغط مهارات الوكلاء (SkillReducer)

> **التصنيف:** 🧪 ناشئة | **الإثبات:** ⭐⭐ نموذج أولي
>
> **المسار:** المكتبة ← اقتصاديات الوكلاء ← تحسين السلاسل

---

## المحتوى العربي

### ما هو SkillReducer؟

SkillReducer — وهو نظام يضغط "مهارات" الوكيل (system prompts المفصلة التي تحدد سلوكه) عن طريق تصنيف محتواها إلى: جوهري، خلفية، أمثلة، وقوالب — ثم الاحتفاظ بالجوهري فقط في السياق وتحويل الباقي إلى مراجع عند الطلب.

### الفرق عن AgentDiet

| | AgentDiet | SkillReducer |
|---|---------|-------------|
| **ماذا يضغط** | المسار المتراكم (trajectory) | تعريف المهارة (skill/prompt) |
| **متى** | أثناء التنفيذ | قبل التنفيذ (مرة واحدة) |
| **التكلفة** | مستمرة (5-15% overhead) | لمرة واحدة (~$14-18 لـ 600 مهارة) |

### النتائج

| الادعاء | القيمة | المصدر |
|---------|--------|--------|
| تقليل توكنات الجسم (body) | **79%** (من 2,543 إلى 540 توكن) | مثال مفصل في الورقة |
| متوسط تقليل الإدخال الكلي | **26.8%** | عبر جميع المهارات |
| تأثير أقل-هو-أكثر (less-is-more) | score_compressed = 1.0 vs score_original = 0.93 | بوابة الجودة |
| تكلفة ضغط 600 مهارة | **$14-18** (لمرة واحدة) | بنماذج مفتوحة رخيصة |
| زيادة المخرجات | +1.7% متوسط (ضئيلة) | بوابة الجودة |

### كيف يعمل؟

**مرحلتان:**
1. **ضغط الوصف (Stage 1):** ddmin يزيل الأجزاء الزائدة من وصف المهارة (63% تقليل)
2. **ضغط الجسم (Stage 2):** يُصنف المحتوى إلى 4 فئات:
   - 🟢 **جوهري** (قواعد، KPIs، معايير قرار) → يبقى دائماً
   - 🟡 **خلفية** (شرح سير العمل) → مرجع عند الطلب
   - 🟠 **أمثلة** (رسائل محددة) → مرجع عند الطلب
   - 🔴 **قوالب** (تكوينات HubSpot مثلاً) → مرجع عند الطلب

### لماذا ⭐⭐؟

- ✅ منهجية واضحة ومكمّلة لـ AgentDiet
- ✅ تكلفة لمرة واحدة فقط
- ❌ preprint (مارس 2026) — لم يُراجع
- ❌ مُختبر على نظام وكيل واحد

---

## English Content

SkillReducer compresses agent skill definitions (system prompts) by classifying content into core rules, background, examples, and templates — keeping only core in context and converting the rest to on-demand references. Average 26.8% input reduction. One-time cost of $14-18 for 600 skills.

---

## المصادر | Sources

1. **[Tier 2]** "SkillReducer: Optimizing LLM Agent Skills for Token Efficiency", arXiv:2603.29919, March 2026.

### العلاقة بإدخالات أخرى

| الإدخال | العلاقة |
|---------|---------|
| **AgentDiet** | **تكاملي** — SkillReducer يضغط المهارة (قبل التنفيذ)، AgentDiet يضغط المسار (أثناء التنفيذ) |
| **Context Compression** | **تكاملي** — SkillReducer = ضغط system prompt، Context Compression = ضغط التاريخ |
| **Prompt Caching** | **يُحسّن** — مهارة مضغوطة = بادئة أقصر = cache أكفأ |

### مقارنة تقنيات تقليل توكنات الوكلاء (2026)

| التقنية | ماذا تضغط | متى | التقليل | التكلفة |
|---------|-----------|-----|---------|---------|
| **SkillReducer** | system prompt / المهارة | قبل التنفيذ | 27% | $14-18 لمرة واحدة |
| **AgentDiet** | المسار المتراكم | أثناء التنفيذ | 40-60% | 5-15% overhead مستمر |
| **Context Compression** | تاريخ المحادثة | أثناء التنفيذ | 22-57% | متغير |
| **Anthropic Compaction** | كل السياق | تلقائي | تلقائي | مُدمج في API |
| **Model Routing (فرعي)** | اختيار النموذج | لكل خطوة | 60-80% | < 1ms overhead |

### مصادر إضافية

2. **[Tier 2]** "Cross-Lingual Token Arbitrage: Optimizing Code Agent Context Windows", arXiv:2606.03618, June 2026. References SkillReducer as complementary.
3. **[Tier 2]** Zylos AI, "AI Agent Context Compression Strategies", February 2026. Compares SkillReducer to ACON and Focus.
