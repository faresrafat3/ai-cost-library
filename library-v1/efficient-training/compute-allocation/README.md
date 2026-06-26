# التخصيص الديناميكي للحوسبة | Dynamic Compute Allocation

## العربية

تُشير هذه الفئة إلى تقنيات توزيع موارد الحوسبة (FLOPs) ديناميكياً بين أجزاء النموذج أو بين المدخلات المختلفة. بدلاً من تطبيق نفس كمية الحساب على كل رمز أو عينة، تُخصِّص هذه التقنيات الحوسبة حسب الحاجة.

### التقنيات

| التقنية | الوصف | الحالة |
|---------|-------|--------|
| [Mixture-of-Depths](mixture-of-depths.md) | توجيه ديناميكي للرموز مع ميزانية حوسبة ثابتة | 🧪 ناشئة |
| [Mixture-of-Experts](../parameter-efficient/lora.md) | خبراء متخصصون مع موجِّه (ليس في هذه الفئة مباشرة) | 📘 تطبيقية |

### تأثير التكلفة

- **التدريب**: تخفيض FLOPs لكل تمرير أمامي
- **الاستدلال**: تسريع أخذ العينات حتى 50% (MoD)
- **الطاقة**: توفير نسبي حسب توزيع الرموز

---

## English

This category covers techniques that dynamically distribute compute resources (FLOPs) across model parts or inputs. Instead of applying the same computation to every token, these methods allocate compute based on need.

### Techniques

| Technique | Description | Status |
|-----------|-------------|--------|
| [Mixture-of-Depths](mixture-of-depths.md) | Dynamic token routing with fixed compute budget | 🧪 Emerging |
| [Mixture-of-Experts](../parameter-efficient/lora.md) | Specialized experts with router (not directly in this category) | 📘 Practical |

### Cost Impact

- **Training**: Reduced FLOPs per forward pass
- **Inference**: Up to 50% sampling speedup (MoD)
- **Energy**: Relative savings based on token distribution
