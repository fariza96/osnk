# Audit GE01 — Sudut, Segitiga, dan Hubungan Panjang

Tanggal: 2026-10-22. Pemeriksa: Claude, model yang sama dengan penulis. Belum ada tinjauan guru.

## Metode

Langkah A1–A6 sama dengan `audit_TB01.md`. Khusus geometri:

- **A5:** `python3 scripts/checks/GE01.py` membangun ulang setiap konfigurasi dari data pernyataan dengan koordinat
  (sympy, eksak bila memungkinkan). Teorema garis bagi **tidak** dipakai untuk menempatkan titik; kaki garis bagi
  dihitung dari arah jumlah vektor satuan. GE01-P004 diselesaikan secara numerik (bisection) dari syarat
  $DA=DB$, $CA=CD$, $\angle C=52^\circ$, dan diperiksa bahwa $D$ terletak di antara $B$ dan $C$. Soal pencacahan
  diperiksa dengan enumerasi.
- **Diagram:** dibuat oleh `scripts/diagrams/GE01.py` dari koordinat yang memenuhi data soal (berskala). Setiap
  diagram punya `diagram_alt`, dan semua data esensial juga ada di teks soal. Gambar tidak dipakai sebagai bukti.
  Tampilan diperiksa visual pada tema terang dan gelap.

Keluaran A5 (2026-10-22): 14/14 `OK`.

## Per butir

| ID | Kunci | A5 | Temuan | Perbaikan | Status |
|---|---|---|---|---|---|
| GE01-E01 | 72 | OK | diagram: D ditempatkan dengan $AD=BC$ (segitiga emas), sesuai bonus pembahasan | — | verified |
| GE01-E02 | 45 | OK | label panjang tidak dicantumkan di gambar agar $AB$ dihitung siswa | — | verified |
| GE01-P001 | 105 | OK | Kekeliruan umum awal kabur | ditulis ulang | verified |
| GE01-P002 | 60 | OK | — | — | verified |
| GE01-P003 | 13 | OK | ketidaksamaan ketat dijelaskan | — | verified |
| GE01-P004 | 96 | OK | konfigurasi ada dan tunggal ($x=32^\circ$, $D$ di dalam $BC$) | — | verified |
| GE01-P005 | 3 | OK | $\angle ABD=\angle ABC$ karena $D$ pada $BC$; pembahasan memakai garis bagi di segitiga $ABD$ | — | verified |
| GE01-P006 | 30 | OK | — | — | verified |
| GE01-P007 | 6 | OK | solusi alternatif $r=(a+b-c)/2$ cocok | — | verified |
| GE01-P008 | 84 | OK | kaki garis tinggi di dalam $BC$ dicek ($0<x<14$) | persamaan dipecah tiga baris dan langkah $140=28x$ ditambah | verified |
| GE01-P009 | 10 | OK | kasus $x=17$ (siku-siku) dikecualikan; dua kasus sisi terpanjang lengkap | — | verified |
| GE01-P010 | 150 | OK | "di dalam persegi" eksplisit, karena segitiga di luar persegi memberi jawaban lain | persamaan dipecah dua baris | verified |
| GE01-P011 | 90 | OK | pemeriksaan jarak $I$ ke $AB$ ada di pembahasan | — | verified |
| GE01-P012 | 12 | OK | — | daftar dalam tabel dipecah untuk ponsel | verified |

## Keterbatasan

- Sama seperti TB01: A2 tidak buta; belum ada tinjauan guru; label kesulitan editorial.
- Kesesuaian diagram diperiksa secara visual oleh model, bukan oleh manusia.
