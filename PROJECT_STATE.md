# PROJECT_STATE

Terakhir diperbarui: 2026-10-22 (sesi 1, bagian 2).

## Tahap

- [x] Tahap 0 — lingkungan, sumber, kredit
- [x] Tahap 1 — blueprint, rencana 8 minggu, skema, standar audit, platform, kerangka proyek + tes
- [x] Tahap 2 — **pilot TB01 + GE01 selesai**: 2 materi, 4 contoh, 24 latihan, semuanya `verified`
- [ ] Tahap 3 — penetapan volume (perlu data pemakaian dari guru, lihat "Anggaran")
- [ ] Tahap 4–6

## Lingkungan

| Hal | Temuan |
|---|---|
| Produk | Claude Code di cloud; kontainer sementara |
| Alat | Python 3.13 + sympy 1.13.3, Node 22, Chromium (Playwright), git |
| Jaringan | hanya npm & PyPI; Puspresnas/CDN diblokir |
| Kredit | `ccr_promotional`, reset/berakhir 2026-11-05 08:00 UTC; biaya tidak terlihat dari dalam sesi |
| GitHub | **belum terhubung**: token sesi tidak valid, tidak ada repositori yang dapat diakses. Commit masih lokal |

## Keputusan

- Silabus: peta materi guru (berbasis silabus tak resmi Evan Chen 2023), dibaca 22 Okt 2026 → `docs/sources.md`, `docs/blueprint.md` §3a.
- Format jawaban: isian singkat bilangan bulat (sesuai peta guru).
- Penyimpanan: **repositori GitHub privat** (keputusan guru). Push menunggu akses.
- MathJax 4.1.2 + font NewCM dibundel lokal (pemecahan baris otomatis untuk ponsel; berjalan tanpa internet, sudah diuji).
- Pages: workflow `.github/workflows/pages.yml` hanya manual (`workflow_dispatch`).
- **19 modul** (AL05 fungsi, KO05 induksi/rekursi/graf, AL06 kompleks & trigonometri ditambahkan, disetujui guru);
  program 10 minggu. Sasaran lengkap: 228 latihan modul + 16 diagnostik + 40 campuran = **284 soal unik**, plus 38 contoh.
- Repositori tujuan: `fariza96/osnk` (privat). Akses ditolak pada 22 Okt 2026, kemungkinan Claude GitHub App belum terpasang.

## Selesai (ID)

- TB01: materi `content/modules/TB01.md`; `TB01-E01..E02`, `TB01-P001..P012`: verified.
- GE01: materi `content/modules/GE01.md`; `GE01-E01..E02`, `GE01-P001..P012`: verified; diagram E01, E02, P001, P004, P010.
- Audit: `review/audit_TB01.md`, `review/audit_GE01.md`. Pemeriksaan: `scripts/checks/TB01.py`, `GE01.py` (28/28 cocok).
- Tes: `npm test` (penilai, validator, build, situs fixture, dan tampilan konten nyata per modul) lulus.

Mutu pilot: 28 butir; 4 butir perlu revisi teks pembahasan (14%), **0 kunci salah**; 0 karantina.
Jenis temuan: kekeliruan umum yang kabur atau salah (3), langkah bukti terlalu ringkas (1), escaping LaTeX
(tertangkap validator), dan rumus terlalu lebar di ponsel (tata letak).

## Cara kerja konten (penting untuk sesi berikutnya)

- JSON di `content/questions/` adalah sumber kebenaran. Skrip penulis sementara tidak disimpan, jadi
  perubahan berikutnya langsung menyunting JSON (backslash LaTeX ganda) lalu menjalankan `validate.py`.
- Rumus display panjang ditulis dengan `\begin{aligned}…\end{aligned}` per baris; daftar panjang dipecah
  menjadi beberapa `$…$`. `tests/content.test.mjs` memastikan tidak ada galat LaTeX dan tidak ada yang melebar di lebar 390 px.

## Keputusan terbuka (guru)

1. **GitHub:** pasang Claude GitHub App pada `fariza96/osnk` (lewat claude.ai/connect-github), lalu minta push.
2. **Anggaran:** baca pemakaian di halaman akun Claude agar biaya pilot dapat dicatat dan proyeksi versi inti dihitung.
3. **Tinjauan guru** atas 28 butir pilot (terutama kesulitan dan bahasa) sebelum dipakai siswa.

## Berikutnya

Modul berikutnya menurut urutan: AL01 (identitas & faktorisasi, termasuk SFFT dan rasionalisasi) dan KO01
(aturan penjumlahan & perkalian, bijeksi, himpunan bagian). Satu batch = 1 materi + 2 contoh + 6 latihan.
