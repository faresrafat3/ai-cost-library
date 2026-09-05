---
id: entry-model-router-cascade
title_ar: توجيه النماذج المتدرج (Model Router Cascade)
title_en: Model Router Cascade (Tiered Inference)
type: pending
status: emerging
category: agentic-economics
subcategory: ""
tree_path: "AI Cost Library → Agentic Economics → Model Router Cascade"
cost_dimensions:
  - inference-cost
  - token-cost
proof_score: "⭐ قيد التقييم | Under Review"
sources_count: 1
created: 2026-06-26
updated: 2026-06-26
research_review:
  paper_read: true
  abstract_read: true
---

# Technique: Model Router Cascade (Tiered Inference)

**Category:** 05-agentic-economics
**Evidence strength:** Strong (multiple vendor benchmarks, 2024-2025)
**Cost lever:** Inference routing

## Claim
Routing each request to the cheapest model that can satisfy it — via a small "router" or a cascade (cheap first, escalate on low confidence) — cuts inference spend 40-70% versus using a single frontier model for everything, with negligible quality loss on most tasks.

## How it works
1. Classify the task (trivial / medium / hard) with a router model or heuristics.
2. Send easy tasks to a small/cheap model (e.g. Haiku, Mini, 8B-class).
3. Escalate to a frontier model only when the cheap model scores low confidence or fails a guardrail.
4. Cache + reuse routed decisions where inputs are repeated.

## Evidence
- Provider routing/cascade docs (Anthropic, OpenAI, Google) report 50-70% token savings on mixed workloads.
- Independent "router" papers (e.g. RouteLLM, 2024) show ~2x cost reduction at parity quality.
- Caveat: savings depend on task mix; homogeneous hard workloads see less benefit.

## Risks / no-hype notes
- Router itself adds latency + a small model call cost.
- Misrouting hard tasks to a weak model can hurt user-visible quality — keep a confidence floor + human-in-loop for critical paths.
- Measure with your own traffic, not vendor marketing.

## Related
- See my [Semitic Router](https://github.com/faresrafat3/semitic-router) for a neural/symbolic routing pattern.
- `token-multiplier`, `chain-optimization` in this library.
