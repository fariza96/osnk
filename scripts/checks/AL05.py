#!/usr/bin/env python3
"""Pemeriksaan komputasional AL05. Persamaan fungsi: nilai yang ditanya dihitung dari sistem persamaan hasil
substitusi (sympy), dan calon fungsi diverifikasi secara simbolik ke persamaan semula (syarat cukup). Pencacahan fungsi
pada {1,2,3,4} dengan pencarian lengkap atas 4^4 fungsi. Iterasi dengan pecahan eksak."""
import json
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

from sympy import Rational, simplify, solve, symbols

BANK = Path(__file__).resolve().parents[2] / "content/questions/AL05.json"
x, y, a, b, c = symbols("x y a b c")


def E01():
    s = solve([a + 2 * b - 6, b + 2 * a - Rational(3, 2)], [a, b])
    f = lambda t: 2 / t - t
    assert simplify(f(x) + 2 * f(1 / x) - 3 * x) == 0 and f(Rational(2)) == s[a]
    return s[a]


def E02():
    f = lambda t: t ** 2 + 3 * t
    assert simplify(f(x + y) - f(x) - f(y) - 2 * x * y) == 0 and f(1) == 4
    return f(Rational(1, 2))


def P001():
    f, g = (lambda t: 2 * t + 3), (lambda t: t * t - 1)
    return f(g(3)) - g(f(1))


def P002():
    sols = [s for s in solve((3 * x + 2) / (x - 1) - 5, x) if s != 1]
    assert len(sols) == 1
    return sols[0]


def P003():
    s = solve(2 * x - 1 - 5, x)[0]
    return 4 * s ** 2 - 2 * s + 1


def vp(q, p):
    q, k = Fraction(q), 0
    while q.numerator % p == 0:
        q, k = q / p, k + 1
    while q.denominator % p == 0:
        q, k = q * p, k - 1
    return k


def P004():  # f(x) = 3 v2(x) + 5 v3(x) memenuhi f(xy) = f(x) + f(y) pada Q+
    f = lambda q: 3 * vp(q, 2) + 5 * vp(q, 3)
    qs = [Fraction(n, d) for n in range(1, 13) for d in range(1, 13)]
    assert all(f(p * q) == f(p) + f(q) for p in qs for q in qs) and f(2) == 3 and f(3) == 5
    return f(72) + f(Fraction(1, 6))


FUNCS = list(product(range(4), repeat=4))


def P005():
    return sum(1 for f in FUNCS if all(f[f[i]] == i for i in range(4)))


def P006():
    v = Fraction(3)
    for _ in range(2026):
        v = 1 / (1 - v)
    return v


def P007():
    f = lambda t: t + 1
    assert simplify(f(x) * f(y) - f(x * y) - x - y) == 0
    # kasus f(0) = 0 ditolak di pembahasan: y = 0 memberi 0 = x untuk semua x
    return f(2026)


def P008():
    f1 = Rational(4) / 2 * 3  # f(1/3) = 4/2, f(1) = 3 f(1/3)
    f = lambda t: f1 * t
    assert f(Rational(2, 3)) == 4 and simplify(f(x + y) - f(x) - f(y)) == 0
    return f(Rational(5, 2))


def P009():
    sols = solve([a ** 2 - 4, (a + 1) * b - 9], [a, b], dict=True)
    for s in sols:
        f = lambda t: s[a] * t + s[b]
        assert simplify(f(f(x)) - 4 * x - 9) == 0
    return sum(s[a] + s[b] for s in sols)


def P010():  # bangun f dari f(0) = -1 dan f(x+1) = f(x) + x + 2 pada [-60, 60]
    N = 60
    f = {0: -1}
    for n in range(0, N):
        f[n + 1] = f[n] + n + 2
    for n in range(0, -N, -1):
        f[n - 1] = f[n] - (n - 1) - 2
    assert f[1] == 1
    assert all(f[p + q] == f[p] + f[q] + p * q + 1 for p in range(-25, 26) for q in range(-25, 26))
    fixed = [n for n in f if f[n] == n]
    assert all(abs(n) < 10 for n in fixed)  # f(n) - n tumbuh kuadratik, jadi tidak ada titik tetap di luar rentang
    return sum(fixed)


def P011():
    s = solve([a + b - 3, b + c - Rational(3, 2), c + a], [a, b, c])
    f = lambda t: (t ** 3 - t ** 2 - 1) / (2 * t * (t - 1))
    assert simplify(f(x) + f((x - 1) / x) - 1 - x) == 0 and f(Rational(2)) == s[a]
    return s[a]


def P012():
    return sum(1 for f in FUNCS if all(f[f[i]] == f[i] for i in range(4)))


def fmt(v):
    v = Fraction(str(v)) if not isinstance(v, Fraction) else v
    return f"{v.numerator}/{v.denominator}" if v.denominator != 1 else str(v.numerator)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"AL05-{name}"
        got = fmt(fn())
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if got == key else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
