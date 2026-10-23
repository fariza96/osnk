#!/usr/bin/env python3
"""Pemeriksaan komputasional AL03. Untuk soal nilai ekstrem diperiksa dua arah:
(1) nilai kunci tercapai secara eksak (sympy) di titik kesamaan yang disebut pembahasan, dan
(2) pencarian numerik acak (seed tetap) pada daerah yang sah tidak menemukan nilai yang lebih baik.
Arah (2) hanya bukti numerik, bukan pembuktian. Soal pencacahan diperiksa dengan enumerasi."""
import json
import random
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

BANK = Path(__file__).resolve().parents[2] / "content/questions/AL03.json"
x, y, z, k = sp.symbols("x y z k", real=True)
R = random.Random(2026)
N = 200_000


def exact(expr, sub):
    return sp.nsimplify(sp.simplify(expr.subs(sub)))


def no_better(f, sampler, best, sense="min", tol=1e-9):
    for _ in range(N):
        v = f(*sampler())
        if (sense == "min" and v < best - tol) or (sense == "max" and v > best + tol):
            raise AssertionError(f"nilai lebih baik ditemukan: {v} vs {best}")


def pos(a=1e-3, b=20):
    return a + (b - a) * R.random() ** 2


def E01():
    f = x**2 + 16 / x
    v = exact(f, {x: 2})
    no_better(lambda t: t * t + 16 / t, lambda: (pos(),), float(v))
    return v


def E02():  # a+b+c=6, min 1/a+4/b+9/c
    a, b = sp.symbols("a b", positive=True)
    v = exact(1 / a + 4 / b + 9 / (6 - a - b), {a: 1, b: 2})

    def samp():
        while True:
            p, q = R.random() * 6, R.random() * 6
            if p + q < 6 - 1e-6:
                return p, q
    no_better(lambda p, q: 1 / p + 4 / q + 9 / (6 - p - q), samp, float(v))
    return v


def P001():
    return sp.minimum(x**2 - 6 * x + 14, x)


def P002():
    v = exact(3 * x + 27 / x, {x: 3})
    no_better(lambda t: 3 * t + 27 / t, lambda: (pos(),), float(v))
    return v


def P003():
    return sum(1 for t in range(-100, 101) if abs(2 * t + 1) <= 13)


def P004():
    f = x**2 + 2 * y**2 + 2 * x * y - 4 * x - 2 * y + 12
    crit = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    assert crit == [{x: 3, y: -1}], crit
    v = exact(f, crit[0])
    no_better(lambda p, q: p * p + 2 * q * q + 2 * p * q - 4 * p - 2 * q + 12,
              lambda: (R.uniform(-50, 50), R.uniform(-50, 50)), float(v))
    return v


def P005():  # xy=32, min 2x+y
    v = exact(2 * x + 32 / x, {x: 4})
    no_better(lambda t: 2 * t + 32 / t, lambda: (pos(1e-3, 100),), float(v))
    return v


def P006():
    pts = [Fraction(n, 4) for n in range(-200, 200)]
    return min(abs(t - 1) + abs(t - 4) + abs(t - 6) + abs(t - 10) for t in pts)


def P007():  # akar real x^2-2kx+k+6; min a^2+b^2 = 4k^2-2k-12 pada k<=-2 atau k>=3
    def val(kk):
        r = sp.Poly(x**2 - 2 * kk * x + kk + 6, x).all_roots()
        assert all(rt.is_real for rt in r)
        return sp.nsimplify(sum(rt**2 for rt in r))
    v = val(-2)
    assert v == 4 * 4 + 4 - 12
    for _ in range(20_000):
        kk = R.choice([R.uniform(-60, -2), R.uniform(3, 60)])
        assert 4 * kk * kk - 2 * kk - 12 >= float(v) - 1e-9
    return v


def P008():  # x+2y+2z=9, min x^2+y^2+z^2
    v = exact(x**2 + y**2 + z**2, {x: 1, y: 2, z: 2})
    no_better(lambda p, q: (9 - 2 * p - 2 * q) ** 2 + p * p + q * q,
              lambda: (R.uniform(-20, 20), R.uniform(-20, 20)), float(v))
    return v


def P009():
    return sum(1 for t in range(-100, 101) if abs(abs(t - 2) - 3) <= 2)


def P010():  # a+b+c=1, max a b^2 c^3
    a, b = sp.symbols("a b", positive=True)
    v = exact(a * b**2 * (1 - a - b) ** 3, {a: sp.Rational(1, 6), b: sp.Rational(1, 3)})

    def samp():
        while True:
            p, q = R.random(), R.random()
            if p + q < 1:
                return p, q
    no_better(lambda p, q: p * q * q * (1 - p - q) ** 3, samp, float(v), sense="max", tol=1e-15)
    return v


def P011():  # a+b+c=3, min sum a^2/(b+c)
    v = exact(sp.Integer(3) * 1 / 2, {})

    def f(p, q):
        r = 3 - p - q
        return p * p / (q + r) + q * q / (r + p) + r * r / (p + q)

    def samp():
        while True:
            p, q = R.random() * 3, R.random() * 3
            if p + q < 3 - 1e-6:
                return p, q
    assert abs(f(1, 1) - 1.5) < 1e-12
    no_better(f, samp, float(v))
    return v


def P012():  # xyz=1, min (x+3y)(y+3z)(xz+1)
    v = exact((x + 3 * y) * (y + 3 * z) * (x * z + 1), {x: 3, y: 1, z: sp.Rational(1, 3)})

    def f(p, q):
        r = 1 / (p * q)
        return (p + 3 * q) * (q + 3 * r) * (p * r + 1)
    no_better(f, lambda: (pos(1e-2, 30), pos(1e-2, 30)), float(v))
    return v


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k_, v) for k_, v in globals().items() if k_[:1] in "EP" and k_[1:].isdigit()]:
        qid = f"AL03-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
