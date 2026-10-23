"""Pembanding bersama untuk skrip cek paket (DG, MX1, MX2): menjalankan fungsi bernama sesuai nomor butir."""
import json
import sys
from fractions import Fraction
from pathlib import Path


def fmt(v):
    if isinstance(v, Fraction):
        return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"
    return str(v).replace(" ", "")


def run(pack, funcs):
    bank_path = Path(__file__).resolve().parents[2] / f"content/questions/{pack}.json"
    bank = {q["id"]: q for q in json.loads(bank_path.read_text("utf-8"))}
    bad = 0
    for name, fn in funcs:
        qid = f"{pack}-{name[1:]}"
        got = fmt(fn())
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if got == key else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    missing = set(bank) - {f"{pack}-{n[1:]}" for n, _ in funcs}
    for qid in sorted(missing):
        print(f"{qid}: tidak dicek BEDA")
    sys.exit(1 if bad or missing else 0)
