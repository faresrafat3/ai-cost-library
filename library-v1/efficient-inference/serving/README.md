# محركات تقديم النماذج | Serving Engines

## العربية

محركات التقديم هي البرامج المسؤولة عن تشغيل نماذج الذكاء الاصطناعي في بيئة الإنتاج، وإدارة الطلبات المتزامنة، وتحسين استخدام GPU. اختيار المحرك يؤثر بشكل مباشر على التكلفة والأداء.

### المحركات الرئيسية

| المحرك | الوصف | الحالة |
|--------|-------|--------|
| vLLM | محرك مفتوح المصدر مع PagedAttention | 📘 تطبيقية |
| TensorRT-LLM | محرك NVIDIA المُحسَّن | 📘 تطبيقية |
| TGI (Text Generation Inference) | محرك HuggingFace | 📘 تطبيقية |
| LMDeploy | محرك OpenMMLab | 📘 تطبيقية |
| Triton Inference Server | خادم تقديم موحّد من NVIDIA | 📘 تطبيقية |

### تأثير التكلفة

- **الإنتاجية**: TensorRT-LLM يتفوق بـ 15-30% على vLLM في الإنتاجية القصوى
- **زمن الوصول الأول للرمز**: vLLM الأفضل مع مستخدمين متزامنين كثيرين
- **تكلفة الهندسة**: vLLM يحتاج ساعات، TensorRT-LLM يحتاج أسابيع
- **استهلاك الطاقة**: TensorRT-LLM الأكثر كفاءة (طاقة أقل لكل رمز)

---

## English

Serving engines are the software responsible for running AI models in production, managing concurrent requests, and optimizing GPU utilization. Engine choice directly impacts cost and performance.

### Major Engines

| Engine | Description | Status |
|--------|-------------|--------|
| vLLM | Open-source with PagedAttention | 📘 Practical |
| TensorRT-LLM | NVIDIA's optimized engine | 📘 Practical |
| TGI (Text Generation Inference) | HuggingFace's engine | 📘 Practical |
| LMDeploy | OpenMMLab's engine | 📘 Practical |
| Triton Inference Server | NVIDIA's unified serving server | 📘 Practical |

### Cost Impact

- **Throughput**: TensorRT-LLM leads by 15-30% over vLLM in peak throughput
- **Time-to-first-token**: vLLM best with many concurrent users
- **Engineering cost**: vLLM needs hours, TensorRT-LLM needs weeks
- **Energy consumption**: TensorRT-LLM most efficient (less energy per token)
