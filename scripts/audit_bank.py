#!/usr/bin/env python3
"""Audit lintas bank (Tahap 5): pemeriksaan otomatis yang melengkapi audit per butir.

  python3 scripts/audit_bank.py            # ringkasan ke layar
  python3 scripts/audit_bank.py --write    # juga menulis review/audit_bank.md

Memeriksa: komposisi per modul (2 contoh; 3 fondasi, 6 inti, 3 tantangan), objective_id yang ada di materi,
kunci yang muncul di pembahasan, kemiripan pernyataan antarbutir, kunci+teknik yang kembar, dan durasi paket.
Temuan berupa peringatan untuk diperiksa manusia, bukan kesalahan pasti."""
import json
import re
import sys
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q = []
for f in sorted((ROOT / "content/questions").glob("*.json")):
    Q += json.loads(f.read_text("utf-8"))
modules = json.loads((ROOT / "content/modules/modules.json").read_text("utf-8"))
out, warn = [], []


def norm(s):
    s = re.sub(r"\\[a-zA-Z]+|[{}$\\^_]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


# 1. Komposisi per modul
out.append("## Komposisi per modul\n\n| Modul | Contoh | Fondasi | Inti | Tantangan | Total | Status |\n|---|---|---|---|---|---|---|")
for m in modules:
    qs = [q for q in Q if q["module_id"] == m["id"]]
    ex = sum(q["role"] == "worked_example" for q in qs)
    c = Counter(q["difficulty"] for q in qs if q["role"] == "practice")
    ok = ex == 2 and (c["foundation"], c["core"], c["challenge"]) == (3, 6, 3)
    st = Counter(q["verification_status"] for q in qs)
    out.append(f"| {m['id']} | {ex} | {c['foundation']} | {c['core']} | {c['challenge']} | {len(qs)} | "
               f"{', '.join(f'{k} {v}' for k, v in st.items())} |")
    if not ok:
        warn.append(f"{m['id']}: komposisi tidak 2 contoh + 3/6/3")

# 2. objective_id ada di materi modul
objs = set()
for f in (ROOT / "content/modules").glob("*.md"):
    objs |= set(re.findall(r"\*\*([A-Z]{2}\d{2}-O\d+)\*\*", f.read_text("utf-8")))
for q in Q:
    if q["objective_id"] not in objs:
        warn.append(f"{q['id']}: objective_id {q['objective_id']} tidak ditemukan di materi")


# 3. Kunci muncul di pembahasan (heuristik)
def key_forms(q):
    v = q["answer_spec"].get("value", "")
    forms = {v}
    if "/" in v:
        p, r = v.lstrip("-").split("/")
        forms |= {f"\\frac{{{p}}}{{{r}}}", f"\\frac{p}{r}", f"\\tfrac{{{p}}}{{{r}}}", f"\\tfrac{p}{r}", f"\\frac{p}{{{r}}}",
                  f"\\frac{{{p}}}{r}", f"\\tfrac{p}{{{r}}}", f"\\tfrac{{{p}}}{r}", f"\\dfrac{{{p}}}{{{r}}}", f"\\dfrac{p}{r}"}
    return forms


for q in Q:
    sol = re.sub(r"\\,|\{,\}|\\!|\s", "", q["solution"])  # pemisah ribuan dan spasi diabaikan
    if q["answer_type"] in ("integer", "rational") and not any(f.replace(" ", "") in sol for f in key_forms(q)):
        warn.append(f"{q['id']}: kunci {q['answer_spec']['value']} tidak tertulis apa adanya di pembahasan")

# 4. Kemiripan pernyataan antarbutir
pairs = []
texts = {q["id"]: norm(q["statement"]) for q in Q}
for a, b in combinations(Q, 2):
    r = SequenceMatcher(None, texts[a["id"]], texts[b["id"]]).ratio()
    if r >= 0.9:
        pairs.append((r, a["id"], b["id"]))
for r, a, b in sorted(pairs, reverse=True):
    warn.append(f"{a} ~ {b}: kemiripan teks {r:.2f}")

# 5. Kunci dan teknik kembar
grp = defaultdict(list)
for q in Q:
    grp[(q["answer_spec"].get("value"), tuple(sorted(q["technique_tags"])))].append(q["id"])
for (v, t), ids in grp.items():
    if len(ids) > 1:
        warn.append(f"{', '.join(ids)}: kunci ({v}) dan teknik ({', '.join(t)}) sama")

# 6. Paket: durasi, sebaran bidang dan kesulitan
out.append("\n## Paket\n\n| Paket | Butir | Menit (jumlah perkiraan) | Per bidang | Fondasi/Inti/Tantangan |\n|---|---|---|---|---|")
for p in ("DG", "MX1", "MX2"):
    qs = [q for q in Q if q["id"].startswith(p + "-")]
    if not qs:
        continue
    dom = Counter(q["domain"] for q in qs)
    d = Counter(q["difficulty"] for q in qs)
    out.append(f"| {p} | {len(qs)} | {sum(q['estimated_minutes'] for q in qs)} | "
               f"{', '.join(f'{k} {v}' for k, v in sorted(dom.items()))} | {d['foundation']}/{d['core']}/{d['challenge']} |")

# 7. Ringkasan status dan asal
st = Counter(q["verification_status"] for q in Q)
og = Counter(q["origin"] for q in Q)
out.insert(0, f"Total butir: {len(Q)}. Status: {dict(st)}. Asal: {dict(og)}.\n")

report = "\n".join(out) + "\n\n## Peringatan untuk diperiksa\n\n" + ("\n".join(f"- {w}" for w in warn) or "- tidak ada") + "\n"
print(report)
if "--write" in sys.argv:
    dest = ROOT / "review/audit_bank.md"
    old = dest.read_text("utf-8") if dest.exists() else ""
    keep = old[old.index("\n## Tindak lanjut"):] if "\n## Tindak lanjut" in old else ""  # catatan manusia dipertahankan
    dest.write_text(
        "# Audit lintas bank (Tahap 5)\n\nDibuat oleh `python3 scripts/audit_bank.py --write`. Peringatan adalah heuristik "
        "(kemiripan teks, kunci yang tidak tertulis persis di pembahasan); setiap peringatan diperiksa manusia dan hasilnya "
        "dicatat di bagian **Tindak lanjut**.\n\n" + report + keep, "utf-8")
