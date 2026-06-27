#!/usr/bin/env python3
"""Generate RANKING.md using a calibrated fair 9-axis MCDA ranking.

Version 2 intentionally avoids over-confident / inflated global scores. It keeps
exactly the 9 requested axes, but adds calibration layers around them:

1) raw 9-axis utility,
2) confidence discount,
3) explicit risk / complexity / narrow-scope penalties,
4) maturity gates for emerging and theoretical work,
5) small niche-excellence bonuses and badges so specialised methods still get
   credit even if they are not the best global default.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WEIGHTS = {
    "E": 0.20,   # Evidence Strength
    "C": 0.25,   # Cost Reduction Magnitude
    "M": 0.15,   # Maturity & Readiness
    "I": 0.10,   # Ease of Implementation
    "R": 0.10,   # Risk & Limitations (inverse)
    "G": 0.05,   # Generalizability
    "T": 0.05,   # Community & Tooling
    "S": 0.05,   # Sustainability
    "P": 0.05,   # Production Compatibility
}

AXIS_NAMES = {
    "E": "Evidence Strength / قوة الدليل",
    "C": "Cost Reduction Magnitude / مقدار الخفض",
    "M": "Maturity & Readiness / النضج",
    "I": "Ease of Implementation / السهولة",
    "R": "Risk & Limitations, inverse / المخاطر عكسيًا",
    "G": "Generalizability / التعميم",
    "T": "Community & Tooling / الأدوات",
    "S": "Sustainability / الاستدامة",
    "P": "Production Compatibility / توافق الإنتاج",
}

NON_DIRECT_METHOD_HINTS = [
    "pricing comparison", "price of progress", "token multiplier", "cost per successful task",
]


def clamp(x: float, lo: int = 1, hi: int = 10) -> int:
    return int(max(lo, min(hi, round(x))))


def clamp_float(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def load_frontmatter_scores(path: Path) -> dict[str, float]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fm = m.group(1)
    sm = re.search(r"scoring:\n((?:  [A-C][0-9]+:\s*[-0-9.]+\n?)+)", fm)
    scores: dict[str, float] = {}
    if sm:
        for line in sm.group(1).splitlines():
            k, v = line.strip().split(":", 1)
            scores[k] = float(v.strip())
    return scores


def source_tier_bonus(text: str) -> float:
    t1 = len(re.findall(r"Tier\s*1", text, flags=re.I))
    t2 = len(re.findall(r"Tier\s*2", text, flags=re.I))
    t3 = len(re.findall(r"Tier\s*3", text, flags=re.I))
    if t1 >= 2:
        return 1.0
    if t1 == 1 and t2 >= 1:
        return 0.5
    if t2 >= 3:
        return 0.25
    if t3 and not (t1 or t2):
        return -1.0
    return 0.0


def axis_scores(entry: dict, base: dict[str, float]) -> dict[str, int]:
    path = ROOT / entry["path"]
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    typ = entry.get("type", "")
    cat = entry.get("category", "")
    sub = entry.get("subcategory", "")
    dims = set(entry.get("cost_dimensions", []))
    title = (entry.get("title_en", "") + " " + entry.get("title_ar", "")).lower()

    A1 = base.get("A1", 4 if typ == "emerging" else 5)
    A2 = base.get("A2", 5)
    A3 = base.get("A3", 5)
    B1 = base.get("B1", 0)
    B2 = base.get("B2", 0)
    B3 = base.get("B3", 0)
    B4 = base.get("B4", 0)
    C1 = base.get("C1", 4)
    C2 = base.get("C2", 5)
    C3 = base.get("C3", 5)
    C4 = base.get("C4", 4)

    # 1) Evidence: source quality + reproducibility + source count + explicit tiers.
    E = clamp(0.58 * A2 + 0.30 * A3 + 0.12 * min(10, entry.get("sources_count") or 1) + source_tier_bonus(text))

    # 2) Magnitude: dominant documented saving, evidence-discounted.
    # This protects training-only methods from API bias, but avoids calling weakly evidenced
    # claims "world-leading" just because one dimension was high.
    C_raw = max(B1, B2, B3, B4) or 1
    if E <= 5:
        C_raw -= 1.0
    if typ == "theoretical":
        C_raw -= 0.7
    if any(h in title for h in NON_DIRECT_METHOD_HINTS):
        C_raw = min(C_raw, 4)
    C = clamp(C_raw)

    # 3) Maturity/readiness.
    M = clamp(A1)

    # 4) Implementation ease.
    I = clamp(C1)

    # 5) Risk is inverse: higher score = fewer risks/limitations.
    # V2 is deliberately stricter: high impact often comes with hidden operational risk.
    R = 0.20 * A1 + 0.18 * C1 + 0.17 * C2 + 0.17 * C4 + 0.18 * A3 + 0.10 * C3
    if typ == "emerging":
        R -= 1.4
    if typ == "theoretical":
        R -= 2.0
    if any(k in title for k in ["quantization", "gptq", "awq", "int8", "fp8", "gguf", "qlora"]):
        R -= 0.7  # accuracy / kernel / hardware edge cases
    if any(k in title for k in ["moe", "custom", "decentralized", "heterogeneous", "sub-quadratic", "sparse", "cpu-gpu"]):
        R -= 1.0  # architecture or infrastructure complexity
    if any(k in title for k in ["semantic caching", "context compression", "speculative", "sleep-time", "babbling", "dvfs", "routing"]):
        R -= 0.7  # correctness, latency, TTL, or policy risks
    if cat in ["market-economics", "finops-governance"]:
        R -= 0.4  # indirect cost-control risk
    R = clamp(R)

    # 6) Generalizability.
    G = clamp(C2)

    # 7) Community/tooling.
    T = clamp(C4)

    # 8) Sustainability/energy: estimated from saving + explicit energy focus.
    S = 3 + 0.34 * C + 0.10 * B4 + 0.08 * B3
    if any(x in dims for x in ["energy", "carbon", "power"]):
        S += 1.5
    if any(k in (str(path) + " " + title) for k in ["energy", "watt", "dvfs", "babbling", "frequency"]):
        S += 1.4
    if C <= 1:
        S = 3
    S = clamp(S)

    # 9) Production compatibility.
    P = clamp(0.48 * C3 + 0.30 * A1 + 0.22 * C4)

    return {"E": E, "C": C, "M": M, "I": I, "R": R, "G": G, "T": T, "S": S, "P": P}


def raw_score(axes: dict[str, int]) -> float:
    return sum(axes[k] * WEIGHTS[k] for k in WEIGHTS) * 10


def confidence_index(axes: dict[str, int]) -> float:
    # 0-1 confidence in the ranking position, not in the method's existence.
    return round((0.40 * axes["E"] + 0.25 * axes["M"] + 0.15 * axes["T"] + 0.10 * axes["P"] + 0.10 * axes["G"]) / 10, 2)


def niche_badges(entry: dict, axes: dict[str, int], base: dict[str, float]) -> list[str]:
    title = entry.get("title_en", "").lower()
    cat = entry.get("category", "")
    badges: list[str] = []
    if base.get("B2", 0) >= 9:
        badges.append("ضبط/تدريب منخفض التكلفة")
    if base.get("B3", 0) >= 9:
        badges.append("خفض ذاكرة قوي")
    if base.get("B4", 0) >= 9:
        badges.append("إنتاجية استدلال عالية")
    if base.get("B1", 0) >= 9 and axes["I"] >= 7:
        badges.append("خفض API سريع التبني")
    if axes["S"] >= 9:
        badges.append("استدامة/طاقة")
    if entry.get("type") == "emerging" and axes["E"] >= 8 and axes["C"] >= 8:
        badges.append("بحث واعد عالي الأثر")
    if cat in ["finops-governance", "market-economics"]:
        badges.append("قياس/حوكمة قرار")
    if "moe" in title:
        badges.append("ميزة معمارية ضخمة لكن معقّدة")
    return badges[:4]


def calibrated_score(entry: dict, axes: dict[str, int], badges: list[str]) -> dict[str, float | str]:
    raw = raw_score(axes)
    conf = confidence_index(axes)

    # Global scores are intentionally conservative: no technique should look like
    # a final answer for every user. Strong methods can still win scenario sections.
    uncertainty_penalty = (1.0 - conf) * 12.0
    risk_penalty = max(0, 7 - axes["R"]) * 1.6
    complexity_penalty = max(0, 5 - axes["I"]) * 0.7
    narrow_scope_penalty = max(0, 6 - axes["G"]) * 0.7
    maturity_penalty = 0.0
    if entry.get("type") == "emerging" and axes["M"] <= 4:
        maturity_penalty += 2.0
    if entry.get("type") == "theoretical":
        maturity_penalty += 3.0

    excellence_bonus = 0.0
    excellence_bonus += 0.5 if axes["C"] >= 9 else 0.0
    excellence_bonus += 0.4 if axes["E"] >= 9 else 0.0
    excellence_bonus += 0.4 if axes["T"] >= 9 and axes["P"] >= 8 else 0.0
    excellence_bonus += 0.5 if axes["S"] >= 9 else 0.0
    excellence_bonus += 0.4 if axes["G"] >= 9 else 0.0
    excellence_bonus += min(0.3 * len(badges), 0.7)
    excellence_bonus = min(excellence_bonus, 2.5)

    adjusted = raw * 0.88 + excellence_bonus - uncertainty_penalty - risk_penalty - complexity_penalty - narrow_scope_penalty - maturity_penalty

    # Maturity gates prevent prototypes from outranking production defaults globally,
    # while scenario lists and badges still preserve their distinctive advantage.
    cap = 100.0
    typ = entry.get("type")
    if typ == "theoretical":
        cap = min(cap, 67.0)
    if typ == "emerging":
        cap = min(cap, 74.0 + (2.0 if axes["E"] >= 8 and axes["C"] >= 8 else 0.0))
    if axes["M"] <= 3:
        cap = min(cap, 62.0)
    elif axes["M"] <= 4:
        cap = min(cap, 70.0)

    title = entry.get("title_en", "").lower()
    if any(h in title for h in NON_DIRECT_METHOD_HINTS):
        cap = min(cap, 60.0)

    final = round(clamp_float(adjusted, 10.0, cap), 1)
    return {
        "raw": round(raw, 1),
        "confidence": conf,
        "bonus": round(excellence_bonus, 1),
        "penalty": round(uncertainty_penalty + risk_penalty + complexity_penalty + narrow_scope_penalty + maturity_penalty, 1),
        "cap": round(cap, 1),
        "final": final,
    }


def make_rows() -> list[dict]:
    entries_data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))["entries"]
    scoring_data = json.loads((ROOT / "data/scoring.json").read_text(encoding="utf-8"))["entries"]
    rows = []
    for entry in entries_data:
        base = dict(scoring_data.get(entry["id"], {}).get("scores", {}))
        base.update(load_frontmatter_scores(ROOT / entry["path"]))
        axes = axis_scores(entry, base)
        badges = niche_badges(entry, axes, base)
        cal = calibrated_score(entry, axes, badges)
        rows.append({"entry": entry, "base": base, "axes": axes, "badges": badges, "calibration": cal})
    rows.sort(key=lambda r: (-float(r["calibration"]["final"]), -float(r["calibration"]["raw"]), r["entry"]["id"]))
    return rows


def scenario_rank(rows: list[dict], ids: list[str]) -> list[dict]:
    by_id = {r["entry"]["id"]: r for r in rows}
    picked = [by_id[x] for x in ids if x in by_id]
    picked.sort(key=lambda r: (-float(r["calibration"]["final"]), -r["axes"]["C"]))
    return picked


def main() -> None:
    rows = make_rows()

    lines: list[str] = []
    lines.append("# التصنيف العادل متعدد المعايير | Fair Multi-Criteria Ranking\n")
    lines.append(f"> إصدار خوارزمية: **v2.0 Calibrated MCDA** | تاريخ الإصدار: 2026-06-27 | عدد المداخل: **{len(rows)}** | المصدر: `data/entries.json`.\n\n")

    lines.append("## لماذا v2؟\n\n")
    lines.append("الإصدار الأول كان مفيدًا كبداية، لكنه كان **متفائلًا أكثر من اللازم**: درجات كثيرة فوق 90 أعطت انطباعًا خاطئًا أن المكتبة وصلت إلى إجابة نهائية أو أن التقنيات العليا تصلح لكل الحالات. لذلك يستخدم هذا الإصدار خوارزمية أعمق وأكثر محافظة: يعطي التقنية حقها إذا كانت ممتازة في سيناريو محدد، لكنه لا يسمح لها بالفوز عالميًا لمجرد أنها قوية في محور واحد.\n\n")

    lines.append("## الخوارزمية\n\n")
    lines.append("نُبقي المحاور التسعة المطلوبة، لكن نحسب درجتين: **المنفعة الخام** ثم **الدرجة المعايرة**. الدرجة المعايرة هي المستخدمة في الترتيب العام.\n\n")
    lines.append("```text\n")
    lines.append("Raw Utility = 10 × Σ(axis_score × axis_weight)\n")
    lines.append("Confidence = (0.40E + 0.25M + 0.15T + 0.10P + 0.10G) / 10\n")
    lines.append("Calibrated Score = Raw×0.88 + ExcellenceBonus - UncertaintyPenalty - RiskPenalty - ComplexityPenalty - ScopePenalty - MaturityPenalty\n")
    lines.append("ثم تُطبَّق بوابات نضج: النظري والناشئ لا يتجاوزان سقفًا معينًا عالميًا، لكن يمكنهما الفوز في أقسام السيناريو.\n")
    lines.append("```\n\n")

    lines.append("### الأوزان الأساسية — لم تتغير\n\n")
    lines.append("| الرمز | المحور | الوزن |\n")
    lines.append("|---|---|---:|\n")
    for k, w in WEIGHTS.items():
        lines.append(f"| {k} | {AXIS_NAMES[k]} | {int(w*100)}% |\n")

    lines.append("\n### طبقات المعايرة الجديدة\n\n")
    lines.append("| الطبقة | الهدف | لماذا تمنع المبالغة؟ |\n")
    lines.append("|---|---|---|\n")
    lines.append("| خصم الثقة | يقلل الدرجة إذا كان الدليل/النضج/الأدوات أضعف | لا نساوي بين ورقة واعدة وتقنية في vLLM/PyTorch. |\n")
    lines.append("| عقوبة المخاطر | تفصل الأثر عن قابلية الاعتماد | التكميم، MoE، التخزين الدلالي، والتوجيه لها مخاطر جودة/تعقيد. |\n")
    lines.append("| عقوبة التعقيد | تعاقب التقنيات التي تحتاج إعادة هندسة أو عتادًا خاصًا | حتى لو وفرت كثيرًا، قد لا تكون اختيارًا عامًا. |\n")
    lines.append("| عقوبة ضيق النطاق | تخفض التقنيات الخاصة بمهمة/نموذج/عتاد | تحفظ فرص التقنيات العامة في الترتيب العام. |\n")
    lines.append("| بوابات النضج | سقف أعلى للنظري والناشئ في الترتيب العام | يمنع \"بحث واعد\" من تجاوز ممارسة إنتاجية مثبتة. |\n")
    lines.append("| مكافأة تميز صغيرة | تعطي نقاطًا محدودة لميزة قوية جدًا | لا تغيّر العالم وحدها، لكنها تمنع دفن التقنيات المتخصصة. |\n\n")

    lines.append("## جدول التصنيف العام المعاير\n\n")
    lines.append("| الرتبة | ID | العنوان | الدرجة المعايرة | الخام | الثقة | شارات التميز | E | C | M | I | R | G | T | S | P |\n")
    lines.append("|---:|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for i, r in enumerate(rows, 1):
        e = r["entry"]
        axes = r["axes"]
        cal = r["calibration"]
        title = f"{e['title_en']}<br><span dir=\"rtl\">{e['title_ar']}</span>"
        badges = "، ".join(r["badges"]) if r["badges"] else "—"
        lines.append(
            f"| {i} | `{e['id']}` | {title} | **{cal['final']:.1f}** | {cal['raw']:.1f} | {cal['confidence']:.2f} | {badges} | "
            + " | ".join(str(axes[k]) for k in WEIGHTS)
            + " |\n"
        )

    lines.append("\n## أفضل الطرق عمومًا — لكن ليست إجابة نهائية\n\n")
    for i, r in enumerate(rows[:10], 1):
        e = r["entry"]
        cal = r["calibration"]
        badges = "؛ ".join(r["badges"]) if r["badges"] else "توازن عام"
        lines.append(f"{i}. **{e['title_en']}** — **{cal['final']:.1f}/100**، الخام {cal['raw']:.1f}، الثقة {cal['confidence']:.2f}. سبب التقدم: {badges}.\n")

    lines.append("\n## الأفضل حسب السيناريو\n\n")
    scenarios = [
        ("تقليل ذاكرة GPU وتشغيل نماذج أكبر", ["entry-qlora-001", "entry-awq-001", "entry-gptq-001", "entry-pagedattention-001", "entry-gguf-001", "entry-llmint8-001"]),
        ("خدمة استدلال عالية التزامن", ["entry-contbatching-001", "entry-pagedattention-001", "entry-flashattn-001", "entry-radixattention-001", "entry-specdec-001", "entry-eagle3-001"]),
        ("تقليل فاتورة API بسرعة بدون امتلاك بنية تحتية", ["entry-promptcache-001", "entry-batchapi-001", "entry-routing-001", "entry-semcache-001", "entry-ragcost-001", "entry-budgetlimits-001"]),
        ("ضبط دقيق منخفض التكلفة", ["entry-lora-001", "entry-qlora-001", "entry-mixedprec-001", "entry-synthdata-001", "entry-deepspeed-001", "entry-merging-001"]),
        ("توفير الطاقة والاستدامة", ["entry-dvfs-001", "entry-babbling-001", "entry-pagedattention-001", "entry-flashattn-001", "entry-ipw-001", "entry-gguf-001"]),
        ("وكلاء LLM وتقليل تضخم التوكنات", ["entry-budgetlimits-001", "entry-ctxcompress-001", "entry-agentdiet-001", "entry-ragcost-001", "entry-agentmultiplier-001", "entry-bagen-001"]),
        ("ميزة معمارية كبيرة مع استعداد لتحمل التعقيد", ["entry-moe-001", "entry-llama4-001", "entry-dsv4-001", "entry-subquad-001", "entry-mod-001", "entry-moequant-001"]),
        ("تخطيط استراتيجي وشراء عتاد أو اختيار مزود", ["entry-gpuecon-001", "entry-breakeven-001", "entry-customchips-001", "entry-apipricing-001", "entry-ipw-001", "entry-finops-001"]),
    ]
    for scenario, ids in scenarios:
        lines.append(f"### {scenario}\n\n")
        for r in scenario_rank(rows, ids):
            e = r["entry"]
            cal = r["calibration"]
            badges = "، ".join(r["badges"]) if r["badges"] else "—"
            lines.append(f"- **{e['title_en']}** (`{e['id']}`) — {cal['final']:.1f}/100؛ {badges}\n")
        lines.append("\n")

    lines.append("## كيف تقرأ النتائج؟\n\n")
    lines.append("- **الدرجة المعايرة**: أفضل مؤشر للترتيب العام المحافظ.\n")
    lines.append("- **الخام**: ماذا كانت ستسجل التقنية لو تجاهلنا عدم اليقين والسقوف.\n")
    lines.append("- **الثقة**: قوة الثقة في موضع التقنية داخل الترتيب، لا ضمان نجاحها عندك.\n")
    lines.append("- **الشارات**: المكان الذي قد تكون فيه التقنية ممتازة حتى لو لم تتصدر عالميًا.\n")
    lines.append("- `R` عكسي: 10 يعني مخاطر قليلة، 1 يعني مخاطر عالية.\n\n")

    lines.append("## حدود النسخة الحالية وما يجب تحسينه لاحقًا\n\n")
    lines.append("1. إضافة قياسات موحدة من نفس العتاد والنماذج ستقوي محور الأثر.\n")
    lines.append("2. فصل تكلفة التدريب عن الاستدلال في ترتيبين مستقلين قد يعطي عدالة أكبر لبعض المستخدمين.\n")
    lines.append("3. يمكن إضافة تحليل حساسية للأوزان: ماذا يحدث لو زاد وزن المخاطر أو نقص وزن الأدلة؟\n")
    lines.append("4. التقنيات المركبة مثل `PagedAttention + Continuous Batching + Quantization` تحتاج ترتيبًا خاصًا للحزم، لا للطرق الفردية فقط.\n")
    lines.append("5. بعض الإدخالات هي مقاييس أو تحليلات سوق وليست طرق خفض مباشرة؛ أُبقيت في الجدول لأنها جزء من المكتبة، لكن وُضعت عليها سقوف محافظة.\n")

    (ROOT / "RANKING.md").write_text("".join(lines), encoding="utf-8")

    audit = [
        {
            "rank": i,
            "id": r["entry"]["id"],
            "title_en": r["entry"]["title_en"],
            "title_ar": r["entry"]["title_ar"],
            "type": r["entry"].get("type"),
            "category": r["entry"].get("category"),
            "score_calibrated_100": r["calibration"]["final"],
            "score_raw_100": r["calibration"]["raw"],
            "confidence": r["calibration"]["confidence"],
            "bonus": r["calibration"]["bonus"],
            "penalty": r["calibration"]["penalty"],
            "cap": r["calibration"]["cap"],
            "badges": r["badges"],
            "axes": r["axes"],
        }
        for i, r in enumerate(rows, 1)
    ]
    (ROOT / "data/fair_ranking.json").write_text(
        json.dumps({"date": "2026-06-27", "algorithm": "v2.0-calibrated-mcda", "weights": WEIGHTS, "ranking": audit}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
