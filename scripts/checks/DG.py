#!/usr/bin/env python3
"""Pemeriksaan komputasional diagnostik DG: pencacahan langsung, aritmetika eksak, koordinat (sympy)."""
import sys
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd, isqrt
from pathlib import Path

from sympy import Point, Rational, nsimplify, simplify, solve, sqrt, symbols

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _pack import run


def p001(): return sum(1 for n in range(1, 101) if n % 6 == 0 and n % 4)
def p002(): return gcd(84, 126) + 84 * 126 // gcd(84, 126)
def p003(): return pow(2, 100, 7)
def p004(): return sum(1 for d in range(1, 361) if 360 % d == 0)
def p005():
    a, b = symbols("a b", real=True)
    vals = {simplify(s[a] ** 2 + s[b] ** 2) for s in solve([a - b - 3, a * b - 10], [a, b], dict=True)}
    assert len(vals) == 1
    return vals.pop()
def p006():
    x = symbols("x")
    return sum(r ** 2 for r in solve(2 * x ** 2 - 7 * x + 3, x))
def p007(): return simplify(1 / (sqrt(5) - 2) - sqrt(5))
def p008(): return min(F(x, 100) ** 2 - 6 * F(x, 100) + 14 for x in range(-1000, 1001))  # minimum di x = 3 termasuk grid
def p009(): return sum(1 for n in range(100, 1000) if len(set(str(n))) == 3)
def p010(): return sum(1 for c in combinations(range(8), 3) if any(i >= 4 for i in c))  # 0-3 putra, 4-7 putri
def p011(): return sum(1 for p in permutations(range(5)) if abs(p.index(0) - p.index(1)) == 1)
def p012(): return F(sum(1 for a, b in product(range(1, 7), repeat=2) if a + b == 10), 36)
def p013():
    C, A, B = Point(0, 0), Point(9, 0), Point(0, 12)
    from sympy import Line
    return nsimplify(C.distance(Line(A, B)))
def p014():
    from sympy import Line, acos, deg, cos, sin, pi
    # AB = AC = 1, sudut A = 40 derajat; D pada perpanjangan CB melewati B
    A = Point(0, 0); B = Point(cos(pi * 20 / 180), -sin(pi * 20 / 180)); C = Point(cos(pi * 20 / 180), sin(pi * 20 / 180))
    D = B + (B - C)
    u, v = A - B, D - B
    return int(round(float(deg(acos(u.dot(v) / (u.distance(Point(0, 0)) * v.distance(Point(0, 0))))))))
def p015():  # A(0,0), B(10,0), BC = 15 dengan dua arah berbeda; D, E membagi AB, AC dengan AD:DB = 4:6
    out = set()
    for C in (Point(10 + 9, 12), Point(10 - 12, 9)):
        B = Point(10, 0)
        assert B.distance(C) == 15
        D, E = B * Rational(4, 10), C * Rational(4, 10)  # DE sejajar BC
        out.add(simplify(D.distance(E)))
    assert len(out) == 1
    return out.pop()


def p016():
    # C pada lingkaran berdiameter AB dengan AC = 5, BC = 12: cek sudut siku dan jari-jari dari pusat lingkaran luar
    from sympy import Triangle
    A, B, C = Point(0, 0), Point(13, 0), None
    x = Rational(25, 13); C = Point(x, sqrt(25 - x ** 2))
    assert simplify(B.distance(C)) == 12
    return nsimplify(Triangle(A, B, C).circumradius)


run("DG", [(k, v) for k, v in globals().items() if k[:1] == "p" and k[1:].isdigit()])
