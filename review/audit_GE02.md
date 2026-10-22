# Audit GE02 — Kesebangunan, Perbandingan, dan Luas

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/GE02.py` membangun setiap konfigurasi dengan
koordinat eksak (sympy) dari data soal. Bila hasil tidak bergantung pada bentuk (posisi puncak, pergeseran alas,
tinggi), soal dicek pada dua bentuk berbeda dan hasilnya harus sama. Untuk E01, panjang $DC$ dan tinggi tidak
dianggap diketahui; keduanya diselesaikan dari dua syarat luas. Untuk P006, $D$ dicari dari syarat sudut (bukan dari
rumus kesebangunan). Klaim pendukung di pembahasan juga dicek dengan `assert`: $O$ titik tengah $PQ$ (P008),
$F$ titik tengah $AD$ (P010), $\angle AGB=90^\circ$ dan $BG:GF=2:3$ (P011). Diagram dibuat dari koordinat oleh
`scripts/diagrams/GE02.py` dan diperiksa secara visual sekali; gambar tidak dijadikan bukti.

Keluaran A5 (2026-10-22): 14/14 `OK`. `npm test` 29/29 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| GE02-E01 | 100 | — | — | verified |
| GE02-E02 | 39 | — | — | verified |
| GE02-P001 | 21 | — | — | verified |
| GE02-P002 | 75 | — | — | verified |
| GE02-P003 | 18 | — | — | verified |
| GE02-P004 | 4 | syarat sudut $B,C$ lancip ditambahkan agar persegi muat; hasil tidak bergantung pada posisi $A$ (dicek dua bentuk) | — | verified |
| GE02-P005 | 30 | — | — | verified |
| GE02-P006 | 5 | contoh urutan titik di materi §1 versi awal persis $\triangle ABD\sim\triangle ACB$ (membocorkan soal) | contoh materi dan kekeliruan umum diganti | verified |
| GE02-P007 | 25 | syarat "konveks" ditambahkan agar dekomposisi pojok sah | — | verified |
| GE02-P008 | 12 | — | — | verified |
| GE02-P009 | 24 | — | — | verified |
| GE02-P010 | 10 | diselesaikan tanpa Menelaus (dipindah ke GE04), memakai garis bantu sejajar + garis tengah | — | verified |
| GE02-P011 | 20 | kekeliruan umum versi awal menyebut $BG:GF=1:4$ (salah); dihitung ulang eksak $2:3$ | diperbaiki, dicek `assert` | verified |
| GE02-P012 | 13 | — | — | verified |

Kemiripan: E01 dan P008 sama-sama trapesium dengan perpotongan diagonal, tetapi tuntutannya berbeda (luas; panjang
ruas sejajar). P009 dan P012 memakai homotetri kaki trapesium (tinggi; pembagi luas). P003 dan P005 sama-sama
rasio luas bertinggi sama (satu langkah; dua langkah).

Keterbatasan: A2 tidak buta; label kesulitan editorial. Pemeriksaan visual diagram dilakukan model yang sama.
