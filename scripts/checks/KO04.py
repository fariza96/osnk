#!/usr/bin/env python3
"""Pemeriksaan komputasional KO04. Semua jawaban dihitung dengan pencarian lengkap pada ruang sampel yang
sama mungkin (pecahan eksak), terpisah dari rumus inklusi-eksklusi di pembahasan."""
import json
import sys
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/KO04.json"


def E01():
    return sum(1 for n in range(1, 1001) if n % 2 and n % 3 and n % 5)


def E02():  # 10 lemparan, harapan banyak AA (tumpang tindih)
    tot = sum(sum(s[i] == s[i + 1] == "A" for i in range(9)) for s in product("AG", repeat=10))
    return Fraction(tot, 2 ** 10)


def P001():  # |M|=23, |F|=18, 40 siswa, 7 tidak keduanya; cek dengan semua kemungkinan irisan
    ok = {x for x in range(19) if 40 - (23 + 18 - x) == 7}
    assert len(ok) == 1
    return ok.pop()


def P002():
    good = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b in (2, 3, 5, 7, 11))
    return Fraction(good, 36)


def P003():
    return Fraction(sum(sum(t) for t in product(range(1, 7), repeat=3)), 6 ** 3)


def P004():
    return sum(1 for n in range(1, 601) if n % 4 == 0 or n % 6 == 0 or n % 15 == 0)


def P005():  # lintasan (0,0)->(5,5) menghindari (2,2) dan (3,3), dihitung dengan DP
    bad = {(2, 2), (3, 3)}
    f = {}
    for x in range(6):
        for y in range(6):
            if (x, y) in bad:
                f[x, y] = 0
            elif x == y == 0:
                f[x, y] = 1
            else:
                f[x, y] = f.get((x - 1, y), 0) + f.get((x, y - 1), 0)
    return f[5, 5]


def P006():
    return sum(1 for g in product(range(3), repeat=5) if set(g) == {0, 1, 2})


def P007():  # 3 merah, 4 putih, 5 biru; 4 bola sekaligus
    balls = "M" * 3 + "P" * 4 + "B" * 5
    S = list(combinations(range(12), 4))
    return Fraction(sum(1 for c in S if {balls[i] for i in c} == {"M", "P", "B"}), len(S))


def P008():  # 8 orang berbeda (4 pria, 4 wanita) di 8 kursi melingkar
    people = "PPPPWWWW"
    tot = cnt = 0
    for perm in permutations(range(8)):
        cnt += 1
        tot += sum(people[perm[i]] != people[perm[(i + 1) % 8]] for i in range(8))
    return Fraction(tot, cnt)


def P009():
    S = list(combinations(range(1, 11), 3))
    return Fraction(sum(1 for a, b, c in S if b - a == c - b), len(S))


def P010():
    S = list(permutations(range(5)))
    return Fraction(sum(1 for p in S if sum(p[i] == i for i in range(5)) == 1), len(S))


def P011():
    S = list(permutations(range(1, 7)))
    return Fraction(sum(sum(p[k] > max(p[:k], default=0) for k in range(6)) for p in S), len(S))


def P012():
    return sum(1 for w in set(permutations("AABBCC")) if all(w[i] != w[i + 1] for i in range(5)))


def fmt(x):
    return f"{x.numerator}/{x.denominator}" if isinstance(x, Fraction) and x.denominator != 1 else str(x)


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"KO04-{name}"
        got = fmt(fn())
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if got == key else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
