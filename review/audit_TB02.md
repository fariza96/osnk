# Audit TB02 — Paritas, Sisa Pembagian, dan Kongruensi

Tanggal: 2026-10-22. Pemeriksa: Claude (model yang sama dengan penulis). Belum ada tinjauan guru.
Metode A1–A6 sama dengan `audit_TB01.md`. A5: `python3 scripts/checks/TB02.py` memakai `pow` modular dan
enumerasi. Untuk P010, eksponen $3^{2026}$ dihitung eksak sebagai bilangan bulat, lalu dipangkatkan modulo $100$.
P008 dan P012 juga diperiksa dengan enumerasi pada rentang terbatas ($p<200$, $m<200$); kelengkapan untuk
nilai yang lebih besar berasal dari argumen di pembahasan.

Keluaran A5 (2026-10-22): 14/14 `OK`. `npm test` 23/23 lulus (TB02 dirender tanpa galat LaTeX dan tanpa scroll horizontal di 390 px).

| ID | Kunci | Temuan | Perbaikan | Status |
|---|---|---|---|---|
| TB02-E01 | 6 | jawaban dari kekeliruan umum ($0$) diperiksa: memang berbeda dari kunci | — | verified |
| TB02-E02 | 157 | — | — | verified |
| TB02-P001 | 9 | — | — | verified |
| TB02-P002 | 3 | — | — | verified |
| TB02-P003 | 6 | versi awal ($7x\equiv3 \bmod 11$) sama dengan contoh di materi §5 | angka diganti | verified |
| TB02-P004 | 56 | kelengkapan (semua $S=0..55$ tercapai) dibuktikan dengan konstruksi, bukan hanya paritas | — | verified |
| TB02-P005 | 49 | — | — | verified |
| TB02-P006 | 1 | versi awal (sampai $100$): jawaban kekeliruan umum kebetulan sama dengan kunci ($14\equiv0 \bmod 7$) | batas diganti menjadi $2026$ | verified |
| TB02-P007 | 25 | versi awal (sisa $2,3,4$ mod $3,4,5$) sama dengan trik di materi §6 | diganti pembagi $4,6,9$ yang tidak saling prima (KPK, bukan hasil kali) | verified |
| TB02-P008 | 3 | kasus $p=3$ dikecualikan dari argumen mod $3$ dan diperiksa terpisah | — | verified |
| TB02-P009 | 12 | versi awal memakai orde $2$ mod $13$, yang sudah dihitung di materi §4 | modulo diganti $17$ | verified |
| TB02-P010 | 83 | versi awal kekeliruan umum (reduksi eksponen mod $100$) menghasilkan jawaban benar karena $20\mid100$ | kekeliruan umum diganti | verified |
| TB02-P011 | 20 | empat kelas sisa mod $20$ ($3,4,6,17$) dicek langsung | — | verified |
| TB02-P012 | 6 | keunikan: $m$ ganjil dibuang mod $4$, $m$ genap diselesaikan dengan pemfaktoran | — | verified |

Kemiripan: E01, P002, P005, P009, P010 sama-sama memakai siklus/orde, tetapi tuntutannya berbeda (dua basis;
angka satuan; mod $100$; mencacah $n$ dengan orde $\ne p-1$; menara dua tingkat). E02 dan P011 sama-sama CRT;
P011 menggabungkan siklus pangkat dengan faktor $n$. P007 sengaja memakai modulo yang tidak saling prima.

Keterbatasan: A2 tidak buta; label kesulitan editorial. P005 mungkin lebih dekat ke fondasi daripada inti.
