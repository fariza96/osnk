# Audit KO04 — Pencacahan Lanjutan dan Peluang

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/KO04.py` menghitung setiap jawaban dengan
pencarian lengkap pada ruang sampel yang sama mungkin (pecahan eksak `Fraction`), terpisah dari rumus di pembahasan:
penyaringan $1..N$ (E01, P004), semua $2^{10}$ barisan koin (E02), semua $6^3$ lemparan (P003), DP lintasan grid
(P005), semua $3^5$ fungsi (P006), semua $\binom{12}4$ pilihan bola (P007), semua $8!$ susunan kursi (P008), semua
$\binom{10}3$ tripel (P009), semua $5!$ dan $6!$ permutasi (P010, P011), semua susunan $\mathrm{AABBCC}$ (P012).

Keluaran A5 (2026-10-23): 14/14 `OK`.

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| KO04-E01 | 266 | — | — | verified |
| KO04-E02 | 9/4 | contoh barisan di soal dicek memuat tepat 3 kemunculan AA | — | verified |
| KO04-P001 | 8 | — | — | verified |
| KO04-P002 | 5/12 | — | — | verified |
| KO04-P003 | 21/2 | kekeliruan umum awal ("rata-rata nilai terkecil dan terbesar") kebetulan menghasilkan kunci | diganti dengan kekeliruan yang menghasilkan jawaban salah ($9$) | verified |
| KO04-P004 | 220 | angka kekeliruan umum (irisan = hasil kali → 250) dihitung ulang | — | verified |
| KO04-P005 | 84 | — | — | verified |
| KO04-P006 | 150 | — | — | verified |
| KO04-P007 | 6/11 | kekeliruan umum menyebut 540 "lebih dari separuh ruang sampel"; 540 > 495 | redaksi diperbaiki | verified |
| KO04-P008 | 32/7 | — | — | verified |
| KO04-P009 | 1/6 | — | — | verified |
| KO04-P010 | 3/8 | "tepat dua benar" diganti "tepat satu benar" agar kunci tidak sama dengan P009; kekeliruan umum ditulis ulang agar jelas; `origin: adapted` (masalah amplop, folklor) | — | verified |
| KO04-P011 | 49/20 | `origin: adapted` (rekor permutasi acak, folklor) | — | verified |
| KO04-P012 | 30 | kekeliruan umum menulis $90-90<0$; yang benar $=0$ | diperbaiki | verified |

Semua perbaikan terjadi sebelum butir pertama kali berstatus `verified` (satu putaran).

Kemiripan dengan materi: contoh materi memakai bilangan/konfigurasi lain (kelipatan 2 atau 3 sampai 100; lintasan ke
$(4,3)$ menghindari $(2,1)$; titik tetap permutasi). Teknik "setiap jenis muncul" dan "blok" dijelaskan tanpa contoh
angka agar P006 dan P012 tidak bocor. KO02-P010 (batas atas bintang-sekat) tidak diulang.

Keterbatasan: A2 tidak buta; label kesulitan editorial. Atribusi P010/P011 berdasarkan pengetahuan umum model.
