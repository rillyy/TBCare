# ─────────────────────────────────────────────────
#  TBCare Desktop — Requirements & Panduan Menjalankan
#  Kelompok A7 | TIK3182_A | UNSRAT 2026
# ─────────────────────────────────────────────────

# ══ REQUIREMENTS ══════════════════════════════════
# File: requirements.txt
# Jalankan: pip install -r requirements.txt

customtkinter>=5.2.0
Pillow>=10.0.0

# Python versi minimum: 3.10
# tkinter sudah termasuk di Python standar (Windows/macOS)
# Linux: sudo apt install python3-tk


# ══ CARA MENJALANKAN ══════════════════════════════

# 1. Install dependensi:
#    pip install customtkinter Pillow

# 2. (Linux/Ubuntu) Install tkinter:
#    sudo apt-get install python3-tk

# 3. Jalankan aplikasi:
#    python tbcare_app.py
#    atau: python3 tbcare_app.py

# ══ FITUR APLIKASI ════════════════════════════════
# ✅ Dashboard (statistik pasien, tren, jadwal, warna dahak)
# ✅ Data Pasien (tabel lengkap, tambah, detail pasien)
# ✅ Kepatuhan Obat (monitoring, distribusi, reminder)
# ✅ Jadwal Kontrol (kalender, list, ringkasan)
# ✅ Antrian Pasien ★ (nomor antrian, panggil berikutnya, daftar prioritas)
# ✅ Peringatan Dini (alert KRITIS/Tinggi/Sedang/Rendah)
# ✅ Lab & Diagnostik (BTA, TCM, Foto Toraks, CD4)
# ✅ Stok Obat (progress bar, peringatan menipis)
# ✅ Laporan Bulanan (rekap indikator, ekspor)
# ✅ Edukasi Pasien (konten per kategori)

# ══ TEKNOLOGI ═════════════════════════════════════
# Bahasa    : Python 3.10+
# GUI       : CustomTkinter (modern Tkinter)
# Tabel     : tkinter.ttk.Treeview
# Database  : SQLite (dapat diintegrasikan)
# Platform  : Windows / macOS / Linux
