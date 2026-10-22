#!/usr/bin/env python3
"""Membuat diagram GE02 di content/diagrams/. Koordinat dihitung dari data soal (berskala)."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import Fig

OUT = Path(__file__).resolve().parents[2] / "content/diagrams"


def meet(p, q, r, s):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p, q, r, s
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    a, b = x1 * y2 - y1 * x2, x3 * y4 - y3 * x4
    return ((a * (x3 - x4) - (x1 - x2) * b) / d, (a * (y3 - y4) - (y1 - y2) * b) / d)


def E01():
    f = Fig(width=280)
    A = f.point("A", (0, 0), dx=-10, dy=8)
    B = f.point("B", (6, 0), dx=10, dy=8)
    C = f.point("C", (5, 3), dx=10, dy=-8)
    D = f.point("D", (1, 3), dx=-10, dy=-8)
    O = f.point("O", meet(A, C, B, D), dy=14)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (A, C), (B, D)]:
        f.seg(p, q)
    return f.svg("Trapesium ABCD dengan AB sejajar DC; diagonal AC dan BD berpotongan di O")


def E02():
    f = Fig(width=300)
    A = f.point("A", (-4, 0), dx=-10, dy=8)
    B = f.point("B", (9, 0), dx=10, dy=8)
    D = f.point("D", (0, 0), dy=14)
    C = f.point("C", (0, 6), dy=-13)
    for p, q in [(A, B), (B, C), (C, A), (C, D)]:
        f.seg(p, q)
    f.right(C, D, B, s=0.5)
    f.right(A, C, B, s=0.5)
    f.text((-2, 0), "4", dy=12)
    f.text((4.5, 0), "9", dy=12)
    return f.svg("Segitiga ABC siku-siku di C; CD garis tinggi ke sisi miring AB dengan AD = 4 dan DB = 9")


def P004():
    f = Fig(width=300)
    A = f.point("A", (4, 6), dy=-13)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (12, 0), dx=10, dy=8)
    S = f.point("S", (8 / 3, 4), dx=-11, dy=-6)
    R = f.point("R", (20 / 3, 4), dx=11, dy=-6)
    P = f.point("P", (8 / 3, 0), dy=14)
    Q = f.point("Q", (20 / 3, 0), dy=14)
    for p, q in [(A, B), (B, C), (C, A), (P, S), (S, R), (R, Q)]:
        f.seg(p, q)
    f.seg(A, (4, 0), dash=True)
    f.right(Q, P, S, s=0.45)
    return f.svg("Segitiga ABC dengan alas BC; persegi PQRS dengan P dan Q pada BC, R pada AC, S pada AB; garis putus-putus adalah tinggi dari A")


def P006():
    f = Fig(width=280)
    A = f.point("A", (0, 0), dx=-10, dy=8)
    C = f.point("C", (9, 0), dx=10, dy=8)
    B = f.point("B", (3, 3 * math.sqrt(3)), dy=-13)
    D = f.point("D", (4, 0), dy=14)
    for p, q in [(A, B), (B, C), (C, A), (B, D)]:
        f.seg(p, q)
    f.angle(A, B, D, r=1.1)
    f.angle(B, C, A, r=1.3)
    return f.svg("Segitiga ABC dengan D pada sisi AC; sudut ABD (ditandai) sama dengan sudut ACB (ditandai)")


def P008():
    f = Fig(width=300)
    A = f.point("A", (0, 0), dx=-10, dy=8)
    B = f.point("B", (10, 0), dx=10, dy=8)
    C = f.point("C", (13, 6), dx=10, dy=-8)
    D = f.point("D", (-2, 6), dx=-10, dy=-8)
    O = f.point("O", meet(A, C, B, D), dy=-13)
    P = f.point("P", meet(A, D, O, (O[0] + 1, O[1])), dx=-11)
    Q = f.point("Q", meet(B, C, O, (O[0] + 1, O[1])), dx=11)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (A, C), (B, D)]:
        f.seg(p, q)
    f.seg(P, Q, dash=True)
    return f.svg("Trapesium ABCD dengan AB sejajar DC; diagonal berpotongan di O; ruas PQ melalui O sejajar AB dengan P pada AD dan Q pada BC")


def P010():
    f = Fig(width=280)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (10, 0), dx=10, dy=8)
    A = f.point("A", (3, 8), dy=-13)
    D = f.point("D", (5, 0), dy=14)
    E = f.point("E", (3 + 7 / 3, 8 - 8 / 3), dx=11, dy=-4)
    F = f.point("F", meet(A, D, B, E), dx=-12, dy=-2)
    for p, q in [(A, B), (B, C), (C, A), (A, D), (B, E)]:
        f.seg(p, q)
    f.ticks(B, D, 1); f.ticks(D, C, 1)
    return f.svg("Segitiga ABC; D titik tengah BC, E pada AC; ruas AD dan BE berpotongan di F")


def P011():
    f = Fig(width=240)
    A = f.point("A", (0, 0), dx=-10, dy=8)
    B = f.point("B", (10, 0), dx=10, dy=8)
    C = f.point("C", (10, 10), dx=10, dy=-8)
    D = f.point("D", (0, 10), dx=-10, dy=-8)
    E = f.point("E", (10, 5), dx=11)
    F = f.point("F", (5, 10), dy=-13)
    G = f.point("G", meet(A, E, B, F), dx=-4, dy=-13)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (A, E), (B, F)]:
        f.seg(p, q)
    f.ticks(B, E, 1); f.ticks(E, C, 1); f.ticks(C, F, 1); f.ticks(F, D, 1)
    return f.svg("Persegi ABCD; E titik tengah BC dan F titik tengah CD; ruas AE dan BF berpotongan di G")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["E01", "E02", "P004", "P006", "P008", "P010", "P011"]:
        (OUT / f"GE02-{name}.svg").write_text(globals()[name](), "utf-8")
        print("ditulis", f"GE02-{name}.svg")


if __name__ == "__main__":
    main()
