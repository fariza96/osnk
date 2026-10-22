#!/usr/bin/env python3
"""Pemeriksaan komputasional KO01: enumerasi lengkap (brute force) langsung dari pernyataan soal."""
import json
import sys
from itertools import product
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/KO01.json"
digits = lambda n: [int(c) for c in str(n)]


def subsets(n):
    return [frozenset(i + 1 for i in range(n) if m >> i & 1) for m in range(1 << n)]


def E01():  # bilangan 3 digit genap dengan digit berbeda
    return sum(1 for n in range(100, 1000) if n % 2 == 0 and len(set(str(n))) == 3)


def E02():  # bilangan 4 digit yang memuat setidaknya satu 7
    return sum(1 for n in range(1000, 10000) if "7" in str(n))


def P001():
    return 26**2 * 10**3


def P002():  # himpunan bagian {1..10} yang memuat 1 dan tidak memuat 2
    return sum(1 for s in subsets(10) if 1 in s and 2 not in s)


def P003():  # 3 pembuka (pilih <=1), 4 utama (tepat 1), 2 penutup (pilih <=1)
    return sum(1 for a, m, d in product(range(4), range(4), range(3)))


def P004():  # 1 <= n < 1000 tanpa digit 0 dan 5
    return sum(1 for n in range(1, 1000) if not set(str(n)) & {"0", "5"})


def P005():  # 5 kotak, 3 warna, bersebelahan beda, kotak 1 dan 5 merah
    return sum(1 for c in product("MHB", repeat=5)
               if c[0] == "M" and c[4] == "M" and all(c[i] != c[i + 1] for i in range(4)))


def P006():  # himpunan bagian {1..10} dengan paling sedikit satu genap
    return sum(1 for s in subsets(10) if any(e % 2 == 0 for e in s))


def P007():  # himpunan bagian {1..12} berbanyak anggota genap
    return sum(1 for s in subsets(12) if len(s) % 2 == 0)


def P008():  # bilangan genap 4 digit, digit berbeda, > 5000
    return sum(1 for n in range(5001, 10000) if n % 2 == 0 and len(set(str(n))) == 4)


def P009():  # kata sandi panjang 3..5 dari ABCD dengan paling sedikit satu A
    return sum(1 for L in (3, 4, 5) for w in product("ABCD", repeat=L) if "A" in w)


def P010():  # 1 <= n < 10000 dengan hasil kali digit 12
    def prod(n):
        r = 1
        for d in digits(n):
            r *= d
        return r
    return sum(1 for n in range(1, 10000) if prod(n) == 12)


def P011():  # bilangan 3 digit abc dengan a < b > c
    return sum(1 for n in range(100, 1000) if (lambda a, b, c: a < b > c)(*digits(n)))


def P012():  # pasangan tak terurut {A,B} himpunan bagian tak kosong {1..5} yang saling lepas
    S = [s for s in subsets(5) if s]
    return len({frozenset((A, B)) for A in S for B in S if not A & B})


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"KO01-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        ok = str(got) == str(key)
        bad += not ok
        print(f"{qid}: hitung={got} kunci={key} {'OK' if ok else 'BEDA'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
