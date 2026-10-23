#!/usr/bin/env python3
"""Membuat diagram GE04 di content/diagrams/. Koordinat dihitung dari data soal (berskala)."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import Fig

OUT = Path(__file__).resolve().parents[2] / "content/diagrams"


def meet(P, Q, R, S):
    """Perpotongan garis PQ dan RS."""
    d = (Q[0] - P[0]) * (S[1] - R[1]) - (Q[1] - P[1]) * (S[0] - R[0])
    t = ((R[0] - P[0]) * (S[1] - R[1]) - (R[1] - P[1]) * (S[0] - R[0])) / d
    return (P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1]))


def div(P, Q, k):
    """Titik pada PQ dengan perbandingan jarak dari P sebesar k (0..1)."""
    return (P[0] + k * (Q[0] - P[0]), P[1] + k * (Q[1] - P[1]))


def E02():
    f = Fig(width=240)
    A = f.point("A", (0, 0), dx=-10, dy=10)
    B = f.point("B", (6, 0), dx=10, dy=10)
    C = f.point("C", (6, 6), dx=10, dy=-10)
    D = f.point("D", (0, 6), dx=-10, dy=-10)
    M = f.point("M", (6, 3), dx=12)
    N = f.point("N", (2, 6), dy=-13)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (A, M), (M, N), (N, A)]:
        f.seg(p, q)
    f.ticks(B, M, 1); f.ticks(M, C, 1)
    return f.svg("Persegi ABCD; M titik tengah BC; N pada CD; segitiga AMN digambar")


def P004():
    f = Fig(width=280)
    A = f.point("A", (1.5, 5), dy=-13)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (7, 0), dx=10, dy=8)
    D = f.point("D", div(B, C, 0.5), dy=14)
    E = f.point("E", div(A, C, 2 / 3), dx=11, dy=-4)
    P = f.point("P", meet(A, D, B, E), dx=-11, dy=-4)
    for p, q in [(A, B), (B, C), (C, A), (A, D), (B, E)]:
        f.seg(p, q)
    f.ticks(B, D, 1); f.ticks(D, C, 1)
    return f.svg("Segitiga ABC; D titik tengah BC; E pada AC; AD dan BE berpotongan di P")


def P007():
    f = Fig(width=240)
    x = 1.2  # PA = 3, PB = 4, PC = 5 dengan P = (x, y)
    y = math.sqrt(9 - x * x)
    w, h = x + math.sqrt(16 - y * y), y + math.sqrt(25 - (16 - y * y))
    A = f.point("A", (0, 0), dx=-10, dy=10)
    B = f.point("B", (w, 0), dx=10, dy=10)
    C = f.point("C", (w, h), dx=10, dy=-10)
    D = f.point("D", (0, h), dx=-10, dy=-10)
    P = f.point("P", (x, y), dx=12, dy=4)
    for p, q in [(A, B), (B, C), (C, D), (D, A), (P, A), (P, B), (P, C)]:
        f.seg(p, q)
    f.seg(P, D, dash=True)
    f.text(div(P, A, 0.5), "3", dx=-9, dy=2)
    f.text(div(P, B, 0.5), "4", dx=6, dy=12)
    f.text(div(P, C, 0.5), "5", dx=-8, dy=-6)
    return f.svg("Persegi panjang ABCD dengan titik P di dalamnya; PA = 3, PB = 4, PC = 5; PD putus-putus")


def P010():
    f = Fig(width=220)
    C = f.point("C", (0, 0), dx=-10, dy=10)
    A = f.point("A", (6, 0), dx=10, dy=10)
    B = f.point("B", (0, 8), dx=-10, dy=-6)
    I = f.point("I", (2, 2), dx=-10, dy=-4)
    O = f.point("O", (3, 4), dx=10, dy=-4)
    for p, q in [(A, B), (B, C), (C, A)]:
        f.seg(p, q)
    f.circle(I, 2, dash=True)
    f.seg(O, I)
    f.right(A, C, B, s=0.6)
    return f.svg("Segitiga ABC siku-siku di C; lingkaran dalam berpusat I; O titik tengah AB; ruas OI digambar")


def P011():
    f = Fig(width=260)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (7, 0), dx=10, dy=8)
    A = f.point("A", (1.5, math.sqrt(33.75)), dy=-13)
    D = f.point("D", (3, 0), dy=14)
    for p, q in [(A, B), (B, C), (C, A), (A, D)]:
        f.seg(p, q)
    f.angle(B, A, D, r=0.9)
    f.angle(D, A, C, r=1.1)
    return f.svg("Segitiga ABC; AD garis bagi sudut A dengan D pada BC; dua sudut sama di A ditandai")


def P012():
    f = Fig(width=280)
    A = f.point("A", (3, 8), dy=-13)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (10, 0), dx=10, dy=8)
    D = f.point("D", div(B, C, 1 / 4), dy=14)
    E = f.point("E", div(C, A, 0.5), dx=11, dy=-4)
    P = f.point("P", meet(A, D, B, E), dx=10, dy=-10)
    F = f.point("F", meet(C, P, A, B), dx=-11, dy=-2)
    for p, q in [(A, B), (B, C), (C, A), (A, D), (B, E), (C, F)]:
        f.seg(p, q)
    f.ticks(C, E, 1); f.ticks(E, A, 1)
    return f.svg("Segitiga ABC; D pada BC, E titik tengah CA, F pada AB; AD, BE, CF berpotongan di P")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["E02", "P004", "P007", "P010", "P011", "P012"]:
        (OUT / f"GE04-{name}.svg").write_text(globals()[name](), "utf-8")
        print("ditulis", f"GE04-{name}.svg")


if __name__ == "__main__":
    main()
