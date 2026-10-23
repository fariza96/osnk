#!/usr/bin/env python3
"""Pemeriksaan komputasional TB04. Setiap jawaban dihitung ulang dengan enumerasi pada rentang yang
mencakup semua solusi (batasnya diturunkan dari pernyataan soal, dicatat per fungsi) atau dengan aritmetika
eksak, lalu dibandingkan dengan answer_spec. Enumerasi hanya memeriksa jawaban, bukan pembuktian umum."""
import json
import sys
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path

import sympy as sp

BANK = Path(__file__).resolve().parents[2] / "content/questions/TB04.json"


def S(n):
    return sum(map(int, str(n)))


def is_sq(n):
    return n >= 0 and isqrt(n) ** 2 == n


def E01():  # 7x + 11y = 500, x, y > 0 (x < 72, y < 46)
    return sum(1 for x in range(1, 72) for y in range(1, 46) if 7 * x + 11 * y == 500)


def E02():  # 1/x + 1/y + 1/z = 1, tripel terurut bulat positif (min <= 3, jadi semua <= 6 cukup; dicek sampai 60)
    return sum(1 for x in range(1, 61) for y in range(1, 61) for z in range(1, 61)
               if Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == 1)


def P001():
    return sum(1 for x in range(0, 16) for y in range(0, 10) if 3 * x + 5 * y == 47)


def P002():
    return sum(1 for n in range(10, 100) if n == 4 * S(n))


def P003():
    return sum(isqrt(n) for n in range(1, 31))


def P004():  # m^2 + 6m = n^2 + 15, bulat (|m|, |n| <= 50 cukup karena faktor 24)
    return sum(1 for m in range(-60, 61) for n in range(-60, 61) if m * m + 6 * m == n * n + 15)


def P005():  # n <= 50 tanpa solusi bulat x^2 - y^2 = n (|x|, |y| <= 26 cukup: x = (n+1)/2 atau n/4+1)
    ok = {x * x - y * y for x in range(0, 60) for y in range(0, 60)}
    return sum(1 for n in range(1, 51) if n not in ok)


def P006():
    sols = [n for n in range(100, 1000) if n == 12 * S(n)]
    assert sols == [108], sols
    return sols[0]


def P007():  # x^2 - 7 floor(x) + 10 = 0; jumlah kuadrat semua solusi real
    x = sp.symbols("x", real=True)
    total, cnt = 0, 0
    for n in range(-50, 51):  # x^2 = 7n - 10 dengan floor(x) = n
        v = 7 * n - 10
        if v < 0:
            continue
        for r in {sp.sqrt(v), -sp.sqrt(v)}:
            if sp.floor(r) == n:
                total += r**2
                cnt += 1
    assert cnt == 4, cnt
    return total


def P008():  # 3x + 5y = 150, x, y >= 1
    return sum(1 for x in range(1, 51) for y in range(1, 31) if 3 * x + 5 * y == 150)


def P009():  # n <= 100 dengan 1! + ... + n! kuadrat sempurna
    s, cnt = 0, 0
    for n in range(1, 101):
        s += factorial(n)
        cnt += is_sq(s)
    return cnt


def P010():
    return len({k * k // 100 for k in range(1, 101)})


def P011():  # 3^x - 2^y = 1, bulat positif; jumlah x+y atas semua solusi (x, y <= 60 dicek)
    sols = [(x, y) for x in range(1, 61) for y in range(1, 61) if 3 ** x - 2 ** y == 1]
    assert sols == [(1, 1), (2, 3)], sols
    return sum(x + y for x, y in sols)


def P012():  # n + S(n) = 2026 (n < 2026)
    sols = [n for n in range(1, 2026) if n + S(n) == 2026]
    assert sols == [2021], sols
    return sum(sols)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"TB04-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
