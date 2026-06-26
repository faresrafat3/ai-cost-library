# دليل تطبيقي: تقليل ذاكرة GPU | Reduce GPU Memory

هذا الدليل مخصص للمهندسين الذين يحتاجون تشغيل نماذج كبيرة على موارد GPU محدودة.

## 🎯 1. تكمية الأوزان (Weight Quantization)

أبسط طريقة لتقليل الذاكرة هي تقليل دقة الأوزان:

| الدقة | الحجم (7B) | الحجم (70B) | الفقد في الدقة |
|---|---|---|---|
| FP16 | 14 GB | 140 GB | صفر |
| INT8 (LLM.int8) | 7 GB | 70 GB | <0.5% |
| INT4 (GPTQ/AWQ) | 3.5 GB | 35 GB | 1-3% |

```python
# GPTQ باستخدام AutoGPTQ
from auto_gptq import AutoGPTQForCausalLM

model = AutoGPTQForCausalLM.from_quantized(
    "TheBloke/Llama-2-7B-GPTQ",
    device="cuda:0",
    use_triton=True
)

# AWQ
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "casperhansen/llama-3-8b-instruct-awq",
    device_map="auto"
)
```

## 🎯 2. تحسين KV Cache

الذاكرة المؤقتة للمفاتيح والقيم تستهلك ~30% من VRAM أثناء الاستدلال:

```bash
# vLLM مع PagedAttention (تقليل الهدر من 60-80% إلى <4%)
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Llama-3.1-8B-Instruct \
    --gpu-memory-utilization 0.90 \
    --max-model-len 8192
```

```bash
# SGLang مع RadixAttention (إعادة استخدام السوابق)
python -m sglang.launch_server \
    --model-path meta-llama/Llama-3.1-8B-Instruct \
    --mem-fraction-static 0.92
```

## 🎯 3. تقنية Offloading إلى CPU/NVMe

عندما لا تكفي ذاكرة GPU:

```python
# DeepSpeed ZeRO-Infinity
import deepspeed

model_engine = deepspeed.init_inference(
    model,
    config={
        "replace_with_kernel_inject": True,
        "dtype": torch.float16,
        "max_out_tokens": 512,
        "injection_policy": {
            "offload": True,
            "offload_device": "nvme",
            "nvme_path": "/local/nvme"
        }
    }
)
```

**العائد:** تمكين نماذج 70B+ على GPU واحد (24GB) باستخدام NVMe.

## 🎯 4. التجميع (Batching) الذكي

```python
# التحكم في حجم الدفعة لتجنب OOM
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=256
)

# vLLM يضبط حجم الدفعة تلقائياً بناءً على الذاكرة المتاحة
outputs = llm.generate(prompts, sampling_params)
```

## ⚠️ تحذيرات

- التكمية إلى INT4 تفقد 1-3% من الدقة.
- Offloading إلى NVMe يزيد الكمون بشكل كبير.
- لا تستخدم أكثر من طريقة تكمية في نفس الوقت.
