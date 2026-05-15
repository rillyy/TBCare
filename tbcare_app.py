"""
TBCare – Aplikasi Desktop Manajemen Pasien Tuberkulosis
Python 3 + CustomTkinter | Kelompok A7 – TIK3182_A | UNSRAT 2026
"""
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import datetime, random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# ── Palet warna (HANYA hex 6-digit, TIDAK ada rgba/CSS) ──────────────────────
C = {
    "sidebar"   : "#2e3a32",
    "sidebar_h" : "#3d4a41",
    "active_nav": "#4a5e50",
    "ivory"     : "#F4F3F1",
    "card"      : "#faf9f7",
    "evergreen" : "#68756D",
    "dark_green": "#3d4a41",
    "terracotta": "#B57B66",
    "sage"      : "#A1A79E",
    "blood"     : "#A63228",
    "sput_yel"  : "#C9B84C",
    "sput_grn"  : "#7A9B52",
    "text_dark" : "#2a3028",
    "text_mid"  : "#5a6358",
    "text_light": "#8a9388",
    "border"    : "#deddd9",
    "antrian"   : "#4a7fa5",
    # warna light (untuk avatar bg) — semua valid 6-digit hex
    "blood_lt"  : "#f2d5d3",
    "terr_lt"   : "#f5e5df",
    "yel_lt"    : "#f7f0d5",
    "grn_lt"    : "#dcefd6",
    "sage_lt"   : "#e8ebe8",
}

F_TITLE = ("Helvetica", 15, "bold")
F_SUB   = ("Helvetica", 12, "bold")
F_BODY  = ("Helvetica", 11)
F_SM    = ("Helvetica", 10)
F_XS    = ("Helvetica", 9)

# ── Risiko → warna (dua dict, tidak ada concatenation) ───────────────────────
RISIKO_CLR  = {"KRITIS":C["blood"],"Tinggi":C["terracotta"],
               "Sedang":C["sput_yel"],"Rendah":C["sput_grn"]}
RISIKO_LITE = {"KRITIS":C["blood_lt"],"Tinggi":C["terr_lt"],
               "Sedang":C["yel_lt"],"Rendah":C["grn_lt"]}

# ── Data dummy ────────────────────────────────────────────────────────────────
PASIEN = [
    {"id":"TBC-2024-001","nama":"Siti Aminah","umur":42,"fase":"Fase Lanjutan","hari":87,
     "kepatuhan":61,"status":"Putus Obat","dahak":"Darah","kontrol":"08:00","risiko":"KRITIS",
     "diagnosa":"TBC Paru (Kambuh)","dokter":"dr. Rina Sari","alamat":"Jl. Piere Tendean No.12"},
    {"id":"TBC-2024-002","nama":"Budi Wahyono","umur":55,"fase":"Fase Intensif","hari":34,
     "kepatuhan":73,"status":"Dalam Terapi","dahak":"Kuning-Hijau","kontrol":"09:30","risiko":"Tinggi",
     "diagnosa":"TBC Paru (Baru)","dokter":"dr. Rina Sari","alamat":"Jl. Sam Ratulangi No.45"},
    {"id":"TBC-2024-003","nama":"Rahmat Hidayat","umur":31,"fase":"Fase Intensif","hari":19,
     "kepatuhan":88,"status":"Dalam Terapi","dahak":"Hijau","kontrol":"10:30","risiko":"Sedang",
     "diagnosa":"TBC Paru (Baru)","dokter":"dr. Budi Santoso","alamat":"Jl. Walanda Maramis No.7"},
    {"id":"TBC-2024-004","nama":"Maria Nengsih","umur":28,"fase":"Fase Lanjutan","hari":122,
     "kepatuhan":95,"status":"Dalam Terapi","dahak":"Bening","kontrol":"10:30","risiko":"Rendah",
     "diagnosa":"TBC Paru (Baru)","dokter":"dr. Rina Sari","alamat":"Jl. Diponegoro No.33"},
    {"id":"TBC-2024-005","nama":"Yusuf Pratama","umur":47,"fase":"Kambuh","hari":11,
     "kepatuhan":82,"status":"Dalam Terapi","dahak":"Kuning","kontrol":"13:00","risiko":"Sedang",
     "diagnosa":"TBC Ekstra Paru","dokter":"dr. Budi Santoso","alamat":"Jl. Bethesda No.18"},
    {"id":"TBC-2024-006","nama":"Dewi Fitriani","umur":36,"fase":"Fase Intensif","hari":57,
     "kepatuhan":79,"status":"Dalam Terapi","dahak":"Hijau","kontrol":"15:00","risiko":"Tinggi",
     "diagnosa":"TBC + HIV Komorbid","dokter":"dr. Rina Sari","alamat":"Jl. Monginsidi No.9"},
    {"id":"TBC-2024-007","nama":"Ahmad Maulana","umur":23,"fase":"Fase Intensif","hari":42,
     "kepatuhan":91,"status":"Dalam Terapi","dahak":"Bening","kontrol":"11:00","risiko":"Rendah",
     "diagnosa":"TBC Paru (Baru)","dokter":"dr. Budi Santoso","alamat":"Jl. Arie Lasut No.55"},
    {"id":"TBC-2024-008","nama":"Nona Rompas","umur":61,"fase":"Fase Lanjutan","hari":155,
     "kepatuhan":98,"status":"Selesai","dahak":"Bening","kontrol":"-","risiko":"Rendah",
     "diagnosa":"TBC Paru (Baru)","dokter":"dr. Rina Sari","alamat":"Jl. Sudirman No.22"},
]


LAB = [
    {"id":"TBC-2024-001","nama":"Siti Aminah",   "jenis":"BTA Sputum",    "hasil":"BTA +3",                    "tgl":"02/04/2026","status":"Kritis"},
    {"id":"TBC-2024-002","nama":"Budi Wahyono",  "jenis":"TCM GeneXpert", "hasil":"MTB Detected-RIF Resistant","tgl":"01/04/2026","status":"MDR"},
    {"id":"TBC-2024-003","nama":"Rahmat Hidayat","jenis":"Foto Toraks",   "hasil":"Infiltrat bilateral",       "tgl":"31/03/2026","status":"Abnormal"},
    {"id":"TBC-2024-004","nama":"Maria Nengsih", "jenis":"BTA Sputum",    "hasil":"BTA Negatif",               "tgl":"28/03/2026","status":"Normal"},
    {"id":"TBC-2024-006","nama":"Dewi Fitriani", "jenis":"CD4 Count",     "hasil":"185 sel/uL",                "tgl":"30/03/2026","status":"Rendah"},
    {"id":"TBC-2024-007","nama":"Ahmad Maulana", "jenis":"TCM GeneXpert", "hasil":"MTB Detected-RIF Sensitive","tgl":"29/03/2026","status":"Positif"},
]

ANTRIAN = [
    {"no":"A-001","nama":"Siti Aminah",  "pukul":"08:00","keperluan":"Evaluasi Hemoptisis",     "status":"Dipanggil","prio":"URGENT"},
    {"no":"A-002","nama":"Budi Wahyono","pukul":"09:30","keperluan":"Ambil Hasil TCM",          "status":"Menunggu", "prio":"Tinggi"},
    {"no":"A-003","nama":"Maria Nengsih","pukul":"10:30","keperluan":"Kontrol Bulan ke-4",      "status":"Menunggu", "prio":"Normal"},
    {"no":"A-004","nama":"Yusuf Pratama","pukul":"13:00","keperluan":"Konsultasi Awal Terapi",  "status":"Menunggu", "prio":"Normal"},
    {"no":"A-005","nama":"Dewi Fitriani","pukul":"15:00","keperluan":"Evaluasi ARV + OAT",      "status":"Menunggu", "prio":"Tinggi"},
]

PERINGATAN = [
    {"nama":"Siti Aminah",  "id":"TBC-2024-001","isu":"Putus obat 3 hari + hemoptisis",      "level":"KRITIS","aksi":"Hubungi Pasien"},
    {"nama":"Budi Wahyono", "id":"TBC-2024-002","isu":"Resistensi Rifampisin terdeteksi",    "level":"Tinggi","aksi":"Jadwalkan Kontrol"},
    {"nama":"Yusuf Pratama","id":"TBC-2024-005","isu":"TCM belum selesai 4 hari",            "level":"Sedang","aksi":"Follow-up Lab"},
    {"nama":"Dewi Fitriani","id":"TBC-2024-006","isu":"CD4 rendah, risiko infeksi oportunis","level":"Tinggi","aksi":"Konsultasi Dokter"},
    {"nama":"Rahmat Hidayat","id":"TBC-2024-003","isu":"Kepatuhan turun minggu ini",         "level":"Sedang","aksi":"Kirim Reminder"},
    {"nama":"Ahmad Maulana","id":"TBC-2024-007","isu":"Jadwal kontrol terlewat",             "level":"Rendah","aksi":"Jadwalkan Kontrol"},
]

EDUKASI = [
    {"judul":"Apa itu Tuberkulosis?",                              "kat":"Pengenalan TBC","dur":"5 mnt","views":234},
    {"judul":"Panduan Minum Obat TBC Tidak Boleh Terputus",        "kat":"Pengobatan",    "dur":"8 mnt","views":189},
    {"judul":"Cara Mencegah Penularan TBC di Rumah",               "kat":"Pencegahan",    "dur":"6 mnt","views":142},
    {"judul":"Pola Makan Sehat Mendukung Kesembuhan TBC",          "kat":"Nutrisi",       "dur":"7 mnt","views":97},
    {"judul":"Efek Samping Obat TBC dan Cara Mengatasinya",        "kat":"Pengobatan",    "dur":"9 mnt","views":215},
    {"judul":"Tips Membangun Kebiasaan Minum Obat Setiap Hari",    "kat":"Kepatuhan",     "dur":"4 mnt","views":178},
]

LAPORAN_ROWS = [
    ("Pasien ART Terdaftar",              "100%", "22/27","63%",   "Tercapai"),
    ("Rata-rata Kepatuhan Minum Obat",    ">=85%","94%",  "98.8%","Mendekati"),
    ("Pasien Putus Obat",                 "<=5%", "6.2%", "98.7%","Perlu Perbaikan"),
    ("Keberhasilan Terapi",               ">=90%","87%",  "96.7%","Mendekati"),
    ("Konversi BTA Bulan 2",              ">=80%","88%",  "110%", "Tercapai"),
    ("Pasien dengan Efek Samping",        "-",    "88",   "-",    "Terpantau"),
]

# ─────────────────────────────────────────────────────────────────────────────
# Helper: separator garis
# ─────────────────────────────────────────────────────────────────────────────
def sep_line(parent, padx=0):
    tk.Frame(parent, bg=C["border"], height=1).pack(fill="x", padx=padx)

# ─────────────────────────────────────────────────────────────────────────────
# Helper: kartu statistik (4-in-a-row)
# ─────────────────────────────────────────────────────────────────────────────
def stat_card(parent, label, value, sub, trend, color, col):
    fr = ctk.CTkFrame(parent, fg_color=C["card"], corner_radius=12,
                      border_width=1, border_color=C["border"])
    fr.grid(row=0, column=col, sticky="nsew", padx=5)
    tk.Frame(fr, bg=color, height=3).pack(fill="x")
    ctk.CTkLabel(fr, text=label.upper(), font=F_XS,
                 text_color=C["text_light"]).pack(anchor="w", padx=14, pady=(8,2))
    ctk.CTkLabel(fr, text=value, font=("Helvetica",26,"bold"),
                 text_color=C["text_dark"]).pack(anchor="w", padx=14)
    ctk.CTkLabel(fr, text=sub, font=F_XS,
                 text_color=C["text_mid"]).pack(anchor="w", padx=14, pady=(0,4))
    tc = C["sput_grn"] if "+" in trend or "up" in trend.lower() else C["blood"]
    ctk.CTkLabel(fr, text=trend, font=F_XS, text_color=tc).pack(anchor="w", padx=14, pady=(0,10))

# ─────────────────────────────────────────────────────────────────────────────
# NavItem sidebar
# ─────────────────────────────────────────────────────────────────────────────
class NavItem(ctk.CTkFrame):
    def __init__(self, parent, icon, label, badge=None, command=None):
        super().__init__(parent, fg_color="transparent", cursor="hand2")
        self._cmd = command
        self.pack(fill="x", padx=8, pady=1)
        self._build(icon, label, badge)
        self.bind("<Button-1>", self._on_click)

    def _build(self, icon, label, badge):
        icon_lbl = ctk.CTkLabel(self, text=icon, width=28, height=28,
                                fg_color="transparent", corner_radius=6,
                                font=("Segoe UI Emoji", 13))
        icon_lbl.pack(side="left", padx=(6,4), pady=5)
        icon_lbl.bind("<Button-1>", self._on_click)

        txt = ctk.CTkLabel(self, text=label, font=F_SM, text_color="#aabba4")
        txt.pack(side="left", padx=2)
        txt.bind("<Button-1>", self._on_click)

        if badge:
            b = ctk.CTkLabel(self, text=str(badge), width=22, height=16,
                             fg_color=C["blood"], corner_radius=8,
                             font=F_XS, text_color="white")
            b.pack(side="right", padx=8)
            b.bind("<Button-1>", self._on_click)

    def set_active(self, active: bool):
        self.configure(fg_color=C["active_nav"] if active else "transparent")

    def _on_click(self, _=None):
        if self._cmd:
            self._cmd()


# ─────────────────────────────────────────────────────────────────────────────
# App utama
# ─────────────────────────────────────────────────────────────────────────────
class TBCareApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TBCare — Sistem Manajemen Pasien Tuberkulosis")
        self.geometry("1280x800")
        self.minsize(1100, 680)
        self.configure(fg_color=C["ivory"])
        self._nav_items: dict[str, NavItem] = {}
        self._current = ""
        self._build_ui()
        self._show("dashboard")

    # ── Layout ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build_sidebar()
        self._build_main_area()

    # ── Sidebar ──────────────────────────────────────────────────────────────
    def _build_sidebar(self):
        sb = ctk.CTkFrame(self, fg_color=C["sidebar"], width=220, corner_radius=0)
        sb.grid(row=0, column=0, sticky="ns")
        sb.grid_propagate(False)

        # Logo
        lf = ctk.CTkFrame(sb, fg_color="transparent")
        lf.pack(fill="x", padx=14, pady=(18,12))
        ib = ctk.CTkFrame(lf, fg_color=C["terracotta"], width=36, height=36, corner_radius=8)
        ib.pack(side="left"); ib.pack_propagate(False)
        ctk.CTkLabel(ib, text="🫁", font=("Segoe UI Emoji",16)).place(relx=.5, rely=.5, anchor="center")
        tf2 = ctk.CTkFrame(lf, fg_color="transparent")
        tf2.pack(side="left", padx=8)
        ctk.CTkLabel(tf2, text="TBCare", font=("Georgia",16,"bold"),
                     text_color=C["ivory"]).pack(anchor="w")
        ctk.CTkLabel(tf2, text="Manajemen Pasien TBC",
                     font=F_XS, text_color=C["sage"]).pack(anchor="w")
        tk.Frame(sb, bg=C["sidebar_h"], height=1).pack(fill="x")

        menus = [
            ("UTAMA", [
                ("📊","Dashboard",       None,  "dashboard"),
                ("👥","Data Pasien",     None,  "pasien"),
                ("💊","Kepatuhan Obat",  3,     "kepatuhan"),
                ("📅","Jadwal Kontrol",  None,  "jadwal"),
                ("🔢","Antrian Pasien",  None,  "antrian"),
            ]),
            ("KLINIS", [
                ("⚠️","Peringatan Dini", 6,     "peringatan"),
                ("🧪","Lab & Diagnostik",None,  "lab"),
            ]),
            ("LAPORAN", [
                ("📋","Laporan Bulanan", None,  "laporan"),
                ("📚","Edukasi Pasien",  None,  "edukasi"),
            ]),
        ]
        for section, items in menus:
            ctk.CTkLabel(sb, text=section, font=F_XS,
                         text_color=C["sage"]).pack(anchor="w", padx=18, pady=(12,2))
            for icon, label, badge, key in items:
                ni = NavItem(sb, icon, label, badge=badge,
                             command=lambda k=key: self._show(k))
                self._nav_items[key] = ni

        # User card
        tk.Frame(sb, bg=C["sidebar_h"], height=1).pack(fill="x", side="bottom")
        uc = ctk.CTkFrame(sb, fg_color="transparent")
        uc.pack(side="bottom", fill="x", padx=12, pady=10)
        av = ctk.CTkFrame(uc, fg_color=C["evergreen"], width=32, height=32, corner_radius=16)
        av.pack(side="left"); av.pack_propagate(False)
        ctk.CTkLabel(av, text="DR", font=F_XS, text_color="white").place(relx=.5, rely=.5, anchor="center")
        ui = ctk.CTkFrame(uc, fg_color="transparent")
        ui.pack(side="left", padx=8)
        ctk.CTkLabel(ui, text="dr. Rina Sari", font=F_SM, text_color=C["ivory"]).pack(anchor="w")
        ctk.CTkLabel(ui, text="Dokter Paru — Admin", font=F_XS, text_color=C["sage"]).pack(anchor="w")

    # ── Area konten ──────────────────────────────────────────────────────────
    def _build_main_area(self):
        self._main = ctk.CTkFrame(self, fg_color=C["ivory"], corner_radius=0)
        self._main.grid(row=0, column=1, sticky="nsew")
        self._main.grid_rowconfigure(1, weight=1)
        self._main.grid_columnconfigure(0, weight=1)
        self._build_topbar()
        self._scroll = ctk.CTkScrollableFrame(self._main, fg_color=C["ivory"],
                                               scrollbar_button_color=C["sage"])
        self._scroll.grid(row=1, column=0, sticky="nsew")
        self._scroll.grid_columnconfigure(0, weight=1)

    def _build_topbar(self):
        tb = ctk.CTkFrame(self._main, fg_color=C["card"], corner_radius=0,
                          border_width=1, border_color=C["border"])
        tb.grid(row=0, column=0, sticky="ew")
        tb.grid_columnconfigure(1, weight=1)
        self._tb_title = ctk.CTkLabel(tb, text="Dashboard",
                                       font=("Georgia",15,"bold"), text_color=C["text_dark"])
        self._tb_title.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        today = datetime.date.today().strftime("%A, %d %B %Y")
        ctk.CTkLabel(tb, text=today, font=F_XS,
                     text_color=C["text_light"]).grid(row=0, column=1, padx=4, sticky="w")
        rr = ctk.CTkFrame(tb, fg_color="transparent")
        rr.grid(row=0, column=2, padx=14, sticky="e")
        ctk.CTkLabel(rr, text="  ⚠  7 Pasien Perlu Tindakan  ",
                     font=F_SM, text_color=C["blood"],
                     fg_color="#f5e6e5", corner_radius=10).pack(side="left", padx=4)
        ctk.CTkEntry(rr, placeholder_text="🔍  Cari pasien...",
                     width=180, font=F_SM).pack(side="left", padx=6)

    # ── Router ───────────────────────────────────────────────────────────────
    def _show(self, key: str):
        if self._current:
            self._nav_items.get(self._current, NavItem.__new__(NavItem))
            ni_old = self._nav_items.get(self._current)
            if ni_old: ni_old.set_active(False)
        self._current = key
        ni_new = self._nav_items.get(key)
        if ni_new: ni_new.set_active(True)

        titles = {"dashboard":"Dashboard","pasien":"Data Pasien",
                  "kepatuhan":"Kepatuhan Obat","jadwal":"Jadwal Kontrol",
                  "antrian":"Antrian Pasien","peringatan":"Peringatan Dini",
                  "lab":"Lab & Diagnostik",
                  "laporan":"Laporan Bulanan","edukasi":"Edukasi Pasien"}
        self._tb_title.configure(text=titles.get(key, key))

        for w in self._scroll.winfo_children():
            w.destroy()

        {"dashboard": self._pg_dashboard,
         "pasien"   : self._pg_pasien,
         "kepatuhan": self._pg_kepatuhan,
         "jadwal"   : self._pg_jadwal,
         "antrian"  : self._pg_antrian,
         "peringatan":self._pg_peringatan,
         "lab"      : self._pg_lab,
         "laporan"  : self._pg_laporan,
         "edukasi"  : self._pg_edukasi,
        }.get(key, lambda: None)()

    # ── Treeview style (shared) ───────────────────────────────────────────────
    def _tree_style(self):
        s = ttk.Style()
        s.configure("TB.Treeview", font=("Helvetica",10), rowheight=30,
                    background=C["card"], fieldbackground=C["card"],
                    foreground=C["text_dark"])
        s.configure("TB.Treeview.Heading", font=("Helvetica",10,"bold"),
                    background=C["ivory"], foreground=C["text_mid"])
        s.map("TB.Treeview", background=[("selected",C["dark_green"])],
              foreground=[("selected","white")])

    # ═════════════════════════════════════════════════════════════════════════
    # DASHBOARD
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_dashboard(self):
        p = self._scroll

        # Greeting
        gf = ctk.CTkFrame(p, fg_color="transparent")
        gf.pack(fill="x", padx=20, pady=(18,6))
        ctk.CTkLabel(gf, text="Selamat Pagi, dr. Rina Sari 👋",
                     font=("Georgia",16,"bold"), text_color=C["text_dark"]).pack(anchor="w")
        ctk.CTkLabel(gf, text="Berikut ringkasan kondisi layanan TBC hari ini.",
                     font=F_BODY, text_color=C["text_mid"]).pack(anchor="w")

        # 4 stat cards
        sr = ctk.CTkFrame(p, fg_color="transparent")
        sr.pack(fill="x", padx=20, pady=(10,10))
        for i in range(4): sr.grid_columnconfigure(i, weight=1)
        stat_card(sr,"Pasien Aktif","148","Dalam terapi DOTS","+ 12 bulan ini",C["evergreen"],0)
        stat_card(sr,"Kepatuhan Rata-rata","87%","Minum obat 30 hari","+ 4% vs bulan lalu",C["terracotta"],1)
        stat_card(sr,"Putus Obat","9","Perlu intervensi segera","+ 2 kasus baru",C["blood"],2)
        stat_card(sr,"Selesai Pengobatan","34","Bulan April 2026","+ Target tercapai",C["sput_grn"],3)

        # Dua kolom
        two = ctk.CTkFrame(p, fg_color="transparent")
        two.pack(fill="both", padx=20, pady=(0,10), expand=True)
        two.grid_columnconfigure(0, weight=7)
        two.grid_columnconfigure(1, weight=5)

        # Panel kiri — pasien butuh perhatian
        pp = ctk.CTkFrame(two, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        pp.grid(row=0, column=0, sticky="nsew", padx=(0,6))
        hd = ctk.CTkFrame(pp, fg_color="transparent")
        hd.pack(fill="x", padx=14, pady=(10,4))
        ctk.CTkLabel(hd, text="Pasien — Butuh Perhatian",
                     font=F_SUB, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkLabel(hd, text="Lihat semua →", font=F_SM,
                     text_color=C["evergreen"], cursor="hand2").pack(side="right")
        sep_line(pp)

        for px in PASIEN[:6]:
            bc   = RISIKO_CLR.get(px["risiko"],  C["sage"])
            blt  = RISIKO_LITE.get(px["risiko"], C["sage_lt"])
            row  = ctk.CTkFrame(pp, fg_color="transparent")
            row.pack(fill="x", padx=10, pady=2)
            tk.Frame(row, bg=bc, width=3).pack(side="left", fill="y", padx=(0,8))
            initials = "".join(n[0] for n in px["nama"].split()[:2])
            av = ctk.CTkFrame(row, fg_color=blt, width=32, height=32, corner_radius=16)
            av.pack(side="left", pady=5); av.pack_propagate(False)
            ctk.CTkLabel(av, text=initials, font=F_XS,
                         text_color=bc).place(relx=.5, rely=.5, anchor="center")
            inf = ctk.CTkFrame(row, fg_color="transparent")
            inf.pack(side="left", padx=8, fill="x", expand=True)
            ctk.CTkLabel(inf, text=f"{px['nama']}, {px['umur']} th",
                         font=("Helvetica",11,"bold"), text_color=C["text_dark"]).pack(anchor="w")
            ctk.CTkLabel(inf, text=f"{px['fase']}  ·  Hari ke-{px['hari']}  ·  {px['diagnosa']}",
                         font=F_XS, text_color=C["text_light"]).pack(anchor="w")
            ctk.CTkLabel(row, text=px["risiko"], fg_color=bc, text_color="white",
                         corner_radius=8, font=F_XS, width=60).pack(side="right", padx=8, pady=5)
            sep_line(pp, padx=10)

        # Panel kanan
        rp = ctk.CTkFrame(two, fg_color="transparent")
        rp.grid(row=0, column=1, sticky="nsew")

        # Panduan warna dahak
        dg = ctk.CTkFrame(rp, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        dg.pack(fill="x", pady=(0,8))
        ctk.CTkLabel(dg, text="Indikator Warna Dahak",
                     font=F_SUB, text_color=C["text_dark"]).pack(anchor="w", padx=14, pady=(10,4))
        sep_line(dg)
        for clr, nm, note, sev, sev_c in [
            ("#f0f0ec","Bening/Putih","Batuk biasa","Monitor",C["sage"]),
            (C["sput_yel"],"Kuning","Infeksi bakteri aktif","Waspada",C["sput_yel"]),
            (C["sput_grn"],"Hijau-Kuning","Indikasi kuat TBC","Prioritas",C["sput_grn"]),
            ("#4d7a2a","Hijau Gelap","Infeksi parah","Segera",C["evergreen"]),
            (C["blood"],"Bercampur Darah","Hemoptisis — rawat inap","KRITIS",C["blood"]),
        ]:
            df = ctk.CTkFrame(dg, fg_color="transparent")
            df.pack(fill="x", padx=10, pady=3)
            tk.Frame(df, bg=clr, width=18, height=18).pack(side="left", padx=(0,8))
            dc = ctk.CTkFrame(df, fg_color="transparent")
            dc.pack(side="left", fill="x", expand=True)
            ctk.CTkLabel(dc, text=nm, font=("Helvetica",10,"bold"),
                         text_color=C["text_dark"]).pack(anchor="w")
            ctk.CTkLabel(dc, text=note, font=F_XS,
                         text_color=C["text_light"]).pack(anchor="w")
            ctk.CTkLabel(df, text=sev, fg_color=sev_c, text_color="white",
                         corner_radius=6, font=F_XS, width=55).pack(side="right", padx=6, pady=3)

        # Jadwal hari ini
        jd = ctk.CTkFrame(rp, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        jd.pack(fill="x")
        ctk.CTkLabel(jd, text="Jadwal Kontrol Hari Ini",
                     font=F_SUB, text_color=C["text_dark"]).pack(anchor="w", padx=14, pady=(10,4))
        sep_line(jd)
        for px in PASIEN:
            if px["kontrol"] != "-":
                jf = ctk.CTkFrame(jd, fg_color="transparent")
                jf.pack(fill="x", padx=12, pady=3)
                ctk.CTkLabel(jf, text=px["kontrol"], font=F_XS,
                             text_color=C["text_light"], width=42).pack(side="left")
                dot_c = C["sput_grn"] if px["risiko"] == "Rendah" else C["blood"]
                tk.Frame(jf, bg=dot_c, width=7, height=7).pack(side="left", padx=4)
                ctk.CTkLabel(jf, text=px["nama"], font=("Helvetica",10,"bold"),
                             text_color=C["text_dark"]).pack(side="left", padx=4)
                ctk.CTkLabel(jf, text=px["fase"], font=F_XS,
                             text_color=C["text_light"]).pack(side="left")

        # Tren kepatuhan
        tp = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        tp.pack(fill="x", padx=20, pady=(0,20))
        ctk.CTkLabel(tp, text="Tren Kepatuhan — 6 Bulan Terakhir",
                     font=F_SUB, text_color=C["text_dark"]).pack(anchor="w", padx=14, pady=(10,4))
        sep_line(tp)
        pf = ctk.CTkFrame(tp, fg_color="transparent")
        pf.pack(fill="x", padx=14, pady=10)
        for lbl, val, clr in [("TBC Paru Baru",91,C["sput_grn"]),
                               ("TBC Kambuh",   73,C["terracotta"]),
                               ("MDR-TBC",       68,C["blood"])]:
            rw = ctk.CTkFrame(pf, fg_color="transparent")
            rw.pack(fill="x", pady=4)
            ctk.CTkLabel(rw, text=lbl, font=F_SM, width=140,
                         text_color=C["text_mid"]).pack(side="left")
            bar_bg = ctk.CTkFrame(rw, fg_color="#e0e0d8", height=8, corner_radius=4)
            bar_bg.pack(side="left", fill="x", expand=True, padx=(0,8))
            fill = ctk.CTkFrame(bar_bg, fg_color=clr, height=8, corner_radius=4,
                                width=int(400 * val / 100))
            fill.place(x=0, y=0, relheight=1, relwidth=val/100)
            ctk.CTkLabel(rw, text=f"{val}%", font=("Helvetica",10,"bold"),
                         text_color=clr, width=36).pack(side="right")

    # ═════════════════════════════════════════════════════════════════════════
    # DATA PASIEN
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_pasien(self):
        p = self._scroll
        self._tree_style()
        hdr = ctk.CTkFrame(p, fg_color="transparent")
        hdr.pack(fill="x", padx=20, pady=(18,10))
        ctk.CTkLabel(hdr, text="Manajemen Data Pasien TBC",
                     font=F_TITLE, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(hdr, text="+ Tambah Pasien", fg_color=C["dark_green"],
                      hover_color=C["evergreen"], font=F_BODY,
                      command=self._dlg_tambah_pasien).pack(side="right")

        fb = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=10,
                          border_width=1, border_color=C["border"])
        fb.pack(fill="x", padx=20, pady=(0,10))
        ctk.CTkEntry(fb, placeholder_text="🔍 Cari nama / ID pasien…",
                     width=260, font=F_BODY).pack(side="left", padx=10, pady=8)
        for lbl in ["Semua Status","Dalam Terapi","Putus Obat","Selesai"]:
            ctk.CTkButton(fb, text=lbl, width=110, height=28,
                          fg_color=C["dark_green"] if lbl=="Semua Status" else C["ivory"],
                          text_color="white" if lbl=="Semua Status" else C["text_dark"],
                          hover_color=C["sage"], font=F_XS,
                          border_width=1, border_color=C["border"]).pack(side="left", padx=4, pady=8)

        cols = ("ID","Nama","Usia","Diagnosa","Fase","Kepatuhan","Kontrol","Status","Risiko")
        tf = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        tf.pack(fill="both", padx=20, pady=(0,20), expand=True)
        tree = ttk.Treeview(tf, columns=cols, show="headings",
                            style="TB.Treeview", height=14)
        for col, w in zip(cols, [90,140,50,160,120,80,80,110,80]):
            tree.heading(col, text=col)
            tree.column(col, width=w, anchor="w" if col in ("Nama","Diagnosa") else "center")
        for px in PASIEN:
            tag = "putus" if px["status"]=="Putus Obat" else ("selesai" if px["status"]=="Selesai" else "")
            tree.insert("","end", values=(
                px["id"],px["nama"],f"{px['umur']} th",px["diagnosa"],
                px["fase"],f"{px['kepatuhan']}%",px["kontrol"],px["status"],px["risiko"]
            ), tags=(tag,))
        tree.tag_configure("putus",  foreground=C["blood"])
        tree.tag_configure("selesai",foreground=C["sput_grn"])
        vsb = ttk.Scrollbar(tf, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side="left", fill="both", expand=True, padx=2, pady=2)
        vsb.pack(side="right", fill="y")
        tree.bind("<Double-1>", lambda e: self._dlg_detail_pasien(
            next((px for px in PASIEN
                  if tree.item(tree.focus())["values"] and
                  px["nama"]==tree.item(tree.focus())["values"][1]), None)))

    def _dlg_tambah_pasien(self):
        dlg = ctk.CTkToplevel(self); dlg.title("Tambah Pasien Baru")
        dlg.geometry("460x520"); dlg.grab_set()
        ctk.CTkLabel(dlg, text="Form Pendaftaran Pasien TBC",
                     font=F_TITLE, text_color=C["text_dark"]).pack(pady=(18,10))
        for lbl, default in [("Nama Lengkap",""),("Usia",""),("Alamat",""),
                              ("No. Telepon",""),("Diagnosa","TBC Paru (Baru)"),
                              ("Dokter","dr. Rina Sari"),("Fase Terapi","Fase Intensif")]:
            fr = ctk.CTkFrame(dlg, fg_color="transparent")
            fr.pack(fill="x", padx=24, pady=4)
            ctk.CTkLabel(fr, text=lbl, font=F_BODY, width=130,
                         text_color=C["text_mid"]).pack(side="left")
            e = ctk.CTkEntry(fr, font=F_BODY)
            if default: e.insert(0, default)
            e.pack(side="left", fill="x", expand=True)
        ctk.CTkButton(dlg, text="Simpan Data Pasien", fg_color=C["dark_green"],
                      hover_color=C["evergreen"], font=F_BODY,
                      command=lambda:(messagebox.showinfo("Berhasil","Data berhasil disimpan!"),
                                      dlg.destroy())).pack(pady=16)

    def _dlg_detail_pasien(self, px):
        if not px: return
        dlg = ctk.CTkToplevel(self); dlg.title(f"Detail — {px['nama']}")
        dlg.geometry("460x480"); dlg.grab_set()
        ctk.CTkLabel(dlg, text=px["nama"], font=F_TITLE,
                     text_color=C["text_dark"]).pack(pady=(16,2))
        ctk.CTkLabel(dlg, text=px["id"], font=F_BODY,
                     text_color=C["text_light"]).pack()
        sep_line(dlg, padx=20)
        for k, v in [("Usia",f"{px['umur']} tahun"),("Diagnosa",px["diagnosa"]),
                     ("Fase",px["fase"]),("Hari Terapi",f"Hari ke-{px['hari']}"),
                     ("Kepatuhan",f"{px['kepatuhan']}%"),("Dokter",px["dokter"]),
                     ("Alamat",px["alamat"]),("Status",px["status"]),("Risiko",px["risiko"])]:
            fr = ctk.CTkFrame(dlg, fg_color="transparent")
            fr.pack(fill="x", padx=24, pady=2)
            ctk.CTkLabel(fr, text=k+":", font=("Helvetica",10,"bold"),
                         width=100, text_color=C["text_mid"]).pack(side="left")
            ctk.CTkLabel(fr, text=v, font=F_BODY,
                         text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(dlg, text="Tutup", fg_color=C["sage"],
                      command=dlg.destroy).pack(pady=14)

    # ═════════════════════════════════════════════════════════════════════════
    # KEPATUHAN OBAT
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_kepatuhan(self):
        p = self._scroll; self._tree_style()
        ctk.CTkLabel(p, text="Monitoring Kepatuhan Minum Obat",
                     font=F_TITLE, text_color=C["text_dark"]).pack(anchor="w", padx=20, pady=(18,4))
        sr = ctk.CTkFrame(p, fg_color="transparent")
        sr.pack(fill="x", padx=20, pady=(0,12))
        for i in range(3): sr.grid_columnconfigure(i, weight=1)
        for col,(lbl,val,sub,clr) in enumerate([
            ("Kepatuhan Minggu Ini","84%","Naik dari 79% minggu lalu",C["sput_grn"]),
            ("Total Reminder Terkirim","107","Periode 13-19 April 2026",C["terracotta"]),
            ("Pasien Tidak Konfirmasi","28","Perlu tindak lanjut",C["blood"]),
        ]):
            fc = ctk.CTkFrame(sr, fg_color=C["card"], corner_radius=12,
                              border_width=1, border_color=C["border"])
            fc.grid(row=0, column=col, sticky="nsew", padx=5)
            tk.Frame(fc, bg=clr, height=3).pack(fill="x")
            ctk.CTkLabel(fc, text=lbl.upper(), font=F_XS,
                         text_color=C["text_light"]).pack(anchor="w", padx=14, pady=(8,2))
            ctk.CTkLabel(fc, text=val, font=("Helvetica",24,"bold"),
                         text_color=C["text_dark"]).pack(anchor="w", padx=14)
            ctk.CTkLabel(fc, text=sub, font=F_XS,
                         text_color=clr).pack(anchor="w", padx=14, pady=(0,10))

        df2 = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                           border_width=1, border_color=C["border"])
        df2.pack(fill="x", padx=20, pady=(0,12))
        ctk.CTkLabel(df2, text="Distribusi Kepatuhan Pasien",
                     font=F_SUB, text_color=C["text_dark"]).pack(anchor="w", padx=14, pady=(10,6))
        sep_line(df2)
        for lbl, n, pct, clr in [
            ("Patuh (>=90%)",          81, 81, C["sput_grn"]),
            ("Cukup Patuh (50-79%)",   72, 72, C["terracotta"]),
            ("Tidak Patuh (<50%)",      9,  9, C["blood"]),
        ]:
            rw = ctk.CTkFrame(df2, fg_color="transparent")
            rw.pack(fill="x", padx=14, pady=5)
            ctk.CTkLabel(rw, text=lbl, font=F_BODY, width=220,
                         text_color=C["text_mid"]).pack(side="left")
            bb = ctk.CTkFrame(rw, fg_color="#e8e8e0", height=10, corner_radius=5)
            bb.pack(side="left", fill="x", expand=True, padx=(0,8))
            ctk.CTkFrame(bb, fg_color=clr, height=10, corner_radius=5).place(
                x=0, y=0, relheight=1, relwidth=pct/100)
            ctk.CTkLabel(rw, text=f"{n} pasien", font=("Helvetica",10,"bold"),
                         text_color=clr, width=80).pack(side="right")

        cols = ("ID","Nama","Fase","Kepatuhan","Status Minggu Ini","Terakhir Minum","Aksi")
        tf = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        tf.pack(fill="both", padx=20, pady=(0,20), expand=True)
        tree = ttk.Treeview(tf, columns=cols, show="headings",
                            style="TB.Treeview", height=10)
        for col, w in zip(cols, [90,140,110,90,120,120,100]):
            tree.heading(col, text=col); tree.column(col, width=w, anchor="center")
        days = ["Hari ini","Kemarin","2 hari lalu","3 hari lalu"]
        for px in PASIEN:
            st = "Konfirmasi" if px["kepatuhan"]>85 else ("Terlewat" if px["kepatuhan"]<70 else "Parsial")
            tree.insert("","end", values=(
                px["id"],px["nama"],px["fase"],f"{px['kepatuhan']}%",
                st,random.choice(days),"Kirim Reminder"))
        tree.pack(fill="both", expand=True, padx=2, pady=2)

    # ═════════════════════════════════════════════════════════════════════════
    # JADWAL KONTROL
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_jadwal(self):
        p = self._scroll
        hdr = ctk.CTkFrame(p, fg_color="transparent")
        hdr.pack(fill="x", padx=20, pady=(18,10))
        ctk.CTkLabel(hdr, text="Jadwal Kontrol & Kunjungan Pasien",
                     font=F_TITLE, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(hdr, text="+ Jadwalkan Pasien", fg_color=C["dark_green"],
                      hover_color=C["evergreen"], font=F_BODY,
                      command=lambda: messagebox.showinfo("Info","Form jadwal")).pack(side="right")
        two = ctk.CTkFrame(p, fg_color="transparent")
        two.pack(fill="both", padx=20, expand=True)
        two.grid_columnconfigure(0, weight=3); two.grid_columnconfigure(1, weight=2)

        lf = ctk.CTkFrame(two, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        lf.grid(row=0, column=0, sticky="nsew", padx=(0,8))
        ctk.CTkLabel(lf, text="Jadwal Kontrol — Minggu Ini",
                     font=F_SUB, text_color=C["text_dark"]).pack(anchor="w", padx=14, pady=(10,6))
        sep_line(lf)
        for date_lbl, idxs in [("HARI INI — 15 APRIL",[0,1,2]),
                                ("BESOK — 16 APRIL",  [3,4]),
                                ("LUSA — 17 APRIL",   [5,6,7])]:
            ctk.CTkLabel(lf, text=date_lbl, font=F_XS,
                         text_color=C["text_light"], fg_color=C["ivory"]).pack(fill="x", padx=10, pady=(6,2))
            for i in idxs:
                px = PASIEN[i % len(PASIEN)]
                rw = ctk.CTkFrame(lf, fg_color="transparent")
                rw.pack(fill="x", padx=10, pady=2)
                tb2 = ctk.CTkFrame(rw, fg_color=C["dark_green"], width=44, height=44, corner_radius=8)
                tb2.pack(side="left", padx=(0,10)); tb2.pack_propagate(False)
                ctk.CTkLabel(tb2, text=px["kontrol"] if px["kontrol"]!="-" else "09:00",
                             font=F_XS, text_color="white").place(relx=.5, rely=.5, anchor="center")
                inf = ctk.CTkFrame(rw, fg_color="transparent")
                inf.pack(side="left", fill="x", expand=True)
                ctk.CTkLabel(inf, text=px["nama"], font=("Helvetica",11,"bold"),
                             text_color=C["text_dark"]).pack(anchor="w")
                ctk.CTkLabel(inf, text=f"{px['id']} · {px['fase']}",
                             font=F_XS, text_color=C["text_light"]).pack(anchor="w")
                sc = C["sput_grn"] if px["status"]=="Dalam Terapi" else C["blood"]
                ctk.CTkLabel(rw, text=px["status"], fg_color=sc, text_color="white",
                             corner_radius=8, font=F_XS, width=80).pack(side="right", padx=8)
                sep_line(lf, padx=10)

        rf = ctk.CTkFrame(two, fg_color="transparent")
        rf.grid(row=0, column=1, sticky="nsew")
        for lbl, val, clr in [("Total Hari Ini","5 Pasien",C["dark_green"]),
                               ("Menunggu","3 Pasien",C["sput_yel"]),
                               ("Tidak Hadir","2 Pasien",C["blood"])]:
            fc = ctk.CTkFrame(rf, fg_color=C["card"], corner_radius=10,
                              border_width=1, border_color=C["border"])
            fc.pack(fill="x", pady=4)
            tk.Frame(fc, bg=clr, height=3).pack(fill="x")
            ctk.CTkLabel(fc, text=lbl, font=F_SM,
                         text_color=C["text_light"]).pack(anchor="w", padx=12, pady=(6,0))
            ctk.CTkLabel(fc, text=val, font=("Helvetica",18,"bold"),
                         text_color=C["text_dark"]).pack(anchor="w", padx=12, pady=(0,8))

    # ═════════════════════════════════════════════════════════════════════════
    # ANTRIAN PASIEN
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_antrian(self):
        p = self._scroll; self._tree_style()
        hdr = ctk.CTkFrame(p, fg_color="transparent")
        hdr.pack(fill="x", padx=20, pady=(18,10))
        ctk.CTkLabel(hdr, text="Manajemen Antrian Pasien",
                     font=F_TITLE, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(hdr, text="+ Daftarkan Antrian", fg_color=C["antrian"],
                      hover_color="#3d6a8a", font=F_BODY,
                      command=self._dlg_antrian_baru).pack(side="right")

        now_fr = ctk.CTkFrame(p, fg_color=C["dark_green"], corner_radius=14)
        now_fr.pack(fill="x", padx=20, pady=(0,14))
        ctk.CTkLabel(now_fr, text="Sedang Dilayani",
                     font=F_SM, text_color="#a8c4b0").pack(pady=(14,0))
        ctk.CTkLabel(now_fr, text="A-001",
                     font=("Helvetica",42,"bold"), text_color="white").pack()
        ctk.CTkLabel(now_fr, text="Siti Aminah  —  Evaluasi Hemoptisis  |  08:00",
                     font=F_BODY, text_color="#c8e0d0").pack(pady=(0,14))

        act_fr = ctk.CTkFrame(p, fg_color="transparent")
        act_fr.pack(fill="x", padx=20, pady=(0,12))
        for lbl, clr in [("Panggil Berikutnya",C["dark_green"]),
                          ("Selesai & Tutup",   C["sput_grn"]),
                          ("Tunda Antrian",      C["sput_yel"]),
                          ("Reset Antrian",      C["blood"])]:
            ctk.CTkButton(act_fr, text=lbl, fg_color=clr, hover_color=C["text_dark"],
                          font=F_BODY, width=185,
                          command=lambda l=lbl: messagebox.showinfo("Antrian", l)).pack(side="left", padx=4)

        sr = ctk.CTkFrame(p, fg_color="transparent")
        sr.pack(fill="x", padx=20, pady=(0,12))
        for i in range(4): sr.grid_columnconfigure(i, weight=1)
        for col,(lbl,val,sub,clr) in enumerate([
            ("Total Antrian","12","Terdaftar hari ini",C["antrian"]),
            ("Sudah Dilayani","1","Selesai",C["sput_grn"]),
            ("Menunggu","4","Dalam antrean",C["sput_yel"]),
            ("Rata-rata Tunggu","18 mnt","Per pasien",C["terracotta"]),
        ]):
            fc = ctk.CTkFrame(sr, fg_color=C["card"], corner_radius=12,
                              border_width=1, border_color=C["border"])
            fc.grid(row=0, column=col, sticky="nsew", padx=4)
            tk.Frame(fc, bg=clr, height=3).pack(fill="x")
            ctk.CTkLabel(fc, text=lbl.upper(), font=F_XS,
                         text_color=C["text_light"]).pack(anchor="w", padx=12, pady=(8,2))
            ctk.CTkLabel(fc, text=val, font=("Helvetica",22,"bold"),
                         text_color=C["text_dark"]).pack(anchor="w", padx=12)
            ctk.CTkLabel(fc, text=sub, font=F_XS,
                         text_color=clr).pack(anchor="w", padx=12, pady=(0,8))

        ctk.CTkLabel(p, text="Daftar Antrian Aktif",
                     font=F_SUB, text_color=C["text_dark"]).pack(anchor="w", padx=20, pady=(4,6))
        cols = ("No. Antrian","Nama Pasien","Pukul","Keperluan","Prioritas","Status")
        tf = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        tf.pack(fill="both", padx=20, pady=(0,20), expand=True)
        tree = ttk.Treeview(tf, columns=cols, show="headings",
                            style="TB.Treeview", height=8)
        for col, w in zip(cols, [90,160,70,220,90,110]):
            tree.heading(col, text=col); tree.column(col, width=w, anchor="center")
        for a in ANTRIAN:
            tag = "urgent" if a["prio"]=="URGENT" else ("tinggi" if a["prio"]=="Tinggi" else "")
            tree.insert("","end", values=(a["no"],a["nama"],a["pukul"],
                                          a["keperluan"],a["prio"],a["status"]), tags=(tag,))
        tree.tag_configure("urgent", foreground=C["blood"])
        tree.tag_configure("tinggi", foreground=C["terracotta"])
        tree.pack(fill="both", expand=True, padx=2, pady=2)

    def _dlg_antrian_baru(self):
        dlg = ctk.CTkToplevel(self); dlg.title("Daftarkan Antrian Baru")
        dlg.geometry("420x360"); dlg.grab_set()
        ctk.CTkLabel(dlg, text="Form Pendaftaran Antrian",
                     font=F_TITLE, text_color=C["text_dark"]).pack(pady=(18,10))
        for lbl, default in [("Nama / ID Pasien",""),("Keperluan",""),
                              ("Prioritas","Normal"),("Pukul Kedatangan","")]:
            fr = ctk.CTkFrame(dlg, fg_color="transparent")
            fr.pack(fill="x", padx=24, pady=5)
            ctk.CTkLabel(fr, text=lbl, font=F_BODY, width=150,
                         text_color=C["text_mid"]).pack(side="left")
            e = ctk.CTkEntry(fr, font=F_BODY)
            if default: e.insert(0, default)
            e.pack(side="left", fill="x", expand=True)
        ctk.CTkButton(dlg, text="Tambahkan ke Antrian",
                      fg_color=C["antrian"], hover_color="#3d6a8a", font=F_BODY,
                      command=lambda:(messagebox.showinfo("Berhasil","Pasien ditambahkan ke antrian!"),
                                      dlg.destroy())).pack(pady=16)

    # ═════════════════════════════════════════════════════════════════════════
    # PERINGATAN DINI
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_peringatan(self):
        p = self._scroll
        ctk.CTkLabel(p, text="Peringatan Dini & Tindak Lanjut",
                     font=F_TITLE, text_color=C["text_dark"]).pack(anchor="w", padx=20, pady=(18,4))
        fp = ctk.CTkFrame(p, fg_color="transparent")
        fp.pack(fill="x", padx=20, pady=(0,10))
        for lbl in ["Semua","Kritis","Tinggi","Sedang","Rendah"]:
            ctk.CTkButton(fp, text=lbl, width=90, height=28,
                          fg_color=C["dark_green"] if lbl=="Semua" else C["ivory"],
                          text_color="white" if lbl=="Semua" else C["text_dark"],
                          hover_color=C["sage"], font=F_SM,
                          border_width=1, border_color=C["border"]).pack(side="left", padx=4)
        for pw in PERINGATAN:
            clr = RISIKO_CLR.get(pw["level"], C["sage"])
            card = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                                border_width=1, border_color=clr)
            card.pack(fill="x", padx=20, pady=4)
            top = ctk.CTkFrame(card, fg_color="transparent")
            top.pack(fill="x", padx=14, pady=(10,4))
            ctk.CTkLabel(top, text=pw["level"], fg_color=clr, text_color="white",
                         corner_radius=8, font=F_XS, width=70).pack(side="left")
            ctk.CTkLabel(top, text=pw["nama"], font=("Helvetica",12,"bold"),
                         text_color=C["text_dark"]).pack(side="left", padx=10)
            ctk.CTkLabel(top, text=pw["id"], font=F_XS,
                         text_color=C["text_light"]).pack(side="left")
            today_str = datetime.date.today().strftime("%d/%m/%Y")
            ctk.CTkLabel(top, text=today_str, font=F_XS,
                         text_color=C["text_light"]).pack(side="right")
            ctk.CTkLabel(card, text=f"  {pw['isu']}", font=F_BODY,
                         text_color=C["text_mid"]).pack(anchor="w", padx=14, pady=(0,6))
            bf = ctk.CTkFrame(card, fg_color="transparent")
            bf.pack(fill="x", padx=14, pady=(0,10))
            ctk.CTkButton(bf, text=pw["aksi"], fg_color=clr, hover_color=C["text_dark"],
                          font=F_SM, height=28, width=140,
                          command=lambda a=pw["aksi"]: messagebox.showinfo("Aksi", a)).pack(side="left", padx=(0,8))
            ctk.CTkButton(bf, text="Lihat Detail", fg_color="transparent",
                          text_color=C["evergreen"], hover_color=C["ivory"],
                          font=F_SM, height=28, border_width=1,
                          border_color=C["evergreen"]).pack(side="left")

    # ═════════════════════════════════════════════════════════════════════════
    # LAB & DIAGNOSTIK
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_lab(self):
        p = self._scroll; self._tree_style()
        hdr = ctk.CTkFrame(p, fg_color="transparent")
        hdr.pack(fill="x", padx=20, pady=(18,10))
        ctk.CTkLabel(hdr, text="Lab & Diagnostik",
                     font=F_TITLE, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(hdr, text="+ Input Hasil Lab", fg_color=C["dark_green"],
                      hover_color=C["evergreen"], font=F_BODY,
                      command=lambda: messagebox.showinfo("Lab","Form input hasil lab")).pack(side="right")
        cols = ("ID Pasien","Nama","Jenis Pemeriksaan","Hasil","Tanggal","Status")
        tf = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        tf.pack(fill="both", padx=20, pady=(0,20), expand=True)
        tree = ttk.Treeview(tf, columns=cols, show="headings",
                            style="TB.Treeview", height=14)
        for col, w in zip(cols, [100,140,160,220,100,90]):
            tree.heading(col, text=col); tree.column(col, width=w, anchor="center")
        tags = {"Kritis":"kritis_l","MDR":"mdr_l","Abnormal":"abn_l",
                "Positif":"pos_l","Rendah":"rend_l","Normal":""}
        for ld in LAB:
            tree.insert("","end", values=(ld["id"],ld["nama"],ld["jenis"],
                                           ld["hasil"],ld["tgl"],ld["status"]),
                        tags=(tags.get(ld["status"],""),))
        tree.tag_configure("kritis_l", foreground=C["blood"])
        tree.tag_configure("mdr_l",    foreground="#7a0000")
        tree.tag_configure("abn_l",    foreground=C["sput_yel"])
        tree.tag_configure("pos_l",    foreground=C["terracotta"])
        tree.tag_configure("rend_l",   foreground=C["sput_yel"])
        tree.pack(fill="both", expand=True, padx=2, pady=2)

    # ═════════════════════════════════════════════════════════════════════════
    # ═════════════════════════════════════════════════════════════════════════
    # LAPORAN BULANAN
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_laporan(self):
        p = self._scroll; self._tree_style()
        hdr = ctk.CTkFrame(p, fg_color="transparent")
        hdr.pack(fill="x", padx=20, pady=(18,10))
        ctk.CTkLabel(hdr, text="Laporan Bulanan — April 2026",
                     font=F_TITLE, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(hdr, text="Cetak / Ekspor PDF", fg_color=C["dark_green"],
                      hover_color=C["evergreen"], font=F_BODY,
                      command=lambda: messagebox.showinfo("Ekspor","Laporan diekspor ke PDF")).pack(side="right")
        sr = ctk.CTkFrame(p, fg_color="transparent")
        sr.pack(fill="x", padx=20, pady=(0,12))
        sr.grid_columnconfigure(0, weight=1); sr.grid_columnconfigure(1, weight=1)
        for col,(lbl,val,sub,clr) in enumerate([
            ("Pasien Baru Terdaftar","14","Periode April 2026",C["terracotta"]),
            ("Tingkat Keberhasilan","87%","Target: >=90%",C["sput_grn"]),
        ]):
            fc = ctk.CTkFrame(sr, fg_color=C["card"], corner_radius=12,
                              border_width=1, border_color=C["border"])
            fc.grid(row=0, column=col, sticky="nsew", padx=5)
            tk.Frame(fc, bg=clr, height=3).pack(fill="x")
            ctk.CTkLabel(fc, text=lbl, font=F_SM,
                         text_color=C["text_light"]).pack(anchor="w", padx=14, pady=(8,2))
            ctk.CTkLabel(fc, text=val, font=("Helvetica",28,"bold"),
                         text_color=C["text_dark"]).pack(anchor="w", padx=14)
            ctk.CTkLabel(fc, text=sub, font=F_XS,
                         text_color=clr).pack(anchor="w", padx=14, pady=(0,10))
        cols = ("Indikator","Target","Bulan Lalu","Bulan Ini","Pencapaian","Status")
        tf = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        tf.pack(fill="both", padx=20, pady=(0,20), expand=True)
        tree = ttk.Treeview(tf, columns=cols, show="headings",
                            style="TB.Treeview", height=10)
        for col, w in zip(cols, [230,80,80,80,90,120]):
            tree.heading(col, text=col)
            tree.column(col, width=w, anchor="w" if col=="Indikator" else "center")
        for row in LAPORAN_ROWS:
            tag = "tercapai" if row[-1]=="Tercapai" else ("perlu" if row[-1]=="Perlu Perbaikan" else "")
            tree.insert("","end", values=row, tags=(tag,))
        tree.tag_configure("tercapai", foreground=C["sput_grn"])
        tree.tag_configure("perlu",    foreground=C["blood"])
        tree.pack(fill="both", expand=True, padx=2, pady=2)

    # ═════════════════════════════════════════════════════════════════════════
    # EDUKASI PASIEN
    # ═════════════════════════════════════════════════════════════════════════
    def _pg_edukasi(self):
        p = self._scroll
        hdr = ctk.CTkFrame(p, fg_color="transparent")
        hdr.pack(fill="x", padx=20, pady=(18,10))
        ctk.CTkLabel(hdr, text="Konten Edukasi Pasien TBC",
                     font=F_TITLE, text_color=C["text_dark"]).pack(side="left")
        ctk.CTkButton(hdr, text="+ Tambah Konten", fg_color=C["dark_green"],
                      hover_color=C["evergreen"], font=F_BODY,
                      command=lambda: messagebox.showinfo("Edukasi","Form tambah konten")).pack(side="right")
        fp = ctk.CTkFrame(p, fg_color="transparent")
        fp.pack(fill="x", padx=20, pady=(0,12))
        for lbl in ["Semua","Pengenalan TBC","Pengobatan","Pencegahan","Nutrisi","Kepatuhan"]:
            ctk.CTkButton(fp, text=lbl, width=100, height=28,
                          fg_color=C["dark_green"] if lbl=="Semua" else C["ivory"],
                          text_color="white" if lbl=="Semua" else C["text_dark"],
                          hover_color=C["sage"], font=F_SM,
                          border_width=1, border_color=C["border"]).pack(side="left", padx=4)
        gf = ctk.CTkFrame(p, fg_color="transparent")
        gf.pack(fill="both", padx=20, pady=(0,20), expand=True)
        kat_clr = {"Pengenalan TBC":C["dark_green"],"Pengobatan":C["terracotta"],
                   "Pencegahan":C["sput_grn"],"Nutrisi":C["sput_yel"],
                   "Kepatuhan":C["antrian"]}
        icons = ["📖","💊","🏠","🥗","⚗️","⏰"]
        for i in range(3): gf.grid_columnconfigure(i, weight=1)
        for i, edu in enumerate(EDUKASI):
            col = i % 3; row = i // 3
            clr = kat_clr.get(edu["kat"], C["sage"])
            card = ctk.CTkFrame(gf, fg_color=C["card"], corner_radius=12,
                                border_width=1, border_color=C["border"])
            card.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
            ib2 = ctk.CTkFrame(card, fg_color=clr, width=44, height=44, corner_radius=8)
            ib2.pack(anchor="w", padx=14, pady=(12,6)); ib2.pack_propagate(False)
            ctk.CTkLabel(ib2, text=icons[i], font=("Segoe UI Emoji",20)).place(relx=.5, rely=.5, anchor="center")
            ctk.CTkLabel(card, text=edu["kat"].upper(), font=F_XS,
                         text_color=clr).pack(anchor="w", padx=14)
            ctk.CTkLabel(card, text=edu["judul"], font=("Helvetica",11,"bold"),
                         text_color=C["text_dark"], wraplength=180).pack(anchor="w", padx=14, pady=4)
            ctk.CTkLabel(card, text=f"  {edu['dur']}     {edu['views']} dilihat",
                         font=F_XS, text_color=C["text_light"]).pack(anchor="w", padx=14, pady=(0,8))
            ctk.CTkButton(card, text="Buka Materi", fg_color="transparent",
                          text_color=clr, hover_color=C["ivory"],
                          font=F_SM, height=26, anchor="w",
                          command=lambda j=edu["judul"]: messagebox.showinfo("Edukasi", j)).pack(anchor="w", padx=10, pady=(0,10))


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = TBCareApp()
    app.mainloop()