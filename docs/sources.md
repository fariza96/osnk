# Sumber cakupan — log verifikasi

Tanggal akses: 22 Oktober 2026. Status keseluruhan cakupan: **`peta_guru` — mengikuti peta materi dari guru; belum dicocokkan dengan dokumen resmi Puspresnas**.

## Dokumen dari guru (dibaca lengkap, 22 Okt 2026)

| Hal | Isi |
|---|---|
| Berkas | `Peta-Materi-Silabus-Olimpiade-OSNK.docx` (diunggah guru; tidak disalin ke repositori) |
| Judul | "Peta Materi Persiapan OSN-K — Silabus Olimpiade Internasional untuk OSN-K" |
| Dasar | *Unofficial syllabus for math olympiads*, Evan Chen (31 Jan 2023); dokumen menyatakan itu **bukan** pedoman resmi |
| Klaim format | "OSN-K berbentuk isian singkat tanpa pembuktian" (pernyataan guru, belum dicocokkan dengan pedoman resmi) |
| Frekuensi OSN-K 2021–2026 (analisis guru, 100 soal) | Aljabar 27, Teori Bilangan 26, Geometri 25 (luas & kesebangunan 8, kuasa titik 8), Kombinatorika 22 (inklusi-eksklusi, permutasi-kombinasi, rekursi masing-masing 4) |
| Status topik | Wajib → diajarkan penuh; Berguna → alat bantu/kotak wawasan; Lanjutan → pengayaan OSN-P; Tidak diperlukan → tidak diajarkan |
| Soal AoPS yang sudah dipakai guru di Modul 2 | AIME 1983 #6, AIME 1985 #13, AIME 1986 #5, AIME 2006 II #3, AMC 10B 2017 #14 — **dihindari** di bank ini agar tidak tumpang-tindih |

Pemetaan topik wajib ke 16 modul ada di `docs/blueprint.md` §3a.


## Upaya akses dokumen resmi

| Sumber | URL | Hasil | Status |
|---|---|---|---|
| Portal Puspresnas OSN SMA 2026 | https://pusatprestasinasional.kemendikdasmen.go.id/event/riset-dan-inovasi/sma/olimpiade-sains-nasional-2026-2026-sma | Diblokir kebijakan jaringan lingkungan cloud (proxy menolak host) | belum_terverifikasi |
| Pedoman/panduan OSN SMA 2026 (PDF) | belum diketahui (dirujuk sumber sekunder: "lampiran 3, mulai hlm. 58") | tidak dapat diunduh | belum_terverifikasi |
| Silabus OSN Matematika SMA 2027 | — | diperkirakan belum terbit (OSN-K 2026 telah berlangsung Juni 2026) | belum_terbit/belum_dicek |

## Informasi dari sumber sekunder (cuplikan hasil pencarian, isi halaman tidak terbaca)

Hanya cuplikan mesin pencari; halaman tidak dapat dibuka dari lingkungan ini. Jangan dikutip
sebagai fakta resmi.

| Klaim | Sumber sekunder | Dipakai untuk |
|---|---|---|
| Cakupan matematika OSN SMA: aljabar, geometri, kombinatorika, teori bilangan | tirto.id, "Link unduh kumpulan materi silabus OSN SMA 2026 PDF" (https://tirto.id/link-unduh-kumpulan-materi-silabus-osn-sma-2026-pdf-hqCC) | empat bidang modul |
| Silabus lengkap ada di pedoman pelaksanaan, lampiran 3 mulai hlm. 58 | sama | petunjuk dokumen yang harus dibaca |
| OSN-K SMA 2026: 18–19 Juni 2026; kuota maks. 5 murid/cabang/sekolah | tirto.id, "Jadwal OSN SMA 2026 tingkat kabupaten" (https://tirto.id/jadwal-osn-sma-2026-tingkat-kabupaten-dan-teknisnya-huKS) | menetapkan asumsi tahun sasaran 2027 |
| Peserta kelas X dan XI; OSN-K berbasis moda semi daring | cuplikan pencarian (tirto.id / mamikos.com) | kelas peserta |
| Jumlah soal, bentuk soal, durasi, penskoran Matematika OSN-K 2026 | **tidak ditemukan** | — |

## Akibat bagi proyek

- 16 modul adalah rancangan pedagogis, bukan pemetaan silabus resmi.
- Paket campuran diberi label **Latihan Campuran**, bukan "simulasi format resmi".
- Bentuk jawaban (isian bulat/pecahan dan pilihan ganda) dibuat dapat dikonfigurasi sampai format
  resmi terverifikasi.
- Tidak ada paket soal OSN-K terdahulu yang ditelaah; kalibrasi gaya belum dilakukan.

## Yang dibutuhkan untuk verifikasi

Salah satu:
1. Guru mengunggah PDF pedoman/silabus OSN SMA (2026 atau 2027) ke sesi; atau
2. Domain `pusatprestasinasional.kemendikdasmen.go.id` diizinkan dalam pengaturan jaringan
   lingkungan cloud.

Setelah dibaca: catat judul, penerbit, tahun terbit, tahun berlaku, halaman, lalu perbarui kolom
"Sumber" di `docs/blueprint.md` §3.
