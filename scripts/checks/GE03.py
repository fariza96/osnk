#!/usr/bin/env python3
"""Pemeriksaan komputasional GE03. Setiap konfigurasi dibangun ulang dengan koordinat (sympy, eksak bila
memungkinkan) dari data soal; data yang diberikan di soal dicek berlaku pada konfigurasi itu, lalu besaran
yang ditanyakan dihitung. Bila jawaban tidak bergantung pada bagian konfigurasi yang bebas, dicek pada dua
bentuk berbeda. Gambar tidak dipakai sebagai bukti."""
import json
import math
import sys
from pathlib import Path

from sympy import (Circle, Line, Point, Rational, Segment, Triangle, acos, cos, deg, nsimplify, pi, rad, simplify,
                   sin, solve, sqrt, symbols)

BANK = Path(__file__).resolve().parents[2] / "content/questions/GE03.json"
t = symbols("t", real=True)


def ang(P, Q, R):
    """Besar sudut PQR (derajat), dibulatkan ke bilangan rasional sederhana."""
    u, v = P - Q, R - Q
    c = float(u.dot(v)) / (float(u.distance(Point(0, 0))) * float(v.distance(Point(0, 0))))
    return nsimplify(round(math.degrees(math.acos(max(-1, min(1, c)))), 9), rational=True)


def on_circle(deg_):
    return Point(cos(rad(deg_)), sin(rad(deg_)))


def E01():  # ABCD tali busur, sudut ABC = 110, sudut ACD = 40; sudut CBD (busur AB dan BC bebas)
    out = set()
    for ab in (70, 30):
        A, B, C, D = on_circle(0), on_circle(ab), on_circle(140), on_circle(280)
        assert ang(A, B, C) == 110 and ang(A, C, D) == 40
        out.add(ang(C, B, D))
    assert len(out) == 1
    return out.pop()


def E02():  # PT = 12, PA = 8 pada garis melalui pusat; jari-jari
    r, d = symbols("r d", positive=True)
    sol = solve([d**2 - r**2 - 144, d - r - 8], [r, d], dict=True)
    assert len(sol) == 1
    return sol[0][r]


def P001():
    out = set()
    for c in (200, 300):  # C pada busur besar
        A, B, C = on_circle(0), on_circle(130), on_circle(c)
        out.add(ang(A, C, B))
    assert len(out) == 1
    return out.pop()


def P002():  # tali busur AB dan CD berpotongan di P: AP=4, PB=6, CP=3; CD
    out = set()
    for th in (Rational(1, 3), 2):
        P, A, B = Point(0, 0), Point(-4, 0), Point(6, 0)
        u = Point(1, th) / sqrt(1 + th**2)
        C = P + u * 3
        circ = Circle(A, B, C)
        D = [q for q in circ.intersection(Line(C, P)) if q != C][0]
        out.add(simplify(C.distance(D)))
    assert len(out) == 1
    return out.pop()


def P003():
    O, P = Point(0, 0), Point(13, 0)
    T = [q for q in Circle(O, 5).intersection(Circle((O + P) / 2, Rational(13, 2)))][0]  # kaki garis singgung (Thales)
    return P.distance(T)


def P004():  # garis singgung di A membentuk 62 derajat dengan AB (sisi berlawanan C), sudut ABC = 70; sudut BAC
    A = on_circle(90)
    B = on_circle(90 + 124)  # busur AB (tanpa C) = 2*62
    C = on_circle(90 + 124 + 96)  # busur BC = 2*48
    assert ang(A, B, C) == 70
    tang = [A + Point(1, 0), A - Point(1, 0)]  # garis singgung di A (jari-jari OA vertikal)
    side = lambda X: (B.x - A.x) * (X.y - A.y) - (B.y - A.y) * (X.x - A.x)  # tanda: sisi garis AB
    Tp = [X for X in tang if side(X) * side(C) < 0][0]
    assert ang(Tp, A, B) == 62
    return ang(B, A, C)


def P005():  # 13-14-15, lingkaran dalam menyinggung BC di D; BD
    B, C = Point(0, 0), Point(14, 0)
    A = [q for q in Circle(B, 13).intersection(Circle(C, 15)) if q.y > 0][0]
    T = Triangle(A, B, C)
    I, r = T.incenter, T.inradius
    D = Point(I.x, 0)
    assert simplify(I.y - r) == 0
    return B.distance(D)


def P006():  # garis potong PAB (PA=4, AB=5) dan PCD (PC=3); CD
    out = set()
    for th in (Rational(1, 2), 3):
        P, A, B = Point(0, 0), Point(4, 0), Point(9, 0)
        u = Point(1, th) / sqrt(1 + th**2)
        C = u * 3
        circ = Circle(A, B, C)
        D = [q for q in circ.intersection(Line(P, C)) if q != C][0]
        assert P.distance(D) > 3
        out.add(simplify(C.distance(D)))
    assert len(out) == 1
    return out.pop()


def P007():  # jari-jari lingkaran luar segitiga 13-14-15
    B, C = Point(0, 0), Point(14, 0)
    A = [q for q in Circle(B, 13).intersection(Circle(C, 15)) if q.y > 0][0]
    return Triangle(A, B, C).circumradius


def P008():  # AB diameter 10, CD tegak lurus AB, AD = 2; CD
    A, B = Point(-5, 0), Point(5, 0)
    D = Point(-3, 0)
    C = [q for q in Circle(Point(0, 0), 5).intersection(Line(D, D + Point(0, 1))) if q.y > 0][0]
    return C.distance(D)


def P009():  # dua lingkaran melalui A, B; garis singgung persekutuan menyinggung di S, T; AB memotong ST di M
    out = set()
    M, A, B = Point(0, 0), Point(0, 2), Point(0, 8)
    for slope in (0, Rational(1, 3)):
        L = Line(M, Point(1, slope))
        h = symbols("h", real=True)
        Ctr = Point(h, 5)
        hs = solve(L.distance(Ctr) ** 2 - Ctr.distance(A) ** 2, h)
        assert len(hs) == 2
        S, T = [L.projection(Point(hv, 5)) for hv in hs]
        out.add(simplify(S.distance(T)))
    assert len(out) == 1
    return out.pop()


def P010():  # sudut B = 70, C = 50; garis tinggi BE, CF; sudut EFC
    B, C = Point(0, 0), Point(10, 0)
    A = Line(B, B + Point(cos(rad(70)), sin(rad(70)))).intersection(Line(C, C + Point(-cos(rad(50)), sin(rad(50)))))[0]
    E = Line(A, C).projection(B)
    F = Line(A, B).projection(C)
    return ang(E, F, C)


def P011():  # r = 10, OP = 8; banyak tali busur melalui P yang panjangnya bulat
    r, d = 10, 8
    count = 0
    for L in range(1, 2 * r + 1):
        s2 = Rational(r * r * 4 - L * L, 4 * d * d)  # sin^2(phi), phi = sudut tali busur terhadap OP
        if 0 <= s2 <= 1:
            count += 1 if s2 in (0, 1) else 2
    return count


def P012():  # AB = AC = 10, BC = 12; AD diameter lingkaran luar; BD
    A, B, C = Point(0, 8), Point(-6, 0), Point(6, 0)
    O = Triangle(A, B, C).circumcenter
    D = 2 * O - A
    assert simplify((A - B).dot(D - B)) == 0  # Thales: sudut ABD siku-siku
    return simplify(B.distance(D))


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"GE03-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
