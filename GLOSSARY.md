# المعجم العلمي | Scientific Glossary

كل مصطلح تقني جديد في المكتبة يجب أن يظهر هنا وفي `data/glossary.json`. العربية العلمية مقدمة أولاً، ثم المقابل الإنجليزي.

Every technical term used by the library should appear here and in `data/glossary.json`.

| المصطلح العربي | English Term | تعريف عربي | English Definition |
|---|---|---|---|
| التكمية | Quantization | عملية تحويل الأوزان أو التنشيطات من دقة عالية إلى دقة منخفضة لتقليل حجم النموذج وتسريع الاستدلال | Converting weights or activations from high precision to low precision to reduce model size and accelerate inference |
| التكمية بعد التدريب | Post-Training Quantization | ضغط النموذج دون الحاجة لإعادة التدريب، باستخدام مجموعة بيانات معايرة صغيرة | Compressing a model without retraining, using a small calibration dataset |
| التدريب الواعي بالتكمية | Quantization-Aware Training | تدريب النموذج مع محاكاة تأثير التكمية أثناء عملية التدريب لتحسين الدقة النهائية | Training the model while simulating quantization effects to improve final accuracy |
| التقليم | Pruning | إزالة الأوزان أو الوحدات العصبية غير الضرورية من النموذج لتقليل حجمه وتعقيده | Removing unnecessary weights or neural units from a model to reduce size and complexity |
| التقطير | Distillation | تدريب نموذج صغير (طالب) لتقليد سلوك نموذج كبير (معلّم) مع الحفاظ على الأداء | Training a small student model to mimic a large teacher model while preserving performance |
| تكمية الأوزان | Weight Quantization | تقليل دقة أوزان النموذج فقط مع إبقاء التنشيطات بدقة عالية | Reducing precision of model weights only while keeping activations at high precision |
| تكمية التنشيطات | Activation Quantization | تقليل دقة القيم الوسيطة (التنشيطات) أثناء تمرير البيانات عبر طبقات النموذج | Reducing precision of intermediate values (activations) during forward passes |
| الاستدلال | Inference | عملية استخدام نموذج مدرب لتوليد مخرجات من مدخلات جديدة دون تحديث أوزانه | Using a trained model to generate outputs from new inputs without updating its weights |
| الكمون / التأخير | Latency | الزمن المستغرق لمعالجة طلب واحد من بدايته إلى نهايته | Time taken to process a single request from start to finish |
| الإنتاجية | Throughput | عدد الطلبات التي يمكن معالجتها في وحدة زمنية واحدة | Number of requests that can be processed per unit of time |
| التجميع | Batching | معالجة عدة طلبات معاً في دفعة واحدة لتحسين كفاءة استخدام العتاد | Processing multiple requests together in a single batch to improve hardware utilization |
| التجميع المستمر | Continuous Batching | تقنية جدولة تزيل الطلبات المنتهية وتُدخل طلبات جديدة في كل خطوة تكرارية | A scheduling technique that removes finished requests and inserts new ones at each iteration |
| فك التشفير التكهني | Speculative Decoding | استخدام نموذج صغير لتوليد رموز مسودة يتحقق منها النموذج الكبير بالتوازي | Using a small model to generate draft tokens that the large model verifies in parallel |
| الذاكرة المؤقتة للمفاتيح والقيم | KV Cache | تخزين حالات التحويل (Key-Value pairs) الناتجة عن الرموز السابقة لتجنب إعادة حسابها | Storing transformer states from previous tokens to avoid recomputation |
| الزمن حتى أول رمز | Time To First Token | مقياس للكمون يقيس الوقت من إرسال الطلب حتى تلقي أول رمز من المخرج | A latency metric measuring time from request submission to receiving the first output token |
| الضبط الدقيق | Fine-tuning | إعادة تدريب نموذج مُدرَّب مسبقاً على بيانات محددة لمهمة معينة | Retraining a pre-trained model on task-specific data |
| التكيّف منخفض الرتبة | Low-Rank Adaptation | إضافة مصفوفات منخفضة الرتبة قابلة للتدريب إلى طبقات النموذج المجمّد | Adding trainable low-rank matrices to frozen model layers |
| الضبط الدقيق الموفّر للمعاملات | Parameter-Efficient Fine-Tuning | عائلة تقنيات تضبط جزءاً صغيراً فقط من معاملات النموذج مع تجميد الباقي | Techniques that update only a small fraction of model parameters while freezing the rest |
| ترقيم النقاط المرجعية للتدرج | Gradient Checkpointing | تقنية توفّر الذاكرة بإعادة حساب التدرجات بدلاً من تخزينها | A memory-saving technique that recomputes gradients instead storing them |
| ذاكرة وحدة معالجة الرسومات | GPU Memory | الذاكرة عالية السرعة المخصصة لوحدة معالجة الرسومات، تحدد حجم النماذج التي يمكن تحميلها | High-speed memory dedicated to the GPU, determining maximum model size that can be loaded |
| الكثافة الحسابية | Arithmetic Intensity | نسبة عدد العمليات الحسابية إلى كمية البيانات المنقولة من الذاكرة | Ratio of computation operations to memory data transfers |
| عرض النطاق الترددي للذاكرة | Memory Bandwidth | السرعة القصوى لنقل البيانات بين الذاكرة ووحدة المعالجة | Maximum rate at which data can be transferred between memory and processor |
| نواة الموترات | Tensor Core | وحدة معالجة متخصصة في مصفوفات GPU مصممة للعمليات الخطية المتوازية | Specialized GPU processing unit designed for parallel linear algebra operations |
| التوليد المعزّز بالاسترجاع | Retrieval-Augmented Generation | نظام يدمج استرجاع المستندات مع توليد النص لتحسين الدقة وتقليل التكلفة | A system combining document retrieval with text generation to improve accuracy and reduce cost |
| نافذة السياق | Context Window | الحد الأقصى لعدد الرموز التي يمكن للنموذج معالجتها في طلب واحد | Maximum number of tokens a model can process in a single request |
| رمز | Token | الوحدة الأساسية التي يقسّم النموذج النص إليها للمعالجة | The basic unit into which a model splits text for processing |
| تخزين الموجهات المؤقت | Prompt Caching | إعادة استخدام الحسابات السابقة للمقاطع المشتركة بين الطلبات المتعددة | Reusing previous computations for shared text segments across multiple requests |
| تكلفة الاستعلام الواحد | Cost per Query | إجمالي التكلفة الحسابية مقسومة على عدد الطلبات المعالجة | Total computational cost divided by number of requests processed |
| محرك تقديم النماذج | Serving Engine | نظام برمجي يدير استقبال طلبات الاستدلال وجدولتها وتنفيذها على المسرّعات مع تحسين الذاكرة والإنتاجية. | Software that receives, schedules, and executes inference requests on accelerators while optimizing memory and throughput. |
| كفاءة الطاقة | Energy Efficiency | نسبة العمل المفيد، مثل عدد التوكنات أو العينات المعالجة، إلى الطاقة المستهلكة أثناء التدريب أو الاستدلال. | The amount of useful work, such as processed tokens or samples, per unit of energy consumed during training or inference. |
| الجدولة الواعية بالكربون | Carbon-Aware Scheduling | تشغيل أحمال الحوسبة في أوقات أو مناطق تكون فيها كثافة الكربون في الكهرباء أقل لتقليل الأثر البيئي. | Running compute workloads at times or locations with lower electricity carbon intensity to reduce environmental impact. |
| إعادة استخدام البادئات | Prefix Reuse | إعادة استعمال نتائج حسابية لسياقات أو بادئات متكررة بدلاً من حسابها من جديد في كل طلب. | Reusing computed results for repeated contexts or prefixes instead of recomputing them for every request. |
