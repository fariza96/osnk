#!/usr/bin/env python3
"""Membuat diagram GE03 di content/diagrams/. Koordinat dihitung dari data soal (berskala)."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import Fig

OUT = Path(__file__).resolve().parents[2] / "content/diagrams"


def on(deg, r=1.0, c=(0.0, 0.0)):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


def lab(deg, k=14):
    return k * math.cos(math.radians(deg)), -k * math.sin(math.radians(deg))


def E01():
    f = Fig(width=240)
    f.circle((0, 0), 1)
    pts = {"A": -20, "B": 50, "C": 120, "D": 260}
    P = {n: f.point(n, on(a), dx=lab(a)[0], dy=lab(a)[1]) for n, a in pts.items()}
    for p, q in ["AB", "BC", "CD", "DA", "AC", "BD"]:
        f.seg(P[p], P[q])
    return f.svg("Segi empat ABCD pada lingkaran dengan diagonal AC dan BD")


def E02():
    f = Fig(width=300)
    O = f.point("O", (0, 0), dy=14)
    f.circle(O, 5)
    P = f.point("P", (13, 0), dx=10)
    T = f.point("T", (25 / 13, 60 / 13), dx=-4, dy=-13)
    A = f.point("A", (5, 0), dx=8, dy=12)
    B = f.point("B", (-5, 0), dx=-10, dy=12)
    f.seg(P, T); f.seg(P, B); f.seg(O, T, dash=True)
    f.right(O, T, P, s=0.7)
    return f.svg("Lingkaran berpusat O; dari titik P di luar lingkaran ditarik garis singgung PT dan garis potong melalui O yang memotong lingkaran di A (dekat P) dan B")


def P004():
    f = Fig(width=260)
    f.circle((0, 0), 1)
    A = f.point("A", on(90), dy=-13)
    B = f.point("B", on(214), dx=-10, dy=8)
    C = f.point("C", on(310), dx=10, dy=8)
    f.seg(A, B); f.seg(B, C); f.seg(C, A)
    Tp = f.point("X", (-1.5, 1), dx=-6, dy=-12, dot=False)
    f.seg((1.2, 1), Tp)
    f.angle(Tp, A, B, r=0.3)
    return f.svg("Segitiga ABC pada lingkaran; garis singgung di A; titik X pada garis singgung di sisi AB yang berlawanan dengan C; sudut XAB ditandai")


def P009():
    f = Fig(width=280)
    c1, c2 = (4, 5), (-4, 5)
    f.circle(c1, 5); f.circle(c2, 5)
    A = f.point("A", (0, 2), dx=12, dy=2)
    B = f.point("B", (0, 8), dx=12, dy=-2)
    M = f.point("M", (0, 0), dy=14)
    S = f.point("S", (4, 0), dy=14)
    T = f.point("T", (-4, 0), dy=14)
    f.seg((-6.5, 0), (6.5, 0))
    f.seg(M, B, dash=True)
    return f.svg("Dua lingkaran berpotongan di A dan B; garis singgung persekutuan menyinggung lingkaran di S dan T; perpanjangan BA memotong ST di M")


def P010():
    f = Fig(width=280)
    B = f.point("B", (0, 0), dx=-10, dy=8)
    C = f.point("C", (10, 0), dx=10, dy=8)
    tb, tc = math.tan(math.radians(70)), math.tan(math.radians(50))
    x = 10 * tc / (tb + tc)
    A = f.point("A", (x, x * tb), dy=-13)

    def foot(P, Q, X):
        dx, dy = Q[0] - P[0], Q[1] - P[1]
        k = ((X[0] - P[0]) * dx + (X[1] - P[1]) * dy) / (dx * dx + dy * dy)
        return (P[0] + k * dx, P[1] + k * dy)
    E = f.point("E", foot(A, C, B), dx=10, dy=-4)
    F = f.point("F", foot(A, B, C), dx=-11, dy=-2)
    for p, q in [(A, B), (B, C), (C, A), (B, E), (C, F), (E, F)]:
        f.seg(p, q)
    f.right(B, E, C, s=0.5); f.right(C, F, B, s=0.5)
    return f.svg("Segitiga ABC dengan garis tinggi BE (E pada AC) dan CF (F pada AB); ruas EF digambar")


def P012():
    f = Fig(width=240)
    f.circle((0, 1.75), 6.25)
    A = f.point("A", (0, 8), dy=-13)
    B = f.point("B", (-6, 0), dx=-11, dy=4)
    C = f.point("C", (6, 0), dx=11, dy=4)
    D = f.point("D", (0, -4.5), dy=14)
    f.point("O", (0, 1.75), dx=10, dy=-6)
    for p, q in [(A, B), (B, C), (C, A), (A, D), (B, D)]:
        f.seg(p, q)
    f.ticks(A, B, 1); f.ticks(A, C, 1)
    return f.svg("Segitiga ABC dengan AB = AC pada lingkaran berpusat O; AD diameter; ruas BD digambar")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["E01", "E02", "P004", "P009", "P010", "P012"]:
        (OUT / f"GE03-{name}.svg").write_text(globals()[name](), "utf-8")
        print("ditulis", f"GE03-{name}.svg")


if __name__ == "__main__":
    main()
