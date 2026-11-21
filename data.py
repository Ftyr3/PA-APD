GAME = ["Mobile Legends", "Valorant", "Free Fire", "PUBG Mobile"]

ROLE = {
    "Mobile Legends": ["Roamer", "Exp Laner", "Jungler", "Mid Laner", "Gold Laner"],
    "Valorant": ["Duelist", "Initiator", "Controller", "Sentinel"],
    "Free Fire": ["Rusher", "Sniper", "Supporter", "Flanker"],
    "PUBG Mobile": ["Fragger", "Support", "Scout", "Sniper",],
}

MENU_ADMIN = ("Tambah anggota", "Lihat semua anggota", "Ubah data anggota",
              "Hapus anggota", "Kelola game dan role", "Jumlah anggota per role", "Logout")
MENU_USER = ("Lihat semua anggota", "Cari anggota berdasarkan game dan role",
             "Jumlah anggota per role", "Logout")

anggota = {
    "Cortez/kris": {"game": {"Mobile Legends": "Assassin", "Valorant": "Duelist"},
                    "jadwal": "Kapan aja"},
    "BiburNextDoor": {"game": {"Mobile Legends": "Gold Laner", "PUBG Mobile": "Support"},
                      "jadwal": "Free kalau ga malam"},
    "Ghozali": {"game": {"Mobile Legends": "Exp Laner", "Free Fire": "Rusher"},
                "jadwal": "Sabtu, Minggu"},
    "Psych1cparty": {"game": {"Mobile Legend": "Roamer"}, "jadwal": "Jumat malam"},
}

akun = {
    "admin": {"password": "admin123", "level": "admin"},
    "user": {"password": "user123", "level": "user"},
}
