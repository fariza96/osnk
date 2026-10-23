#!/usr/bin/env python3
"""Pemeriksaan komputasional Latihan Campuran 1: pencarian lengkap, aritmetika eksak, koordinat (sympy)."""
import sys
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd, isqrt
from pathlib import Path

from sympy import Line, Point, Polygon, Rational, expand, rem, simplify, solve, symbols

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _pack import run

x, y = symbols("x y")


def p001(): return next(n for n in range(1, 1000) if isqrt(84 * n) ** 2 == 84 * n)
def p002(): return pow(3, 100, 13)
def p003(): return sum(1 for n in range(1, 101) if gcd(n, 12) == 1)
def p004():
    ok = {a * a - b * b for a in range(0, 60) for b in range(0, a + 1)}
    return sum(1 for n in range(1, 101) if n in ok)
def p005(): return next(n for n in range(1, 10 ** 4) if n % 3 == 0 and (n + 1) % 4 == 0 and (n + 2) % 5 == 0 and (n + 3) % 7 == 0)
def p006():
    vals = {simplify((s + 1 / s) ** 2) for s in solve(x - 1 / x - 3, x)}
    assert len(vals) == 1
    return vals.pop()
def p007(): return simplify(sum(r ** 3 for r in solve(x ** 2 - 5 * x + 2, x)))
def p008():
    r = rem(x ** 100 + 2 * x ** 51 - 3, x ** 2 - 1, x)
    return r.subs(x, 10)
def p009():
    a, b = symbols("a b")
    sols = solve([a + b + a * b - 11, a * a * b + a * b * b - 30], [a, b], dict=True)
    vals = {simplify(s[a] ** 2 + s[b] ** 2) for s in sols if s[a].is_real and s[b].is_real}
    return sum(vals)
def p010():
    def prime(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
    found = [n for n in range(1, 300) if prime(n ** 4 + 4)]
    # untuk n >= 2 faktorisasi Sophie Germain menunjukkan komposit; pencarian hanya mengonfirmasi rentang kecil
    assert all(expand((n * n + 2 * n + 2) * (n * n - 2 * n + 2)) == n ** 4 + 4 for n in range(1, 50))
    return len(found)
def p011(): return sum(1 for p in permutations("12345", 4) if int(p[3]) % 2 == 0)
def p012(): return sum(1 for w in set(permutations("BANANA")) if "AA" not in "".join(w))
def p013(): return sum(1 for c in combinations(range(1, 21), 3) if sum(c) % 2 == 0)
def p014(): return sum(1 for t in product(range(1, 11, 2), repeat=4) if sum(t) == 10)
def p015(): return sum(1 for c in combinations(range(12), 3) if all((a - b) % 12 not in (1, 11) for a, b in combinations(c, 2)))
def p016():
    from sympy import Triangle, acos, deg, pi, cos, sin
    out = set()
    for B_ang in (60, 35):  # sudut B bebas, A = 50
        A_ang, C_ang = 50, 130 - B_ang
        B, C = Point(0, 0), Point(1, 0)
        A = Line(B, Point(cos(pi * B_ang / 180), sin(pi * B_ang / 180))).intersection(
            Line(C, Point(1 - cos(pi * C_ang / 180), sin(pi * C_ang / 180))))[0]
        I = Triangle(A, B, C).incenter
        u, v = B - I, C - I
        out.add(int(round(float(deg(acos(u.dot(v) / (u.distance(Point(0, 0)) * v.distance(Point(0, 0)))))))))
    assert len(out) == 1
    return out.pop()
def p017():
    from sympy import Triangle
    B, C = Point(0, 0), Point(10, 0)
    xa = Rational(36 - 81 + 100, 20)
    from sympy import sqrt
    A = Point(xa, sqrt(36 - xa ** 2))
    D = Triangle(A, B, C).bisectors()[A].points[1]
    return simplify(B.distance(D))
def p018():
    out = set()
    for A, B, D in [(Point(0, 0), Point(8, 0), Point(2, 7.5)), (Point(0, 0), Point(6, 0), Point(-3, 10))]:
        A, B, D = Point(A), Point(B), Point(*[Rational(str(t)) for t in D.args])
        C = B + (D - A)
        k = Rational(60) / abs(Polygon(A, B, C, D).area)
        A, B, C, D = [P.scale(1, k) for P in (A, B, C, D)]
        assert abs(Polygon(A, B, C, D).area) == 60
        E = C.midpoint(D)
        Fp = Line(A, E).intersection(Line(B, D))[0]
        out.add(abs(Polygon(D, E, Fp).area))
    assert len(out) == 1
    return out.pop()
def p019():
    from sympy import Triangle
    from sympy import sqrt
    leg = sqrt(25 ** 2 - 7 ** 2)
    return Triangle(Point(0, 0), Point(7, 0), Point(0, leg)).inradius
def p020():
    out = set()
    for A, B, C in [(Point(1, 4), Point(0, 0), Point(9, 0)), (Point(-3, 8), Point(2, 0), Point(11, 3))]:
        k = 20 / A.distance(C)
        A, B, C = A * k, B * k, C * k
        D = B + (C - B) * Rational(2, 3)
        E = A.midpoint(D)
        Fp = Line(B, E).intersection(Line(A, C))[0]
        out.add(simplify(A.distance(Fp)))
    assert len(out) == 1
    return out.pop()


run("MX1", [(k, v) for k, v in globals().items() if k[:1] == "p" and k[1:].isdigit()])
