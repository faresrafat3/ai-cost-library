# سجل المطالبات | Claims Ledger

يسجل هذا الملف جميع الادعاءات الموثقة بالأرقام لخفض التكلفة/الذاكرة/الكمون.

This ledger records all quantified claims for cost/memory/latency reduction.

---

| Claim ID | Entry (Method) | Metric | Improvement | Source | Confidence |
|---|---|---|---|---|---|
| `CLAIM-GPTQ-01` | GPTQ | Memory | 3-4× reduction | Frantar et al., 2023 | High |
| `CLAIM-GPTQ-02` | GPTQ | Accuracy | <1% loss vs FP16 | Frantar et al., 2023 | High |
| `CLAIM-AWQ-01` | AWQ | Latency | 1.45× faster than GPTQ | Lin et al., 2023-2024 | High |
| `CLAIM-AWQ-02` | AWQ | Memory / Speed | 13B on 8GB VRAM (33 tok/s) | Lin et al., 2023-2024 | High |
| `CLAIM-SQ-01` | SmoothQuant | Memory | 2× reduction (INT8 vs FP16) | Xiao et al., 2023 | High |
| `CLAIM-SQ-02` | SmoothQuant | Accuracy | 71.1% vs 71.6% FP16 (OPT-175B) | Xiao et al., 2023 | High |
| `CLAIM-SQ-03` | SmoothQuant | Latency | 1689ms vs 1707ms (seq 1024) | Xiao et al., 2023 | High |
| `CLAIM-SQ-04` | SmoothQuant+ | Throughput | 1.9-4.0× vs FP16 | Pan et al., 2023 | High |
| `CLAIM-INT8-01` | LLM.int8() | Memory | 1.96× reduction (BLOOM-176B) | Dettmers et al., 2022 | High |
| `CLAIM-INT8-02` | LLM.int8() | Accuracy | 0% loss (66.7% vs 66.9%) | Dettmers et al., 2022 | High |
| `CLAIM-SPECDEC-01` | Speculative Decoding | Latency | 2-3× speedup | Leviathan et al., 2023 | High |
| `CLAIM-SPECDEC-02` | Speculative Decoding | Cost | Up to 60% reduction in processing time | Leviathan et al., 2023 | Medium |
| `CLAIM-CBATCH-01` | Continuous Batching | Throughput | Up to 23× vs Static Batching | Anyscale Benchmark, 2026 | High |
| `CLAIM-CBATCH-02` | Continuous Batching | Throughput | 36.9× vs FasterTransformer | Yu et al., 2022 (Orca OSDI) | High |
| `CLAIM-PA-01` | PagedAttention | Memory Waste | <4% vs 60-80% (traditional) | Kwon et al., 2023 | High |
| `CLAIM-PA-02` | PagedAttention | Throughput | 2-4× vs traditional systems | Kwon et al., 2023 | High |
| `CLAIM-RA-01` | RadixAttention | Throughput | Up to 6.4× (structured workloads) | Zheng et al., 2023 | High |
| `CLAIM-RA-02` | RadixAttention | Cache Hit Rate | 70-95% (RAG/Agent workloads) | LMSYS Blog, 2024 | High |
| `CLAIM-RA-03` | RadixAttention | TTFT | 3-4× reduction (cached vs cold) | Spheron, 2026 | High |
| `CLAIM-PCACHE-01` | Prompt Caching | API Cost | 41-80% reduction in agent tasks | Du et al., 2026 | High |
| `CLAIM-PCACHE-02` | Prompt Caching | Latency (TTFT) | 13-31% improvement | Du et al., 2026 | High |
| `CLAIM-LORA-01` | LoRA | Trainable Params | 10,000× reduction (GPT-3) | Hu et al., 2022 | High |
| `CLAIM-LORA-02` | LoRA | VRAM | 3× reduction (1.2TB → 350GB for GPT-3) | Hu et al., 2022 | High |
| `CLAIM-LORA-03` | LoRA | Checkpoint Size | 350GB → 35MB per task (GPT-3) | Hu et al., 2022 | High |
| `CLAIM-QLORA-01` | QLoRA | Memory | 780GB → 48GB (for 65B model) | Dettmers et al., 2023 | High |
| `CLAIM-QLORA-02` | QLoRA | Training Speed | 39% slower than LoRA | Raschka, 2025 | Medium |
| `CLAIM-LOFA-01` | LoRA-FA | Memory | 27.8GB less than LoRA (LLaMA-7B) | Zhang et al., 2023 | High |
