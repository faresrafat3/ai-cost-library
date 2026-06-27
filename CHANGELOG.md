# سجل التغييرات | Changelog

## 0.4.0 — 2026-06-28
- 🔴 إصلاح LICENSE المكسور (كان 12 bytes فقط) — كتابة MIT License كامل مع ملاحظة على content licensing.
- 🟡 حل تعارض التسمية بين `RANKING.md` و `RANKINGS.md` — إعادة تسمية `RANKINGS.md` → `USER_RANKINGS.md` لتوضيح أنه الترتيب حسب نوع المستخدم.
- 🟡 تنظيم الهيكل: نقل ملفات الإدارة الداخلية إلى مجلد `internal/` (AGENT_STATE, NEXT_ACTIONS, SESSION_LOG, CONTINUATION_PROTOCOL).
- 🟡 إضافة `internal/README.md` يوضح محتوى المجلد وكيفية استئناف العمل.
- 🟢 إعادة كتابة `README.md` بشكل احترافي:
  - Badges (license, version, language, no-hype, PRs welcome, citation)
  - لوحة القيادة المرئية `assets/dashboard.svg`
  - قسم "لماذا هذه المكتبة؟"
  - قسم "ما الذي بداخلها؟" بإحصائيات سريعة
  - قسم "البدء السريع" موجه لكل نوع مستخدم
  - قسم "حالات الاستخدام" بـ 5 سيناريوهات
  - فهرس كامل منظم
- 🟢 توليد `assets/dashboard.svg` حقيقي (بدلاً من placeholder) — Python script في `scripts/generate_dashboard.py`.
- 🟢 إضافة `CITATION.cff` للاقتباس الأكاديمي (GitHub يدعم زر "Cite this repository" تلقائيًا).
- 🟢 إضافة `pyproject.toml` لتثبيت السكربتات كأدوات CLI (`acl-sync`, `acl-rank`).
- 🟢 توسيع `.gitignore` ليشمل إعدادات Python احترافية + IDEs + coverage.
- 🟢 إضافة GitHub Actions workflow (`.github/workflows/validate.yml`):
  - التحقق من صحة كل ملفات JSON في `data/`
  - التحقق من front matter في `library/**/*.md`
  - تشغيل `sync_metadata.py` والتأكد من أن `data/*.json` متزامن
- 🟢 إضافة issue templates:
  - `bug_report.yml` (مع حقل للملف المتأثر + الخطورة + المصدر المرجعي)
  - `feature_request.yml`
  - `new_entry.yml` (مفصل — يشمل checklist للـ no-hype policy)
  - `config.yml` (تعطيل blank issues + روابط Discussions)
- 🟢 إضافة `PULL_REQUEST_TEMPLATE.md` مع checklist كامل.
- 🟢 إضافة `CODEOWNERS` (المالك الافتراضي لكل الريبو).

## 0.3.0 — 2026-06-26
- فحص المستودع الموجود وتحديثه دون حذف المحتوى.
- إضافة ملفات README للفئات الفرعية.
- إضافة فئة Energy and Sustainability.
- نقل Prompt Caching إلى بنية L2/L3.
- ملء ملفات JSON الخاصة بالمصادر والادعاءات والأدلة ومصفوفة القرار.
- تحديث ملفات الاستمرار والحالة.

## 0.2.0 — 2026-06-26
- توسيع أولي للإدخالات العملية والمقارنات والأدلة.

## 0.1.0 — 2026-06-26
- إنشاء الهيكل الأولي للمكتبة.
