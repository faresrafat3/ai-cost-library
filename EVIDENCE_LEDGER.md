# سجل الأدلة | Evidence Ledger

يسجل هذا الملف كافة الادعاءات الموثقة بالأرقام لخفض التكلفة/الذاكرة/الكمون.
This ledger records all quantified claims for cost/memory/latency reduction.

| Claim ID | Entry (Method) | Metric | Improvement | Source |
|---|---|---|---|---|
| `CLAIM-GPTQ-01` | GPTQ | Memory | x3 to x4 reduction | Frantar et al., 2023 [1] |
| `CLAIM-QLORA-01` | QLoRA | Memory | 780GB -> 48GB (for 65B model) | Dettmers et al., 2023 [1] |
| `CLAIM-SPECDEC-01` | Speculative Decoding | Latency | 2x to 3x speedup | Leviathan et al., 2023 [1] |
| `CLAIM-PCACHE-01` | Prompt Caching | API Cost | 41% to 80% reduction in agent tasks | Du et al., 2026 (arXiv:2601.06007) |
| `CLAIM-PCACHE-02` | Prompt Caching | Latency (TTFT) | 13% to 31% improvement | Du et al., 2026 (arXiv:2601.06007) |
| `CLAIM-CBATCH-01` | Continuous Batching | Throughput | Up to 23x vs Static Batching | Anyscale Benchmark, 2026 |
| `CLAIM-CBATCH-02` | Continuous Batching | Throughput | 36.9x vs FasterTransformer | Yu et al., 2022 (Orca OSDI) |
| `CLAIM-AWQ-01` | AWQ | Latency | 1.45x faster than GPTQ | Lin et al., 2023-2024 (AWQ) |
| `CLAIM-AWQ-02` | AWQ | Memory / Speed | Fits 13B on 8GB VRAM (33 tok/s) | Lin et al., 2023-2024 (AWQ) |
