#!/usr/bin/env python3
"""Pemeriksaan komputasional AL02. Menghitung ulang setiap jawaban dari pernyataan soal dengan
aljabar eksak (sympy) atau enumerasi, lalu membandingkannya dengan answer_spec di bank soal.
Enumerasi pada rentang hingga hanya memeriksa jawaban, bukan pengganti pembuktian umum."""
import json
import sys
from itertools import product
from pathlib import Path

import sympy as sp

BANK = Path(__file__).resolve().parents[2] / "content/questions/AL02.json"
x, y, z, a, b = sp.symbols("x y z a b")


def E01():  # 3x^2+qx+r berakar a/b dan b/a, dengan a,b akar x^2-7x+3
    r1, r2 = sp.solve(x**2 - 7 * x + 3, x)
    poly = sp.expand(3 * (x - r1 / r2) * (x - r2 / r1))
    q, r = sp.nsimplify(poly.coeff(x, 1)), sp.nsimplify(poly.coeff(x, 0))
    return sp.simplify(q + r)


def E02():  # P(1)=5, P(-3)=-3; sisa oleh x^2+2x-3 = ax+b. Beberapa P berbeda harus memberi sisa yang sama.
    base = sp.interpolate([(1, 5), (-3, -3)], x)
    rems = {sp.rem(sp.expand(base + (x**2 + 2 * x - 3) * h), x**2 + 2 * x - 3, x) for h in (0, 1, x**3 - 7, 5 * x**4 + x)}
    assert len(rems) == 1, rems
    R = sp.Poly(rems.pop(), x)
    return R.coeff_monomial(x) * R.coeff_monomial(1)


def P001():  # bilangan bulat k: x^2+kx+9 tanpa akar real (diskriminan < 0)
    return sum(1 for k in range(-100, 101) if k * k - 36 < 0)


def P002():
    r1, r2 = sp.solve(2 * x**2 - 6 * x + 1, x)
    return sp.simplify(r1**2 + r2**2)


def P003():
    return sp.rem(x**2026 + 3 * x**5 - 2, x + 1, x)


def P004():  # k bulat sehingga semua akar x^2-kx+2k bulat; |k| <= 200 cukup karena (r-2)(s-2)=4
    ks = set()
    for k in range(-200, 201):
        roots = sp.roots(sp.Poly(x**2 - k * x + 2 * k, x))
        if all(rt.is_integer for rt in roots):
            ks.add(k)
    assert ks == {9, 8, 0, -1}, ks
    return sum(ks)


def P005():  # x^3+ax^2+bx-6 habis dibagi x-1 dan x+2; akar ketiga
    P = x**3 + a * x**2 + b * x - 6
    s = sp.solve([P.subs(x, 1), P.subs(x, -2)], [a, b])
    roots = set(sp.roots(sp.Poly(P.subs(s), x))) - {1, -2}
    assert len(roots) == 1, roots
    return roots.pop()


def P006():  # jumlah koefisien pangkat genap dari (2x-1)^5 (x+1)^3
    p = sp.Poly(sp.expand((2 * x - 1) ** 5 * (x + 1) ** 3), x)
    return sum(c for (e,), c in p.terms() if e % 2 == 0)


def P007():  # tripel real terurut dengan x+y+z=6, xy+yz+zx=11, xyz=6
    sols = sp.solve([x + y + z - 6, x * y + y * z + z * x - 11, x * y * z - 6], [x, y, z], dict=True)
    real = {(s[x], s[y], s[z]) for s in sols if all(v.is_real for v in s.values())}
    return len(real)


def P008():  # a sehingga x^2+ax+6 dan x^2+6x+a punya TEPAT satu akar persekutuan (real)
    good = []
    for av in range(-50, 51):
        r1 = set(sp.roots(sp.Poly(x**2 + av * x + 6, x)))
        r2 = set(sp.roots(sp.Poly(x**2 + 6 * x + av, x)))
        if len({r for r in r1 & r2 if r.is_real}) == 1:
            good.append(av)
    assert good == [-7], good
    return good[0]


def P009():  # koefisien x^4 pada (x^2 - 2/x)^5
    return sp.expand((x**2 - 2 / x) ** 5).coeff(x, 4)


def P010():  # (a+b)(b+c)(c+a) untuk akar x^3-6x^2+9x-1 (ketiganya real)
    P = x**3 - 6 * x**2 + 9 * x - 1
    rs = sp.Poly(P, x).nroots(n=40)
    assert all(abs(sp.im(r)) < 1e-30 for r in rs)
    val = (rs[0] + rs[1]) * (rs[1] + rs[2]) * (rs[2] + rs[0])
    v = sp.nsimplify(sp.re(val), tolerance=1e-25, rational=True)
    assert v == P.subs(x, 6), (v, P.subs(x, 6))
    return v


def P011():  # P berderajat 3 dengan P(1)=1, P(2)=2, P(3)=3, P(4)=5; P(6)
    return sp.interpolate([(1, 1), (2, 2), (3, 3), (4, 5)], x).subs(x, 6)


def P012():  # x,y real dengan x^2+y^2=7, x^3+y^3=10; semua nilai x+y
    sols = sp.solve([x**2 + y**2 - 7, x**3 + y**3 - 10], [x, y], dict=True)
    sums = {sp.simplify(s[x] + s[y]) for s in sols if s[x].is_real and s[y].is_real}
    assert sums == {1}, sums
    return sums.pop()


def main():
    bank = {q["id"]: q for q in json.loads(BANK.read_text("utf-8"))} if BANK.exists() else {}
    bad = 0
    for name, fn in [(k, v) for k, v in globals().items() if k[:1] in "EP" and k[1:].isdigit()]:
        qid = f"AL02-{name}"
        got = fn()
        key = bank.get(qid, {}).get("answer_spec", {}).get("value", "—")
        status = "OK" if str(got) == str(key) else "BEDA"
        bad += status != "OK"
        print(f"{qid}: hitung={got} kunci={key} {status}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
