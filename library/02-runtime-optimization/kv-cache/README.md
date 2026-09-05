# 2.3 إدارة ذاكرة KV | KV Cache Management

> **المسار:** المكتبة ← تحسين التشغيل ← ذاكرة KV

> **آخر تحديث: 2026-09-04 (round 84)**: تم إكمال الجدول بإضافة `sparse-linear-attention.md` الذي كان مفقوداً.

| الإدخال | التصنيف | الإثبات | الملف |
|---------|---------|---------|-------|
| PagedAttention | 📘 عملية | ⭐⭐⭐⭐ | [paged-attention.md](paged-attention.md) |
| FlashAttention | 📘 عملية | ⭐⭐⭐⭐ | [flash-attention.md](flash-attention.md) |
| RadixAttention | 📘 عملية | ⭐⭐⭐ | [radix-attention.md](radix-attention.md) |
| الانتباه المتناثر والخطي | 🧪 ناشئة | ⭐⭐ | [sparse-linear-attention.md](sparse-linear-attention.md) |

| ضغط ذاكرة KV | 🧪 ناشئة | ⭐⭐ | [kv-cache-compression.md](kv-cache-compression.md) |

**قاعدة عملية:** خصص 40-60% من ذاكرة GPU لذاكرة KV المؤقتة.

**الاتجاه الحديث (2026):** 4 أبحاث جديدة تحقق 95%+ أداء مع 3-5% فقط من KV cache — مجال نشط جداً.
