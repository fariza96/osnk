# Audit MX2 — Latihan Campuran 2

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
20 soal dari modul 1–19 dengan tekanan pada modul 9–19 (5 per bidang; 6 fondasi, 10 inti, 4 tantangan). Semua soal baru; sebelum ditulis, rancangan dicocokkan dengan pernyataan seluruh bank modul, dan rancangan
yang sama atau terlalu mirip diganti (lihat kolom temuan). Metode A1–A6 sama dengan `audit_TB01.md`.
A5: `python3 scripts/checks/MX2.py` — pencarian lengkap (termasuk semua urutan langkah MX2-015), grid pecahan eksak yang memuat titik kesamaan (MX2-006, MX2-010), sympy (MX2-009), koordinat (MX2-016 sampai MX2-020). Gambar tidak dipakai sebagai bukti.

Keluaran A5 (2026-10-23): 20/20 `OK`.

| ID | Kunci | Modul rujukan | Kesulitan | Temuan | Status |
|---|---|---|---|---|---|
| MX2-001 | 22 | TB03 | foundation | — | verified |
| MX2-002 | 6 | TB04, TB01 | core | rancangan awal ($xy-2x-3y=0$) mirip AL01-E02 → diganti keterbagian polinom | verified |
| MX2-003 | 16 | TB03 | core | rancangan awal (faktor kuadrat sempurna) setipe TB03-E01 → diganti faktor kelipatan 6 | verified |
| MX2-004 | 63 | TB04 | foundation | — | verified |
| MX2-005 | 30 | TB02 | challenge | rancangan awal ($n+S(n)=2026$, lalu $\frac1x+\frac1y=\frac16$) sama dengan TB04-P012 dan AL01-P012 → diganti orde modulo 77 | verified |
| MX2-006 | 8 | AL03 | foundation | — | verified |
| MX2-007 | 11/45 | AL04 | core | rancangan awal (teleskopik akar) mirip AL01-P011 → diganti teleskopik tiga faktor | verified |
| MX2-008 | 2025 | AL05 | core | — | verified |
| MX2-009 | 25 | AL06 | core | `origin: adapted`; bilangan diubah dari bentuk yang dikenal model ($2+8i$) menjadi $1+7i$ | verified |
| MX2-010 | 12 | AL03 | challenge | — | verified |
| MX2-011 | 22 | KO03 | foundation | — | verified |
| MX2-012 | 5/14 | KO04, TB02 | core | — | verified |
| MX2-013 | 81 | KO05 | core | — | verified |
| MX2-014 | 78 | KO04 | core | — | verified |
| MX2-015 | 5 | KO03 | challenge | pembahasan konstruksi awal tidak rapi (memuat percobaan yang gagal) → ditulis ulang dengan konstruksi umum $m=10-k$; nilai akhir yang mungkin dicek dengan pencarian lengkap atas semua urutan langkah | verified |
| MX2-016 | 60 | GE03 | foundation | — | verified |
| MX2-017 | 65/4 | GE03, GE04 | core | — | verified |
| MX2-018 | 22 | GE04 | foundation | — | verified |
| MX2-019 | 85/8 | GE04, GE03 | core | segitiga awal $13,14,15$ sudah dipakai GE04-E01 → diganti $9,10,17$ | verified |
| MX2-020 | 25/4 | GE04, GE03 | challenge | — | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified`.

Keterbatasan: A2 tidak buta; label kesulitan editorial; cakupan belum dicocokkan dengan silabus resmi.
