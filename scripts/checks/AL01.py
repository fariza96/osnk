#!/usr/bin/env python3
"""Pemeriksaan komputasional AL01: aritmetika eksak (sympy/Fraction) dan enumerasi dari pernyataan soal.
Enumerasi rentang hingga hanya memeriksa jawaban, bukan pengganti bukti."""
import json
import sys
from fractions import Fraction
from pathlib import Path

from sympy import Poly, factorint, real_roots, simplify, solve, sqrt, symbols

BANK = Path(__file__).resolve().parents[2] / "content/questions/AL01.json"
x, t = symbols("x t")


def E01():  # x + 1/x = 3 -> x^4 + 1/x^4
    vals = {simplify(r**4 + 1 / r**4) for r in solve(x + 1 / x - 3, x)}
    assert len(vals) == 1
    return vals.pop()


def E02():  # bilangan bulat positif (x,y) dengan xy - 2x - 3y = 6
    return sum(1 for a in range(1, 2000) for b in range(1, 2000) if a * b - 2 * a - 3 * b == 6)


def P001():
    return 2026 * 2024 - 2025**2


def P002():  # a+b=7, ab=10 -> a^3+b^3
    a, b = 2, 5
    assert a + b == 7 and a * b == 10
    return a**3 + b**3


def P003():  # sum_{k=1}^{99} 1/(sqrt(k)+sqrt(k+1)), numerik 40 digit
    return round(float(sum(1 / (sqrt(k) + sqrt(k + 1)) for k in range(1, 100)).evalf(40)), 10)


def P004():  # x^2 - y^2 = 45, x,y bulat positif
    return sum(1 for a in range(1, 100) for b in range(1, 100) if a * a - b * b == 45)


def P005():  # a - b = 3, ab = 4 -> a^3 - b^3 (dua pasangan (a,b))
    sols = solve([symbols("a") - symbols("b") - 3, symbols("a") * symbols("b") - 4], [symbols("a"), symbols("b")])
    vals = {a**3 - b**3 for a, b in sols}
    assert len(vals) == 1
    return vals.pop()


def P006():  # xy + 3x + 2y = 30, x,y bulat positif; jumlah semua x
    return sum(a for a in range(1, 100) for b in range(1, 100) if a * b + 3 * a + 2 * b == 30)


def P007():  # faktor prima terbesar 18^4 + 4
    return max(factorint(18**4 + 4))


def P008():  # x+y=1, x^2+y^2=3 -> x^4+y^4
    a, b = symbols("a b")
    vals = {simplify(p**4 + q**4) for p, q in solve([a + b - 1, a**2 + b**2 - 3], [a, b])}
    assert len(vals) == 1
    return vals.pop()


def P009():
    v = Fraction(2024**3 + 1, 2024**2 - 2023)
    assert v.denominator == 1
    return v.numerator


def P010():  # a+b+c=5, ab+bc+ca=2, abc=-1 -> a^3+b^3+c^3; akar real
    rs = real_roots(Poly(t**3 - 5 * t**2 + 2 * t + 1, t))
    assert len(rs) == 3
    return round(float(sum(r.evalf(50) ** 3 for r in rs)), 9)


def P011():  # sum_{k=1}^{99} 1/((k+1)sqrt(k) + k sqrt(k+1))
    s = sum(1 / ((k + 1) * sqrt(k) + k * sqrt(k + 1)) for k in range(1, 100))
    return Fraction(round(float(s.evalf(40)) * 10**9), 10**9).limit_denominator(1000)


def P012():  # 1/x + 1/y = 1/6, x,y bulat tak nol; |x|,|y| <= 6+36 cukup karena (x-6)(y-6)=36
    return sum(1 for a in range(-100, 101) for b in range(-100, 101)
               if a and b and Fraction(1, a) + Fraction(1, b) == Fraction(1, 6))


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"AL01-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        ok = key != "—" and Fraction(str(key)) == Fraction(str(got))
        bad += not ok
        print(f"{qid}: hitung={got} kunci={key} {'OK' if ok else 'BEDA'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
