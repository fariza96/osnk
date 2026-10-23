# Audit KO03 — Prinsip Rumah Merpati dan Invariant

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/KO03.py`. Soal "minimal agar pasti" dihitung
sebagai (konfigurasi terbesar yang belum memenuhi) + 1, dengan pencarian lengkap himpunan bebas (E01, P003, P004),
pencacahan kasus kelas sisa (P009), pencocokan bipartit maksimum (P005), BFS langkah kuda (P006), pencarian lengkap
susunan ubin (P012), dan enumerasi multiset sisa (P011). Untuk P007, P008, P010, komponen bukti dicek: saksi kasus
terburuk (jarak minimum 9 titik; himpunan 51..100 tanpa pasangan saling bagi) dan banyak rumah. Konstruksi kincir P012
dicek `assert`. E02 disimulasikan dengan 2000 urutan acak.

Keluaran A5 (2026-10-23): 14/14 `OK`. Tes tampilan KO03 lulus.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| KO03-E01 | 11 | kedua arah (cukup dan perlu) ditulis | — | verified |
| KO03-E02 | 5039 | — | — | verified |
| KO03-P001 | 3 | — | — | verified |
| KO03-P002 | 7 | stok setiap warna ≥ 2 diperiksa agar kasus terburuk realistis | — | verified |
| KO03-P003 | 12 | — | — | verified |
| KO03-P004 | 16 | — | — | verified |
| KO03-P005 | 1 | konstruksi (dua cincin berpetak genap) dijelaskan | — | verified |
| KO03-P006 | 9 | lintasan 6 langkah dicek per langkah | — | verified |
| KO03-P007 | 10 | — | — | verified |
| KO03-P008 | 97 | — | — | verified |
| KO03-P009 | 46 | ukuran kelas sisa dihitung ulang | — | verified |
| KO03-P010 | 51 | `origin: adapted` (soal klasik folklor) | — | verified |
| KO03-P011 | 5 | `origin: adapted` (kasus n = 3 teorema Erdős–Ginzburg–Ziv) | — | verified |
| KO03-P012 | 8 | — | — | verified |

Kemiripan: E01, P003, P004, P009, P010 sama-sama memilih rumah, dengan jenis rumah berbeda (pasangan, kelas sisa,
rantai, kelas sisa yang saling bermusuhan, bagian ganjil). P005, P006, P012 sama-sama pewarnaan, dengan tuntutan berbeda.

Keterbatasan: A2 tidak buta; label kesulitan editorial. Atribusi sumber P010/P011 berdasarkan pengetahuan umum model.
