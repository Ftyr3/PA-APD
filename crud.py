from data import GAME, ROLE, anggota
import tampilan
import validasi


def minta_daftar_game():
    daftar_game = {}
    while True:
        sisa = [g for g in GAME if g not in daftar_game]
        game = validasi.pilih_game(sisa)
        daftar_game[game] = validasi.pilih_role(game)
        if len(daftar_game) == len(GAME):
            print("Semua game sudah dipilih.")
            break
        lagi = input("Tambah game lain? (y/t): ").strip().lower()
        if lagi != "y":
            break
    return daftar_game


def kelola_game_anggota(data):
    while True:
        print("\nGame saat ini:", tampilan.format_game(data["game"]))
        tampilan.tampilkan_menu(("Tambah game", "Ubah role di game", "Hapus game", "Selesai"))
        pilih = validasi.minta_angka("Pilih: ", 4)
        if pilih == 1:
            sisa = [g for g in GAME if g not in data["game"]]
            if len(sisa) == 0:
                print("Semua game sudah terdaftar.")
            else:
                game = validasi.pilih_game(sisa)
                data["game"][game] = validasi.pilih_role(game)
        elif pilih == 2:
            game = validasi.pilih_game(list(data["game"]))
            data["game"][game] = validasi.pilih_role(game)
        elif pilih == 3:
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
    try:
        jadwal_baru = input("Kapan bisa main? (contoh: Senin): ").strip()
        if jadwal_baru == "":
            raise ValueError("Jadwal tidak boleh kosong!")
    except ValueError as pesan_error:
        print(pesan_error, "Data tidak disimpan.")
    else:
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
    try:
        if len(anggota) == 0:
            raise ValueError("Belum ada anggota.")
        tampilan.tampilkan_anggota(anggota)
        nama = input("Ketik nama anggota yang diubah: ").strip()
        data = anggota[nama]
    except ValueError as pesan_error:
        print(pesan_error)
    except KeyError:
        print("Anggota tidak ditemukan.")
    else:
        print("Kosongkan (Enter) jika tidak ingin mengubah bagian itu.")
        nama_baru = input("Nama baru: ").strip()
        kelola = input("Kelola game & role? (y/t): ").strip().lower()
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
    finally:
        print("-" * 50)


def hapus_anggota():
    print("\n--- HAPUS ANGGOTA ---")
    try:
        if len(anggota) == 0:
            raise ValueError("Belum ada anggota.")
        tampilan.tampilkan_anggota(anggota)
        nama = input("Ketik nama anggota yang dihapus: ").strip()
        anggota.pop(nama)
    except ValueError as pesan_error:
        print(pesan_error)
    except KeyError:
        print("Anggota tidak ditemukan.")
    else:
        print("Anggota", nama, "berhasil dihapus.")
    finally:
        print("-" * 50)


# ---------- KELOLA GAME DAN ROLE (khusus admin) ----------


def tambah_game():
    print("\n--- TAMBAH GAME ---")
    try:
        game_baru = input("Nama game baru: ").strip()
        if game_baru == "":
            raise ValueError("Nama game tidak boleh kosong!")
        for game in GAME:
            if game.lower() == game_baru.lower():
                raise ValueError("Game sudah ada!")
        role_pertama = input("Role pertama untuk game ini: ").strip()
        if role_pertama == "":
            raise ValueError("Role pertama tidak boleh kosong!")
    except ValueError as pesan_error:
        print(pesan_error, "Game tidak ditambahkan.")
    else:
        GAME.append(game_baru)
        ROLE[game_baru] = [role_pertama]
        print("Game", game_baru, "berhasil ditambahkan.")


def hapus_game():
    print("\n--- HAPUS GAME ---")
    try:
        if len(GAME) <= 1:
            raise ValueError("Minimal harus ada 1 game.")
        game_dihapus = validasi.pilih_game()
        pemakai = []
        for nama, info in anggota.items():
            if game_dihapus in info["game"]:
                pemakai.append(nama)
        if len(pemakai) > 0:
            raise ValueError("Game tidak bisa dihapus, masih dipakai oleh: " + ", ".join(pemakai))
    except ValueError as pesan_error:
        print(pesan_error)
    else:
        GAME.remove(game_dihapus)
        ROLE.pop(game_dihapus)
        print("Game", game_dihapus, "berhasil dihapus.")


def lihat_role():
    print("\n--- DAFTAR GAME DAN ROLE ---")
    tampilan.tampilkan_role(ROLE)


def tambah_role():
    print("\n--- TAMBAH ROLE ---")
    game = validasi.pilih_game()
    try:
        role_baru = input("Nama role baru: ").strip()
        if role_baru == "":
            raise ValueError("Nama role tidak boleh kosong!")
        for role in ROLE[game]:
            if role.lower() == role_baru.lower():      # "tank" dianggap sama dengan "Tank"
                raise ValueError("Role sudah ada di " + game + "!")
    except ValueError as pesan_error:
        print(pesan_error)
    else:
        ROLE[game].append(role_baru)
        print("Role", role_baru, "berhasil ditambahkan ke", game + ".")


def hapus_role():
    print("\n--- HAPUS ROLE ---")
    game = validasi.pilih_game()
    try:
        if len(ROLE[game]) <= 1:
            raise ValueError("Minimal harus ada 1 role di setiap game.")
        role_dihapus = validasi.pilih_role(game)
        pemakai = []
        for nama, info in anggota.items():
            if info["game"].get(game) == role_dihapus:
                pemakai.append(nama)
        if len(pemakai) > 0:
            raise ValueError("Role tidak bisa dihapus, masih dipakai oleh: " + ", ".join(pemakai))
    except ValueError as pesan_error:
        print(pesan_error)
    else:
        ROLE[game].remove(role_dihapus)
        print("Role", role_dihapus, "berhasil dihapus dari", game + ".")


def menu_role():
    while True:
        tampilan.tampilkan_judul("KELOLA GAME DAN ROLE")
        tampilan.tampilkan_menu(("Lihat game dan role", "Tambah game", "Hapus game",
                                 "Tambah role", "Hapus role", "Kembali"))
        pilih = validasi.minta_angka("Pilih menu: ", 6)
        if pilih == 1:
            lihat_role()
        elif pilih == 2:
            tambah_game()
        elif pilih == 3:
            hapus_game()
        elif pilih == 4:
            tambah_role()
        elif pilih == 5:
            hapus_role()
        else:
            break
