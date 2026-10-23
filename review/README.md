# Review

- `audit_<MODUL>.md` — catatan audit per ID (metode, temuan, perbaikan, hasil, keterbatasan).
- `audit_DG.md`, `audit_MX1.md`, `audit_MX2.md` — audit paket diagnostik dan Latihan Campuran.
- `audit_bank.md` — audit lintas bank (komposisi, kemiripan antarbutir, kunci di pembahasan) dan tindak lanjutnya.
- `tinjauan_guru.csv` — lembar tinjauan guru (dibuat ulang dengan `python3 scripts/review_sheet.py`).
- `issues.md` — masalah terbuka lintas modul.
- `quarantine/` — butir yang gagal setelah 2 putaran perbaikan (tidak ikut build); belum ada.

Skrip pemeriksaan komputasional ada di `scripts/checks/<MODUL>.py` dan dijalankan ulang setiap
kali butir terkait diubah.
