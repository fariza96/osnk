# Audit MX1 — Latihan Campuran 1

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
20 soal dari modul 1–8 (5 per bidang; 6 fondasi, 10 inti, 4 tantangan). Semua soal baru; sebelum ditulis, rancangan dicocokkan dengan pernyataan seluruh bank modul, dan rancangan
yang sama atau terlalu mirip diganti (lihat kolom temuan). Metode A1–A6 sama dengan `audit_TB01.md`.
A5: `python3 scripts/checks/MX1.py` — pencarian lengkap (MX1-004, MX1-011 sampai MX1-015), aritmetika modular langsung, sympy (sistem, sisa pembagian polinom), koordinat pada dua bentuk segitiga/jajargenjang (MX1-016, MX1-018, MX1-020), objek `Triangle` (MX1-017, MX1-019). Gambar tidak dipakai sebagai bukti.

Keluaran A5 (2026-10-23): 20/20 `OK`.

| ID | Kunci | Modul rujukan | Kesulitan | Temuan | Status |
|---|---|---|---|---|---|
| MX1-001 | 21 | TB01 | foundation | — | verified |
| MX1-002 | 3 | TB02 | core | kekeliruan umum awal (Fermat kecil) kebetulan menghasilkan kunci → diganti | verified |
| MX1-003 | 33 | TB02, TB01 | core | — | verified |
| MX1-004 | 75 | TB02, AL01 | core | kedua arah (mustahil mod 4, konstruksi) ditulis | verified |
| MX1-005 | 123 | TB02 | challenge | rancangan awal (pasangan dengan KPK 72) sama dengan TB01-P009 → diganti sistem kongruensi | verified |
| MX1-006 | 13 | AL01 | foundation | — | verified |
| MX1-007 | 95 | AL02, AL01 | core | — | verified |
| MX1-008 | 18 | AL02 | core | rancangan awal (akar polinom, tanya $a+b$) terjawab langsung oleh $P(1)=0$ dan mirip AL02-P005 → diganti teorema sisa | verified |
| MX1-009 | 39 | AL01, AL02 | challenge | — | verified |
| MX1-010 | 1 | AL01 | core | — | verified |
| MX1-011 | 48 | KO01 | foundation | — | verified |
| MX1-012 | 12 | KO02 | core | — | verified |
| MX1-013 | 570 | KO01, KO02 | core | — | verified |
| MX1-014 | 20 | KO02 | core | — | verified |
| MX1-015 | 112 | KO02 | challenge | — | verified |
| MX1-016 | 115 | GE01 | foundation | — | verified |
| MX1-017 | 4 | GE01 | foundation | — | verified |
| MX1-018 | 5 | GE02 | core | rancangan awal (trapesium + diagonal) mirip GE02-E01 → diganti jajargenjang | verified |
| MX1-019 | 3 | GE01 | foundation | versi 1 sama/terlalu mirip dengan GE01-P007 (ditemukan audit lintas bank Tahap 5) → diganti, diaudit ulang (versi 2) | verified |
| MX1-020 | 8 | GE02 | challenge | — | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified`.

Keterbatasan: A2 tidak buta; label kesulitan editorial; cakupan belum dicocokkan dengan silabus resmi.
