# Audit AL06 — Bilangan Kompleks dan Trigonometri

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/AL06.py`. Aritmetika kompleks eksak (sympy, `I`),
tanpa De Moivre: pangkat dijabarkan langsung (E01, P004, P005), $\omega$ dalam bentuk eksak (E02). P006: sisa pembagian
polinom oleh $x^4+x^3+x^2+x+1$ (berlaku untuk setiap akar ke-5 satuan selain 1) plus cek numerik 50 digit. P003, P008:
semua solusi sistem real. P009: kedua kuadran dengan $\tan x=\frac13$. P007, P010: nilai trigonometri numerik 50 digit
dikenali sebagai pecahan. P011: jumlah binomial langsung. P012: pencarian lengkap atas $2^9$ himpunan bagian.

Keluaran A5 (2026-10-23): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| AL06-E01 | -512 | — | — | verified |
| AL06-E02 | 4 | — | — | verified |
| AL06-P001 | 21 | — | — | verified |
| AL06-P002 | 5 | — | — | verified |
| AL06-P003 | 24/25 | keberadaan $x$ ditunjukkan | — | verified |
| AL06-P004 | 200 | — | — | verified |
| AL06-P005 | 12 | — | — | verified |
| AL06-P006 | 5 | — | — | verified |
| AL06-P007 | 1/8 | — | — | verified |
| AL06-P008 | 5 | — | — | verified |
| AL06-P009 | 7/5 | kekeliruan umum awal kabur | diganti dengan kekeliruan konkret ($\frac{14}9$) | verified |
| AL06-P010 | -1/2 | sudut dalam radian (materi memakai derajat); konversi ditulis di soal | — | verified |
| AL06-P011 | -1024 | — | — | verified |
| AL06-P012 | 176 | rancangan awal (himpunan bagian berukuran kelipatan 3 dari 12 anggota) dapat dijumlah langsung dari 5 binomial, tidak menantang | diganti dengan jumlah anggota habis dibagi 3; pembahasan memuat cek pencacahan | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified`.

Kemiripan dengan materi: bagian pengayaan materi menyebut gagasan P010 dan P011 tanpa angka (sengaja, sebagai teknik).

Keterbatasan: A2 tidak buta; label kesulitan editorial.
