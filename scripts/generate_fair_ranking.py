#!/usr/bin/env python3
"""Generate RANKING.md using a fair 9-axis weighted ranking.

This script maps the repository's existing 12-dimensional scoring system to the
9 criteria requested for the global ranking. It does not mutate data files.
"""
from __future__ import annotations

import json
import re
from datetime import date
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

LABELS_AR = {
    "E": "الدليل",
    "C": "الأثر",
    "M": "النضج",
    "I": "السهولة",
    "R": "المخاطر⁻",
    "G": "التعميم",
    "T": "الأدوات",
    "S": "الاستدامة",
    "P": "الإنتاج",
}


def clamp(x: float, lo: int = 1, hi: int = 10) -> int:
    return int(max(lo, min(hi, round(x))))


def load_frontmatter_scores(path: Path) -> dict[str, float]:
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
    title = entry.get("title_en", "") + " " + entry.get("title_ar", "")

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

    # 1) Evidence: source quality + reproducibility, adjusted by explicit tier signals.
    E = clamp(0.60 * A2 + 0.30 * A3 + 0.10 * min(10, entry.get("sources_count") or 1) + source_tier_bonus(text))

    # 2) Magnitude: best demonstrated economic lever (inference/training/memory/throughput).
    # A technique usually targets one dominant cost dimension; using max avoids penalising LoRA
    # for not reducing inference, or Prompt Caching for not reducing training.
    C = clamp(max(B1, B2, B3, B4) or 1)

    # 3) Maturity/readiness.
    M = clamp(A1)

    # 4) Implementation ease.
    I = clamp(C1)

    # 5) Risk is inverse: higher score = fewer risks/limitations.
    R = 0.30 * A1 + 0.25 * C1 + 0.20 * C2 + 0.15 * C4 + 0.10 * A3
    if typ == "emerging":
        R -= 1.0
    if typ == "theoretical":
        R -= 1.5
    if any(k in (cat + " " + sub + " " + title).lower() for k in ["moe", "custom", "decentral", "heterogeneous", "sub-quadratic", "sparse", "cpu-gpu"]):
        R -= 0.8
    if any(k in title.lower() for k in ["semantic caching", "context compression", "speculative", "sleep-time", "babbling", "dvfs"]):
        R -= 0.5
    if any(k in title.lower() for k in ["full", "scaling laws", "price of progress"]):
        R -= 0.3
    R = clamp(R)

    # 6) Generalizability.
    G = clamp(C2)

    # 7) Community/tooling.
    T = clamp(C4)

    # 8) Sustainability/energy: proportional to measured savings, with bonus for explicit energy work.
    S = 3 + 0.42 * max(B1, B2, B3, B4) + 0.12 * B4 + 0.08 * B3
    if any(x in dims for x in ["energy", "carbon", "power"]):
        S += 1.5
    if any(k in (str(path) + " " + title).lower() for k in ["energy", "watt", "dvfs", "babbling", "frequency"]):
        S += 1.3
    if max(B1, B2, B3, B4) == 0:
        S = 3
    S = clamp(S)

    # 9) Production compatibility.
    P = clamp(0.50 * C3 + 0.30 * A1 + 0.20 * C4)

    return {"E": E, "C": C, "M": M, "I": I, "R": R, "G": G, "T": T, "S": S, "P": P}


def weighted_score(axes: dict[str, int]) -> float:
    # Return 0-100 for readability. Raw weighted 1-10 score is this / 10.
    return round(sum(axes[k] * WEIGHTS[k] for k in WEIGHTS) * 10, 1)


def main() -> None:
    entries_data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))["entries"]
    scoring_data = json.loads((ROOT / "data/scoring.json").read_text(encoding="utf-8"))["entries"]

    rows = []
    for entry in entries_data:
        base = dict(scoring_data.get(entry["id"], {}).get("scores", {}))
        base.update(load_frontmatter_scores(ROOT / entry["path"]))
        axes = axis_scores(entry, base)
        rows.append({"entry": entry, "axes": axes, "score": weighted_score(axes)})

    rows.sort(key=lambda r: (-r["score"], r["entry"]["id"]))

    lines: list[str] = []
    lines.append("# التصنيف العادل متعدد المعايير | Fair Multi-Criteria Ranking\n")
    lines.append(f"> تاريخ الإصدار: 2026-06-27 | عدد المداخل المصنّفة: **{len(rows)}** | النطاق: كل ما في `data/entries.json`.\n")
    lines.append("\n")
    lines.append("## الخلاصة التنفيذية\n\n")
    lines.append("هذا الملف يرتّب طرق خفض تكلفة الذكاء الاصطناعي في المكتبة ترتيبًا عامًا من 1 إلى N باستخدام 9 محاور كمية. الهدف ليس اختيار التقنية \"الأكثر لمعانًا\"، بل الأكثر نفعًا عمليًا عند الموازنة بين قوة الدليل، مقدار التوفير، النضج، سهولة التطبيق، المخاطر، قابلية التعميم، الأدوات، الاستدامة، والتوافق الإنتاجي.\n\n")
    lines.append("## الخوارزمية والأوزان\n\n")
    lines.append("لم أغيّر الأوزان الافتراضية المطلوبة؛ استخدمت الأوزان كما هي لأن المكتبة تحتوي مزيجًا واسعًا من تقنيات تدريب/استدلال/حوكمة، وتغيير الأوزان كان سيجعل التصنيف العام منحازًا لسيناريو واحد. الدرجة النهائية معروضة من **100**، وهي تساوي: `10 × Σ(درجة المحور من 1 إلى 10 × الوزن)`.\n\n")
    lines.append("| الرمز | المحور | الوزن | كيف حُسب عمليًا |\n")
    lines.append("|---|---|---:|---|\n")
    lines.append("| E | قوة الأدلة والتوثيق | 20% | جودة المصدر وقابلية التكرار وعدد المصادر وإشارات Tier 1/2/3. |\n")
    lines.append("| C | مقدار خفض التكلفة الفعلي | 25% | أعلى أثر موثق بين خفض تكلفة الاستدلال/التدريب/الذاكرة/تحسين الإنتاجية. |\n")
    lines.append("| M | النضج والجاهزية | 15% | نضج الإنتاج من بيانات المكتبة وحالة الإدخال. |\n")
    lines.append("| I | سهولة التطبيق | 10% | مدى بساطة التبني: إعدادات/مكتبة جاهزة مقابل تعديل معماري أو عتاد خاص. |\n")
    lines.append("| R | المخاطر والقيود، عكسي | 10% | درجة أعلى تعني مخاطر أقل؛ خُفّضت للنماذج الأولية، التقنيات النظرية، أو المخاطر المعروفة كفقد الدقة/التعقيد/الاعتماد على عتاد. |\n")
    lines.append("| G | قابلية التعميم | 5% | قابلية العمل عبر نماذج ومهام وبيئات مختلفة. |\n")
    lines.append("| T | الدعم المجتمعي والأدوات | 5% | وجود مكتبات ومحركات وخيارات مفتوحة المصدر وتوثيق. |\n")
    lines.append("| S | الاستدامة والأثر البيئي | 5% | مشتقة من أثر التوفير والإنتاجية والذاكرة، مع مكافأة للعمل الصريح على الطاقة/الواط. |\n")
    lines.append("| P | التوافق مع الإنتاج | 5% | قابلية النشر السحابي/API/محركات الاستدلال والتوسع. |\n\n")
    lines.append("### ملاحظات العدالة\n\n")
    lines.append("- التقنيات التدريبية مثل LoRA/QLoRA لا تُعاقَب لأنها لا تخفض تكلفة API مباشرة؛ محور الأثر يأخذ أقوى بُعد موثق لها.\n")
    lines.append("- التقنيات النظرية/الناشئة يمكن أن تحصل على أثر مرتفع، لكنها تخسر نقاطًا في النضج والمخاطر والتوافق الإنتاجي.\n")
    lines.append("- عند نقص المعلومات التفصيلية في ملف إدخال، استُخدمت درجات `data/scoring.json` والـ frontmatter ثم حُكم علمي محافظ، لذلك هذه قائمة قابلة للمراجعة وليست حكمًا نهائيًا.\n\n")

    lines.append("## جدول التصنيف العام\n\n")
    lines.append("| الرتبة | ID | العنوان | الدرجة | E | C | M | I | R | G | T | S | P |\n")
    lines.append("|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for i, r in enumerate(rows, 1):
        e = r["entry"]
        axes = r["axes"]
        title = f"{e['title_en']}<br><span dir=\"rtl\">{e['title_ar']}</span>"
        lines.append(f"| {i} | `{e['id']}` | {title} | **{r['score']:.1f}** | " + " | ".join(str(axes[k]) for k in WEIGHTS) + " |\n")

    top = rows[:10]
    lines.append("\n## الطرق الأفضل عمومًا\n\n")
    for i, r in enumerate(top, 1):
        e = r["entry"]
        axes = r["axes"]
        lines.append(f"{i}. **{e['title_en']}** — **{r['score']:.1f}/100**: توازن قوي بين الدليل ({axes['E']}/10)، الأثر ({axes['C']}/10)، النضج ({axes['M']}/10)، والأدوات ({axes['T']}/10).\n")

    lines.append("\n## الأفضل حسب السيناريو\n\n")
    scenarios = [
        ("إذا كنت تريد تقليل ذاكرة GPU وتشغيل نماذج أكبر", ["entry-qlora-001", "entry-awq-001", "entry-gptq-001", "entry-pagedattention-001", "entry-gguf-001"]),
        ("إذا كنت تشغّل خدمة استدلال عالية التزامن", ["entry-pagedattention-001", "entry-contbatching-001", "entry-flashattn-001", "entry-radixattention-001", "entry-specdec-001"]),
        ("إذا كنت تريد تقليل فاتورة API بسرعة دون امتلاك بنية تحتية", ["entry-promptcache-001", "entry-batchapi-001", "entry-routing-001", "entry-semcache-001", "entry-ragcost-001"]),
        ("إذا كان هدفك الضبط الدقيق منخفض التكلفة", ["entry-qlora-001", "entry-lora-001", "entry-mixedprec-001", "entry-synthdata-001", "entry-deepspeed-001"]),
        ("إذا كان هدفك الاستدامة والطاقة", ["entry-dvfs-001", "entry-babbling-001", "entry-pagedattention-001", "entry-flashattn-001", "entry-ipw-001"]),
        ("إذا كنت تبني وكلاء LLM وتخشى تضخم التوكنات", ["entry-budgetlimits-001", "entry-ctxcompress-001", "entry-agentdiet-001", "entry-ragcost-001", "entry-agentmultiplier-001"]),
        ("إذا كنت في مرحلة تخطيط استراتيجي أو شراء عتاد", ["entry-gpuecon-001", "entry-breakeven-001", "entry-customchips-001", "entry-apipricing-001", "entry-ipw-001"]),
    ]
    by_id = {r["entry"]["id"]: r for r in rows}
    for scenario, ids in scenarios:
        available = [by_id[x] for x in ids if x in by_id]
        available.sort(key=lambda r: -r["score"])
        lines.append(f"### {scenario}\n\n")
        for r in available:
            e = r["entry"]
            lines.append(f"- **{e['title_en']}** (`{e['id']}`) — {r['score']:.1f}/100\n")
        lines.append("\n")

    lines.append("## قراءة سريعة للمحاور\n\n")
    lines.append("`E` الدليل، `C` الأثر، `M` النضج، `I` سهولة التطبيق، `R` المخاطر عكسيًا، `G` التعميم، `T` الأدوات، `S` الاستدامة، `P` توافق الإنتاج. كل محور من 1 إلى 10.\n\n")
    lines.append("## حدود التقييم\n\n")
    lines.append("هذا التصنيف عام. في قرار شراء أو هندسة فعلي يجب إعادة وزن المحاور حسب السياق: شركة API، فريق تدريب، باحث، أو مطور فردي. كما أن أرقام 2026 الخاصة بالأسعار والعتاد تتغير بسرعة، لذلك يفضّل تحديث التصنيف عند إضافة مصادر Tier 1 أو قياسات إنتاجية جديدة.\n")

    (ROOT / "RANKING.md").write_text("".join(lines), encoding="utf-8")

    # Also write machine-readable sidecar for auditability.
    audit = [
        {
            "rank": i,
            "id": r["entry"]["id"],
            "title_en": r["entry"]["title_en"],
            "title_ar": r["entry"]["title_ar"],
            "score_100": r["score"],
            "axes": r["axes"],
        }
        for i, r in enumerate(rows, 1)
    ]
    (ROOT / "data/fair_ranking.json").write_text(json.dumps({"date": "2026-06-27", "weights": WEIGHTS, "ranking": audit}, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
