# Audit KO02 — Permutasi dan Kombinasi

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/KO02.py` menghitung setiap jawaban dengan
**enumerasi langsung** (semua permutasi/kombinasi/lintasan/solusi didaftar dengan `itertools`), bukan dengan rumus
di pembahasan. Susunan melingkar dinormalkan terhadap putaran sebelum dihitung.

Keluaran A5 (2026-10-22): 14/14 `OK`. Tes tampilan konten 14/14 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| KO02-E01 | 14400 | pemeriksaan kasus kecil (2+2) ditambahkan di pembahasan | — | verified |
| KO02-E02 | 220 | — | — | verified |
| KO02-P001 | 210 | — | — | verified |
| KO02-P002 | 151200 | banyak huruf MATEMATIKA dicek (M2, A3, T2, E, I, K) | — | verified |
| KO02-P003 | 240 | redaksi "putaran dianggap sama" eksplisit; pencerminan tidak disamakan | — | verified |
| KO02-P004 | 432 | dicek ulang dengan komplemen di pembahasan | — | verified |
| KO02-P005 | 186 | dicek ulang per kasus | — | verified |
| KO02-P006 | 36 | urutan $(2,2)$ sebelum $(4,3)$ dijelaskan | — | verified |
| KO02-P007 | 165 | batas atas digit dibuktikan tidak aktif | — | verified |
| KO02-P008 | 120 | bijeksi dua arah dinyatakan | — | verified |
| KO02-P009 | 144 | — | — | verified |
| KO02-P010 | 28 | himpunan pelanggar saling lepas dibuktikan; dicek ulang dengan penjumlahan langsung | — | verified |
| KO02-P011 | 5120 | — | — | verified |
| KO02-P012 | 50 | pasangan $A_{10}A_1$ bertetangga ditegaskan; dicek dengan simetri | — | verified |

Kemiripan: E01, P004, P008, P012 sama-sama memakai celah, dengan tuntutan berbeda (baris; blok + celah; bijeksi
pergeseran; lingkaran dengan pembagian kasus). E02, P007, P010 memakai bintang-sekat (batas bawah; bijeksi digit;
batas atas). Inklusi-eksklusi penuh tidak dipakai (KO04); P010 hanya memakai komplemen dengan pelanggar yang saling lepas.

Keterbatasan: A2 tidak buta; label kesulitan editorial. P011 (menghitung dua cara) adalah pengayaan.
