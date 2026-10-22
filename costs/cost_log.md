# Catatan biaya

Tidak memuat kredensial. Semua angka dolar di bawah adalah **estimasi berlabel** kecuali
dinyatakan "aktual".

## Mekanisme kredit (Tahap 0)

| Hal | Temuan |
|---|---|
| Lingkungan | Claude Code di cloud (claude.ai/code), dibuka dari aplikasi desktop |
| Jenis batas pemakaian sesi | metadata sesi: `rate_limit_type = ccr_promotional`, status `allowed`, `resetsAt = 2026-11-05 08:00 UTC` (dari epoch 1793865600) |
| Tafsiran | sesi ini memakai kuota/kredit promosi Claude Code on the web; **bukan** kredit API Console yang bisa dipakai skrip |
| Saldo / biaya terpakai | **tidak tersedia** dari dalam sesi |
| Panggilan API Claude dari proyek | tidak ada; tidak ada API key; Batch API & prompt caching **tidak** dipakai oleh proyek |
| Pembatas tagihan | hanya di sisi penyedia (pengaturan akun); prompt/proyek tidak dapat menegakkannya |

Catatan: tanggal `resetsAt` mungkin berarti kredit promosi berakhir/di-reset 5 Nov 2026. Perlu
dikonfirmasi guru dari halaman pengaturan/penagihan Claude.

## Tarif rujukan (untuk estimasi saja)

Sumber: dokumentasi bawaan alat Claude API di sesi ini (data harga di-cache 2026-10-06); halaman
harga resmi tidak dapat dibuka karena pembatasan jaringan. Tidak diketahui apakah kredit promosi
dihitung dengan tarif API ini.

| Model | Input /1 jt | Output /1 jt | Baca cache /1 jt |
|---|---:|---:|---:|
| Claude Opus 5.5 (model sesi ini) | $4.00 | $20.00 | $0.20 |
| Claude Sonnet 5.5 | $2.00 | $10.00 | $0.20 |
| Claude Haiku 5.5 | $0.10 | $0.50 | — |

Token penalaran (thinking) ditagih sebagai output.

## Log

| Waktu (UTC) | Fase | Model | Token | Biaya | Jenis |
|---|---|---|---|---|---|
| 2026-10-22 | Tahap 0–1 (lingkungan, sumber, blueprint, kerangka proyek, tes) | sesi Claude Code | tidak tersedia | tidak tersedia | — |
| 2026-10-22 | Tahap 2 pilot TB01+GE01 (28 butir, 2 materi, 5 SVG, audit, MathJax 4) | sesi Claude Code | tidak tersedia | tidak tersedia; estimasi pra-pilot $4–13 | estimasi |

**Untuk kalibrasi:** guru diminta mencatat pemakaian aktual dari halaman akun Claude sebelum dan sesudah
sesi berikutnya. Tanpa angka itu, proyeksi versi inti/lengkap hanya bisa berupa skala relatif:
satu modul ≈ setengah pilot (pilot = 2 modul + penyiapan alat diagram/MathJax 4 yang tidak perlu diulang).

## Estimasi pilot (2 modul, 4 contoh, 24 latihan, audit + skrip cek + web minimum)

Asumsi kasar sesi agentik: ±60–100 giliran, konteks rata-rata 100–200 rb token sebagian besar
terbaca dari cache, output + penalaran 80–200 rb token.

| Komponen | Rendah | Tinggi |
|---|---:|---:|
| Output + penalaran (80 rb–200 rb × $20/jt) | $1.6 | $4.0 |
| Baca cache (6 jt–20 jt × $0.20/jt) | $1.2 | $4.0 |
| Tulis cache/input tak tercache (0.3 jt–1 jt × $4–5/jt) | $1.2 | $5.0 |
| **Total pilot (estimasi, tarif Opus 5.5)** | **≈ $4** | **≈ $13** |

Ketidakpastian tinggi; dikalibrasi ulang setelah pilot hanya bila guru dapat membaca pemakaian
aktual di akun.
