# قوالب الإدخالات | Entry Templates

## 📘 قالب الإدخال التطبيقي | Practical Entry Template

```yaml
---
id: "entry-XXX-001"
title_ar: "العنوان العربي"
title_en: "English Title"
type: "Practical"
status: "Deployed"
category: "الفئة"
subcategory: "الفئة الفرعية"
tree_path: ["L1", "L2", "Entry"]
cost_dimensions: ["memory", "inference-cost", "latency"]
proof_score: 4
sources_count: 2
---
```

الملف يجب أن يحتوي على:
1. ملخص عربي علمي دقيق
2. English Summary أكاديمي
3. أبعاد التكلفة المتأثرة
4. بوابات الأدلة الأربعة (Built, Tested, Deployed, Saved)
5. القيود والمخاطر
6. المصادر بتنسيق: [Tier] Author, "Title", Venue, Year, URL
7. إدخالات ذات صلة

## 🧪 قالب الإدخال الناشئ | Emerging Entry Template

نفس الهيكل لكن:
- `type: "Emerging"`
- `status: "Research"`
- `proof_score: 2`
- حالة البحث بدلاً من بوابات الأدلة
- المسار المتوقع إلى الإنتاج

## 📐 قالب الإدخال النظري | Theoretical Entry Template

نفس الهيكل لكن:
- `type: "Theoretical"`
- `status: "Academic"`
- `proof_score: 1`
- الأساس الرياضي/النظري
- الفجوة بين النظرية والتطبيق
- البحث المطلوب
