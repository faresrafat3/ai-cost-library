#!/usr/bin/env python3
"""Synchronize lightweight metadata from the markdown knowledge tree.
This script is intentionally dependency-free so future agents can run it in a fresh shell.
"""
from __future__ import annotations
from pathlib import Path
import json, re, datetime, collections

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-06-26"

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")

def front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    out = {}
    for line in parts[1].splitlines():
        if ":" not in line or line.startswith("  "):
            continue
        k, v = line.split(":", 1)
        v = v.strip().strip('"')
        if v.startswith("[") and v.endswith("]"):
            vals=[x.strip().strip('"\'') for x in v[1:-1].split(',') if x.strip()]
            out[k.strip()] = vals
        else:
            out[k.strip()] = v
    return out

entry_files = sorted(p for p in (ROOT/"library").glob("**/*.md") if p.name != "README.md")
entries=[]
type_counts=collections.Counter()
status_counts=collections.Counter()
for p in entry_files:
    txt=read(p)
    fm=front_matter(txt)
    entry_id=fm.get("id") or f"entry-{p.stem}"
    typ=fm.get("type", "pending")
    status=fm.get("status", "pending")
    type_counts[typ]+=1
    status_counts[status]+=1
    entries.append({
        "id": entry_id,
        "title_ar": fm.get("title_ar", p.stem.replace('-', ' ')),
        "title_en": fm.get("title_en", p.stem.replace('-', ' ').title()),
        "type": typ,
        "status": status,
        "category": fm.get("category", p.parts[1] if len(p.parts)>1 else "library"),
        "subcategory": fm.get("subcategory", p.parts[-2] if len(p.parts)>2 else "uncategorized"),
        "path": str(p.relative_to(ROOT)),
        "cost_dimensions": fm.get("cost_dimensions", []),
        "proof_score": fm.get("proof_score", ""),
        "sources_count": int(fm.get("sources_count", "0") or 0) if str(fm.get("sources_count", "0")).isdigit() else 0,
        "updated": fm.get("updated", TODAY),
    })

# Count source records in markdown conservatively from Tier markers.
tier_re = re.compile(r"\[Tier\s+[123]\]", re.I)
source_records=[]
seen=set()
for p in sorted(ROOT.glob("**/*.md")):
    if ".git" in p.parts:
        continue
    for line in read(p).splitlines():
        if tier_re.search(line):
            key=(str(p.relative_to(ROOT)), line.strip())
            if key in seen: continue
            seen.add(key)
            source_records.append({"id": f"SRC-AUTO-{len(source_records)+1:03d}", "path": key[0], "record": key[1]})

# Tree/category counts from directories.
l1=[]
for d in sorted(x for x in (ROOT/"library").iterdir() if x.is_dir()):
    if d.name == "README.md":
        continue
    subs=[]
    for s in sorted(x for x in d.iterdir() if x.is_dir()):
        files=[p for p in s.glob("**/*.md") if p.name != "README.md"]
        subs.append({"id": s.name, "path": str(s.relative_to(ROOT)), "entry_count": len(files), "entries": [e["id"] for e in entries if str(e["path"]).startswith(str(s.relative_to(ROOT))+"/")]})
    files=[p for p in d.glob("**/*.md") if p.name != "README.md"]
    l1.append({"id": d.name, "path": str(d.relative_to(ROOT)), "entry_count": len(files), "subcategories": subs})

# Existing manually curated claims/evidence are preserved if valid.
def load_json(path, fallback):
    try:
        return json.loads((ROOT/path).read_text(encoding="utf-8"))
    except Exception:
        return fallback
claims=load_json(Path("data/claims.json"), {"claims": []}).get("claims", []) if isinstance(load_json(Path("data/claims.json"), {}), dict) else []
evidence=load_json(Path("data/evidence.json"), {"evidence": []}).get("evidence", []) if isinstance(load_json(Path("data/evidence.json"), {}), dict) else []
gloss=load_json(Path("data/glossary.json"), {"terms": []})
terms=gloss.get("terms", []) if isinstance(gloss, dict) else []

(ROOT/"data/entries.json").write_text(json.dumps({"version":"2.1.0","last_updated":TODAY,"entries":entries}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(ROOT/"data/sources.json").write_text(json.dumps({"version":"2.1.0","last_updated":TODAY,"sources":source_records,"note_ar":"سجل آلي خفيف مستخرج من أسطر [Tier] في ملفات Markdown؛ لا يغني عن المراجعة اليدوية للمصادر المهمة.","note_en":"Lightweight automatic ledger extracted from [Tier] lines in Markdown files; important sources still require manual review."}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
(ROOT/"data/tree.json").write_text(json.dumps({"version":"2.1.0","last_updated":TODAY,"tree":{"root":"AI Cost Library","categories":l1}}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
cat_list=[]
for c in l1:
    cat_list.append({"id":c["id"],"level":1,"path":c["path"],"entry_count":c["entry_count"],"subcategory_count":len(c["subcategories"]),"status":"active"})
    for s in c["subcategories"]:
        cat_list.append({"id":s["id"],"level":2,"parent":c["id"],"path":s["path"],"entry_count":s["entry_count"],"status":"active" if s["entry_count"] else "seeded"})
(ROOT/"data/categories.json").write_text(json.dumps(cat_list, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

stats={
    "version":"2.1.0",
    "last_updated":TODAY,
    "total_entries":len(entries),
    "total_categories":len(l1),
    "total_subcategories":sum(len(c["subcategories"]) for c in l1),
    "total_sources":len(source_records),
    "total_glossary_terms":len(terms),
    "total_claims":len(claims),
    "total_evidence_records":len(evidence),
    "classification":{
        "practical": type_counts.get("practical",0),
        "emerging": type_counts.get("emerging",0),
        "theoretical": type_counts.get("theoretical",0),
        "rejected": type_counts.get("rejected",0),
        "pending": type_counts.get("pending",0),
    },
    "status_counts": dict(status_counts),
    "quality_note_ar":"الأرقام مستخرجة آلياً من ملفات Markdown في هذه الجلسة؛ راجع المصادر الرقمية الحساسة يدوياً قبل اتخاذ قرارات إنتاجية.",
}
(ROOT/"data/stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(stats, ensure_ascii=False, indent=2))
