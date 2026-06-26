---
id: entry-ctxcompress-001
title_ar: ضغط السياق وتقليل التوكنات
title_en: "Context Compression & Token Reduction for Agents"
type: emerging
status: active-research
category: agentic-economics
subcategory: chain-optimization
cost_dimensions: [token-cost, inference-cost, api-cost, latency]
proof_score: "⭐⭐ نموذج أولي | Prototype"
sources_count: 5
created: 2026-06-26
scoring:
  A1: 4
  A2: 7
  A3: 6
  A4: 10
  B1: 7
  B2: 0
  B3: 0
  B4: 2
  C1: 5
  C2: 6
  C3: 6
  C4: 5
research_review:
  papers_scanned: 5
  papers_read: 3
  decision: "يُضاف — مجال نشط جداً في 2026 مع 5+ أساليب مختلفة"
---

# 🧪 ضغط السياق وتقليل التوكنات | Context Compression

> **التصنيف:** 🧪 ناشئة — مجال بحثي نشط | **الإثبات:** ⭐⭐

---

## المحتوى العربي

### المشكلة

في الوكلاء والمحادثات الطويلة، السياق ينمو بلا حدود:
- كل دور يُضيف 500-5,000 توكن
- بعد 20 دوراً: 10,000-100,000 توكن في السياق
- **معظمها غير مفيد** — أخطاء قديمة، محاولات فاشلة، بيانات منتهية الصلاحية

### 5 أساليب ضغط مُراجعة (2025-2026)

#### 1. Focus — ضغط ذاتي مستوحى من البيولوجيا (يناير 2026)
**arXiv:2601.07190 — قُرئ:**
- الوكيل يقرر بنفسه متى يضغط سياقه (مستوحى من العفن الغروي!)
- **22.7% تقليل** (14.9M → 11.5M tokens) مع نفس الدقة
- وفر يصل **57%** على مهام فردية

#### 2. ACON — تحسين الضغط بتحليل الفشل (أكتوبر 2025)
- يحلل: أين فشل الضغط؟ ما المعلومات المفقودة؟
- يُحدّث قواعد الضغط بناءً على الفشل
- **26-54% تقليل** في ذروة استهلاك التوكنات
- بدون تدريب — يعمل مع أي نموذج API

#### 3. Anthropic Compaction API (يناير 2026)
- خدمة إنتاجية من Anthropic: `compact-2026-01-12`
- ضغط تلقائي عند تجاوز عتبة التوكنات
- يعمل على Claude API + AWS Bedrock + Google Vertex
- **جاهز للإنتاج — لا يحتاج تطوير**

#### 4. Cross-Lingual Token Arbitrage (يونيو 2026)
**arXiv:2606.03618 — قُرئ:**
- يستغل أن tokenizers غير فعّالة للغات غير الإنجليزية (3× توكنات أكثر!)
- يُعيد كتابة الموجّهات لتكون أكفأ في التوكن
- **12-34% تقليل** في توكنات الإدخال

#### 5. LLM-DCP — ضغط ديناميكي بالتعلم المعزز (أبريل 2025)
**arXiv:2504.11004:**
- يُدرّب وكيلاً لحذف التوكنات الزائدة عبر MDP
- تدريب بدون الحاجة لنموذج المستهدف (black-box compatible)

### مقارنة الأساليب

| الأسلوب | التقليل | يحتاج تدريب؟ | جاهز للإنتاج؟ |
|---------|---------|------------|-------------|
| Focus | 22-57% | لا | لا |
| ACON | 26-54% | لا | لا |
| Anthropic Compaction | تلقائي | لا | **نعم** ✅ |
| Token Arbitrage | 12-34% | لا | مبدئياً |
| LLM-DCP | متغير | نعم | لا |
| AgentDiet (مذكور سابقاً) | 40-60% | لا | لا |

### العلاقة بإدخالات أخرى

- **AgentDiet:** يضغط المسار المتراكم (تكميلي)
- **SkillReducer:** يضغط المهارات/system prompts (تكميلي)
- **Semantic Caching:** يتجنب الاستدعاء أصلاً (بديل جزئي)

---

## المصادر

1. **[Tier 2]** Verma, N., "Focus: Active Context Compression", arXiv:2601.07190, January 2026. 22.7% reduction.
2. **[Tier 2]** "ACON: Agent Context Optimization", arXiv (October 2025). 26-54% peak reduction.
3. **[Tier 2]** Anthropic, "Compact API beta (compact-2026-01-12)", January 2026. Production-ready.
4. **[Tier 2]** "Cross-Lingual Token Arbitrage", arXiv:2606.03618, June 2026. 12-34% reduction.
5. **[Tier 2]** "LLM-DCP: Dynamic Compressing Prompts", arXiv:2504.11004, April 2025. MDP-based compression.
