from data import GAME, ROLE, anggota
import tampilan
import validasi


def konfirmasi(pesan):
    while True:
        jawab = input(pesan + " (y/t): ").strip().lower()
        if jawab in ("y", "t"):
            return jawab == "y"
        print("Input tidak valid! Masukkan y atau t.")


def minta_daftar_game():
    daftar_game = {}
    while True:
        sisa = [g for g in GAME if g not in daftar_game]
        if len(sisa) == 0:
            print("Semua game sudah dipilih.")
            break
        game = validasi.pilih_game(sisa)
        daftar_game[game] = validasi.pilih_role(game)
        while True:
            lagi = input("Tambah game lain? (y/n): ").strip().lower()
            if lagi in ("y", "n"):
                break
            print("Input tidak valid! Masukkan y atau n.")
        if lagi != "y":
            break
    return daftar_game


def kelola_game_anggota(data):
    while True:
        print("\nGame saat ini:", tampilan.format_game(data["game"]))
        aksi = validasi.pilih_dari_daftar("Kelola game anggota",
                                          ("Tambah game", "Ubah role di game", "Hapus game", "Selesai"))
        if aksi == "Tambah game":
            sisa = [g for g in GAME if g not in data["game"]]
            if len(sisa) == 0:
                print("Semua game sudah terdaftar.")
            else:
                game = validasi.pilih_game(sisa)
                data["game"][game] = validasi.pilih_role(game)
        elif aksi == "Ubah role di game":
            game = validasi.pilih_game(list(data["game"]))
            data["game"][game] = validasi.pilih_role(game)
        elif aksi == "Hapus game":
            if len(data["game"]) == 1:
                print("Minimal harus ada 1 game.")
            else:
                game = validasi.pilih_game(list(data["game"]))
                data["game"].pop(game)
        else:
            break


def tambah_anggota():
    print("\n--- TAMBAH ANGGOTA ---")
    nama_baru = validasi.minta_nama_baru()
    game_baru = minta_daftar_game()
    while True:
        jadwal_baru = input("Kapan bisa main? (contoh: Senin): ").strip()
        if jadwal_baru == "":
            print("Jadwal tidak boleh kosong!")
        else:
            break
    anggota[nama_baru] = {"game": game_baru, "jadwal": jadwal_baru}
    print("Anggota berhasil ditambahkan!")


def lihat_anggota():
    print("\n--- DAFTAR SEMUA ANGGOTA ---")
    tampilan.tampilkan_anggota(anggota)


def cari_anggota():
    print("\n--- CARI ANGGOTA BERDASARKAN GAME DAN ROLE ---")
    game_dicari = validasi.pilih_game()
    role_dicari = validasi.pilih_role(game_dicari)
    hasil = {}
    for nama, info in anggota.items():
        if info["game"].get(game_dicari) == role_dicari:
            hasil[nama] = info
    print("\nAnggota", game_dicari, "dengan role", role_dicari + ":")
    tampilan.tampilkan_anggota(hasil)


def ubah_anggota():
    print("\n--- UBAH DATA ANGGOTA ---")
    if len(anggota) == 0:
        print("Belum ada anggota.")
        return
    nama = validasi.pilih_anggota()
    if nama is None:
        print("Dibatalkan.")
        return
    data = anggota[nama]
    print("Kosongkan (Enter) jika tidak ingin mengubah bagian itu.")
    nama_baru = input("Nama baru: ").strip()
    while True:
        kelola = input("Kelola game & role? (y/t): ").strip().lower()
        if kelola in ("y", "t"):
            break
        print("Input tidak valid! Masukkan y atau t.")
    if kelola == "y":
        kelola_game_anggota(data)
    jadwal_baru = input("Jadwal baru: ").strip()

    if jadwal_baru != "":
        data["jadwal"] = jadwal_baru
    if nama_baru != "" and nama_baru != nama:
        if nama_baru in anggota:
            print("Nama baru sudah dipakai, nama tidak diubah.")
        else:
            anggota[nama_baru] = anggota.pop(nama)
    print("Data anggota berhasil diubah!")


def hapus_anggota():
    print("\n--- HAPUS ANGGOTA ---")
    if len(anggota) == 0:
        print("Belum ada anggota.")
        return
    nama = validasi.pilih_anggota()
    if nama is None:
        print("Dibatalkan.")
        return
    if not konfirmasi("Yakin hapus anggota " + nama + "?"):
        print("Penghapusan dibatalkan.")
        return
    anggota.pop(nama)
    print("Anggota", nama, "berhasil dihapus.")


# ---------- KELOLA GAME DAN ROLE (khusus admin) ----------


def tambah_game():
    print("\n--- TAMBAH GAME ---")
    while True:
        game_baru = input("Nama game baru: ").strip()
        if game_baru == "":
            print("Nama game tidak boleh kosong!")
        elif any(game.lower() == game_baru.lower() for game in GAME):
            print("Game sudah ada!")
        else:
            break
    while True:
        role_pertama = input("Role pertama untuk game ini: ").strip()
        if role_pertama == "":
            print("Role pertama tidak boleh kosong!")
        else:
            break
    GAME.append(game_baru)
    ROLE[game_baru] = [role_pertama]
    print("Game", game_baru, "berhasil ditambahkan.")


def hapus_game():
    print("\n--- HAPUS GAME ---")
    if len(GAME) <= 1:
        print("Minimal harus ada 1 game.")
        return
    game_dihapus = validasi.pilih_game()
    pemakai = [nama for nama, info in anggota.items() if game_dihapus in info["game"]]
    if len(pemakai) > 0:
        print("Game tidak bisa dihapus, masih dipakai oleh: " + ", ".join(pemakai))
        return
    if not konfirmasi("Yakin hapus game " + game_dihapus + "?"):
        print("Penghapusan dibatalkan.")
        return
    GAME.remove(game_dihapus)
    ROLE.pop(game_dihapus)
    print("Game", game_dihapus, "berhasil dihapus.")


def ubah_game():
    print("\n--- UBAH GAME ---")
    game_lama = validasi.pilih_game()
    while True:
        game_baru = input("Nama game baru: ").strip()
        if game_baru == "":
            print("Nama game tidak boleh kosong!")
        elif any(g.lower() == game_baru.lower() for g in GAME if g != game_lama):
            print("Nama game sudah dipakai!")
        else:
            break
    GAME[GAME.index(game_lama)] = game_baru
    ROLE[game_baru] = ROLE.pop(game_lama)
    for info in anggota.values():
        if game_lama in info["game"]:
            info["game"][game_baru] = info["game"].pop(game_lama)
    print("Game", game_lama, "berhasil diubah menjadi", game_baru + ".")


def lihat_role():
    print("\n--- DAFTAR GAME DAN ROLE ---")
    tampilan.tampilkan_role(ROLE)


def tambah_role():
    print("\n--- TAMBAH ROLE ---")
    game = validasi.pilih_game()
    while True:
        role_baru = input("Nama role baru: ").strip()
        if role_baru == "":
            print("Nama role tidak boleh kosong!")
        elif any(role.lower() == role_baru.lower() for role in ROLE[game]):
            print("Role sudah ada di " + game + "!")
        else:
            break
    ROLE[game].append(role_baru)
    print("Role", role_baru, "berhasil ditambahkan ke", game + ".")


def hapus_role():
    print("\n--- HAPUS ROLE ---")
    game = validasi.pilih_game()
    if len(ROLE[game]) <= 1:
        print("Minimal harus ada 1 role di setiap game.")
        return
    role_dihapus = validasi.pilih_role(game)
    pemakai = [nama for nama, info in anggota.items() if info["game"].get(game) == role_dihapus]
    if len(pemakai) > 0:
        print("Role tidak bisa dihapus, masih dipakai oleh: " + ", ".join(pemakai))
        return
    if not konfirmasi("Yakin hapus role " + role_dihapus + " dari " + game + "?"):
        print("Penghapusan dibatalkan.")
        return
    ROLE[game].remove(role_dihapus)
    print("Role", role_dihapus, "berhasil dihapus dari", game + ".")


def ubah_role():
    print("\n--- UBAH ROLE ---")
    game = validasi.pilih_game()
    role_lama = validasi.pilih_role(game)
    while True:
        role_baru = input("Nama role baru: ").strip()
        if role_baru == "":
            print("Nama role tidak boleh kosong!")
        elif any(r.lower() == role_baru.lower() for r in ROLE[game] if r != role_lama):
            print("Nama role sudah dipakai di " + game + "!")
        else:
            break
    ROLE[game][ROLE[game].index(role_lama)] = role_baru
    for info in anggota.values():
        if info["game"].get(game) == role_lama:
            info["game"][game] = role_baru
    print("Role", role_lama, "berhasil diubah menjadi", role_baru + ".")


def menu_role():
    while True:
        tampilan.tampilkan_judul("KELOLA GAME DAN ROLE")
        aksi = validasi.pilih_dari_daftar(
            "Pilih menu",
            ("Lihat game dan role", "Tambah game", "Hapus game", "Ubah game",
             "Tambah role", "Hapus role", "Ubah role", "Kembali"))
        if aksi == "Lihat game dan role":
            lihat_role()
        elif aksi == "Tambah game":
            tambah_game()
        elif aksi == "Hapus game":
            hapus_game()
        elif aksi == "Ubah game":
            ubah_game()
        elif aksi == "Tambah role":
            tambah_role()
        elif aksi == "Hapus role":
            hapus_role()
        elif aksi == "Ubah role":
            ubah_role()
        else:
            break
