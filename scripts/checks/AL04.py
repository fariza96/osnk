#!/usr/bin/env python3
"""Pemeriksaan komputasional AL04. Setiap jawaban dihitung ulang langsung dari pernyataan soal dengan
aritmetika pecahan eksak (menjumlah/mengalikan suku satu per satu, mengiterasi rekursi), bukan dengan bentuk
tertutup yang dipakai di pembahasan. Deret tak hingga diperiksa dengan sympy (jumlah eksak) dan jumlah parsial."""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

BANK = Path(__file__).resolve().parents[2] / "content/questions/AL04.json"


def E01():  # prod_{k=2}^{100} (1 - 1/k^2)
    p = F(1)
    for k in range(2, 101):
        p *= 1 - F(1, k * k)
    return p


def E02():  # a1=1, a2=3, a_{n+2} = a_{n+1} - a_n; jumlah 2026 suku pertama
    a = [1, 3]
    while len(a) < 2026:
        a.append(a[-1] - a[-2])
    return sum(a)


def P001():  # aritmetika: u5 = 17, u12 = 38; u20
    a, d = sp.symbols("a d")
    s = sp.solve([a + 4 * d - 17, a + 11 * d - 38], [a, d])
    return s[a] + 19 * s[d]


def P002():  # geometri real: u2 = 6, u5 = 162; u7
    a, r = sp.symbols("a r", real=True)
    sols = sp.solve([a * r - 6, a * r**4 - 162], [a, r], dict=True)
    vals = {s[a] * s[r] ** 6 for s in sols}
    assert len(vals) == 1, vals
    return vals.pop()


def P003():
    return sum(n for n in range(100, 1000) if n % 7 == 0)


def P004():  # deret geometri tak hingga: jumlah 12, jumlah kuadrat 48; suku pertama
    a, r = sp.symbols("a r", real=True)
    sols = [s for s in sp.solve([a / (1 - r) - 12, a**2 / (1 - r**2) - 48], [a, r], dict=True) if abs(s[r]) < 1]
    assert len(sols) == 1, sols
    return sols[0][a]


def P005():  # n terkecil dengan sum_{k=1}^n 1/((2k-1)(2k+1)) > 49/100
    s, n = F(0), 0
    while s <= F(49, 100):
        n += 1
        s += F(1, (2 * n - 1) * (2 * n + 1))
    return n


def P006():  # a1 = 5, a_{n+1} = 3 a_n - 4; a6
    a = 5
    for _ in range(5):
        a = 3 * a - 4
    return a


def P007():  # tiga bilangan aritmetika naik berjumlah 15; +1, +3, +9 menjadi geometri; hasil kali
    out = []
    for d in range(1, 50):
        x, y, z = 5 - d, 5, 5 + d
        if (y + 3) ** 2 == (x + 1) * (z + 9):
            out.append(x * y * z)
    assert out == [105], out
    return out[0]


def P008():  # a1 = 2, a_{n+1} = (1 + a_n)/(1 - a_n); hasil kali 2026 suku pertama
    a, p = F(2), F(1)
    for _ in range(2026):
        p *= a
        a = (1 + a) / (1 - a)
    return p


def P009():  # 100 * sum_{k=1}^9 (2k+1)/(k^2 (k+1)^2)
    return 100 * sum(F(2 * k + 1, k * k * (k + 1) ** 2) for k in range(1, 10))


def P010():  # sum F_n / 2^n (Fibonacci F1 = F2 = 1)
    # Nilai eksak lewat rumus Binet: F_n = (phi^n - psi^n)/sqrt5, jadi jumlahnya dua deret geometri (|phi/2| < 1).
    phi, psi = (1 + sp.sqrt(5)) / 2, (1 - sp.sqrt(5)) / 2
    geo = lambda q: (q / 2) / (1 - q / 2)
    exact = sp.nsimplify(sp.simplify((geo(phi) - geo(psi)) / sp.sqrt(5)))
    # Jumlah parsial 200 suku; ekornya < (phi/2)^201 / (1 - phi/2) < 1e-17.
    fa, fb, part = 1, 1, F(0)
    for k in range(1, 201):
        part += F(fa, 2**k)
        fa, fb = fb, fa + fb
    assert abs(float(part) - float(exact)) < 1e-12
    return exact


def P011():  # sum_{k=1}^9 k/(k^4 + k^2 + 1)
    return sum(F(k, k**4 + k**2 + 1) for k in range(1, 10))


def P012():  # barisan aritmetika tak hingga, suku pertama 1, beda bulat positif, memuat 2026
    return sum(1 for d in range(1, 2026) if (2026 - 1) % d == 0)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"AL04-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
