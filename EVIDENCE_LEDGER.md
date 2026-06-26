# سجل الأدلة | Evidence Ledger

يسجل هذا الملف كافة الادعاءات الموثقة بالأرقام لخفض التكلفة/الذاكرة/الكمون مع مراجعها.
This ledger records all quantified claims for cost/memory/latency reduction with references.

---

| Claim ID | Entry (Method) | Metric | Improvement | Source | Confidence |
|---|---|---|---|---|---|
| `CLAIM-GPTQ-01` | GPTQ | Memory | x3 to x4 reduction | Frantar et al., 2023 [1] | High |
| `CLAIM-GPTQ-02` | GPTQ | Accuracy | <1% loss vs FP16 | Frantar et al., 2023 [1] | High |
| `CLAIM-QLORA-01` | QLoRA | Memory | 780GB -> 48GB (for 65B model) | Dettmers et al., 2023 [1] | High |
| `CLAIM-QLORA-02` | QLoRA | Training Speed | 39% slower than LoRA | Raschka, 2025 | Medium |
| `CLAIM-SPECDEC-01` | Speculative Decoding | Latency | 2x to 3x speedup | Leviathan et al., 2023 [1] | High |
| `CLAIM-CBATCH-01` | Continuous Batching | Throughput | Up to 23x vs Static Batching | Anyscale Benchmark, 2026 | High |
| `CLAIM-CBATCH-02` | Continuous Batching | Throughput | 36.9x vs FasterTransformer | Yu et al., 2022 (Orca OSDI) | High |
| `CLAIM-AWQ-01` | AWQ | Latency | 1.45x faster than GPTQ | Lin et al., 2023-2024 (AWQ) | High |
| `CLAIM-AWQ-02` | AWQ | Memory / Speed | Fits 13B on 8GB VRAM (33 tok/s) | Lin et al., 2023-2024 (AWQ) | High |
| `CLAIM-PCACHE-01` | Prompt Caching | API Cost | 41% to 80% reduction in agent tasks | Du et al., 2026 (arXiv:2601.06007) | High |
| `CLAIM-PCACHE-02` | Prompt Caching | Latency (TTFT) | 13% to 31% improvement | Du et al., 2026 (arXiv:2601.06007) | High |
| `CLAIM-SQ-01` | SmoothQuant | Memory | 2x reduction (INT8 vs FP16) | Xiao et al., 2023 [1] | High |
| `CLAIM-SQ-02` | SmoothQuant | Accuracy | 71.1% vs 71.6% FP16 (OPT-175B) | Xiao et al., 2023 [1] | High |
| `CLAIM-SQ-03` | SmoothQuant | Latency | 1689ms vs 1707ms (seq 1024) | Xiao et al., 2023 [1] | High |
| `CLAIM-INT8-01` | LLM.int8() | Memory | 1.96x reduction (BLOOM-176B) | Dettmers et al., 2022 | High |
| `CLAIM-INT8-02` | LLM.int8() | Accuracy | 0% loss (66.7% vs 66.9%) | Dettmers et al., 2022 | High |
| `CLAIM-LORA-01` | LoRA | Params | 10,000x reduction (GPT-3) | Hu et al., 2022 | High |
| `CLAIM-LORA-02` | LoRA | VRAM | 3x reduction (1.2TB -> 350GB) | Hu et al., 2022 | High |
| `CLAIM-LORA-03` | LoRA | Checkpoint | 350GB -> 35MB per task | Hu et al., 2022 | High |
| `CLAIM-PA-01` | PagedAttention | Mem Waste | <4% vs 60-80% (traditional) | Kwon et al., 2023 | High |
| `CLAIM-PA-02` | PagedAttention | Throughput | 2-4x vs traditional | Kwon et al., 2023 | High |
| `CLAIM-RA-01` | RadixAttention | Throughput | Up to 6.4x (structured) | Zheng et al., 2023 | High |
| `CLAIM-RA-02` | RadixAttention | Hit Rate | 70-95% (RAG/Agents) | LMSYS Blog, 2024 | High |
