# Audit lintas bank (Tahap 5)

Dibuat oleh `python3 scripts/audit_bank.py --write`. Peringatan adalah heuristik (kemiripan teks, kunci yang tidak tertulis persis di pembahasan); setiap peringatan diperiksa manusia dan hasilnya dicatat di bagian **Tindak lanjut**.

Total butir: 322. Status: {'verified': 322}. Asal: {'original': 309, 'adapted': 13}.

## Komposisi per modul

| Modul | Contoh | Fondasi | Inti | Tantangan | Total | Status |
|---|---|---|---|---|---|---|
| TB01 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| AL01 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| KO01 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| GE01 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| TB02 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| AL02 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| KO02 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| GE02 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| TB03 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| AL03 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| KO03 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| GE03 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| TB04 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| AL04 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| KO04 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| GE04 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| AL05 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| KO05 | 2 | 3 | 6 | 3 | 14 | verified 14 |
| AL06 | 2 | 3 | 6 | 3 | 14 | verified 14 |

## Paket

| Paket | Butir | Menit (jumlah perkiraan) | Per bidang | Fondasi/Inti/Tantangan |
|---|---|---|---|---|
| DG | 16 | 49 | aljabar 4, geometri 4, kombinatorika 4, teori_bilangan 4 | 12/4/0 |
| MX1 | 20 | 108 | aljabar 5, geometri 5, kombinatorika 5, teori_bilangan 5 | 6/10/4 |
| MX2 | 20 | 110 | aljabar 5, geometri 5, kombinatorika 5, teori_bilangan 5 | 6/10/4 |

## Peringatan untuk diperiksa

- MX1-003 ~ TB01-P004: kemiripan teks 0.99
- AL05-P005 ~ AL05-P012: kemiripan teks 0.98
- TB03-P003 ~ TB03-P007: kemiripan teks 0.98
- MX2-001 ~ TB03-P003: kemiripan teks 0.97
- MX2-001 ~ TB03-P007: kemiripan teks 0.96
- AL05-E01 ~ AL05-P011: kemiripan teks 0.96
- TB01-P004 ~ TB01-P005: kemiripan teks 0.94
- AL03-E01 ~ AL03-P002: kemiripan teks 0.94
- KO05-E01 ~ KO05-P004: kemiripan teks 0.94
- DG-003 ~ MX1-002: kemiripan teks 0.94
- DG-006 ~ MX1-007: kemiripan teks 0.93
- MX1-003 ~ TB01-P005: kemiripan teks 0.93
- KO03-E01 ~ KO03-P009: kemiripan teks 0.93
- GE04-E01 ~ MX2-019: kemiripan teks 0.93
- KO03-E01 ~ KO03-P004: kemiripan teks 0.92
- AL05-P007 ~ MX2-008: kemiripan teks 0.91
- GE04-P011 ~ MX1-017: kemiripan teks 0.91
- MX2-004 ~ TB04-P003: kemiripan teks 0.90
- AL06-P003 ~ AL06-P009: kemiripan teks 0.90
- AL01-P002 ~ AL01-P005: kemiripan teks 0.90

## Tindak lanjut (2026-10-23)

Putaran pertama audit ini (ambang kemiripan 0,75) menemukan **empat butir paket yang sama atau terlalu mirip dengan butir
modul** dan lolos dari pencocokan manual sebelumnya (pencarian kata kunci, bukan pembandingan seluruh teks):

| Butir | Sama/mirip dengan | Tindakan |
|---|---|---|
| DG-004 (banyak faktor $360$) | TB03-P001 (identik) | diganti banyak faktor $450$ (versi 2), diaudit ulang |
| DG-008 (minimum $x^2-6x+14$) | AL03-P001 (identik) | diganti maksimum $-2x^2+8x+3$ (versi 2), diaudit ulang |
| DG-009 (tiga digit berbeda) | KO01-E01 (varian contoh) | diganti tiga digit semuanya ganjil (versi 2), diaudit ulang |
| MX1-019 ($r$ segitiga siku-siku $20,21$) | GE01-P007 (identik) | diganti hipotenusa $25$, kaki $7$ (versi 2), diaudit ulang |

Peringatan yang tersisa di atas (ambang 0,9) sudah dibaca satu per satu: semuanya kerangka kalimat yang sama dengan
bilangan dan pertanyaan berbeda (misalnya $\mathrm{FPB}(n,12)=1$ vs $=4$; $v_3(50!)$ vs $v_2(20!)$; Heron untuk $r$ vs $R$),
atau pasangan contoh–latihan dalam satu modul yang memang sengaja setipe. Tidak ada tindakan, kecuali dicatat untuk
tinjauan guru (`review/issues.md` no. 6): MX1-003 ~ TB01-P004 dan MX2-001 ~ TB03-P003 adalah soal setipe dengan bilangan lain.

Pemeriksaan "kunci tertulis di pembahasan": semua butir lolos setelah pemisah ribuan ($676\,000$) diabaikan.
Komposisi 19 modul tepat 2 contoh + 3/6/3. Total perkiraan DG $49$ menit (slot $60$ menit memberi waktu baca).
