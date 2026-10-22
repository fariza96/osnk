# Ruang Latihan OSN-K Matematika

Materi, bank soal, dan situs latihan statis untuk pembinaan OSN-K Matematika SMA/MA.
Situs tidak memanggil Claude dan tidak memerlukan server; progres siswa tersimpan di browser.

**Status: pilot selesai.** Modul TB01 dan GE01 (4 contoh, 24 latihan, semuanya `verified`). Lihat `PROJECT_STATE.md`.

## Menjalankan

Kebutuhan: Node.js 18+ dan Python 3.10+.

```bash
npm install
python3 scripts/validate.py
npm run build          # hasil di dist/
```

Buka `dist/index.html` langsung di browser (bisa via `file://`) atau sajikan:
`python3 -m http.server -d dist 8000` lalu buka http://localhost:8000.

MathJax 4.1.2 dan font NewCM dibundel di `dist/vendor` (lisensi Apache-2.0). Rumus tampil tanpa internet,
dan ini sudah diuji di Chromium dengan semua jaringan diblokir. Tetap uji sekali di perangkat siswa.

## Menambah atau memperbarui konten

- Materi: `content/modules/<ID>.md` (Markdown + LaTeX `$...$`, `$$...$$`).
- Soal: `content/questions/<ID>.json`, mengikuti `content/schema/question.schema.json`.
  Di JSON, backslash LaTeX ditulis ganda: `"$\\frac{a}{b}$"`.
- Diagram: `content/diagrams/<ID-soal>.svg`.
- Setelah mengubah: `python3 scripts/validate.py`, `npm run check:math`, lalu `npm run build`.
- Diagram GE01 dibuat ulang dengan `python3 scripts/diagrams/GE01.py`.
- Rilis untuk siswa: `npm run build:release` (hanya butir berstatus `verified`).

## Tes

```bash
npm test
```

Menguji penilai jawaban (bulat, negatif, nol, pecahan ekuivalen, toleransi desimal, kosong,
pilihan ganda, pengacakan opsi), validator, build, dan situs di Chromium (via `file://` dan subpath
seperti GitHub Pages: rumus tampil, petunjuk, progres setelah reload, cetak, tanpa scroll
horizontal di lebar ponsel). Tes perangkat lunak **tidak** menggantikan audit matematika.

## Membagikan (setelah guru memutuskan)

Rencana: repositori GitHub privat. Opsi Pages: workflow `.github/workflows/pages.yml`, yang hanya berjalan
manual dan membangun versi rilis (verified). Pages pada repositori privat memerlukan paket GitHub berbayar.
Tanpa Pages, `dist/` dapat dibagikan sebagai arsip zip yang dibuka langsung di browser. Semua URL di situs relatif,
sehingga cocok untuk subpath `https://<akun>.github.io/<repo>/`. Catatan:

- Repositori privat tidak otomatis membuat situs Pages privat. Periksa pengaturan akses sebelum
  memakai Pages untuk materi terbatas.
- Kunci jawaban ada di frontend. Situs ini untuk latihan mandiri, bukan ujian rahasia.

## Batasan

- Cakupan modul belum diverifikasi terhadap silabus resmi Puspresnas (`docs/sources.md`).
- Label kesulitan bersifat editorial sampai diuji pada siswa.
- Progres tidak berpindah perangkat secara otomatis; gunakan ekspor/impor JSON di halaman Progres.

## Lisensi

Materi dan soal orisinal: ditentukan guru sebelum publikasi (usulan: CC BY-NC-SA 4.0). Kode:
ditentukan guru (usulan: MIT). MathJax: Apache-2.0.
