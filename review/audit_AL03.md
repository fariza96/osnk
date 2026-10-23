# Audit AL03 — Pertidaksamaan Dasar dan Nilai Ekstrem

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/AL03.py` memeriksa setiap soal nilai ekstrem
**dua arah**: (1) nilai kunci dicapai secara eksak (sympy) di titik kesamaan yang disebut pembahasan; (2) pencarian
acak 200 000 titik (seed tetap) pada daerah yang sah tidak menemukan nilai yang lebih baik. Arah (2) hanya bukti
numerik; batasnya dibuktikan di pembahasan. P007 juga mengecek akar real di titik optimum. Soal pencacahan
(P003, P009) dienumerasi, P006 dicek pada kisi seperempatan.

Keluaran A5 (2026-10-23): 14/14 `OK`. `npm test` 33/33 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| AL03-E01 | 12 | — | — | verified |
| AL03-E02 | 6 | — | — | verified |
| AL03-P001 | 5 | — | — | verified |
| AL03-P002 | 18 | — | — | verified |
| AL03-P003 | 14 | — | — | verified |
| AL03-P004 | 7 | titik kritis tunggal dicek sympy | — | verified |
| AL03-P005 | 16 | — | — | verified |
| AL03-P006 | 11 | kekeliruan umum versi awal ($x=5{,}25$) justru memberi nilai minimum, jadi bukan kesalahan | ditulis ulang | verified |
| AL03-P007 | 8 | jebakan puncak di luar daerah asal; akar kembar di $k=-2$ diterima karena redaksi "boleh sama" | — | verified |
| AL03-P008 | 9 | — | — | verified |
| AL03-P009 | 10 | — | — | verified |
| AL03-P010 | 1/432 | jawaban pecahan (`rational`) | — | verified |
| AL03-P011 | 3/2 | versi awal bertipe `integer` (tertangkap validator) | diubah ke `rational` | verified |
| AL03-P012 | 24 | ketiga syarat kesamaan konsisten dengan $xyz=1$ dicek | — | verified |

Kemiripan: E01, P002, P005, P010, P012 sama-sama AM-GM, dengan tuntutan berbeda (memecah suku; dua suku langsung;
koefisien; pemecahan berbobot; per faktor). E02, P008, P011 memakai Cauchy-Schwarz/Titu dengan bentuk berbeda.

Keterbatasan: A2 tidak buta; label kesulitan editorial. Pengecekan "tidak ada nilai lebih baik" bersifat numerik.
