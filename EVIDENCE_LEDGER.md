# سجل الأدلة | Evidence Ledger

> **آخر تحديث: 2026-09-04 (round 74)**
>
> **ملاحظة عن drift (2026-09-04)**: هذا الملف **يحوي نفس جدول الادعاءات** الموجود في `CLAIMS.md` — وهو الـ canonical claim ledger الأمثل للقراءة السريعة. الـ canonical **evidence ledger** الفعلي موجود في `data/evidence.json` (19 بند: `EV-001` إلى `EV-019`، تربط ادعاءات `CL-NNN` بأدلة Tier 1/2/3).
>
> حسب السياسة (NO_HYPE_POLICY.md، QUALITY_CHECKLIST.md، CONTRIBUTING.md):
> - `EVIDENCE_LEDGER.md` يجب أن يطابق `data/evidence.json` (الأدلة)
> - `CLAIMS.md` يجب أن يطابق `data/claims.json` (الادعاءات)
> - لكن تاريخياً الاثنين يحويان نفس جدول الـ 15 ادعاء المختار — drift موثّق هنا دون إصلاح هيكلي.
>
> الإصلاح الصحيح (out of scope لهذه الجلسة): إعادة بناء `EVIDENCE_LEDGER.md` ليحوي 19 بند `EV-NNN` من JSON، مع روابط للـ claims المرتبطة. حالياً يبقى متطابقاً مع CLAIMS.md لأسباب backward-compat (عدة ملفات تشير إليه: README.md, PULL_REQUEST_TEMPLATE, QUALITY_CHECKLIST, NO_HYPE_POLICY, CONTRIBUTING, internal/NEXT_ACTIONS).
>
> **Drift note (2026-09-04)**: This file currently contains the **same claim table as `CLAIMS.md`** — it should be the evidence ledger but historically mirrors the claims ledger. The canonical evidence ledger is in `data/evidence.json` (19 items, `EV-001` to `EV-019`, linking `CL-NNN` claims to Tier 1/2/3 evidence).
>
> Per the policy docs, EVIDENCE_LEDGER.md should match `data/evidence.json` and CLAIMS.md should match `data/claims.json`, but historically both MD files contain the same 15-claim curated table. The structural fix (rebuild this file from `data/evidence.json`) is out of scope for a sync round; preserved as-is for backward-compat with the 6+ files that link to it.

يسجل هذا الملف الأدلة والادعاءات المهمة المرتبطة بتقليل التكلفة أو الذاكرة أو الكمون. كل ادعاء مرتبط بمعرّف مصدر في `data/sources.json`.

This file records important AI cost-reduction claims. Each claim links to source identifiers in `data/sources.json`.

| Claim ID | Entry | Metric | Claim | Sources | Confidence |
|---|---|---|---|---|---|
| `CLAIM-GPTQ-01` | `entry-gptq-001` | memory/storage | تكمية الأوزان إلى 3 أو 4 بت تخفض الذاكرة النظرية بنحو 4-5× مقارنة بـ FP16، مع قياسات دقة قريبة من الأصل في نماذج OPT كبيرة.<br><br>3/4-bit weight quantization provides roughly 4-5× theoretical weight memory reduction versus FP16 with near-baseline accuracy in large OPT experiments. | SRC-GPTQ-2023 | high |
| `CLAIM-GPTQ-02` | `entry-gptq-001` | quantization time | أبلغت الورقة عن تكمية نموذج 175B خلال نحو أربع ساعات GPU.<br><br>The paper reports quantizing a 175B model in about four GPU hours. | SRC-GPTQ-2023 | high |
| `CLAIM-AWQ-01` | `entry-awq-001` | latency/edge serving | أظهر TinyChat المرتبط بـ AWQ تسريعاً يتجاوز 3× مقارنة بتنفيذ Hugging Face FP16 على حواسيب مكتبية ومحمولة في تجارب الورقة.<br><br>TinyChat with AWQ reports more than 3× speedup over Hugging Face FP16 on desktop and mobile GPUs. | SRC-AWQ-2024 | high |
| `CLAIM-SQ-01` | `entry-smoothquant-001` | memory/accuracy | تنقل SmoothQuant صعوبة التكمية من التنشيطات إلى الأوزان لتمكين W8A8 مع فقد دقة صغير في نماذج كبيرة.<br><br>SmoothQuant migrates quantization difficulty from activations to weights, enabling W8A8 quantization with small accuracy loss on large models. | SRC-SMOOTHQUANT-2023 | high |
| `CLAIM-INT8-01` | `entry-llmint8-001` | memory | تخفض LLM.int8() ذاكرة الأوزان تقريباً إلى النصف مقارنة بـ FP16 مع معالجة القيم الشاذة بدقة أعلى.<br><br>LLM.int8() roughly halves weight memory compared with FP16 while handling outlier features in higher precision. | SRC-LLMINT8-2022 | high |
| `CLAIM-SPECDEC-01` | `entry-specdec-001` | latency | يمكن لفك التشفير التكهني إعطاء تسريع يقارب 2-3× في ظروف يكون فيها نموذج المسودة جيداً وتكلفة التحقق مناسبة.<br><br>Speculative decoding can provide about 2-3× speedups when the draft model is accurate enough and verification overhead is favorable. | SRC-SPECDEC-2023 | high |
| `CLAIM-CBATCH-01` | `entry-contbatching-001` | throughput | أظهر Orca تحسينات كبيرة في إنتاجية تقديم النماذج عبر جدولة على مستوى التكرار بدلاً من التجميع الثابت.<br><br>Orca demonstrates substantial serving throughput gains via iteration-level scheduling rather than static request batching. | SRC-ORCA-2022 | high |
| `CLAIM-PA-01` | `entry-pagedattention-001` | memory waste | يخفض PagedAttention هدر ذاكرة KV Cache إلى أقل من 4% مقارنة بهدر كبير في التخصيص التقليدي.<br><br>PagedAttention reduces KV-cache memory waste to below 4% compared with much higher waste under conventional allocation. | SRC-VLLM-2023 | high |
| `CLAIM-PA-02` | `entry-pagedattention-001` | throughput | أبلغ vLLM عن إنتاجية أعلى بنحو 2-4× مقارنة بأنظمة تقديم سابقة في أحمال متعددة.<br><br>vLLM reports roughly 2-4× throughput gains over prior serving systems across multiple workloads. | SRC-VLLM-2023 | high |
| `CLAIM-RA-01` | `entry-radixattention-001` | prefix reuse | يوفر RadixAttention إعادة استخدام منظمة للبادئات المشتركة في البرامج اللغوية، لكن مقدار الوفر يعتمد بشدة على نمط الحمل.<br><br>RadixAttention enables structured reuse of shared prefixes in language-model programs, but savings depend strongly on workload shape. | SRC-SGLANG-2023 | medium |
| `CLAIM-LORA-01` | `entry-lora-001` | trainable parameters | تخفض LoRA عدد المعاملات القابلة للتدريب بعدة رتب مقدارية مقارنة بالضبط الكامل، وقد تصل في تجارب GPT-3 إلى 10,000×.<br><br>LoRA reduces trainable parameters by orders of magnitude compared with full fine-tuning, up to 10,000× in GPT-3 experiments. | SRC-LORA-2022 | high |
| `CLAIM-LORA-02` | `entry-lora-001` | checkpoint storage | تخفض LoRA حجم نقاط الحفظ الخاصة بكل مهمة بدرجة كبيرة لأنها تخزن مصفوفات منخفضة الرتبة بدلاً من نسخة كاملة من النموذج.<br><br>LoRA greatly reduces per-task checkpoint storage by saving low-rank matrices rather than a full model copy. | SRC-LORA-2022 | high |
| `CLAIM-QLORA-01` | `entry-qlora-001` | GPU memory | أتاحت QLoRA ضبط نموذج 65B على بطاقة واحدة بسعة 48GB مع الحفاظ على أداء قريب من الضبط الكامل 16-بت.<br><br>QLoRA enabled fine-tuning a 65B model on a single 48GB GPU while preserving near 16-bit fine-tuning performance. | SRC-QLORA-2023 | high |
| `CLAIM-PCACHE-01` | `entry-promptcache-001` | api/token cost | يوفر تخزين الموجهات المؤقت خصومات على أجزاء الموجه المتكررة في واجهات تجارية، لكن مقدار الوفر يتغير حسب المزود وطول البادئة ونمط الطلبات.<br><br>Prompt caching can discount repeated prompt prefixes in commercial APIs, but realized savings vary by provider, prefix length, and traffic pattern. | SRC-OPENAI-PROMPT-CACHING, SRC-ANTHROPIC-PROMPT-CACHING | medium |
| `CLAIM-PCACHE-02` | `entry-promptcache-001` | latency | توضح أبحاث Prompt Cache أن إعادة استخدام الانتباه يمكن أن تخفض زمن الاستجابة للبادئات المتكررة، مع اعتماد الأثر على قابلية مشاركة السياق.<br><br>Prompt Cache research shows attention reuse can reduce latency for repeated prefixes, with impact depending on context shareability. | SRC-PROMPTCACHE-2023 | medium |
