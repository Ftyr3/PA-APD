import inquirer
from data import GAME, ROLE, anggota


def pilih_dari_daftar(pesan, daftar):
    pertanyaan = [inquirer.List("pilihan", message=pesan, choices=list(daftar))]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["pilihan"]


def pilih_game(daftar=None):
    if daftar is None:
        daftar = GAME
    return pilih_dari_daftar("Pilih game", daftar)


def pilih_role(game):
    return pilih_dari_daftar("Pilih role untuk " + game, ROLE[game])


def pilih_anggota():
    daftar = list(anggota.keys()) + ["Batal"]
    pilihan = pilih_dari_daftar("Pilih anggota", daftar)
    if pilihan == "Batal":
        return None
    return pilihan


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
