# CLAUDE.md — Ruang Latihan OSN-K Matematika

Paket pembinaan OSN-K Matematika SMA/MA (kelas X–XI, pemula olimpiade) dalam bahasa Indonesia:
16 modul, bank soal, dan situs latihan statis. Brief lengkap: prompt induk guru; ringkasannya di
`docs/blueprint.md`. Status terakhir selalu di `PROJECT_STATE.md`. Baca dua berkas itu dulu, lalu
hanya berkas yang relevan.

## Aturan inti

1. **Benar dulu, banyak belakangan.** Bank kecil yang terverifikasi lebih baik daripada bank besar
   yang belum diperiksa. Jangan memangkas audit demi jumlah.
2. **Satu sumber kebenaran.** Materi: `content/modules/<ID>.md`. Soal: `content/questions/<ID>.json`.
   Situs (`dist/`) selalu dibangun ulang dari sumber; jangan menyunting `dist/`.
3. **Skema soal** mengikuti `content/schema/question.schema.json`; jalankan
   `python3 scripts/validate.py` setelah setiap perubahan. LaTeX di JSON: backslash ganda (`\\frac`).
   Rumus display panjang: `aligned` per baris; daftar panjang: beberapa `$…$` (layar ponsel 390 px).
4. **Status**: `draft → reviewed → verified`, cabang `needs_revision`, `quarantined`. Mengubah
   redaksi, data, opsi, diagram, atau solusi mengembalikan status ke `draft`. Build rilis
   (`npm run build:release`) hanya memuat `verified`.
5. **Audit wajib per butir** (blueprint §8): redaksi → selesaikan ulang dari pernyataan → bandingkan
   → syarat/kasus batas/kelengkapan → cek komputasional di `scripts/checks/<MODUL>.py` bila relevan →
   konsistensi petunjuk/opsi/kunci/pembahasan. Catat di `review/audit_<MODUL>.md`. Maks. 2 putaran
   perbaikan, lalu karantina. Nyatakan jujur bahwa pemeriksa kedua adalah model yang sama.
6. **Kesulitan** ditentukan oleh jumlah gagasan dan jenis penalaran, bukan angka besar atau hitungan
   panjang. Per modul: 3 foundation, 6 core, 3 challenge; 2 contoh terselesaikan.
7. **Orisinalitas.** `origin: original` kecuali benar-benar diadaptasi; jangan mengarang sumber.
   Jangan menyalin kumpulan soal berhak cipta.
8. **Cakupan** belum diverifikasi terhadap silabus resmi (`docs/sources.md`). Jangan menyebut
   "sesuai silabus resmi" atau "simulasi format resmi". Paket campuran = "Latihan Campuran".
9. **Geometri**: diagram SVG presisi di `content/diagrams/`, `diagram_alt` wajib, semua data
   esensial juga ada di teks. Angka diperiksa dengan koordinat eksak (sympy), bukan dari gambar.
10. **Anggaran**: produksi berjalan di sesi Claude Code; tidak ada skrip API. Biaya sesi tidak
    terlihat dari dalam sesi — catat estimasi berlabel di `costs/cost_log.md`, jangan mengarang
    angka aktual. Batas operasional US$90; US$10 cadangan hanya dengan keputusan guru.
11. **Publikasi**: jangan membuat repositori publik, mendorong, atau menerbitkan situs tanpa
    otorisasi guru. Tidak ada secret, API key, atau data siswa di repositori.
12. **Hemat token**: kerjakan per batch (≤ 6 soal), simpan, perbarui `PROJECT_STATE.md`, laporkan
    singkat (Selesai / Mutu / Anggaran / Berikutnya). Jangan mencetak ulang materi yang tersimpan.

## Perintah

```
python3 scripts/validate.py            # validasi bank soal
npm run build                          # dist/ (draf ditandai)
npm run build:release                  # dist/ hanya verified
npm test                               # penilai, validator, build, situs (Chromium)
python3 scripts/checks/<MODUL>.py      # pemeriksaan komputasional per modul
```
