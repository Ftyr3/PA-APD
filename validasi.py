from data import GAME, ROLE, anggota


def minta_angka(pesan, batas):
    while True:
        try:
            angka = int(input(pesan))
            if angka < 1 or angka > batas:
                raise ValueError
        except ValueError:
            print("Input tidak valid! Masukkan angka 1 sampai", batas)
        else:
            return angka


def pilih_game(daftar=GAME):
    print("\nPilihan game:")
    for i in range(len(daftar)):
        print(str(i + 1) + ".", daftar[i])
    nomor = minta_angka("Pilih nomor game: ", len(daftar))
    return daftar[nomor - 1]


def pilih_role(game):
    daftar_role = ROLE[game]                           # list role milik game tsb
    print("\nPilihan role untuk", game + ":")
    for i in range(len(daftar_role)):
        print(str(i + 1) + ".", daftar_role[i])
    nomor = minta_angka("Pilih nomor role: ", len(daftar_role))
    return daftar_role[nomor - 1]


def minta_nama_baru():
    while True:
        try:
            nama = input("Nama anggota: ").strip()
            if nama == "":
                raise ValueError("Nama tidak boleh kosong!")
            if nama in anggota:
                raise ValueError("Nama sudah terdaftar!")
        except ValueError as pesan_error:
            print(pesan_error)
        else:
            return nama