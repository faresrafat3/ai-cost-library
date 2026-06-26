# دليل تطبيقي: الضبط الدقيق بميزانية منخفضة | Fine-tune on Low Budget

هذا الدليل مُصمّم للفرق الصغيرة والأفراد الذين يريدون ضبط نماذج لغوية كبيرة دون موارد مالية ضخمة.

## 🎯 1. استخدم QLoRA بدلاً من الضبط الكامل

QLoRA يُمكّن ضبط نماذج 70B+ على GPU واحد بدقة 4 بت.

### الإعداد الأساسي

```bash
pip install transformers peft bitsandbytes accelerate trl
```

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model

# تحميل النموذج بدقة 4 بت
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="float16",
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-8B",
    quantization_config=bnb_config,
    device_map="auto"
)

# إعداد LoRA
lora_config = LoraConfig(
    r=16,                    # الرتبة (8-64)
    lora_alpha=32,           # معامل التحجيم (2× الرتبة)
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.05,
    bias="none",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# Expected: ~0.1-0.3% of total parameters
```

### مقارنة التكلفة

| الطريقة | VRAM المطلوب | وقت التدريب | التكلفة التقريبية (ساعة GPU) |
|---|---|---|---|
| ضبط كامل (70B) | 1120GB | 5-10 أيام | $500-1000 |
| QLoRA (70B) | 48GB | 1-2 أيام | $50-100 |
| QLoRA (8B) | 10GB | 2-6 ساعات | $5-15 |

## 🎯 2. اختر حجم الرتبة (Rank) بعناية

- **r=4-8:** مناسب للمهام البسيطة (تصنيف، استخراج كيان).
- **r=16-32:** جيد للتوليد والتلخيص.
- **r=64+:** مطلوب للمهام المعقدة (البرمجة، الاستدلال المنطقي).

قاعدة عامة: ابدأ بـ r=16 و α=32، ثم زد إذا لزم الأمر.

## 🎯 3. استخدم Gradient Checkpointing

يُقلّل الذاكرة بنسبة ~50% بإعادة حساب التدرجات بدلاً من تخزينها:

```python
model.gradient_checkpointing_enable()
```

## 🎯 4. استخدم بيانات عالية الجودة بدلاً من كمية كبيرة

- 500-1000 مثال مُعد بعناية أفضل من 50,000 مثال عشوائي.
- راجع كل مثال يدوياً إن أمكن.
- استخدم نموذج أكبر لتوليد بيانات تدريب لنموذج أصغر (Distillation).

## 🎯 5. راقب Overfitting

```python
# احسب الخسارة على مجموعة التحقق
eval_loss = trainer.evaluate()["eval_loss"]
train_loss = trainer.state.log_history[-1]["loss"]

# إذا eval_loss > train_loss بشكل كبير → Overfitting
# الحل: قلل r، زد dropout، زد بيانات التحقق
```

## ⚠️ تحذيرات

- QLoRA أبطأ بنسبة ~39% من LoRA الأصلي بسبب أعباء فك التكمية.
- LoRA-FA يوفر ذاكرة إضافية (~27.8GB أقل من LoRA العادي على LLaMA-7B).
- لا تُجمّع QLoRA مع SmoothQuant — قد تتعارض تقنيات التكمية.
