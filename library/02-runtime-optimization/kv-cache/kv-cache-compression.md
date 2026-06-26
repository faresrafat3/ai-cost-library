---
id: entry-kvcachecompress-001
title_ar: ضغط ذاكرة KV المؤقتة
title_en: KV Cache Compression & Eviction
type: emerging
status: active-research
category: runtime-optimization
subcategory: kv-cache
tree_path: "AI Cost Library → Runtime Optimization → KV Cache → KV Cache Compression"
cost_dimensions:
  - memory
  - inference-cost
  - throughput
  - latency
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 4
created: 2026-06-26
updated: 2026-06-26
research_review:
  papers_scanned: 4
  papers_fully_read: 2
  decision: "يُضاف كإدخال ناشئ جامع — مجال بحثي نشط جداً في 2026 مع 4+ أبحاث جديدة"
  limitations_noted: "لا توجد تقارير نشر إنتاجي لأي منها بعد. معظمها preprints."
---

# 🧪 ضغط ذاكرة KV المؤقتة | KV Cache Compression & Eviction

> **التصنيف:** 🧪 ناشئة — مجال بحثي نشط جداً | **الإثبات:** ⭐⭐ نموذج أولي
>
> **المسار:** المكتبة ← تحسين التشغيل ← ذاكرة KV ← الضغط

---

## المحتوى العربي

### ما هو ضغط ذاكرة KV؟

ضغط ذاكرة KV المؤقتة (KV Cache Compression) — وهو مجموعة تقنيات تُقلل حجم الذاكرة المؤقتة المستخدمة لتخزين مفاتيح وقيم الانتباه أثناء الاستدلال، مما يسمح بمعالجة سياقات أطول بذاكرة أقل.

### لماذا هذا مهم؟

ذاكرة KV تنمو **خطياً** مع طول السياق. لنموذج 70B مع سياق 128K:
- KV Cache بـ FP16: ~40-80 جيجابايت (قد تتجاوز ذاكرة GPU كاملة!)
- هذا يحدّ عدد الطلبات المتزامنة وطول السياق الممكن

### الأبحاث الحديثة المُراجعة (2026)

#### 1. CompressKV — ضغط دلالي (يونيو 2026)
**arXiv:2606.24467 — TU Darmstadt**

ما قرأت من الورقة:
- يحدد "رؤوس الاسترجاع الدلالي" (Semantic Retrieval Heads) — رؤوس انتباه مسؤولة عن استرجاع المعلومات المهمة
- يستخدم هذه الرؤوس فقط لتقرير أي أزواج KV يُحتفظ بها
- يوزّع ميزانية التخزين عبر الطبقات حسب خطأ الإخراج المقدّر

**النتائج:**
| الادعاء | القيمة |
|---------|--------|
| الاحتفاظ بالأداء مع 3% فقط من KV cache | 97% من أداء التخزين الكامل |
| دقة Needle-in-a-Haystack مع 0.7% من التخزين | 90% |

**القرار:** ناشئ — نتائج مبهرة جداً لكن preprint حديث جداً (يونيو 2026) بدون تبنٍّ بعد.

#### 2. Fast KVzip — إخراج بالبوابات (يناير 2026)
**arXiv:2601.17668**

- يُضيف بوابات خفيفة لكل طبقة انتباه لتقييم أهمية أزواج KV
- التدريب يعتمد على forward passes فقط (بدون backpropagation مكلف)
- **النتيجة:** إخراج 70% من KV cache مع الحفاظ على الأداء
- مُختبر على Qwen2.5-1M, Qwen3, Gemma3

**القرار:** ناشئ — منهجية أنيقة لكن preprint.

#### 3. IndexMem — ذاكرة كامنة للمُخرَج (مايو 2026)
**arXiv:2605.25475**

- يتعلم "مُفهرِس" (indexer) يتنبأ بأهمية KV
- يضغط التوكنات المُخرَجة في حالة كامنة مُحدَّثة (latent memory)
- **النتيجة:** +25 نقطة على RULER تحت الضغط الشديد

**القرار:** ناشئ — واعد لكن معقد التطبيق.

#### 4. LaProx — إخراج واعٍ بالمخرجات (مايو 2026)
**arXiv:2605.07234**

- يُعيد صياغة مشكلة الإخراج كتقريب لضرب مصفوفات
- يحقق أداء كامل مع **5% فقط** من KV cache
- **النتيجة:** 2× تقليل في فقدان الدقة مقابل الطرق السابقة

**القرار:** ناشئ — نهج رياضي أنيق.

### لماذا ⭐⭐ وليس أعلى؟

- ✅ **بوابة 1 (مبني):** نعم — أكواد منشورة لمعظمها
- ✅ **بوابة 2 (مُختبر):** نعم — معايير أكاديمية (LongBench, RULER, NIAH)
- ❌ **بوابة 3 (مُنشَر):** لا — لا يوجد نشر إنتاجي لأي منها بعد
- ❌ **بوابة 4 (وفَّر):** لا — لا توجد أرقام وفر فعلية

### متى تستخدم (مستقبلاً)

- ✅ نماذج تحتاج سياق طويل (>32K) على عتاد محدود الذاكرة
- ✅ خدمة كثيفة التزامن حيث KV cache هو عنق الزجاجة

### المخاطر

1. **جميعها preprints** — لم تُراجع من أقران بعد (باستثناء CompressKV الذي لديه كود عام).
2. **تعقيد التكامل** — تحتاج تعديل محرك الاستدلال.
3. **تفاعل مع تقنيات أخرى** — التفاعل مع FP8, speculative decoding غير مدروس.

---

## English Content

KV cache compression is an active 2026 research area with 4+ new papers. Key results:
- **CompressKV:** 97% performance with only 3% KV cache (June 2026)
- **Fast KVzip:** Evicts 70% of KV cache with negligible loss (Jan 2026)
- **IndexMem:** +25 points on RULER under aggressive eviction (May 2026)
- **LaProx:** Full performance with 5% KV cache (May 2026)

All are preprints without production deployment. Classified as Emerging ⭐⭐.

---

## المصادر | Sources

1. **[Tier 2]** Lin, X., et al., "CompressKV: Semantic-Retrieval-Guided KV-Cache Compression", arXiv:2606.24467, June 2026. TU Darmstadt. Code: github.com/TUDa-HWAI/CompressKV
2. **[Tier 2]** Kim, J.-H., et al., "Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction", arXiv:2601.17668, January 2026.
3. **[Tier 2]** Yang, X., et al., "IndexMem: Learned KV-Cache Eviction with Latent Memory", arXiv:2605.25475, May 2026.
4. **[Tier 2]** Mai, T., et al., "LaProx: Reformulating KV Cache Eviction Problem", arXiv:2605.07234, May 2026.
