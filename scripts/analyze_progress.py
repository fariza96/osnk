#!/usr/bin/env python3
"""Analisis uji coba (Tahap 5): rangkum berkas progres yang diekspor siswa dari halaman Progres situs.

  python3 scripts/analyze_progress.py FOLDER [--out laporan.md] [--min-n 5]

FOLDER berisi berkas `progres-osnk*.json` (format osnk-progres-v1). Simpan folder itu DI LUAR repositori
(atau di `data-siswa/`, yang diabaikan git): berkas progres adalah data siswa. Laporan tidak memuat nama berkas,
hanya hitungan, jadi aman dibagikan.

Laporan: (1) ringkasan diagnostik per bidang, (2) butir yang label kesulitannya mungkin tidak cocok dengan data,
(3) tabel per butir. Ambang (fondasi < 40% tuntas tanpa bantuan; tantangan > 80%) hanya penanda untuk ditinjau."""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOM = {"teori_bilangan": "Teori Bilangan", "aljabar": "Aljabar", "geometri": "Geometri", "kombinatorika": "Kombinatorika"}
DIFF = {"foundation": "fondasi", "core": "inti", "challenge": "tantangan"}


def load_bank():
    bank = {}
    for f in sorted((ROOT / "content/questions").glob("*.json")):
        for q in json.loads(f.read_text("utf-8")):
            bank[q["id"]] = q
    return bank


def load_students(folder):
    students, skipped = [], 0
    for f in sorted(Path(folder).glob("*.json")):
        try:
            j = json.loads(f.read_text("utf-8"))
            if j.get("format") != "osnk-progres-v1" or not isinstance(j.get("data"), dict):
                raise ValueError
            students.append(j["data"])
        except (ValueError, json.JSONDecodeError):
            skipped += 1
    return students, skipped


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out")
    ap.add_argument("--min-n", type=int, default=5, help="minimal siswa yang mencoba agar butir ditandai")
    a = ap.parse_args()
    bank = load_bank()
    students, skipped = load_students(a.folder)
    if not students:
        sys.exit("Tidak ada berkas progres yang valid di folder itu.")

    stat = defaultdict(lambda: {"tried": 0, "solved": 0, "unaided": 0, "attempts": 0, "hint": 0, "sol": 0})
    for s in students:
        for qid, r in s.items():
            if qid not in bank or not r.get("attempts"):
                continue
            t = stat[qid]
            t["tried"] += 1; t["attempts"] += r.get("attempts", 0)
            t["solved"] += bool(r.get("solved")); t["unaided"] += bool(r.get("solvedUnaided"))
            t["hint"] += r.get("hintsUsed", 0) > 0; t["sol"] += bool(r.get("solutionViewed"))

    L = [f"# Laporan uji coba\n\nBerkas progres valid: {len(students)}" + (f" ({skipped} berkas dilewati)" if skipped else "") +
         f". Butir yang dicoba paling sedikit satu siswa: {len(stat)}.\n"]

    # 1. Diagnostik per bidang: rata-rata proporsi tuntas tanpa bantuan per siswa
    dg = [q for q in bank.values() if q["id"].startswith("DG-")]
    if dg:
        L.append("## Diagnostik per bidang\n\nSoal diagnostik yang tidak dicoba dihitung belum tuntas.\n\n| Bidang | Rata-rata tuntas tanpa bantuan | Siswa di bawah 50% |\n|---|---|---|")
        for d, name in DOM.items():
            ids = [q["id"] for q in dg if q["domain"] == d]
            scores = [sum(bool(s.get(i, {}).get("solvedUnaided")) for i in ids) / len(ids)
                      for s in students if any(s.get(i, {}).get("attempts") for i in ids)]
            if scores:
                L.append(f"| {name} | {100 * sum(scores) / len(scores):.0f}% (n={len(scores)}) | {sum(x < 0.5 for x in scores)} |")
        L.append("")

    # 2. Penanda kesulitan
    flags = []
    for qid, t in stat.items():
        if t["tried"] < a.min_n:
            continue
        rate = t["unaided"] / t["tried"]
        d = bank[qid]["difficulty"]
        if d == "foundation" and rate < 0.4:
            flags.append(f"- {qid} (fondasi): hanya {pct(t['unaided'], t['tried'])} tuntas tanpa bantuan dari {t['tried']} siswa; mungkin lebih sulit dari label, atau redaksinya kabur.")
        if d == "challenge" and rate > 0.8:
            flags.append(f"- {qid} (tantangan): {pct(t['unaided'], t['tried'])} tuntas tanpa bantuan dari {t['tried']} siswa; mungkin lebih mudah dari label.")
        if t["solved"] and t["attempts"] / t["tried"] >= 4:
            flags.append(f"- {qid}: rata-rata {t['attempts'] / t['tried']:.1f} percobaan per siswa; periksa apakah format isian membingungkan.")
    L.append(f"## Butir untuk ditinjau (minimal {a.min_n} siswa mencoba)\n")
    L.append("\n".join(sorted(flags)) or "- tidak ada")

    # 3. Tabel per butir
    L.append("\n## Per butir\n\n| ID | Kesulitan | Mencoba | Tuntas | Tanpa bantuan | Pakai petunjuk | Lihat pembahasan | Rata-rata percobaan |\n|---|---|---|---|---|---|---|---|")
    for qid in sorted(stat):
        t = stat[qid]
        L.append(f"| {qid} | {DIFF[bank[qid]['difficulty']]} | {t['tried']} | {pct(t['solved'], t['tried'])} | "
                 f"{pct(t['unaided'], t['tried'])} | {pct(t['hint'], t['tried'])} | {pct(t['sol'], t['tried'])} | {t['attempts'] / t['tried']:.1f} |")
    text = "\n".join(L) + "\n"
    if a.out:
        Path(a.out).write_text(text, "utf-8")
        print(f"ditulis {a.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
