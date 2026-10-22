#!/usr/bin/env python3
"""Pemeriksaan komputasional KO02. Setiap jawaban dihitung ulang dengan enumerasi langsung
(itertools), bukan dengan rumus yang dipakai di pembahasan, lalu dibandingkan dengan answer_spec."""
import json
import sys
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/KO02.json"


def adjacent(seq, u, v):
    return any({seq[i], seq[i + 1]} == {u, v} for i in range(len(seq) - 1))


def circ_classes(people, ok):
    """Banyak susunan melingkar (rotasi dianggap sama) yang memenuhi ok(susunan)."""
    seen = set()
    for p in permutations(people):
        if ok(p):
            k = p.index(people[0])
            seen.add(p[k:] + p[:k])
    return len(seen)


def circ_adj(p, u, v):
    n = len(p)
    return any({p[i], p[(i + 1) % n]} == {u, v} for i in range(n))


def E01():  # 5 putra, 3 putri berbaris; tidak ada dua putri bersebelahan
    people = ["L1", "L2", "L3", "L4", "L5", "P1", "P2", "P3"]
    return sum(1 for p in permutations(people)
               if not any(p[i][0] == "P" and p[i + 1][0] == "P" for i in range(7)))


def E02():  # x1+x2+x3+x4 = 12, x1>=1, x2>=2, x3,x4>=0
    return sum(1 for a, b, c in product(range(13), repeat=3) if a >= 1 and b >= 2 and 12 - a - b - c >= 0)


def P001():  # 4 orang dari 7 putra + 5 putri, tepat 2 putri
    people = [("L", i) for i in range(7)] + [("P", i) for i in range(5)]
    return sum(1 for c in combinations(people, 4) if sum(g == "P" for g, _ in c) == 2)


def P002():
    return len(set(permutations("MATEMATIKA")))


def P003():  # 7 orang melingkar, A dan B bersebelahan
    return circ_classes(tuple("ABCDEFG"), lambda p: circ_adj(p, "A", "B"))


def P004():  # 3 buku matematika berdampingan, 2 buku fisika tidak bersebelahan, 2 buku lain
    books = ["M1", "M2", "M3", "F1", "F2", "L1", "L2"]
    cnt = 0
    for p in permutations(books):
        pos = sorted(p.index(m) for m in ("M1", "M2", "M3"))
        if pos[2] - pos[0] == 2 and not adjacent(p, "F1", "F2"):
            cnt += 1
    return cnt


def P005():  # tim 5 dari 6 guru + 4 siswa, paling sedikit 2 siswa
    people = [("G", i) for i in range(6)] + [("S", i) for i in range(4)]
    return sum(1 for c in combinations(people, 5) if sum(g == "S" for g, _ in c) >= 2)


def P006():  # lintasan R/U dari (0,0) ke (6,4), melalui (2,2), tidak melalui (4,3)
    cnt = 0
    for rs in combinations(range(10), 6):
        pts, xx, yy = {(0, 0)}, 0, 0
        for i in range(10):
            xx, yy = (xx + 1, yy) if i in rs else (xx, yy + 1)
            pts.add((xx, yy))
        cnt += (2, 2) in pts and (4, 3) not in pts
    return cnt


def P007():  # bilangan 4 digit dengan jumlah digit 9
    return sum(1 for n in range(1000, 10000) if sum(map(int, str(n))) == 9)


def P008():  # himpunan 3 anggota dari {1..12} tanpa dua bilangan berurutan
    return sum(1 for a, b, c in combinations(range(1, 13), 3) if b - a > 1 and c - b > 1)


def P009():  # 4 putra, 4 putri melingkar, berselang-seling
    people = ("L1", "P1", "L2", "P2", "L3", "P3", "L4", "P4")
    return circ_classes(people, lambda p: all(p[i][0] != p[(i + 1) % 8][0] for i in range(8)))


def P010():  # x+y+z = 15, 0 <= x,y,z <= 7
    return sum(1 for a, b in product(range(8), repeat=2) if 0 <= 15 - a - b <= 7)


def P011():  # sum k*C(10,k): hitung sebagai banyak pasangan (tim, ketua) dari 10 orang
    return sum(len(t) for r in range(11) for t in combinations(range(10), r))


def P012():  # segitiga dari titik sudut segi-10 tanpa sisi yang berimpit dengan sisi segi-10
    def side(u, v):
        return (u - v) % 10 in (1, 9)
    return sum(1 for a, b, c in combinations(range(10), 3) if not (side(a, b) or side(b, c) or side(a, c)))


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"KO02-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
