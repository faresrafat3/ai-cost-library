# المعجم العلمي | Scientific Glossary

يحتوي هذا الملف على المصطلحات العلمية المستخدمة في المكتبة مع تعريفاتها العربية والإنجليزية.

This file contains the scientific terminology used throughout the library with Arabic and English definitions.

---

## 📖 مصطلحات التكمية والضغط | Quantization & Compression

| المصطلح الإنجليزي | المصطلح العربي | التعريف العلمي | Scientific Definition |
|---|---|---|---|
| Quantization | التكمية | عملية تحويل الأوزان أو التنشيطات من دقة عالية (مثل FP16) إلى دقة منخفضة (مثل INT4) لتقليل حجم النموذج وتسريع الاستدلال | Converting weights or activations from high precision (e.g., FP16) to low precision (e.g., INT4) to reduce model size and accelerate inference |
| Post-Training Quantization (PTQ) | التكمية بعد التدريب | ضغط النموذج دون الحاجة لإعادة التدريب، باستخدام مجموعة بيانات معايرة صغيرة | Compressing a model without retraining, using a small calibration dataset |
| Quantization-Aware Training (QAT) | التدريب الواعي بالتكمية | تدريب النموذج مع محاكاة تأثير التكمية أثناء عملية التدريب لتحسين الدقة النهائية | Training the model while simulating quantization effects to improve final accuracy |
| Pruning | التقليم | إزالة الأوزان أو الوحدات العصبية غير الضرورية من النموذج لتقليل حجمه وتعقيده | Removing unnecessary weights or neural units from a model to reduce size and complexity |
| Distillation | التقطير | تدريب نموذج صغير (طالب) لتقليد سلوك نموذج كبير (معلّم) مع الحفاظ على الأداء | Training a small student model to mimic a large teacher model while preserving performance |
| Weight Quantization | تكمية الأوزان | تقليل دقة أوزان النموذج فقط مع إبقاء التنشيطات بدقة عالية | Reducing precision of model weights only while keeping activations at high precision |
| Activation Quantization | تكمية التنشيطات | تقليل دقة القيم الوسيطة (التنشيطات) أثناء تمرير البيانات عبر طبقات النموذج | Reducing precision of intermediate values (activations) during forward passes |

## 📖 مصطلحات الاستدلال | Inference

| المصطلح الإنجليزي | المصطلح العربي | التعريف العلمي | Scientific Definition |
|---|---|---|---|
| Inference | الاستدلال | عملية استخدام نموذج مدرب لتوليد مخرجات من مدخلات جديدة دون تحديث أوزانه | Using a trained model to generate outputs from new inputs without updating its weights |
| Latency | الكمون / التأخير | الزمن المستغرق لمعالجة طلب واحد من بدايته إلى نهايته | Time taken to process a single request from start to finish |
| Throughput | الإنتاجية | عدد الطلبات التي يمكن معالجتها في وحدة زمنية واحدة | Number of requests that can be processed per unit of time |
| Batching | التجميع | معالجة عدة طلبات معاً في دفعة واحدة لتحسين كفاءة استخدام العتاد | Processing multiple requests together in a single batch to improve hardware utilization |
| Continuous Batching | التجميع المستمر | تقنية جدولة تزيل الطلبات المنتهية وتُدخل طلبات جديدة في كل خطوة تكرارية | A scheduling technique that removes finished requests and inserts new ones at each iteration |
| Speculative Decoding | فك التشفير التكهني | استخدام نموذج صغير لتوليد رموز مسودة يتحقق منها النموذج الكبير بالتوازي | Using a small model to generate draft tokens that the large model verifies in parallel |
| KV Cache | الذاكرة المؤقتة للمفاتيح والقيم | تخزين حالات التحويل (Key-Value pairs) الناتجة عن الرموز السابقة لتجنب إعادة حسابها | Storing transformer states from previous tokens to avoid recomputation |
| Time To First Token (TTFT) | الزمن حتى أول رمز | مقياس للكمون يقيس الوقت من إرسال الطلب حتى تلقي أول رمز من المخرج | A latency metric measuring time from request submission to receiving the first output token |

## 📖 مصطلحات التدريب | Training

| المصطلح الإنجليزي | المصطلح العربي | التعريف العلمي | Scientific Definition |
|---|---|---|---|
| Fine-tuning | الضبط الدقيق | إعادة تدريب نموذج مُدرَّب مسبقاً على بيانات محددة لمهمة معينة | Retraining a pre-trained model on task-specific data |
| Low-Rank Adaptation (LoRA) | التكيّف منخفض الرتبة | إضافة مصفوفات منخفضة الرتبة قابلة للتدريب إلى طبقات النموذج المجمّد | Adding trainable low-rank matrices to frozen model layers |
| Parameter-Efficient Fine-Tuning (PEFT) | الضبط الدقيق الموفّر للمعاملات | عائلة تقنيات تضبط جزءاً صغيراً فقط من معاملات النموذج مع تجميد الباقي | Techniques that update only a small fraction of model parameters while freezing the rest |
| Gradient Checkpointing | ترقيم النقاط المرجعية للتدرج | تقنية توفّر الذاكرة بإعادة حساب التدرجات بدلاً من تخزينها | A memory-saving technique that recomputes gradients instead of storing them |

## 📖 مصطلحات العتاد والأنظمة | Hardware & Systems

| المصطلح الإنجليزي | المصطلح العربي | التعريف العلمي | Scientific Definition |
|---|---|---|---|
| GPU Memory (VRAM) | ذاكرة وحدة معالجة الرسومات | الذاكرة عالية السرعة المخصصة لوحدة معالجة الرسومات، تحدد حجم النماذج التي يمكن تحميلها | High-speed memory dedicated to the GPU, determining maximum model size that can be loaded |
| Arithmetic Intensity | الكثافة الحسابية | نسبة عدد العمليات الحسابية إلى كمية البيانات المنقولة من الذاكرة | Ratio of computation operations to memory data transfers |
| Memory Bandwidth | عرض النطاق الترددي للذاكرة | السرعة القصوى لنقل البيانات بين الذاكرة ووحدة المعالجة | Maximum rate at which data can be transferred between memory and processor |
| Tensor Core | نواة الموترات | وحدة معالجة متخصصة في مصفوفات GPU مصممة للعمليات الخطية المتوازية | Specialized GPU processing unit designed for parallel linear algebra operations |

## 📖 مصطلحات البيانات والسياق | Data & Context

| المصطلح الإنجليزي | المصطلح العربي | التعريف العلمي | Scientific Definition |
|---|---|---|---|
| Retrieval-Augmented Generation (RAG) | التوليد المعزّز بالاسترجاع | نظام يدمج استرجاع المستندات مع توليد النص لتحسين الدقة وتقليل التكلفة | A system combining document retrieval with text generation to improve accuracy and reduce cost |
| Context Window | نافذة السياق | الحد الأقصى لعدد الرموز التي يمكن للنموذج معالجتها في طلب واحد | Maximum number of tokens a model can process in a single request |
| Token | رمز | الوحدة الأساسية التي يقسّم النموذج النص إليها للمعالجة | The basic unit into which a model splits text for processing |
| Prompt Caching | تخزين الموجهات المؤقت | إعادة استخدام الحسابات السابقة للمقاطع المشتركة بين الطلبات المتعددة | Reusing previous computations for shared text segments across multiple requests |

## 📖 مصطلحات التكلفة والتقييم | Cost & Evaluation

| المصطلح الإنجليزي | المصطلح العربي | التعريف العلمي | Scientific Definition |
|---|---|---|---|
| Cost per Query | تكلفة الاستعلام الواحد | إجمالي التكلفة الحسابية مقسومة على عدد الطلبات المعالجة | Total computational cost divided by number of requests processed |
| Proof Score | درجة الإثبات | تقييم من 1 إلى 4 يقيس مدى نضج الطريقة بناءً على بوابات الأدلة الأربعة | A 1-4 rating measuring method maturity based on the Four Evidence Gates |
| Confidence Level | مستوى الثقة | تصنيف الأدلة إلى: عالية، متوسطة، منخفضة، أو غير متحقق | Evidence classification: High, Medium, Low, or Unverified |
