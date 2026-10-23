# PROJECT_STATE

Terakhir diperbarui: 2026-10-23 (sesi 2).

## Tahap

- [x] Tahap 0 — lingkungan, sumber, kredit
- [x] Tahap 1 — blueprint, rencana 8 minggu, skema, standar audit, platform, kerangka proyek + tes
- [x] Tahap 2 — **pilot TB01 + GE01 selesai**: 2 materi, 4 contoh, 24 latihan, semuanya `verified`
- [x] Tahap 3 — volume dipertahankan (12 latihan/modul); biaya aktual US$11 setelah pilot, proyeksi di `costs/cost_log.md`
- [ ] Tahap 4 — produksi: **12/19 modul selesai** (versi inti 8 modul lengkap + TB03, AL03, KO03, GE03)
- [ ] Tahap 5–6

## Lingkungan

| Hal | Temuan |
|---|---|
| Produk | Claude Code di cloud; kontainer sementara |
| Alat | Python 3.13 + sympy 1.13.3, Node 22, Chromium (Playwright), git |
| Jaringan | hanya npm & PyPI; Puspresnas/CDN diblokir |
| Kredit | `ccr_promotional`, reset/berakhir 2026-11-05 08:00 UTC; biaya tidak terlihat dari dalam sesi |
| GitHub | terhubung ke `fariza96/osnk` (privat), cabang `main`, sejak 22 Okt 2026 |

## Keputusan

- Silabus: peta materi guru (berbasis silabus tak resmi Evan Chen 2023), dibaca 22 Okt 2026 → `docs/sources.md`, `docs/blueprint.md` §3a.
- Format jawaban: isian singkat bilangan bulat (sesuai peta guru).
- Penyimpanan: repositori GitHub privat `fariza96/osnk`.
- MathJax 4.1.2 + font NewCM dibundel lokal (pemecahan baris otomatis untuk ponsel; berjalan tanpa internet, sudah diuji).
- Pages: workflow `.github/workflows/pages.yml` berjalan **otomatis setiap push ke `main`** dan tetap bisa manual
  (`workflow_dispatch`), disetujui guru 23 Okt 2026. Setiap push ke `main` = situs terbit. Versi yang terbit tampil di
  footer situs ("Versi <sha>") dan di ringkasan run Actions. Sebelumnya hanya manual, sehingga situs tertahan di `1e769c0`.
- **19 modul** (AL05 fungsi, KO05 induksi/rekursi/graf, AL06 kompleks & trigonometri ditambahkan, disetujui guru);
  program 10 minggu. Sasaran lengkap: 228 latihan modul + 16 diagnostik + 40 campuran = **284 soal unik**, plus 38 contoh.
- Repositori: `fariza96/osnk` (privat), `main`. Setiap batch di-commit dan di-push.

## Selesai (ID)

- TB01: materi `content/modules/TB01.md`; `TB01-E01..E02`, `TB01-P001..P012`: verified.
- GE01: materi `content/modules/GE01.md`; `GE01-E01..E02`, `GE01-P001..P012`: verified; diagram E01, E02, P001, P004, P010.
- AL01: materi + `AL01-E01..E02`, `AL01-P001..P012`: verified.
- KO01: materi + `KO01-E01..E02`, `KO01-P001..P012`: verified.
- TB02: materi + `TB02-E01..E02`, `TB02-P001..P012`: verified.
- AL02: materi + `AL02-E01..E02`, `AL02-P001..P012`: verified.
- KO02: materi + `KO02-E01..E02`, `KO02-P001..P012`: verified.
- TB03: materi + `TB03-E01..E02`, `TB03-P001..P012`: verified (P005 `adapted`).
- AL03: materi + `AL03-E01..E02`, `AL03-P001..P012`: verified (P010, P011 `rational`).
- KO03: materi + `KO03-E01..E02`, `KO03-P001..P012`: verified (P010, P011 `adapted`).
- GE03: materi + `GE03-E01..E02`, `GE03-P001..P012`: verified; diagram E01, E02, P004, P009, P010, P012 (`scripts/diagrams/GE03.py`).
- GE02: materi + `GE02-E01..E02`, `GE02-P001..P012`: verified; diagram E01, E02, P004, P006, P008, P010, P011 (`scripts/diagrams/GE02.py`).
- Audit: `review/audit_<MODUL>.md` untuk kedua belas modul. Pemeriksaan: `npm run check:math` (168/168 cocok).
- Lingkungan sesi baru: `npm ci` dan `pip install sympy==1.13.3` (sympy tidak terpasang bawaan).
- Tes: `npm test` (penilai, validator, build, situs fixture, dan tampilan konten nyata per modul) lulus.

Mutu kumulatif: 168 butir; batch GE03: 0 temuan yang mengubah kunci, 0 kunci salah; batch KO03: 0 temuan yang mengubah kunci, 0 kunci salah; batch AL03: 2 temuan (kekeliruan umum P006 bukan kesalahan; tipe jawaban P011), 0 kunci salah; batch TB03: 4 temuan (2 contoh materi membocorkan soal, 1 kekeliruan umum tidak konsisten, 1 tata letak), 0 kunci salah; batch GE02: 2 temuan (contoh materi membocorkan P006; klaim rasio salah di kekeliruan umum P011), keduanya diperbaiki sebelum verified, 0 kunci salah; batch KO02: 0 temuan yang mengubah kunci, 0 kunci salah; batch AL02: 1 temuan (pemantik materi membocorkan trik P010, diganti), 0 kunci salah. Batch TB02: 5 butir diubah sebelum audit selesai (3 terlalu mirip contoh di materi, 2 kekeliruan umum yang kebetulan menghasilkan kunci), 0 kunci salah. Batch AL01+KO01: 5 butir revisi teks (0 kunci salah). Mutu pilot: 28 butir; 4 butir perlu revisi teks pembahasan (14%), **0 kunci salah**; 0 karantina.
Jenis temuan: kekeliruan umum yang kabur atau salah (3), langkah bukti terlalu ringkas (1), escaping LaTeX
(tertangkap validator), dan rumus terlalu lebar di ponsel (tata letak).

## Cara kerja konten (penting untuk sesi berikutnya)

- JSON di `content/questions/` adalah sumber kebenaran. Skrip penulis sementara tidak disimpan, jadi
  perubahan berikutnya langsung menyunting JSON (backslash LaTeX ganda) lalu menjalankan `validate.py`.
- Rumus display panjang ditulis dengan `\begin{aligned}…\end{aligned}` per baris; daftar panjang dipecah
  menjadi beberapa `$…$`. `tests/content.test.mjs` memastikan tidak ada galat LaTeX dan tidak ada yang melebar di lebar 390 px.

## Keputusan terbuka (guru)

1. **Anggaran:** kirim angka pemakaian kumulatif lagi setelah modul ke-8 (versi inti) untuk kalibrasi ulang.
2. **Tinjauan guru** atas 28 butir pilot (terutama kesulitan dan bahasa) sebelum dipakai siswa.

## Berikutnya

12/19 modul. Menurut blueprint berikutnya TB04 (persamaan bilangan bulat, digit, floor) dan AL04 (barisan, deret,
teleskopik, rekursi). Angka pemakaian kumulatif dari akun guru masih diminta (keputusan terbuka 1).
