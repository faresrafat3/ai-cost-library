# 1.1 التكميم | Quantization

> **المسار:** المكتبة ← تحسين النموذج ← التكميم

تقليل دقة الأوزان والتفعيلات لتقليل الذاكرة وزيادة الإنتاجية.

| الإدخال | التصنيف | الإثبات | الملف |
|---------|---------|---------|-------|
| LLM.int8() | 📘 عملية | ⭐⭐⭐⭐ | [llm-int8.md](llm-int8.md) |
| GPTQ | 📘 عملية | ⭐⭐⭐⭐ | [gptq.md](gptq.md) |
| AWQ | 📘 عملية | ⭐⭐⭐⭐ | [awq.md](awq.md) |
| SmoothQuant | 📘 عملية | ⭐⭐⭐ | [smoothquant.md](smoothquant.md) |
| FP8 Quantization | 📘 عملية | ⭐⭐⭐⭐ | [fp8-quantization.md](fp8-quantization.md) |

**التوصية في 2026:** FP8 هو المعيار الافتراضي على Hopper/Blackwell. ابدأ به، ثم جرّب INT4 (AWQ/GPTQ) إذا احتجت ضغطاً أكبر.
