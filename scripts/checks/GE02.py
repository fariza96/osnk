#!/usr/bin/env python3
"""Pemeriksaan komputasional GE02. Setiap konfigurasi dibangun ulang dengan koordinat eksak (sympy)
dari data di pernyataan soal (bentuk bebas dipilih sembarang yang sah); besaran yang ditanyakan dihitung
lalu dibandingkan dengan kunci. Bila hasilnya tidak bergantung pada bentuk, dicek dengan dua bentuk berbeda.
Gambar tidak dipakai sebagai bukti."""
import json
import sys
from pathlib import Path

from sympy import Line, Point, Polygon, Rational, Segment, nsimplify, simplify, solve, sqrt, symbols, nsolve, acos

BANK = Path(__file__).resolve().parents[2] / "content/questions/GE02.json"
h, s, t, y = symbols("h s t y", positive=True)


def area(*P):
    return abs(Polygon(*P).area)


def meet(P, Q, R, S):
    return Line(P, Q).intersection(Line(R, S))[0]


def on(P, Q, r):
    """Titik X pada PQ dengan PX:PQ = r."""
    return P + (Q - P) * r


def E01():  # trapesium AB || DC, [AOB]=36, [COD]=16; luas trapesium. CD dan tinggi tidak diketahui.
    out = set()
    c = symbols("c", positive=True)
    for ab, dx in [(6, 1), (9, -2)]:  # dua panjang AB dan pergeseran berbeda
        A, B, D, C = Point(0, 0), Point(ab, 0), Point(dx, h), Point(dx + c, h)
        O = meet(A, C, B, D)
        sols = solve([area(A, O, B) - 36, area(C, O, D) - 16], [c, h], dict=True)
        assert len(sols) == 1, sols
        out.add(simplify(area(A, B, C, D).subs(sols[0])))
    assert len(out) == 1
    return out.pop()


def E02():  # siku-siku di C, CD garis tinggi, AD=4, DB=9; luas ABC
    A, B, D = Point(-4, 0), Point(9, 0), Point(0, 0)
    c = solve((A - Point(0, y)).dot(B - Point(0, y)), y)[0]  # C=(0,y) dengan CA ⟂ CB
    return area(A, B, Point(0, c))


def P001():  # tiang 3 m, bayangan 2 m; pohon bayangan 14 m
    return Rational(3, 2) * 14


def P002():
    return 27 * Rational(5, 3) ** 2


def P003():
    out = set()
    for A in [Point(1, 5), Point(-3, 2)]:
        B, C = Point(0, 0), Point(7, 0)
        k = 63 / area(A, B, C)
        A = Point(A.x, A.y * k)
        D = on(B, C, Rational(2, 7))
        out.add(area(A, B, D))
    assert len(out) == 1
    return out.pop()


def P004():  # BC=12, tinggi 6, persegi PQRS dengan PQ pada BC
    out = set()
    for ax in [4, 7]:
        A, B, C = Point(ax, 6), Point(0, 0), Point(12, 0)
        xl = Line(A, B).intersection(Line(Point(0, s), Point(1, s)))[0].x
        xr = Line(A, C).intersection(Line(Point(0, s), Point(1, s)))[0].x
        out.add(solve(xr - xl - s, s)[0])
    assert len(out) == 1
    return out.pop()


def P005():
    out = set()
    for A in [Point(2, 9), Point(-1, 4)]:
        B, C = Point(0, 0), Point(10, 0)
        A = Point(A.x, A.y * 120 / area(A, B, C))
        D, E = on(A, B, Rational(1, 3)), on(A, C, Rational(3, 4))
        out.add(area(A, D, E))
    assert len(out) == 1
    return out.pop()


def P006():  # AB=6, AC=9, D pada AC dengan sudut ABD = sudut ACB; DC
    out = set()
    for B in [Point(3, 3 * sqrt(3)), Point(Rational(18, 5), Rational(24, 5))]:  # |AB| = 6
        A, C = Point(0, 0), Point(9, 0)
        assert A.distance(B) == 6
        target = float(acos((A - C).dot(B - C) / (C.distance(A) * C.distance(B))))
        d = symbols("d")
        D = Point(d, 0)
        f = acos((A - B).dot(D - B) / (B.distance(A) * B.distance(D))) - target
        dv = nsimplify(nsolve(f, d, 4.5), tolerance=1e-20, rational=True)
        assert 0 < dv < 9
        out.add(9 - dv)
    assert len(out) == 1
    return out.pop()


def P007():  # titik tengah sisi segi empat berluas 50
    out = set()
    for P in [(Point(0, 0), Point(9, 1), Point(7, 8), Point(1, 6)), (Point(0, 0), Point(12, 0), Point(5, 3), Point(2, 7))]:
        k = sqrt(50 / area(*P))
        P = [Point(p.x * k, p.y * k) for p in P]
        M = [on(P[i], P[(i + 1) % 4], Rational(1, 2)) for i in range(4)]
        out.add(simplify(area(*M)))
    assert len(out) == 1
    return out.pop()


def P008():  # AB=10, CD=15, PQ melalui O sejajar alas
    out = set()
    for dx, hh in [(2, 7), (-4, 3)]:
        A, B, D, C = Point(0, 0), Point(10, 0), Point(dx, hh), Point(dx + 15, hh)
        O = meet(A, C, B, D)
        P = meet(A, D, O, O + Point(1, 0))
        Q = meet(B, C, O, O + Point(1, 0))
        assert simplify(P.distance(O) - O.distance(Q)) == 0  # klaim catatan: O titik tengah PQ
        out.add(P.distance(Q))
    assert len(out) == 1
    return out.pop()


def P009():  # AB=6, CD=9, tinggi 4; kaki diperpanjang bertemu di P; luas PAB
    out = set()
    for dx in [-1, 2]:
        A, B, D, C = Point(0, 0), Point(6, 0), Point(dx, -4), Point(dx + 9, -4)
        P = meet(A, D, B, C)
        out.add(area(P, A, B))
    assert len(out) == 1
    return out.pop()


def P010():  # luas 120, D titik tengah BC, AE:EC = 1:2, F = AD ∩ BE; luas AFE
    out = set()
    for A in [Point(3, 8), Point(-2, 5)]:
        B, C = Point(0, 0), Point(10, 0)
        A = Point(A.x, A.y * 120 / area(A, B, C))
        D, E = on(B, C, Rational(1, 2)), on(A, C, Rational(1, 3))
        F = meet(A, D, B, E)
        assert F == on(A, D, Rational(1, 2))  # klaim pembahasan: F titik tengah AD
        out.add(area(A, F, E))
    assert len(out) == 1
    return out.pop()


def P011():  # persegi sisi 10, E tengah BC, F tengah CD, G = AE ∩ BF; luas GECF
    A, B, C, D = Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10)
    E, F = on(B, C, Rational(1, 2)), on(C, D, Rational(1, 2))
    G = meet(A, E, B, F)
    assert (G - A).dot(G - B) == 0  # klaim: sudut AGB siku-siku
    assert simplify(B.distance(G) / G.distance(F)) == Rational(2, 3)  # klaim kekeliruan umum: BG:GF = 2:3
    return area(G, E, C, F)


def P012():  # trapesium alas 7 dan 17; garis sejajar alas membagi dua sama luas
    out = set()
    for dx, hh in [(3, 5), (-2, 9)]:
        A, B, D, C = Point(0, 0), Point(17, 0), Point(dx, hh), Point(dx + 7, hh)
        L = lambda yy: meet(A, D, Point(0, yy), Point(1, yy)).distance(meet(B, C, Point(0, yy), Point(1, yy)))
        total = area(A, B, C, D)
        yy = [v for v in solve((17 + L(t)) / 2 * t - total / 2, t) if 0 < v < hh][0]
        out.add(simplify(L(yy)))
    assert len(out) == 1
    return out.pop()


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"GE02-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
