# Review

- `audit_<MODUL>.md` — catatan audit per ID (metode, temuan, perbaikan, hasil, keterbatasan).
- `issues.md` — masalah terbuka lintas modul.
- `quarantine/` — butir yang gagal setelah 2 putaran perbaikan (tidak ikut build).

Skrip pemeriksaan komputasional ada di `scripts/checks/<MODUL>.py` dan dijalankan ulang setiap
kali butir terkait diubah.
