#!/usr/bin/env python3
"""Pemeriksaan komputasional AL06. Aritmetika kompleks eksak dengan sympy (I, akar satuan dalam bentuk eksak),
nilai trigonometri disederhanakan secara simbolik dan dicek numerik presisi tinggi, pencacahan himpunan bagian
dengan pencarian lengkap. Rumus di pembahasan (De Moivre, saringan akar satuan) tidak dipakai."""
import json
import sys
from itertools import combinations
from math import comb
from pathlib import Path

from sympy import I, Abs, Rational, atan, cos, exp, expand, im, nsimplify, pi, re, simplify, sin, solve, sqrt, symbols, tan

BANK = Path(__file__).resolve().parents[2] / "content/questions/AL06.json"
a, b, x = symbols("a b x", real=True)


def num(e):
    """Nilai eksak yang dicek numerik 50 digit."""
    v = simplify(e)
    assert abs(complex(e.evalf(50)) - complex(v.evalf(50))) < 1e-40
    return v


def E01():
    return expand((1 + I * sqrt(3)) ** 9)


def E02():
    w = Rational(-1, 2) + I * sqrt(3) / 2
    assert expand(w ** 3) == 1 and w != 1
    return expand((1 - w + w ** 2) * (1 + w - w ** 2))


def P001():
    z = expand((2 + 3 * I) * (4 - I))
    return re(z) + im(z)


def P002():
    return num(Abs((1 + 7 * I) / (1 - I)))


def P003():
    # semua x real dengan sin x + cos x = 7/5: sin2x sama untuk setiap solusi
    vals = set()
    for s_ in solve([a + b - Rational(7, 5), a ** 2 + b ** 2 - 1], [a, b]):
        vals.add(2 * s_[0] * s_[1])
    assert len(vals) == 1
    return vals.pop()


def P004():
    S = sum(k * I ** k for k in range(1, 21))
    return expand(S * S.conjugate())


def P005():
    return next(n for n in range(1, 100) if (lambda z: im(z) == 0 and re(z) > 0)(expand((sqrt(3) + I) ** n)))


def P006():  # sisa pembagian oleh x^4+x^3+x^2+x+1 (polinom minimal setiap akar ke-5 satuan selain 1)
    from sympy import rem
    r = rem(expand((1 - x) * (1 - x ** 2) * (1 - x ** 3) * (1 - x ** 4)), x ** 4 + x ** 3 + x ** 2 + x + 1, x)
    z = exp(2 * pi * I / 5)
    assert abs(complex(((1 - z) * (1 - z ** 2) * (1 - z ** 3) * (1 - z ** 4)).evalf(50)) - complex(r)) < 1e-40
    return r


def P007():
    v = cos(pi / 9) * cos(2 * pi / 9) * cos(4 * pi / 9)
    assert abs(float(v.evalf(50)) - 1 / 8) < 1e-30
    return nsimplify(v.evalf(50), rational=True)


def P008():
    sols = [s_ for s_ in solve([a ** 2 - b ** 2 + 5, 2 * a * b - 12], [a, b]) if s_[0] > 0]
    assert len(sols) == 1 and expand((sols[0][0] + sols[0][1] * I) ** 2) == -5 + 12 * I
    return sols[0][0] + sols[0][1]


def P009():
    vals = set()
    for t0 in (pi * 0, pi):  # x di kuadran I dan III
        xv = t0 + atan(Rational(1, 3))
        assert simplify(tan(xv) - Rational(1, 3)) == 0
        vals.add(nsimplify((sin(2 * xv) + cos(2 * xv)).evalf(50), rational=True))
    assert len(vals) == 1
    return vals.pop()


def P010():
    v = cos(2 * pi / 7) + cos(4 * pi / 7) + cos(6 * pi / 7)
    assert abs(float(v.evalf(50)) + 0.5) < 1e-30
    return nsimplify(v.evalf(50), rational=True)


def P011():
    return sum((-1) ** (k // 2) * comb(20, k) for k in range(0, 21, 2))


def P012():
    return sum(1 for r in range(10) for c in combinations(range(1, 10), r) if sum(c) % 3 == 0)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"AL06-{name}"
        got = str(fn()).replace(" ", "")
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if got == key else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
