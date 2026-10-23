# Audit AL04 — Barisan, Deret, dan Rekursi

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/AL04.py` menghitung ulang setiap jawaban
langsung dari pernyataan soal dengan pecahan eksak (menjumlah/mengalikan suku satu per satu, mengiterasi rekursi
2026 langkah), bukan dengan bentuk tertutup di pembahasan. P002 dan P004 diselesaikan dengan sympy, termasuk
pengecekan bahwa solusinya tunggal ($r$ real; $|r|<1$). P010 dihitung eksak lewat rumus Binet (cara berbeda dari
pembahasan) dan dicocokkan dengan jumlah parsial 200 suku. P007 mengecek bahwa hanya $b=2$ yang memenuhi syarat naik.

Keluaran A5 (2026-10-23): 14/14 `OK`. `npm test` 42/42 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| AL04-E01 | 101/200 | kekeliruan umum versi awal menyebut hasil $\frac{101}{100}$ yang tidak muncul dari kekeliruan itu | ditulis ulang | verified |
| AL04-E02 | 5 | — | — | verified |
| AL04-P001 | 62 | — | — | verified |
| AL04-P002 | 1458 | "bilangan real" ditambahkan agar $r=3$ tunggal | — | verified |
| AL04-P003 | 70336 | versi awal materi (kekeliruan umum 1) memakai angka persis soal ini (105 sampai 994) | contoh materi diganti | verified |
| AL04-P004 | 6 | — | — | verified |
| AL04-P005 | 25 | — | — | verified |
| AL04-P006 | 731 | — | — | verified |
| AL04-P007 | 105 | $b=-10$ dibuang oleh syarat "naik" (dinyatakan di redaksi) | — | verified |
| AL04-P008 | −6 | — | — | verified |
| AL04-P009 | 99 | versi awal materi §3 memuat $2k+1=(k+1)^2-k^2$ (kunci langsung soal ini) | poin itu dihapus dari materi | verified |
| AL04-P010 | 2 | konvergensi dibuktikan ($F_n\le(5/3)^n$) sebelum memanipulasi deret | — | verified |
| AL04-P011 | 45/91 | — | — | verified |
| AL04-P012 | 15 | — | — | verified |

Kemiripan: E01, P005, P009, P011 sama-sama teleskopik dengan bentuk berbeda (hasil kali; pecahan parsial dengan
syarat ketaksamaan; selisih kuadrat; pemfaktoran derajat empat). E02 dan P008 sama-sama periodik (jumlah; hasil kali).

Keterbatasan: A2 tidak buta; label kesulitan editorial.
