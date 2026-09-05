# حالة الوكيل | Agent State

**آخر تحديث:** 2026-09-04 (تحديث Round 68 — توافق الأرقام مع `data/*.json`)
**آخر تحديث هيكلي:** 2026-06-28 (Session 6 — Ihsan Polish)
**حالة المشروع:** نشط وقابل للاستمرار
**المستودع:** https://github.com/faresrafat3/ai-cost-library
**الإصدار:** 2.1.0 (تحديث الأرقام والالتزامن)

> **ملاحظة Round 68:** تم تحديث الأرقام في هذا الملف لتطابق `data/*.json` الفعلي.
> الجلسات السابقة (Session 1-6) لا تزال موثقة في `SESSION_LOG.md` كما هي.
> الإصدار الفعلي في `pyproject.toml` هو `2.1.0` (منذ 2026-09-04، بعد روند 41+).

## ملخص الحالة الحالية

المستودع موجود مسبقاً، وبموافقة المستخدم تم فحصه وتحديث ملفات البيانات والتتبع دون حذف أي محتوى. الشجرة الحالية أوسع من الهيكل الأولي: 7 فئات كبرى، 25 فئة فرعية، و61 ملف إدخال معرفي داخل `library/` (60 مُقيَّمة + 1 قيد المراجعة).

في الجلسة 2026-06-28 (session 6)، تم تنفيذ عملية **إتقان شاملة** على هيكل المستودع:

- ✅ إصلاح LICENSE المكسور (MIT كامل)
- ✅ حل تعارض التسمية بين `RANKING.md` و `RANKINGS.md` (الأخير أصبح `USER_RANKINGS.md`)
- ✅ نقل ملفات الإدارة الداخلية إلى `internal/` (هذا الملف ضمنها الآن)
- ✅ إعادة كتابة README بشكل احترافي مع badges + dashboard SVG
- ✅ توليد `assets/dashboard.svg` حقيقي + سكربت `scripts/generate_dashboard.py`
- ✅ إضافة `CITATION.cff` + `pyproject.toml` + `.gitignore` موسّع
- ✅ إضافة GitHub Actions (`validate.yml`) يتحقق من JSON + front matter + sync
- ✅ إضافة issue templates (bug, feature, new_entry) + PR template + CODEOWNERS

## الإحصائيات المتزامنة

> **مصدر الأرقام:** `data/stats.json` + `data/entries.json` + `data/sources.json` + `data/claims.json` + `data/glossary.json` (تم التحقق في 2026-09-04 round 68).

| المقياس | العدد | المصدر |
|---------|-------|--------|
| 🌿 فئات كبرى | 7 | `data/categories.json` (level=1) |
| 🍃 فئات فرعية | 25 | `data/categories.json` (level=2) |
| 📝 إدخالات Markdown | **61** | `data/entries.json` (60 مُقيَّمة + 1 pending) |
| 📘 عملية | 40 | `data/entries.json` (type=practical) |
| 🧪 ناشئة | 17 | `data/entries.json` (type=emerging) |
| 📐 نظرية | 3 | `data/entries.json` (type=theoretical) |
| ⏳ قيد المراجعة | **1** | `entry-model-router-cascade` (type=pending) |
| ❌ مرفوضة | 0 | (لا توجد حالياً) |
| 🔗 مصادر موثّقة (Tier 1-3) | **217** | `data/sources.json` |
| 🧾 ادعاءات مسجلة | **29** | `data/claims.json` |
| 📚 مصطلحات المعجم | **59** | `data/glossary.json` |

> **التغييرات عن الجلسة 6 (2026-06-28):**
> - إدخالات: 60 → 61 (+1: entry-model-router-cascade، type=pending)
> - مصادر: 213+ → 217 (+4)
> - ادعاءات: 25+ → 29 (+4)
> - معجم: 58+ → 59 (+1)
> - pending: 0 → 1 (الإدخال الجديد في `05-agentic-economics/`)
> - الإصدار: 0.4.0 → 2.1.0 (تحديث README، CHANGELOG، badges في روند 41)

## ما تم في آخر جلسة (2026-06-28 — Session 6 — Ihsan Polish)

### المرحلة 1: تدقيق قبل التنفيذ
- قراءة 16 ملف MD + 14 ملف JSON + scripts بتمعن
- اكتشاف: LICENSE مكسور + تعارض RANKING/RANKINGS + 28 ملف في الجذر + README بدون badges
- توثيق التدقيق في `fares-career-lab/LOG/audit-2026-06-28-acl-polish.md`

### المرحلة 2: إصلاحات حرجة
- كتابة MIT LICENSE كامل (مع ملاحظة على content licensing)
- توسيع `.gitignore`
- إضافة `CITATION.cff` (للاقتباس الأكاديمي)
- إضافة `pyproject.toml` (للـ scripts كأدوات CLI)

### المرحلة 3: تنظيم الهيكل
- إنشاء `internal/` ونقل: AGENT_STATE, NEXT_ACTIONS, SESSION_LOG, CONTINUATION_PROTOCOL
- إعادة تسمية `RANKINGS.md` → `USER_RANKINGS.md`
- إنشاء `internal/README.md` يوضح محتوى المجلد
- تحديث الروابط الداخلية في README.md

### المرحلة 4: رفع جودة README
- إعادة كتابة README كامل مع:
  - 6 badges (license, version, language, no-hype, PRs welcome, citation)
  - لوحة قيادة SVG مرئية
  - "Quick Start" موجه لـ 5 أنواع مستخدمين
  - "Use Cases" بـ 5 سيناريوهات
  - فهرس كامل منظم
- توليد `assets/dashboard.svg` + سكربت `scripts/generate_dashboard.py` (stdlib only)

### المرحلة 5: CI/CD + قوالب
- إضافة `.github/workflows/validate.yml`:
  - يتحقق من صحة JSON
  - يتحقق من front matter في كل إدخالات library
  - يشغل `sync_metadata.py` ويتأكد من التزامن
- إضافة 3 issue templates (bug, feature, new_entry)
- إضافة PR template مع checklist
- إضافة CODEOWNERS

## قرارات مهمة (محدثة)

- لم يتم حذف المستودع أو إعادة إنشائه لأنه كان موجوداً مسبقاً.
- اعتُمدت الشجرة الحالية v2.x بدلاً من الرجوع إلى الهيكل الأولي الأضيق، لأنها أغنى.
- `data/sources.json` سجل آلي خفيف لأسطر `[Tier]` من Markdown؛ المصادر الرقمية الحساسة تحتاج مراجعة يدوية.
- **جديد**: نقل الملفات الإدارية إلى `internal/` لأنها لا تهم القارئ الخارجي لكنها ضرورية لاستمرارية العمل.
- **جديد**: حل تعارض التسمية `RANKING.md` vs `RANKINGS.md` بإعادة تسمية الأخير إلى `USER_RANKINGS.md` (أوضح).

## تحذيرات جودة

- بعض الإدخالات تحتوي مصادر من طبقة ثالثة أو مصادر حديثة جداً؛ يجب تمييز الأرقام الحساسة بثقة مناسبة.
- `data/claims.json` و`data/evidence.json` أقل اكتمالاً من عدد المصادر الفعلي؛ ينبغي توسيعهما تدريجياً.
- لا توجد إدخالات Rejected أو Pending حالياً، رغم أن سياسة المشروع تتطلب دعمها.

## نقطة الاستئناف السريعة

ابدأ بقراءة: `internal/CONTINUATION_PROTOCOL.md` → `internal/AGENT_STATE.md` → `internal/NEXT_ACTIONS.md` → `data/stats.json` → `TREE.md`. ثم شغّل:

```bash
python3 scripts/sync_metadata.py
python3 scripts/generate_fair_ranking.py
python3 scripts/generate_dashboard.py
```

بعد أي إضافة إدخالات جديدة، حدّث الادعاءات والأدلة يدوياً ثم أعد تشغيل السكربتات.

> ملاحظة: الملفات الإدارية الآن في `internal/` (محدثة الروابط).

## تحديث 2026-06-27
- أُضيف إدخال جديد: **Sleep-time Compute** ضمن `02-runtime-optimization/inference-time-compute/`.
- أُضيف مصطلح جديد إلى المعجم: **حوسبة وقت النوم**.
- سُجلت 4 مصادر جديدة، و4 ادعاءات، و4 أدلة مرتبطة مباشرة بالإدخال.
