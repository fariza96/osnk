#!/usr/bin/env python3
"""Validasi bank soal. Tanpa dependensi.

Pemakaian:
  python3 scripts/validate.py                # periksa content/questions
  python3 scripts/validate.py --release      # juga tolak butir yang belum verified
  python3 scripts/validate.py --dir PATH     # folder soal lain (dipakai tes)
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = ["id", "version", "module_id", "domain", "subtopic", "objective_id", "role", "difficulty",
            "estimated_minutes", "prerequisites", "technique_tags", "statement", "answer_type",
            "answer_spec", "hints", "solution", "key_idea", "common_error", "origin", "source_refs",
            "verification_status", "verification_notes"]
OPTIONAL = {"choices", "alternative_solution", "diagram", "diagram_alt"}
ENUMS = {
    "domain": {"teori_bilangan", "aljabar", "geometri", "kombinatorika"},
    "role": {"worked_example", "practice", "diagnostic", "mixed"},
    "difficulty": {"foundation", "core", "challenge"},
    "answer_type": {"integer", "rational", "decimal", "choice", "self_check"},
    "origin": {"original", "adapted", "reproduced_with_permission"},
    "verification_status": {"draft", "reviewed", "verified", "needs_revision", "quarantined"},
}
ID_RE = re.compile(r"^(?:(?P<mod>[A-Z]{2}\d{2})-(?P<kind>E\d{2}|P\d{3})|DG-\d{3}|MX\d-\d{3})$")
INT_RE = re.compile(r"^-?\d+$")
RAT_RE = re.compile(r"^-?\d+(?:/\d+|\.\d+)?$")
CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
DOMAIN_PREFIX = {"TB": "teori_bilangan", "AL": "aljabar", "GE": "geometri", "KO": "kombinatorika"}


def text_fields(q):
    out = [("statement", q.get("statement")), ("solution", q.get("solution")),
           ("key_idea", q.get("key_idea")), ("common_error", q.get("common_error")),
           ("alternative_solution", q.get("alternative_solution"))]
    out += [(f"hints[{i}]", h) for i, h in enumerate(q.get("hints") or [])]
    out += [(f"choices[{c.get('id')}]", c.get("text")) for c in q.get("choices") or []]
    out.append(("answer_spec.display", (q.get("answer_spec") or {}).get("display")))
    return [(k, v) for k, v in out if isinstance(v, str)]


def unescaped_dollars(s):
    return len(re.findall(r"(?<!\\)\$", s))


def check_item(q, modules, diagram_dir, err):
    qid = q.get("id", "<tanpa id>")
    for k in REQUIRED:
        if k not in q:
            err(qid, f"field wajib hilang: {k}")
    for k in q:
        if k not in REQUIRED and k not in OPTIONAL:
            err(qid, f"field tidak dikenal: {k}")
    for k, allowed in ENUMS.items():
        if k in q and q[k] not in allowed:
            err(qid, f"{k}={q[k]!r} tidak valid")

    m = ID_RE.match(qid) if isinstance(qid, str) else None
    if not m:
        err(qid, "format ID tidak valid")
    else:
        expected_role = ("worked_example" if m.group("kind") and m.group("kind").startswith("E")
                         else "practice" if m.group("kind")
                         else "diagnostic" if qid.startswith("DG") else "mixed")
        if q.get("role") != expected_role:
            err(qid, f"role harus {expected_role} untuk ID ini")
        if m.group("mod"):
            if q.get("module_id") != m.group("mod"):
                err(qid, "module_id tidak cocok dengan prefiks ID")
    mod = q.get("module_id")
    if mod is not None:
        if mod not in modules:
            err(qid, f"module_id {mod} tidak ada di modules.json")
        elif q.get("domain") != DOMAIN_PREFIX.get(mod[:2]):
            err(qid, "domain tidak cocok dengan module_id")
    for p in q.get("prerequisites") or []:
        if p not in modules:
            err(qid, f"prasyarat {p} tidak dikenal")

    if not isinstance(q.get("version"), int) or q["version"] < 1:
        err(qid, "version harus bilangan bulat ≥ 1")
    em = q.get("estimated_minutes")
    if not isinstance(em, int) or not 1 <= em <= 30:
        err(qid, "estimated_minutes harus 1–30")
    if not q.get("technique_tags"):
        err(qid, "technique_tags kosong")
    for k in ("statement", "solution", "key_idea", "common_error", "subtopic", "objective_id"):
        if k in q and (not isinstance(q[k], str) or not q[k].strip()):
            err(qid, f"{k} kosong")
    hints = q.get("hints")
    if not isinstance(hints, list) or len(hints) != 2 or not all(isinstance(h, str) and h.strip() for h in hints):
        err(qid, "hints harus tepat 2 teks tidak kosong")

    at, spec = q.get("answer_type"), q.get("answer_spec") or {}
    if not isinstance(spec.get("display"), str) or not spec["display"].strip():
        err(qid, "answer_spec.display wajib")
    if at == "integer":
        if not INT_RE.match(str(spec.get("value", ""))):
            err(qid, "answer_spec.value harus bilangan bulat (string)")
    elif at == "rational":
        if not RAT_RE.match(str(spec.get("value", ""))):
            err(qid, "answer_spec.value harus p/q, bulat, atau desimal hingga")
        elif "/" in spec["value"] and spec["value"].split("/")[1].lstrip("0") == "":
            err(qid, "penyebut nol")
    elif at == "decimal":
        try:
            float(spec.get("value"))
            if not (isinstance(spec.get("tolerance"), (int, float)) and spec["tolerance"] > 0):
                raise ValueError
        except (TypeError, ValueError):
            err(qid, "decimal butuh value numerik dan tolerance > 0")
    elif at == "choice":
        ch = q.get("choices") or []
        ids = [c.get("id") for c in ch]
        texts = [re.sub(r"\s+", "", c.get("text", "")) for c in ch]
        if len(ch) < 2:
            err(qid, "choice butuh ≥ 2 opsi")
        if len(set(ids)) != len(ids) or not all(re.match(r"^[A-E]$", i or "") for i in ids):
            err(qid, "ID opsi harus unik A–E")
        if len(set(texts)) != len(texts):
            err(qid, "teks opsi ganda")
        if spec.get("correct") not in ids:
            err(qid, "answer_spec.correct tidak menunjuk ID opsi")
    elif at == "self_check":
        if not (isinstance(spec.get("rubric"), list) and spec["rubric"]):
            err(qid, "self_check butuh answer_spec.rubric (daftar)")
    if at != "choice" and q.get("choices"):
        err(qid, "choices hanya untuk answer_type choice")

    if q.get("diagram"):
        if not (diagram_dir / q["diagram"]).is_file():
            err(qid, f"diagram {q['diagram']} tidak ditemukan")
        if not (q.get("diagram_alt") or "").strip():
            err(qid, "diagram_alt wajib bila ada diagram")
    if q.get("origin") in ("adapted", "reproduced_with_permission") and not q.get("source_refs"):
        err(qid, "soal adaptasi/reproduksi wajib punya source_refs")

    for name, s in text_fields(q):
        if CTRL_RE.search(s):
            err(qid, f"{name}: karakter kontrol (kemungkinan backslash LaTeX tidak di-escape di JSON)")
        if '\\"' in s:
            err(qid, f"{name}: ada \\\" (tanda kutip ter-escape ganda akan tampil sebagai backslash)")
        if unescaped_dollars(s) % 2:
            err(qid, f"{name}: jumlah $ ganjil")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--dir", default=str(ROOT / "content" / "questions"))
    args = ap.parse_args()

    qdir = Path(args.dir)
    modules = {m["id"] for m in json.loads((ROOT / "content/modules/modules.json").read_text("utf-8"))}
    diagram_dir = ROOT / "content" / "diagrams"
    errors, seen, items = [], {}, []

    def err(qid, msg):
        errors.append(f"{qid}: {msg}")

    for f in sorted(qdir.glob("*.json")):
        try:
            data = json.loads(f.read_text("utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: JSON tidak valid ({e})")
            continue
        if not isinstance(data, list):
            errors.append(f"{f.name}: isi harus array butir")
            continue
        for q in data:
            qid = q.get("id")
            if qid in seen:
                err(qid, f"ID ganda ({seen[qid]} dan {f.name})")
            seen[qid] = f.name
            check_item(q, modules, diagram_dir, err)
            items.append(q)

    if args.release:
        for q in items:
            if q.get("verification_status") != "verified":
                err(q.get("id"), f"status {q.get('verification_status')} tidak boleh masuk rilis")

    counts = {}
    for q in items:
        key = (q.get("module_id") or q["id"][:3], q.get("role"), q.get("verification_status"))
        counts[key] = counts.get(key, 0) + 1
    print(f"{len(items)} butir dari {qdir}")
    for (mod, role, st), n in sorted(counts.items(), key=lambda kv: tuple(map(str, kv[0]))):
        print(f"  {mod:5} {role:15} {st:15} {n}")
    if errors:
        print(f"\n{len(errors)} masalah:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
