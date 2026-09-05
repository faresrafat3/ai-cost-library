#!/usr/bin/env python3
"""Generate a clean SVG dashboard visualization from data/stats.json + categories.json.

Dependency-free (stdlib only) — same convention as the other scripts in this repo.
Output: assets/dashboard.svg
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "dashboard.svg"

stats = json.loads((ROOT / "data" / "stats.json").read_text(encoding="utf-8"))
categories = json.loads((ROOT / "data" / "categories.json").read_text(encoding="utf-8"))

# Filter to top-level categories only
top_cats = [c for c in categories if c.get("level") == 1]
top_cats.sort(key=lambda c: c["id"])

# Color palette
BG = "#0F172A"          # slate-900
PANEL = "#1E293B"       # slate-800
ACCENT = "#3B82F6"      # blue-500
ACCENT2 = "#10B981"     # emerald-500
ACCENT3 = "#F59E0B"     # amber-500
TEXT = "#E2E8F0"        # slate-200
TEXT_DIM = "#94A3B8"    # slate-400
GRID = "#334155"        # slate-700

total = stats["total_entries"]
practical = stats["classification"]["practical"]
emerging = stats["classification"]["emerging"]
theoretical = stats["classification"]["theoretical"]
sources = stats["total_sources"]
glossary = stats["total_glossary_terms"]
claims = stats["total_claims"]
version = stats["version"]

# --- Layout ---
W = 880
H = 460

# Bars
max_count = max(c["entry_count"] for c in top_cats) or 1
bar_area_x = 260
bar_area_w = 560
bar_h = 24
bar_gap = 14
bars_total_h = len(top_cats) * (bar_h + bar_gap) - bar_gap
bars_start_y = 150

# Stacked classification bar
stack_y = 380
stack_h = 28
stack_x = 60
stack_w = 760

parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter, "Helvetica Neue", Arial, sans-serif">')

# Background
parts.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# Title
parts.append(f'<text x="40" y="50" fill="{TEXT}" font-size="22" font-weight="700">AI Cost Library — Dashboard</text>')
parts.append(f'<text x="40" y="74" fill="{TEXT_DIM}" font-size="13">v{version} · last updated {stats["last_updated"]}</text>')

# --- KPI strip (top) ---
kpi_y = 100
kpis = [
    ("Entries", str(total), ACCENT),
    ("Sources", str(sources), ACCENT2),
    ("Glossary", str(glossary), ACCENT3),
    ("Claims", str(claims), ACCENT),
]
kpi_w = 130
kpi_gap = 14
kpi_x = 40
for label, value, color in kpis:
    parts.append(f'<rect x="{kpi_x}" y="{kpi_y}" width="{kpi_w}" height="40" rx="6" fill="{PANEL}"/>')
    parts.append(f'<rect x="{kpi_x}" y="{kpi_y}" width="3" height="40" fill="{color}"/>')
    parts.append(f'<text x="{kpi_x+14}" y="{kpi_y+17}" fill="{TEXT_DIM}" font-size="11">{label}</text>')
    parts.append(f'<text x="{kpi_x+14}" y="{kpi_y+33}" fill="{TEXT}" font-size="15" font-weight="600">{value}</text>')
    kpi_x += kpi_w + kpi_gap

# --- Bars: entries per top-level category ---
parts.append(f'<text x="40" y="170" fill="{TEXT}" font-size="13" font-weight="600">Entries per category</text>')

# Subtle gridlines
for i in range(1, 5):
    gx = bar_area_x + (bar_area_w * i / 5)
    parts.append(f'<line x1="{gx}" y1="{bars_start_y}" x2="{gx}" y2="{bars_start_y + bars_total_h}" stroke="{GRID}" stroke-width="1" stroke-dasharray="2,3"/>')

for i, c in enumerate(top_cats):
    y = bars_start_y + i * (bar_h + bar_gap)
    count = c["entry_count"]
    w = int(bar_area_w * count / max_count)
    label = c["id"].split("-", 1)[1].replace("-", " ").title()
    parts.append(f'<text x="40" y="{y + bar_h - 7}" fill="{TEXT}" font-size="12">{label}</text>')
    parts.append(f'<rect x="{bar_area_x}" y="{y}" width="{w}" height="{bar_h}" rx="3" fill="{ACCENT}"/>')
    parts.append(f'<text x="{bar_area_x + w + 8}" y="{y + bar_h - 7}" fill="{TEXT_DIM}" font-size="12">{count}</text>')

# --- Classification bar (stacked) ---
parts.append(f'<text x="40" y="370" fill="{TEXT}" font-size="13" font-weight="600">Classification breakdown</text>')

cls_items = [
    ("Practical", practical, ACCENT2),
    ("Emerging", emerging, ACCENT3),
    ("Theoretical", theoretical, ACCENT),
]
x_cursor = stack_x
for label, count, color in cls_items:
    if count == 0:
        continue
    seg_w = int(stack_w * count / total) if total else 0
    parts.append(f'<rect x="{x_cursor}" y="{stack_y}" width="{seg_w}" height="{stack_h}" fill="{color}"/>')
    if seg_w > 40:
        parts.append(f'<text x="{x_cursor + seg_w/2}" y="{stack_y + 18}" fill="{BG}" font-size="11" font-weight="600" text-anchor="middle">{label}: {count}</text>')
    x_cursor += seg_w

# Legend for classification
legend_y = stack_y + stack_h + 18
lx = stack_x
for label, count, color in cls_items:
    parts.append(f'<rect x="{lx}" y="{legend_y - 11}" width="12" height="12" rx="2" fill="{color}"/>')
    parts.append(f'<text x="{lx + 18}" y="{legend_y}" fill="{TEXT_DIM}" font-size="11">{label} ({count})</text>')
    lx += 150

# Footer
parts.append(f'<text x="40" y="{H - 18}" fill="{TEXT_DIM}" font-size="11">Bilingual (Arabic/English) · Evidence-based · No-hype policy · github.com/faresrafat3/ai-cost-library</text>')

parts.append('</svg>')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(parts), encoding="utf-8")
print(f"Dashboard saved to {OUT.relative_to(ROOT)}")
print(f"  Entries: {total} | Sources: {sources} | Categories: {len(top_cats)}")
