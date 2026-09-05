#!/usr/bin/env python3
"""Generate a tree visualization SVG from data/categories.json + data/stats.json.

Dependency-free (stdlib only) — same convention as the other scripts in this repo.
Output: assets/tree-visual.svg

This script is the source of truth for the tree visualization;
the SVG file itself is the rendered output (committed to the repo so
the README can link to it without requiring users to run the script).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "tree-visual.svg"

cats = json.loads((ROOT / "data" / "categories.json").read_text(encoding="utf-8"))
stats = json.loads((ROOT / "data" / "stats.json").read_text(encoding="utf-8"))

l1 = sorted([c for c in cats if c.get("level") == 1], key=lambda c: c["id"])
l2_by_parent = {}
for c in cats:
    if c.get("level") == 2:
        l2_by_parent.setdefault(c.get("parent"), []).append(c)
for v in l2_by_parent.values():
    v.sort(key=lambda c: c["id"])

# Color palette for L1 categories
COLORS = ["#DC2626", "#EA580C", "#CA8A04", "#65A30D", "#059669", "#0891B2", "#7C3AED"]

# Layout
W, H = 900, 800
def header_lines():
    return [
        f'<text x="450" y="30" text-anchor="middle" class="title">AI Cost Library — Tree Visualization</text>',
        f'<text x="450" y="50" text-anchor="middle" class="subtitle">'
        f'{len(l1)} categories · {len(l2_by_parent)} subcategory groups · '
        f'{stats["total_entries"]} entries (60 ranked + 1 pending) · generated 2026-09-05</text>',
    ]

# Root box
ROOT_Y = 70
def root_box():
    return [
        '<rect x="350" y="70" width="200" height="36" rx="6" class="root-bg"/>',
        '<text x="450" y="93" text-anchor="middle" class="root">AI Cost Library</text>',
    ]

# L1 boxes (top row, 5 of them + 2 below)
def l1_section(i, cat, x, y, color):
    lines = [
        f'<line x1="450" y1="106" x2="{x+70}" y2="{y}" class="l2-line"/>',
        f'<rect x="{x}" y="{y}" width="140" height="30" rx="4" fill="{color}"/>',
        f'<text x="{x+70}" y="{y+20}" text-anchor="middle" class="l1">'
        f'{cat["id"].split("-")[0]}. {cat["id"].split("-", 1)[1][:10]} ({cat["entry_count"]})</text>',
    ]
    # Subcategories
    for j, sub in enumerate(l2_by_parent.get(cat["id"], [])):
        lines.append(
            f'<text x="{x}" y="{y + 50 + j*15}" class="l2">'
            f'├ {sub["id"][:18]} ({sub["entry_count"]})</text>'
        )
    return lines

# ... (full SVG generation here)

# For simplicity, use a static template with category data interpolated
parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 800" font-family="system-ui, -apple-system, sans-serif">']
parts.append('''<style>
  .title { font-size: 22px; font-weight: 700; fill: #0F172A; }
  .subtitle { font-size: 12px; fill: #64748B; }
  .root { font-size: 14px; font-weight: 700; fill: #FFFFFF; }
  .root-bg { fill: #1E40AF; }
  .l1 { font-size: 12px; font-weight: 600; fill: #FFFFFF; }
  .l2 { font-size: 10px; fill: #334155; }
  .l2-line { stroke: #94A3B8; stroke-width: 1; fill: none; }
  .legend { font-size: 10px; fill: #475569; }
</style>
<rect width="900" height="800" fill="#F8FAFC"/>''')
parts.extend(header_lines())
parts.extend(root_box())

# Render 7 L1 categories
# Top row: 5 categories
# Bottom row: 2 categories
# 1-5 in top row at y=150
# 6-7 in bottom row at y=320
top_x_positions = [40, 190, 340, 490, 640]
bottom_x_positions = [40, 190]
for i, cat in enumerate(l1):
    if i < 5:
        x = top_x_positions[i]
        y = 150
    else:
        x = bottom_x_positions[i - 5]
        y = 320
    color = COLORS[i % len(COLORS)]
    parts.extend(l1_section(i, cat, x, y, color))

# Counts panel
parts.append('''<rect x="380" y="320" width="500" height="160" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
<text x="400" y="345" class="l1" fill="#0F172A">Counts</text>''')

# Status
parts.append(f'<text x="400" y="370" class="l2">Type:  practical={stats["classification"]["practical"]}  emerging={stats["classification"]["emerging"]}  theoretical={stats["classification"]["theoretical"]}  pending={stats["classification"]["pending"]}</text>')
parts.append(f'<text x="400" y="388" class="l2">Sources: {stats["total_sources"]}  Claims: {stats["total_claims"]}  Evidence: {stats["total_evidence_records"]}  Glossary: {stats["total_glossary_terms"]}</text>')
parts.append('<text x="400" y="406" class="l2">Skipped from RANKING: 1 (entry-model-router-cascade, pending)</text>')

# Legend
parts.append('''<text x="40" y="540" class="l1" fill="#0F172A">Legend</text>
<text x="40" y="560" class="l2">L1 (category): colored box with count</text>
<text x="40" y="575" class="l2">L2 (subcategory): text under L1, with count</text>
<text x="40" y="590" class="l2">Pending entry: shown at L1 level (no subcategory)</text>
<text x="40" y="620" class="l2" fill="#64748B">Source: data/categories.json + data/stats.json (re-runnable)</text>
<text x="40" y="635" class="l2" fill="#64748B">Replaces the original 100x100 placeholder.</text>
<text x="40" y="755" class="legend">License: MIT (per repo root)  ·  Generated: 2026-09-05</text>''')

parts.append('</svg>')

OUT.write_text('\n'.join(parts) + '\n', encoding="utf-8")
print(f"Tree visualization saved to {OUT}")
print(f"Categories: {len(l1)}  Subcategory groups: {len(l2_by_parent)}  Total entries: {stats['total_entries']}")
