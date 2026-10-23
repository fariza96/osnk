# Audit GE03 — Lingkaran

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/GE03.py` membangun setiap konfigurasi dengan
koordinat sympy dari data soal. Data yang diberikan (mis. $\angle ABC=110^\circ$, $\angle ACD=40^\circ$ pada E01;
sudut singgung $62^\circ$ pada P004) dicek berlaku pada konfigurasi itu, lalu besaran yang ditanya dihitung. Bagian
konfigurasi yang bebas (pembagian busur $AB/BC$ pada E01, posisi $C$ pada P001, arah tali busur/garis potong pada
P002/P006, kemiringan garis singgung persekutuan pada P009) divariasikan pada dua bentuk dan hasilnya harus sama.
P011 dicacah dari rumus panjang tali busur sebagai fungsi sudut. Thales pada P012 dicek dengan `assert`.
Diagram dibuat dari koordinat oleh `scripts/diagrams/GE03.py` (lingkaran ditambahkan ke `svg.py`; diagram lama tidak
berubah) dan diperiksa visual sekali.

Keluaran A5 (2026-10-23): 14/14 `OK`. `npm test` 38/38 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| GE03-E01 | 70 | konsistensi data dicek dengan busur di pembahasan | — | verified |
| GE03-E02 | 5 | — | — | verified |
| GE03-P001 | 65 | — | — | verified |
| GE03-P002 | 11 | — | — | verified |
| GE03-P003 | 12 | — | — | verified |
| GE03-P004 | 48 | letak $X$ (sisi berlawanan $C$) ditegaskan di redaksi agar sudut singgung tidak ambigu | — | verified |
| GE03-P005 | 6 | — | — | verified |
| GE03-P006 | 9 | — | — | verified |
| GE03-P007 | 65/8 | jawaban pecahan (`rational`) | — | verified |
| GE03-P008 | 4 | — | — | verified |
| GE03-P009 | 8 | — | — | verified |
| GE03-P010 | 40 | — | — | verified |
| GE03-P011 | 16 | `origin: adapted` (gagasan soal klasik; angka dipilih ulang); kedua ujung rentang hanya satu tali busur | — | verified |
| GE03-P012 | 15/2 | jawaban pecahan (`rational`) | — | verified |

Kemiripan: E02, P002, P006, P009, P011 sama-sama kuasa titik, dengan bentuk berbeda (singgung–potong; tali busur;
dua garis potong; sumbu radikal; pencacahan). P008 dan P012 sama-sama Thales (garis tinggi; diameter lingkaran luar).

Keterbatasan: A2 tidak buta; label kesulitan editorial. Pemeriksaan visual diagram dilakukan model yang sama.
