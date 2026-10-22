# PROJECT_STATE

Terakhir diperbarui: 2026-10-22 (sesi 1).

## Tahap

- [x] Tahap 0 — lingkungan, sumber, kredit (lihat di bawah)
- [x] Tahap 1 — blueprint 16 modul, rencana 8 minggu, skema, standar audit, platform, rencana biaya, kerangka proyek + tes
- [ ] Tahap 2 — pilot TB01 + GE01 (4 contoh, 24 latihan) — **menunggu keputusan guru** (lihat "Keputusan terbuka")
- [ ] Tahap 3–6

## Lingkungan (diperiksa, bukan diasumsikan)

| Hal | Temuan |
|---|---|
| Produk | Claude Code di cloud (dibuka dari aplikasi desktop); kontainer sementara — berkas hilang bila sesi berakhir kecuali diunduh/didorong |
| Alat | Python 3.13 + sympy 1.13.3, Node 22, Chromium (Playwright), git |
| Jaringan | hanya registry paket (npm, PyPI). Situs Puspresnas, tirto.id, CDN **diblokir** |
| Kredit | `rate_limit_type = ccr_promotional`, reset/berakhir 2026-11-05 08:00 UTC; saldo & biaya **tidak tersedia** dari dalam sesi |
| API Claude | tidak ada API key; tidak ada skrip API; Batch/caching tidak dipakai |

## Keputusan yang sudah diambil (dapat diubah)

- Jenjang SMA/MA X–XI; tahun sasaran **OSN 2027 (asumsi)** karena OSN-K 2026 sudah lewat (Juni 2026).
- Platform: situs statis + MathJax lokal, siap GitHub Pages. Apps Script ditunda.
- Data dibundel `data.js` (bukan fetch) → bisa dibuka via `file://`.
- Pilot: TB01 + GE01 (satu modul mudah diverifikasi, satu modul berisiko/diagram).
- Paket campuran berlabel "Latihan Campuran" sampai format resmi terverifikasi.

## Selesai

Berkas: `docs/blueprint.md`, `docs/sources.md`, `costs/cost_log.md`, `CLAUDE.md`, `README.md`,
`content/modules/modules.json`, `content/schema/question.schema.json`, `scripts/validate.py`,
`scripts/build.mjs`, `web/` (index.html, css, js/app.js, js/grader.js), `tests/` (13 tes, lulus).

Butir soal: 0. Modul bermateri: 0.

## Belum dibangun (sengaja ditunda)

- Paket campuran dengan timer + pemulihan setelah reload (Tahap 4, setelah bank stabil).
- Pengacakan urutan soal pada paket campuran (fungsi `shuffle` sudah ada dan teruji).
- Workflow GitHub Pages (setelah guru memilih tujuan publikasi).
- `scripts/checks/` per modul (dibuat bersama konten pilot).

## Keputusan terbuka (guru)

1. Lanjut pilot di sesi ini? Biaya tidak terlihat dari dalam sesi; estimasi pilot ≈ US$4–13 (tarif Opus 5.5, ketidakpastian tinggi).
2. Penyimpanan: kontainer sementara. Repositori GitHub privat (butuh otorisasi) atau unduh arsip tiap akhir sesi?
3. Dokumen silabus/pedoman OSN SMA resmi: unggah PDF, atau izinkan domain Puspresnas di pengaturan jaringan.

## Masalah terbuka

- Cakupan `belum_terverifikasi` (lihat `docs/sources.md`).

## Berikutnya

Setelah keputusan 1: tulis `content/modules/TB01.md` + `TB01-E01..E02` + batch `TB01-P001..P006`,
`scripts/checks/TB01.py`, audit, `review/audit_TB01.md`.
