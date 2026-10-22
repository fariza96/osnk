# Audit AL02 — Persamaan dan Polinom Dasar

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/AL02.py` memakai sympy secara eksak
(`solve`, `roots`, `rem`, `interpolate`, penjabaran). E02 diperiksa dengan empat suku banyak berbeda yang
memenuhi syarat soal, dan semuanya harus memberi sisa yang sama. P010 dihitung dari akar numerik 40 digit,
lalu dicocokkan dengan nilai eksak $P(6)$. P004 dan P008 juga dienumerasi pada rentang terbatas.

Keluaran A5 (2026-10-22): 14/14 `OK`. `npm test` 25/25 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| AL02-E01 | −40 | $a,b$ real dan tak nol dicek ($D=37$, $ab=3$) | — | verified |
| AL02-E02 | 6 | — | — | verified |
| AL02-P001 | 11 | batas $k=\pm6$ ($D=0$, akar kembar real) dikecualikan dengan benar | — | verified |
| AL02-P002 | 8 | — | — | verified |
| AL02-P003 | −4 | — | — | verified |
| AL02-P004 | 16 | akar kembar ($k=8$, $k=0$) termasuk karena redaksinya "semua akar bulat"; kebalikan (setiap $k$ memang memberi akar bulat) dicek | — | verified |
| AL02-P005 | −3 | — | — | verified |
| AL02-P006 | 4 | — | — | verified |
| AL02-P007 | 6 | kelengkapan: $x,y,z$ harus merupakan multiset akar polinom, jadi tidak ada solusi lain | — | verified |
| AL02-P008 | −7 | kasus $a=6$ (dua akar persekutuan) dibahas dan dibuang | — | verified |
| AL02-P009 | 40 | — | — | verified |
| AL02-P010 | 53 | tiga akar real dicek (perubahan tanda pada $[0,1]$, $[1,3]$, $[3,5]$), sehingga "bilangan real" sah. Versi awal materi memakai soal ini sebagai pemantik, sehingga triknya terbongkar | pemantik diganti soal E01; contoh §2 diganti $(1-a)(1-b)(1-c)$ | verified |
| AL02-P011 | 16 | — | — | verified |
| AL02-P012 | 1 | jebakan $s=4$ (tidak real) dan $s=-5$ dibuang dengan diskriminan; kekeliruan umum berisi alasan konkret | — | verified |

Kemiripan: E01, P002, P010 sama-sama memakai Vieta, tetapi tuntutannya berbeda (menyusun persamaan baru; ekspresi
simetris langsung; derajat tiga dengan evaluasi $P(t)$). P004 memakai ulang SFFT dari AL01 dalam konteks akar bulat.
E02, P003, P005, P011 memakai teorema sisa/faktor dengan tuntutan berbeda.

Keterbatasan: A2 tidak buta; label kesulitan editorial. Binomial hanya muncul di P009 dan materi §4 karena
$\binom nk$ baru dibahas tuntas di KO02.
