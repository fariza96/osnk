#!/usr/bin/env python3
"""Pemeriksaan komputasional GE04. Setiap konfigurasi dibangun ulang dengan koordinat eksak (sympy) dari data soal;
data yang diberikan dicek berlaku, lalu besaran yang ditanyakan dihitung tanpa memakai rumus di pembahasan
(Heron, Ceva, Menelaus, aturan sinus/kosinus). Bila jawaban tidak bergantung pada bagian konfigurasi yang bebas,
dicek pada dua bentuk berbeda. Gambar tidak dipakai sebagai bukti."""
import json
import sys
from pathlib import Path

from sympy import Line, Point, Polygon, Rational, Segment, Triangle, cos, pi, simplify, sin, solve, sqrt, symbols

BANK = Path(__file__).resolve().parents[2] / "content/questions/GE04.json"


def tri_sides(a, b, c):
    """Segitiga dengan BC = a, CA = b, AB = c: B(0,0), C(a,0), A di atas."""
    x = Rational(c * c - b * b + a * a, 2 * a)
    return Point(x, sqrt(c * c - x * x)), Point(0, 0), Point(a, 0)


def area(*P):
    return abs(Polygon(*P).area)


def E01():
    A, B, C = tri_sides(14, 15, 13)
    return simplify(Triangle(A, B, C).inradius)


def E02():
    A, M, N = Point(0, 0), Point(6, 3), Point(2, 6)
    assert M == Point(6, 0).midpoint(Point(6, 6)) and N.distance(Point(0, 6)) == 2
    return area(A, M, N)


def P001():
    pts = [Point(0, 0), Point(6, 1), Point(5, 5), Point(1, 4)]
    assert Polygon(*pts).is_convex()
    assert area(pts[0], pts[2], pts[1], pts[3]) == 1  # urutan menyilang pada kekeliruan umum
    return area(*pts)


def P002():
    A, B = Point(0, 0), Point(3, 0)
    C = Point(5 * cos(2 * pi / 3), 5 * sin(2 * pi / 3))
    return simplify(B.distance(C))


def P003():
    return simplify(Triangle(*tri_sides(20, 15, 7)).area)


def P004():  # D titik tengah BC, AE:EC = 2:1; AP/PD pada dua segitiga berbeda
    out = set()
    for A, B, C in [(Point(0, 3), Point(0, 0), Point(2, 0)), (Point(3, 7), Point(-1, 0), Point(9, 1))]:
        D = B.midpoint(C)
        E = A + (C - A) * Rational(2, 3)
        P = Line(A, D).intersection(Line(B, E))[0]
        out.add(simplify(A.distance(P) / P.distance(D)))
    assert len(out) == 1
    return out.pop()


def P005():
    x, y = symbols("x y", real=True)
    O, r2 = Point(2, 1), 25
    assert simplify((x - 2) ** 2 + (y - 1) ** 2 - r2 - (x * x + y * y - 4 * x - 2 * y - 20)) == 0
    P = Point(14, 6)
    # titik singgung T: OT tegak lurus PT dan T pada lingkaran
    sols = solve([(x - 2) ** 2 + (y - 1) ** 2 - r2, (x - 2) * (x - 14) + (y - 1) * (y - 6)], [x, y], dict=True)
    lens = {simplify(P.distance(Point(s[x], s[y]))) for s in sols}
    assert len(sols) == 2 and len(lens) == 1
    return lens.pop()


def P006():
    A, B, C = tri_sides(8, 9, 7)
    return simplify(A.distance(B.midpoint(C)))


def P007():  # persegi panjang nyata dengan PA=3, PB=4, PC=5 untuk dua pilihan x
    out = set()
    for x in (Rational(6, 5), Rational(2)):
        y = sqrt(9 - x * x)
        p = x + sqrt(16 - y * y)
        q = y + sqrt(25 - (p - x) ** 2)
        A, B, C, D, P = Point(0, 0), Point(p, 0), Point(p, q), Point(0, q), Point(x, y)
        assert 0 < x < p and 0 < y < q
        assert [simplify(P.distance(T)) for T in (A, B, C)] == [3, 4, 5]
        out.add(simplify(P.distance(D) ** 2))
    assert len(out) == 1
    return out.pop()


def P008():
    A, B, C = tri_sides(21, 17, 10)
    return min(simplify(V.distance(Line(*[W for W in (A, B, C) if W != V]))) for V in (A, B, C))


def P009():
    A, B = Point(0, 0), Point(15, 0)
    C = Point(8 * cos(pi / 3), 8 * sin(pi / 3))
    return simplify(Triangle(A, B, C).circumradius ** 2)


def P010():
    C, A, B = Point(0, 0), Point(6, 0), Point(0, 8)
    T = Triangle(A, B, C)
    return simplify(T.incenter.distance(T.circumcenter) ** 2)


def P011():
    A, B, C = tri_sides(7, 8, 6)
    D = Triangle(A, B, C).bisectors()[A].points[1]
    assert simplify(D.y) == 0  # D pada BC
    return simplify(A.distance(D))


def P012():  # [ABC] = 80, BD:DC = 1:3, E titik tengah CA, AD, BE, CF konkuren di P; luas AFP, dua bentuk segitiga
    out = set()
    for A, B, C in [(Point(0, 10), Point(0, 0), Point(16, 0)), (Point(3, 8), Point(-5, 0), Point(15, 0))]:
        assert area(A, B, C) == 80
        D = B + (C - B) * Rational(1, 4)
        E = C.midpoint(A)
        P = Line(A, D).intersection(Line(B, E))[0]
        F = Line(C, P).intersection(Line(A, B))[0]
        assert Segment(A, B).contains(F)
        out.add(area(A, F, P))
    assert len(out) == 1
    return out.pop()


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"GE04-{name}"
        got = str(fn()).replace(" ", "")
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if got == key else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
