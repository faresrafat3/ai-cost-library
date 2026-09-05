# 1.4 البنية الفعّالة | Efficient Architecture

> **المسار:** المكتبة ← تحسين النموذج ← البنية الفعّالة

بنى نموذجية تُقلل الحوسبة المطلوبة لكل توكن.

> **آخر تحديث: 2026-09-04 (round 82)**
>
> **ملاحظة عن drift (2026-09-04)**: الجدول التالي كان يعرض **3 إدخالات فقط** (LayerSkip, Mixture-of-Depths, قوانين التحجيم المعماري) لكن المجلد يحوي **8 ملفات إدخال** فعلية. تم إصلاح الجدول في round 82 ليطابق الـ filesystem.
>
> **الإدخالات الـ 5 المضافة للجدول:**
> - `deepseek-v4-economics.md` (DeepSeek V4)
> - `llama4-moe-economics.md` (Llama 4)
> - `mixture-of-experts-economics.md` (MoE)
> - `qwen3-efficiency.md` (Qwen3)
> - `subquadratic-models.md` (Mamba-3)
>
> **Drift note (2026-09-04)**: This subcategory README listed only 3 of 8 entries in the directory. The 5 missing entries (deepseek-v4, llama4-moe, mixture-of-experts, qwen3, subquadratic) have all been added. Same audit pattern as rounds 71 (arsenal README), 73 (CLAIMS.md), 75 (backlog), 78 (decision matrix), 79 (roadmap): surface the drift, fix it cleanly, document the proper fix.

| الإدخال | التصنيف | الإثبات | الملف | مصدر القرار |
|---------|---------|---------|-------|------------|
| LayerSkip | 📘 عملية | ⭐⭐⭐ | [layer-skip.md](layer-skip.md) | — |
| Mixture-of-Depths | 🧪 ناشئة | ⭐⭐ | [mixture-of-depths.md](mixture-of-depths.md) | — |
| قوانين التحجيم المعماري | 📐 نظرية | ⭐⭐⭐ | [inference-efficient-scaling.md](inference-efficient-scaling.md) | ICLR 2026 — قُرئ بالكامل |
| اقتصاديات DeepSeek V4 | 📘 عملية | ⭐⭐⭐⭐ | [deepseek-v4-economics.md](deepseek-v4-economics.md) | — |
| اقتصاديات Llama 4 MoE | 📘 عملية | ⭐⭐⭐⭐ | [llama4-moe-economics.md](llama4-moe-economics.md) | — |
| اقتصاديات مزيج الخبراء (MoE) | 📘 عملية | ⭐⭐⭐⭐ | [mixture-of-experts-economics.md](mixture-of-experts-economics.md) | — |
| كفاءات Qwen3 | 📘 عملية | ⭐⭐⭐⭐ | [qwen3-efficiency.md](qwen3-efficiency.md) | — |
| النماذج دون التربيعية (Mamba-3) | 🧪 ناشئة | ⭐⭐ | [subquadratic-models.md](subquadratic-models.md) | — |
