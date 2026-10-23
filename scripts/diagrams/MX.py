#!/usr/bin/env python3
"""Membuat diagram paket Latihan Campuran (MX1, MX2) di content/diagrams/. Koordinat dihitung dari data soal."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import Fig

OUT = Path(__file__).resolve().parents[2] / "content/diagrams"


def meet(P, Q, R, S):
    d = (Q[0] - P[0]) * (S[1] - R[1]) - (Q[1] - P[1]) * (S[0] - R[0])
    t = ((R[0] - P[0]) * (S[1] - R[1]) - (R[1] - P[1]) * (S[0] - R[0])) / d
    return (P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1]))


def div(P, Q, k):
    return (P[0] + k * (Q[0] - P[0]), P[1] + k * (Q[1] - P[1]))


def MX1_018():
    f = Fig(width=280)
    A = f.point("A", (0, 0), dx=-10, dy=10)
    B = f.point("B", (8, 0), dx=10, dy=10)
    C = f.point("C", (10, 5), dx=10, dy=-8)
    D = f.point("D", (2, 5), dx=-10, dy=-8)
    E = f.point("E", div(C, D, 0.5), dy=-13)
    F = f.point("F", meet(A, E, B, D), dx=12, dy=2)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (A, E), (B, D)]:
        f.seg(p, q)
    f.ticks(D, E, 1); f.ticks(E, C, 1)
    return f.svg("Jajargenjang ABCD; E titik tengah CD; AE dan BD berpotongan di F")


def MX1_020():
    f = Fig(width=260)
    A = f.point("A", (2.5, 7), dy=-13)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (9, 0), dx=10, dy=8)
    D = f.point("D", div(B, C, 2 / 3), dy=14)
    E = f.point("E", div(A, D, 0.5), dx=-12, dy=-2)
    F = f.point("F", meet(B, E, A, C), dx=11, dy=-4)
    for p, q in [(A, B), (B, C), (C, A), (A, D), (B, F)]:
        f.seg(p, q)
    f.ticks(A, E, 1); f.ticks(E, D, 1)
    return f.svg("Segitiga ABC; D pada BC; E titik tengah AD; BE memotong AC di F")


def MX2_017():
    f = Fig(width=240)
    O = (2, -0.5)
    r = math.sqrt(65 / 4)
    f.circle(O, r)
    A = f.point("A", (-2, 0), dx=-11, dy=-6)
    B = f.point("B", (6, 0), dx=11, dy=-6)
    C = f.point("C", (0, 3), dx=-6, dy=-12)
    D = f.point("D", (0, -4), dx=-6, dy=14)
    P = f.point("P", (0, 0), dx=-10, dy=12)
    f.seg(A, B); f.seg(C, D)
    f.right(B, P, C, s=0.5)
    return f.svg("Lingkaran dengan tali busur AB dan CD yang berpotongan tegak lurus di P")


def MX2_020():
    f = Fig(width=240)
    A = f.point("A", (0, 0), dx=-10, dy=10)
    B = f.point("B", (10, 0), dx=10, dy=10)
    C = f.point("C", (10, 10), dx=10, dy=-10)
    D = f.point("D", (0, 10), dx=-10, dy=-10)
    k = 15 / 4
    f.circle((5, k), 10 - k)
    f.point("O", (5, k), dx=10, dy=-4)
    for p, q in [(A, B), (B, C), (C, D), (D, A)]:
        f.seg(p, q)
    return f.svg("Persegi ABCD; lingkaran berpusat O melalui A dan B serta menyinggung sisi CD")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["MX1_018", "MX1_020", "MX2_017", "MX2_020"]:
        fn = name.replace("_", "-") + ".svg"
        (OUT / fn).write_text(globals()[name](), "utf-8")
        print("ditulis", fn)


if __name__ == "__main__":
    main()
