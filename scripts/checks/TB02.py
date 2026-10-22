#!/usr/bin/env python3
"""Pemeriksaan komputasional TB02. Menghitung ulang setiap jawaban dari pernyataan soal
(enumerasi/aritmetika eksak) lalu membandingkannya dengan answer_spec di bank soal.
Enumerasi pada rentang hingga hanya memeriksa jawaban, bukan pengganti pembuktian umum."""
import json
import sys
from itertools import product
from math import factorial, isqrt
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/TB02.json"


def is_prime(n):
    return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))


def E01():
    return (pow(2, 2026, 7) + pow(3, 2026, 7)) % 7


def E02():  # n positif terkecil: n≡2 (mod 5), n≡3 (mod 7), n≡4 (mod 9)
    return next(n for n in range(1, 10_000) if n % 5 == 2 and n % 7 == 3 and n % 9 == 4)


def P001():
    return sum(factorial(k) for k in range(1, 101)) % 12


def P002():
    return pow(7, 2027, 10)


def P003():  # x positif terkecil dengan 5x ≡ 4 (mod 13)
    return next(x for x in range(1, 100) if (5 * x - 4) % 13 == 0)


def P004():  # banyak nilai ±1±2±...±10 (semua 2^10 pilihan tanda)
    return len({sum(s * k for s, k in zip(signs, range(1, 11))) for signs in product((1, -1), repeat=10)})


def P005():
    return pow(7, 2026, 100)


def P006():
    return sum(k ** 6 for k in range(1, 2027)) % 7


def P007():  # 100 < n < 1000; sisa 3, 5, 8 bila dibagi 4, 6, 9
    return sum(1 for n in range(101, 1000) if n % 4 == 3 and n % 6 == 5 and n % 9 == 8)


def P008():  # prima p dengan 2^p + p^2 prima; untuk p > 3 nilainya kelipatan 3 (dibuktikan), cek p < 200
    ps = [p for p in range(2, 200) if is_prime(p) and is_prime(2 ** p + p * p)]
    assert ps == [3], ps
    return sum(ps)


def P009():
    return sum(1 for n in range(1, 101) if (pow(2, n, 17) - 1) % 17 == 0)


def P010():  # dua digit terakhir 3^(3^2026), eksponen dihitung eksak lalu dipangkatkan modular
    return pow(3, 3 ** 2026, 100)


def P011():
    return sum(1 for n in range(1, 101) if (n * pow(2, n, 5) + 1) % 5 == 0)


def P012():  # (m,n) positif dengan 3^m + 7 = n^2; m > 40 dibuang oleh argumen mod 4 + pemfaktoran
    sols = [(m, isqrt(3 ** m + 7)) for m in range(1, 200) if isqrt(3 ** m + 7) ** 2 == 3 ** m + 7]
    assert sols == [(2, 4)], sols
    return sum(sols[0])


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"TB02-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
