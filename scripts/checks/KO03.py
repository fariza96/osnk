#!/usr/bin/env python3
"""Pemeriksaan komputasional KO03. Soal "minimal berapa agar pasti" dihitung sebagai
(ukuran maksimum himpunan/konfigurasi yang belum memenuhi syarat) + 1, dengan pencarian lengkap,
pencocokan bipartit, atau BFS. Bila pencarian lengkap terlalu besar, dicek komponen buktinya:
contoh ekstrem (saksi) dan batas atas per kelas."""
import json
import random
import sys
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import dist, factorial
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "content/questions/KO03.json"


def max_free(n, bad):
    """Ukuran maksimum himpunan bagian {1..n} tanpa pasangan 'bad' (pencarian lengkap dengan memo)."""
    adj = {v: {u for u in range(1, n + 1) if u != v and bad(u, v)} for v in range(1, n + 1)}

    @lru_cache(None)
    def mis(rest):
        if not rest:
            return 0
        v = max(rest, key=lambda u: len(adj[u] & set(rest)))
        if not adj[v] & set(rest):
            return len(rest)  # tidak ada sisi lagi
        r = frozenset(rest)
        return max(mis(tuple(sorted(r - {v}))), 1 + mis(tuple(sorted(r - {v} - adj[v]))))
    return mis(tuple(range(1, n + 1)))


def E01():
    return max_free(20, lambda a, b: a + b == 21) + 1


def E02():  # 1..6, ganti a,b dengan a+b+ab; nilai akhir selalu sama (dicek 2000 urutan acak)
    R = random.Random(1)
    finals = set()
    for _ in range(2000):
        xs = list(range(1, 7))
        while len(xs) > 1:
            i, j = sorted(R.sample(range(len(xs)), 2))
            b, a = xs.pop(j), xs.pop(i)
            xs.append(a + b + a * b)
        finals.add(xs[0])
    assert finals == {factorial(7) - 1}, finals
    return finals.pop()


def P001():  # 30 siswa, 12 bulan: nilai terkecil dari bulan terpadat atas semua sebaran
    m = 1
    while 12 * m < 30:  # sebaran paling merata: tiap bulan paling banyak m
        m += 1
    # cek: dengan maks m-1 per bulan hanya muat 12(m-1) < 30 siswa; sebaran 6 bulan x3 + 6 bulan x2 = 30 memberi maks 3
    assert 12 * (m - 1) < 30 and 6 * 3 + 6 * 2 == 30
    return m


def P002():  # 5 merah, 7 biru, 9 hijau; minimal ambil agar pasti 3 sewarna
    worst = max(r + b + g for r in range(6) for b in range(8) for g in range(10) if max(r, b, g) <= 2)
    return worst + 1


def P003():  # minimal bilangan bulat agar pasti dua berselisih kelipatan 11
    return max_free(40, lambda a, b: (a - b) % 11 == 0) + 1  # 1..40 memuat semua sisa mod 11


def P004():
    return max_free(30, lambda a, b: abs(a - b) == 5) + 1


def matching(left, right, adj):
    match = {}

    def aug(u, seen):
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                if v not in match or aug(match[v], seen):
                    match[v] = u
                    return True
        return False
    return sum(aug(u, set()) for u in left)


def P005():  # 5x5, setiap kumbang pindah ke petak bertetangga; minimal petak kosong
    cells = [(i, j) for i in range(5) for j in range(5)]
    nb = {c: [(c[0] + di, c[1] + dj) for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
              if 0 <= c[0] + di < 5 and 0 <= c[1] + dj < 5] for c in cells}
    black = [c for c in cells if sum(c) % 2 == 0]
    white = [c for c in cells if sum(c) % 2]
    # kumbang hitam menempati petak putih dan sebaliknya; terisi maksimum = pencocokan maksimum tiap arah
    covered = matching(white, black, nb) + matching(black, white, nb)
    return 25 - covered


def P006():  # kuda dari a1 ke h8 dalam tepat k langkah, 1 <= k <= 23
    moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    reach = {(0, 0)}
    ok = []
    for k in range(1, 24):
        reach = {(x + dx, y + dy) for x, y in reach for dx, dy in moves if 0 <= x + dx < 8 and 0 <= y + dy < 8}
        if (7, 7) in reach:
            ok.append(k)
    return len(ok)


def P007():  # persegi sisi 3: 9 titik saksi berjarak > sqrt2, dan 9 persegi satuan berdiameter sqrt2
    pts = [(1.5 * i, 1.5 * j) for i in range(3) for j in range(3)]
    assert min(dist(p, q) for p, q in combinations(pts, 2)) > 2 ** 0.5
    return len(pts) + 1


def P008():  # 12 bulan x 2 jenis kelamin; pasti ada 5 di kelompok yang sama
    return 24 * 4 + 1


def P009():  # dari 1..100, pasti ada dua yang jumlahnya kelipatan 7 (konflik hanya bergantung pada sisa)
    size = {r: sum(1 for n in range(1, 101) if n % 7 == r) for r in range(7)}
    best = 0
    for chosen in product((0, 1), repeat=7):
        S = [r for r in range(7) if chosen[r]]
        if any((a + b) % 7 == 0 for a, b in combinations(S, 2)):
            continue
        best = max(best, sum(1 if (2 * r) % 7 == 0 else size[r] for r in S))
    return best + 1


def P010():  # dari 1..100, pasti ada dua yang satu membagi yang lain
    witness = list(range(51, 101))
    assert not any(b % a == 0 for a, b in combinations(witness, 2))
    odd_part = lambda n: n // (n & -n)
    houses = {odd_part(n) for n in range(1, 101)}
    assert len(houses) == 50  # dua bilangan dengan bagian ganjil sama: yang kecil membagi yang besar
    return len(witness) + 1


def P011():  # n terkecil: dari n bilangan bulat sembarang pasti ada 3 yang jumlahnya kelipatan 3
    def always(n):
        return all(any(sum(t) % 3 == 0 for t in combinations(ms, 3)) for ms in combinations_with_replacement(range(3), n))
    return next(n for n in range(3, 10) if always(n))


def P012():  # maksimum ubin 1x4 tanpa tumpang tindih pada papan 6x6
    N = 6
    tiles = []
    for i in range(N):
        for j in range(N - 3):
            tiles.append(frozenset((i, j + t) for t in range(4)))
            tiles.append(frozenset((j + t, i) for t in range(4)))
    best = 0

    def go(idx, used, cnt):
        nonlocal best
        best = max(best, cnt)
        if cnt + (N * N - len(used)) // 4 <= best:
            return
        for k in range(idx, len(tiles)):
            if not tiles[k] & used:
                go(k + 1, used | tiles[k], cnt + 1)
    go(0, frozenset(), 0)
    pinwheel = [frozenset((r, c + t) for t in range(4)) for r in (0, 1) for c in (0,)] + \
        [frozenset((r + t, c) for t in range(4)) for c in (4, 5) for r in (0,)] + \
        [frozenset((r, c + t) for t in range(4)) for r in (4, 5) for c in (2,)] + \
        [frozenset((r + t, c) for t in range(4)) for c in (0, 1) for r in (2,)]
    assert len(pinwheel) == 8 and len(frozenset().union(*pinwheel)) == 32  # konstruksi di pembahasan sah
    assert all(0 <= r < N and 0 <= c < N for t in pinwheel for r, c in t)
    return best


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"KO03-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
