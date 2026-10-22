# Audit TB01 — Keterbagian, Bilangan Prima, FPB dan KPK

Tanggal: 2026-10-22. Pemeriksa: Claude, model yang sama dengan penulis. Belum ada tinjauan guru.

## Metode

| Langkah | Pelaksanaan |
|---|---|
| A1 Redaksi | Setiap pernyataan dibaca ulang: domain variabel (bulat/positif/boleh negatif), rentang inklusif/eksklusif, satu target pertanyaan, jawaban isian bilangan bulat |
| A2 Selesaikan ulang | Setiap soal diselesaikan ulang dari pernyataannya. **Keterbatasan:** kunci awal sudah ada dalam konteks yang sama, jadi ini bukan penyelesaian buta |
| A3 Banding | Hasil A2 dan A5 dibandingkan dengan `answer_spec` |
| A4 Syarat | Kasus batas, kelengkapan kasus, keberadaan (nilai terbesar tercapai), keunikan |
| A5 Komputasi | `python3 scripts/checks/TB01.py`: enumerasi langsung dari pernyataan. Rentang enumerasi dipilih lebih lebar dari batas yang dibuktikan; untuk P003 dan P012 hanya memeriksa, bukan membuktikan |
| A6 Konsistensi | Petunjuk 1 → strategi, petunjuk 2 → langkah kunci; jawaban di pembahasan = kunci; kekeliruan umum menghasilkan jawaban yang memang salah |

Keluaran A5 (2026-10-22): 14/14 `OK`.

## Per butir

| ID | Kunci | A5 | Temuan | Perbaikan | Status |
|---|---|---|---|---|---|
| TB01-E01 | 39 | OK | — | — | verified |
| TB01-E02 | 4 | OK | Kekeliruan umum awal kabur (contoh $(6,5)$ tidak jelas salahnya) | ditulis ulang: pasangan terurut vs $a<b$ | verified |
| TB01-P001 | 119 | OK | rumus panjang melebar di ponsel | dipecah dua baris | verified |
| TB01-P002 | 60 | OK | Kekeliruan umum awal ("$420/84\cdot12$") justru menghasilkan jawaban benar | diganti dengan kesalahan yang memang salah | verified |
| TB01-P003 | 5 | OK | nilai terbesar perlu bukti tercapai, dan pembahasan sudah menunjukkannya ($n=3$) | — | verified |
| TB01-P004 | 17 | OK | — | — | verified |
| TB01-P005 | 25 | OK | — | — | verified |
| TB01-P006 | 8 | OK | "$x,y$ boleh negatif atau nol" eksplisit, sehingga jawaban tidak ambigu | — | verified |
| TB01-P007 | 140 | OK | selang $0<t\le3600$ eksplisit, sehingga $t=0$ tidak dihitung | — | verified |
| TB01-P008 | −4 | OK | jawaban negatif; penilai sudah diuji untuk input negatif | — | verified |
| TB01-P009 | 35 | OK | "terurut" ditebalkan | — | verified |
| TB01-P010 | 572 | OK | solusi alternatif (komplemen) dihitung ulang dan juga memberi 572 | — | verified |
| TB01-P011 | 23 | OK | bukti dua arah (pangkat prima ⇔ berubah) ada | daftar dipecah untuk ponsel | verified |
| TB01-P012 | 4 | OK | langkah $g\mid3$ awalnya terlalu ringkas | dirumuskan via $\mathrm{FPB}(g,ab)=1$ | verified |

## Temuan proses

- Saat merevisi, `\ne` di skrip penulis berubah menjadi karakter baris baru. `scripts/validate.py` menangkapnya sebelum disimpan, sehingga pemeriksaan karakter kontrol terbukti berguna.
- Soal AoPS yang sudah dipakai guru di Modul 2 (mis. AIME 1985 #13, barisan $100+n^2$) sengaja tidak diadaptasi.
- Kemiripan di dalam bank: E01 ($n+3\mid n^2+15$) dan P005/P010 sama-sama memakai "kurangi kelipatan hingga konstanta", tetapi berbeda struktur: E01 membagi konstanta, P005 menghitung nilai FPB tertentu, P010 menggabungkannya dengan inklusi–eksklusi.

## Keterbatasan

- Belum ada penyelesaian buta yang benar-benar independen (model lain atau guru).
- Label kesulitan bersifat editorial; belum diuji pada siswa.
