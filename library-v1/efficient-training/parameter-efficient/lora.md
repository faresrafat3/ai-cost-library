---
id: "entry-lora-001"
title_ar: "التكيّف منخفض الرتبة (LoRA)"
title_en: "Low-Rank Adaptation (LoRA)"
type: "Practical"
status: "Deployed"
category: "Efficient Training"
subcategory: "Parameter-Efficient Fine-Tuning"
tree_path: ["Efficient Training", "Parameter-Efficient Fine-Tuning", "LoRA"]
cost_dimensions: ["training-cost", "memory", "storage", "engineering-cost"]
proof_score: 4
sources_count: 4
---

# التكيّف منخفض الرتبة | Low-Rank Adaptation (LoRA)

![Proof Score: 4/4](https://img.shields.io/badge/Proof_Score-4%2F4-brightgreen)
![Practical](https://img.shields.io/badge/Class-Practical-blue)

## 📌 الملخص العربي | Arabic Summary

التكيّف منخفض الرتبة (LoRA) هو تقنية ضبط دقيق موفّرة للمعاملات (PEFT) تُجمّد أوزان النموذج المُدرَّب مسبقاً وتحقن مصفوفتين منخفضتي الرتبة (A و B) في طبقات الانتباه (Attention) والطبقات الخطية. أثناء التدريب، تُحدّث هاتان المصفوفتان فقط، بينما تبقى الأوزان الأساسية ثابتة. عند الاستدلال، يمكن دمج المصفوفتين مع الأوزان الأصلية دون أي كمون إضافي.

على نموذج GPT-3 بحجم 175B معامل، يقلل LoRA المعاملات القابلة للتدريب من 175 ملياراً إلى حوالي 15-20 مليوناً فقط، مع تقليل متطلبات ذاكرة GPU بمقدار 3 أضعاف وتقليل حجم نقاط التفتيش من 350GB إلى 35MB لكل مهمة.

## 📌 English Summary

Low-Rank Adaptation (LoRA) is a parameter-efficient fine-tuning (PEFT) technique that freezes pre-trained model weights and injects two trainable low-rank matrices (A and B) into attention and linear layers. During training, only these matrices are updated; during inference, they can be merged with the base weights with zero additional latency.

On GPT-3 (175B parameters), LoRA reduces trainable parameters from 175 billion to approximately 15-20 million, cuts GPU memory requirements by 3×, and reduces checkpoint size from 350GB to 35MB per task.

## ⚙️ أبعاد التكلفة | Cost Dimensions Affected

- **تكلفة التدريب (Training Cost):** تقليل المعاملات القابلة للتدريب بنسبة تصل إلى 10,000×.
- **تكلفة الذاكرة (Memory Cost):** تقليل متطلبات VRAM بمقدار 3 أضعاف (من 1.2TB إلى 350GB لنموذج GPT-3).
- **تكلفة التخزين (Storage Cost):** نقاط تفتيش بحجم 35MB بدلاً من 350GB لكل مهمة.
- **تكلفة الاستدلال (Inference Cost):** صفر كمون إضافي — يمكن دمج الأوزان في النموذج الأساسي.

## 🛡️ بوابات الأدلة | Evidence Gates

- ✅ **Gate 1 (Built):** مُدمجة في مكتبة `PEFT` من Hugging Face و `trl`، مع دعم رسمي من Microsoft.
- ✅ **Gate 2 (Tested):** أداء مكافئ أو أفضل من الضبط الدقيق الكامل على معايير RoBERTa, DeBERTa, GPT-2, GPT-3.
- ✅ **Gate 3 (Deployed):** الخيار القياسي لضبط النماذج المفتوحة المصدر (Llama, Mistral, Qwen) على منصات سحابية مثل OpenAI, Together.AI, Fireworks.
- ✅ **Gate 4 (Saved):** 10,000× تقليل في المعاملات القابلة للتدريب، 3× تقليل VRAM، 35MB مقابل 350GB نقاط تفتيش.

## ⚠️ القيود والمخاطر | Limitations & Risks

- LoRA الأصلي يتطلب تحميل النموذج الأساسي بدقة 16 بت — مما يظل كثيف الذاكرة للنماذج الكبيرة جداً (70B+).
- يُظهر LoRA overhead في التدريب (~40% أبطأ) بسبب أنماط الوصول غير الفعّالة للذاكرة.
- الأداء قد يكون أدنى من الضبط الكامل في مهام التوليد الطويلة المعقدة.
- اختيار الرتبة (rank) والطبقات المستهدفة يتطلب خبرة تجريبية.

## 📚 المصادر | Sources

- [1] Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR, 2022. DOI: [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- [2] Zhang et al., "LoRAFusion: Efficient LoRA Fine-Tuning for LLMs", arXiv, 2025. DOI: [arXiv:2510.00206](https://arxiv.org/abs/2510.00206)
- [3] IBM, "What is LoRA (Low-Rank Adaptation)?", 2026. [URL](https://www.ibm.com/think/topics/lora)
- [4] Raschka, "Practical Tips for Finetuning LLMs Using LoRA", 2025. [URL](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms)

## 🔗 إدخالات ذات صلة | Related Entries

- [QLoRA](./qlora.md)
- [SLoRA](../../../efficient-inference/serving/slora.md)
