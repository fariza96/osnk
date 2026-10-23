# Audit KO05 — Induksi, Rekursi, dan Graf Dasar

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/KO05.py`, tanpa memakai rekurensi di pembahasan:
pencarian lengkap barisan/kata (E01, P004, P007), pengubinan (P002, P005), pemasangan tali busur dengan uji perpotongan
(P011, dicocokkan juga dengan pemotongan rekursif); BFS ruang keadaan menara Hanoi ($3^7$ keadaan, P008); Havel–Hakimi
untuk keberadaan graf berderajat yang diberikan (E02, P001); graf sirkulan untuk setiap $k$ genap (P006); rumus Euler
pada $10$ garis acak dengan titik potong yang benar-benar dihitung (P003); untuk P010 batas $\binom k2+\binom{10-k}2$ dan
pengecekan penuh pola yang sama pada $5$ titik ($2^{10}$ graf); untuk P012 pertidaksamaan batas dan konstruksi turnamen.

Keluaran A5 (2026-10-23): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| KO05-E01 | 144 | — | — | verified |
| KO05-E02 | 7 | keberadaan graf berderajat $3^8 4^7$ dicek | — | verified |
| KO05-P001 | 12 | barisan derajat dicek grafis | — | verified |
| KO05-P002 | 19 | — | — | verified |
| KO05-P003 | 56 | `origin: adapted` (folklor) | — | verified |
| KO05-P004 | 149 | kekeliruan umum awal kabur ("posisi yang salah") | diganti dengan kekeliruan konkret (rekurensi Fibonacci → 55) | verified |
| KO05-P005 | 171 | — | — | verified |
| KO05-P006 | 13 | — | — | verified |
| KO05-P007 | 448 | angka kekeliruan umum ($3^6-5\cdot3^4=324$) dihitung ulang | — | verified |
| KO05-P008 | 127 | `origin: adapted` (menara Hanoi); argumen minimal ditulis | — | verified |
| KO05-P009 | 375 | — | — | verified |
| KO05-P010 | 37 | — | — | verified |
| KO05-P011 | 42 | — | — | verified |
| KO05-P012 | 5 | kekeliruan umum awal ($\lfloor28/5\rfloor$) kebetulan menghasilkan kunci | diganti dengan kekeliruan yang menghasilkan $6$ | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified`.

Keterbatasan: A2 tidak buta; label kesulitan editorial. P012 tidak dicek dengan pencarian lengkap atas $2^{28}$ turnamen;
yang dicek adalah batas atas (pertidaksamaan untuk setiap $k$) dan konstruksi untuk $k=5$.
