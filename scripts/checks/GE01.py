#!/usr/bin/env python3
"""Pemeriksaan komputasional GE01. Setiap konfigurasi dibangun ulang dengan koordinat eksak (sympy)
dari data di pernyataan soal; besaran yang ditanyakan dihitung lalu dibandingkan dengan kunci.
Soal pencacahan diperiksa dengan enumerasi. Gambar tidak dipakai sebagai bukti."""
import json
import sys
from pathlib import Path

from sympy import Point, Polygon, Segment, Line, Rational, acos, deg, nsimplify, rad, simplify, sqrt, cos, sin

BANK = Path(__file__).resolve().parents[2] / "content/questions/GE01.json"


def angle(P, Q, R):
    """Besar sudut PQR dalam derajat (eksak bila mungkin)."""
    u, v = P - Q, R - Q
    c = (u.dot(v)) / (sqrt(u.dot(u)) * sqrt(v.dot(v)))
    return nsimplify(simplify(deg(acos(simplify(c)))), tolerance=1e-12, rational=True)


def num_angle(P, Q, R):
    u, v = P - Q, R - Q
    c = float(u.dot(v)) / (float(sqrt(u.dot(u))) * float(sqrt(v.dot(v))))
    import math
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def bisector_foot(A, B, C):
    """Kaki garis bagi dari A pada BC (titik pembagi dalam BD:DC = AB:AC), dihitung tanpa teorema garis bagi:
    perpotongan BC dengan garis yang membentuk sudut sama terhadap AB dan AC (arah jumlah vektor satuan)."""
    u = (B - A) / A.distance(B)
    v = (C - A) / A.distance(C)
    return Line(A, A + u + v).intersection(Line(B, C))[0]


def E01():  # AB=AC, sudut A = 36, garis bagi sudut B memotong AC di D; sudut BDC
    A = Point(0, 0)
    B = Point(cos(rad(-18)) * 10, sin(rad(-18)) * 10)  # simetris terhadap sumbu x
    C = Point(cos(rad(18)) * 10, sin(rad(18)) * 10)
    D = bisector_foot(B, A, C)
    return round(num_angle(B, D, C), 9)


def E02():  # C siku-siku, AC=6, BC=8; garis bagi dari A memotong BC di D; AD^2
    C, A, B = Point(0, 0), Point(0, 6), Point(8, 0)
    D = bisector_foot(A, B, C)
    return simplify(A.distance(D) ** 2)


def P001():  # l: y=1, m: y=-1; sudut A'AP = 40, sudut B'BP = 65 (A', B' ke arah +x); sudut APB
    import math
    A = (0.0, 1.0)
    P = (1 / math.tan(math.radians(40)), 0.0)
    B = (P[0] - 1 / math.tan(math.radians(65)), -1.0)
    return round(num_angle(Point(*A), Point(*P), Point(*B)), 9)


def P002():
    return Polygon(Point(-5, 0), Point(5, 0), Point(0, 12)).area if Point(5, 0).distance(Point(0, 12)) == 13 else None


def P003():
    return sum(1 for x in range(1, 100) if 7 + 12 > x and 7 + x > 12 and 12 + x > 7)


def P004():  # DA=DB, CA=CD, sudut C = 52; sudut BAC (sudut B dicari numerik dari syarat)
    import math
    # sudut B = x memenuhi 180 - 4x = 52 menurut penalaran; di sini dibangun langsung:
    # B=(0,0), C=(c,0), A dengan sudut B = x dan sudut C = 52; cari x sehingga ada D di BC dengan DA=DB dan CA=CD.
    def defect(x):
        B = (0.0, 0.0)
        c = 1.0
        a_ang, c_ang = math.radians(x), math.radians(52)
        # A = perpotongan sinar dari B bersudut x dan sinar dari C bersudut 180-52
        t = c * math.sin(c_ang) / math.sin(math.pi - a_ang - c_ang)
        A = (t * math.cos(a_ang), t * math.sin(a_ang))
        CA = math.dist(A, (c, 0))
        D = (c - CA, 0.0)  # CD = CA dengan D pada BC
        return math.dist(D, A) - math.dist(D, B), A, D
    lo, hi = 1.0, 63.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if (defect(lo)[0] > 0) == (defect(mid)[0] > 0):
            lo = mid
        else:
            hi = mid
    x = (lo + hi) / 2
    _, A, D = defect(x)
    assert 0 < D[0] < 1, "D harus di antara B dan C"
    return round(num_angle(Point(0, 0), Point(*A), Point(1, 0)), 6)


def P005():  # AB=12, AC=9, BC=7; I pusat garis bagi, D kaki garis bagi dari A; AI/ID
    B, C = Point(0, 0), Point(7, 0)
    # A dengan AB=12, AC=9
    x = Rational(12**2 - 9**2 + 7**2, 2 * 7)
    A = Point(x, sqrt(12**2 - x**2))
    D = bisector_foot(A, B, C)
    E = bisector_foot(B, A, C)
    I = Line(A, D).intersection(Line(B, E))[0]
    return simplify(A.distance(I) / I.distance(D))


def P006():  # luas ABC = 90; median AD dan BE berpotongan di G; luas GDCE
    A, B, C = Point(0, 0), Point(15, 0), Point(4, 12)
    assert Polygon(A, B, C).area == 90
    D, E = Segment(B, C).midpoint, Segment(C, A).midpoint
    G = Line(A, D).intersection(Line(B, E))[0]
    return abs(Polygon(G, D, C, E).area)


def P007():  # siku-siku kaki 20, 21; jari-jari lingkaran dalam
    T = Polygon(Point(0, 0), Point(20, 0), Point(0, 21))
    return simplify(T.inradius)


def P008():
    B, C = Point(0, 0), Point(14, 0)
    x = Rational(13**2 - 15**2 + 14**2, 28)
    A = Point(x, sqrt(13**2 - x**2))
    assert A.distance(C) == 15
    return abs(Polygon(A, B, C).area)


def P009():  # banyak x bulat sehingga 8, 15, x segitiga tumpul
    def obtuse(s):
        a, b, c = sorted(s)
        return a + b > c and a * a + b * b < c * c
    return sum(1 for x in range(1, 100) if obtuse((8, 15, x)))


def P010():  # persegi ABCD, segitiga sama sisi ABE di dalam persegi; sudut DEC
    A, B, C, D = Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)
    E = Point(1, sqrt(3))
    return angle(D, E, C)


def P011():  # C siku-siku, CA=12, CB=9; I pusat lingkaran dalam; AI^2
    C, A, B = Point(0, 0), Point(12, 0), Point(0, 9)
    I = Polygon(A, B, C).incenter
    return simplify(A.distance(I) ** 2)


def P012():  # segitiga sisi bulat tak kongruen dengan keliling 24
    return sum(1 for a in range(1, 24) for b in range(a, 24) for c in [24 - a - b] if c >= b and a + b > c)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"GE01-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        ok = key != "—" and abs(float(got) - float(key)) < 1e-6
        bad += not ok
        print(f"{qid}: hitung={got} kunci={key} {'OK' if ok else 'BEDA'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
