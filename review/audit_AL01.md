# Audit AL01 — Identitas dan Faktorisasi

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/AL01.py` memakai aritmetika eksak
(sympy `solve` untuk sistem simetris, `factorint`, `Fraction`), akar real polinom untuk P010, dan enumerasi
untuk soal bilangan bulat. Untuk P003 dan P011, jumlah akar dihitung numerik dengan 40 digit, lalu dicocokkan dengan pecahan eksak.

Keluaran A5 (2026-10-22): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| AL01-E01 | 47 | — | — | verified |
| AL01-E02 | 6 | kasus faktor negatif dibahas dan terbukti kosong | — | verified |
| AL01-P001 | −1 | — | — | verified |
| AL01-P002 | 133 | — | — | verified |
| AL01-P003 | 9 | — | — | verified |
| AL01-P004 | 3 | syarat paritas faktor dijelaskan | — | verified |
| AL01-P005 | 63 | dua pasangan $(a,b)$ memberi nilai yang sama, dan keduanya dicek | — | verified |
| AL01-P006 | 14 | — | — | verified |
| AL01-P007 | 181 | keprimaan 181 dicek sampai 13 | — | verified |
| AL01-P008 | 7 | $x,y$ real dicek | — | verified |
| AL01-P009 | 2025 | kekeliruan umum versi awal kontradiktif | ditulis ulang | verified |
| AL01-P010 | 92 | ketiga akar real dicek (perubahan tanda), sehingga "bilangan real" sah | — | verified |
| AL01-P011 | 9/10 | jawaban pecahan (tipe `rational`, pecahan senilai diterima); kekeliruan umum versi awal bukan kesalahan nyata | ditulis ulang | verified |
| AL01-P012 | 17 | solusi palsu $(0,0)$ dari perkalian dengan $xy$ dibahas | — | verified |

Kemiripan: E02, P006, dan P012 sama-sama memakai SFFT, tetapi berbeda tuntutannya (banyak solusi dengan kasus
tanda; jumlah nilai dengan batas dua arah; kedua tanda dan pengecualian). P003 dan P011 sama-sama teleskopik;
P011 memerlukan pemfaktoran penyebut lebih dulu.

Keterbatasan: A2 tidak buta; label kesulitan editorial.
