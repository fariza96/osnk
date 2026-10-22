#!/usr/bin/env python3
"""Membuat diagram GE01 di content/diagrams/. Koordinat dihitung dari data soal (berskala)."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import Fig

OUT = Path(__file__).resolve().parents[2] / "content/diagrams"
r = math.radians


def E01():
    f = Fig(width=260)
    A = f.point("A", (0, 0), dx=-12)
    B = f.point("B", (10 * math.cos(r(-18)), 10 * math.sin(r(-18))), dx=10, dy=8)
    C = f.point("C", (10 * math.cos(r(18)), 10 * math.sin(r(18))), dx=10, dy=-8)
    # D pada AC dengan AD = BC (segitiga emas): AD/AC = 1/phi
    phi = (1 + 5 ** 0.5) / 2
    D = f.point("D", (C[0] / phi, C[1] / phi), dx=-4, dy=-13)
    f.seg(A, B); f.seg(B, C); f.seg(C, A); f.seg(B, D)
    f.angle(B, A, C, r=1.6, label="36°", lr=2.5)
    f.ticks(A, B, 1); f.ticks(A, C, 1)
    return f.svg("Segitiga ABC sama kaki dengan AB = AC, sudut A 36 derajat, BD garis bagi sudut B dengan D pada AC")


def E02():
    f = Fig(width=260)
    C = f.point("C", (0, 0), dx=-12, dy=8)
    A = f.point("A", (0, 6), dx=-12)
    B = f.point("B", (8, 0), dx=10, dy=8)
    D = f.point("D", (3, 0), dy=14)
    f.seg(A, B); f.seg(B, C); f.seg(C, A); f.seg(A, D)
    f.right(A, C, B, s=0.6)
    return f.svg("Segitiga siku-siku di C dengan AC = 6 dan BC = 8; AD garis bagi sudut A dengan D pada BC")


def P001():
    f = Fig(width=300)
    A = f.point("A", (0, 1), dy=-13)
    P = f.point("P", (1 / math.tan(r(40)), 0), dx=12)
    B = f.point("B", (P[0] - 1 / math.tan(r(65)), -1), dy=14)
    A2 = f.point("A'", (2.6, 1), dy=-13)
    B2 = f.point("B'", (2.6, -1), dy=14)
    f.line((-0.6, 1), A2, ext=0.05, label="ℓ")
    f.line((-0.6, -1), B2, ext=0.05, label="m")
    f.seg(A, P); f.seg(P, B)
    f.angle(A2, A, P, r=0.35, label="40°", lr=0.62)
    f.angle(P, B, B2, r=0.3, label="65°", lr=0.58)
    f.angle(B, P, A, r=0.22)
    return f.svg("Garis l dan m sejajar; A dan A' pada l, B dan B' pada m; P di antara kedua garis; sudut A'AP 40 derajat dan sudut B'BP 65 derajat")


def P004():
    f = Fig(width=300)
    x = 32
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (1, 0), dx=10, dy=8)
    t = math.sin(r(52)) / math.sin(r(180 - x - 52))
    A = f.point("A", (t * math.cos(r(x)), t * math.sin(r(x))), dy=-13)
    CA = math.dist(A, C)
    D = f.point("D", (1 - CA, 0), dy=14)
    f.seg(A, B); f.seg(B, C); f.seg(C, A); f.seg(A, D)
    f.ticks(D, A, 1); f.ticks(D, B, 1)
    f.ticks(C, A, 2); f.ticks(C, D, 2)
    f.angle(A, C, B, r=0.12, label="52°", lr=0.22)
    return f.svg("Segitiga ABC dengan D pada BC, DA = DB, CA = CD, dan sudut ACB 52 derajat")


def P010():
    f = Fig(width=240)
    A = f.point("A", (0, 0), dx=-10, dy=8)
    B = f.point("B", (2, 0), dx=10, dy=8)
    C = f.point("C", (2, 2), dx=10, dy=-8)
    D = f.point("D", (0, 2), dx=-10, dy=-8)
    E = f.point("E", (1, 3 ** 0.5), dy=-13)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (A, E), (B, E), (D, E), (C, E)]:
        f.seg(p, q)
    return f.svg("Persegi ABCD dengan titik E di dalam persegi sehingga segitiga ABE sama sisi; ruas DE dan CE digambar")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["E01", "E02", "P001", "P004", "P010"]:
        (OUT / f"GE01-{name}.svg").write_text(globals()[name](), "utf-8")
        print("ditulis", f"GE01-{name}.svg")


if __name__ == "__main__":
    main()
