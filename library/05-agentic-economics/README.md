# 5. اقتصاديات الوكلاء | Agentic AI Economics

> **المسار:** المكتبة ← اقتصاديات الوكلاء
> **الوصف:** التحدي الأحدث والأكبر في 2026 — الوكلاء يستهلكون 5-30× أكثر من المحادثة البسيطة.
> **الحالة:** 🆕 فئة جديدة — قيد البناء

## لماذا هذه الفئة حرجة؟

> **"محادثة بسيطة = $0.001. وكيل متعدد الخطوات = $0.10-1.00 لكل مهمة."**
> — Zylos AI, Inference Economics 2026

- Gartner (مارس 2026): الوكلاء يستهلكون **5-30×** أكثر من روبوتات المحادثة
- Uber (2026): استنفد ميزانية أدوات الترميز AI لسنة كاملة في **4 أشهر**
- Gartner (2025): **40%+** من مشاريع الوكلاء ستُلغى بحلول 2027 بسبب التكاليف المتصاعدة
- IDC FutureScape (2026): المؤسسات ستُقلل تقدير تكاليف البنية التحتية AI بنسبة **30%**

## الفئات الفرعية

> **آخر تحديث: 2026-09-04 (round 85)**: تم تصحيح عدد الإدخالات — جميع الفئات كانت "0 ⏳" لكنها تحوي فعلياً: token-multiplier 1، chain-optimization 4، tool-and-rag-costs 1.

| الفئة | الوصف | الإدخالات |
|-------|-------|----------|
| [مضاعف التوكن](token-multiplier/) | لماذا الوكلاء أغلى 100-1000× | 1 |
| [تحسين سلاسل الوكلاء](chain-optimization/) | تقليل الخطوات، التخزين المؤقت | 4 |
| [تكلفة الأدوات والاسترجاع](tool-and-rag-costs/) | RAG vs سياق طويل، تحسين النافذة | 1 |

## إدخالات على مستوى الفئة (Top-level)

| الإدخال | التصنيف | الإثبات | الملف |
|---------|---------|---------|-------|
| توجيه النماذج المتدرج (Model Router Cascade) | 🧪 ناشئة | ⭐ قيد التقييم | [model-router-cascade.md](model-router-cascade.md) |

> **ملاحظة Round 94 (2026-09-05)**: `model-router-cascade.md` يعيش مباشرة تحت `05-agentic-economics/` (ليس داخل فئة فرعية). هذا الإدخال هو الإدخال الـ 7 الذي لم يكن مُدرجاً في جدول الفئات الفرعية. كان ملاحظاً في `data/categories.json` (entry_count=7) لكنه مفقود من README.
> 
> **Round 94 drift note**: `model-router-cascade.md` lives directly under `05-agentic-economics/` (not inside any subcategory). This is the 7th entry that wasn't listed in the subcategory table. It was reflected in `data/categories.json` (entry_count=7) but missing from the README.

## المصادر الأساسية
1. **[Tier 2]** Zylos AI, "Inference Economics: AI Agent Compute Markets in 2026", April 2026
2. **[Tier 2]** Oplexa, "AI Inference Cost Crisis 2026", March 2026
3. **[Tier 2]** Gartner, "Agentic AI Cost Analysis", March 2026
4. **[Tier 3]** TechAhead Corp, "The Inference Cost Trap", June 2026

> *الفئة تحتوي **7 إدخالات فعلية** الآن (6 في الفئات الفرعية + 1 على مستوى الفئة) — تم تحديث الجدول في round 85 (الفئات الفرعية) و round 94 (الإدخال على مستوى الفئة).*
