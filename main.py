import auth
import crud
import statistik
import tampilan
import validasi
from data import MENU_ADMIN, MENU_USER


while True:
    try:
        if auth.level_aktif == "":
            tampilan.tampilkan_judul("SISTEM PENGELOLAAN ANGGOTA DAN JADWAL MABAR TIM")
            aksi = validasi.pilih_dari_daftar("Pilih menu", ("Login", "Register", "Keluar"))

            if aksi == "Login":
                auth.login()
            elif aksi == "Register":
                auth.register()
            else:
                print("Terima kasih, sampai jumpa!")
                break

        else:
            if auth.level_aktif == "admin":
                daftar_menu = MENU_ADMIN
            else:
                daftar_menu = MENU_USER

            tampilan.tampilkan_judul("MENU " + auth.level_aktif.upper() + " | Login sebagai: " + auth.pengguna_aktif)
            aksi = validasi.pilih_dari_daftar("Pilih menu", daftar_menu)

            if aksi == "Tambah anggota":
                crud.tambah_anggota()
            elif aksi == "Lihat semua anggota":
                crud.lihat_anggota()
            elif aksi == "Cari anggota berdasarkan game dan role":
                crud.cari_anggota()
            elif aksi == "Ubah data anggota":
                crud.ubah_anggota()
            elif aksi == "Hapus anggota":
                crud.hapus_anggota()
            elif aksi == "Kelola game dan role":
                crud.menu_role()
            elif aksi == "Jumlah anggota per role":
                statistik.lihat_statistik()
            else:
                auth.logout()
    except KeyboardInterrupt:
        print("\nKembali ke menu.")
