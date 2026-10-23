# Audit TB04 — Persamaan Bilangan Bulat

Tanggal: 2026-10-23. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/TB04.py` mengenumerasi solusi pada rentang
yang mencakup semua solusi (batasnya diturunkan dari soal dan dicatat di komentar fungsi), dengan pecahan eksak
untuk E02 dan sympy untuk P007. P011 dan P012 juga mengecek bahwa daftar solusi tepat sama dengan pembahasan
(`assert`). Kelengkapan di luar rentang berasal dari argumen di pembahasan (batas ukuran, modulo).

Keluaran A5 (2026-10-23): 14/14 `OK`. Tes tampilan TB04 lulus setelah satu perbaikan tata letak (E01).

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| TB04-E01 | 6 | daftar enam pasangan melebar di layar 390 px | dipecah menjadi beberapa `$…$` | verified |
| TB04-E02 | 10 | — | — | verified |
| TB04-P001 | 3 | versi awal materi §1 memakai persamaan $3x+5y=47$ sebagai contoh (persis soal ini) | contoh diganti $4x+9y=59$ | verified |
| TB04-P002 | 4 | — | — | verified |
| TB04-P003 | 100 | — | — | verified |
| TB04-P004 | 8 | — | — | verified |
| TB04-P005 | 13 | konstruksi eksplisit untuk $n$ ganjil dan $4\mid n$ melengkapi arah "mungkin" | — | verified |
| TB04-P006 | 108 | — | — | verified |
| TB04-P007 | 58 | akar negatif dibuang dengan syarat $\lfloor x\rfloor=n\ge2$ | — | verified |
| TB04-P008 | 9 | — | — | verified |
| TB04-P009 | 2 | — | — | verified |
| TB04-P010 | 76 | versi awal materi §5 menjelaskan teknik selisih suku $\lfloor k^2/N\rfloor$ (kunci soal ini); contoh pengganti di materi awalnya salah hitung ($24$, seharusnya $22$) | teknik dihapus dari materi; contoh dihitung ulang | verified |
| TB04-P011 | 7 | — | — | verified |
| TB04-P012 | 2021 | — | — | verified |

`origin: adapted`: P010 (tipe soal klasik floor$(k^2/N)$, angka dipilih ulang).

Kemiripan: E01, P001, P008 sama-sama persamaan linear (pencacahan positif; tak negatif; soal cerita). P004 dan P011
memakai selisih kuadrat dengan tuntutan berbeda (paritas faktor; pangkat 2).

Keterbatasan: A2 tidak buta; label kesulitan editorial.
