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
| 2026-10-22 | Tahap 2 pilot TB01+GE01 (28 butir, 2 materi, 5 SVG, audit, MathJax 4) | sesi Claude Code | tidak tersedia | (lihat baris kumulatif) | — |
| 2026-10-22 | **Kumulatif Tahap 0–2 + koneksi GitHub** | sesi Claude Code | tidak tersedia | **US$11 (aktual, dilaporkan guru dari halaman akun)** | aktual |
| 2026-10-22 | Tahap 4: AL01+KO01 (sesi 1) dan TB02+AL02 (sesi 2), masing-masing materi + 14 butir + audit | sesi Claude Code | tidak tersedia | estimasi ≈ US$3,5–4 per modul (proyeksi pilot), belum dikalibrasi | estimasi |

### Proyeksi setelah pilot (dikalibrasi dengan US$11 aktual)

- Pilot = 2 modul + penyiapan alat (validator, build, situs, MathJax 4, diagram, tes) ≈ US$11.
  Perkiraan porsi alat ≈ US$3–4, sehingga per modul ≈ **US$3,5–4** (konservatif, termasuk audit).
- Sisa 17 modul: ≈ US$60–68. Diagnostik + 2 Latihan Campuran (56 soal, tanpa materi): ≈ US$8–10.
  Pengemasan akhir: ≈ US$3. **Total proyeksi ≈ US$82–92** terhadap batas operasional US$90.
- Konsekuensi: margin tipis. Aturan kerja: tidak ada fitur tampilan baru sebelum konten selesai, tangkapan layar
  hanya bila tes gagal, dan pemakaian dicek ulang oleh guru setiap 4 modul. Jika kumulatif melewati US$50 sebelum
  modul ke-12 selesai, volume diturunkan (mis. 10 latihan per modul) dengan persetujuan guru.

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
