# Audit TB03 — Faktorisasi Prima dan Banyak Faktor

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/TB03.py` menghitung ulang setiap jawaban
dengan **mendaftar pembagi secara langsung** dan menghitung faktorial secara eksak (banyak nol dibaca dari digit
desimal), bukan dengan rumus $\tau$, $\sigma$, atau Legendre yang dipakai di pembahasan.

Keluaran A5 (2026-10-22): 14/14 `OK`. Tes tampilan TB03 lulus setelah satu perbaikan tata letak (P012).

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| TB03-E01 | 30 | kekeliruan umum versi awal tidak konsisten secara aritmetika | ditulis ulang | verified |
| TB03-E02 | 505 | $v_2\ge v_5$ dijustifikasi | — | verified |
| TB03-P001 | 24 | — | — | verified |
| TB03-P002 | 195 | — | — | verified |
| TB03-P003 | 18 | — | — | verified |
| TB03-P004 | 32 | rentang $2\le n$ dipilih agar $n=1$ (hasil kali $1=1^2$) tidak memicu sengketa | — | verified |
| TB03-P005 | 12 | `origin: adapted` (gagasan AIME 1995 Soal 6, angka diubah) | — | verified |
| TB03-P006 | 2 | kedua nilai $k$ dicek sebagai kubus | — | verified |
| TB03-P007 | 13 | versi awal materi §4 memakai contoh $v_3(30!)$, bahan langsung soal ini | contoh diganti $v_3(50!)$ | verified |
| TB03-P008 | 78 | — | — | verified |
| TB03-P009 | 60 | versi awal materi §1 menjabarkan semua bentuk $\tau(n)=12$ (membocorkan soal) | contoh diganti $\tau(n)=8$ | verified |
| TB03-P010 | 9 | tabel lompatan dicek per baris; $z(205)=50$ memastikan $50$ tercapai | — | verified |
| TB03-P011 | 17 | — | — | verified |
| TB03-P012 | 22 | daftar prima panjang melebar di layar 390 px | dipecah menjadi beberapa `$…$` | verified |

Kemiripan: P009 dan P012 sama-sama memakai pola eksponen dari $\tau(n)$, tetapi arahnya berbeda (bilangan terkecil;
mencacah semua sampai 1000). P004 dan P005 sama-sama memakai pasangan pembagi (hasil kali; simetri di sekitar $n$).

Keterbatasan: A2 tidak buta; label kesulitan editorial. Pengakuan sumber P005 berdasarkan ingatan model tentang
soal AIME 1995 dan belum dicek ke dokumen aslinya (akses web dibatasi).
