#!/usr/bin/env python3
"""Pemeriksaan komputasional Latihan Campuran 2: pencarian lengkap (termasuk semua urutan langkah pada MX2-015),
aritmetika eksak, koordinat (sympy)."""
import sys
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial, isqrt
from pathlib import Path

from sympy import Abs, I, Line, Point, Polygon, Rational, Triangle, nsimplify, simplify, solve, sqrt, symbols

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _pack import run

x = symbols("x")


def p001():
    n, k = factorial(50), 0
    while n % 3 == 0:
        n //= 3; k += 1
    return k
def p002(): return sum(1 for n in range(1, 10 ** 4) if (n * n + 20) % (n + 2) == 0)
def p003(): return sum(1 for d in range(1, 721) if 720 % d == 0 and d % 6 == 0)
def p004(): return sum(k // 3 for k in range(1, 21))
def p005(): return next(n for n in range(1, 1000) if (2 ** n - 1) % 77 == 0)
def p006(): return min(F(t, 1000) + 16 / F(t, 1000) for t in range(1, 20001))  # x = 4 termasuk grid
def p007(): return sum(F(1, k * (k + 1) * (k + 2)) for k in range(1, 9))
def p008():
    f = lambda t: t - 1
    assert simplify(f(x) - 3 * f(-x) - 4 * x - 2) == 0
    # keunikan: sistem linear dalam f(x), f(-x) dengan determinan 1 - 9 != 0
    return f(2026)
def p009():
    a, b = symbols("a b", real=True)
    sols = solve([a + sqrt(a ** 2 + b ** 2) - 1, b - 7], [a, b], dict=True)
    assert len(sols) == 1
    z = sols[0][a] + sols[0][b] * I
    assert simplify(z + Abs(z) - (1 + 7 * I)) == 0
    return simplify(Abs(z))
def p010():
    best = min(1 / F(p, 60) + 4 / F(q, 60) + 9 / F(180 - p - q, 60) for p in range(1, 179) for q in range(1, 180 - p))
    assert 1 / F(1, 2) + 4 / F(1) + 9 / F(3, 2) == 12
    return best  # grid kelipatan 1/60 memuat titik kesamaan (1/2, 1, 3/2)
def p011(): return next(N for N in range(1, 100) if -(-N // 7) >= 4)  # terkecil N dengan ceil(N/7) >= 4
def p012():
    S = list(combinations(range(1, 10), 3))
    return F(sum(1 for c in S if sum(c) % 3 == 0), len(S))
def p013():
    @lru_cache(None)
    def t(n): return 1 if n == 0 else sum(t(n - s) for s in (1, 2, 3) if s <= n)
    return t(8)
def p014(): return sum(1 for p in permutations(range(1, 6)) if p[0] != 1 and p[1] != 2)
def p015():
    @lru_cache(None)
    def finals(ms):
        if len(ms) == 1:
            return frozenset(ms)
        out = set()
        for i, j in combinations(range(len(ms)), 2):
            rest = list(ms[:i] + ms[i + 1:j] + ms[j + 1:]) + [abs(ms[i] - ms[j])]
            out |= finals(tuple(sorted(rest)))
        return frozenset(out)
    vals = finals(tuple(range(1, 11)))
    assert vals == {1, 3, 5, 7, 9}
    return len(vals)
def p016():
    # segi empat tali busur: A + C = 180; dicek pada konfigurasi nyata dengan sudut BCD = 60
    from sympy import cos, sin, pi, acos, deg
    pt = lambda d: Point(cos(pi * d / 180), sin(pi * d / 180))
    A, B, C, D = pt(300), pt(0), pt(100), pt(240)  # berurutan; busur BAD = 120 -> sudut BCD = 60
    ang = lambda P, Q, R: deg(acos(((P - Q).dot(R - Q)) / ((P - Q).distance(Point(0, 0)) * (R - Q).distance(Point(0, 0)))))
    c, a = nsimplify(float(ang(B, C, D)), rational=True), nsimplify(float(ang(B, A, D)), rational=True)
    assert a == 2 * c
    return c
def p017():
    P = Point(0, 0); A, B, C = Point(-2, 0), Point(6, 0), Point(0, 3)
    D = Point(0, -Rational(2 * 6, 3))
    O = Triangle(A, B, C).circumcenter
    assert O.distance(D) == O.distance(A)  # D juga pada lingkaran
    return simplify(O.distance(A) ** 2)
def p018(): return abs(Polygon(Point(1, 1), Point(7, 3), Point(3, 9)).area)
def p019():
    B, C = Point(0, 0), Point(17, 0)
    xa = Rational(9 ** 2 - 10 ** 2 + 17 ** 2, 34)
    A = Point(xa, sqrt(81 - xa ** 2))
    assert simplify(A.distance(C)) == 10
    return simplify(Triangle(A, B, C).circumradius)
def p020():
    k = symbols("k")
    sol = [s for s in solve(25 + k ** 2 - (10 - k) ** 2, k) if 0 <= s <= 10]
    assert len(sol) == 1
    return 10 - sol[0]


run("MX2", [(k, v) for k, v in globals().items() if k[:1] == "p" and k[1:].isdigit()])
