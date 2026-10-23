# Audit AL05 — Fungsi dan Persamaan Fungsi

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/AL05.py`. Untuk persamaan fungsi, nilai yang
ditanya dihitung dari sistem persamaan hasil substitusi (sympy), lalu calon fungsi diverifikasi simbolik ke persamaan semula
(E01, E02, P007, P008, P009, P011), sehingga keberadaan fungsi juga terbukti. P004 memakai fungsi konkret
$f(x)=3v_2(x)+5v_3(x)$ yang dicek sifat perkaliannya pada semua pecahan $\frac nd$, $n,d\le12$. P010 membangun $f$ dari
$f(0)$ dan rekursi pada $[-60,60]$, mengecek persamaan semula pada $[-25,25]^2$, lalu mencari titik tetap. P005, P012:
pencarian lengkap atas $4^4$ fungsi. P006: iterasi $2026$ kali dengan pecahan eksak.

Keluaran A5 (2026-10-23): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| AL05-E01 | -1 | keberadaan $f$ ditunjukkan ($f(x)=\frac2x-x$) | — | verified |
| AL05-E02 | 7/4 | — | — | verified |
| AL05-P001 | -5 | — | — | verified |
| AL05-P002 | 7/2 | — | — | verified |
| AL05-P003 | 31 | — | — | verified |
| AL05-P004 | 11 | rancangan awal berdomain bilangan real positif; keberadaan fungsi dengan $f(2)=3$, $f(3)=5$ di sana butuh basis Hamel | domain diganti bilangan rasional positif, contoh fungsi ditulis di pembahasan | verified |
| AL05-P005 | 10 | — | — | verified |
| AL05-P006 | -1/2 | gagasan periodik mirip AL04-P008; sudut pandangnya komposisi fungsi | — | verified |
| AL05-P007 | 2027 | `origin: adapted` (folklor) | — | verified |
| AL05-P008 | 15 | — | — | verified |
| AL05-P009 | -6 | kedua kasus $a=\pm2$ dicek | — | verified |
| AL05-P010 | -1 | `origin: adapted` (folklor); rumus berlaku juga untuk $n$ negatif | — | verified |
| AL05-P011 | 3/4 | keberadaan $f$ diverifikasi simbolik | — | verified |
| AL05-P012 | 41 | — | — | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified`.

Keterbatasan: A2 tidak buta; label kesulitan editorial. Atribusi P007/P010 berdasarkan pengetahuan umum model.
