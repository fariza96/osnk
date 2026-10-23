# Audit DG — Diagnostik

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
16 soal sebelum program (4 per bidang, kebanyakan fondasi) untuk memetakan bidang lemah. Semua soal baru; sebelum ditulis, rancangan dicocokkan dengan pernyataan seluruh bank modul, dan rancangan
yang sama atau terlalu mirip diganti (lihat kolom temuan). Metode A1–A6 sama dengan `audit_TB01.md`.
A5: `python3 scripts/checks/DG.py` — pencacahan langsung, aritmetika eksak, sympy (Vieta, rasionalisasi), koordinat untuk DG-013 sampai DG-016 (dua bentuk segitiga untuk DG-015). Gambar tidak dipakai sebagai bukti.

Keluaran A5 (2026-10-23): 16/16 `OK`.

| ID | Kunci | Modul rujukan | Kesulitan | Temuan | Status |
|---|---|---|---|---|---|
| DG-001 | 8 | TB01 | foundation | — | verified |
| DG-002 | 294 | TB01 | foundation | — | verified |
| DG-003 | 2 | TB02 | foundation | rancangan awal (angka satuan $7^{2026}$) hampir sama dengan TB02-P002 → diganti sisa $2^{100}$ mod 7; kekeliruan umum awal kebetulan menghasilkan kunci → diganti | verified |
| DG-004 | 24 | TB03 | core | — | verified |
| DG-005 | 29 | AL01 | foundation | — | verified |
| DG-006 | 37/4 | AL02 | foundation | — | verified |
| DG-007 | 2 | AL01 | foundation | — | verified |
| DG-008 | 5 | AL03 | core | — | verified |
| DG-009 | 648 | KO01 | foundation | — | verified |
| DG-010 | 52 | KO02 | core | — | verified |
| DG-011 | 48 | KO02 | foundation | — | verified |
| DG-012 | 1/12 | KO04 | foundation | — | verified |
| DG-013 | 36/5 | GE01, GE02 | foundation | — | verified |
| DG-014 | 110 | GE01 | foundation | — | verified |
| DG-015 | 6 | GE02 | foundation | — | verified |
| DG-016 | 13/2 | GE03, GE01 | core | — | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified`.

Keterbatasan: A2 tidak buta; label kesulitan editorial; cakupan belum dicocokkan dengan silabus resmi.
