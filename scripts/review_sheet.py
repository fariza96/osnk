#!/usr/bin/env python3
"""Lembar tinjauan guru (Tahap 5): satu baris per butir, siap dibuka di Excel/Google Sheets.

  python3 scripts/review_sheet.py      # menulis review/tinjauan_guru.csv

Kolom isian guru (kosong): kesulitan_guru (fondasi/inti/tantangan), bahasa_ok (ya/tidak), keputusan
(terima/revisi/buang), catatan. Prioritas 1 = pilot (TB01, GE01) dan diagnostik; 2 = paket campuran; 3 = modul lain."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIFF = {"foundation": "fondasi", "core": "inti", "challenge": "tantangan"}
rows = []
for f in sorted((ROOT / "content/questions").glob("*.json")):
    for q in json.loads(f.read_text("utf-8")):
        grp = q["module_id"] or q["id"].split("-")[0]
        prio = 1 if grp in ("TB01", "GE01", "DG") else 2 if grp in ("MX1", "MX2") else 3
        route = f"#/m/{grp}" if q["module_id"] else f"#/p/{grp}"
        text = re.sub(r"\s+", " ", q["statement"]).strip()
        rows.append({
            "prioritas": prio, "id": q["id"], "modul_paket": grp, "halaman_situs": route,
            "peran": {"worked_example": "contoh", "practice": "latihan", "diagnostic": "diagnostik", "mixed": "campuran"}[q["role"]],
            "kesulitan": DIFF[q["difficulty"]], "menit": q["estimated_minutes"], "kunci": q["answer_spec"]["value"],
            "asal": q["origin"], "soal": text[:300] + ("…" if len(text) > 300 else ""),
            "kesulitan_guru": "", "bahasa_ok": "", "keputusan": "", "catatan": "",
        })
rows.sort(key=lambda r: (r["prioritas"], r["id"]))
out = ROOT / "review/tinjauan_guru.csv"
with out.open("w", newline="", encoding="utf-8-sig") as fh:  # BOM agar Excel membaca UTF-8
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
print(f"{out.relative_to(ROOT)}: {len(rows)} butir")
