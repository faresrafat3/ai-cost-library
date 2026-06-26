# استخلاص المعرفة | Knowledge Distillation

## العربية

يُقصد بـ **استخلاص المعرفة** تدريب نموذج أصغر (طالب) على تقليد سلوك نموذج أكبر (معلّم). بدلاً من تدريب الطالب من الصفر على بيانات خام، يتعلم من مخرجات المعلم (soft targets) أو تمثيلاته الداخلية، مما يُقلل بشكل كبير من تكلفة التدريب ويُحافظ على معظم الأداء.

### تقنيات فرعية

| التقنية | الوصف | الحالة |
|---------|-------|--------|
| [DistilBERT](distillation.md) | نسخة مُستخلصة من BERT (60% أسرع، 97% دقة) | 📘 تطبيقية |
| [DeepSeek-R1 Distills](distillation.md) | 6 نماذج مُستخلصة من R1-671B إلى Qwen/Llama | 📘 تطبيقية |
| [MiniLLM](distillation.md) | استخلاص عكسي KL لنماذج توليدية | 📘 تطبيقية |
| [NVIDIA Minitron](distillation.md) | قصّ + استخلاص (15B → 8B/4B) | 📘 تطبيقية |
| TinyBERT | مرحلتان: استخلاص ما قبل التدريب ثم المهمة | 📘 تطبيقية |

### تأثير التكلفة

- **التدريب**: 1/40 من الرموز مقارنة بالتدريب من الصفر (Minitron)
- **الحجم**: 40% أصغر (DistilBERT) إلى 7.5× أصغر (TinyBERT)
- **الاستدلال**: 60% أسرع (DistilBERT) إلى 9.4× أسرع (TinyBERT)
- **التكلفة**: 18× تخفيض تكلفة لكل رمز (8B vs 405B)

---

## English

**Knowledge Distillation** trains a smaller "student" model to mimic a larger "teacher" model's behavior. Instead of training from scratch on raw data, the student learns from the teacher's outputs (soft targets) or internal representations, significantly reducing training cost while preserving most performance.

### Sub-techniques

| Technique | Description | Status |
|-----------|-------------|--------|
| [DistilBERT](distillation.md) | Distilled BERT (60% faster, 97% accuracy) | 📘 Practical |
| [DeepSeek-R1 Distills](distillation.md) | 6 models distilled from R1-671B to Qwen/Llama | 📘 Practical |
| [MiniLLM](distillation.md) | Reverse KL distillation for generative models | 📘 Practical |
| [NVIDIA Minitron](distillation.md) | Pruning + distillation (15B → 8B/4B) | 📘 Practical |
| TinyBERT | Two-stage: pre-training then task-specific distillation | 📘 Practical |

### Cost Impact

- **Training**: 1/40 tokens vs. from-scratch (Minitron)
- **Size**: 40% smaller (DistilBERT) to 7.5× smaller (TinyBERT)
- **Inference**: 60% faster (DistilBERT) to 9.4× faster (TinyBERT)
- **Cost**: 18× per-token cost reduction (8B vs 405B)
