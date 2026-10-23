# Panduan Guru — Ruang Latihan OSN-K Matematika

Paket pembinaan OSN-K Matematika SMA/MA kelas X–XI untuk siswa pemula olimpiade: **19 modul**, **266 butir modul**
(38 contoh terselesaikan + 228 latihan), **diagnostik** 16 soal, dan **dua Latihan Campuran** masing-masing 20 soal.
Semua butir berstatus `verified` menurut audit internal (lihat bagian *Batasan*).

## 1. Membuka situs

- **Daring:** situs terbit otomatis setiap ada push ke cabang `main` (GitHub Pages). Alamatnya ada di
  *Settings → Pages* repositori. Versi yang tampil tertulis di kaki halaman ("Versi …").
- **Luring:** jalankan `npm run build:release`, lalu bagikan folder `dist/` (misalnya sebagai zip). Siswa membuka
  `dist/index.html` langsung di browser; rumus tetap tampil tanpa internet.

Halaman utama berisi daftar modul (bisa disaring per bidang, kesulitan, atau kata kunci), daftar **Paket latihan**
(Diagnostik, Latihan Campuran 1 dan 2), serta saran modul untuk diulang berdasarkan soal yang terakhir dijawab salah.

## 2. Jadwal 10 minggu

| Minggu | Pertemuan A | Pertemuan B | Tugas mandiri |
|---|---|---|---|
| 0 | Diagnostik (60 menit) | — | ekspor progres, kirim ke guru |
| 1 | TB01 Keterbagian, prima, FPB/KPK | AL01 Identitas dan faktorisasi | sisa latihan |
| 2 | KO01 Aturan tambah dan kali | GE01 Sudut, segitiga, panjang | |
| 3 | TB02 Paritas dan kongruensi | AL02 Persamaan dan polinom | |
| 4 | KO02 Permutasi dan kombinasi | GE02 Kesebangunan dan luas | **Latihan Campuran 1** |
| 5 | TB03 Faktorisasi prima, banyak faktor | AL03 Pertidaksamaan, nilai ekstrem | bahas Latihan Campuran 1 (15 menit di awal A) |
| 6 | KO03 Rumah merpati, invarian | GE03 Lingkaran | |
| 7 | TB04 Persamaan bilangan bulat | AL04 Barisan, deret, rekursi | |
| 8 | KO04 Pencacahan lanjutan, peluang | GE04 Koordinat, hubungan metrik | |
| 9 | AL05 Fungsi, persamaan fungsi | KO05 Induksi, rekursi, graf | |
| 10 | AL06 Kompleks dan trigonometri | review bidang terlemah | **Latihan Campuran 2** |

Jika program harus tetap 8 minggu, AL05, KO05, dan AL06 dijadikan tugas mandiri.

## 3. Satu pertemuan (90 menit)

1. **10'** soal pemantik di awal materi modul.
2. **25'** konsep (bagian bernomor di materi).
3. **15'** dua contoh terselesaikan.
4. **35'** latihan: semua soal Fondasi, lalu pilihan soal Inti. Soal Tantangan dan sisa latihan menjadi tugas mandiri.
5. **5'** refleksi: "Kesalahan umum" dan "Rangkuman" di akhir materi.

Setiap soal punya dua petunjuk bertahap, jawaban, pembahasan, ide kunci, dan kekeliruan umum. Situs mencatat apakah soal
diselesaikan **tanpa bantuan** atau setelah membuka petunjuk/pembahasan. Tombol **Cetak** di setiap modul dan paket
menghasilkan lembar soal atau lembar soal + pembahasan (simpan sebagai PDF dari dialog cetak).

## 4. Diagnostik dan Latihan Campuran

- **Diagnostik** (`#/p/DG`): 4 soal per bidang, kebanyakan fondasi, dikerjakan mandiri sebelum program tanpa membuka
  petunjuk. Tabel di atas paket menunjukkan, per bidang, berapa soal yang benar tanpa bantuan.
- **Latihan Campuran 1** (modul 1–8) dan **2** (modul 1–19): 5 soal per bidang, 6 fondasi, 10 inti, 4 tantangan.
  Setiap soal diberi label bidang dan modul rujukan, sehingga kesalahan langsung menunjuk modul yang perlu diulang.

## 5. Progres siswa dan uji coba

Progres tersimpan **di browser siswa saja**. Untuk mengumpulkan hasil:

1. Siswa membuka halaman **Progres** → **Ekspor progres (JSON)** dan mengirim berkas `progres-osnk.json` kepada guru.
2. Guru menyimpan semua berkas di satu folder **di luar repositori** (atau di `data-siswa/`, yang diabaikan git).
   Jangan pernah meng-commit berkas progres: itu data siswa.
3. Jalankan
   ```bash
   python3 scripts/analyze_progress.py FOLDER --out laporan.md
   ```
   Laporan memuat ringkasan diagnostik per bidang, butir yang label kesulitannya mungkin tidak cocok (misalnya soal
   Fondasi yang jarang tuntas tanpa bantuan), dan tabel per butir. Laporan tidak memuat nama berkas.

## 6. Tinjauan guru

`review/tinjauan_guru.csv` (buka di Excel atau Google Sheets) berisi satu baris per butir, diurutkan menurut prioritas:
1 = pilot (TB01, GE01) dan diagnostik, 2 = Latihan Campuran, 3 = modul lain. Isi kolom `kesulitan_guru`,
`bahasa_ok`, `keputusan` (terima/revisi/buang), dan `catatan`. Berkas yang sudah diisi dapat diberikan ke sesi Claude
Code berikutnya untuk diproses: setiap butir yang diubah kembali ke status `draft`, diaudit ulang, lalu diverifikasi.

## 7. Batasan yang perlu diketahui

- **Cakupan** mengikuti peta materi guru (berbasis silabus tak resmi), **belum** dicocokkan dengan silabus resmi
  Puspresnas. Jangan menyebutnya "sesuai silabus resmi" atau "simulasi format resmi".
- **Label kesulitan** bersifat editorial sampai diuji pada siswa (bagian 5).
- **Audit** dilakukan oleh model yang sama dengan penulis soal, jadi bukan penyelesaian buta. Kunci diperiksa dengan
  skrip komputasional (`npm run check:math`, 322/322 cocok), tetapi tinjauan guru tetap diperlukan.
- **Kunci jawaban ada di situs.** Situs ini untuk latihan mandiri, bukan ujian rahasia.
- Lisensi materi dan kode belum ditetapkan (usulan di README).
