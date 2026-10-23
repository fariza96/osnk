#!/usr/bin/env python3
"""Pemeriksaan komputasional KO05. Pencacahan dengan pencarian lengkap (barisan, kata, pengubinan, pemasangan tali
busur), BFS untuk menara Hanoi, Havel–Hakimi untuk keberadaan graf dengan derajat tertentu, rumus Euler pada
susunan garis acak yang benar-benar dihitung titik potongnya, dan pemeriksaan batas + konstruksi untuk soal ekstrem.
Rekurensi di pembahasan tidak dipakai."""
import json
import random
import sys
from collections import deque
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/KO05.json"


def graphical(seq):
    s = sorted(seq, reverse=True)
    while s and s[0] > 0:
        d = s.pop(0)
        if d > len(s):
            return False
        for i in range(d):
            s[i] -= 1
            if s[i] < 0:
                return False
        s.sort(reverse=True)
    return True


def E01():
    return sum(1 for w in product("01", repeat=10) if "11" not in "".join(w))


def E02():
    sols = [(x, y) for x in range(16) for y in range(16) if x + y == 15 and 3 * x + 4 * y == 52]
    assert len(sols) == 1
    x, y = sols[0]
    assert graphical([3] * x + [4] * y)
    return y


def P001():
    seq = [1, 2, 2, 3, 3, 4, 4, 5]
    assert graphical(seq)
    return sum(seq) // 2


def P002():
    def ways(n):
        return 1 if n == 0 else sum(ways(n - t) for t in (1, 3) if t <= n)
    return ways(9)


def P003():  # 10 garis acak; hitung titik potong nyata, lalu daerah dengan rumus Euler (titik di tak hingga)
    R = random.Random(7)
    lines = [(Fraction(R.randint(-50, 50)), Fraction(R.randint(-50, 50))) for _ in range(10)]  # y = m x + c
    assert len({m for m, _ in lines}) == 10  # tidak ada yang sejajar
    pts = {}
    for i, j in combinations(range(10), 2):
        (m1, c1), (m2, c2) = lines[i], lines[j]
        x = (c2 - c1) / (m1 - m2)
        pts.setdefault((x, m1 * x + c1), set()).update({i, j})
    assert all(len(v) == 2 for v in pts.values())  # tidak ada tiga garis melalui satu titik
    V = len(pts) + 1
    E = sum(sum(1 for p in pts.values() if i in p) + 1 for i in range(10))
    return E - V + 2


def P004():
    return sum(1 for w in product("01", repeat=8) if "111" not in "".join(w))


def P005():  # pencarian lengkap pengubinan papan 2 x 8
    W = 8

    def count(filled):
        free = [(r, c) for c in range(W) for r in range(2) if (r, c) not in filled]
        if not free:
            return 1
        r, c = free[0]
        tot = 0
        for cells in ([(r, c), (r + 1, c)], [(r, c), (r, c + 1)], [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]):
            if all(0 <= a < 2 and 0 <= b < W and (a, b) not in filled for a, b in cells):
                tot += count(filled | frozenset(cells))
        return tot
    return count(frozenset())


def P006():
    ok = []
    for k in range(25):
        if (25 * k) % 2:
            continue  # jumlah derajat ganjil: mustahil
        m = k // 2
        nb = {v: {(v + d) % 25 for d in range(-m, m + 1) if d} for v in range(25)}
        assert all(len(nb[v]) == k and all(v in nb[u] for u in nb[v]) for v in range(25))
        ok.append(k)
    return len(ok)


def P007():
    return sum(1 for w in product("ABC", repeat=6) if "AA" not in "".join(w))


def P008():  # BFS ruang keadaan: keadaan = tiang setiap cakram
    n = 7
    start, goal = (0,) * n, (2,) * n
    dist = {start: 0}
    q = deque([start])
    while q:
        s = q.popleft()
        if s == goal:
            return dist[s]
        tops = {}
        for disk in range(n):  # cakram 0 terkecil
            tops.setdefault(s[disk], disk)
        for a, disk in tops.items():
            for b in range(3):
                if b != a and (b not in tops or tops[b] > disk):
                    t = s[:disk] + (b,) + s[disk + 1:]
                    if t not in dist:
                        dist[t] = dist[s] + 1
                        q.append(t)


def P009():
    return comb(30, 2) - 30 * 4 // 2


def min_edges_connected_brute(n):
    edges = list(combinations(range(n), 2))
    worst = 0
    for mask in range(1 << len(edges)):
        es = [edges[i] for i in range(len(edges)) if mask >> i & 1]
        seen, stack = {0}, [0]
        while stack:
            v = stack.pop()
            for a, b in es:
                for u, w in ((a, b), (b, a)):
                    if u == v and w not in seen:
                        seen.add(w); stack.append(w)
        if len(seen) < n:
            worst = max(worst, len(es))
    return worst + 1


def P010():
    assert min_edges_connected_brute(5) == comb(4, 2) + 1  # pola K_{n-1} + titik terpencil dicek penuh untuk n = 5
    return max(comb(k, 2) + comb(10 - k, 2) for k in range(1, 10)) + 1


def P011():
    def matchings(pts):
        if not pts:
            return 1
        a, rest = pts[0], pts[1:]
        tot = 0
        for i, b in enumerate(rest):
            inside, outside = rest[:i], rest[i + 1:]
            tot += matchings(inside) * matchings(outside) if len(inside) % 2 == 0 else 0
        return tot

    def brute(n):  # semua pemasangan, buang yang berpotongan
        def all_pm(p):
            if not p:
                yield []
                return
            for i in range(1, len(p)):
                for r in all_pm(p[1:i] + p[i + 1:]):
                    yield [(p[0], p[i])] + r
        cross = lambda e, f: (e[0] < f[0] < e[1] < f[1]) or (f[0] < e[0] < f[1] < e[1])
        return sum(1 for m in all_pm(list(range(n))) if not any(cross(e, f) for e, f in combinations(m, 2)))
    got = brute(10)
    assert got == matchings(list(range(10)))
    return got


def P012():
    feasible = [k for k in range(1, 9) if 5 * k <= comb(k, 2) + k * (8 - k)]
    k = max(feasible)
    # konstruksi: T_i mengalahkan T_{i+1}, T_{i+2} (mod 5) dan semua tim 5, 6, 7
    wins = {i: 0 for i in range(8)}
    for i in range(5):
        for d in (1, 2):
            wins[i] += 1
        wins[i] += 3
    for a, b in combinations(range(5, 8), 2):
        wins[a] += 1
    assert sum(wins.values()) == comb(8, 2) and sum(w >= 5 for w in wins.values()) == k
    return k


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"KO05-{name}"
        got = str(fn())
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if got == key else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
