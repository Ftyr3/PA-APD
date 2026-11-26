from data import ROLE, anggota
import tampilan
import validasi


def hitung_role(daftar, game_dicari, role_dicari):
    if len(daftar) == 0:
        return 0
    if daftar[0]["game"].get(game_dicari) == role_dicari:
        return 1 + hitung_role(daftar[1:], game_dicari, role_dicari)
    return hitung_role(daftar[1:], game_dicari, role_dicari)


def lihat_statistik():
    print("\n--- JUMLAH ANGGOTA PER ROLE ---")
    game = validasi.pilih_game()
    print("\nStatistik role untuk", game + ":")
    daftar_data = list(anggota.values())
    hasil = {}
    for role in ROLE[game]:
        hasil[role] = hitung_role(daftar_data, game, role)
    tampilan.tampilkan_statistik(hasil)
