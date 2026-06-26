# القصّ الهيكلي | Structural Pruning

## العربية

يُقصد بـ **القصّ الهيكلي** إزالة أجزاء كاملة من الشبكة العصبية (طبقات كاملة، رؤوس اهتمام، قنوات) بدلاً من إزالة أوزان فردية متفرقة. هذا يُنتج نموذجاً أصغر يعمل على أجهزة عادية بدون حاجة لمكتبات خاصة.

### تقنيات فرعية

| التقنية | الوصف | الحالة |
|---------|-------|--------|
| [ShortGPT](short-gpt.md) | إزالة طبقات كاملة بناءً على إنتروبيا الاهتمام | 📘 تطبيقية |
| [SlimGPT](short-gpt.md) | قصّ هيكلي طبقة-بطبقة | 📘 تطبيقية |
| [E3-Pruner](#) | قصّ فعال واقتصادي | 🧪 ناشئة |
| [Týr-the-Pruner](#) | قصّ عبر التفرّد الشامل | 🧪 ناشئة |

### تأثير التكلفة

- **الذاكرة**: تخفيض 20-50% من المعاملات
- **الحوسبة**: تخفيض مماثل في FLOPs
- **الزمنية**: تسريع 1.4-2.18× حسب نسبة القصّ

---

## English

**Structural pruning** removes entire components of a neural network (full layers, attention heads, channels) rather than individual sparse weights. This produces a smaller model that runs on standard hardware without special libraries.

### Sub-techniques

| Technique | Description | Status |
|-----------|-------------|--------|
| [ShortGPT](short-gpt.md) | Full layer removal based on attention entropy | 📘 Practical |
| [SlimGPT](short-gpt.md) | Layer-wise structured pruning | 📘 Practical |
| [E3-Pruner](#) | Efficient, economical, effective pruning | 🧪 Emerging |
| [Týr-the-Pruner](#) | Global sparsity-based structural pruning | 🧪 Emerging |

### Cost Impact

- **Memory**: 20-50% parameter reduction
- **Compute**: Proportional FLOPs reduction
- **Latency**: 1.4-2.18× speedup depending on pruning ratio
