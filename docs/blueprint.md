# Blueprint — Ruang Latihan OSN-K Matematika (SMA/MA)

Status: **rancangan Tahap 1, 22 Oktober 2026**. Cakupan modul adalah rancangan pedagogis dan
**belum diverifikasi** terhadap silabus resmi Puspresnas (lihat `docs/sources.md`). Label
kesulitan adalah label editorial sampai diuji pada siswa.

## 1. Sasaran dan asumsi

| Parameter | Nilai kerja | Catatan |
|---|---|---|
| Jenjang | SMA/MA kelas X–XI | Peserta OSN SMA 2026 kelas X–XI (sumber sekunder) |
| Tahap | OSN-K (kabupaten/kota) | OSN-K 2026 sudah berlangsung 18–19 Juni 2026 (sumber sekunder) |
| Tahun sasaran | **OSN 2027 (asumsi)** | Dokumen 2027 diperkirakan belum terbit; cakupan bersifat sementara |
| Program | 8 minggu × 2 pertemuan × 90 menit | 16 pertemuan = 16 modul |
| Peserta | Matematika sekolah cukup baik, pemula olimpiade | |

## 2. Pembagian inti / prasyarat / pengayaan

- **Inti OSN-K**: konsep dan teknik yang menjadi tujuan modul dan diuji pada soal `core`.
- **Prasyarat**: materi sekolah yang diulang singkat agar modul dapat diikuti (mis. faktorisasi
  aljabar SMP, sudut sejajar). Diuji pada soal `foundation`.
- **Pengayaan**: jembatan ke tahap provinsi; hanya muncul di soal `challenge` dan ditandai.
  Tidak diajarkan panjang di OSN-K.

Materi TKA/UTBK/ASAS (limit, turunan, integral, matriks, vektor, statistika deskriptif, program
linear) **tidak** dimasukkan.

## 3. Matriks cakupan 16 modul

Kolom "Sumber" untuk semua baris saat ini: `belum_terverifikasi` (lihat `docs/sources.md`).

| Urutan | Kode | Modul | Subtopik inti | Prasyarat | Tujuan belajar terukur (siswa mampu…) | Teknik utama | Pengayaan (challenge) |
|---|---|---|---|---|---|---|---|
| 1 | TB01 | Keterbagian, prima, FPB/KPK | definisi $a\mid b$, sifat keterbagian linear, algoritma Euclid, $\mathrm{FPB}\cdot\mathrm{KPK}=ab$, uji keterbagian 2–11 | aritmetika bulat | menentukan FPB/KPK dengan Euclid; membuktikan $d\mid a,\,d\mid b\Rightarrow d\mid ax+by$; memakai uji keterbagian | kombinasi linear, faktor bersama, kasus kecil | identitas Bézout sederhana |
| 2 | AL01 | Identitas & faktorisasi | kuadrat/kubus sempurna, selisih kuadrat/kubus, $(a+b+c)^2$, faktorisasi parsial, Sophie Germain dasar | aljabar SMP | menyederhanakan ekspresi dengan identitas; menghitung nilai ekspresi simetris dari $a+b$ dan $ab$ | substitusi, simetri, melengkapkan kuadrat | $a^3+b^3+c^3-3abc$ |
| 3 | KO01 | Aturan tambah & kali | aturan penjumlahan/perkalian, pencacahan sistematis, komplemen, tabel/diagram pohon | — | mencacah dengan memecah kasus yang saling lepas dan lengkap; memakai komplemen | partisi kasus, komplemen, bijeksi sederhana | pencacahan dengan simetri |
| 4 | GE01 | Sudut, segitiga, panjang | sudut sejajar, jumlah sudut, segitiga sama kaki, Pythagoras, ketaksamaan segitiga, teorema bisektor | geometri SMP | menghitung sudut/panjang dengan rantai hubungan sudut; memakai Pythagoras dan bisektor | angle chasing, garis bantu | Stewart (pengayaan) |
| 5 | TB02 | Paritas, sisa, kongruensi | paritas, sisa pembagian, aritmetika modulo, siklus sisa pangkat | TB01 | menentukan sisa $a^n \bmod m$; memakai paritas/modulo untuk menunjukkan ketakmungkinan | tabel sisa, siklus, invariant paritas | Fermat kecil (pernyataan) |
| 6 | AL02 | Persamaan & polinom dasar | persamaan kuadrat, Vieta derajat 2–3, teorema sisa/faktor, sistem persamaan | AL01 | memakai Vieta untuk ekspresi akar tanpa menghitung akar; memakai teorema sisa | Vieta, substitusi, pemfaktoran | polinom dengan akar bersama |
| 7 | KO02 | Permutasi & kombinasi | $n!$, $\binom{n}{k}$, susunan dengan pembatasan, objek identik, melingkar | KO01 | mencacah susunan berbatasan; memilih model permutasi vs kombinasi dengan alasan | blok, sekat, komplemen | identitas binomial sederhana |
| 8 | GE02 | Kesebangunan & luas | kesebangunan, perbandingan luas, rumus luas segitiga, rasio luas berbagi tinggi | GE01 | menghitung rasio panjang/luas melalui segitiga sebangun dan alas-tinggi bersama | rasio luas, garis sejajar | teorema Menelaus/Ceva (pengayaan) |
| 9 | TB03 | Faktorisasi prima & banyak faktor | teorema dasar aritmetika, $\tau(n)$, $\sigma(n)$, valuasi $v_p(n!)$ (Legendre) | TB01, TB02 | menghitung banyak/jumlah faktor; menentukan banyak nol di akhir $n!$ | faktorisasi, rumus Legendre | bilangan sempurna, kuadrat sempurna |
| 10 | AL03 | Pertidaksamaan & nilai ekstrem | kuadrat ≥ 0, AM-GM 2–3 variabel, nilai ekstrem fungsi kuadrat, nilai mutlak | AL01, AL02 | menentukan nilai minimum/maksimum dan menunjukkan dicapai | melengkapkan kuadrat, AM-GM, syarat kesamaan | Cauchy-Schwarz bentuk sederhana |
| 11 | KO03 | Rumah merpati & invariant | prinsip rumah merpati (dasar & umum), invariant/monovariant sederhana | KO01, TB02 | memilih "rumah" yang tepat; memakai invariant untuk ketakmungkinan | konstruksi rumah, paritas, pewarnaan | pewarnaan papan |
| 12 | GE03 | Lingkaran | sudut keliling/pusat, segi empat tali busur, garis singgung, kuasa titik | GE01, GE02 | menghitung sudut/panjang di lingkaran; memakai kuasa titik | angle chasing di lingkaran, kuasa titik | sumbu radikal (pengayaan) |
| 13 | TB04 | Persamaan bilangan bulat | persamaan linear Diophantine, pemfaktoran $xy+ax+by=c$, pembatasan, modulo | TB01–TB03, AL01 | menentukan semua solusi bulat dan membuktikan kelengkapannya | SFFT, batas, modulo | persamaan Pell sederhana (sebut saja) |
| 14 | AL04 | Barisan, deret, rekursi | aritmetika/geometri, teleskopik, pola periodik, rekursi linear sederhana | AL01, AL02 | menjumlah deret teleskopik; menemukan periode atau bentuk tertutup rekursi | teleskopik, periodisitas, induksi | fungsi bilangan bulat terbesar |
| 15 | KO04 | Pencacahan lanjutan & peluang | bintang-dan-sekat, inklusi-eksklusi 2–3 himpunan, lintasan grid, peluang klasik | KO01, KO02 | mencacah dengan bintang-sekat dan inklusi-eksklusi; menghitung peluang ruang sampel seragam | bijeksi, inklusi-eksklusi, rekursi | derangement |
| 16 | GE04 | Koordinat & hubungan metrik | koordinat, jarak, luas shoelace, persamaan garis/lingkaran, Heron | GE01–GE03, AL02 | memilih sistem koordinat yang baik; menggabungkan hubungan metrik | koordinatisasi, Heron, shoelace | trigonometri segitiga (aturan sinus/kosinus) |

ID soal: `<KODE>-E01..E02` (contoh terselesaikan), `<KODE>-P001..P012` (latihan),
`DG-001..016` (diagnostik), `MX1-001..020`, `MX2-001..020` (paket campuran).

## 4. Rencana pembinaan 8 minggu

Setiap pertemuan 90 menit: 10' pemantik → 25' konsep → 15' contoh terselesaikan →
35' latihan (fondasi dikerjakan semua; inti dipilih) → 5' refleksi. Soal tantangan dan
sisa latihan menjadi tugas mandiri.

| Minggu | Pertemuan A | Pertemuan B | Catatan |
|---|---|---|---|
| 0 | Diagnostik (16 soal, 60', mandiri) | — | sebelum program; memetakan bidang lemah |
| 1 | TB01 | AL01 | |
| 2 | KO01 | GE01 | |
| 3 | TB02 | AL02 | |
| 4 | KO02 | GE02 | Latihan Campuran 1 (20 soal, modul 1–8), mandiri akhir minggu |
| 5 | TB03 | AL03 | pembahasan Latihan Campuran 1 di awal pertemuan A (15') |
| 6 | KO03 | GE03 | |
| 7 | TB04 | AL04 | |
| 8 | KO04 | GE04 | Latihan Campuran 2 (20 soal, modul 1–16) |

Urutan memastikan setiap modul hanya memakai prasyarat dari modul sebelumnya, dan empat bidang
bergantian. Modul 1–8 = **versi inti** (tonggak 2).

## 5. Pilot

**TB01 (Keterbagian, prima, FPB/KPK) + GE01 (Sudut, segitiga, panjang).**

Alasan: TB01 adalah modul pertama dan jawabannya mudah diverifikasi komputasional; GE01 adalah
bidang paling berisiko (diagram SVG, kesalahan berkorelasi pada geometri). Memasukkan geometri ke
pilot membuat proyeksi biaya dan tingkat revisi lebih konservatif.

## 6. Komposisi soal per modul

| Peran | Jumlah | Definisi kesulitan |
|---|---|---|
| foundation | 3 | 1 gagasan; penerapan langsung definisi/rumus modul; 2–4 menit |
| core | 6 | 2 gagasan dihubungkan; satu langkah non-rutin (pemilihan kasus, garis bantu, modulo yang tepat); 4–8 menit |
| challenge | 3 | ≥3 gagasan atau perlu argumen kelengkapan kasus/ketakmungkinan; boleh menyentuh pengayaan; 8–15 menit |

Kesulitan **tidak** dinaikkan dengan angka besar atau hitungan panjang.

## 7. Skema soal

Satu sumber kebenaran: `content/questions/<MODUL>.json` (array butir). Skema formal:
`content/schema/question.schema.json`. Validasi: `python3 scripts/validate.py`.

Tipe jawaban yang dinilai otomatis:

| `answer_type` | Diterima | Penilaian |
|---|---|---|
| `integer` | bilangan bulat, boleh tanda `-`, spasi diabaikan | sama persis |
| `rational` | bulat, `p/q`, desimal hingga | aritmetika rasional eksak (BigInt), pecahan ekuivalen diterima |
| `decimal` | desimal | toleransi mutlak `answer_spec.tolerance` (wajib) |
| `choice` | ID opsi stabil (`A`..`E`) | sama dengan `answer_spec.correct` |
| `self_check` | — | rubrik; siswa menilai sendiri, tidak dihitung otomatis |

Isian tidak pernah dievaluasi dengan `eval`. Bentuk akar/π tidak diterima sebagai isian otomatis;
soal dengan jawaban seperti $2\sqrt3$ memakai `choice` atau meminta bentuk bulat (mis. "nilai
$a+b$ jika jawabannya $a\sqrt b$").

## 8. Standar audit matematika

Alur status: `draft → reviewed → verified`, cabang `needs_revision`, dan `quarantined`.

| Langkah | Isi | Bukti yang dicatat di `review/audit_<MODUL>.md` |
|---|---|---|
| A1 Redaksi | domain variabel, data lengkap, target pertanyaan tunggal | temuan atau "tidak ada" |
| A2 Penyelesaian ulang buta | soal diselesaikan ulang dari pernyataan saja | jawaban solver ulang |
| A3 Pembandingan | hasil A2 vs kunci; perbedaan diselesaikan dengan argumen, bukan suara terbanyak | hasil |
| A4 Syarat | pembagian nol, akar semu, kasus batas, keunikan, kelengkapan kasus | temuan |
| A5 Pemeriksaan komputasional | `scripts/checks/<MODUL>.py`: enumerasi/aritmetika eksak/sympy bila relevan | perintah + keluaran |
| A6 Konsistensi | petunjuk, opsi, kunci, pembahasan, diagram | hasil |

Keterbatasan yang dinyatakan apa adanya:
- A2 di sesi Claude Code dilakukan oleh model yang sama dalam konteks yang sama; kunci awal ada
  dalam konteks, sehingga ini **bukan** penyelesaian buta sejati. Penyelesaian buta yang lebih
  kuat: subagen terpisah yang hanya menerima `statement` (+ diagram), atau tinjauan guru.
- Brute force pada rentang terbatas hanya memeriksa jawaban, bukan pembuktian umum.
- Geometri: angka diperiksa dengan koordinat eksak (sympy); gambar tidak dijadikan bukti.

Maksimal 2 putaran perbaikan per butir; gagal → `quarantined` dan diganti butir baru.
Perubahan redaksi/data/opsi/solusi membatalkan `verified`. Build rilis hanya memuat `verified`.

## 9. Platform

**Jalur utama: situs statis (HTML/CSS/JS + MathJax lokal), siap GitHub Pages.**

| Pilihan | Keputusan |
|---|---|
| GitHub + Pages | **dipilih**: berversi, gratis, tanpa server, progres disimpan lokal di perangkat |
| Apps Script + Sheets | ditunda; hanya bila guru meminta nilai terpusat |
| HTML unduhan | dihasilkan dari sumber yang sama (`dist/`), MathJax dibundel lokal |
| Hosting alternatif | tidak dipakai kecuali Pages tidak cocok |

Data soal dibundel sebagai `data.js` (bukan `fetch`) agar halaman dapat dibuka via `file://`.
Kunci jawaban ada di frontend (latihan mandiri); **tidak** cocok untuk ujian rahasia.

## 10. Rencana anggaran

Lihat `costs/cost_log.md`. Ringkas: tidak ada panggilan API berbayar yang dibuat oleh proyek;
seluruh produksi berjalan di dalam sesi Claude Code. Biaya sesi tidak terlihat dari dalam sesi.
