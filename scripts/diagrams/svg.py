"""Pembuat diagram geometri SVG sederhana dari koordinat (sumbu y matematika ke atas).
Warna memakai currentColor agar terbaca di tema terang dan gelap."""
import math


class Fig:
    def __init__(self, width=320, pad=28):
        self.width, self.pad = width, pad
        self.items = []   # (jenis, data)
        self.pts = {}

    def point(self, name, xy, label=None, dx=0, dy=0, dot=True):
        self.pts[name] = xy
        self.items.append(("pt", (xy, name if label is None else label, dx, dy, dot)))
        return xy

    def seg(self, p, q, dash=False):
        self.items.append(("seg", (self._p(p), self._p(q), dash)))

    def line(self, p, q, ext=0.25, dash=False, label=None):
        """Garis melalui p, q diperpanjang ext (proporsi) di kedua ujung."""
        (x1, y1), (x2, y2) = self._p(p), self._p(q)
        dx, dy = x2 - x1, y2 - y1
        self.items.append(("seg", ((x1 - ext * dx, y1 - ext * dy), (x2 + ext * dx, y2 + ext * dy), dash)))
        if label:
            self.items.append(("txt", ((x2 + ext * dx, y2 + ext * dy), label, 8, 0)))

    def angle(self, a, v, b, r=0.6, label=None, lr=None):
        """Busur sudut avb (berlawanan arah jarum jam dari va ke vb pada sisi kecil)."""
        self.items.append(("arc", (self._p(a), self._p(v), self._p(b), r, label, lr)))

    def right(self, a, v, b, s=0.35):
        self.items.append(("right", (self._p(a), self._p(v), self._p(b), s)))

    def ticks(self, p, q, n=1):
        self.items.append(("tick", (self._p(p), self._p(q), n)))

    def text(self, xy, s, dx=0, dy=0):
        self.items.append(("txt", (self._p(xy), s, dx, dy)))

    def _p(self, p):
        return self.pts[p] if isinstance(p, str) else p

    # ---- render ----
    def svg(self, title):
        xs, ys = [], []
        for kind, d in self.items:
            if kind == "pt":
                xs.append(d[0][0]); ys.append(d[0][1])
            elif kind == "seg":
                for x, y in d[:2]:
                    xs.append(x); ys.append(y)
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        k = (self.width - 2 * self.pad) / max(x1 - x0, 1e-9)
        h = (y1 - y0) * k + 2 * self.pad
        T = lambda x, y: (round((x - x0) * k + self.pad, 2), round((y1 - y) * k + self.pad, 2))
        unit = k  # 1 satuan koordinat dalam piksel
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {round(h, 2)}" '
               f'width="{self.width}" height="{round(h)}" role="img" aria-label="{title}" '
               f'font-family="serif" font-size="15" fill="none" stroke="currentColor" stroke-width="1.5" '
               f'stroke-linecap="round">']
        for kind, d in self.items:
            if kind == "seg":
                (a, b, dash) = d
                p, q = T(*a), T(*b)
                da = ' stroke-dasharray="5 4"' if dash else ""
                out.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}"{da}/>')
            elif kind == "arc":
                a, v, b, r, label, lr = d
                t1 = math.atan2(a[1] - v[1], a[0] - v[0])
                t2 = math.atan2(b[1] - v[1], b[0] - v[0])
                sweep = (t2 - t1) % (2 * math.pi)
                if sweep > math.pi:
                    t1, t2, sweep = t2, t1, 2 * math.pi - sweep
                P1 = T(v[0] + r * math.cos(t1), v[1] + r * math.sin(t1))
                P2 = T(v[0] + r * math.cos(t1 + sweep), v[1] + r * math.sin(t1 + sweep))
                R = round(r * unit, 2)
                out.append(f'<path d="M{P1[0]} {P1[1]} A{R} {R} 0 0 0 {P2[0]} {P2[1]}" stroke-width="1.2"/>')
                if label:
                    tm = t1 + sweep / 2
                    lrr = lr if lr is not None else r + 0.45
                    L = T(v[0] + lrr * math.cos(tm), v[1] + lrr * math.sin(tm))
                    out.append(f'<text x="{L[0]}" y="{L[1]}" text-anchor="middle" dominant-baseline="middle" '
                               f'fill="currentColor" stroke="none" font-size="13">{label}</text>')
            elif kind == "right":
                a, v, b, s = d
                ua = _unit(a, v); ub = _unit(b, v)
                p1 = (v[0] + s * ua[0], v[1] + s * ua[1]); p3 = (v[0] + s * ub[0], v[1] + s * ub[1])
                p2 = (p1[0] + s * ub[0], p1[1] + s * ub[1])
                pts = " ".join(f"{T(*p)[0]},{T(*p)[1]}" for p in (p1, p2, p3))
                out.append(f'<polyline points="{pts}" stroke-width="1.2"/>')
            elif kind == "tick":
                a, b, n = d
                m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
                u = _unit(b, a); nrm = (-u[1], u[0])
                L = 7 / unit
                for i in range(n):
                    off = (i - (n - 1) / 2) * 5 / unit
                    c = (m[0] + off * u[0], m[1] + off * u[1])
                    p = T(c[0] + L * nrm[0], c[1] + L * nrm[1]); q = T(c[0] - L * nrm[0], c[1] - L * nrm[1])
                    out.append(f'<line x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}" stroke-width="1.2"/>')
        for kind, d in self.items:
            if kind == "pt":
                xy, label, dx, dy, dot = d
                p = T(*xy)
                if dot:
                    out.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="2.6" fill="currentColor" stroke="none"/>')
                if label:
                    out.append(f'<text x="{round(p[0] + dx, 2)}" y="{round(p[1] + dy, 2)}" text-anchor="middle" '
                               f'dominant-baseline="middle" fill="currentColor" stroke="none" font-style="italic">{label}</text>')
            elif kind == "txt":
                xy, s, dx, dy = d
                p = T(*xy)
                out.append(f'<text x="{round(p[0] + dx, 2)}" y="{round(p[1] + dy, 2)}" text-anchor="middle" '
                           f'dominant-baseline="middle" fill="currentColor" stroke="none" font-style="italic">{s}</text>')
        out.append("</svg>")
        return "\n".join(out) + "\n"


def _unit(p, v):
    dx, dy = p[0] - v[0], p[1] - v[1]
    n = math.hypot(dx, dy)
    return dx / n, dy / n
