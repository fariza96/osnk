# Audit KO01 — Aturan Penjumlahan dan Perkalian

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/KO01.py` mengenumerasi **seluruh** ruang
objek langsung dari pernyataan soal (semua bilangan, semua himpunan bagian, semua pewarnaan). Ini pemeriksaan
lengkap, bukan sampel.

Keluaran A5 (2026-10-22): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| KO01-E01 | 328 | pemeriksaan kedua lewat komplemen ada di pembahasan | — | verified |
| KO01-E02 | 3168 | — | — | verified |
| KO01-P001 | 676000 | — | — | verified |
| KO01-P002 | 256 | — | — | verified |
| KO01-P003 | 48 | `\"` tampil sebagai backslash di petunjuk | dibetulkan; validator kini menolak `\"` | verified |
| KO01-P004 | 584 | — | — | verified |
| KO01-P005 | 6 | keenam pewarnaan didaftar di pembahasan | — | verified |
| KO01-P006 | 992 | — | — | verified |
| KO01-P007 | 2048 | `\"` di petunjuk | dibetulkan | verified |
| KO01-P008 | 1288 | batas "> 5000" dicek: 5000 tidak berdigit berbeda | — | verified |
| KO01-P009 | 993 | kekeliruan umum kabur | ditulis ulang | verified |
| KO01-P010 | 55 | kelengkapan kumpulan digit untuk 4 digit dijelaskan | — | verified |
| KO01-P011 | 240 | — | — | verified |
| KO01-P012 | 90 | — | — | verified |

Keterbatasan: A2 tidak buta; label kesulitan editorial.
