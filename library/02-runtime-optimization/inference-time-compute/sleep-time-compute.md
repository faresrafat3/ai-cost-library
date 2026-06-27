---
id: entry-sleeptime-001
title_ar: حوسبة وقت النوم
title_en: "Sleep-time Compute"
type: emerging
status: active-research
category: runtime-optimization
subcategory: inference-time-compute
cost_dimensions: [inference-cost, token-cost, latency, compute]
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 4
created: 2026-06-27
scoring:
  A1: 5
  A2: 8
  A3: 8
  A4: 9
  B1: 6
  B2: 0
  B3: 0
  B4: 2
  C1: 6
  C2: 7
  C3: 8
  C4: 6
research_review:
  papers_scanned: 4
  papers_read: 2
  decision: "يُضاف — تقنية جديدة عالية القيمة لتقليل كلفة الاستدلال في الأنظمة ذات السياق المتكرر والاستعلامات المتعددة"
---

# 🧪 حوسبة وقت النوم | Sleep-time Compute

> **التصنيف:** 🧪 ناشئة — بحث واعد لكنه غير مُقنَّن إنتاجياً بعد | **الإثبات:** ⭐⭐

---

## المحتوى العربي

### الفكرة الأساسية

حوسبة وقت النوم هي نقل جزء من "التفكير" المكلف من **وقت الاستدلال** إلى **وقت سابق غير متزامن**، عندما يكون السياق معروفاً مسبقاً لكن سؤال المستخدم لم يصل بعد.

بدلاً من أن يعيد النموذج تحليل السياق نفسه مع كل استعلام جديد، يمكنه في وقت الخمول أن:
- يستنتج أسئلة محتملة،
- يستخرج حقائق أو بنى وسيطة مفيدة،
- ويُنشئ تمثيلاً مُعاد الصياغة للسياق.

ثم يُستخدم هذا التمثيل لاحقاً لتقليل حوسبة وقت الطلب، وخفض الكمون، وأحياناً تحسين الدقة أيضاً.

### لماذا تهم اقتصادياً؟

تقنيات **حوسبة وقت الاستدلال** ترفع الجودة عبر إنفاق توكنات وحوسبة إضافية أثناء الإجابة، لكنها تدفع الثمن في:
- الكمون،
- تكلفة التوكنات،
- وتكرار التفكير نفسه على السياق نفسه.

حوسبة وقت النوم تحاول علاج هذا الهدر عندما يكون النظام:
- **حاليّاً/مستمراً stateful** لا عديم الحالة،
- ويعمل فوق **سياق دائم أو شبه دائم** مثل:
  - مستودع برمجي،
  - ملفات قضية أو عقود،
  - قاعدة معرفة داخلية،
  - محادثات طويلة العمر،
  - أو وثائق RAG تتكرر الأسئلة حولها.

### ماذا تُظهر الأدلة الحالية؟

#### 1) خفض حوسبة وقت الاستدلال لنفس الدقة
ورقة Sleep-time Compute تُظهر أن التقنية تستطيع **تقليل مقدار حوسبة وقت الاستدلال المطلوبة للوصول إلى نفس الدقة بحوالي 5×** على Stateful GSM-Symbolic وStateful AIME. هذا أهم دليل اقتصادي مباشر: نفس الجودة تقريباً لكن باعتماد أكبر على الحوسبة المسبقة بدلاً من الحوسبة التفاعلية.

#### 2) خفض متوسط التكلفة لكل سؤال عند تكرار الاستعلامات
عندما توجد **عدة أسئلة مرتبطة على نفس السياق**، استطاعت الورقة **خفض متوسط التكلفة لكل سؤال بمقدار 2.5×** عبر توزيع كلفة الحوسبة المسبقة على عدة استعلامات لاحقة.

#### 3) تحسين الجودة عند توسيع الحوسبة المسبقة
أظهرت النتائج أيضاً أن زيادة حوسبة وقت النوم قد ترفع الدقة نفسها **حتى 13%** على Stateful GSM-Symbolic و**حتى 18%** على Stateful AIME، ما يعني أن التقنية ليست مجرد خفض تكلفة، بل قد تحسن نقطة التوازن بين الجودة والكمون والتكلفة.

### أين تكون مفيدة فعلاً؟

#### مفيدة جداً عندما:
- يكون **السياق ثابتاً نسبياً** بين عدة أسئلة.
- تكون الأسئلة **قابلة للتنبؤ جزئياً** من السياق.
- يكون **الكمون التفاعلي** غالي الثمن أو حساساً.
- يكون النظام وكيلاً يتعامل مع **ملف عمل طويل العمر**.

#### فائدتها أضعف عندما:
- تكون الأسئلة عشوائية وغير متوقعة.
- يتغير السياق بسرعة عالية.
- تكون تكلفة الحوسبة المسبقة نفسها أعلى من الوفر الناتج.
- يكون الاستعلام **وحيداً** على كل سياق ولا يوجد تكرار أو إعادة استخدام.

### العلاقة بإدخالات المكتبة الأخرى

- **Inference-Time Compute:** حوسبة وقت النوم لا تلغيها، بل تعيد توزيعها زمنياً.
- **Prompt / Prefix Caching:** التخزين المؤقت يعيد استخدام حسابات متطابقة أو متشابهة، أما حوسبة وقت النوم فتضيف **استدلالاً جديداً مسبقاً** على السياق.
- **Semantic Caching:** التخزين الدلالي يمنع بعض الاستدعاءات؛ حوسبة وقت النوم تُخفف تكلفة الاستدعاءات التي ما زالت ضرورية.
- **Context Compression:** ضغط السياق يقلل حجم المدخل؛ حوسبة وقت النوم تُحسن محتوى المدخل نفسه.
- **RAG Cost Optimization:** يمكن استخدام حوسبة وقت النوم بعد الاسترجاع المتكرر لاستخراج تمثيل أرخص للسياقات كثيرة الاستعمال.

### التقييم وفق البوابات الأربع

| البوابة | الحكم | السبب |
|---|---|---|
| Built | ✅ نعم | يوجد كود وبيانات منشورة من الباحثين |
| Tested | ✅ نعم | تم تقييمها على مجموعات Stateful AIME وStateful GSM-Symbolic ودراسة حالة SWE |
| Deployed | ❌ ليس بعد بشكل واسع | لا توجد أدلة قوية على انتشار إنتاجي واسع متعدد المؤسسات |
| Saved | ⚠️ جزئياً | يوجد خفض مُوثق في تكلفة/حوسبة الاختبار داخل الورقة، لكن ليس بعد بدراسات إنتاجية كبيرة |

**النتيجة:** التقنية **واعدة جداً لكن ما تزال ناشئة**؛ لا تستحق تصنيف 📘 Practical بعد.

### القيود والمخاطر

1. **تعتمد على قابلية التنبؤ بالاستعلامات**: إذا كانت الأسئلة المقبلة غير قابلة للتوقع، قد تصبح الحوسبة المسبقة هدراً.
2. **تعقيد هندسي أعلى**: تحتاج طبقة orchestration بين الحالة الحالية، والتجهيز المسبق، والاستعلام الفعلي.
3. **خطر التقادم**: إذا تغيّر السياق بعد الحوسبة المسبقة، فقد تصبح الاستنتاجات القديمة غير صالحة.
4. **تكلفة خفية**: بعض الفرق قد تظن أنها خفضت تكلفة وقت الطلب بينما هي فقط نقلت التكلفة إلى الخلفية دون قياس شامل.
5. **أدلة الإنتاج ما تزال محدودة**: الأدلة الحالية قوية بحثياً لكنها ليست بعد دراسات سوقية واسعة.

### الحكم العملي

- **للباحثين وبناة الوكلاء:** موضوع شديد الأهمية ويستحق التجريب.
- **لفرق الإنتاج:** مناسب كبنية تجريبية في الأنظمة ذات السياق الطويل والمتكرر، لكن ليس بعد كافتراض افتراضي عام.
- **للمكتبة:** إدخال عالي القيمة لأنه يفتح فئة تصميمية جديدة: **تحويل الحوسبة من لحظة الطلب إلى ما قبل الطلب**.

---

## English Content

### Core idea

Sleep-time compute shifts part of expensive reasoning from **interactive inference time** to an **offline pre-query phase**, when the context is already available but the user’s next question has not yet arrived.

Instead of repeatedly re-analyzing the same context for every new query, the system can use idle time to:
- anticipate likely questions,
- infer useful intermediate facts or structures,
- and rewrite the context into a more useful representation.

That precomputed representation is then used at request time to reduce latency, token usage, and inference-time compute.

### Why it matters economically

Inference-time scaling often improves accuracy by spending more compute during response generation, but this increases:
- latency,
- token cost,
- and repeated reasoning over the same context.

Sleep-time compute attacks that waste in **stateful systems** with reused context, such as code assistants, persistent knowledge bases, long-lived chats, legal/corporate document agents, and repeated-query RAG workflows.

### What the current evidence shows

1. The original paper reports that sleep-time compute can **reduce the amount of test-time compute needed to reach the same accuracy by ~5×** on Stateful GSM-Symbolic and Stateful AIME.
2. For multiple related questions over the same context, it can **reduce average cost per query by 2.5×** through amortization.
3. Increasing sleep-time compute can also improve quality itself, with **up to 13%** accuracy gains on Stateful GSM-Symbolic and **up to 18%** on Stateful AIME.

### When it works best

Best fit:
- reusable or slowly changing context,
- partially predictable future queries,
- high value on low interactive latency,
- long-lived agent state.

Weak fit:
- highly unpredictable queries,
- rapidly changing context,
- one-off questions per context,
- environments where background compute cannot be justified.

### Relationship to adjacent techniques

- **Inference-Time Compute:** sleep-time compute complements it by moving part of the reasoning budget earlier.
- **Prompt/Prefix Caching:** caching reuses prior identical/shared computation; sleep-time compute adds new anticipatory reasoning.
- **Semantic Caching:** semantic caching avoids some calls entirely; sleep-time compute reduces the cost of calls that still need to happen.
- **Context Compression:** compression shrinks context length; sleep-time compute improves context usefulness.

### Four-gate assessment

- **Built:** Yes — public code and datasets exist.
- **Tested:** Yes — evaluated on stateful reasoning benchmarks plus an agentic SWE case study.
- **Deployed:** Not broadly proven.
- **Saved:** Partially — strong paper evidence, but limited large-scale production validation.

### Bottom line

Sleep-time compute is a **high-upside emerging technique** for stateful agent systems. It is not yet a default production pattern, but it may become an important design primitive for reducing interactive AI cost in multi-query settings.

---

## المصادر | Sources

1. **[Tier 1]** Lin, K., Snell, C., Wang, Y., Packer, C., Wooders, S., Stoica, I., Gonzalez, J. E., "Sleep-time Compute: Beyond Inference Scaling at Test-time," arXiv:2504.13171, April 2025. مباشر: ~5× تقليل حوسبة وقت الاختبار لنفس الدقة، و2.5× خفض متوسط التكلفة لكل سؤال، و13-18% تحسن دقة.
2. **[Tier 2]** Letta + UC Berkeley, "sleep-time-compute" code repository, GitHub, April 2025. دليل البناء وإتاحة الكود والبيانات.
3. **[Tier 2]** Letta documentation, "Sleep-time agents developer docs," 2025-2026. دليل تطبيقي لفكرة الوكلاء المعتمدين على sleep-time.
4. **[Tier 2]** Sadhukhan, R., et al., "Kinetics: Rethinking Test-Time Scaling Laws," arXiv:2506.05333, June 2025. مرجع مكمل يوضح أن تكلفة وقت الاختبار ليست مجرد FLOPs بل تتأثر بشدة بكلفة الذاكرة والانتباه.
