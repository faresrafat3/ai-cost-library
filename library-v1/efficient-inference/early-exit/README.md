# الإنهاء المبكر | Early Exit

## العربية

يُشير **الإنهاء المبكر** إلى فئة من تقنيات الاستدلال التكيفي التي تسمح للشبكة العصبية بإصدار تنبؤ بعد مرور جزئي عبر طبقاتها، بدلاً من المرور الكامل عبر جميع الطبقات. الفكرة الأساسية هي أن العينات "السهلة" لا تحتاج إلى حساب كامل، بينما العينات "الصعبة" تستفيد من الطبقات الأعمق.

### كيف يعمل

1. تُضاف رؤوس تصنيف مساعدة (auxiliary classifier heads) عند طبقات وسيطة محددة.
2. أثناء الاستدلال، يُقيَّم مقياس ثقة (confidence score) عند كل رأس.
3. إذا تجاوز المقياس عتبة محددة، يتوقف النموذج ويُعيد الناتج من تلك النقطة.
4. إذا لم تتجاوز العتبة، يستمر الحساب إلى الطبقة التالية.

### تقنيات فرعية

| التقنية | الوصف | الحالة |
|---------|-------|--------|
| [SpecExit](../decoding/speculative-decoding.md) | إنهاء مبكر مع ترميز تخميني للاستدلال المنطقي | 📘 تطبيقية |
| [LayerSkip](layer-skip.md) | قفز طبقات مع فك ترميز تخميني ذاتي | 📘 تطبيقية |
| الإنهاء المبكر التقليدي | رؤوس مساعدة مع عتبات ثقة | 📘 تطبيقية (لنماذج التصنيف) |
| الإنهاء المبكر في LLMs | إنفاذ عند مستوى الرموز في نماذج التوليد | 🧪 ناشئة |

### تأثير التكلفة

- **الحوسبة**: تخفيض 60-80% في FLOPs للعينات السهلة
- **الزمنية**: تسريع 2-5× في مهام التوليد
- **الطاقة**: توفير 26%+ في استهلاك الطاقة
- **الذاكرة**: لا تخفيض مباشر في الذاكرة (يتطلب آليات KV Cache إضافية)

### المصادر

- [Tier 2] Elhoushi et al., "LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding", ACL 2024, DOI: 10.18653/v1/2024.acl-long.681
- [Tier 2] Yang et al., "SpecExit: Accelerating Large Reasoning Model via Speculative Exit", arXiv:2509.29Sep2025
- [Tier 2] Bajpai et al., "BEEM: Early-Exit Aggregation", arXiv:2025

---

## English

**Early Exit** refers to a class of adaptive inference techniques that allow a neural network to emit a prediction after a partial forward pass through its layers, rather than traversing all layers. The core idea is that "easy" samples don't need full computation, while "hard" samples benefit from deeper layers.

### How It Works

1. Auxiliary classifier heads are inserted at specific intermediate layers.
2. During inference, a confidence score is evaluated at each head.
3. If the score exceeds a threshold, the model exits and returns the prediction.
4. Otherwise, computation continues to the next layer.

### Sub-techniques

| Technique | Description | Status |
|-----------|-------------|--------|
| [SpecExit](../decoding/speculative-decoding.md) | Early exit with speculative decoding for reasoning | 📘 Practical |
| [LayerSkip](layer-skip.md) | Layer skipping with self-speculative decoding | 📘 Practical |
| Traditional Early Exit | Auxiliary heads with confidence thresholds | 📘 Practical (classification models) |
| Early Exit in LLMs | Token-level exits in generative models | 🧪 Emerging |

### Cost Impact

- **Compute**: 60-80% FLOPs reduction for easy samples
- **Latency**: 2-5× speedup in generation tasks
- **Energy**: 26%+ energy savings
- **Memory**: No direct reduction (requires additional KV Cache mechanisms)

### Sources

- [Tier 2] Elhoushi et al., "LayerSkip: Enabling Early Exit Inference and Self-Speculative Decoding", ACL 2024, DOI: 10.18653/v1/2024.acl-long.681
- [Tier 2] Yang et al., "SpecExit: Accelerating Large Reasoning Model via Speculative Exit", arXiv:2509.29Sep2025
- [Tier 2] Bajpai et al., "BEEM: Early-Exit Aggregation", arXiv:2025
