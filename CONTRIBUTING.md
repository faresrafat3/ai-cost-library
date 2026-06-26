# دليل المساهمة | Contributing Guide

## 🤝 كيف تساهم في المكتبة | How to Contribute

مرحباً بك في مكتبة تكلفة الذكاء الاصطناعي! نقبل المساهمات من المطورين والباحثين والمترجمين.

Welcome to the AI Cost Library! We welcome contributions from developers, researchers, and translators.

### 📋 أنواع المساهمات | Contribution Types

1. **إضافة طريقة جديدة (New Method Entry)**
   - اختر التصنيف المناسب في `library/` أو اقترح تصنيفاً جديداً
   - استخدم القالب المناسب: `templates/practical-entry-template.md` أو `templates/emerging-entry-template.md` أو `templates/theoretical-entry-template.md`
   - يجب أن يكون كل إدخال ثنائي اللغة (عربي أولاً، إنجليزي ثانياً)

2. **إضافة أو تحسين مصدر (Source Addition)**
   - كل ادعاء رقمي يجب أن يكون مدعوماً بمصدر موثوق
   - تنسيق المصدر: `[Tier] Author, "Title", Venue, Year, DOI/URL`
   - المستويات: Tier 1 (مجلات/مؤتمرات)، Tier 2 (أبحاث ما قبل النشر المعتمدة)، Tier 3 (أبحاث حديثة/مقالات تقنية)

3. **تحسين الترجمة العربية (Arabic Translation Improvement)**
   - راجع `ARABIC_TERMINOLOGY_GUIDE.md` لسياسات الترجمة
   - تجنب النقل الحرفي الضعيف (Weak Transliteration)
   - المصطلحات الجديدة تُضاف إلى `GLOSSARY.md` و `data/glossary.json`

4. **إضافة دليل تطبيقي (Playbook)**
   - يجب أن يقدّم خطوات عملية قابلة للتطبيق
   - كل خطوة يجب أن تشير إلى الإدخالات ذات العلاقة في المكتبة
   - يجب أن يتضمن "متى تستخدم" و "متى تتجنب"

### 🔍 معايير القبول | Acceptance Criteria

- ✅ إدخال ثنائي اللغة (عربي + إنجليزي)
- ✅ تصنيف واضح (Practical/Emerging/Theoretical/Rejected/Pending)
- ✅ درجات الإثبات (للمدخلات التطبيقية)
- ✅ مصادر موثقة لكل ادعاء رقمي
- ✅ ذكر التنازلات والمخاطر (Tradeoffs & Risks)
- ✅ تحديث ملفات JSON و EVIDENCE_LEDGER و CLAIMS

### 📝 عملية المراجعة | Review Process

1. أنشئ Pull Request مع وصف واضح للتغييرات
2. سيُراجع الإدخال وفق `QUALITY_CHECKLIST.md`
3. سيتم التحقق من المصادر والادعاءات الرقمية
4. بعد الموافضة، يُدمج في الفرع الرئيسي

---

**ملاحظة:** هذه مكتبة علمية، ليست مدونة ترويجية. نلتزم بـ `NO_HYPE_POLICY.md` بصرامة.

**Note:** This is a scientific library, not a marketing blog. We strictly follow `NO_HYPE_POLICY.md`.
