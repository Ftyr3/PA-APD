try:
    from prettytable import PrettyTable
except ImportError:
    print("Library prettytable belum terpasang.")
    print("Jalankan perintah ini di terminal: pip install prettytable")
    raise SystemExit


def tampilkan_judul(teks):
    print()
    print("=" * 50)
    print(teks.center(50))
    print("=" * 50)


def tampilkan_menu(daftar_menu):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    for i in range(len(daftar_menu)):
        tabel.add_row([i + 1, daftar_menu[i]])
    print(tabel)


def format_game(daftar_game):
    teks = []
    for game, role in daftar_game.items():
        teks.append(game + " (" + role + ")")
    return ", ".join(teks)


def tampilkan_anggota(data):
    if len(data) == 0:
        print("Tidak ada data anggota.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama", "Game (Role)", "Kapan bisa main"]
        tabel.align["Nama"] = "l"
        tabel.align["Game (Role)"] = "l"
        tabel.align["Kapan bisa main"] = "l"
        nomor = 1
        for nama, info in data.items():
            tabel.add_row([nomor, nama, format_game(info["game"]), info["jadwal"]])
            nomor += 1
        print(tabel)


def tampilkan_role(data_role):
    tabel = PrettyTable()
    tabel.field_names = ["Game", "Role"]
    tabel.align["Game"] = "l"
    tabel.align["Role"] = "l"
    for game, daftar_role in data_role.items():
        tabel.add_row([game, ", ".join(daftar_role)])
    print(tabel)


def tampilkan_statistik(hasil):
    tabel = PrettyTable()
    tabel.field_names = ["Role", "Jumlah Anggota"]
    tabel.align["Role"] = "l"
    for role, jumlah in hasil.items():
        tabel.add_row([role, jumlah])
    print(tabel)
