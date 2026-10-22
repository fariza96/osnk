#!/usr/bin/env python3
"""Pemeriksaan komputasional TB01. Menghitung ulang setiap jawaban dari pernyataan soal
(enumerasi/aritmetika eksak) lalu membandingkannya dengan answer_spec di bank soal.
Enumerasi pada rentang hingga hanya memeriksa jawaban, bukan pengganti pembuktian umum."""
import json
import sys
from math import gcd, lcm
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/TB01.json"


def is_prime(n):
    return n >= 2 and all(n % p for p in range(2, int(n ** 0.5) + 1))


def E01():  # jumlah n>=1 dengan (n+3) | (n^2+15); n+3 | 24 membatasi n <= 21, cek sampai 10^4
    return sum(n for n in range(1, 10_000) if (n * n + 15) % (n + 3) == 0)


def E02():  # banyak pasangan (a,b), a<b, FPB 12, KPK 360 (a,b | 360)
    return sum(1 for a in range(1, 361) for b in range(a + 1, 361) if gcd(a, b) == 12 and lcm(a, b) == 360)


def P001():
    return gcd(2023, 1547)


def P002():  # b tunggal dengan FPB(84,b)=12, KPK=420 (b | 420)
    bs = [b for b in range(1, 421) if gcd(84, b) == 12 and lcm(84, b) == 420]
    assert len(bs) == 1, bs
    return bs[0]


def P003():  # max FPB(n+2, 3n+11); nilainya membagi 5, jadi n sampai 10^4 cukup untuk menemukannya
    return max(gcd(n + 2, 3 * n + 11) for n in range(1, 10_000))


def P004():
    return sum(1 for n in range(1, 101) if gcd(n, 12) == 4)


def P005():
    return sum(1 for n in range(1, 101) if gcd(n * n + 3, n + 1) == 4)


def P006():  # k = 84x+120y, x,y bulat; rentang x,y cukup lebar untuk k <= 100
    reach = {84 * x + 120 * y for x in range(-200, 201) for y in range(-200, 201)}
    return sum(1 for k in range(1, 101) if k in reach)


def P007():  # 0 < t <= 3600, tepat dua lampu
    return sum(1 for t in range(1, 3601) if sum(t % p == 0 for p in (12, 18, 30)) == 2)


def P008():  # |n^2+4n-21| prima; |n|>10 membuat kedua faktor |n+7|,|n-3| > 1
    sols = [n for n in range(-1000, 1001) if is_prime(abs(n * n + 4 * n - 21))]
    assert sols == [-8, 4], sols
    return sum(sols)


def P009():  # pasangan terurut (a,b) dengan KPK 72 (a,b | 72)
    return sum(1 for a in range(1, 73) for b in range(1, 73) if lcm(a, b) == 72)


def P010():  # 1 <= n <= 999, (n+5)/(n^2+3) tidak sederhana
    return sum(1 for n in range(1, 1000) if gcd(n + 5, n * n + 3) > 1)


def P011():
    def L(n):
        r = 1
        for k in range(1, n + 1):
            r = lcm(r, k)
        return r
    return sum(1 for n in range(2, 51) if L(n) != L(n - 1))


def P012():  # himpunan nilai FPB(a+b, a^2-ab+b^2) untuk a,b relatif prima; dibuktikan {1,3}
    vals = {gcd(a + b, a * a - a * b + b * b) for a in range(1, 300) for b in range(1, 300) if gcd(a, b) == 1}
    assert vals == {1, 3}, vals
    return sum(vals)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"TB01-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
