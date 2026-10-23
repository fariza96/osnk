# Audit GE04 — Koordinat dan Hubungan Metrik

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/GE04.py` membangun setiap konfigurasi dengan
koordinat eksak sympy dari data soal dan menghitung besaran yang ditanya tanpa rumus pembahasan (Heron, Ceva,
Menelaus, aturan sinus/kosinus tidak dipakai; luas dari poligon, jari-jari dari objek `Triangle`, perpotongan dari
`Line`). Bagian konfigurasi yang bebas divariasikan pada dua bentuk: bentuk segitiga (P004, P012) dan posisi $P$ (P007,
dengan persegi panjang nyata yang memenuhi $PA=3$, $PB=4$, $PC=5$ dan $P$ di dalam). P005 mencari kedua titik singgung
secara eksplisit. P012 juga mengecek $F$ terletak pada sisi $AB$. Diagram dibuat dari koordinat oleh
`scripts/diagrams/GE04.py` dan diperiksa visual.

Keluaran A5 (2026-10-23): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| GE04-E01 | 4 | — | — | verified |
| GE04-E02 | 15 | dicek juga dengan pengurangan tiga segitiga pojok | — | verified |
| GE04-P001 | 20 | segi empat dicek cembung; angka kekeliruan umum (urutan menyilang → 1) dicek | — | verified |
| GE04-P002 | 7 | data awal ($5$, $8$, $60^\circ$) sama dengan contoh $5,7,8$ di materi | diganti $3$, $5$, $120^\circ$ | verified |
| GE04-P003 | 42 | — | — | verified |
| GE04-P004 | 4 | — | — | verified |
| GE04-P005 | 12 | — | — | verified |
| GE04-P006 | 7 | — | — | verified |
| GE04-P007 | 18 | diagram awal: $P$ hampir pada diagonal $AC$ (menyesatkan) | koordinat diagram diganti | verified |
| GE04-P008 | 8 | — | — | verified |
| GE04-P009 | 169/3 | — | — | verified |
| GE04-P010 | 5 | — | — | verified |
| GE04-P011 | 6 | — | — | verified |
| GE04-P012 | 12 | rancangan awal ($BD:DC=1:2$, luas $60$) memberi kunci yang sama dengan anggapan keliru "$P$ titik berat" | diganti $1:3$, luas $80$ (anggapan keliru memberi $\frac{40}3$) | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified` (satu putaran).

Kemiripan: P003, P008, E01 sama-sama Heron dengan tuntutan berbeda (luas, garis tinggi terpendek, $r$). P006 dan P011
sama-sama "sudut bersama"; P011 menambah teorema garis bagi. P004 dan P012 sama-sama Menelaus; P012 menambah Ceva dan
perbandingan luas.

Keterbatasan: A2 tidak buta; label kesulitan editorial. P007 `origin: adapted` (teorema bendera Inggris, folklor).
