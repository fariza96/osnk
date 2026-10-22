#!/usr/bin/env python3
"""Pemeriksaan komputasional TB03. Setiap jawaban dihitung ulang dengan mendaftar pembagi secara langsung
(bukan dengan rumus tau/sigma/Legendre yang dipakai di pembahasan), lalu dibandingkan dengan answer_spec.
Enumerasi pada rentang hingga hanya memeriksa jawaban, bukan pengganti pembuktian umum."""
import json
import sys
from math import factorial, isqrt, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BANK = Path(__file__).resolve().parents[2] / "content/questions/TB03.json"


def divisors(n):
    small = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return sorted(set(small + [n // d for d in small]))


def is_square(n):
    return isqrt(n) ** 2 == n


def is_cube(n):
    r = round(n ** (1 / 3))
    return any((r + e) ** 3 == n for e in (-1, 0, 1))


def vp(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def trailing_zeros(n):
    s = str(n)
    return len(s) - len(s.rstrip("0"))


def E01():  # pembagi 10! yang kuadrat sempurna
    return sum(1 for d in divisors(factorial(10)) if is_square(d))


def E02():  # banyak angka 0 di akhir 2026!
    return trailing_zeros(factorial(2026))


def P001():
    return len(divisors(360))


def P002():
    return sum(divisors(72))


def P003():
    return vp(factorial(20), 2)


def P004():  # 2 <= n <= 100, hasil kali semua pembagi = n^2
    return sum(1 for n in range(2, 101) if prod(divisors(n)) == n ** 2)


def P005():  # pembagi n^2 yang < n dan tidak membagi n, n = 2^4 3^3
    n = 2 ** 4 * 3 ** 3
    return sum(1 for d in divisors(n * n) if d < n and n % d)


def P006():  # k <= 1000 dengan 540k kubus sempurna
    return sum(1 for k in range(1, 1001) if is_cube(540 * k))


def P007():  # k terbesar dengan 12^k | 30!
    f, k = factorial(30), 0
    while f % 12 ** (k + 1) == 0:
        k += 1
    return k


def P008():  # jumlah pembagi ganjil 360
    return sum(d for d in divisors(360) if d % 2)


def P009():  # bilangan positif terkecil dengan tepat 12 pembagi
    return next(n for n in range(1, 10_000) if len(divisors(n)) == 12)


def P010():  # banyak k, 1..50, yang bukan banyak nol di akhir n! untuk n mana pun (n <= 300 cukup: z(300) = 74)
    vals = {trailing_zeros(factorial(n)) for n in range(1, 301)}
    return sum(1 for k in range(1, 51) if k not in vals)


def P011():  # n <= 100 dengan sigma(n) ganjil
    return sum(1 for n in range(1, 101) if sum(divisors(n)) % 2)


def P012():  # n <= 1000 dengan tepat 10 pembagi
    return sum(1 for n in range(1, 1001) if len(divisors(n)) == 10)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"TB03-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
